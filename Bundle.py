import streamlit as st
import random
import re

# ========== SAMPLE QUESTIONS (with prefixed options) ==========
# The options may contain "A) ...", "B) ..." etc. – the app strips them automatically.
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
        "option_explanations": {
            "A) ISACA Code of Professional Ethics": "Incorrect – The ITAF does include the ISACA Code of Professional Ethics.",
            "B) IS audit and assurance standards": "Incorrect – The ITAF does include IS audit and assurance standards.",
            "C) ISACA Audit Job Practice": "Correct – The IT Assurance Framework does not contain the ISACA Audit Job Practice.",
            "D) IS audit and assurance guidelines": "Incorrect – The ITAF does include IS audit and assurance guidelines."
        }
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
        "option_explanations": {
            "A) Information technology policies": "Incorrect – IT policies alone do not control processes; they are only one part.",
            "B) Information technology policies along with audits of those policies": "Incorrect – IT policies and audits are only one component of governance.",
            "C) Information technology governance": "Correct – ISACA defines governance as the processes that ensure stakeholder needs are evaluated…",
            "D) Metrics as compared to similar organizations": "Incorrect – Benchmarking metrics is not a significant part of governance; many organisations forego it entirely."
        }
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
        "option_explanations": {
            "A) The system being considered is too expensive to implement all at once.": "Incorrect – Cost alone is not the primary driver for a proof of concept.",
            "B) The system being considered will be a fully customized solution.": "Incorrect – A fully custom solution may not yet exist for a POC.",
            "C) The system being considered is too complicated to evaluate fully.": "Correct – A POC is used when complexity makes it hard to evaluate through documents or walkthroughs.",
            "D) The system being considered is not yet available.": "Incorrect – A POC requires an existing solution to evaluate."
        }
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
        "option_explanations": {
            "A) Bridge": "Incorrect – A bridge forwards all packets regardless of destination.",
            "B) Gateway": "Incorrect – A gateway translates between protocols, not IP forwarding.",
            "C) Router": "Correct – Routers forward packets based on destination IP addresses.",
            "D) Switch": "Incorrect – A switch forwards based on MAC addresses, not IP."
        }
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
        "option_explanations": {
            "A) Jump server": "Incorrect – A jump server does not address configuration consistency.",
            "B) Firewall rule": "Incorrect – Firewall rules help control traffic, not internal server hardening.",
            "C) Hardening standard": "Correct – A hardening standard defines security configurations for systems and devices.",
            "D) CMDB": "Incorrect – A CMDB manages configuration data but does not define security settings."
        }
    }
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
    st.session_state.shuffled_data = None  # will store (original_text, stripped_text, is_correct)

# Helper: strip leading "X) " or "X)"
def strip_option_prefix(text):
    return re.sub(r"^[A-D]\)\s*", "", text)

# Domain filter
all_domains = sorted({q["domain"] for q in QUESTIONS})
selected_domains = st.sidebar.multiselect(
    "Filter by Domain",
    options=all_domains,
    default=all_domains,
    key="domain_filter"
)

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

# Prepare shuffled options (stable until next question)
if st.session_state.shuffled_data is None:
    raw_options = q["options"]
    correct_letter = q["correct"]
    correct_raw = raw_options[ord(correct_letter) - ord("A")]
    # Build list of (original_text, stripped_text, is_correct)
    opts_with_flag = []
    for opt in raw_options:
        stripped = strip_option_prefix(opt)
        is_correct = (stripped == strip_option_prefix(correct_raw))
        opts_with_flag.append((opt, stripped, is_correct))
    random.shuffle(opts_with_flag)
    st.session_state.shuffled_data = opts_with_flag

shuffled = st.session_state.shuffled_data
labels = ["A", "B", "C", "D"]
radio_choices = [f"{labels[i]}) {shuffled[i][1]}" for i in range(4)]

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
            selected_label = selected[0]
            selected_idx = labels.index(selected_label)
            st.session_state.selected_idx = selected_idx
            st.session_state.answered = True
            if shuffled[selected_idx][2]:  # is_correct?
                st.session_state.score += 1
            st.rerun()
        else:
            st.warning("Please select an answer first.")
else:
    # Detailed per-option feedback
    st.markdown("---")
    selected_idx = st.session_state.selected_idx
    explanations = q.get("option_explanations", {})

    for i, (orig_text, stripped_text, is_correct) in enumerate(shuffled):
        letter = labels[i]
        display_text = f"{letter}) {stripped_text}"
        # Use original text (with prefix) to look up explanation
        explanation = explanations.get(orig_text, "No detailed explanation available.")

        if is_correct:
            st.success(f"**{display_text}**  \n{explanation}")
        elif i == selected_idx and not is_correct:
            st.error(f"**{display_text}** (your answer)  \n{explanation}")
        else:
            st.error(f"**{display_text}**  \n{explanation}")

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
