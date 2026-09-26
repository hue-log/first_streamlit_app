import streamlit as st
import random

# ==========================================
# 1. QUESTIONS DATABASE
# ==========================================
# Note: The structure now includes specific explanations for EACH option (A, B, C, D)
# to match the detailed feedback in your screenshot.

QUESTIONS_DB = {
    "Domain 1: IS Auditing Process": [
        {
            "q": "Which of the following is MOST useful for making risk treatment decisions?",
            "opts": {
                "A": "A control testing procedure",
                "B": "A control framework",
                "C": "A risk appetite statement",
                "D": "A security policy"
            },
            "ans": "C",
            "exp": {
                "A": "Control testing procedures are not related to risk treatment decisions.",
                "B": "An organization's control framework is not typically used for making risk treatment decisions.",
                "C": "A risk appetite statement provides guidance on the types of risk and the amount of risk an organization may be willing to accept versus what it prefers to mitigate, avoid, or transfer.",
                "D": "Security policy is not a primary means for making risk treatment decisions."
            }
        },
        {
            "q": "Which of the following is the BEST factor for determining the required extent of data collection during the planning phase of an information systems (IS) compliance audit?",
            "opts": {
                "A": "Complexity of the organization's operation",
                "B": "Findings and issues noted from the prior year",
                "C": "Purpose, objective and scope of the audit",
                "D": "Auditor's familiarity with the organization"
            },
            "ans": "C",
            "exp": {
                "A": "The complexity of the organization's operation is a factor in planning but does not directly determine the extent of data collection.",
                "B": "Prior findings are factors in planning but do not directly determine the extent of data collection.",
                "C": "The extent to which data will be collected is related directly to the purpose, objective and scope of the audit.",
                "D": "An auditor's familiarity is a factor but the audit must be based on sufficient evidence, not familiarity."
            }
        },
        {
            "q": "What BEST describes the risk that information collected may contain a material error that may go undetected during information systems (IS) auditing?",
            "opts": {
                "A": "Inherent risk",
                "B": "Audit risk",
                "C": "Control risk",
                "D": "Detection risk"
            },
            "ans": "B",
            "exp": {
                "A": "Inherent risk is the risk level without considering controls.",
                "B": "Audit risk is the probability that reports may contain material errors and the auditor may not detect them.",
                "C": "Control risk is the risk that a material error exists that would not be prevented by internal controls.",
                "D": "Detection risk is the risk that material errors will not be detected by the auditor."
            }
        }
    ],
    "Domain 2: Governance and Management of IT": [
        {
            "q": "Organizations requiring employees to take a mandatory vacation each year PRIMARILY want to ensure that:",
            "opts": {
                "A": "adequate cross-training exists between functions.",
                "B": "an effective internal control environment is in place by increasing morale.",
                "C": "potential irregularities in processing are identified by a temporary replacement.",
                "D": "the risk of processing errors is reduced."
            },
            "ans": "C",
            "exp": {
                "A": "Cross-training is good practice but can be achieved without mandatory vacation.",
                "B": "Good morale is worthwhile but not a means to achieve an effective internal control system.",
                "C": "Employees in critical functions should take time off to help ensure irregularities and fraud are detected by a replacement.",
                "D": "Rotating employees can reduce errors, but this is not the primary reason for mandatory vacation."
            }
        }
    ]
}

# ==========================================
# 2. STREAMLIT UI & SESSION STATE
# ==========================================
st.set_page_config(page_title="CISA Exam Prep", layout="wide")

# Initialize Session State
if 'quiz_active' not in st.session_state: st.session_state.quiz_active = False
if 'questions' not in st.session_state: st.session_state.questions = []
if 'current_idx' not in st.session_state: st.session_state.current_idx = 0
if 'selected' not in st.session_state: st.session_state.selected = None
if 'submitted' not in st.session_state: st.session_state.submitted = False
if 'score' not in st.session_state: st.session_state.score = 0

# --- SIDEBAR CONTROLS ---
st.sidebar.title("⚙️ Quiz Settings")
st.sidebar.markdown("---")

domains = list(QUESTIONS_DB.keys())
selected_domains = st.sidebar.multiselect("1. Select Domains:", domains, default=[domains[0]])

# Pool questions based on selection
pool = []
for d in selected_domains:
    pool.extend(QUESTIONS_DB[d])

max_q = len(pool)

if max_q > 0:
    num_q = st.sidebar.slider("2. Number of Questions:", 1, max_q, min(1, max_q))
    
    if st.sidebar.button("🔄 Shuffle & Start Quiz", use_container_width=True, type="primary"):
        st.session_state.questions = random.sample(pool, num_q)
        st.session_state.current_idx = 0
        st.session_state.selected = None
        st.session_state.submitted = False
        st.session_state.score = 0
        st.session_state.quiz_active = True
        st.rerun()
