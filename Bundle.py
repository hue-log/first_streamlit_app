import streamlit as st
import random

# ========== ALL QUESTIONS FROM ALL DOMAINS ==========
# Format: {"domain": str, "question": str, "options": [A, B, C, D], "answer": "A/B/C/D", "explanation": str}

QUESTIONS = [
    # ================== DOMAIN 1 – THE AUDIT PROCESS ==================
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
        "explanation": "The IT Assurance Framework includes the ISACA Code of Professional Ethics, IS audit and assurance standards, guidelines, and tools/techniques. It does not contain the ISACA Audit Job Practice."
    },
    {
        "domain": "Domain 1 – The Audit Process",
        "question": "An auditor is examining an IT organization's change control process. ... (full question from Domain 1 Q2)",
        "options": [...],
        "answer": "B",
        "explanation": "..."
    },
    # ... add all 63 Domain 1 questions here ...

    # ================== DOMAIN 2 – IT GOVERNANCE & MANAGEMENT ==================
    {
        "domain": "Domain 2 – IT Governance and Management",
        "question": "Management's control of information technology processes is best described as:",
        "options": [
            "Information technology policies",
            "Information technology policies along with audits of those policies",
            "Information technology governance",
            "Metrics as compared to similar organizations"
        ],
        "answer": "C",
        "explanation": "ISACA defines governance as the set of processes that ensure stakeholder needs are evaluated to determine balanced, agreed-on enterprise objectives."
    },
    # ... add all 52 Domain 2 questions ...

    # ================== DOMAIN 3 – IT LIFE CYCLE MANAGEMENT ==================
    {
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "What is the best reason for considering a proof of concept?",
        "options": [
            "The system being considered is too expensive to implement all at once.",
            "The system being considered will be a fully customized solution.",
            "The system being considered is too complicated to evaluate fully.",
            "The system being considered is not yet available."
        ],
        "answer": "C",
        "explanation": "A POC is used when a system is too complex to evaluate by simply walking through specifications."
    },
    # ... add all 35 Domain 3 questions ...

    # ================== DOMAIN 4 – IT SERVICE MANAGEMENT & CONTINUITY ==================
    {
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "A device that forwards packets to their destination based on their destination IP address is known as:",
        "options": ["Bridge", "Gateway", "Router", "Switch"],
        "answer": "C",
        "explanation": "A router uses destination IP addresses to forward packets toward their destination."
    },
    # ... add all 68 Domain 4 questions ...

    # ================== DOMAIN 5 – INFORMATION ASSET PROTECTION ==================
    {
        "domain": "Domain 5 – Information Asset Protection",
        "question": "A new information security manager has examined the systems in the production environment and has found that their security-related configurations are inadequate and inconsistent. To improve this situation, the security manager should create a:",
        "options": ["Jump server", "Firewall rule", "Hardening standard", "CMDB"],
        "answer": "C",
        "explanation": "A hardening standard defines the security configurations applicable to systems and devices."
    },
    # ... add all 82 Domain 5 questions ...
]

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
if "user_answer" not in st.session_state:
    st.session_state.user_answer = None

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
    st.session_state.idx = 0
    st.session_state.answered = False
    st.session_state.score = 0
    random.shuffle(st.session_state.questions)

total = len(st.session_state.questions)
if total == 0:
    st.warning("No questions selected.")
    st.stop()

# Current question
q = st.session_state.questions[st.session_state.idx]
options = q["options"]
correct_letter = q["answer"]

# Shuffle options for this rendering
option_letters = ["A", "B", "C", "D"]
shuffled = list(zip(option_letters, options))
random.shuffle(shuffled)
letter_map = {orig: new for (new, _), (orig, _) in zip(shuffled, zip(option_letters, options))}
# Build display
radio_choices = [f"{letter}. {text}" for letter, text in shuffled]

# Progress
st.sidebar.progress((st.session_state.idx + 1) / total)
st.sidebar.write(f"Question {st.session_state.idx + 1} of {total}")
st.sidebar.write(f"Score: {st.session_state.score} / {st.session_state.idx}")

st.subheader(f"Question {st.session_state.idx + 1}")
st.write(q["question"])

selected = st.radio(
    "Choose one:",
    radio_choices,
    index=None,
    key=f"radio_{st.session_state.idx}",
    disabled=st.session_state.answered
)

col1, col2 = st.columns([1, 2])
if not st.session_state.answered:
    if col1.button("Submit", use_container_width=True):
        if selected is not None:
            user_letter = selected[0]               # e.g., "A"
            st.session_state.user_answer = user_letter
            st.session_state.answered = True
            if user_letter == correct_letter:
                st.session_state.score += 1
            st.rerun()
        else:
            st.warning("Please select an answer.")
else:
    # Show feedback
    if st.session_state.user_answer == correct_letter:
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Incorrect. The correct answer is **{correct_letter}**.")
    st.markdown(f"**Explanation:** {q['explanation']}")
    # Show mapping of correct answer
    correct_text = next(text for letter, text in shuffled if letter == correct_letter)
    st.info(f"Correct answer: {correct_letter}. {correct_text}")

    # Navigation
    nav1, nav2, nav3 = st.columns([1, 2, 1])
    if st.session_state.idx > 0:
        if nav1.button("⬅ Previous", use_container_width=True):
            st.session_state.idx -= 1
            st.session_state.answered = False
            st.rerun()
    if st.session_state.idx < total - 1:
        if nav2.button("Next ➡", use_container_width=True):
            st.session_state.idx += 1
            st.session_state.answered = False
            st.rerun()
    else:
        st.markdown("---")
        st.subheader("🎉 Quiz Completed!")
        st.write(f"Final Score: **{st.session_state.score} / {total}**")
        if st.button("Restart"):
            st.session_state.idx = 0
            st.session_state.score = 0
            st.session_state.answered = False
            random.shuffle(st.session_state.questions)
            st.rerun()
