import streamlit as st
import random
import json

# --- Comprehensive CISA Question Bank ---
# Questions extracted and structured from the provided CISA exam preparation materials

question_bank = [
    {
        "id": 1,
        "question": "The purpose of business continuity planning and disaster-recovery planning is to:",
        "options": [
            "A) Transfer the risk and impact of a business interruption or disaster",
            "B) Mitigate, or reduce, the risk and impact of a business interruption or disaster",
            "C) Accept the risk and impact of a business",
            "D) Eliminate the risk and impact of a business interruption or disaster"
        ],
        "correct": "B",
        "explanation": "The primary purpose of business continuity planning (BCP) and disaster recovery planning (DRP) is to mitigate, or reduce, the risk and impact of a business interruption or disaster. Complete elimination of risk is not possible."
    },
    {
        "id": 2,
        "question": "If a database is restored from information backed up before the last system image, which of the following is recommended?",
        "options": [
            "A) The system should be restarted after the last transaction.",
            "B) The system should be restarted before the last transaction.",
            "C) The system should be restarted at the first transaction.",
            "D) The system should be restarted on the last transaction."
        ],
        "correct": "B",
        "explanation": "If a database is restored from information backed up before the last system image, the system should be restarted before the last transaction so that the final transaction can be reprocessed."
    },
    {
        "id": 3,
        "question": "An off-site processing facility should be easily identifiable externally because easy identification helps ensure smoother recovery. True or false?",
        "options": [
            "A) True",
            "B) False"
        ],
        "correct": "B",
        "explanation": "An off-site processing facility should NOT be easily identifiable externally as this would make it vulnerable to sabotage or attacks."
    },
    {
        "id": 4,
        "question": "Which of the following is the dominating objective of BCP and DRP?",
        "options": [
            "A) To protect human life",
            "B) To mitigate the risk and impact of a business interruption",
            "C) To eliminate the risk and impact of a business interruption",
            "D) To transfer the risk and impact of a business interruption"
        ],
        "correct": "A",
        "explanation": "Although mitigating the risk and impact of a business interruption is important, the overriding priority in BCP and DRP is always the protection of human life."
    },
    {
        "id": 5,
        "question": "How can minimizing single points of failure or vulnerabilities of a common disaster best be controlled?",
        "options": [
            "A) By implementing redundant systems and applications onsite",
            "B) By geographically dispersing resources",
            "C) By retaining onsite data backup in fireproof vaults",
            "D) By preparing BCP and DRP documents for commonly identified disasters"
        ],
        "correct": "B",
        "explanation": "Geographically dispersing resources reduces the risk of a common disaster affecting all systems, thus mitigating vulnerabilities related to single points of failure."
    },
    {
        "id": 6,
        "question": "Mitigating the risk and impact of a disaster or business interruption usually takes priority over transference of risk to a third party such as an insurer. True or false?",
        "options": [
            "A) True",
            "B) False"
        ],
        "correct": "A",
        "explanation": "Mitigating the risk and impact of a disaster generally takes priority over transferring risk to an insurer because reducing the risk directly affects the organization's ability to continue operations."
    },
    {
        "id": 7,
        "question": "Off-site data storage should be kept synchronized when preparing for recovery of time-sensitive data such as that resulting from which of the following?",
        "options": [
            "A) Financial reporting",
            "B) Sales reporting",
            "C) Inventory reporting",
            "D) Transaction processing"
        ],
        "correct": "D",
        "explanation": "Time-sensitive data such as transaction processing data must be synchronized with off-site backups to ensure accurate recovery."
    },
    {
        "id": 8,
        "question": "What is an acceptable recovery mechanism for extremely time-sensitive transaction processing?",
        "options": [
            "A) Off-site remote journaling",
            "B) Electronic vaulting",
            "C) Shadow file processing",
            "D) Storage area network"
        ],
        "correct": "C",
        "explanation": "Shadow file processing is an effective recovery mechanism for extremely time-sensitive transaction processing because it allows data to be mirrored and recovered quickly."
    },
    {
        "id": 9,
        "question": "Off-site data backup and storage should be geographically separated so as to _____ the risk of a widespread physical disaster such as a hurricane or earthquake.",
        "options": [
            "A) Accept",
            "B) Eliminate",
            "C) Transfer",
            "D) Mitigate"
        ],
        "correct": "D",
        "explanation": "Off-site backups should be geographically separated to mitigate the risk of widespread disasters such as earthquakes or hurricanes."
    },
    {
        "id": 10,
        "question": "Why is a clause for requiring source code escrow in an application vendor agreement important?",
        "options": [
            "A) To segregate systems development and live environments",
            "B) To protect the organization from copyright disputes",
            "C) To ensure that sufficient code is available when needed",
            "D) To ensure that the source code remains available even if the application vendor goes out of business"
        ],
        "correct": "D",
        "explanation": "A source code escrow ensures that the organization has access to the source code if the vendor goes out of business, allowing them to maintain and modify the application."
    },
    {
        "id": 11,
        "question": "What uses questionnaires to lead the user through a series of choices to reach a conclusion?",
        "options": [
            "A) Logic trees",
            "B) Decision trees",
            "C) Decision algorithms",
            "D) Logic algorithms"
        ],
        "correct": "B",
        "explanation": "Decision trees use a series of questions or choices to guide users to a conclusion, making them useful for decision-making processes."
    },
    {
        "id": 12,
        "question": "What protects an application purchaser's ability to fix or change an application in case the application vendor goes out of business?",
        "options": [
            "A) Assigning copyright to the organization",
            "B) Program back doors",
            "C) Source code escrow",
            "D) Internal programming expertise"
        ],
        "correct": "C",
        "explanation": "Source code escrow protects the organization by ensuring they can access and modify the source code if the vendor goes out of business."
    },
    {
        "id": 13,
        "question": "Who is ultimately responsible for providing requirement specifications to the software development team?",
        "options": [
            "A) The project sponsor",
            "B) The project members",
            "C) The project leader",
            "D) The project steering committee"
        ],
        "correct": "A",
        "explanation": "The project sponsor is responsible for ensuring that the requirement specifications are provided to the software development team."
    },
    {
        "id": 14,
        "question": "What should regression testing use to obtain accurate conclusions regarding the effects of changes or corrections to a program?",
        "options": [
            "A) Contrived data",
            "B) Independently created data",
            "C) Live data",
            "D) Data from previous tests"
        ],
        "correct": "D",
        "explanation": "Regression testing should use data from previous tests to ensure accurate conclusions about the effects of program changes or corrections."
    },
    {
        "id": 15,
        "question": "An IS auditor should carefully review the functional requirements in a systems-development project to ensure that the project is designed to:",
        "options": [
            "A) Meet business objectives",
            "B) Enforce data security",
            "C) Be culturally feasible",
            "D) Be financially feasible"
        ],
        "correct": "A",
        "explanation": "The primary role of an IS auditor is to ensure that the system is designed to meet the business objectives of the project."
    },
    {
        "id": 16,
        "question": "Which of the following processes are performed during the design phase of the systems-development life cycle (SDLC) model?",
        "options": [
            "A) Develop test plans.",
            "B) Baseline procedures to prevent scope creep.",
            "C) Define the need that requires resolution and map to the major requirements of the solution.",
            "D) Program and test the new system."
        ],
        "correct": "B",
        "explanation": "Procedures to prevent scope creep are established during the design phase of the SDLC to ensure the project stays within its defined boundaries."
    },
    {
        "id": 17,
        "question": "When should application controls be considered within the system-development process?",
        "options": [
            "A) After application unit testing",
            "B) After application module testing",
            "C) After application systems testing",
            "D) As early as possible, even in the development of the project's functional specifications"
        ],
        "correct": "D",
        "explanation": "Application controls should be considered as early as possible in the system development process, even during the creation of the project's functional specifications."
    },
    {
        "id": 18,
        "question": "What is used to develop strategically important systems faster, reduce development costs, and still maintain high quality?",
        "options": [
            "A) Rapid application development (RAD)",
            "B) GANTT",
            "C) PERT",
            "D) Decision trees"
        ],
        "correct": "A",
        "explanation": "Rapid Application Development (RAD) is a methodology used to develop strategically important systems faster, reduce costs, and maintain quality."
    },
    {
        "id": 19,
        "question": "Test and development environments should be separated. True or false?",
        "options": [
            "A) True",
            "B) False"
        ],
        "correct": "A",
        "explanation": "Test and development environments should be separated to maintain the stability and integrity of testing processes."
    },
    {
        "id": 20,
        "question": "What kind of testing should programmers perform following any changes to an application or system?",
        "options": [
            "A) Unit, module, and full regression testing",
            "B) Module testing",
            "C) Unit testing",
            "D) Regression testing"
        ],
        "correct": "A",
        "explanation": "Following any changes to an application or system, programmers should perform unit, module, and full regression testing to ensure the changes work as intended and do not introduce new issues."
    },
    {
        "id": 21,
        "question": "Which of the following uses a prototype that can be updated continually to meet changing user or business requirements?",
        "options": [
            "A) PERT",
            "B) Rapid application development (RAD)",
            "C) Function point analysis (FPA)",
            "D) GANTT"
        ],
        "correct": "B",
        "explanation": "Rapid Application Development (RAD) focuses on continuous iterations and updating prototypes to meet changing user or business requirements."
    },
    {
        "id": 22,
        "question": "What is the most common reason for information systems to fail to meet the needs of users?",
        "options": [
            "A) Lack of funding",
            "B) Inadequate user participation during system requirements definition",
            "C) Inadequate senior management participation during system requirements definition",
            "D) Poor IT strategic planning"
        ],
        "correct": "B",
        "explanation": "The most common reason for systems failing to meet user needs is inadequate user participation during the requirements definition phase."
    },
    {
        "id": 23,
        "question": "Who is responsible for the overall direction, costs, and timetables for systems-development projects?",
        "options": [
            "A) The project sponsor",
            "B) The project steering committee",
            "C) Senior management",
            "D) The project team leader"
        ],
        "correct": "B",
        "explanation": "The project steering committee is tasked with overseeing the overall direction, budgets, and schedules of systems-development projects."
    },
    {
        "id": 24,
        "question": "When should plans for testing for user acceptance be prepared?",
        "options": [
            "A) In the requirements definition phase of the systems-development project",
            "B) In the feasibility phase of the systems-development project",
            "C) In the design phase of the systems-development project",
            "D) In the development phase of the systems-development project"
        ],
        "correct": "A",
        "explanation": "User acceptance testing (UAT) should be planned early, usually during the requirements definition phase, to ensure the system meets business needs."
    },
    {
        "id": 25,
        "question": "Above almost all other concerns, what often results in the greatest negative impact on the implementation of new application software?",
        "options": [
            "A) Failing to perform user acceptance testing",
            "B) Lack of user training for the new system",
            "C) Lack of software documentation and run manuals",
            "D) Insufficient unit, module, and systems testing"
        ],
        "correct": "A",
        "explanation": "Failing to perform user acceptance testing (UAT) often has the most significant negative impact on the successful implementation of new software."
    },
    {
        "id": 26,
        "question": "Input/output controls should be implemented for which applications in an integrated systems environment?",
        "options": [
            "A) The receiving application",
            "B) The sending application",
            "C) Both the sending and receiving applications",
            "D) Output on the sending application and input on the receiving application"
        ],
        "correct": "C",
        "explanation": "Input/output controls should be implemented on both sending and receiving applications to ensure data accuracy and completeness in an integrated environment."
    },
    {
        "id": 27,
        "question": "Authentication techniques for sending and receiving data between EDI systems are crucial to prevent which of the following?",
        "options": [
            "A) Unsynchronized transactions",
            "B) Unauthorized transactions",
            "C) Inaccurate transactions",
            "D) Incomplete transactions"
        ],
        "correct": "B",
        "explanation": "Authentication is essential in Electronic Data Interchange (EDI) systems to prevent unauthorized transactions."
    },
    {
        "id": 28,
        "question": "After identifying potential security vulnerabilities, what should be the IS auditor's next step?",
        "options": [
            "A) To evaluate potential countermeasures and compensatory controls",
            "B) To implement effective countermeasures and compensatory controls",
            "C) To perform a business impact analysis of the threats that would exploit the vulnerabilities",
            "D) To immediately advise senior management of the findings"
        ],
        "correct": "C",
        "explanation": "Once vulnerabilities are identified, the IS auditor should conduct a business impact analysis (BIA) to understand the threats and prioritize their mitigation."
    },
    {
        "id": 29,
        "question": "What is the primary security concern for EDI environments?",
        "options": [
            "A) Transaction authentication",
            "B) Transaction completeness",
            "C) Transaction accuracy",
            "D) Transaction authorization"
        ],
        "correct": "D",
        "explanation": "In EDI environments, transaction authorization is the primary security concern to ensure that only authorized parties can initiate transactions."
    },
    {
        "id": 30,
        "question": "Which of the following exploit vulnerabilities to cause loss or damage to the organization and its assets?",
        "options": [
            "A) Exposures",
            "B) Threats",
            "C) Hazards",
            "D) Insufficient controls"
        ],
        "correct": "B",
        "explanation": "Threats exploit vulnerabilities, leading to potential loss or damage to the organization's assets."
    },
    {
        "id": 31,
        "question": "Business process re-engineering often results in _____ automation, which results in _____ number of people using technology.",
        "options": [
            "A) Increased; a greater",
            "B) Increased; a fewer",
            "C) Less; a fewer",
            "D) Increased; the same"
        ],
        "correct": "A",
        "explanation": "Business process re-engineering typically increases automation, which leads to a greater number of people relying on technology."
    },
    {
        "id": 32,
        "question": "Whenever business processes have been re-engineered, the IS auditor attempts to identify and quantify the impact of any controls that might have been removed. True or false?",
        "options": [
            "A) True",
            "B) False"
        ],
        "correct": "A",
        "explanation": "It is crucial for the IS auditor to assess the impact on controls when business processes are reengineered, as this can affect the effectiveness of existing controls."
    },
    {
        "id": 33,
        "question": "When should an application-level edit check to verify availability of funds be completed at the electronic funds transfer (EFT) interface?",
        "options": [
            "A) Before transaction completion",
            "B) Immediately after an EFT is initiated",
            "C) During run-to-run total testing",
            "D) Before an EFT is initiated"
        ],
        "correct": "D",
        "explanation": "The availability of funds should be verified before initiating an EFT to ensure the transaction can be completed successfully."
    },
    {
        "id": 34,
        "question": "_____ should be implemented as early as data preparation to support data integrity at the earliest point possible.",
        "options": [
            "A) Control totals",
            "B) Authentication controls",
            "C) Parity bits",
            "D) Authorization controls"
        ],
        "correct": "A",
        "explanation": "Control totals are used to support data integrity by ensuring that data processed matches expected values from the earliest stages of data preparation."
    },
    {
        "id": 35,
        "question": "What is used as a control to detect loss, corruption, or duplication of data?",
        "options": [
            "A) Redundancy check",
            "B) Reasonableness check",
            "C) Hash totals",
            "D) Accuracy check"
        ],
        "correct": "C",
        "explanation": "Hash totals are used to verify the integrity of data and detect any loss, corruption, or duplication during processing."
    },
    {
        "id": 36,
        "question": "Data edits are implemented before processing and are considered which of the following?",
        "options": [
            "A) Deterrent integrity controls",
            "B) Detective integrity controls",
            "C) Corrective integrity controls",
            "D) Preventative integrity controls"
        ],
        "correct": "D",
        "explanation": "Data edits, which are designed to check the accuracy and validity of data before processing, are considered preventive controls."
    },
    {
        "id": 37,
        "question": "Processing controls ensure that data is accurate and complete, and is processed only through which of the following?",
        "options": [
            "A) Documented routines",
            "B) Authorized routines",
            "C) Accepted routines",
            "D) Approved routines"
        ],
        "correct": "B",
        "explanation": "Processing controls ensure that data is only processed through authorized routines to maintain accuracy and completeness."
    },
    {
        "id": 38,
        "question": "What is a data validation edit control that matches input data to an occurrence rate?",
        "options": [
            "A) Accuracy check",
            "B) Completeness check",
            "C) Reasonableness check",
            "D) Redundancy check"
        ],
        "correct": "C",
        "explanation": "A reasonableness check ensures that the input data is logical and within an expected range based on occurrence rates or other parameters."
    },
    {
        "id": 39,
        "question": "Database snapshots can provide an excellent audit trail for an IS auditor. True or false?",
        "options": [
            "A) True",
            "B) False"
        ],
        "correct": "A",
        "explanation": "Database snapshots capture the state of a database at a specific point in time, offering an effective audit trail for tracking changes."
    },
    {
        "id": 40,
        "question": "An IS auditor is using a statistical sample to inventory the tape library. What type of test would this be considered?",
        "options": [
            "A) Substantive",
            "B) Compliance",
            "C) Integrated",
            "D) Continuous audit"
        ],
        "correct": "A",
        "explanation": "Using statistical sampling to inventory the tape library is an example of a substantive test, which aims to gather evidence about the completeness and accuracy of an asset inventory."
    },
    {
        "id": 41,
        "question": "An IS auditor is reviewing access to an application to determine whether the 10 most recent 'new user' forms were correctly authorized. This is an example of:",
        "options": [
            "A) Variable sampling",
            "B) Substantive testing",
            "C) Compliance testing",
            "D) Stop-or-go sampling"
        ],
        "correct": "C",
        "explanation": "Compliance testing is used to verify if controls are being followed in line with policies and procedures."
    },
    {
        "id": 42,
        "question": "The decisions and actions of an IS auditor are MOST likely to affect which of the following risks?",
        "options": [
            "A) Inherent",
            "B) Detection",
            "C) Control",
            "D) Business"
        ],
        "correct": "B",
        "explanation": "Detection risk refers to the risk that the auditor's procedures will not detect material issues or errors. This risk is directly influenced by the auditor's choice of audit procedures."
    },
    {
        "id": 43,
        "question": "Overall business risk for a particular threat can be expressed as:",
        "options": [
            "A) A product of the probability and magnitude of the impact if a threat successfully exploits a vulnerability.",
            "B) The magnitude of the impact should a threat source successfully exploit the vulnerability.",
            "C) The likelihood of a given threat source exploiting a given vulnerability.",
            "D) The collective judgment of the risk assessment team."
        ],
        "correct": "A",
        "explanation": "Business risk is best expressed as the combination of both the likelihood of the threat and the magnitude of its impact."
    },
    {
        "id": 44,
        "question": "Which of the following is a substantive test?",
        "options": [
            "A) Checking a list of exception reports",
            "B) Ensuring approval for parameter changes",
            "C) Using a statistical sample to inventory the tape library",
            "D) Reviewing password history reports"
        ],
        "correct": "C",
        "explanation": "Substantive testing focuses on the accuracy and integrity of actual transactions or records, such as verifying the existence of items in the tape library."
    },
    {
        "id": 45,
        "question": "Which of the following is a benefit of a risk-based approach to audit planning?",
        "options": [
            "A) Audit scheduling may be performed months in advance.",
            "B) Budgets are more likely to be met by the IS audit staff.",
            "C) Staff will be exposed to a variety of technologies.",
            "D) Resources are allocated to the areas of highest concern."
        ],
        "correct": "D",
        "explanation": "The risk-based approach ensures that audit resources are directed to areas with the highest risks, which delivers the most value."
    },
    {
        "id": 46,
        "question": "An audit charter should:",
        "options": [
            "A) Be dynamic and change often to coincide with the changing nature of technology.",
            "B) Clearly state audit objectives and delegation of authority.",
            "C) Document the audit procedures designed to achieve planned audit objectives.",
            "D) Outline the overall authority, scope, and responsibilities of the audit function."
        ],
        "correct": "D",
        "explanation": "An audit charter defines the audit function's role, authority, scope, and responsibilities at a high level."
    },
    {
        "id": 47,
        "question": "The MAJOR advantage of the risk assessment approach over the baseline approach to information security management is that it ensures:",
        "options": [
            "A) Information assets are overprotected.",
            "B) A basic level of protection is applied regardless of asset value.",
            "C) Appropriate levels of protection are applied to information assets.",
            "D) An equal proportion of resources are devoted to protecting all information assets."
        ],
        "correct": "C",
        "explanation": "The risk assessment approach ensures that protection is proportional to the value and risk associated with each asset."
    },
    {
        "id": 48,
        "question": "Which of the following sampling methods is MOST useful when testing for compliance?",
        "options": [
            "A) Attribute sampling",
            "B) Variable sampling",
            "C) Stratified mean per unit",
            "D) Difference estimation"
        ],
        "correct": "A",
        "explanation": "Attribute sampling is used to test whether a specific control is present or absent in compliance testing."
    },
    {
        "id": 49,
        "question": "Which of the following is the MOST likely reason why e-mail systems have become a useful source of evidence for litigation?",
        "options": [
            "A) Multiple cycles of backup files remain available.",
            "B) Access controls establish accountability for e-mail activity.",
            "C) Data classification regulates what information should be communicated via e-mail.",
            "D) A clear policy for using e-mail ensures that evidence is available."
        ],
        "correct": "A",
        "explanation": "E-mail backup files often retain data even after it has been deleted by users, making them a valuable source of evidence."
    },
    {
        "id": 50,
        "question": "An IS auditor is assigned to perform a post-implementation review of an application system. Which situation may have impaired the independence of the IS auditor?",
        "options": [
            "A) The IS auditor implemented a specific control during the development of the application system.",
            "B) The IS auditor designed an embedded audit module exclusively for auditing the application system.",
            "C) The IS auditor participated as a member of the application system project team but did not have operational responsibilities.",
            "D) The IS auditor provided consulting advice concerning application system best practices."
        ],
        "correct": "A",
        "explanation": "Independence is impaired if the IS auditor was directly involved in developing or implementing the system they are reviewing."
    },
    {
        "id": 51,
        "question": "The PRIMARY advantage of a continuous audit approach is that it:",
        "options": [
            "A) Does not require an IS auditor to collect evidence on system reliability while processing is taking place.",
            "B) Requires the IS auditor to review and follow up immediately on all information collected.",
            "C) Can improve system security when used in time-sharing environments that process a large number of transactions.",
            "D) Does not depend on the complexity of an organization's computer systems."
        ],
        "correct": "C",
        "explanation": "Continuous auditing is particularly beneficial in environments with high transaction volumes, allowing for ongoing monitoring and quick detection of issues."
    },
    {
        "id": 52,
        "question": "The PRIMARY purpose of audit trails is to:",
        "options": [
            "A) Improve response time for users.",
            "B) Establish accountability and responsibility for processed transactions.",
            "C) Improve the operational efficiency of the system.",
            "D) Provide useful information to auditors who may wish to track transactions."
        ],
        "correct": "B",
        "explanation": "Audit trails are primarily used to establish accountability and track responsibility for transactions."
    },
    {
        "id": 53,
        "question": "To ensure that audit resources deliver the best value to the organization, the FIRST step would be to:",
        "options": [
            "A) Schedule the audits and monitor the time spent on each audit.",
            "B) Train the IS audit staff on current technology used in the company.",
            "C) Develop the audit plan on the basis of a detailed risk assessment.",
            "D) Monitor progress of audits and initiate cost control measures."
        ],
        "correct": "C",
        "explanation": "Developing the audit plan based on a thorough risk assessment ensures that resources are focused on the most critical areas."
    },
    {
        "id": 54,
        "question": "An organization's IS audit charter should specify the:",
        "options": [
            "A) Short- and long-term plans for IS audit engagements.",
            "B) Objectives and scope of IS audit engagements.",
            "C) Detailed training plan for the IS audit staff.",
            "D) Role of the IS audit function."
        ],
        "correct": "D",
        "explanation": "The IS audit charter defines the role, scope, and authority of the audit function within the organization."
    },
    {
        "id": 55,
        "question": "An IS auditor is evaluating management's risk assessment of information systems. The IS auditor should FIRST review:",
        "options": [
            "A) The controls already in place.",
            "B) The effectiveness of the controls in place.",
            "C) The mechanism for monitoring the risks related to the assets.",
            "D) The threats/vulnerabilities affecting the assets."
        ],
        "correct": "D",
        "explanation": "The first step in evaluating a risk assessment is understanding the threats and vulnerabilities that could impact the information systems."
    },
    {
        "id": 56,
        "question": "In planning an audit, the MOST critical step is the identification of the:",
        "options": [
            "A) Areas of high risk.",
            "B) Skill sets of the audit staff.",
            "C) Test steps in the audit.",
            "D) Time allotted for the audit."
        ],
        "correct": "A",
        "explanation": "Identifying the areas of highest risk is the most critical step in audit planning."
    },
    {
        "id": 57,
        "question": "During the planning stage of an IS audit, the PRIMARY goal of an IS auditor is to:",
        "options": [
            "A) Address audit objectives",
            "B) Collect sufficient evidence",
            "C) Specify appropriate tests",
            "D) Minimize audit resources"
        ],
        "correct": "A",
        "explanation": "ISACA auditing standards require an IS auditor to plan the audit work to address the audit objectives."
    },
    {
        "id": 58,
        "question": "When selecting audit procedures, an IS auditor should use professional judgment to ensure that:",
        "options": [
            "A) Sufficient evidence will be collected",
            "B) All significant deficiencies identified will be corrected within a reasonable period",
            "C) All material weaknesses will be identified",
            "D) Audit costs will be kept at a minimum level"
        ],
        "correct": "A",
        "explanation": "An IS auditor should use professional judgment to ensure that sufficient and appropriate evidence will be collected during the audit."
    },
    {
        "id": 59,
        "question": "An IS auditor evaluating logical access controls should FIRST:",
        "options": [
            "A) Document the controls applied to the potential access paths to the system",
            "B) Test controls over the access paths to determine if they are functional",
            "C) Evaluate the security environment in relation to written policies and practices",
            "D) Obtain an understanding of the security risks to information processing"
        ],
        "correct": "D",
        "explanation": "The IS auditor should first understand the security risks to information processing by reviewing relevant documentation and conducting a risk assessment."
    },
    {
        "id": 60,
        "question": "The PRIMARY purpose of an IT forensic audit is:",
        "options": [
            "A) To participate in investigations related to corporate fraud",
            "B) The systematic collection of evidence after a system irregularity",
            "C) To assess the correctness of an organization's financial statements",
            "D) To determine that there has been criminal activity"
        ],
        "correct": "B",
        "explanation": "An IT forensic audit focuses on the systematic collection of evidence after a system irregularity."
    },
    {
        "id": 61,
        "question": "An IS auditor is performing an audit of a remotely managed server backup. The IS auditor reviews the logs for one day and finds one case where logging on a server has failed. What should the auditor do?",
        "options": [
            "A) Issue an audit finding",
            "B) Seek an explanation from IS management",
            "C) Review the classifications of data held on the server",
            "D) Expand the sample of logs reviewed"
        ],
        "correct": "D",
        "explanation": "The auditor should expand the sample to gather more evidence before making conclusions."
    },
    {
        "id": 62,
        "question": "Which of the following tools are MOST suitable for discovering potential anomalies in user or system behavior from audit trails?",
        "options": [
            "A) CASE tools",
            "B) Embedded data collection tools",
            "C) Heuristic scanning tools",
            "D) Trend/variance detection tools"
        ],
        "correct": "D",
        "explanation": "Trend/variance detection tools are used to analyze audit trails for anomalies in user or system behavior."
    },
    {
        "id": 63,
        "question": "An IS auditor is evaluating a corporate network for possible penetration by employees. Which finding should give the IS auditor the GREATEST concern?",
        "options": [
            "A) There are a number of external modems connected to the network",
            "B) Users can install software on their desktops",
            "C) Network monitoring is very limited",
            "D) Many user IDs have identical passwords"
        ],
        "correct": "D",
        "explanation": "Identical passwords for many user IDs pose the greatest risk since it makes unauthorized access easier."
    },
    {
        "id": 64,
        "question": "Which of the following is the PRIMARY advantage of using computer forensic software for investigations?",
        "options": [
            "A) The preservation of the chain of custody for electronic evidence",
            "B) Time and cost savings",
            "C) Efficiency and effectiveness",
            "D) Ability to search for violations of intellectual property rights"
        ],
        "correct": "A",
        "explanation": "The primary purpose of forensic software is to ensure the preservation of the chain of custody for electronic evidence."
    },
    {
        "id": 65,
        "question": "To confirm whether imported data are complete, an IS auditor should:",
        "options": [
            "A) Match control totals of the imported data to control totals of the original data",
            "B) Sort the data to confirm whether the data are in the same order as the original data",
            "C) Review the printout of the first 100 records",
            "D) Filter data for different categories and match them to the original data"
        ],
        "correct": "A",
        "explanation": "Matching control totals of the imported data with those of the original data ensures the completeness of the imported data."
    },
    {
        "id": 66,
        "question": "Which would be the BEST audit technique to identify payroll overpayments for the previous year?",
        "options": [
            "A) Test data",
            "B) Generalized audit software",
            "C) Integrated test facility",
            "D) Embedded audit module"
        ],
        "correct": "B",
        "explanation": "Generalized audit software is suitable for performing data analysis to recompute payrolls and detect overpayments."
    },
    {
        "id": 67,
        "question": "During a security audit, an IS auditor found that there were no documented security procedures. The IS auditor should:",
        "options": [
            "A) Create the procedures document",
            "B) Terminate the audit",
            "C) Conduct compliance testing",
            "D) Identify and evaluate existing practices"
        ],
        "correct": "D",
        "explanation": "The auditor should identify and evaluate the existing security practices rather than create documentation."
    },
    {
        "id": 68,
        "question": "In the course of performing a risk analysis, an IS auditor has identified threats and potential impacts. Next, the IS auditor should:",
        "options": [
            "A) Identify and assess the risk assessment process used by management",
            "B) Identify information assets and the underlying systems",
            "C) Disclose the threats and impacts to management",
            "D) Identify and evaluate the existing controls"
        ],
        "correct": "D",
        "explanation": "Once threats and potential impacts are identified, the auditor's next step is to identify and evaluate the existing controls."
    },
    {
        "id": 69,
        "question": "Which of the following would normally be the MOST reliable evidence for an auditor?",
        "options": [
            "A) A confirmation letter received from a third party verifying an account balance",
            "B) Assurance from line management that an application is working as designed",
            "C) Trend data obtained from World Wide Web (Internet) sources",
            "D) Ratio analysis developed by the IS auditor from reports supplied by line management"
        ],
        "correct": "A",
        "explanation": "Third-party confirmations are considered the most reliable source of evidence."
    },
    {
        "id": 70,
        "question": "Which audit technique provides the BEST evidence of the segregation of duties in an IS department?",
        "options": [
            "A) Discussion with management",
            "B) Review of the organization chart",
            "C) Observation and interviews",
            "D) Testing of user access rights"
        ],
        "correct": "C",
        "explanation": "Observation and interviews provide the best evidence regarding segregation of duties because they allow the auditor to directly assess what tasks staff members perform."
    },
    {
        "id": 71,
        "question": "Which of the following is an advantage of PERT over CPM?",
        "options": [
            "A) PERT considers different scenarios for activity completion",
            "B) PERT deals with known activities and definite completion time",
            "C) CPM considers different scenarios for activity completion",
            "D) CPM evaluates the amount of buffer needed for resources"
        ],
        "correct": "A",
        "explanation": "PERT is designed to handle uncertainty in project schedules by considering different scenarios for activity completion times."
    },
    {
        "id": 72,
        "question": "Which of the following is the GREATEST risk of an inadequate policy definition for data ownership?",
        "options": [
            "A) User management coordination does not exist",
            "B) Specific user accountability cannot be established",
            "C) Audit recommendations may not be implemented",
            "D) Users may have unauthorized access to originate, modify, or delete data"
        ],
        "correct": "D",
        "explanation": "The greatest risk of inadequate data ownership policies is that users may have unauthorized access to data."
    },
    {
        "id": 73,
        "question": "Which of the following risks could result from inadequate software baselining?",
        "options": [
            "A) Scope creep",
            "B) Sign-off delays",
            "C) Software integrity violations",
            "D) Inadequate controls"
        ],
        "correct": "A",
        "explanation": "Inadequate software baselining can lead to scope creep, where uncontrolled changes to a project can cause it to grow beyond its intended limits."
    },
    {
        "id": 74,
        "question": "An IS auditor reviews an organizational chart PRIMARILY for:",
        "options": [
            "A) An understanding of workflows.",
            "B) Investigating various communication channels.",
            "C) Understanding the responsibilities and authority of individuals.",
            "D) Investigating the network connected to different employees."
        ],
        "correct": "C",
        "explanation": "The primary purpose of reviewing an organizational chart is to understand the responsibilities and authority of individuals."
    },
    {
        "id": 75,
        "question": "The BEST method of proving the accuracy of a system tax calculation is by:",
        "options": [
            "A) Detailed visual review and analysis of the source code",
            "B) Recreating program logic using generalized audit software",
            "C) Preparing simulated transactions for processing and comparing results to predetermined results",
            "D) Automatic flowcharting and analysis of the source code"
        ],
        "correct": "C",
        "explanation": "Simulated transactions, where the results are compared with predetermined outcomes, offer the most reliable way to verify accuracy."
    },
    {
        "id": 76,
        "question": "An IS auditor performing a review of an application's controls would evaluate the:",
        "options": [
            "A) Efficiency of the application in meeting the business processes",
            "B) Impact of any exposures discovered",
            "C) Business processes served by the application",
            "D) Application's optimization"
        ],
        "correct": "B",
        "explanation": "The primary goal of an application control review is to assess the control mechanisms and identify any exposures or risks."
    },
    {
        "id": 77,
        "question": "Which online auditing technique is most effective for the early detection of errors or irregularities?",
        "options": [
            "A) Embedded audit module",
            "B) Integrated test facility",
            "C) Snapshots",
            "D) Audit hooks"
        ],
        "correct": "D",
        "explanation": "Audit hooks are proactive and allow the auditor to monitor and respond to certain types of transactions as they occur."
    },
    {
        "id": 78,
        "question": "When assessing the design of network monitoring controls, an IS auditor should FIRST review network:",
        "options": [
            "A) Topology diagrams.",
            "B) Bandwidth usage.",
            "C) Traffic analysis reports.",
            "D) Bottleneck locations."
        ],
        "correct": "A",
        "explanation": "The first step is reviewing the network topology diagrams to ensure that documentation is up to date."
    },
    {
        "id": 79,
        "question": "While conducting an audit, an IS auditor detects the presence of a virus. What should be the IS auditor's next step?",
        "options": [
            "A) Observe the response mechanism.",
            "B) Clear the virus from the network.",
            "C) Inform appropriate personnel immediately.",
            "D) Ensure deletion of the virus."
        ],
        "correct": "C",
        "explanation": "The first thing an IS auditor should do upon detecting a virus is to immediately notify the appropriate personnel."
    },
    {
        "id": 80,
        "question": "A substantive test to verify that tape library inventory records are accurate is:",
        "options": [
            "A) Determining whether bar code readers are installed.",
            "B) Determining whether the movement of tapes is authorized.",
            "C) Conducting a physical count of the tape inventory.",
            "D) Checking if receipts and issues of tapes are accurately recorded."
        ],
        "correct": "C",
        "explanation": "Conducting a physical count of the tape inventory is a substantive test that provides direct evidence of accuracy."
    },
    {
        "id": 81,
        "question": "When performing a computer forensic investigation, the IS auditor should be MOST concerned with:",
        "options": [
            "A) Analysis.",
            "B) Evaluation.",
            "C) Preservation.",
            "D) Disclosure."
        ],
        "correct": "C",
        "explanation": "The primary concern in a forensic investigation is preserving evidence so it can be used in legal proceedings."
    },
    {
        "id": 82,
        "question": "An IS auditor issues an audit report recommending a vendor product to address a vulnerability. The IS auditor has failed to exercise:",
        "options": [
            "A) Professional independence",
            "B) Organizational independence",
            "C) Technical competence",
            "D) Professional competence"
        ],
        "correct": "A",
        "explanation": "By recommending a specific vendor product, the IS auditor compromises their professional independence."
    },
    {
        "id": 83,
        "question": "The PRIMARY reason an IS auditor performs a functional walkthrough during the preliminary phase is to:",
        "options": [
            "A) Understand the business process.",
            "B) Comply with auditing standards.",
            "C) Identify control weakness.",
            "D) Plan substantive testing."
        ],
        "correct": "A",
        "explanation": "The primary purpose of a functional walkthrough is to understand the business processes and systems under audit."
    },
    {
        "id": 84,
        "question": "The PRIMARY purpose for meeting with auditees prior to formally closing a review is to:",
        "options": [
            "A) Confirm that the auditors did not overlook any important issues.",
            "B) Gain agreement on the findings.",
            "C) Receive feedback on the adequacy of the audit procedures.",
            "D) Test the structure of the final presentation."
        ],
        "correct": "B",
        "explanation": "The primary reason for meeting with auditees before closing an audit review is to gain their agreement on the findings."
    },
    {
        "id": 85,
        "question": "Which audit technique would BEST aid in determining whether there have been unauthorized program changes?",
        "options": [
            "A) Test data run",
            "B) Code review",
            "C) Automated code comparison",
            "D) Review of code migration procedures"
        ],
        "correct": "C",
        "explanation": "An automated code comparison is the most efficient technique for detecting unauthorized changes by comparing current and previous versions."
    },
    {
        "id": 86,
        "question": "Though management has stated otherwise, an IS auditor has reason to believe the organization is using unlicensed software. The IS auditor should:",
        "options": [
            "A) Include the statement of management in the audit report.",
            "B) Identify whether such software is indeed being used by the organization.",
            "C) Reconfirm with management the usage of the software.",
            "D) Discuss the issue with senior management."
        ],
        "correct": "B",
        "explanation": "The IS auditor must gather sufficient evidence before reporting. Independent verification is required."
    },
    {
        "id": 87,
        "question": "The MOST important reason for an IS auditor to obtain sufficient and appropriate audit evidence is to:",
        "options": [
            "A) Comply with regulatory requirements.",
            "B) Provide a basis for drawing reasonable conclusions.",
            "C) Ensure complete audit coverage.",
            "D) Perform the audit according to the defined scope."
        ],
        "correct": "B",
        "explanation": "The purpose of gathering evidence is to support the audit conclusions."
    },
    {
        "id": 88,
        "question": "After initial investigation, an IS auditor has reason to believe that fraud may be present. The IS auditor should:",
        "options": [
            "A) Expand activities to determine whether an investigation is warranted.",
            "B) Report the matter to the audit committee.",
            "C) Report the possibility of fraud to top management.",
            "D) Consult with external legal counsel."
        ],
        "correct": "A",
        "explanation": "The IS auditor must evaluate fraud indicators further before recommending a formal investigation."
    },
    {
        "id": 89,
        "question": "Which should an IS auditor use to detect duplicate invoice records within an invoice master file?",
        "options": [
            "A) Attribute sampling",
            "B) Generalized audit software (GAS)",
            "C) Test data",
            "D) Integrated test facility (ITF)"
        ],
        "correct": "B",
        "explanation": "GAS allows for a comprehensive review of all records and can easily identify duplicate invoices."
    },
    {
        "id": 90,
        "question": "Which is the MOST effective audit technique for identifying segregation of duties violations in a new ERP implementation?",
        "options": [
            "A) Reviewing a report of security rights in the system",
            "B) Reviewing the complexities of authorization objects",
            "C) Building a program to identify conflicts in authorization",
            "D) Examining recent access rights violation cases"
        ],
        "correct": "C",
        "explanation": "Developing a program that can systematically identify authorization conflicts is the most efficient approach."
    },
    {
        "id": 91,
        "question": "During the collection of forensic evidence, which action would MOST likely result in destruction of evidence?",
        "options": [
            "A) Dumping the memory content to a file",
            "B) Generating disk images of the compromised system",
            "C) Rebooting the system",
            "D) Removing the system from the network"
        ],
        "correct": "C",
        "explanation": "Rebooting a compromised system can change the system state and potentially destroy evidence in volatile memory."
    },
    {
        "id": 92,
        "question": "An IS auditor involved in designing an organization's BCP has been assigned to audit the plan. The IS auditor should:",
        "options": [
            "A) Decline the assignment.",
            "B) Inform management of the possible conflict after completing the audit.",
            "C) Inform the BCP team of the possible conflict prior to beginning.",
            "D) Communicate the possibility of conflict of interest to management prior to starting."
        ],
        "correct": "D",
        "explanation": "It is important to disclose any potential conflicts of interest to management before proceeding with the audit."
    },
    {
        "id": 93,
        "question": "Corrective action has been taken by an auditee immediately after identification of a reportable finding. The auditor should:",
        "options": [
            "A) Include the finding in the final report.",
            "B) Not include the finding because the audit report should include only unresolved findings.",
            "C) Not include the finding because corrective action can be verified during the audit.",
            "D) Include the finding in the closing meeting for discussion purposes only."
        ],
        "correct": "A",
        "explanation": "If action is taken after the audit started and before it ended, the audit report should identify the finding and describe the corrective action taken."
    },
    {
        "id": 94,
        "question": "During an exit interview where there is disagreement regarding a finding, an IS auditor should:",
        "options": [
            "A) Ask the auditee to sign a release form.",
            "B) Elaborate on the significance of the finding and the risks of not correcting it.",
            "C) Report the disagreement to the audit committee.",
            "D) Accept the auditee's position since they are the process owners."
        ],
        "correct": "B",
        "explanation": "If the auditee disagrees, it is important for the IS auditor to elaborate and clarify the risks and exposures."
    },
    {
        "id": 95,
        "question": "The final decision to include a material finding in an audit report should be made by the:",
        "options": [
            "A) Audit committee.",
            "B) Auditee's manager.",
            "C) IS auditor.",
            "D) CEO of the organization."
        ],
        "correct": "C",
        "explanation": "The IS auditor should make the final decision about what to include or exclude from the audit report to maintain independence."
    },
    {
        "id": 96,
        "question": "A PRIMARY benefit of control self-assessment (CSA) techniques is that it:",
        "options": [
            "A) Can identify high-risk areas for detailed review later.",
            "B) Is a cost-effective way to conduct a comprehensive audit.",
            "C) Engages staff in the risk management process.",
            "D) Reduces the need for external audits."
        ],
        "correct": "C",
        "explanation": "Engaging staff in the risk management process enhances accountability and promotes a control-conscious culture."
    },
    {
        "id": 97,
        "question": "An IS auditor has identified that an organization's firewall allows outbound traffic on all ports. What is the MOST significant risk?",
        "options": [
            "A) Exposure to external threats.",
            "B) Data leakage.",
            "C) Misconfiguration of security policies.",
            "D) Increased administrative overhead."
        ],
        "correct": "B",
        "explanation": "Allowing unrestricted outbound traffic significantly increases the risk of data leakage."
    },
    {
        "id": 98,
        "question": "An IT steering committee should review information systems PRIMARILY to assess:",
        "options": [
            "A) Whether IT processes support business requirements.",
            "B) If proposed system functionality is adequate.",
            "C) The stability of existing software.",
            "D) The complexity of installed technology."
        ],
        "correct": "A",
        "explanation": "The primary role of an IT steering committee is to ensure that the IS department aligns with the organization's mission and objectives."
    },
    {
        "id": 99,
        "question": "The MOST likely effect of lack of senior management commitment to IT strategic planning is:",
        "options": [
            "A) A lack of investment in technology.",
            "B) A lack of a methodology for systems development.",
            "C) Technology not aligning with the organization's objectives.",
            "D) An absence of control over technology contracts."
        ],
        "correct": "C",
        "explanation": "Absence of senior management commitment can lead to misalignment between IT and organizational strategy."
    },
    {
        "id": 100,
        "question": "Effective IT governance will ensure that the IT plan is consistent with the organization's:",
        "options": [
            "A) Business plan.",
            "B) Audit plan.",
            "C) Security plan.",
            "D) Investment plan."
        ],
        "correct": "A",
        "explanation": "IT governance requires that IT and business strategies are aligned to support the organization's goals."
    },
    {
        "id": 101,
        "question": "Establishing the level of acceptable risk is the responsibility of:",
        "options": [
            "A) Quality assurance management.",
            "B) Senior business management.",
            "C) The chief information officer.",
            "D) The chief security officer."
        ],
        "correct": "B",
        "explanation": "Senior management is responsible for establishing acceptable risk levels due to their accountability for organizational operations."
    },
    {
        "id": 102,
        "question": "IT governance is PRIMARILY the responsibility of the:",
        "options": [
            "A) Chief executive officer.",
            "B) Board of directors.",
            "C) IT steering committee.",
            "D) Audit committee."
        ],
        "correct": "B",
        "explanation": "IT governance is the responsibility of the board of directors, who provide strategic direction and oversight."
    },
    {
        "id": 103,
        "question": "Which IT governance best practice improves strategic alignment?",
        "options": [
            "A) Supplier and partner risks are managed.",
            "B) A knowledge base on customers, products, markets, and processes is in place.",
            "C) A structure is provided that facilitates creation and sharing of business information.",
            "D) Top management mediates between the imperatives of business and technology."
        ],
        "correct": "D",
        "explanation": "Top management mediation is essential for ensuring that IT strategies align with business needs and objectives."
    },
    {
        "id": 104,
        "question": "The ultimate purpose of IT governance is to:",
        "options": [
            "A) Encourage optimal use of IT.",
            "B) Reduce IT costs.",
            "C) Decentralize IT resources across the organization.",
            "D) Centralize control of IT."
        ],
        "correct": "A",
        "explanation": "IT governance aims to optimize the use of IT resources to support business objectives."
    },
    {
        "id": 105,
        "question": "From a control perspective, the key element in job descriptions is that they:",
        "options": [
            "A) Provide instructions on how to do the job and define authority.",
            "B) Are current, documented, and readily available to the employee.",
            "C) Communicate management's specific job performance expectations.",
            "D) Establish responsibility and accountability for the employee's actions."
        ],
        "correct": "D",
        "explanation": "Job descriptions are essential for establishing accountability and responsibility, which are crucial from a control perspective."
    },
    {
        "id": 106,
        "question": "When an employee is terminated, the MOST important action is to:",
        "options": [
            "A) Hand over all of the employee's files to another designated employee.",
            "B) Complete a backup of the employee's work.",
            "C) Notify other employees of the termination.",
            "D) Disable the employee's logical access."
        ],
        "correct": "D",
        "explanation": "Disabling the terminated employee's logical access is critical to prevent potential misuse of access rights."
    },
    {
        "id": 107,
        "question": "Many organizations require mandatory vacations to:",
        "options": [
            "A) Ensure the employee maintains a good quality of life.",
            "B) Reduce the opportunity for an employee to commit an improper or illegal act.",
            "C) Provide proper cross-training for another employee.",
            "D) Eliminate potential disruption from one-day-at-a-time vacations."
        ],
        "correct": "B",
        "explanation": "Mandatory vacations help reduce the opportunity for improper or illegal acts by allowing another employee to review the work."
    },
    {
        "id": 108,
        "question": "A LAN administrator normally would be restricted from:",
        "options": [
            "A) Having end-user responsibilities.",
            "B) Reporting to the end-user manager.",
            "C) Having programming responsibilities.",
            "D) Being responsible for LAN security administration."
        ],
        "correct": "C",
        "explanation": "A LAN administrator should not have programming responsibilities to prevent conflicts of interest."
    },
    {
        "id": 109,
        "question": "Which reduces the potential impact of social engineering attacks?",
        "options": [
            "A) Compliance with regulatory requirements",
            "B) Promoting ethical understanding",
            "C) Security awareness programs",
            "D) Effective performance incentives"
        ],
        "correct": "C",
        "explanation": "Security awareness programs educate users, making them less susceptible to social engineering."
    },
    {
        "id": 110,
        "question": "Which DBA activity should be performed by a different person?",
        "options": [
            "A) Deleting database activity logs",
            "B) Implementing database optimization tools",
            "C) Monitoring database usage",
            "D) Defining backup and recovery procedures"
        ],
        "correct": "A",
        "explanation": "Deleting activity logs should be done by someone other than the DBA to ensure proper segregation of duties."
    },
    {
        "id": 111,
        "question": "IS management has decided to rewrite a legacy system using 4GLs. Which risk is MOST often associated with 4GLs?",
        "options": [
            "A) Inadequate screen/report design facilities",
            "B) Complex programming language subsets",
            "C) Lack of portability across operating systems",
            "D) Inability to perform data-intensive operations"
        ],
        "correct": "D",
        "explanation": "4GLs are usually not suitable for data-intensive operations. They are mainly used for GUI design or simple query/report generators."
    },
    {
        "id": 112,
        "question": "Which is the BEST method for ensuring that critical fields in a master record have been updated properly?",
        "options": [
            "A) Field checks",
            "B) Control totals",
            "C) Reasonableness checks",
            "D) A before-and-after maintenance report"
        ],
        "correct": "D",
        "explanation": "A before-and-after maintenance report provides the most positive verification that updates were executed correctly."
    },
    {
        "id": 113,
        "question": "Which is a dynamic analysis tool for testing software modules?",
        "options": [
            "A) Blackbox test",
            "B) Desk checking",
            "C) Structured walk-through",
            "D) Design and code"
        ],
        "correct": "A",
        "explanation": "A blackbox test is a dynamic analysis tool that tests software modules by examining behavior without knowledge of internal workings."
    },
    {
        "id": 114,
        "question": "Which device extends the network and has the capacity to store frames and act as a storage and forward device?",
        "options": [
            "A) Router",
            "B) Bridge",
            "C) Repeater",
            "D) Gateway"
        ],
        "correct": "B",
        "explanation": "A bridge connects two separate networks to form a logical network and can store frames and act as a storage-and-forward device."
    },
    {
        "id": 115,
        "question": "Which is a benefit of using callback devices?",
        "options": [
            "A) Provide an audit trail",
            "B) Can be used in a switchboard environment",
            "C) Permit unlimited user mobility",
            "D) Allow call forwarding"
        ],
        "correct": "A",
        "explanation": "A callback feature logs all authorized and unauthorized access attempts, allowing for follow-up and review."
    },
    {
        "id": 116,
        "question": "Structured programming is BEST described as a technique that:",
        "options": [
            "A) Provides knowledge of program functions to other programmers via peer reviews.",
            "B) Reduces the maintenance time of programs by using small-scale program modules.",
            "C) Makes readable coding reflect dynamic execution of the program.",
            "D) Controls coding and testing of high-level functions in development."
        ],
        "correct": "B",
        "explanation": "Structured programming emphasizes small, manageable modules, which are easier to maintain and debug."
    },
    {
        "id": 117,
        "question": "Which data validation edit is effective in detecting transposition and transcription errors?",
        "options": [
            "A) Range check",
            "B) Check digit",
            "C) Validity check",
            "D) Duplicate check"
        ],
        "correct": "B",
        "explanation": "A check digit is a numeric value appended to data, calculated mathematically, and helps detect errors such as transposition or transcription."
    },
    {
        "id": 118,
        "question": "An offsite facility with electrical wiring, air conditioning, and flooring but no computer equipment is a:",
        "options": [
            "A) Cold site.",
            "B) Warm site.",
            "C) Dial-up site.",
            "D) Duplicate processing facility."
        ],
        "correct": "A",
        "explanation": "A cold site is prepared to receive equipment but does not have any components installed ahead of need."
    },
    {
        "id": 119,
        "question": "System failures occur when corrections to previously detected errors are resubmitted. This indicates inadequate:",
        "options": [
            "A) Unit testing",
            "B) Integration testing",
            "C) Design walk-throughs",
            "D) Configuration management"
        ],
        "correct": "B",
        "explanation": "Integration testing ensures that all components work together correctly. Failures during acceptance testing suggest inadequate integration testing."
    },
    {
        "id": 120,
        "question": "The MOST significant level of effort for BCP is generally required during the:",
        "options": [
            "A) Testing stage.",
            "B) Evaluation stage.",
            "C) Maintenance stage.",
            "D) Early stages of planning."
        ],
        "correct": "D",
        "explanation": "The most effort in BCP typically occurs during the early stages of planning, where the framework and resources are established."
    },
    {
        "id": 121,
        "question": "Which network configuration contains a direct link between any two host machines?",
        "options": [
            "A) Bus",
            "B) Ring",
            "C) Star",
            "D) Completely connected (mesh)"
        ],
        "correct": "D",
        "explanation": "A completely connected (mesh) configuration allows for a direct link between any two host machines."
    },
    {
        "id": 122,
        "question": "Which validation edit checks if a field contains data and not zeros or blanks?",
        "options": [
            "A) Check digit",
            "B) Existence check",
            "C) Completeness check",
            "D) Reasonableness check"
        ],
        "correct": "C",
        "explanation": "A completeness check verifies that a field contains actual data, excluding blanks or zeros."
    },
    {
        "id": 123,
        "question": "A data administrator is responsible for:",
        "options": [
            "A) Maintaining database system software.",
            "B) Defining data elements, data names and their relationship.",
            "C) Developing physical database structures.",
            "D) Developing data dictionary system software."
        ],
        "correct": "B",
        "explanation": "The primary role of a data administrator includes defining data elements, names, and their relationships."
    },
    {
        "id": 124,
        "question": "To affix a digital signature, the sender must first create a message digest by applying a hashing algorithm against:",
        "options": [
            "A) The entire message and then encipher the digest using the sender's private key.",
            "B) Any arbitrary part of the message and then encipher using sender's private key.",
            "C) The entire message and then encipher the message using sender's private key.",
            "D) The entire message and encipher message with digest using sender's private key."
        ],
        "correct": "A",
        "explanation": "The sender generates a message digest of the entire message, which is then encrypted using the sender's private key."
    },
    {
        "id": 125,
        "question": "A critical function of a firewall is to act as a:",
        "options": [
            "A) Special router connecting the Internet to a LAN.",
            "B) Device for preventing unauthorized users from accessing the LAN.",
            "C) Server used to connect authorized users to private trusted network resources.",
            "D) Proxy server to increase speed of access to authorized users."
        ],
        "correct": "B",
        "explanation": "Firewalls are designed to protect private networks from unauthorized access."
    },
    {
        "id": 126,
        "question": "Which hardware device relieves the central computer from network control, format conversion and message handling?",
        "options": [
            "A) Spool",
            "B) Cluster controller",
            "C) Protocol converter",
            "D) Front end processor"
        ],
        "correct": "D",
        "explanation": "A front-end processor manages communications and relieves the central computer from handling message formatting and control."
    },
    {
        "id": 127,
        "question": "Which translates e-mail formats from one network to another?",
        "options": [
            "A) Gateway",
            "B) Protocol converter",
            "C) Front-end communication processor",
            "D) Concentrator/multiplexor"
        ],
        "correct": "A",
        "explanation": "A gateway connects different networks and translates data formats, allowing messages to be transmitted between diverse network architectures."
    },
    {
        "id": 128,
        "question": "A hub is a device that connects:",
        "options": [
            "A) Two LANs using different protocols.",
            "B) A LAN with a WAN.",
            "C) A LAN with a metropolitan area network (MAN).",
            "D) Two segments of a single LAN."
        ],
        "correct": "D",
        "explanation": "A hub operates at the physical layer and connects multiple segments of the same LAN."
    },
    {
        "id": 129,
        "question": "Which telecommunication device translates data from digital to analog and back?",
        "options": [
            "A) Multiplexer",
            "B) Modem",
            "C) Protocol converter",
            "D) Concentrator"
        ],
        "correct": "B",
        "explanation": "A modem (modulator-demodulator) converts digital signals to analog for transmission over telephone lines and vice versa."
    },
    {
        "id": 130,
        "question": "Which systems-based approach monitors spending patterns to identify abnormal patterns?",
        "options": [
            "A) A neural network",
            "B) Database management software",
            "C) Management information systems",
            "D) Computer assisted audit techniques"
        ],
        "correct": "A",
        "explanation": "Neural networks are capable of learning and identifying patterns in data, making them effective for monitoring anomalies."
    },
    {
        "id": 131,
        "question": "A hardware control that detects errors when data is communicated is known as a:",
        "options": [
            "A) Duplicate check.",
            "B) Table lookup.",
            "C) Validity check.",
            "D) Parity check."
        ],
        "correct": "D",
        "explanation": "A parity check adds an extra bit to indicate whether the total number of 1-bits is odd or even, helping detect transmission errors."
    },
    {
        "id": 132,
        "question": "For which application would rapid recovery be MOST crucial?",
        "options": [
            "A) Point-of-sale system",
            "B) Corporate planning",
            "C) Regulatory reporting",
            "D) Departmental chargeback"
        ],
        "correct": "A",
        "explanation": "A point-of-sale system is critical for real-time transactions. Downtime can directly affect revenue generation."
    },
    {
        "id": 133,
        "question": "The initial step in establishing an information security program is:",
        "options": [
            "A) Development of an information security standards manual.",
            "B) Performance of a comprehensive security control review.",
            "C) Adoption of a corporate information security policy statement.",
            "D) Purchase of security access control software."
        ],
        "correct": "C",
        "explanation": "Adoption of a corporate information security policy statement provides a framework and demonstrates management's commitment."
    },
    {
        "id": 134,
        "question": "Malicious code that changes itself with each file it infects is called a:",
        "options": [
            "A) Logic bomb.",
            "B) Stealth virus.",
            "C) Trojan horse.",
            "D) Polymorphic virus."
        ],
        "correct": "D",
        "explanation": "A polymorphic virus can modify its code with each infection, making it difficult for antivirus software to detect."
    },
    {
        "id": 135,
        "question": "Which continuity plan test uses actual resources to simulate a system crash?",
        "options": [
            "A) Paper test",
            "B) Post test",
            "C) Preparedness test",
            "D) Walk-through"
        ],
        "correct": "C",
        "explanation": "A preparedness test is a scaled-back version of a full test, using real resources to simulate a disaster scenario."
    },
    {
        "id": 136,
        "question": "In a PKI, the authority responsible for identification and authentication of certificate applicants is the:",
        "options": [
            "A) Registration authority (RA).",
            "B) Issuing certification authority (CA).",
            "C) Subject CA.",
            "D) Policy management authority."
        ],
        "correct": "A",
        "explanation": "The RA is responsible for verifying the identity of certificate applicants before issuing digital certificates."
    },
    {
        "id": 137,
        "question": "What is the primary objective of a control self-assessment (CSA) program?",
        "options": [
            "A) Enhancement of the audit responsibility.",
            "B) Elimination of the audit responsibility.",
            "C) Replacement of the audit responsibility.",
            "D) Integrity of the audit responsibility."
        ],
        "correct": "A",
        "explanation": "The primary goal of a CSA program is to enhance audit responsibilities by involving management and staff."
    },
    {
        "id": 138,
        "question": "How does a risk-based approach to audit planning benefit systems auditing?",
        "options": [
            "A) Controls testing starts earlier.",
            "B) Auditing resources are allocated to the areas of highest concern.",
            "C) Auditing risk is reduced.",
            "D) Controls testing is more thorough."
        ],
        "correct": "B",
        "explanation": "A risk-based approach ensures that auditing resources focus on the highest risk areas."
    },
    {
        "id": 139,
        "question": "After identifying threats and potential impacts, the auditor should:",
        "options": [
            "A) Identify and evaluate the existing controls.",
            "B) Conduct a business impact analysis (BIA).",
            "C) Report on existing controls.",
            "D) Propose new controls."
        ],
        "correct": "A",
        "explanation": "The next logical step after identifying threats is to assess existing controls."
    },
    {
        "id": 140,
        "question": "What type of risk results when an IS auditor uses inadequate test procedures and concludes errors do not exist?",
        "options": [
            "A) Business risk.",
            "B) Detection risk.",
            "C) Residual risk.",
            "D) Inherent risk."
        ],
        "correct": "B",
        "explanation": "Detection risk occurs when an auditor fails to detect material misstatements due to ineffective testing."
    },
    {
        "id": 141,
        "question": "Who is accountable for maintaining appropriate security measures over information assets?",
        "options": [
            "A) Data and systems owners.",
            "B) Data and systems users.",
            "C) Data and systems custodians.",
            "D) Data and systems auditors."
        ],
        "correct": "A",
        "explanation": "Data and systems owners are ultimately responsible for ensuring adequate security measures."
    },
    {
        "id": 142,
        "question": "Proper segregation of duties prohibits a system analyst from performing quality-assurance functions. True or false?",
        "options": [
            "A) True",
            "B) False"
        ],
        "correct": "A",
        "explanation": "Proper segregation of duties is essential to prevent conflicts of interest."
    },
    {
        "id": 143,
        "question": "What should an IS auditor do if project-approval procedures do not exist?",
        "options": [
            "A) Advise senior management to invest in project-management training.",
            "B) Create project-approval procedures for future implementations.",
            "C) Assign project leaders.",
            "D) Recommend that formal approval procedures be adopted and documented."
        ],
        "correct": "D",
        "explanation": "The IS auditor should recommend establishment and documentation of formal project-approval procedures."
    },
    {
        "id": 144,
        "question": "Who is ultimately accountable for the development of an IS security policy?",
        "options": [
            "A) The board of directors.",
            "B) Middle management.",
            "C) Security administrators.",
            "D) Network administrators."
        ],
        "correct": "A",
        "explanation": "The board of directors has ultimate accountability for IS security policies."
    },
    {
        "id": 145,
        "question": "A core tenet of an IS strategy is that it must:",
        "options": [
            "A) Be inexpensive.",
            "B) Be protected as sensitive confidential information.",
            "C) Protect information confidentiality, integrity, and availability.",
            "D) Support the business objectives of the organization."
        ],
        "correct": "D",
        "explanation": "An effective IS strategy must align with and support overall business objectives."
    },
    {
        "id": 146,
        "question": "Batch control reconciliation is a _____ control for mitigating risk of inadequate segregation of duties.",
        "options": [
            "A) Detective",
            "B) Corrective",
            "C) Preventative",
            "D) Compensatory"
        ],
        "correct": "D",
        "explanation": "Batch control reconciliation serves as a compensatory control to mitigate risks from inadequate segregation of duties."
    },
    {
        "id": 147,
        "question": "Which could lead to an unintentional loss of confidentiality?",
        "options": [
            "A) Lack of employee awareness of a company's information security policy",
            "B) Failure to comply with a company's information security policy",
            "C) A momentary lapse of reason",
            "D) Lack of security policy enforcement procedures"
        ],
        "correct": "A",
        "explanation": "Lack of employee awareness of information security policy could lead to unintentional loss of confidentiality."
    },
    {
        "id": 148,
        "question": "What topology provides the greatest redundancy of routes and fault tolerance?",
        "options": [
            "A) A star network topology",
            "B) A mesh network topology with packet forwarding enabled at each host",
            "C) A bus network topology",
            "D) A ring network topology"
        ],
        "correct": "B",
        "explanation": "A mesh network with packet forwarding provides the greatest redundancy and fault tolerance."
    },
    {
        "id": 149,
        "question": "An IS auditor usually places more reliance on evidence directly collected. What is an example?",
        "options": [
            "A) Evidence collected through personal observation",
            "B) Evidence from systems logs provided by security administration",
            "C) Evidence from surveys collected from internal staff",
            "D) Evidence from transaction reports provided by IT administration"
        ],
        "correct": "A",
        "explanation": "An IS auditor places more reliance on evidence directly collected, such as through personal observation."
    },
    {
        "id": 150,
        "question": "Atomicity enforces data integrity by ensuring a transaction is completed entirely or not at all. True or false?",
        "options": [
            "A) True",
            "B) False"
        ],
        "correct": "A",
        "explanation": "Atomicity ensures a transaction is either completed in its entirety or not at all, part of the ACID test."
    },
]

