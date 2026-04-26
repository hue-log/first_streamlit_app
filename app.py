import streamlit as st
import PyPDF2
import openai
import json
import re

# ---------- Page config ----------
st.set_page_config(page_title="PDF → MCQ Quiz", layout="wide")
st.title("📄 PDF to MCQ Quiz with Explanations")
st.markdown("Upload a PDF, generate MCQs, and test your knowledge!")

# ---------- Sidebar: API key ----------
with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input("OpenAI API Key", type="password")
    if api_key:
        openai.api_key = api_key
    num_questions = st.slider("Number of questions", 3, 10, 5)
    st.markdown("---")
    st.markdown("**How it works**")
    st.markdown("""
    1. Upload a PDF  
    2. Text is extracted and split  
    3. OpenAI generates MCQs with explanations  
    4. Select answers and get instant feedback
    """)

# ---------- Session state initialisation ----------
if 'quiz' not in st.session_state:
    st.session_state.quiz = []          # list of question dicts
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}  # question index -> selected answer index
if 'generated' not in st.session_state:
    st.session_state.generated = False

# ---------- Helper: extract text from PDF ----------
def extract_text_from_pdf(uploaded_file):
    """Return full text from an uploaded PDF file."""
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

# ---------- Helper: split text into manageable chunks ----------
def chunk_text(text, max_chars=3000):
    """Split text into chunks of roughly max_chars characters."""
    words = text.split()
    chunks = []
    current_chunk = []
    current_len = 0
    for word in words:
        if current_len + len(word) + 1 > max_chars and current_chunk:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_len = len(word)
        else:
            current_chunk.append(word)
            current_len += len(word) + 1
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

# ---------- Helper: generate MCQs from a text chunk ----------
def generate_mcq_from_chunk(chunk, n):
    """
    Send chunk to OpenAI and return a list of MCQ dicts.
    Each dict: {"question": ..., "options": [...], "correct_index": int, "explanation": ...}
    """
    prompt = f"""
You are an expert quiz creator. From the following text, generate {n} multiple-choice questions.
Each question must have four distinct options (A, B, C, D) and a clear, detailed explanation for the correct answer.
Output ONLY a valid JSON array. Every element must be an object with these keys:
"question", "options" (array of 4 strings), "correct_index" (integer 0-3), "explanation".

Text:
\"\"\"
{chunk}
\"\"\"

JSON array:
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=2000,
        )
        raw = response.choices[0].message.content.strip()
        # Sometimes the response is wrapped in ```json ... ``` – remove that
        if raw.startswith("```"):
            raw = re.sub(r"```(?:json)?", "", raw).strip("`").strip()
        mcq_list = json.loads(raw)
        # Validate the structure
        for item in mcq_list:
            assert "question" in item
            assert "options" in item and len(item["options"]) == 4
            assert "correct_index" in item and isinstance(item["correct_index"], int)
            assert "explanation" in item
        return mcq_list
    except Exception as e:
        st.error(f"Failed to generate MCQs: {e}")
        return []

# ---------- File uploader ----------
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file is not None and api_key:
    if st.button("🚀 Generate MCQs"):
        with st.spinner("Extracting text..."):
            full_text = extract_text_from_pdf(uploaded_file)
        if not full_text.strip():
            st.error("No text found in the PDF. It may be scanned or image-based.")
        else:
            # Split text
            chunks = chunk_text(full_text, max_chars=3000)
            if len(chunks) > 3:
                # Keep only a few chunks to avoid excessive API calls
                chunks = chunks[:3]
            all_mcqs = []
            with st.spinner("Generating questions with OpenAI (this may take a minute)..."):
                # Distribute question budget across chunks
                q_per_chunk = max(1, num_questions // len(chunks))
                for chunk in chunks:
                    mcqs = generate_mcq_from_chunk(chunk, q_per_chunk)
                    all_mcqs.extend(mcqs)
                # Trim to exact number if needed
                all_mcqs = all_mcqs[:num_questions]
            if all_mcqs:
                st.session_state.quiz = all_mcqs
                st.session_state.user_answers = {}
                st.session_state.generated = True
                st.success(f"✅ {len(all_mcqs)} MCQs generated!")
            else:
                st.error("Could not generate any questions. Check your API key or try a different PDF.")
elif not api_key:
    st.info("Please enter your OpenAI API key in the sidebar.")

# ---------- Display quiz ----------
if st.session_state.generated and st.session_state.quiz:
    st.markdown("---")
    st.subheader("📝 Quiz")
    
    # Let the user answer each question (radio buttons)
    for idx, q in enumerate(st.session_state.quiz):
        st.markdown(f"**Q{idx+1}.** {q['question']}")
        # Radio buttons return the option string, we want the index
        options = q["options"]
        choice = st.radio(
            f"Select answer for Q{idx+1}",
            options,
            format_func=lambda x: x,
            key=f"q_{idx}",
            index=None,  # no default selection
        )
        if choice is not None:
            st.session_state.user_answers[idx] = options.index(choice)
        st.markdown("---")

    # Submit button for checking all answers
    if st.button("✅ Check Answers"):
        if len(st.session_state.user_answers) != len(st.session_state.quiz):
            st.warning("Please answer all questions before checking.")
        else:
            correct_count = 0
            for idx, q in enumerate(st.session_state.quiz):
                user_ans = st.session_state.user_answers[idx]
                correct_ans = q["correct_index"]
                is_correct = (user_ans == correct_ans)
                if is_correct:
                    correct_count += 1
                
                # Display result for each question
                with st.expander(f"Q{idx+1} {'✅' if is_correct else '❌'} {q['question']}"):
                    st.markdown("**Your answer:** " + ("✅" if is_correct else "❌") + f" {q['options'][user_ans]}")
                    if not is_correct:
                        st.markdown("**Correct answer:** " + q['options'][correct_ans])
                    st.markdown("**Explanation:** " + q["explanation"])

            # Overall score
            st.success(f"🎯 Your score: {correct_count}/{len(st.session_state.quiz)}")
            st.balloons()
