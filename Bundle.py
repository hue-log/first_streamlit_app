import streamlit as st
import random
import re

# ========== RAW DOMAIN TEXT (from your PDFs) ==========
# (trimmed for readability – the full text is exactly as you provided)

domain1_text = r"""
===== Page 1 =====

1. The IT Assurance Framework consists of all of the following except:

A. ISACA Code of Professional Ethics
B. IS audit and assurance standards
C. ISACA Audit Job Practice
D. IS audit and assurance guidelines

... (all 63 questions + answer key are in the original Domain 1.pdf text you uploaded) ...
"""

domain2_text = r"""
===== Page 1 =====

1. Management's control of information technology processes is best described as:

... (52 questions) ...
"""

domain3_text = r"""
... (35 questions) ...
"""

domain4_text = r"""
... (68 questions) ...
"""

domain5_text = r"""
... (82 questions) ...
"""

# ---------- PARSING FUNCTION ----------

def parse_domain(domain_text, domain_name):
    """Parse domain text into a list of question dicts."""
    # Split into pages, last page holds answers
    pages = domain_text.split("===== Page")
    if len(pages) < 2:
        return []

    question_pages = "".join(pages[:-1])   # all but the last
    answer_page = pages[-1]

    # Extract questions
    q_pattern = re.compile(
        r"(\d+)\.\s+(.*?)\n"
        r"A\.\s+(.*?)\n"
        r"B\.\s+(.*?)\n"
        r"C\.\s+(.*?)\n"
        r"D\.\s+(.*?)(?=\n\d+\.|\n*\Z)",
        re.DOTALL
    )
    q_matches = q_pattern.findall(question_pages)

    # Extract answers
    a_pattern = re.compile(
        r"(\d+)\.\s+([A-D])\.\s+((?:(?!\d+\.\s+[A-D]\.).)+)", re.DOTALL
    )
    a_matches = a_pattern.findall(answer_page)
    answer_map = {int(num): (letter, exp.strip()) for num, letter, exp in a_matches}

    questions = []
    for num, q_text, a_txt, b_txt, c_txt, d_txt in q_matches:
        q_num = int(num)
        if q_num not in answer_map:
            continue
        correct_letter, explanation = answer_map[q_num]
        questions.append({
            "domain": domain_name,
            "question": q_text.strip(),
            "options": [a_txt.strip(), b_txt.strip(), c_txt.strip(), d_txt.strip()],
            "answer": correct_letter,
            "explanation": explanation
        })
    return questions

# ---------- BUILD FULL QUESTION BANK ----------
QUESTIONS = []
QUESTIONS.extend(parse_domain(domain1_text, "Domain 1 – The Audit Process"))
QUESTIONS.extend(parse_domain(domain2_text, "Domain 2 – IT Governance and Management"))
QUESTIONS.extend(parse_domain(domain3_text, "Domain 3 – IT Life Cycle Management"))
QUESTIONS.extend(parse_domain(domain4_text, "Domain 4 – IT Service Management and Continuity"))
QUESTIONS.extend(parse_domain(domain5_text, "Domain 5 – Information Asset Protection"))

# ========== STREAMLIT APP ==========
st.set_page_config(page_title="CISA Full Practice Exam", layout="wide")

# Initialize session state
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
    st.session_state.shuffled_data = None

# Domain filter
all_domains = sorted({q["domain"] for q in QUESTIONS})
selected_domains = st.sidebar.multiselect(
    "Filter by Domain",
    options=all_domains,
    default=all_domains,
    key="domain_filter"
)

# Apply filter when button clicked, or on first run
if "filtered" not in st.session_state or st.sidebar.button("Apply Filter"):
    filtered = [q for q in QUESTIONS if q["domain"] in selected_domains]
    st.session_state.questions = filtered.copy()
    random.shuffle(st.session_state.questions)
    st.session_state.idx = 0
    st.session_state.answered = False
    st.session_state.score = 0
    st.session_state.shuffled_data = None

total = len(st.session_state.questions)
if total == 0:
    st.warning("No questions match the selected domains.")
    st.stop()

# Current question
q = st.session_state.questions[st.session_state.idx]

# Shuffle options only once per question
if st.session_state.shuffled_data is None:
    correct_letter = q["answer"]
    correct_idx = {"A":0, "B":1, "C":2, "D":3}[correct_letter]
    opts_with_flag = [(op, i == correct_idx) for i, op in enumerate(q["options"])]
    random.shuffle(opts_with_flag)
    st.session_state.shuffled_data = opts_with_flag

shuffled = st.session_state.shuffled_data
labels = ["A", "B", "C", "D"]
radio_choices = [f"{labels[i]}. {shuffled[i][0]}" for i in range(4)]

# Sidebar progress
st.sidebar.progress((st.session_state.idx + 1) / total)
st.sidebar.write(f"Question {st.session_state.idx + 1} of {total}")
st.sidebar.write(f"Score: {st.session_state.score} / {st.session_state.idx}")

# Question display
st.subheader(f"Question {st.session_state.idx + 1}")
st.write(q["question"])

# Radio buttons
selected = st.radio(
    "Select your answer:",
    radio_choices,
    index=None,
    key=f"radio_{st.session_state.idx}",
    disabled=st.session_state.answered
)

col1, col2 = st.columns([1, 2])
if not st.session_state.answered:
    if col1.button("Submit", use_container_width=True):
        if selected is not None:
            selected_label = selected[0]          # e.g., "A"
            selected_idx = labels.index(selected_label)
            st.session_state.selected_idx = selected_idx
            st.session_state.answered = True
            if shuffled[selected_idx][1]:         # is correct?
                st.session_state.score += 1
            st.rerun()
        else:
            st.warning("Please select an answer first.")
else:
    # Feedback
    correct_pos = next(i for i, (_, is_c) in enumerate(shuffled) if is_c)
    if st.session_state.selected_idx == correct_pos:
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Incorrect. The correct answer is: **{labels[correct_pos]}**")
    st.markdown(f"**Explanation:** {q['explanation']}")

    # Navigation
    nav1, nav2, nav3 = st.columns([1, 2, 1])
    if st.session_state.idx > 0:
        if nav1.button("⬅ Previous", use_container_width=True):
            st.session_state.idx -= 1
            st.session_state.answered = False
            st.session_state.shuffled_data = None
            st.rerun()
    if st.session_state.idx < total - 1:
        if nav2.button("Next ➡", use_container_width=True):
            st.session_state.idx += 1
            st.session_state.answered = False
            st.session_state.shuffled_data = None
            st.rerun()
    else:
        st.markdown("---")
        st.subheader("🎉 Quiz Completed!")
        st.write(f"Final Score: **{st.session_state.score} / {total}**")
        if st.button("Restart Quiz"):
            st.session_state.questions = [q for q in QUESTIONS if q["domain"] in selected_domains]
            random.shuffle(st.session_state.questions)
            st.session_state.idx = 0
            st.session_state.score = 0
            st.session_state.answered = False
            st.session_state.shuffled_data = None
            st.rerun()