# ─── Streamlit App ─────────────────────────────
st.set_page_config(
    page_title="CISA Exam Prep - Interactive Quiz",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .stButton > button {
        width: 100%;
        border-radius: 8px;
        font-weight: 600;
    }
    .correct-answer {
        background-color: #d4edda;
        border: 2px solid #28a745;
        border-radius: 8px;
        padding: 10px;
        color: #155724;
    }
    .wrong-answer {
        background-color: #f8d7da;
        border: 2px solid #dc3545;
        border-radius: 8px;
        padding: 10px;
        color: #721c24;
    }
    .explanation-box {
        background-color: #e7f3ff;
        border-left: 4px solid #2196F3;
        border-radius: 8px;
        padding: 15px;
        margin-top: 10px;
    }
    .score-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("📋 CISA Exam Prep")
    st.markdown("---")
    
    # Mode selection
    mode = st.radio(
        "Select Mode:",
        ["📝 Practice Mode", "🎯 Exam Simulation", "🔀 Random 50 Questions"],
        help="Practice: one question at a time with feedback. Exam: timed session. Random: 50 random questions."
    )
    
    st.markdown("---")
    
    # Session state management
    if 'current_index' not in st.session_state:
        st.session_state.current_index = 0
    if 'answers' not in st.session_state:
        st.session_state.answers = {}
    if 'submitted' not in st.session_state:
        st.session_state.submitted = {}
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'total_answered' not in st.session_state:
        st.session_state.total_answered = 0
    if 'shuffled_questions' not in st.session_state:
        st.session_state.shuffled_questions = question_bank.copy()
    
    # Reset button
    if st.button("🔄 Reset All Progress", use_container_width=True):
        st.session_state.current_index = 0
        st.session_state.answers = {}
        st.session_state.submitted = {}
        st.session_state.score = 0
        st.session_state.total_answered = 0
        st.session_state.shuffled_questions = question_bank.copy()
        random.shuffle(st.session_state.shuffled_questions)
        st.rerun()
    
    # Handle random 50 mode
    if mode == "🔀 Random 50 Questions":
        if len(st.session_state.shuffled_questions) == len(question_bank):
            sampled = random.sample(question_bank, min(50, len(question_bank)))
            st.session_state.shuffled_questions = sampled
            st.session_state.current_index = 0
            st.session_state.answers = {}
            st.session_state.submitted = {}
            st.session_state.score = 0
            st.session_state.total_answered = 0
    else:
        if len(st.session_state.shuffled_questions) != len(question_bank):
            st.session_state.shuffled_questions = question_bank.copy()
    
    total_questions = len(st.session_state.shuffled_questions)
    
    # Score display
    st.markdown(f"""
    <div class="score-card">
        <h3>📊 Your Score</h3>
        <h1>{st.session_state.score} / {st.session_state.total_answered}</h1>
        <p>{'🌟 ' + str(round(st.session_state.score/st.session_state.total_answered*100, 1)) + '%' if st.session_state.total_answered > 0 else '0%'}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Progress bar
    progress = (st.session_state.current_index + 1) / total_questions if total_questions > 0 else 0
    st.progress(progress, text=f"Question {st.session_state.current_index + 1} of {total_questions}")
    
    # Navigation
    st.markdown("### 📍 Navigation")
    col_nav1, col_nav2, col_nav3 = st.columns(3)
    with col_nav1:
        if st.button("⬅️ Previous", use_container_width=True, disabled=(st.session_state.current_index == 0)):
            st.session_state.current_index = max(0, st.session_state.current_index - 1)
            st.rerun()
    with col_nav2:
        jump_to = st.number_input("Jump to:", min_value=1, max_value=total_questions, value=st.session_state.current_index + 1, label_visibility="collapsed")
        if st.button("🎯 Go", use_container_width=True):
            st.session_state.current_index = jump_to - 1
            st.rerun()
    with col_nav3:
        if st.button("Next ➡️", use_container_width=True, disabled=(st.session_state.current_index >= total_questions - 1)):
            st.session_state.current_index = min(total_questions - 1, st.session_state.current_index + 1)
            st.rerun()

# Main content
st.title("🔐 CISA Certification Exam Preparation")
st.markdown("*Interactive multiple-choice quiz with instant feedback and explanations*")
st.markdown("---")

# Get current question
if total_questions > 0 and 0 <= st.session_state.current_index < total_questions:
    q = st.session_state.shuffled_questions[st.session_state.current_index]
    q_id = q['id']
    
    # Question display
    st.markdown(f"""
    <div style="background-color: #f8f9fa; padding: 20px; border-radius: 12px; margin-bottom: 20px; border: 1px solid #dee2e6;">
        <h3 style="color: #333; margin-top: 0;">Question {st.session_state.current_index + 1} (ID: {q_id})</h3>
        <p style="font-size: 18px; color: #1a1a1a; font-weight: 500;">{q['question']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Options
    option_labels = [opt[0] for opt in q['options']]  # A, B, C, D
    option_texts = [opt[3:].strip() for opt in q['options']]  # Text without prefix
    
    # Check if already submitted
    is_submitted = q_id in st.session_state.submitted
    
    if not is_submitted:
        selected = st.radio(
            "Select your answer:",
            options=option_labels,
            format_func=lambda x: f"{x}) {option_texts[option_labels.index(x)]}",
            key=f"radio_{q_id}",
            index=None
        )
        
        col_submit, col_skip = st.columns([1, 1])
        with col_submit:
            if st.button("✅ Submit Answer", use_container_width=True, type="primary", disabled=(selected is None)):
                if selected:
                    is_correct = (selected == q['correct'])
                    st.session_state.submitted[q_id] = {
                        'selected': selected,
                        'correct': is_correct
                    }
                    st.session_state.answers[q_id] = selected
                    st.session_state.total_answered += 1
                    if is_correct:
                        st.session_state.score += 1
                    st.rerun()
        with col_skip:
            if st.button("⏭️ Skip", use_container_width=True):
                st.session_state.current_index = min(total_questions - 1, st.session_state.current_index + 1)
                st.rerun()
    else:
        # Show results
        submission = st.session_state.submitted[q_id]
        selected = submission['selected']
        is_correct = submission['correct']
        
        # Display options with color coding
        st.markdown("### Your Answer:")
        for i, (label, text) in enumerate(zip(option_labels, option_texts)):
            if label == q['correct']:
                st.markdown(f"""
                <div class="correct-answer">
                    ✅ <strong>{label}) {text}</strong> ← Correct Answer
                </div>
                """, unsafe_allow_html=True)
            elif label == selected and not is_correct:
                st.markdown(f"""
                <div class="wrong-answer">
                    ❌ <strong>{label}) {text}</strong> ← Your Answer (Incorrect)
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"{label}) {text}")
        
        # Result banner
        if is_correct:
            st.success("🎉 Correct! Well done!")
        else:
            st.error("😔 Incorrect. Review the explanation below.")
        
        # Explanation
        st.markdown(f"""
        <div class="explanation-box">
            <h4>📖 Explanation:</h4>
            <p>{q['explanation']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Navigation buttons
        col_next1, col_next2 = st.columns([1, 1])
        with col_next1:
            if st.button("⬅️ Previous Question", use_container_width=True):
                st.session_state.current_index = max(0, st.session_state.current_index - 1)
                st.rerun()
        with col_next2:
            next_btn_text = "Next Question ➡️" if st.session_state.current_index < total_questions - 1 else "🏁 Finish"
            if st.button(next_btn_text, use_container_width=True, type="primary"):
                if st.session_state.current_index < total_questions - 1:
                    st.session_state.current_index += 1
                st.rerun()

else:
    st.info("No questions available. Click 'Reset All Progress' to reload the question bank.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 10px;">
    <p>📋 <strong>CISA Exam Preparation Tool</strong> | Study smart, pass with confidence! 🎓</p>
    <p>Tips: Review explanations carefully. Focus on understanding concepts rather than memorizing answers.</p>
</div>
""", unsafe_allow_html=True)
# Custom CSS for better styling
st.markdown("""
<style>
    .stButton > button {
        width: 100%;
        border-radius: 8px;
        font-weight: 600;
    }
    .correct-answer {
        background-color: #d4edda;
        border: 2px solid #28a745;
        border-radius: 8px;
        padding: 10px;
        color: #155724;
    }
    .wrong-answer {
        background-color: #f8d7da;
        border: 2px solid #dc3545;
        border-radius: 8px;
        padding: 10px;
        color: #721c24;
    }
    .explanation-box {
        background-color: #e7f3ff;
        border-left: 4px solid #2196F3;
        border-radius: 8px;
        padding: 15px;
        margin-top: 10px;
        color: black;   /* Change added here */
    }
    .score-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)
