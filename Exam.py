import streamlit as st
import random

# ==========================================
# 1. QUESTIONS DATABASE
# ==========================================
# Note: The structure includes specific explanations for EACH option (A, B, C, D)
# so they can be shuffled along with the option text.

QUESTIONS_DB = {
    "Domain 1: IS Auditing Process": [
        {
            "q": "Which of the following is MOST useful for making risk treatment decisions?",
            "opts": {"A": "A control testing procedure", "B": "A control framework", "C": "A risk appetite statement", "D": "A security policy"},
            "ans": "C",
            "exp": {
                "A": "Control testing procedures are not related to risk treatment decisions.",
                "B": "An organization's control framework is not typically used for making risk treatment decisions.",
                "C": "A risk appetite statement provides guidance on the types of risk and the amount of risk an organization may be willing to accept versus what it prefers to mitigate, avoid, or transfer.",
                "D": "Security policy is not a primary means for making risk treatment decisions."
            }
        },
        {
            "q": "Which of the following is the BEST factor for determining the required extent of data collection during the planning phase of an IS compliance audit?",
            "opts": {"A": "Complexity of the organization's operation", "B": "Findings and issues noted from the prior year", "C": "Purpose, objective and scope of the audit", "D": "Auditor's familiarity with the organization"},
            "ans": "C",
            "exp": {
                "A": "The complexity of the organization's operation is a factor in planning but does not directly determine the extent of data collection.",
                "B": "Prior findings are factors in planning but do not directly determine the extent of data collection.",
                "C": "The extent to which data will be collected is related directly to the purpose, objective and scope of the audit.",
                "D": "An auditor's familiarity is a factor but the audit must be based on sufficient evidence, not familiarity."
            }
        },
        {
            "q": "What BEST describes the risk that information collected may contain a material error that may go undetected during IS auditing?",
            "opts": {"A": "Inherent risk", "B": "Audit risk", "C": "Control risk", "D": "Detection risk"},
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
            "opts": {"A": "adequate cross-training exists between functions.", "B": "an effective internal control environment is in place by increasing morale.", "C": "potential irregularities in processing are identified by a temporary replacement.", "D": "the risk of processing errors is reduced."},
            "ans": "C",
            "exp": {
                "A": "Cross-training is good practice but can be achieved without mandatory vacation.",
                "B": "Good morale is worthwhile but not a means to achieve an effective internal control system.",
                "C": "Employees in critical functions should take time off to help ensure irregularities and fraud are detected by a replacement.",
                "D": "Rotating employees can reduce errors, but this is not the primary reason for mandatory vacation."
            }
        },
        {
            "q": "Which of the following factors is MOST critical when evaluating the effectiveness of an IT governance implementation?",
            "opts": {"A": "Ensure assurance objectives are defined.", "B": "Determine stakeholder requirements and involvement.", "C": "Identify relevant risk and opportunities.", "D": "Determine relevant enablers."},
            "ans": "B",
            "exp": {
                "A": "Stakeholder needs form the basis for scoping and defining assurance objectives.",
                "B": "The most critical factor is to determine stakeholder requirements and involvement. This drives the success of the project.",
                "C": "Relevant risk and opportunities are identified and driven by the assurance objectives.",
                "D": "Relevant enablers are considered based on assurance objectives."
            }
        }
    ],
    "Domain 3: IS Acquisition, Development and Implementation": [
        {
            "q": "Who should review and approve system deliverables to ensure successful completion of a new business system?",
            "opts": {"A": "User management", "B": "Project steering committee", "C": "Senior management", "D": "Quality assurance (QA) staff"},
            "ans": "A",
            "exp": {
                "A": "User management assumes ownership of the project and resulting system, and should review/approve deliverables.",
                "B": "A project steering committee provides overall direction and is ultimately responsible for deliverables, but user management approves them as they are defined.",
                "C": "Senior management demonstrates commitment and approves resources, but not specific deliverables.",
                "D": "QA staff review results within each phase to confirm compliance, but do not approve deliverables for the business."
            }
        },
        {
            "q": "Which BEST helps to prioritize project activities and determine the timeline?",
            "opts": {"A": "Gantt chart", "B": "Earned value analysis", "C": "Program evaluation review technique (PERT)", "D": "Function point analysis"},
            "ans": "C",
            "exp": {
                "A": "A Gantt chart shows timeline and status but is not as effective as PERT for prioritizing.",
                "B": "Earned value analysis tracks cost versus deliverables but does not assist in prioritizing tasks.",
                "C": "PERT calculates timelines based on worst, best, and normal scenarios, identifying the critical path.",
                "D": "Function point analysis measures complexity of input/output and does not help prioritize activities."
            }
        }
    ],
    "Domain 4: IS Operations and Business Resilience": [
        {
            "q": "From an audit perspective, what is the MOST important item to review when considering a new IT service provider?",
            "opts": {"A": "References from other clients", "B": "Physical security of the site", "C": "The proposed service level agreement (SLA)", "D": "Background checks of employees"},
            "ans": "C",
            "exp": {
                "A": "Reviewing references is good practice, but the SLA is most critical because it defines required performance levels.",
                "B": "Reviewing physical security is good practice, but the SLA is most critical.",
                "C": "An SLA is a guarantee that the provider will deliver services according to the contract. The IS auditor must ensure performance and security requirements are clearly stated.",
                "D": "Background checks are good practice, but the SLA is most critical."
            }
        },
        {
            "q": "Which of the following is the MOST critical element to execute a disaster recovery plan (DRP) effectively?",
            "opts": {"A": "Offsite storage of backup data", "B": "Up-to-date list of key disaster recovery contacts", "C": "Availability of a replacement data center", "D": "Clearly defined recovery time objective"},
            "ans": "A",
            "exp": {
                "A": "Remote storage of backups is the most critical DRP element because access to backup data is required to restore systems.",
                "B": "Having a list of key contacts is important but not as important as having adequate data backup.",
                "C": "A DRP may use a replacement data center or some other solution, but data is the core element.",
                "D": "Having a clearly defined RTO is important for BCP, but the core element of DR is data backup."
            }
        }
    ],
    "Domain 5: Protection of Information Assets": [
        {
            "q": "Web developers use hidden fields to save session info. The MOST likely web-based attack due to this is:",
            "opts": {"A": "parameter tampering.", "B": "cross-site scripting.", "C": "cookie poisoning.", "D": "stealth commanding."},
            "ans": "A",
            "exp": {
                "A": "Attackers can intercept and modify hidden form fields (parameters) to perform unintended functions.",
                "B": "Cross-site scripting involves compromising the web page to redirect users, unrelated to hidden fields.",
                "C": "Cookie poisoning refers to the interception and modification of session cookies, not hidden fields.",
                "D": "Stealth commanding is the hijacking of a web server by installing unauthorized code."
            }
        },
        {
            "q": "Which control is the BEST way to ensure data in a file has not been changed during transmission?",
            "opts": {"A": "Reasonableness check", "B": "Parity bits", "C": "Hash values", "D": "Check digits"},
            "ans": "C",
            "exp": {
                "A": "A reasonableness check ensures input data is within expected values, not transmission integrity.",
                "B": "Parity bits are a weak form of data integrity check, not as good as a hash.",
                "C": "Hash values are calculated on the file and are very sensitive to any changes in the data values, making them the best way to ensure integrity.",
                "D": "Check digits detect errors in numeric fields like account numbers, usually related to transposition errors."
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
st.sidebar.title("️ Quiz Settings")
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
    
    # --- QUIZ INITIALIZATION & SHUFFLING LOGIC ---
    if st.sidebar.button("🔄 Shuffle & Start Quiz", use_container_width=True, type="primary"):
        # 1. Randomly select questions from the pool
        raw_questions = random.sample(pool, num_q)
        shuffled_quiz = []
        labels = ['A', 'B', 'C', 'D']
        
        # 2. Shuffle the options for each selected question
        for q in raw_questions:
            correct_key = q['ans']
            
            # Bundle option text, explanation, and correct flag
            opts_list = [
                {'text': v, 'exp': q['exp'].get(k, ''), 'is_correct': (k == correct_key)} 
                for k, v in q['opts'].items()
            ]
            random.shuffle(opts_list)
            
            new_opts = {}
            new_exps = {}
            new_ans = ''
            
            # 3. Re-assign A, B, C, D labels to the shuffled options
            for i, item in enumerate(opts_list):
                label = labels[i]
                new_opts[label] = item['text']
                new_exps[label] = item['exp']
                if item['is_correct']:
                    new_ans = label
                    
            shuffled_quiz.append({
                'q': q['q'],
                'opts': new_opts,
                'ans': new_ans,
                'exp': new_exps
            })
            
        # Update session state
        st.session_state.questions = shuffled_quiz
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
    st.markdown(f"###  Question {idx + 1} of {total} &nbsp;&nbsp;|&nbsp;&nbsp; 🏆 Score: {st.session_state.score}/{idx}")
    
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
            st.error(f" The answer you selected ({user_ans}) is incorrect. The correct answer is ({correct_ans}).")
            
        st.markdown("<br>", unsafe_allow_html=True)

        # Display Options as Styled Blocks
        for key in ["A", "B", "C", "D"]:
            opt_text = current_q['opts'][key]
            exp_text = current_q['exp'].get(key, "No specific explanation provided.")
            
            if key == correct_ans:
                html_block = f"""
                <div style="background-color: #1e2d1e; padding: 15px; border-radius: 8px; margin-bottom: 10px; border-left: 5px solid #00b894;">
                    <p style="color: #55efc4; font-weight: bold; font-size: 1.1em; margin-bottom: 5px;">{key}) {opt_text}</p>
                    <p style="color: #55efc4; font-size: 0.95em; margin-top: 0;">Correct – {exp_text}</p>
                </div>
                """
            else:
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
