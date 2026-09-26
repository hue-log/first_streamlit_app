import streamlit as st
import random

# ==========================================
# 1. QUESTIONS DATABASE (Sample 5 per Domain)
# ==========================================
QUESTIONS_DB = {
    "Domain 1: IS Auditing Process": [
        {"q": "The internal audit department wrote some scripts for continuous auditing. IT asked for copies to set up continuous monitoring. Should sharing these scripts be permitted?", "opts": {"A": "No, it gives IT the ability to pre-audit systems.", "B": "Yes, IT must review all programs regardless of independence.", "C": "Yes, if IT recognizes audits may cover areas not in the scripts.", "D": "No, IS auditors who wrote them cannot audit those systems."}, "ans": "C", "exp": "IS audit can still audit all aspects of the systems. IT's ability to continuously monitor does not affect IS audit's ability to perform a comprehensive audit."},
        {"q": "Which is the BEST factor for determining the required extent of data collection during the planning phase of an IS compliance audit?", "opts": {"A": "Complexity of the organization's operation", "B": "Findings and issues noted from the prior year", "C": "Purpose, objective and scope of the audit", "D": "Auditor's familiarity with the organization"}, "ans": "C", "exp": "The extent of data collection is directly related to the purpose, objective, and scope of the audit."},
        {"q": "What BEST describes the risk that information collected may contain a material error that may go undetected during IS auditing?", "opts": {"A": "Inherent risk", "B": "Audit risk", "C": "Control risk", "D": "Detection risk"}, "ans": "B", "exp": "Audit risk is the probability that reports may contain material errors and that the auditor may not detect them."},
        {"q": "For which controls would an IS auditor look in an environment where duties cannot be appropriately segregated?", "opts": {"A": "Overlapping controls", "B": "Boundary controls", "C": "Access controls", "D": "Compensating controls"}, "ans": "D", "exp": "Compensating controls reduce the risk of a control weakness when duties cannot be segregated."},
        {"q": "Which is the MOST critical step when planning an IS audit?", "opts": {"A": "Review findings from prior audits", "B": "Obtain executive management approval", "C": "Review infosec policies", "D": "Perform a risk assessment"}, "ans": "D", "exp": "Performing a risk assessment is the most critical step to ensure high-risk areas are identified for evaluation."}
    ],
    "Domain 2: Governance and Management of IT": [
        {"q": "Organizations requiring employees to take a mandatory vacation PRIMARILY want to ensure that:", "opts": {"A": "adequate cross-training exists.", "B": "an effective internal control environment is in place by increasing morale.", "C": "potential irregularities in processing are identified by a temporary replacement.", "D": "the risk of processing errors is reduced."}, "ans": "C", "exp": "Mandatory vacations help ensure that irregularities and fraud are detected by a temporary replacement."},
        {"q": "An IS auditor finds some IT policies have not been approved by management, but employees strictly follow them. What should the auditor do FIRST?", "opts": {"A": "Ignore the absence of approval.", "B": "Recommend immediate management approval.", "C": "Emphasize the importance of approval.", "D": "Report the absence of documented approval."}, "ans": "D", "exp": "Unapproved policies present a potential risk and may prevent management from enforcing them legally. The finding must be reported."},
        {"q": "What is the PRIMARY consideration for an IS auditor reviewing the prioritization of IT projects?", "opts": {"A": "Projects are aligned with the organization's strategy.", "B": "Identified project risk is monitored.", "C": "Controls related to planning are appropriate.", "D": "IT project metrics are reported accurately."}, "ans": "A", "exp": "IT projects must align with business strategy to add value and achieve intended results."},
        {"q": "In a review of HR policies, an IS auditor is MOST concerned with the absence of a:", "opts": {"A": "requirement for periodic job rotations.", "B": "process for formalized exit interviews.", "C": "termination checklist.", "D": "requirement for new employees to sign an NDA."}, "ans": "C", "exp": "A termination checklist is critical to ensure logical and physical security, preventing unauthorized access by former employees."},
        {"q": "Which factor is MOST critical when evaluating the effectiveness of an IT governance implementation?", "opts": {"A": "Ensure assurance objectives are defined.", "B": "Determine stakeholder requirements and involvement.", "C": "Identify relevant risk and opportunities.", "D": "Determine relevant enablers."}, "ans": "B", "exp": "Stakeholder needs and involvement form the basis for scoping IT governance and drive the success of the project."}
    ],
    "Domain 3: IS Acquisition, Development and Implementation": [
        {"q": "Who should review and approve system deliverables to ensure successful completion of a new business system?", "opts": {"A": "User management", "B": "Project steering committee", "C": "Senior management", "D": "Quality assurance (QA) staff"}, "ans": "A", "exp": "User management assumes ownership of the project and resulting system, and should review/approve deliverables."},
        {"q": "Which BEST helps to prioritize project activities and determine the timeline?", "opts": {"A": "Gantt chart", "B": "Earned value analysis", "C": "Program evaluation review technique (PERT)", "D": "Function point analysis"}, "ans": "C", "exp": "PERT calculates timelines based on worst, best, and normal scenarios, identifying the critical path."},
        {"q": "Implemented functionality often exceeded requirements and projects ran over budget. What is the MOST likely cause?", "opts": {"A": "Project scope management", "B": "Project time management", "C": "Project risk management", "D": "Project procurement management"}, "ans": "A", "exp": "Failure to effectively manage project scope leads to implementing more functionality than required (scope creep)."},
        {"q": "Which function is appropriate for end users to perform in software development?", "opts": {"A": "Program output testing", "B": "System configuration", "C": "Program logic specification", "D": "Performance tuning"}, "ans": "A", "exp": "Users can test program output by checking input vs output. Other options are too technical and violate separation of duties."},
        {"q": "Production data are used in the test environment. What is the MOST significant potential risk?", "opts": {"A": "Test environment may not ensure data accuracy.", "B": "Test environment may produce inaccurate results.", "C": "Hardware may not be identical.", "D": "Test environment may not have adequate access controls to ensure confidentiality."}, "ans": "D", "exp": "Test environments often lack production-level access controls, exposing sensitive production data to unauthorized access."}
    ],
    "Domain 4: IS Operations and Business Resilience": [
        {"q": "From an audit perspective, what is the MOST important item to review when considering a new IT service provider?", "opts": {"A": "References from other clients", "B": "Physical security of the site", "C": "The proposed service level agreement (SLA)", "D": "Background checks of employees"}, "ans": "C", "exp": "The SLA guarantees the provider will deliver services according to contract, including performance and security requirements."},
        {"q": "Which BEST describes the function of control self-assessment (CSA)?", "opts": {"A": "Quality control", "B": "Quality assessment", "C": "Quality planning", "D": "Quality assurance (QA)"}, "ans": "D", "exp": "CSA is a QA approach where the IS auditor acts as a consultant/facilitator to help business areas assess their own controls."},
        {"q": "An IS auditor reviewing a new outsourcing contract would be MOST concerned if which was missing?", "opts": {"A": "A clause providing a right to audit the service provider", "B": "A clause defining penalty payments", "C": "Predefined service level report templates", "D": "A clause regarding supplier limitation of liability"}, "ans": "A", "exp": "Without a right-to-audit clause, the IS auditor cannot investigate control deficiencies or compliance at the provider."},
        {"q": "When reviewing desktop software compliance, the IS auditor should be MOST concerned if installed software:", "opts": {"A": "is not documented in IT records.", "B": "is used by untrained users.", "C": "is not listed in the approved software standards document.", "D": "has a license expiring in 15 days."}, "ans": "C", "exp": "Installing unapproved software violates policy and introduces severe security, legal, and financial risks."},
        {"q": "Reviewing a cloud provider contract for patient health info. Which term is the GREATEST risk?", "opts": {"A": "Data ownership is retained by the customer.", "B": "The provider reserves the right to access data to perform certain operations.", "C": "Bulk data withdrawal mechanisms are undefined.", "D": "Customer is responsible for backup and restoration."}, "ans": "B", "exp": "Regulations may restrict third-party access to protected health info. The provider accessing data poses a major compliance risk."}
    ],
    "Domain 5: Protection of Information Assets": [
        {"q": "Web developers use hidden fields to save session info. The MOST likely web-based attack due to this is:", "opts": {"A": "parameter tampering.", "B": "cross-site scripting.", "C": "cookie poisoning.", "D": "stealth commanding."}, "ans": "A", "exp": "Attackers can intercept and modify hidden form fields (parameters) to perform unintended functions."},
        {"q": "Which control is the BEST way to ensure data in a file has not been changed during transmission?", "opts": {"A": "Reasonableness check", "B": "Parity bits", "C": "Hash values", "D": "Check digits"}, "ans": "C", "exp": "Hash values are highly sensitive to any changes in data, making them the best method to verify integrity."},
        {"q": "The PRIMARY purpose of audit trails is to:", "opts": {"A": "improve response time for users.", "B": "establish accountability for processed transactions.", "C": "improve operational efficiency.", "D": "provide information to auditors."}, "ans": "B", "exp": "Audit trails trace transactions through the system to establish accountability and responsibility."},
        {"q": "Which system can recognize a credit card transaction is MORE likely from a stolen card?", "opts": {"A": "Intrusion detection systems (IDS)", "B": "Data mining techniques", "C": "Stateful inspection firewalls", "D": "Packet filtering routers"}, "ans": "B", "exp": "Data mining detects trends/patterns. A change in historical charging patterns flags potential fraud."},
        {"q": "Which BEST ensures the integrity of a server's operating system?", "opts": {"A": "Protecting the server in a secure location", "B": "Setting a boot password", "C": "Hardening the server configuration", "D": "Implementing activity logging"}, "ans": "C", "exp": "Hardening (patching, disabling unused services, configuring access) prevents unauthorized privileged execution."}
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
    num_q = st.sidebar.slider("2. Number of Questions:", 1, max_q, min(10, max_q))
    
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

# --- MAIN AREA ---
st.title("🎓 CISA Exam Practice App")

if not st.session_state.quiz_active:
    st.info("👈 **Step 1:** Select your domains from the sidebar.\n\n👈 **Step 2:** Choose the number of questions.\n\n👈 **Step 3:** Click **Shuffle & Start Quiz** to begin!")
else:
    total = len(st.session_state.questions)
    idx = st.session_state.current_idx
    
    # Progress Bar
    st.progress((idx + 1) / total)
    st.markdown(f"### 📝 Question {idx + 1} of {total} &nbsp;&nbsp;|&nbsp;&nbsp; 🏆 Score: {st.session_state.score}/{idx}")
    
    current_q = st.session_state.questions[idx]
    st.markdown(f"#### {current_q['q']}")
    
    # Handle Question Logic
    if not st.session_state.submitted:
        # Radio buttons for options
        keys = list(current_q['opts'].keys())
        choice = st.radio("Select your answer:", keys, format_func=lambda x: f"{x}. {current_q['opts'][x]}", key=f"radio_{idx}")
        st.session_state.selected = choice
        
        if st.button("✅ Submit Answer", type="primary"):
            if st.session_state.selected:
                st.session_state.submitted = True
                if st.session_state.selected == current_q['ans']:
                    st.session_state.score += 1
                st.rerun()
            else:
                st.warning("Please select an option before submitting.")
    else:
        # Show Results & Explanation
        correct_ans = current_q['ans']
        user_ans = st.session_state.selected
        
        # Color-coded options
        for k, v in current_q['opts'].items():
            if k == correct_ans:
                bg, border, icon = "#d4edda", "#28a745", "✅"
            elif k == user_ans and k != correct_ans:
                bg, border, icon = "#f8d7da", "#dc3545", "❌"
            else:
                bg, border, icon = "#f8f9fa", "#cccccc", ""
                
            st.markdown(f"""
            <div style="background-color:{bg}; padding:12px; border-radius:6px; margin:6px 0; border-left: 5px solid {border};">
                <b>{icon} {k}.</b> {v}
            </div>
            """, unsafe_allow_html=True)
            
        # Feedback Summary
        if user_ans == correct_ans:
            st.success("🎉 **Correct!** Great job.")
        else:
            st.error(f"❌ **Incorrect.** The correct answer is **{correct_ans}**.")
            
        st.info(f"💡 **Explanation:** {current_q['exp']}")
        
        # Navigation
        if idx < total - 1:
            if st.button("Next Question ➡️", use_container_width=True):
                st.session_state.current_idx += 1
                st.session_state.selected = None
                st.session_state.submitted = False
                st.rerun()
        else:
            st.balloons()
            st.success(f"🏆 **Quiz Completed!** Your final score is **{st.session_state.score}** out of **{total}**.")
            if st.sidebar.button("🔙 Reset & Configure New Quiz"):
                st.session_state.quiz_active = False
                st.rerun()
