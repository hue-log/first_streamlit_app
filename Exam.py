import streamlit as st
import re

# ==========================================
# 1. PARSER & SAMPLE DATA
# ==========================================
def parse_questions_from_text(text):
    """Regex engine to parse questions from the raw PDF text dumps."""
    pattern = re.compile(
        r'(\d+)\.\s+(.*?)\r?\n\s*A\.\s+(.*?)\r?\n\s*B\.\s+(.*?)\r?\n\s*C\.\s+(.*?)\r?\n\s*D\.\s+(.*?)\r?\n\s*([A-D]) is the correct answer\.\s*\r?\n\s*Justification[:：]\s*\r?\n(.*?)(?=\r?\n\d+\.\s+|\Z)', 
        re.DOTALL
    )
    questions = []
    for match in pattern.finditer(text):
        q_num = match.group(1)
        q_text = match.group(2).strip().replace('\n', ' ')
        opt_a = match.group(3).strip()
        opt_b = match.group(4).strip()
        opt_c = match.group(5).strip()
        opt_d = match.group(6).strip()
        correct = match.group(7).strip()
        justification = match.group(8).strip()
        
        questions.append({
            "question": f"{q_num}. {q_text}",
            "options": {"A": opt_a, "B": opt_b, "C": opt_c, "D": opt_d},
            "correct_answer": correct,
            "justification": justification
        })
    return questions

# 5 Sample Questions embedded for immediate testing
sample_questions = [
    {"question": "1. Who should review and approve system deliverables as they are defined and accomplished, to ensure the successful completion and implementation of a new business system application?", "options": {"A": "User management", "B": "Project steering committee", "C": "Senior management", "D": "Quality assurance (QA) staff"}, "correct_answer": "A", "justification": "User management assumes ownership of the project and resulting system, allocates qualified representatives to the team, and actively participates in system requirements definition, acceptance testing and user training."},
    {"question": "2. Organizations requiring employees to take a mandatory vacation each year PRIMARILY want to ensure that:", "options": {"A": "adequate cross-training exists between functions.", "B": "an effective internal control environment is in place by increasing morale.", "C": "potential irregularities in processing are identified by a temporary replacement.", "D": "the risk of processing errors is reduced."}, "correct_answer": "C", "justification": "Employees who perform critical and sensitive functions within an organization should be required to take some time off to help ensure that irregularities and fraud are detected."},
    {"question": "3. Web application developers occasionally use hidden fields on web pages to save information about a client session. The MOST likely web-based attack due to this practice is:", "options": {"A": "parameter tampering.", "B": "cross-site scripting.", "C": "cookie poisoning.", "D": "stealth commanding."}, "correct_answer": "A", "justification": "Web application developers sometimes use hidden fields to save information about a client session or to submit hidden parameters. Because hidden form fields do not display in the browser, developers may feel safe passing unvalidated data. An attacker can intercept, modify and submit requests. This malicious modification is known as parameter tampering."},
    {"question": "4. An organization is considering using a new IT service provider. From an audit perspective, which of the following is the MOST important item to review?", "options": {"A": "References from other clients for the service provider", "B": "The physical security of the service provider site", "C": "The proposed service level agreement (SLA) with the service provider", "D": "Background checks of the service provider's employees"}, "correct_answer": "C", "justification": "An SLA is a guarantee that the provider will deliver the services according to the contract. The IS auditor will want to ensure that performance and security requirements are clearly stated in the SLA."},
    {"question": "5. Which of the following is the BEST factor for determining the required extent of data collection during the planning phase of an information systems (IS) compliance audit?", "options": {"A": "Complexity of the organization's operation", "B": "Findings and issues noted from the prior year", "C": "Purpose, objective and scope of the audit", "D": "Auditor's familiarity with the organization"}, "correct_answer": "C", "justification": "The extent to which data will be collected during an IS audit is related directly to the purpose, objective and scope of the audit."}
]

# ==========================================
# 2. STREAMLIT UI & SESSION STATE
# ==========================================
st.set_page_config(page_title="CISA Exam Prep", layout="wide")