else:
    st.sidebar.warning("Please select at least one domain.")

if st.sidebar.button("🔙 Reset & Configure New Quiz"):
    st.session_state.quiz_active = False
    st.rerun()

# --- MAIN AREA ---
st.title("🎓 CISA Exam Practice App")

if not st.session_state.quiz_active:
    st.info("👈 **Step 1:** Select your domains from the sidebar.\n\n👈 **Step 2:** Choose the number of questions.\n\n **Step 3:** Click **Shuffle & Start Quiz** to begin!")
else:
    total = len(st.session_state.questions)
    idx = st.session_state.current_idx
    
    # Progress Bar
    st.progress((idx + 1) / total)
    st.markdown(f"### 📝 Question {idx + 1} of {total} &nbsp;&nbsp;|&nbsp;&nbsp; 🏆 Score: {st.session_state.score}/{idx}")
    
    current_q = st.session_state.questions[idx]
    st.markdown(f"#### {current_q['q']}")
    
    # --- LOGIC FLOW ---
    
    # 1. If NOT submitted yet: Show Radio Buttons and Submit Button
    if not st.session_state.submitted:
        keys = list(current_q['opts'].keys())
        choice = st.radio(
            "Select your answer:", 
            keys, 
            format_func=lambda x: f"{x}. {current_q['opts'][x]}", 
            key=f"radio_{idx}",
            index=keys.index(st.session_state.selected) if st.session_state.selected else None
        )
        st.session_state.selected = choice
        
        st.markdown("<br>", unsafe_allow_html=True) # Spacer
        if st.button("✅ Submit Answer", type="primary"):
            if st.session_state.selected:
                st.session_state.submitted = True
                if st.session_state.selected == current_q['ans']:
                    st.session_state.score += 1
                st.rerun()
            else:
                st.warning("Please select an option before submitting.")

    # 2. If SUBMITTED: Show Color-Coded Options, Result, Explanation, and Next Button
    else:
        correct_ans = current_q['ans']
        user_ans = st.session_state.selected
        
        # Top Alert Banner
        if user_ans == correct_ans:
            st.success(f"✅ The answer you selected ({user_ans}) is correct!")
        else:
            st.error(f"❌ The answer you selected ({user_ans}) is incorrect. The correct answer is ({correct_ans}).")
            
        st.markdown("<br>", unsafe_allow_html=True)

        # Display Options as Styled Blocks
        for key in ["A", "B", "C", "D"]:
            opt_text = current_q['opts'][key]
            # Get specific explanation if available, otherwise use generic
            exp_text = current_q['exp'].get(key, "No specific explanation provided.")
            
            if key == correct_ans:
                # Correct Option Style (Dark Green Background, Green Text)
                html_block = f"""
                <div style="background-color: #1e2d1e; padding: 15px; border-radius: 8px; margin-bottom: 10px; border-left: 5px solid #00b894;">
                    <p style="color: #55efc4; font-weight: bold; font-size: 1.1em; margin-bottom: 5px;">{key}) {opt_text}</p>
                    <p style="color: #55efc4; font-size: 0.95em; margin-top: 0;">Correct – {exp_text}</p>
                </div>
                """
            else:
                # Incorrect Option Style (Dark Red/Brown Background, Red Text)
                # If this was the selected wrong answer, maybe make it slightly more distinct? 
                # The screenshot shows all wrong options looking similar (dark red).
                html_block = f"""
                <div style="background-color: #2d1e1e; padding: 15px; border-radius: 8px; margin-bottom: 10px; border-left: 5px solid #d63031;">
                    <p style="color: #ff7675; font-weight: bold; font-size: 1.1em; margin-bottom: 5px;">{key}) {opt_text}</p>
                    <p style="color: #ff7675; font-size: 0.95em; margin-top: 0;">Incorrect – {exp_text}</p>
                </div>
                """
            
            st.markdown(html_block, unsafe_allow_html=True)
            
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Next Question Button
        if idx < total - 1:
            if st.button("Next Question ➡️", use_container_width=True, type="secondary"):
                st.session_state.current_idx += 1
                st.session_state.selected = None
                st.session_state.submitted = False
                st.rerun()
        else:
            st.balloons()
            st.success(f"🏆 **Quiz Completed!** Your final score is **{st.session_state.score}** out of **{total}**.")
            if st.button("🔄 Start New Quiz", use_container_width=True):
                st.session_state.quiz_active = False
                st.rerun()
