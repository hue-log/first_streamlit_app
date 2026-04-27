import streamlit as st
import random

# ========== FULL QUESTION BANK (replace with complete list) ==========
# Keep the structure exactly as below. I'll send the full list in a separate message.
QUESTIONS = [
    # Example questions – replace with the full set
    {
        "domain": "Domain 1 – The Audit Process",
        "question": "The IT Assurance Framework consists of all of the following except:",
        "options": [
            "ISACA Code of Professional Ethics",
            "IS audit and assurance standards",
            "ISACA Audit Job Practice",
            "IS audit and assurance guidelines"
        ],
        "answer": "C",
        "explanation": "The IT Assurance Framework includes ISACA Code of Professional Ethics, IS audit and assurance standards, guidelines, and tools/techniques. It does not contain the ISACA Audit Job Practice."
    },
    # ... add ALL questions from the PDFs here ...
]

# ========== STREAMLIT APP LOGIC (options shuffle only on new question) ==========
st.set_page_config(page_title="CISA Full Practice Exam", layout="wide")

# Session state init
if "questions" not in st.session_state:
    st.session_state.questions = QUESTIONS.copy()
    random.shuffle(st.session_state.questions)
if "idx" not in st.session_state:
    st.session_state.idx = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "selected_idx" not in st.session_state:
    st.session_state.selected_idx = None
if "shuffled_data" not in st.session_state:
    st.session_state.shuffled_data = None   # will hold [(text, is_correct), ...] for current Q

# Sidebar filters
domains = sorted({q["domain"] for q in QUESTIONS})
selected_domains = st.sidebar.multiselect(
    "Filter by Domain",
    options=domains,
    default=domains,
    key="domain_filter"
)

# Apply filter
filtered = [q for q in QUESTIONS if q["domain"] in selected_domains]
if st.sidebar.button("Apply Filter"):
    st.session_state.questions = filtered.copy()
    random.shuffle(st.session_state.questions)
    st.session_state.idx = 0
    st.session_state.answered = False
    st.session_state.score = 0
    st.session_state.shuffled_data = None   # force reshuffle for new question set

total = len(st.session_state.questions)
if total == 0:
    st.warning("No questions selected.")
    st.stop()

# Current question
q = st.session_state.questions[st.session_state.idx]

# *** FIX: Only shuffle when shuffling_data is None (i.e., first time for this question) ***
if st.session_state.shuffled_data is None:
    correct_letter = q["answer"]
    original_index = {"A":0, "B":1, "C":2, "D":3}[correct_letter]
    options_with_flag = [(text, i == original_index) for i, text in enumerate(q["options"])]
    random.shuffle(options_with_flag)
    st.session_state.shuffled_data = options_with_flag

options_with_flag = st.session_state.shuffled_data  # stable until next question

# Radio labels: A) B) C) D) are fixed
labels = ["A", "B", "C", "D"]
radio_options = [f"{labels[i]}. {options_with_flag[i][0]}" for i in range(4)]

# Progress sidebar
st.sidebar.progress((st.session_state.idx + 1) / total)
st.sidebar.write(f"Question {st.session_state.idx + 1} of {total}")
st.sidebar.write(f"Score: {st.session_state.score} / {st.session_state.idx}")

# Question display
st.subheader(f"Question {st.session_state.idx + 1}")
st.write(q["question"])

# Radio selection
selected = st.radio(
    "Select your answer:",
    radio_options,
    index=None,
    key=f"radio_{st.session_state.idx}",
    disabled=st.session_state.answered
)

col1, col2 = st.columns([1, 2])
if not st.session_state.answered:
    if col1.button("Submit", use_container_width=True):
        if selected is not None:
            selected_label = selected[0]   # e.g., "A"
            selected_idx = labels.index(selected_label)
            st.session_state.selected_idx = selected_idx
            st.session_state.answered = True
            if options_with_flag[selected_idx][1]:  # is_correct?
                st.session_state.score += 1
            st.rerun()
        else:
            st.warning("Please select an answer first.")
else:
    # Find correct index in the shuffled set
    correct_idx = next(i for i, (_, is_correct) in enumerate(options_with_flag) if is_correct)
    if st.session_state.selected_idx == correct_idx:
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Incorrect. The correct answer is: **{labels[correct_idx]}**")
    correct_text = options_with_flag[correct_idx][0]
    st.info(f"Correct answer: {correct_text}")
    st.markdown(f"**Explanation:** {q.get('explanation', '')}")

    # Navigation buttons
    nav1, nav2, nav3 = st.columns([1, 2, 1])
    if st.session_state.idx > 0:
        if nav1.button("⬅ Previous", use_container_width=True):
            st.session_state.idx -= 1
            st.session_state.answered = False
            st.session_state.shuffled_data = None   # reshuffle for the previous question
            st.rerun()
    if st.session_state.idx < total - 1:
        if nav2.button("Next ➡", use_container_width=True):
            st.session_state.idx += 1
            st.session_state.answered = False
            st.session_state.shuffled_data = None   # reshuffle for the next question
            st.rerun()
    else:
        st.markdown("---")
        st.subheader("🎉 Quiz Completed!")
        st.write(f"Final Score: **{st.session_state.score} / {total}**")
        if st.button("Restart Quiz"):
            st.session_state.questions = filtered.copy()
            random.shuffle(st.session_state.questions)
            st.session_state.idx = 0
            st.session_state.score = 0
            st.session_state.answered = False
            st.session_state.shuffled_data = None
            st.rerun()