# Initialize Session State
if 'questions' not in st.session_state:
    st.session_state.questions = sample_questions
if 'current_q_index' not in st.session_state:
    st.session_state.current_q_index = 0
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = None
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Sidebar for File Upload
st.sidebar.title("📚 Exam Preparation")
st.sidebar.markdown("---")
uploaded_file = st.sidebar.file_uploader("Upload Full TXT File", type=["txt"])
if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    parsed = parse_questions_from_text(text)
    if parsed:
        st.session_state.questions = parsed
        st.session_state.current_q_index = 0
        st.session_state.submitted = False
        st.sidebar.success(f"✅ Loaded {len(parsed)} questions!")
    else:
        st.sidebar.error("❌ No questions found in file. Check formatting.")

# Reset Button
if st.sidebar.button("🔄 Reset Quiz"):
    st.session_state.questions = sample_questions
    st.session_state.current_q_index = 0
    st.session_state.selected_option = None
    st.session_state.submitted = False
    st.rerun()

# ==========================================
# 3. MAIN QUIZ LOGIC
# ==========================================
if st.session_state.questions:
    q_data = st.session_state.questions[st.session_state.current_q_index]
    
    # Progress Bar
    progress = (st.session_state.current_q_index + 1) / len(st.session_state.questions)
    st.progress(progress, text=f"Question {st.session_state.current_q_index + 1} of {len(st.session_state.questions)}")
    
    st.markdown(f"### {q_data['question']}")
    
    # Options (Radio Buttons)
    options = list(q_data["options"].keys())
    option_texts = [f"{k}. {v}" for k, v in q_data["options"].items()]
    
    selected_text = st.radio(
        "Select your answer:",
        option_texts,
        index=options.index(st.session_state.selected_option) if st.session_state.selected_option else None,
        disabled=st.session_state.submitted,
        label_visibility="collapsed"
    )
    
    if selected_text:
        st.session_state.selected_option = selected_text[0] # Extract 'A', 'B', 'C', or 'D'
        
    # Action Buttons
    col1, col2 = st.columns(2)
    with col1:
        submit_btn = st.button("✅ Submit Answer", disabled=st.session_state.submitted, use_container_width=True, type="primary")
    with col2:
        next_btn = st.button("➡️ Next Question", disabled=not st.session_state.submitted, use_container_width=True)
        
    # Handle Submit
    if submit_btn:
        if st.session_state.selected_option:
            st.session_state.submitted = True
            st.rerun()
        else:
            st.warning("Please select an option before submitting.")
            
    # Handle Next
    if next_btn:
        if st.session_state.current_q_index < len(st.session_state.questions) - 1:
            st.session_state.current_q_index += 1
            st.session_state.selected_option = None
            st.session_state.submitted = False
            st.rerun()
        else:
            st.balloons()
            st.success("🎉 Congratulations! You have completed all questions in this set.")
            
    # ==========================================
    # 4. FEEDBACK & EXPLANATION (COLOR CODED)
    # ==========================================
    if st.session_state.submitted:
        correct = q_data["correct_answer"]
        selected = st.session_state.selected_option
        
        # Generate HTML for Color-Coded Options
        results_html = "<br>"
        for k, v in q_data["options"].items():
            if k == correct:
                color = "#28a745" # Green
                icon = "✅"
                bg = "#e6f4ea"
            elif k == selected and k != correct:
                color = "#dc3545" # Red
                icon = "❌"
                bg = "#fce8e6"
            else:
                color = "#6c757d" # Gray
                icon = ""
                bg = "#f8f9fa"
                
            results_html += f'<div style="padding: 12px; margin: 6px 0; border-radius: 6px; background-color: {bg}; color: {color}; font-weight: bold; font-size: 16px; border-left: 5px solid {color};">{icon} {k}. {v}</div>'
            
        st.markdown(results_html, unsafe_allow_html=True)
        
        # Result Summary
        if selected == correct:
            st.success("**🎉 Correct!** Great job.")
        else:
            st.error(f"**❌ Incorrect.** The correct answer is **{correct}**.")
            
        # Justification
        st.markdown("### 💡 Explanation:")
        st.info(q_data["justification"])
