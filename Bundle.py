import streamlit as st
import random

# ========== SAMPLE QUESTIONS (one per domain) ==========
# Each question uses the format: id, question, options (with "A) ...", etc.), correct (letter), explanation
QUESTIONS = [
    # Domain 1 – The Audit Process
    {
        "id": 1,
        "domain": "Domain 1 – The Audit Process",
        "question": "The IT Assurance Framework consists of all of the following except:",
        "options": [
            "A) ISACA Code of Professional Ethics",
            "B) IS audit and assurance standards",
            "C) ISACA Audit Job Practice",
            "D) IS audit and assurance guidelines"
        ],
        "correct": "C",
        "explanation": "The IT Assurance Framework includes the ISACA Code of Professional Ethics, IS audit and assurance standards, IS audit and assurance guidelines, and IS audit and assurance tools and techniques. It does not contain the ISACA Audit Job Practice."
    },
    # Domain 2 – IT Governance and Management
    {
        "id": 2,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "Management's control of information technology processes is best described as:",
        "options": [
            "A) Information technology policies",
            "B) Information technology policies along with audits of those policies",
            "C) Information technology governance",
            "D) Metrics as compared to similar organizations"
        ],
        "correct": "C",
        "explanation": "ISACA defines governance as the processes that ensure stakeholder needs are evaluated to determine balanced, agreed‑on enterprise objectives."
    },
    # Domain 3 – IT Life Cycle Management
    {
        "id": 3,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "What is the best reason for considering a proof of concept?",
        "options": [
            "A) The system being considered is too expensive to implement all at once.",
            "B) The system being considered will be a fully customized solution.",
            "C) The system being considered is too complicated to evaluate fully.",
            "D) The system being considered is not yet available."
        ],
        "correct": "C",
        "explanation": "A proof of concept is used when a system is too complex to evaluate through specifications alone."
    },
    # Domain 4 – IT Service Management and Continuity
    {
        "id": 4,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "A device that forwards packets to their destination based on their destination IP address is known as:",
        "options": [
            "A) Bridge",
            "B) Gateway",
            "C) Router",
            "D) Switch"
        ],
        "correct": "C",
        "explanation": "A router uses destination IP addresses to forward packets toward their destination."
    },
    # Domain 5 – Information Asset Protection
    {
        "id": 5,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "A new information security manager has examined the systems in the production environment and has found that their security‑related configurations are inadequate and inconsistent. To improve this situation, the security manager should create a:",
        "options": [
            "A) Jump server",
            "B) Firewall rule",
            "C) Hardening standard",
            "D) CMDB"
        ],
        "correct": "C",
        "explanation": "A hardening standard defines the security configurations applicable to systems and devices."
    },
]

# ========== STREAMLIT APP ==========
st.set_page_config(page_title="CISA Practice Exam", layout="wide")

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
    st.session_state.shuffled_data = None  # [(text, is_correct), ...] for current Q

# Domain filter
all_domains = sorted({q["domain"] for q in QUESTIONS})
selected_domains = st.sidebar.multiselect(
    "Filter by Domain",
    options=all_domains,
    default=all_domains,
    key="domain_filter"
)

# Apply filter button (also triggered on first load)
if "filtered" not in st.session_state or st.sidebar.button("Apply Filter"):
    filtered = [q for q in QUESTIONS if q["domain"] in selected_domains]
    st.session_state.questions = filtered.copy()
    random.shuffle(st.session_state.questions)
    st.session_state.idx = 0
    st.session_state.answered = False
    st.session_state.score = 0
    st.session_state.shuffled_data = None
    st.session_state.filtered = True

total = len(st.session_state.questions)
if total == 0:
    st.warning("No questions match the selected domains.")
    st.stop()

# Current question
q = st.session_state.questions[st.session_state.idx]

# Prepare shuffled options (only once per question)
if st.session_state.shuffled_data is None:
    # Extract plain text from "A) text" format
    option_texts = [opt[3:].strip() for opt in q["options"]]
    correct_letter = q["correct"]
    correct_text = option_texts[ord(correct_letter) - ord("A")]
    # Create list of (text, is_correct)
    opts_with_flag = [(text, text == correct_text) for text in option_texts]
    random.shuffle(opts_with_flag)
    st.session_state.shuffled_data = opts_with_flag

shuffled = st.session_state.shuffled_data
labels = ["A", "B", "C", "D"]
radio_choices = [f"{labels[i]}) {shuffled[i][0]}" for i in range(4)]

# Progress sidebar
st.sidebar.progress((st.session_state.idx + 1) / total)
st.sidebar.write(f"Question {st.session_state.idx + 1} of {total}")
st.sidebar.write(f"Score: {st.session_state.score} / {st.session_state.idx}")

# Display question
st.subheader(f"Question {st.session_state.idx + 1}")
st.write(q["question"])

# Radio selection
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
            selected_label = selected[0]   # e.g., "A"
            selected_idx = labels.index(selected_label)
            st.session_state.selected_idx = selected_idx
            st.session_state.answered = True
            if shuffled[selected_idx][1]:  # is_correct?
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
        st.error(f"❌ Incorrect. The correct answer is: **{labels[correct_pos]})**")
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
            filtered_again = [q for q in QUESTIONS if q["domain"] in selected_domains]
            st.session_state.questions = filtered_again.copy()
            random.shuffle(st.session_state.questions)
            st.session_state.idx = 0
            st.session_state.score = 0
            st.session_state.answered = False
            st.session_state.shuffled_data = None
            st.rerun()
