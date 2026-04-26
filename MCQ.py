import streamlit as st
import random
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

# ─── Full Question Bank: IDs 150 to 300 ─────
    {
        "id": 150,
        "question": "Atomicity enforces data integrity by ensuring a transaction is completed entirely or not at all. True or false?",
        "options": ["A) True", "B) False"],
        "correct": "A",
        "explanation": "Atomicity ensures a transaction is either completed in its entirety or not at all; it is part of the ACID test."
    },
    {
        "id": 151,
        "question": "If an IS auditor finds evidence of risk involved in not implementing proper segregation of duties, what is the auditor's primary responsibility?",
        "options": ["A) To advise senior management.", "B) To reassign job functions to eliminate potential fraud.", "C) To implement compensator controls.", "D) Segregation of duties is an administrative control not considered by an IS auditor."],
        "correct": "A",
        "explanation": "The IS auditor's primary responsibility is to advise senior management on risks like improper segregation of duties."
    },
    {
        "id": 152,
        "question": "Who is responsible for implementing cost-effective controls in an automated system?",
        "options": ["A) Security policy administrators", "B) Business unit management", "C) Senior management", "D) Board of directors"],
        "correct": "B",
        "explanation": "Business unit management is responsible for implementing cost-effective controls in automated systems."
    },
    {
        "id": 153,
        "question": "Why does an IS auditor review an organization chart?",
        "options": ["A) To optimize the responsibilities and authority of individuals", "B) To control the responsibilities and authority of individuals", "C) To better understand the responsibilities and authority of individuals", "D) To identify project sponsors"],
        "correct": "C",
        "explanation": "An IS auditor reviews the organizational chart to understand the responsibilities and authority within the organization."
    },
    {
        "id": 154,
        "question": "Ensuring that security and control policies support business and IT objectives is a primary objective of:",
        "options": ["A) An IT security policies audit", "B) A processing audit", "C) A software audit", "D) A vulnerability assessment"],
        "correct": "A",
        "explanation": "The primary objective of an IT security policies audit is to ensure security and control policies align with business and IT objectives."
    },
    {
        "id": 155,
        "question": "When auditing third-party service providers, an IS auditor should be concerned with which of the following? Choose the BEST answer.",
        "options": ["A) Ownership of the programs and files", "B) A statement of due care and confidentiality, and the capability for continued service of the service provider in the event of a disaster", "C) A statement of due care", "D) Ownership of programs and files, a statement of due care and confidentiality, and the capability for continued service of the service provider in the event of a disaster"],
        "correct": "D",
        "explanation": "When auditing third-party service providers, an auditor should be concerned with ownership, due care, confidentiality, and continued service capability."
    },
    {
        "id": 156,
        "question": "When performing an IS strategy audit, an IS auditor should especially focus on procedures. True or false?",
        "options": ["A) True", "B) False"],
        "correct": "B",
        "explanation": "When auditing IS strategy, the focus should not only be on procedures but on aligning strategy with organizational objectives and external environment."
    },
    {
        "id": 157,
        "question": "What process allows IS management to determine whether the activities of the organization differ from the planned or expected levels? Choose the BEST answer.",
        "options": ["A) Business impact assessment", "B) Risk assessment", "C) IS assessment methods", "D) Key performance indicators (KPIs)"],
        "correct": "C",
        "explanation": "IS assessment methods are used by management to determine whether the organization's activities align with planned levels."
    },
    {
        "id": 158,
        "question": "When should reviewing an audit client's business plan be performed relative to reviewing an organization's IT strategic plan?",
        "options": [
            "A) Reviewing an audit client's business plan should be performed before reviewing an organization's IT strategic plan.",
            "B) Reviewing an audit client's business plan should be performed after reviewing an organization's IT strategic plan.",
            "C) Reviewing an audit client's business plan should be performed during the review of an organization's IT strategic plan.",
            "D) Reviewing an audit client's business plan should be performed without regard to an organization's IT strategic plan."
        ],
        "correct": "A",
        "explanation": "Reviewing the business plan should come before the IT strategic plan to ensure alignment."
    },
    {
        "id": 159,
        "question": "Allowing application programmers to directly patch or change code in production programs increases the risk of fraud. True or false?",
        "options": ["A) True", "B) False"],
        "correct": "A",
        "explanation": "Allowing programmers to directly patch production code increases fraud risk due to lack of segregation of duties."
    },
    {
        "id": 160,
        "question": "Who should be responsible for network security operations?",
        "options": ["A) Business unit managers", "B) Security administrators", "C) Network administrators", "D) IS auditors"],
        "correct": "B",
        "explanation": "Security administrators are responsible for managing and ensuring the security of network operations."
    },
    {
        "id": 161,
        "question": "Proper segregation of duties does not prohibit a quality control administrator from also being responsible for change control and problem management. True or false?",
        "options": ["A) True", "B) False"],
        "correct": "A",
        "explanation": "Proper segregation of duties does not prohibit a quality-control administrator from also being responsible for change control and problem management."
    },
    {
        "id": 162,
        "question": "What can be implemented to provide the highest level of protection from external attack?",
        "options": [
            "A) Layering perimeter network protection by configuring the firewall as a screened host in a screened subnet behind the bastion host",
            "B) Configuring the firewall as a screened host behind a router",
            "C) Configuring the firewall as the protecting bastion host",
            "D) Configuring two load-sharing firewalls facilitating VPN access from external hosts to internal hosts"
        ],
        "correct": "A",
        "explanation": "Layering perimeter network protection using a screened host in a screened subnet behind a bastion host provides the highest protection."
    },
    {
        "id": 163,
        "question": "The directory system of a database-management system describes:",
        "options": ["A) The access method to the data", "B) The location of data AND the access method", "C) The location of data", "D) Neither the location of data NOR the access method"],
        "correct": "B",
        "explanation": "The directory system describes the location of data and the access method."
    },
    {
        "id": 164,
        "question": "How is the risk of improper file access affected upon implementing a database system?",
        "options": ["A) Risk varies", "B) Risk is reduced", "C) Risk is not affected", "D) Risk is increased"],
        "correct": "D",
        "explanation": "Improper file access becomes a greater risk when implementing a database system."
    },
    {
        "id": 165,
        "question": "In order to properly protect against unauthorized disclosure of sensitive data, how should hard disks be sanitized?",
        "options": ["A) The data should be deleted and overwritten with binary Os", "B) The data should be demagnetized", "C) The data should be low-level formatted", "D) The data should be deleted"],
        "correct": "B",
        "explanation": "To properly protect against unauthorized disclosure, hard disks should be demagnetized before disposal."
    },
    {
        "id": 166,
        "question": "When reviewing print systems spooling, an IS auditor is MOST concerned with which of the following vulnerabilities?",
        "options": [
            "A) The potential for unauthorized deletion of report copies",
            "B) The potential for unauthorized modification of report copies",
            "C) The potential for unauthorized printing of report copies",
            "D) The potential for unauthorized editing of report copies"
        ],
        "correct": "C",
        "explanation": "The auditor is most concerned with unauthorized printing of report copies."
    },
    {
        "id": 167,
        "question": "Why is the WAP gateway a component warranting critical concern for the IS auditor when auditing message confidentiality?",
        "options": [
            "A) WAP is often configured by default settings and is thus insecure",
            "B) WAP provides weak encryption for wireless traffic",
            "C) WAP functions as a protocol-conversion gateway for wireless TLS to Internet SSL",
            "D) WAP often interfaces critical IT systems"
        ],
        "correct": "C",
        "explanation": "The WAP gateway acts as a protocol-conversion gateway, making it critical for message confidentiality."
    },
    {
        "id": 168,
        "question": "Proper segregation of duties prevents a computer operator (user) from performing security administration duties. True or false?",
        "options": ["A) True", "B) False"],
        "correct": "A",
        "explanation": "Proper segregation of duties prohibits a computer operator from performing security administration duties."
    },
    {
        "id": 169,
        "question": "How do modems function to facilitate analog transmissions entering a digital network?",
        "options": [
            "A) Modems convert analog transmissions to digital, and digital transmission to analog",
            "B) Modems encapsulate analog transmissions within digital, and digital transmissions within analog",
            "C) Modems convert digital transmissions to analog, and analog transmissions to digital",
            "D) Modems encapsulate digital transmissions within analog, and analog transmissions within digital"
        ],
        "correct": "A",
        "explanation": "Modems convert analog to digital and digital to analog, enabling analog transmissions on a digital network."
    },
    {
        "id": 170,
        "question": "Which of the following are effective in detecting fraud because they can consider a large number of variables?",
        "options": ["A) Expert systems", "B) Neural networks", "C) Integrated synchronized systems", "D) Multitasking applications"],
        "correct": "B",
        "explanation": "Neural networks are effective at detecting fraud because they can consider a large number of variables."
    },
    {
        "id": 171,
        "question": "What supports data transmission through split cable facilities or duplicate cable facilities?",
        "options": ["A) Diverse routing", "B) Dual routing", "C) Alternate routing", "D) Redundant routing"],
        "correct": "A",
        "explanation": "Diverse routing supports data transmission through split or duplicate cable facilities."
    },
    {
        "id": 172,
        "question": "Which firewall type(s) provide(s) the greatest degree of protection by inspecting all seven OSI layers?",
        "options": [
            "A) A first-generation packet-filtering firewall",
            "B) A circuit-level gateway",
            "C) An application-layer gateway, or proxy firewall, and stateful-inspection firewalls",
            "D) An application-layer gateway, or proxy firewall, but not stateful-inspection firewalls"
        ],
        "correct": "C",
        "explanation": "Both application-layer gateways and stateful-inspection firewalls inspect all seven OSI layers."
    },
    {
        "id": 173,
        "question": "Which of the following can degrade network performance? Choose the BEST answer.",
        "options": [
            "A) Superfluous use of redundant load-sharing gateways",
            "B) Increasing traffic collisions due to host congestion by creating new collision domains",
            "C) Inefficient and superfluous use of network devices such as switches",
            "D) Inefficient and superfluous use of network devices such as hubs"
        ],
        "correct": "D",
        "explanation": "Inefficient and superfluous use of hubs can degrade network performance."
    },
    {
        "id": 174,
        "question": "Which provide(s) near-immediate recoverability for time-sensitive systems?",
        "options": ["A) Automated electronic journaling and parallel processing", "B) Data mirroring and parallel processing", "C) Data mirroring", "D) Parallel processing"],
        "correct": "B",
        "explanation": "Data mirroring and parallel processing together provide near-immediate recoverability."
    },
    {
        "id": 175,
        "question": "What is an effective control for granting temporary access to vendors?",
        "options": [
            "A) Creating user accounts that automatically expire by a predetermined date",
            "B) Creating permanent guest accounts for temporary use",
            "C) Creating user accounts that restrict logon access to certain hours",
            "D) Creating a single shared vendor administrator account"
        ],
        "correct": "A",
        "explanation": "Accounts that automatically expire by a set date are an effective temporary access control."
    },
    {
        "id": 176,
        "question": "Which helps prevent an organization's systems from participating in a DDoS attack?",
        "options": ["A) Inbound traffic filtering", "B) Using ACLs to restrict inbound connections", "C) Outbound traffic filtering", "D) Recentralizing distributed systems"],
        "correct": "C",
        "explanation": "Outbound traffic filtering can prevent participation in DDoS attacks."
    },
    {
        "id": 177,
        "question": "What is a common vulnerability allowing denial-of-service attacks?",
        "options": ["A) Least privilege access", "B) Lack of security policy awareness", "C) Improperly configured routers and router access lists", "D) Configuring firewall access rules"],
        "correct": "C",
        "explanation": "Improperly configured routers and access lists are a common DoS vulnerability."
    },
    {
        "id": 178,
        "question": "What are trojan horse programs? Choose the BEST answer.",
        "options": ["A) A common form of internal attack", "B) Malicious programs requiring a carrier like email", "C) Malicious programs that run independently", "D) A common form of Internet attack"],
        "correct": "D",
        "explanation": "Trojan horse programs are a common form of Internet attack."
    },
    {
        "id": 179,
        "question": "What is used to measure and ensure proper network capacity management and availability?",
        "options": ["A) Network performance-monitoring tools", "B) Network component redundancy", "C) Syslog reporting", "D) IT strategic planning"],
        "correct": "A",
        "explanation": "Network performance-monitoring tools measure capacity and availability."
    },
    {
        "id": 180,
        "question": "What can be used to gather evidence of network attacks?",
        "options": ["A) Access control lists", "B) Intrusion-detection systems (IDS)", "C) Syslog reporting", "D) Antivirus programs"],
        "correct": "B",
        "explanation": "IDS are used to gather evidence of network attacks."
    },
    {
        "id": 181,
        "question": "Which is a passive attack method used to determine network vulnerabilities?",
        "options": ["A) Traffic analysis", "B) SYN flood", "C) Denial of service", "D) Distributed denial of service"],
        "correct": "A",
        "explanation": "Traffic analysis is a passive attack; the others are active."
    },
    {
        "id": 182,
        "question": "Which fire-suppression method is considered the most environmentally friendly?",
        "options": ["A) Halon gas", "B) Deluge sprinklers", "C) Dry-pipe sprinklers", "D) Wet-pipe sprinklers"],
        "correct": "C",
        "explanation": "Dry-pipe sprinklers are the most environmentally friendly fire-suppression method."
    },
    {
        "id": 183,
        "question": "What is a callback system?",
        "options": [
            "A) Remote-access system where the server immediately calls back if the connection fails",
            "B) User application automatically redials the server",
            "C) User dials in, server terminates the connection and dials back a predetermined number",
            "D) User dials in, server disconnects and allows the user to call back an approved number for a limited time"
        ],
        "correct": "C",
        "explanation": "A callback system: user connects, server terminates the connection, and dials back a stored number."
    },
    {
        "id": 184,
        "question": "What type of fire-suppression system uses water delivered through dry pipes?",
        "options": ["A) A dry-pipe sprinkler system", "B) A deluge sprinkler system", "C) A wet-pipe system", "D) A halon sprinkler system"],
        "correct": "A",
        "explanation": "A dry-pipe sprinkler system delivers water through dry pipes."
    },
    {
        "id": 185,
        "question": "Digital signatures require the sender to sign data by encrypting with the sender's public key. True or false?",
        "options": ["A) False", "B) True"],
        "correct": "A",
        "explanation": "The sender signs with the private key; the recipient decrypts with the sender's public key."
    },
    {
        "id": 186,
        "question": "Which provides the BEST single-factor authentication?",
        "options": ["A) Biometrics", "B) Password", "C) Token", "D) PIN"],
        "correct": "A",
        "explanation": "Biometrics provides the strongest single-factor authentication."
    },
    {
        "id": 187,
        "question": "What is used to provide authentication of a website and authenticate encryption keys?",
        "options": ["A) An organizational certificate", "B) A user certificate", "C) A website certificate", "D) Authenticode"],
        "correct": "C",
        "explanation": "A website certificate authenticates the website and can authenticate encryption keys."
    },
    {
        "id": 188,
        "question": "What determines the strength of a secret key in a symmetric cryptosystem?",
        "options": [
            "A) Key length, degree of permutation, and encryption algorithm complexity",
            "B) Key length, initial input vectors, and encryption algorithm complexity",
            "C) Key length and encryption algorithm complexity",
            "D) Initial input vectors and encryption algorithm complexity"
        ],
        "correct": "B",
        "explanation": "Strength is determined by key length, initial input vectors, and algorithm complexity."
    },
    {
        "id": 189,
        "question": "What process is used to validate a subject's identity?",
        "options": ["A) Identification", "B) Nonreproduction", "C) Authorization", "D) Authentication"],
        "correct": "D",
        "explanation": "Authentication validates a subject's identity."
    },
    {
        "id": 190,
        "question": "What is often assured through table link verification and reference checks?",
        "options": ["A) Database integrity", "B) Database synchronization", "C) Database normalcy", "D) Database accuracy"],
        "correct": "A",
        "explanation": "Table link verification and reference checks ensure database integrity."
    },
    {
        "id": 191,
        "question": "Which should an IS auditor review to determine user permissions for a resource?",
        "options": ["A) Systems logs", "B) Access control lists (ACL)", "C) Application logs", "D) Error logs"],
        "correct": "B",
        "explanation": "Access control lists (ACLs) show user permissions for a resource."
    },
    {
        "id": 192,
        "question": "What should IS auditors always check when auditing password files?",
        "options": [
            "A) That deleting password files is protected",
            "B) That password files are encrypted",
            "C) That password files are not accessible over the network",
            "D) That password files are archived"
        ],
        "correct": "B",
        "explanation": "IS auditors should always check that password files are encrypted."
    },
    {
        "id": 193,
        "question": "Using the OSI reference model, which layer(s) are used to encrypt data?",
        "options": ["A) Transport layer", "B) Session layer", "C) Session and transport layers", "D) Data link layer"],
        "correct": "C",
        "explanation": "Data encryption is typically performed in the session or transport layer."
    },
    {
        "id": 194,
        "question": "When should systems administrators first assess the impact of applications or systems patches?",
        "options": [
            "A) Within five business days following installation",
            "B) Prior to installation",
            "C) No sooner than five business days following installation",
            "D) Immediately following installation"
        ],
        "correct": "B",
        "explanation": "Impact should be assessed prior to installation to avoid potential issues."
    },
    {
        "id": 195,
        "question": "Which is the most fundamental step in preventing virus attacks?",
        "options": [
            "A) Adopting and communicating a comprehensive antivirus policy",
            "B) Implementing antivirus software on desktops",
            "C) Implementing antivirus content checking at gateways",
            "D) Inoculating systems with antivirus code"
        ],
        "correct": "A",
        "explanation": "A comprehensive antivirus policy is the most fundamental step."
    },
    {
        "id": 196,
        "question": "Which is of greatest concern when performing an IS audit?",
        "options": [
            "A) Users' ability to directly modify the database",
            "B) Users' ability to submit queries to the database",
            "C) Users' ability to indirectly modify the database",
            "D) Users' ability to directly view the database"
        ],
        "correct": "A",
        "explanation": "Direct modification of the database by users is a major audit concern."
    },
    {
        "id": 197,
        "question": "What are intrusion-detection systems (IDS) primarily used for?",
        "options": ["A) To identify AND prevent intrusion attempts", "B) To prevent intrusion attempts", "C) Forensic incident response", "D) To identify intrusion attempts"],
        "correct": "D",
        "explanation": "IDS are primarily used to identify intrusion attempts."
    },
    {
        "id": 198,
        "question": "The IS auditor is more concerned with effectiveness and utilization of assets than with access controls. True or false?",
        "options": ["A) True", "B) False"],
        "correct": "B",
        "explanation": "The auditor is more concerned with access controls, policies, and safeguards than with asset utilization."
    },
    {
        "id": 199,
        "question": "If a programmer has update access to a live system, IS auditors are more concerned with his ability to initiate/modify transactions than his ability to authorize. True or false?",
        "options": ["A) True", "B) False"],
        "correct": "A",
        "explanation": "Auditors worry more about ability to initiate/modify transactions and access production."
    },
    {
        "id": 200,
        "question": "Organizations should use off-site storage to maintain _____ of critical information within backup files.",
        "options": ["A) Confidentiality", "B) Integrity", "C) Redundancy", "D) Concurrency"],
        "correct": "C",
        "explanation": "Redundancy provides both integrity and availability."
    },
    # ---- Questions 201-300 ----
    {
        "id": 201,
        "question": "The purpose of business continuity planning and disaster-recovery planning is to:",
        "options": [
            "A) Transfer the risk and impact of a business interruption or disaster",
            "B) Mitigate, or reduce, the risk and impact of a business interruption or disaster",
            "C) Accept the risk and impact of a business",
            "D) Eliminate the risk and impact of a business interruption or disaster"
        ],
        "correct": "B",
        "explanation": "The primary purpose is to mitigate, or reduce, the risk and impact; complete elimination is impossible."
    },
    {
        "id": 202,
        "question": "If a database is restored from information backed up before the last system image, what is recommended?",
        "options": [
            "A) The system should be restarted after the last transaction.",
            "B) The system should be restarted before the last transaction.",
            "C) The system should be restarted at the first transaction.",
            "D) The system should be restarted on the last transaction."
        ],
        "correct": "B",
        "explanation": "Restart before the last transaction so the final transaction can be reprocessed."
    },
    {
        "id": 203,
        "question": "An off-site processing facility should be easily identifiable externally. True or false?",
        "options": ["A) True", "B) False"],
        "correct": "B",
        "explanation": "It should NOT be easily identifiable externally to avoid sabotage or attacks."
    },
    {
        "id": 204,
        "question": "Which is the dominating objective of BCP and DRP?",
        "options": [
            "A) To protect human life",
            "B) To mitigate the risk and impact of a business interruption",
            "C) To eliminate the risk and impact of a business interruption",
            "D) To transfer the risk and impact of a business interruption"
        ],
        "correct": "A",
        "explanation": "The overriding priority is always protection of human life."
    },
    {
        "id": 205,
        "question": "How can minimizing single points of failure best be controlled?",
        "options": [
            "A) By implementing redundant systems and applications onsite",
            "B) By geographically dispersing resources",
            "C) By retaining onsite data backup in fireproof vaults",
            "D) By preparing BCP and DRP documents for commonly identified disasters"
        ],
        "correct": "B",
        "explanation": "Geographically dispersing resources reduces the risk of common disaster affecting all systems."
    },
    {
        "id": 206,
        "question": "Mitigating risk usually takes priority over transferring risk to an insurer. True or false?",
        "options": ["A) True", "B) False"],
        "correct": "A",
        "explanation": "Direct risk reduction is more important for operational continuity."
    },
    {
        "id": 207,
        "question": "Off-site data storage should be kept synchronized for recovery of time-sensitive data like:",
        "options": ["A) Financial reporting", "B) Sales reporting", "C) Inventory reporting", "D) Transaction processing"],
        "correct": "D",
        "explanation": "Transaction processing data must be synchronized to ensure accurate recovery."
    },
    {
        "id": 208,
        "question": "What is an acceptable recovery mechanism for extremely time-sensitive transaction processing?",
        "options": ["A) Off-site remote journaling", "B) Electronic vaulting", "C) Shadow file processing", "D) Storage area network"],
        "correct": "C",
        "explanation": "Shadow file processing provides quick mirroring and recovery."
    },
    {
        "id": 209,
        "question": "Off-site data backup should be geographically separated so as to _____ the risk of a widespread disaster.",
        "options": ["A) Accept", "B) Eliminate", "C) Transfer", "D) Mitigate"],
        "correct": "D",
        "explanation": "Geographical separation mitigates the risk of widespread disasters."
    },
    {
        "id": 210,
        "question": "Why is a source code escrow clause in an application vendor agreement important?",
        "options": [
            "A) To segregate systems development and live environments",
            "B) To protect the organization from copyright disputes",
            "C) To ensure that sufficient code is available when needed",
            "D) To ensure source code remains available even if the vendor goes out of business"
        ],
        "correct": "D",
        "explanation": "Source code escrow ensures access to the code if the vendor fails."
    },
    {
        "id": 211,
        "question": "What uses questionnaires to lead the user through a series of choices to reach a conclusion?",
        "options": ["A) Logic trees", "B) Decision trees", "C) Decision algorithms", "D) Logic algorithms"],
        "correct": "B",
        "explanation": "Decision trees use a series of questions to guide users to a conclusion."
    },
    {
        "id": 212,
        "question": "What protects an application purchaser's ability to fix or change an application if the vendor goes out of business?",
        "options": ["A) Assigning copyright to the organization", "B) Program back doors", "C) Source code escrow", "D) Internal programming expertise"],
        "correct": "C",
        "explanation": "Source code escrow allows the organization to access and modify the source code."
    },
    {
        "id": 213,
        "question": "Who is ultimately responsible for providing requirement specifications to the software development team?",
        "options": ["A) The project sponsor", "B) The project members", "C) The project leader", "D) The project steering committee"],
        "correct": "A",
        "explanation": "The project sponsor is responsible for ensuring requirement specifications are provided."
    },
    {
        "id": 214,
        "question": "What should regression testing use to obtain accurate conclusions about changes?",
        "options": ["A) Contrived data", "B) Independently created data", "C) Live data", "D) Data from previous tests"],
        "correct": "D",
        "explanation": "Regression testing should use data from previous tests for accurate conclusions."
    },
    {
        "id": 215,
        "question": "An IS auditor should review functional requirements to ensure the project is designed to:",
        "options": ["A) Meet business objectives", "B) Enforce data security", "C) Be culturally feasible", "D) Be financially feasible"],
        "correct": "A",
        "explanation": "The primary role is to ensure the system meets business objectives."
    },
    {
        "id": 216,
        "question": "Which process is performed during the design phase of the SDLC model?",
        "options": ["A) Develop test plans.", "B) Baseline procedures to prevent scope creep.", "C) Define the need and map to requirements.", "D) Program and test the new system."],
        "correct": "B",
        "explanation": "Procedures to prevent scope creep are established during the design phase."
    },
    {
        "id": 217,
        "question": "When should application controls be considered in system development?",
        "options": [
            "A) After application unit testing",
            "B) After application module testing",
            "C) After application systems testing",
            "D) As early as possible, even in development of functional specifications"
        ],
        "correct": "D",
        "explanation": "Controls should be considered as early as possible, even during functional specifications."
    },
    {
        "id": 218,
        "question": "What is used to develop strategically important systems faster, reduce costs, and maintain quality?",
        "options": ["A) Rapid application development (RAD)", "B) GANTT", "C) PERT", "D) Decision trees"],
        "correct": "A",
        "explanation": "RAD is a methodology for faster development with maintained quality."
    },
    {
        "id": 219,
        "question": "Test and development environments should be separated. True or false?",
        "options": ["A) True", "B) False"],
        "correct": "A",
        "explanation": "They should be separated to maintain stability and integrity of testing."
    },
    {
        "id": 220,
        "question": "What kind of testing should programmers perform following any changes to an application?",
        "options": ["A) Unit, module, and full regression testing", "B) Module testing", "C) Unit testing", "D) Regression testing"],
        "correct": "A",
        "explanation": "Unit, module, and full regression testing ensure changes work and don't introduce new issues."
    },
    {
        "id": 221,
        "question": "Which uses a prototype that can be updated continually to meet changing requirements?",
        "options": ["A) PERT", "B) Rapid application development (RAD)", "C) Function point analysis (FPA)", "D) GANTT"],
        "correct": "B",
        "explanation": "RAD focuses on continuous iteration and prototype updates."
    },
    {
        "id": 222,
        "question": "What is the most common reason for information systems failing to meet user needs?",
        "options": [
            "A) Lack of funding",
            "B) Inadequate user participation during system requirements definition",
            "C) Inadequate senior management participation",
            "D) Poor IT strategic planning"
        ],
        "correct": "B",
        "explanation": "Inadequate user participation during requirements definition is the most common cause."
    },
    {
        "id": 223,
        "question": "Who is responsible for the overall direction, costs, and timetables for systems-development projects?",
        "options": ["A) The project sponsor", "B) The project steering committee", "C) Senior management", "D) The project team leader"],
        "correct": "B",
        "explanation": "The project steering committee oversees overall direction, budgets, and schedules."
    },
    {
        "id": 224,
        "question": "When should plans for user acceptance testing be prepared?",
        "options": [
            "A) In the requirements definition phase",
            "B) In the feasibility phase",
            "C) In the design phase",
            "D) In the development phase"
        ],
        "correct": "A",
        "explanation": "UAT should be planned early, during requirements definition, to ensure needs are met."
    },
    {
        "id": 225,
        "question": "What often results in the greatest negative impact on implementation of new application software?",
        "options": [
            "A) Failing to perform user acceptance testing",
            "B) Lack of user training",
            "C) Lack of software documentation",
            "D) Insufficient unit, module, and systems testing"
        ],
        "correct": "A",
        "explanation": "Failing to perform UAT has the most significant negative impact."
    },
    {
        "id": 226,
        "question": "Input/output controls should be implemented for which applications in an integrated systems environment?",
        "options": [
            "A) The receiving application",
            "B) The sending application",
            "C) Both the sending and receiving applications",
            "D) Output on the sending application and input on the receiving application"
        ],
        "correct": "C",
        "explanation": "Controls should be implemented on both sending and receiving applications."
    },
    {
        "id": 227,
        "question": "Authentication techniques for EDI systems are crucial to prevent:",
        "options": ["A) Unsynchronized transactions", "B) Unauthorized transactions", "C) Inaccurate transactions", "D) Incomplete transactions"],
        "correct": "B",
        "explanation": "Authentication prevents unauthorized transactions."
    },
    {
        "id": 228,
        "question": "After identifying potential security vulnerabilities, what should be the IS auditor's next step?",
        "options": [
            "A) Evaluate potential countermeasures",
            "B) Implement effective countermeasures",
            "C) Perform a business impact analysis of the threats",
            "D) Immediately advise senior management"
        ],
        "correct": "C",
        "explanation": "Conduct a business impact analysis to understand threats and prioritize mitigation."
    },
    {
        "id": 229,
        "question": "What is the primary security concern for EDI environments?",
        "options": ["A) Transaction authentication", "B) Transaction completeness", "C) Transaction accuracy", "D) Transaction authorization"],
        "correct": "D",
        "explanation": "Transaction authorization ensures only authorized parties can initiate transactions."
    },
    {
        "id": 230,
        "question": "Which exploit vulnerabilities to cause loss or damage to the organization?",
        "options": ["A) Exposures", "B) Threats", "C) Hazards", "D) Insufficient controls"],
        "correct": "B",
        "explanation": "Threats exploit vulnerabilities leading to potential loss or damage."
    },
    {
        "id": 231,
        "question": "Business process re-engineering often results in _____ automation, which results in _____ number of people using technology.",
        "options": ["A) Increased; a greater", "B) Increased; a fewer", "C) Less; a fewer", "D) Increased; the same"],
        "correct": "A",
        "explanation": "BPR increases automation, leading to a greater number of people using technology."
    },
    {
        "id": 232,
        "question": "When business processes are re-engineered, the IS auditor should identify and quantify the impact of removed controls. True or false?",
        "options": ["A) True", "B) False"],
        "correct": "A",
        "explanation": "It is crucial to assess the impact on controls after reengineering."
    },
    {
        "id": 233,
        "question": "When should an edit check to verify availability of funds be completed at the EFT interface?",
        "options": [
            "A) Before transaction completion",
            "B) Immediately after an EFT is initiated",
            "C) During run-to-run total testing",
            "D) Before an EFT is initiated"
        ],
        "correct": "D",
        "explanation": "Verify availability before initiating an EFT to ensure success."
    },
    {
        "id": 234,
        "question": "_____ should be implemented as early as data preparation to support data integrity.",
        "options": ["A) Control totals", "B) Authentication controls", "C) Parity bits", "D) Authorization controls"],
        "correct": "A",
        "explanation": "Control totals support data integrity from the earliest stages."
    },
    {
        "id": 235,
        "question": "What is used as a control to detect loss, corruption, or duplication of data?",
        "options": ["A) Redundancy check", "B) Reasonableness check", "C) Hash totals", "D) Accuracy check"],
        "correct": "C",
        "explanation": "Hash totals verify data integrity and detect loss, corruption, or duplication."
    },
    {
        "id": 236,
        "question": "Data edits are implemented before processing and are considered which type of control?",
        "options": ["A) Deterrent integrity controls", "B) Detective integrity controls", "C) Corrective integrity controls", "D) Preventative integrity controls"],
        "correct": "D",
        "explanation": "Data edits are preventive controls that check accuracy and validity before processing."
    },
    {
        "id": 237,
        "question": "Processing controls ensure data is processed only through:",
        "options": ["A) Documented routines", "B) Authorized routines", "C) Accepted routines", "D) Approved routines"],
        "correct": "B",
        "explanation": "Processing must occur only through authorized routines."
    },
    {
        "id": 238,
        "question": "What is a data validation edit control that matches input data to an occurrence rate?",
        "options": ["A) Accuracy check", "B) Completeness check", "C) Reasonableness check", "D) Redundancy check"],
        "correct": "C",
        "explanation": "A reasonableness check ensures data is logical and within expected parameters."
    },
    {
        "id": 239,
        "question": "Database snapshots can provide an excellent audit trail. True or false?",
        "options": ["A) True", "B) False"],
        "correct": "A",
        "explanation": "Snapshots capture the database state at a point in time, offering an effective audit trail."
    },
    {
        "id": 240,
        "question": "An IS auditor using statistical sample to inventory tape library is performing a:",
        "options": ["A) Substantive test", "B) Compliance test", "C) Integrated test", "D) Continuous audit"],
        "correct": "A",
        "explanation": "Statistical sampling for inventory is a substantive test for completeness/accuracy."
    },
    {
        "id": 241,
        "question": "An IS auditor reviewing access to verify new user forms were correctly authorized is an example of:",
        "options": ["A) Variable sampling", "B) Substantive testing", "C) Compliance testing", "D) Stop-or-go sampling"],
        "correct": "C",
        "explanation": "Compliance testing verifies that controls are being followed per policies."
    },
    {
        "id": 242,
        "question": "The decisions and actions of an IS auditor are MOST likely to affect which risk?",
        "options": ["A) Inherent", "B) Detection", "C) Control", "D) Business"],
        "correct": "B",
        "explanation": "Detection risk is directly influenced by the auditor's procedures."
    },
    {
        "id": 243,
        "question": "Overall business risk for a particular threat can be expressed as:",
        "options": [
            "A) The product of probability and magnitude of impact.",
            "B) The magnitude of the impact.",
            "C) The likelihood of the threat exploiting a vulnerability.",
            "D) The collective judgment of the risk assessment team."
        ],
        "correct": "A",
        "explanation": "Business risk = probability × impact."
    },
    {
        "id": 244,
        "question": "Which of the following is a substantive test?",
        "options": [
            "A) Checking a list of exception reports",
            "B) Ensuring approval for parameter changes",
            "C) Using a statistical sample to inventory the tape library",
            "D) Reviewing password history reports"
        ],
        "correct": "C",
        "explanation": "Substantive testing verifies the integrity of actual records, like inventorying tapes."
    },
    {
        "id": 245,
        "question": "Which is a benefit of a risk-based approach to audit planning?",
        "options": [
            "A) Audit scheduling may be done months in advance.",
            "B) Budgets are more likely to be met.",
            "C) Staff are exposed to various technologies.",
            "D) Resources are allocated to areas of highest concern."
        ],
        "correct": "D",
        "explanation": "Risk-based planning directs resources to the highest risk areas."
    },
    {
        "id": 246,
        "question": "An audit charter should:",
        "options": [
            "A) Be dynamic and change often.",
            "B) Clearly state audit objectives and delegation of authority.",
            "C) Document audit procedures.",
            "D) Outline the overall authority, scope, and responsibilities."
        ],
        "correct": "D",
        "explanation": "The audit charter defines the audit function's role, authority, scope, and responsibilities."
    },
    {
        "id": 247,
        "question": "The MAJOR advantage of risk assessment over the baseline approach is that it ensures:",
        "options": [
            "A) Information assets are overprotected.",
            "B) A basic level of protection is applied regardless of asset value.",
            "C) Appropriate levels of protection are applied to information assets.",
            "D) Equal resources are devoted to all assets."
        ],
        "correct": "C",
        "explanation": "Risk assessment applies protection proportional to asset value and risk."
    },
    {
        "id": 248,
        "question": "Which sampling method is MOST useful when testing for compliance?",
        "options": ["A) Attribute sampling", "B) Variable sampling", "C) Stratified mean per unit", "D) Difference estimation"],
        "correct": "A",
        "explanation": "Attribute sampling tests for the presence or absence of a specific control."
    },
    {
        "id": 249,
        "question": "The MOST likely reason e-mail systems are useful for litigation evidence is:",
        "options": [
            "A) Multiple cycles of backup files remain available.",
            "B) Access controls establish accountability.",
            "C) Data classification regulates communication.",
            "D) Clear policy ensures evidence availability."
        ],
        "correct": "A",
        "explanation": "Backup files often retain data even after user deletion, making them valuable evidence."
    },
    {
        "id": 250,
        "question": "An IS auditor assigned to post-implementation review may have impaired independence if they:",
        "options": [
            "A) Implemented a specific control during development.",
            "B) Designed an embedded audit module.",
            "C) Participated as a team member without operational responsibilities.",
            "D) Provided consulting advice on best practices."
        ],
        "correct": "A",
        "explanation": "Implementing a control during development impairs independence."
    },
    {
        "id": 251,
        "question": "The PRIMARY advantage of a continuous audit approach is that it:",
        "options": [
            "A) Does not require collecting evidence during processing.",
            "B) Requires immediate review and follow-up.",
            "C) Can improve system security in high-volume time-sharing environments.",
            "D) Does not depend on system complexity."
        ],
        "correct": "C",
        "explanation": "Continuous auditing is beneficial in high-transaction environments for ongoing monitoring."
    },
    {
        "id": 252,
        "question": "The PRIMARY purpose of audit trails is to:",
        "options": [
            "A) Improve user response time.",
            "B) Establish accountability and responsibility for processed transactions.",
            "C) Improve operational efficiency.",
            "D) Provide useful information to auditors tracking transactions."
        ],
        "correct": "B",
        "explanation": "Audit trails establish accountability for transactions."
    },
    {
        "id": 253,
        "question": "When developing a risk-based audit strategy, an IS auditor should conduct a risk assessment to ensure:",
        "options": [
            "A) Controls needed to mitigate risks are in place.",
            "B) Vulnerabilities and threats are identified.",
            "C) Audit risks are considered.",
            "D) A gap analysis is appropriate."
        ],
        "correct": "C",
        "explanation": "Audit risks (risks to the audit process) must be considered to prioritize scope."
    },
    {
        "id": 254,
        "question": "To ensure audit resources deliver the best value, the FIRST step is to:",
        "options": [
            "A) Schedule audits and monitor time.",
            "B) Train IS audit staff on current technology.",
            "C) Develop the audit plan based on a detailed risk assessment.",
            "D) Monitor progress and initiate cost control measures."
        ],
        "correct": "C",
        "explanation": "Risk-based plan development focuses resources on the most critical areas."
    },
    {
        "id": 255,
        "question": "An organization's IS audit charter should specify the:",
        "options": [
            "A) Short- and long-term plans for IS audit engagements.",
            "B) Objectives and scope of IS audit engagements.",
            "C) Detailed training plan for IS audit staff.",
            "D) Role of the IS audit function."
        ],
        "correct": "D",
        "explanation": "The charter defines the role, scope, and authority of the audit function."
    },
    {
        "id": 256,
        "question": "An IS auditor evaluating management's risk assessment should FIRST review:",
        "options": [
            "A) The controls already in place.",
            "B) The effectiveness of controls.",
            "C) The mechanism for monitoring risks.",
            "D) The threats/vulnerabilities affecting the assets."
        ],
        "correct": "D",
        "explanation": "First understand threats and vulnerabilities before reviewing controls."
    },
    {
        "id": 257,
        "question": "In audit planning, the MOST critical step is identifying:",
        "options": ["A) Areas of high risk.", "B) Skill sets of audit staff.", "C) Test steps.", "D) Time allotted."],
        "correct": "A",
        "explanation": "Identifying high-risk areas is the most critical step."
    },
    {
        "id": 258,
        "question": "The extent of data collection during an IS audit should be determined based on:",
        "options": [
            "A) Availability of critical information.",
            "B) Auditor's familiarity with circumstances.",
            "C) Auditee's ability to find evidence.",
            "D) Purpose and scope of the audit being done."
        ],
        "correct": "D",
        "explanation": "Data collection extent is directly related to the audit's purpose and scope."
    },
    {
        "id": 259,
        "question": "An assessment of risk during audit planning provides:",
        "options": [
            "A) Reasonable assurance that material items will be covered.",
            "B) Definite assurance that material items will be covered.",
            "C) Reasonable assurance that all items will be covered.",
            "D) Sufficient assurance that all items will be covered."
        ],
        "correct": "A",
        "explanation": "Risk assessment provides reasonable assurance that material items are covered."
    },
    {
        "id": 260,
        "question": "An IS auditor should use statistical sampling rather than judgmental sampling when:",
        "options": [
            "A) The probability of error must be objectively quantified.",
            "B) The auditor wishes to avoid sampling risk.",
            "C) Generalized audit software is unavailable.",
            "D) The tolerable error rate cannot be determined."
        ],
        "correct": "A",
        "explanation": "Statistical sampling allows objective quantification of error probabilities."
    },
    {
        "id": 261,
        "question": "During the planning stage of an IS audit, the PRIMARY goal is to:",
        "options": ["A) Address audit objectives", "B) Collect sufficient evidence", "C) Specify appropriate tests", "D) Minimize audit resources"],
        "correct": "A",
        "explanation": "ISACA standards require planning to address audit objectives."
    },
    {
        "id": 262,
        "question": "When selecting audit procedures, an IS auditor should ensure that:",
        "options": [
            "A) Sufficient evidence will be collected",
            "B) All significant deficiencies will be corrected",
            "C) All material weaknesses will be identified",
            "D) Audit costs are kept minimal"
        ],
        "correct": "A",
        "explanation": "Professional judgment is used to ensure sufficient and appropriate evidence collection."
    },
    {
        "id": 263,
        "question": "An IS auditor evaluating logical access controls should FIRST:",
        "options": [
            "A) Document the controls applied to access paths.",
            "B) Test controls over access paths.",
            "C) Evaluate the security environment against policies.",
            "D) Obtain an understanding of the security risks to information processing."
        ],
        "correct": "D",
        "explanation": "First understand the security risks through documentation and risk assessment."
    },
    {
        "id": 264,
        "question": "The PRIMARY purpose of an IT forensic audit is:",
        "options": [
            "A) To participate in corporate fraud investigations.",
            "B) The systematic collection of evidence after a system irregularity.",
            "C) To assess correctness of financial statements.",
            "D) To determine criminal activity."
        ],
        "correct": "B",
        "explanation": "Forensic audit focuses on systematic evidence collection after an irregularity."
    },
    {
        "id": 265,
        "question": "An IS auditor finds one instance of a server backup failure. What should the auditor do?",
        "options": [
            "A) Issue an audit finding",
            "B) Seek an explanation from IS management",
            "C) Review data classifications on the server",
            "D) Expand the sample of logs reviewed"
        ],
        "correct": "D",
        "explanation": "Expand the sample to determine if the issue is isolated or systemic before concluding."
    },
    {
        "id": 266,
        "question": "Which tool is MOST suitable for analyzing audit trails to discover anomalies in user behavior?",
        "options": ["A) CASE tools", "B) Embedded data collection tools", "C) Heuristic scanning tools", "D) Trend/variance detection tools"],
        "correct": "D",
        "explanation": "Trend/variance detection tools analyze audit trails for anomalies."
    },
    {
        "id": 267,
        "question": "An IS auditor evaluating a corporate network for employee penetration should be MOST concerned about:",
        "options": [
            "A) External modems connected to the network",
            "B) Users can install software on desktops",
            "C) Network monitoring is very limited",
            "D) Many user IDs have identical passwords"
        ],
        "correct": "D",
        "explanation": "Identical passwords for many IDs pose the greatest risk for unauthorized access."
    },
    {
        "id": 268,
        "question": "The PRIMARY advantage of using computer forensic software is:",
        "options": [
            "A) The preservation of the chain of custody for electronic evidence.",
            "B) Time and cost savings.",
            "C) Efficiency and effectiveness.",
            "D) Ability to search for IP violations."
        ],
        "correct": "A",
        "explanation": "Forensic software preserves the chain of custody, ensuring evidence admissibility."
    },
    {
        "id": 269,
        "question": "To confirm imported data are complete, an IS auditor should:",
        "options": [
            "A) Match control totals of imported data to original data.",
            "B) Sort the data to confirm order.",
            "C) Review the first 100 records.",
            "D) Filter data for different categories and match."
        ],
        "correct": "A",
        "explanation": "Matching control totals ensures completeness of imported data."
    },
    {
        "id": 270,
        "question": "Which audit technique is BEST to identify payroll overpayments for the previous year?",
        "options": ["A) Test data", "B) Generalized audit software", "C) Integrated test facility", "D) Embedded audit module"],
        "correct": "B",
        "explanation": "Generalized audit software can recompute payroll and detect overpayments."
    },
    {
        "id": 271,
        "question": "During a security audit, the IS auditor finds no documented security procedures. The auditor should:",
        "options": [
            "A) Create the procedures document.",
            "B) Terminate the audit.",
            "C) Conduct compliance testing.",
            "D) Identify and evaluate existing practices."
        ],
        "correct": "D",
        "explanation": "The auditor should identify and evaluate existing practices, not create documentation."
    },
    {
        "id": 272,
        "question": "After identifying threats and potential impacts in a risk analysis, the auditor should next:",
        "options": [
            "A) Identify and assess management's risk process.",
            "B) Identify information assets and systems.",
            "C) Disclose threats and impacts to management.",
            "D) Identify and evaluate existing controls."
        ],
        "correct": "D",
        "explanation": "Next step: identify and evaluate existing controls to mitigate risks."
    },
    {
        "id": 273,
        "question": "What is the most critical concern regarding network attacks?",
        "options": [
            "A) Lack of reporting of a successful attack",
            "B) Failure to notify police of an attempted intrusion",
            "C) Lack of periodic examination of access rights",
            "D) Lack of notification to the public of an intrusion"
        ],
        "correct": "A",
        "explanation": "Lack of reporting a successful attack hinders timely response and remediation."
    },
    {
        "id": 274,
        "question": "Which would normally be the MOST reliable evidence for an auditor?",
        "options": [
            "A) A confirmation letter from a third party verifying an account balance",
            "B) Assurance from line management that an application works",
            "C) Trend data from Internet sources",
            "D) Ratio analysis from reports supplied by line management"
        ],
        "correct": "A",
        "explanation": "Third-party confirmations are the most reliable source of evidence."
    },
    {
        "id": 275,
        "question": "When evaluating the collective effect of controls, an IS auditor should be aware of:",
        "options": [
            "A) The point at which controls are exercised as data flow through the system.",
            "B) Only preventive and detective controls are relevant.",
            "C) Corrective controls are only compensating.",
            "D) Classification allows determination of missing controls."
        ],
        "correct": "A",
        "explanation": "Focus on when and where controls are applied in the data flow."
    },
    {
        "id": 276,
        "question": "Which audit technique provides the BEST evidence of segregation of duties?",
        "options": ["A) Discussion with management", "B) Review of the organization chart", "C) Observation and interviews", "D) Testing of user access rights"],
        "correct": "C",
        "explanation": "Observation and interviews directly assess what tasks staff members perform."
    },
    {
        "id": 277,
        "question": "To determine the extent of customer name duplications, an IS auditor would use:",
        "options": [
            "A) Test data to validate input.",
            "B) Test data to determine sort capabilities.",
            "C) Generalized audit software to search for address field duplications.",
            "D) Generalized audit software to search for account field duplications."
        ],
        "correct": "C",
        "explanation": "Address fields are more consistent than first names; GAS can search for duplicates."
    },
    {
        "id": 278,
        "question": "Which is an advantage of PERT over CPM?",
        "options": [
            "A) PERT considers different scenarios for activity completion.",
            "B) PERT deals with known activities and definite completion times.",
            "C) CPM considers different scenarios.",
            "D) CPM evaluates buffer needed."
        ],
        "correct": "A",
        "explanation": "PERT handles uncertainty by considering optimistic, pessimistic, and most likely times."
    },
    {
        "id": 279,
        "question": "The GREATEST risk of an inadequate policy definition for data ownership is:",
        "options": [
            "A) User management coordination does not exist.",
            "B) Specific user accountability cannot be established.",
            "C) Audit recommendations may not be implemented.",
            "D) Users may have unauthorized access to originate, modify, or delete data."
        ],
        "correct": "D",
        "explanation": "Unauthorized access to data is the greatest risk."
    },
    {
        "id": 280,
        "question": "Which risk could result from inadequate software baselining?",
        "options": ["A) Scope creep", "B) Sign-off delays", "C) Software integrity violations", "D) Inadequate controls"],
        "correct": "A",
        "explanation": "Inadequate baselining leads to uncontrolled changes and scope creep."
    },
    {
        "id": 281,
        "question": "Which form of evidence is MOST reliable for an auditor?",
        "options": [
            "A) An oral statement from the auditee",
            "B) Results of a test performed by an IS auditor",
            "C) An internally generated computer accounting report",
            "D) A confirmation letter received from an outside source"
        ],
        "correct": "D",
        "explanation": "External confirmations are more reliable than internal evidence."
    },
    {
        "id": 282,
        "question": "An IS auditor reviews an organizational chart PRIMARILY for:",
        "options": [
            "A) An understanding of workflows.",
            "B) Investigating communication channels.",
            "C) Understanding responsibilities and authority of individuals.",
            "D) Investigating network connected to employees."
        ],
        "correct": "C",
        "explanation": "Organizational charts show responsibilities and authority for segregation of duties."
    },
    {
        "id": 283,
        "question": "An IS auditor performing an audit of a network operating system should review which user feature?",
        "options": [
            "A) Availability of online network documentation",
            "B) Support of terminal access to remote hosts",
            "C) Handling file transfer between hosts and interuser communications",
            "D) Performance management, audit, and control"
        ],
        "correct": "A",
        "explanation": "Online documentation is a user-oriented feature."
    },
    {
        "id": 284,
        "question": "To determine if access to program documentation is restricted, an IS auditor would MOST likely:",
        "options": [
            "A) Evaluate record retention plans for off-premises storage.",
            "B) Interview programmers about procedures currently followed.",
            "C) Compare utilization records to operations schedules.",
            "D) Review data file access records."
        ],
        "correct": "B",
        "explanation": "Interviewing programmers provides direct insight into current access restriction practices."
    },
    {
        "id": 285,
        "question": "An advantage of an integrated test facility (ITF) is:",
        "options": [
            "A) It uses actual master files and the auditor does not review transaction source.",
            "B) Periodic testing does not require separate test processes.",
            "C) It validates application systems and tests ongoing operation.",
            "D) The need to prepare test data is eliminated."
        ],
        "correct": "B",
        "explanation": "ITF allows test transactions to be processed in live systems without separate environments."
    },
    {
        "id": 286,
        "question": "An IS auditor finds 50% of payment calculations do not match predetermined totals. Next step?",
        "options": [
            "A) Design further tests of the calculations in error.",
            "B) Identify variables that may have caused inaccurate results.",
            "C) Examine some of the test cases to confirm results.",
            "D) Document results and prepare a report of findings."
        ],
        "correct": "C",
        "explanation": "First confirm the errors by examining test cases before further investigation."
    },
    {
        "id": 287,
        "question": "The BEST method of proving accuracy of a system tax calculation is:",
        "options": [
            "A) Detailed visual review of source code.",
            "B) Recreating program logic using generalized audit software.",
            "C) Preparing simulated transactions and comparing to predetermined results.",
            "D) Automatic flowcharting of source code."
        ],
        "correct": "C",
        "explanation": "Simulated transactions with predetermined results provide the most reliable validation."
    },
    {
        "id": 288,
        "question": "An IS auditor reviewing an application's controls would evaluate the:",
        "options": [
            "A) Efficiency of the application in meeting business processes.",
            "B) Impact of any exposures discovered.",
            "C) Business processes served by the application.",
            "D) Application's optimization."
        ],
        "correct": "B",
        "explanation": "The primary goal is to assess control mechanisms and identify exposures."
    },
    {
        "id": 289,
        "question": "In an audit of an inventory application, which provides the BEST evidence that purchase orders are valid?",
        "options": [
            "A) Testing whether inappropriate personnel can change application parameters.",
            "B) Tracing purchase orders to a computer listing.",
            "C) Comparing receiving reports to purchase order details.",
            "D) Reviewing application documentation."
        ],
        "correct": "A",
        "explanation": "Testing access controls ensures only authorized personnel can create valid purchase orders."
    },
    {
        "id": 290,
        "question": "Which online auditing technique is most effective for early detection of errors or irregularities?",
        "options": ["A) Embedded audit module", "B) Integrated test facility", "C) Snapshots", "D) Audit hooks"],
        "correct": "D",
        "explanation": "Audit hooks allow proactive monitoring and response to specific transactions as they occur."
    },
    {
        "id": 291,
        "question": "When assessing the design of network monitoring controls, an IS auditor should FIRST review:",
        "options": ["A) Topology diagrams.", "B) Bandwidth usage.", "C) Traffic analysis reports.", "D) Bottleneck locations."],
        "correct": "A",
        "explanation": "Up-to-date topology diagrams are essential for effective network monitoring."
    },
    {
        "id": 292,
        "question": "While conducting an audit, an IS auditor detects a virus. The next step is to:",
        "options": [
            "A) Observe the response mechanism.",
            "B) Clear the virus from the network.",
            "C) Inform appropriate personnel immediately.",
            "D) Ensure deletion of the virus."
        ],
        "correct": "C",
        "explanation": "Immediately notify the appropriate personnel; do not try to remove the virus."
    },
    {
        "id": 293,
        "question": "A substantive test to verify tape library inventory records is:",
        "options": [
            "A) Determining whether bar code readers are installed.",
            "B) Determining whether movement of tapes is authorized.",
            "C) Conducting a physical count of the tape inventory.",
            "D) Checking if receipts and issues are accurately recorded."
        ],
        "correct": "C",
        "explanation": "A physical count is a substantive test providing direct evidence of accuracy."
    },
    {
        "id": 294,
        "question": "In a computer forensic investigation, the IS auditor should be MOST concerned with:",
        "options": ["A) Analysis.", "B) Evaluation.", "C) Preservation.", "D) Disclosure."],
        "correct": "C",
        "explanation": "Preserving evidence is paramount to ensure admissibility in legal proceedings."
    },
    {
        "id": 295,
        "question": "An IS auditor interviewing a payroll clerk finds answers do not support job descriptions. The auditor should:",
        "options": [
            "A) Conclude that controls are inadequate.",
            "B) Expand the scope to include substantive testing.",
            "C) Place greater reliance on previous audits.",
            "D) Suspend the audit."
        ],
        "correct": "B",
        "explanation": "Expand testing to verify controls; don't conclude inadequacy without further investigation."
    },
    {
        "id": 296,
        "question": "An IS auditor recommends a specific vendor product to address a vulnerability. The auditor has failed to exercise:",
        "options": ["A) Professional independence", "B) Organizational independence", "C) Technical competence", "D) Professional competence"],
        "correct": "A",
        "explanation": "Recommendating a specific vendor compromises professional independence."
    },
    {
        "id": 297,
        "question": "The PRIMARY reason an IS auditor performs a functional walkthrough during the preliminary phase is to:",
        "options": [
            "A) Understand the business process.",
            "B) Comply with auditing standards.",
            "C) Identify control weakness.",
            "D) Plan substantive testing."
        ],
        "correct": "A",
        "explanation": "The walkthrough is to understand the business processes and systems under audit."
    },
    {
        "id": 298,
        "question": "To evaluate program change controls, an IS auditor uses source code comparison software to:",
        "options": [
            "A) Examine source program changes without information from IS personnel.",
            "B) Detect a source program change made between acquiring a copy and the comparison run.",
            "C) Confirm the control copy is the current production version.",
            "D) Ensure all changes in the current source copy are detected."
        ],
        "correct": "A",
        "explanation": "Source code comparison allows independent verification without relying on IS personnel."
    },
    {
        "id": 299,
        "question": "The PRIMARY purpose for meeting with auditees prior to closing a review is to:",
        "options": [
            "A) Confirm no important issues were overlooked.",
            "B) Gain agreement on the findings.",
            "C) Receive feedback on audit procedures.",
            "D) Test the structure of the final presentation."
        ],
        "correct": "B",
        "explanation": "The main reason is to gain auditee agreement on findings."
    },
    {
        "id": 300,
        "question": "Which audit technique BEST aids in determining unauthorized program changes since the last update?",
        "options": [
            "A) Test data run",
            "B) Code review",
            "C) Automated code comparison",
            "D) Review of code migration procedures"
        ],
        "correct": "C",
        "explanation": "Automated code comparison directly detects differences between versions."
    },
# Question 301 to 450

    {
        "id": 301,
        "question": "Though management has stated otherwise, an IS auditor has reasons to believe that the organization is using software that is not licensed. In this situation, the IS auditor should:",
        "options": [
            "A) Include the statement of management in the audit report.",
            "B) Identify whether such software is, indeed, being used by the organization.",
            "C) Reconfirm with management the usage of the software.",
            "D) Discuss the issue with senior management since reporting this could have a negative impact on the organization."
        ],
        "correct": "B",
        "explanation": "The IS auditor must gather sufficient evidence before reporting the use of unlicensed software. Simply relying on management's claims is not enough; independent verification is required to maintain objectivity."
    },
    {
        "id": 302,
        "question": "While reviewing sensitive electronic work papers, the IS auditor noticed that they were not encrypted. This could compromise the:",
        "options": [
            "A) Audit trail of the versioning of the work papers.",
            "B) Approval of the audit phases.",
            "C) Access rights to the work papers.",
            "D) Confidentiality of the work papers."
        ],
        "correct": "D",
        "explanation": "Encryption is essential to ensure the confidentiality of sensitive electronic work papers. Without encryption, they are vulnerable to unauthorized access."
    },
    {
        "id": 303,
        "question": "The MOST important reason for an IS auditor to obtain sufficient and appropriate audit evidence is to:",
        "options": [
            "A) Comply with regulatory requirements.",
            "B) Provide a basis for drawing reasonable conclusions.",
            "C) Ensure complete audit coverage.",
            "D) Perform the audit according to the defined scope."
        ],
        "correct": "B",
        "explanation": "The purpose of gathering evidence is to support the audit conclusions. This helps in identifying and validating control weaknesses."
    },
    {
        "id": 304,
        "question": "After initial investigation, an IS auditor has reasons to believe that fraud may be present. The IS auditor should:",
        "options": [
            "A) Expand activities to determine whether an investigation is warranted.",
            "B) Report the matter to the audit committee.",
            "C) Report the possibility of fraud to top management and ask how they would like to proceed.",
            "D) Consult with external legal counsel to determine the course of action to be taken."
        ],
        "correct": "A",
        "explanation": "The IS auditor must evaluate fraud indicators further before recommending a formal investigation, ensuring that the fraud suspicion is substantial."
    },
    {
        "id": 305,
        "question": "Which of the following should an IS auditor use to detect duplicate invoice records within an invoice master file?",
        "options": [
            "A) Attribute sampling",
            "B) Generalized audit software (GAS)",
            "C) Test data",
            "D) Integrated test facility (ITF)"
        ],
        "correct": "B",
        "explanation": "GAS allows for a comprehensive review of all records and can easily identify duplicate invoices, which sampling methods or other tests might miss."
    },
    {
        "id": 306,
        "question": "Which of the following would be the MOST effective audit technique for identifying segregation of duties violations in a new ERP implementation?",
        "options": [
            "A) Reviewing a report of security rights in the system",
            "B) Reviewing the complexities of authorization objects",
            "C) Building a program to identify conflicts in authorization",
            "D) Examining recent access rights violation cases"
        ],
        "correct": "C",
        "explanation": "Developing a program that can systematically identify authorization conflicts is the most efficient and effective way to identify segregation of duties violations in an ERP system."
    },
    {
        "id": 307,
        "question": "Which of the following would an IS auditor use to determine if unauthorized modifications were made to production programs?",
        "options": [
            "A) System log analysis",
            "B) Compliance testing",
            "C) Forensic analysis",
            "D) Analytical review"
        ],
        "correct": "B",
        "explanation": "Compliance testing helps verify whether the change management process was followed consistently and only authorized changes were made to production programs."
    },
    {
        "id": 308,
        "question": "During a change control audit of a production system, an IS auditor finds that the change management process is not formally documented and that some migration procedures failed. What should the IS auditor do next?",
        "options": [
            "A) Recommend redesigning the change management process.",
            "B) Gain more assurance on the findings through root cause analysis.",
            "C) Recommend that program migration be stopped until the change process is documented.",
            "D) Document the finding and present it to management."
        ],
        "correct": "B",
        "explanation": "Before making recommendations, the auditor must ensure that the incidents were indeed due to deficiencies in the change management process and not another cause."
    },
    {
        "id": 309,
        "question": "During the collection of forensic evidence, which of the following actions would MOST likely result in the destruction or corruption of evidence on a compromised system?",
        "options": [
            "A) Dumping the memory content to a file",
            "B) Generating disk images of the compromised system",
            "C) Rebooting the system",
            "D) Removing the system from the network"
        ],
        "correct": "C",
        "explanation": "Rebooting a compromised system can change the system state and potentially destroy evidence, especially in volatile memory."
    },
    {
        "id": 310,
        "question": "An IS auditor who was involved in designing an organization's business continuity plan (BCP) has been assigned to audit the plan. The IS auditor should:",
        "options": [
            "A) Decline the assignment.",
            "B) Inform management of the possible conflict of interest after completing the audit assignment.",
            "C) Inform the business continuity planning (BCP) team of the possible conflict of interest prior to beginning the assignment.",
            "D) Communicate the possibility of conflict of interest to management prior to starting the assignment."
        ],
        "correct": "D",
        "explanation": "It is important to disclose any potential conflicts of interest, like involvement in the design of the BCP, to management before proceeding with the audit."
    },
    {
        "id": 311,
        "question": "An IS auditor conducting a review of software usage and licensing discovers that numerous PCs contain unauthorized software. Which of the following actions should the IS auditor take?",
        "options": [
            "A) Personally delete all copies of the unauthorized software.",
            "B) Inform the auditee of the unauthorized software, and follow up to confirm deletion.",
            "C) Report the use of the unauthorized software and the need to prevent recurrence to auditee management.",
            "D) Take no action, as it is a commonly accepted practice and operations management is responsible for monitoring such use."
        ],
        "correct": "C",
        "explanation": "The use of unauthorized or illegal software should be prohibited by an organization. Software piracy results in inherent exposure and can result in severe fines. An IS auditor must convince the user and user management of the risk and the need to eliminate the risk."
    },
    {
        "id": 312,
        "question": "Corrective action has been taken by an auditee immediately after the identification of a reportable finding. The auditor should:",
        "options": [
            "A) Include the finding in the final report, because the IS auditor is responsible for an accurate report of all findings.",
            "B) Not include the finding in the final report, because the audit report should include only unresolved findings.",
            "C) Not include the finding in the final report, because corrective action can be verified by the IS auditor during the audit.",
            "D) Include the finding in the closing meeting for discussion purposes only."
        ],
        "correct": "A",
        "explanation": "Including the finding in the final report is a generally accepted audit practice. If an action is taken after the audit started and before it ended, the audit report should identify the finding and describe the corrective action taken."
    },
    {
        "id": 313,
        "question": "During an implementation review of a multiuser distributed application, an IS auditor finds minor weaknesses in three areas - the initial setting of parameters is improperly installed, weak passwords are being used, and some vital reports are not being checked properly. While preparing the audit report, the IS auditor should:",
        "options": [
            "A) Record the observations separately with the impact of each of them marked against each respective finding.",
            "B) Advise the manager of probable risks without recording the observations, as the control weaknesses are minor ones.",
            "C) Record the observations and the risk arising from the collective weaknesses.",
            "D) Apprise the departmental heads concerned with each observation and properly document it in the report."
        ],
        "correct": "C",
        "explanation": "Individually the weaknesses are minor; however, together they have the potential to substantially weaken the overall control structure."
    },
    {
        "id": 314,
        "question": "During an exit interview, in cases where there is disagreement regarding the impact of a finding, an IS auditor should:",
        "options": [
            "A) Ask the auditee to sign a release form accepting full legal responsibility.",
            "B) Elaborate on the significance of the finding and the risks of not correcting it.",
            "C) Report the disagreement to the audit committee for resolution.",
            "D) Accept the auditee's position since they are the process owners."
        ],
        "correct": "B",
        "explanation": "If the auditee disagrees with the impact of a finding, it is important for an IS auditor to elaborate and clarify the risks and exposures, as the auditee may not fully appreciate the magnitude of the exposure."
    },
    {
        "id": 315,
        "question": "When preparing an audit report, the IS auditor should ensure that the results are supported by:",
        "options": [
            "A) Statements from IS management.",
            "B) Workpapers of other auditors.",
            "C) An organizational control self-assessment.",
            "D) Sufficient and appropriate audit evidence."
        ],
        "correct": "D",
        "explanation": "ISACA's standard on 'reporting' requires the IS auditor to have sufficient and appropriate audit evidence to support the reported results."
    },
    {
        "id": 316,
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
        "id": 317,
        "question": "A PRIMARY benefit derived from an organization employing control self-assessment (CSA) techniques is that it:",
        "options": [
            "A) Can identify high-risk areas that might need a detailed review later.",
            "B) Is a cost-effective way to conduct a comprehensive audit.",
            "C) Engages staff in the risk management process.",
            "D) Reduces the need for external audits."
        ],
        "correct": "C",
        "explanation": "Engaging staff in the risk management process is a significant advantage of using CSA techniques. It enhances accountability and promotes a control-conscious culture."
    },
    {
        "id": 318,
        "question": "Which of the following would an IS auditor recommend for ensuring compliance with privacy regulations?",
        "options": [
            "A) Conducting periodic employee training on data protection.",
            "B) Using encryption technology for all sensitive data.",
            "C) Implementing a data classification policy.",
            "D) Establishing an incident response plan."
        ],
        "correct": "A",
        "explanation": "Regular training helps ensure that employees are aware of privacy regulations and the organization's policies, making them more effective at compliance."
    },
    {
        "id": 319,
        "question": "An IS auditor is preparing an audit report on an application under development. Which of the following aspects should be emphasized as the MOST important?",
        "options": [
            "A) That the project is on schedule.",
            "B) That proper change management processes are followed.",
            "C) That the application meets the user requirements.",
            "D) That the application is developed using a formal methodology."
        ],
        "correct": "B",
        "explanation": "Emphasizing proper change management is crucial in development projects, as it mitigates risks associated with unauthorized changes."
    },
    {
        "id": 320,
        "question": "An IS auditor has identified that an organization's firewall is configured to allow outbound traffic on all ports. What is the MOST significant risk associated with this configuration?",
        "options": [
            "A) Exposure to external threats.",
            "B) Data leakage.",
            "C) Misconfiguration of security policies.",
            "D) Increased administrative overhead."
        ],
        "correct": "B",
        "explanation": "Allowing unrestricted outbound traffic significantly increases the risk of data leakage, as sensitive information could be exfiltrated easily without appropriate controls."
    },
    {
        "id": 321,
        "question": "An IT steering committee should review information systems PRIMARILY to assess:",
        "options": [
            "A) whether IT processes support business requirements.",
            "B) if proposed system functionality is adequate.",
            "C) the stability of existing software.",
            "D) the complexity of installed technology."
        ],
        "correct": "A",
        "explanation": "The primary role of an IT steering committee is to ensure that the IS department aligns with the organization's mission and objectives. This involves assessing whether IT processes support business requirements."
    },
    {
        "id": 322,
        "question": "The MOST likely effect of the lack of senior management commitment to IT strategic planning is:",
        "options": [
            "A) a lack of investment in technology.",
            "B) a lack of a methodology for systems development.",
            "C) technology not aligning with the organization's objectives.",
            "D) an absence of control over technology contracts."
        ],
        "correct": "C",
        "explanation": "The absence of a senior management commitment can lead to misalignment between IT and organizational strategy, increasing the risk of IT projects not meeting business objectives."
    },
    {
        "id": 323,
        "question": "Which of the following is a function of an IS steering committee?",
        "options": [
            "A) Monitoring vendor-controlled change control and testing",
            "B) Ensuring a separation of duties within the information's processing environment",
            "C) Approving and monitoring major projects, the status of IS plans and budgets",
            "D) Liaising between the IS department and the end users"
        ],
        "correct": "C",
        "explanation": "The IS steering committee primarily serves as a review board for major IS projects, approving and monitoring their progress without becoming involved in routine operations."
    },
    {
        "id": 324,
        "question": "An IS steering committee should:",
        "options": [
            "A) include a mix of members from different departments and staff levels.",
            "B) ensure that IS security policies and procedures have been executed properly.",
            "C) have formal terms of reference and maintain minutes of its meetings.",
            "D) be briefed about new trends and products at each meeting by a vendor."
        ],
        "correct": "C",
        "explanation": "Maintaining detailed minutes is crucial for documenting decisions and activities. This accountability is important for informing the board of directors about the committee's actions."
    },
    {
        "id": 325,
        "question": "Involvement of senior management is MOST important in the development of:",
        "options": [
            "A) strategic plans.",
            "B) IS policies.",
            "C) IS procedures.",
            "D) standards and guidelines."
        ],
        "correct": "A",
        "explanation": "Senior management involvement is critical to ensure that strategic plans align with organizational goals and objectives."
    },
    {
        "id": 326,
        "question": "Effective IT governance will ensure that the IT plan is consistent with the organization's:",
        "options": [
            "A) business plan.",
            "B) audit plan.",
            "C) security plan.",
            "D) investment plan."
        ],
        "correct": "A",
        "explanation": "IT governance requires that IT and business strategies are aligned to support the organization's goals."
    },
    {
        "id": 327,
        "question": "Establishing the level of acceptable risk is the responsibility of:",
        "options": [
            "A) quality assurance management.",
            "B) senior business management.",
            "C) the chief information officer.",
            "D) the chief security officer."
        ],
        "correct": "B",
        "explanation": "Senior management is responsible for establishing acceptable risk levels due to their accountability for organizational operations."
    },
    {
        "id": 328,
        "question": "IT governance is PRIMARILY the responsibility of the:",
        "options": [
            "A) chief executive officer.",
            "B) board of directors.",
            "C) IT steering committee.",
            "D) audit committee."
        ],
        "correct": "B",
        "explanation": "IT governance is the responsibility of the board of directors, who provide strategic direction and oversight."
    },
    {
        "id": 329,
        "question": "As an outcome of information security governance, strategic alignment provides:",
        "options": [
            "A) security requirements driven by enterprise requirements.",
            "B) baseline security following best practices.",
            "C) institutionalized and commoditized solutions.",
            "D) an understanding of risk exposure."
        ],
        "correct": "A",
        "explanation": "Strategic alignment ensures that security requirements are aligned with the overall enterprise goals and objectives."
    },
    {
        "id": 330,
        "question": "Which of the following IT governance best practices improves strategic alignment?",
        "options": [
            "A) Supplier and partner risks are managed.",
            "B) A knowledge base on customers, products, markets, and processes is in place.",
            "C) A structure is provided that facilitates the creation and sharing of business information.",
            "D) Top management mediate between the imperatives of business and technology."
        ],
        "correct": "D",
        "explanation": "Top management mediation is essential for ensuring that IT strategies align with business needs and objectives."
    },
    {
        "id": 331,
        "question": "Effective IT governance requires organizational structures and processes to ensure that:",
        "options": [
            "A) the organization's strategies and objectives extend the IT strategy.",
            "B) the business strategy is derived from an IT strategy.",
            "C) IT governance is separate and distinct from the overall governance.",
            "D) the IT strategy extends the organization's strategies and objectives."
        ],
        "correct": "D",
        "explanation": "IT governance must align IT strategies with organizational goals, ensuring IT supports and extends those objectives."
    },
    {
        "id": 332,
        "question": "Which of the following is the MOST important element for the successful implementation of IT governance?",
        "options": [
            "A) Implementing an IT scorecard",
            "B) Identifying organizational strategies",
            "C) Performing a risk assessment",
            "D) Creating a formal security policy"
        ],
        "correct": "B",
        "explanation": "Identifying organizational strategies is crucial for aligning IT governance with business objectives."
    },
    {
        "id": 333,
        "question": "The MAJOR consideration for an IS auditor reviewing an organization's IT project portfolio is the:",
        "options": [
            "A) IT budget.",
            "B) existing IT environment.",
            "C) business plan.",
            "D) investment plan."
        ],
        "correct": "C",
        "explanation": "The alignment of IT projects with the business plan is critical for funding and prioritizing IT initiatives."
    },
    {
        "id": 334,
        "question": "When implementing an IT governance framework in an organization, the MOST important objective is:",
        "options": [
            "A) IT alignment with the business.",
            "B) accountability.",
            "C) value realization with IT.",
            "D) enhancing the return on IT investments."
        ],
        "correct": "A",
        "explanation": "The primary goal of IT governance is to ensure that IT aligns with the organization's strategic objectives."
    },
    {
        "id": 335,
        "question": "The ultimate purpose of IT governance is to:",
        "options": [
            "A) encourage optimal use of IT.",
            "B) reduce IT costs.",
            "C) decentralize IT resources across the organization.",
            "D) centralize control of IT."
        ],
        "correct": "A",
        "explanation": "IT governance aims to optimize the use of IT resources to support business objectives, not necessarily to reduce costs or centralize/decentralize resources."
    },
    {
        "id": 336,
        "question": "What is the lowest level of the IT governance maturity model where an IT balanced scorecard exists?",
        "options": [
            "A) Repeatable but Intuitive",
            "B) Defined",
            "C) Managed and Measurable",
            "D) Optimized"
        ],
        "correct": "B",
        "explanation": "The IT balanced scorecard is established at the Defined level (level 3) of the IT governance maturity model."
    },
    {
        "id": 337,
        "question": "Responsibility for the governance of IT should rest with the:",
        "options": [
            "A) IT strategy committee.",
            "B) chief information officer (CIO).",
            "C) audit committee.",
            "D) board of directors."
        ],
        "correct": "D",
        "explanation": "The ultimate accountability for IT governance resides with the board of directors, who set strategic direction and oversight."
    },
    {
        "id": 338,
        "question": "An IS auditor identifies that reports on product profitability produced by an organization's finance and marketing departments give different results. Further investigation reveals that the product definition being used by the two departments is different. What should the IS auditor recommend?",
        "options": [
            "A) User acceptance testing (UAT) occur for all reports before release into production",
            "B) Organizational data governance practices be put in place",
            "C) Standard software tools be used for report development",
            "D) Management sign-off on requirements for new reports"
        ],
        "correct": "B",
        "explanation": "Implementing data governance practices will standardize definitions and improve consistency in reporting across departments."
    },
    {
        "id": 339,
        "question": "From a control perspective, the key element in job descriptions is that they:",
        "options": [
            "A) provide instructions on how to do the job and define authority.",
            "B) are current, documented, and readily available to the employee.",
            "C) communicate management's specific job performance expectations.",
            "D) establish responsibility and accountability for the employee's actions."
        ],
        "correct": "D",
        "explanation": "Job descriptions are essential for establishing accountability and responsibility, which are crucial from a control perspective."
    },
    {
        "id": 340,
        "question": "Which of the following would BEST provide assurance of the integrity of new staff?",
        "options": [
            "A) Background screening",
            "B) References",
            "C) Bonding",
            "D) Qualifications listed on a resume"
        ],
        "correct": "A",
        "explanation": "Background screening is the most reliable method for verifying the integrity of prospective employees."
    },
    {
        "id": 341,
        "question": "When an employee is terminated from service, the MOST important action is to:",
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
        "id": 342,
        "question": "Many organizations require an employee to take a mandatory vacation (holiday) of a week or more to:",
        "options": [
            "A) Ensure the employee maintains a good quality of life, which will lead to greater productivity.",
            "B) Reduce the opportunity for an employee to commit an improper or illegal act.",
            "C) Provide proper cross-training for another employee.",
            "D) Eliminate the potential disruption caused when an employee takes vacation one day at a time."
        ],
        "correct": "B",
        "explanation": "Mandatory vacations help reduce the opportunity for improper or illegal acts by allowing another employee to review the work."
    },
    {
        "id": 343,
        "question": "A local area network (LAN) administrator normally would be restricted from:",
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
        "id": 344,
        "question": "A long-term IS employee with a strong technical background and broad managerial experience has applied for a vacant position in the IS audit department. Determining whether to hire this individual for this position should be based on the individual's experience and:",
        "options": [
            "A) Length of service, since this will help ensure technical competence.",
            "B) Age, as training in audit techniques may be impractical.",
            "C) IS knowledge, since this will bring enhanced credibility to the audit function.",
            "D) Ability, as an IS auditor, to be independent of existing IS relationships."
        ],
        "correct": "D",
        "explanation": "The candidate's ability to maintain independence is crucial for effective auditing."
    },
    {
        "id": 345,
        "question": "An IS auditor should be concerned when a telecommunication analyst:",
        "options": [
            "A) Monitors systems performance and tracks problems resulting from program changes.",
            "B) Reviews network load requirements in terms of current and future transaction volumes.",
            "C) Assesses the impact of the network load on terminal response times and network data transfer rates.",
            "D) Recommends network balancing procedures and improvements."
        ],
        "correct": "A",
        "explanation": "Monitoring system performance puts the analyst in a self-monitoring role, which can compromise objectivity."
    },
    {
        "id": 346,
        "question": "When segregation of duties concerns exist between IT support staff and end users, what would be a suitable compensating control?",
        "options": [
            "A) Restricting physical access to computing equipment",
            "B) Reviewing transaction and application logs",
            "C) Performing background checks prior to hiring IT staff",
            "D) Locking user sessions after a specified period of inactivity"
        ],
        "correct": "B",
        "explanation": "Reviewing logs directly addresses the threat posed by inadequate segregation of duties."
    },
    {
        "id": 347,
        "question": "An IS auditor reviewing an organization that uses cross-training practices should assess the risk of:",
        "options": [
            "A) Dependency on a single person.",
            "B) Inadequate succession planning.",
            "C) One person knowing all parts of a system.",
            "D) A disruption of operations."
        ],
        "correct": "C",
        "explanation": "Assessing the risk of any single employee knowing all parts of a system is critical to identifying potential exposures."
    },
    {
        "id": 348,
        "question": "Which of the following controls would an IS auditor look for in an environment where duties cannot be appropriately segregated?",
        "options": [
            "A) Overlapping controls",
            "B) Boundary controls",
            "C) Access controls",
            "D) Compensating controls"
        ],
        "correct": "D",
        "explanation": "Compensating controls are essential to mitigate risks when segregation of duties is not feasible."
    },
    {
        "id": 349,
        "question": "Which of the following reduces the potential impact of social engineering attacks?",
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
        "id": 350,
        "question": "Which of the following activities performed by a database administrator (DBA) should be performed by a different person?",
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
        "id": 351,
        "question": "To gain an understanding of the effectiveness of an organization's planning and management of investments in IT assets, an IS auditor should review the:",
        "options": [
            "A) Enterprise data model.",
            "B) IT balanced scorecard (BSC).",
            "C) IT organizational structure.",
            "D) Historical financial statements."
        ],
        "correct": "B",
        "explanation": "The IT balanced scorecard (BSC) provides a comprehensive view of IT performance, including investment management, and helps align IT with business objectives."
    },
    {
        "id": 352,
        "question": "Which of the following is the BEST performance criterion for evaluating the adequacy of an organization's security awareness training?",
        "options": [
            "A) Senior management is aware of critical information assets and demonstrates adequate concern for their protection.",
            "B) Job descriptions contain clear statements of accountability for information security.",
            "C) In accordance with the degree of risk and business impact, there is adequate funding for security efforts.",
            "D) No actual incidents have occurred that have caused a loss or public embarrassment."
        ],
        "correct": "B",
        "explanation": "Including security responsibilities in job descriptions ensures staff awareness of their roles regarding information security."
    },
    {
        "id": 353,
        "question": "Which of the following is a risk of cross-training?",
        "options": [
            "A) Increases the dependence on one employee",
            "B) Does not assist in succession planning",
            "C) One employee may know all parts of a system",
            "D) Does not help in achieving a continuity of operations"
        ],
        "correct": "C",
        "explanation": "Cross-training may lead to a situation where one individual knows all aspects of a system, increasing risk exposure."
    },
    {
        "id": 354,
        "question": "Which of the following is normally a responsibility of the chief security officer (CSO)?",
        "options": [
            "A) Periodically reviewing and evaluating the security policy",
            "B) Executing user application and software testing and evaluation",
            "C) Granting and revoking user access to IT resources",
            "D) Approving access to data and applications"
        ],
        "correct": "A",
        "explanation": "The CSO is responsible for ensuring that security policies are adequate to protect company assets."
    },
    {
        "id": 355,
        "question": "To support an organization's goals, an IS department should have:",
        "options": [
            "A) A low-cost philosophy.",
            "B) Long-and short-range plans.",
            "C) Leading-edge technology.",
            "D) Plans to acquire new hardware and software."
        ],
        "correct": "B",
        "explanation": "Long- and short-range plans should align with organizational goals to effectively support them."
    },
    {
        "id": 356,
        "question": "In reviewing the IS short-range (tactical) plan, an IS auditor should determine whether:",
        "options": [
            "A) There is an integration of IS and business staffs within projects.",
            "B) There is a clear definition of the IS mission and vision.",
            "C) A strategic information technology planning methodology is in place.",
            "D) The plan correlates business objectives to IS goals and objectives."
        ],
        "correct": "A",
        "explanation": "Integration of IS and business staff within projects is critical for successful tactical planning."
    },
    {
        "id": 357,
        "question": "Which of the following would an IS auditor consider the MOST relevant to short-term planning for an IS department?",
        "options": [
            "A) Allocating resources",
            "B) Keeping current with technology advances",
            "C) Conducting control self-assessment",
            "D) Evaluating hardware needs"
        ],
        "correct": "A",
        "explanation": "Allocating resources is crucial in short-term planning to align IT investments with management strategies."
    },
    {
        "id": 358,
        "question": "Which of the following goals would you expect to find in an organization's strategic plan?",
        "options": [
            "A) Test a new accounting package.",
            "B) Perform an evaluation of information technology needs.",
            "C) Implement a new project planning system within the next 12 months.",
            "D) Become the supplier of choice for the product offered."
        ],
        "correct": "D",
        "explanation": "Strategic planning focuses on long-term objectives; thus, becoming a preferred supplier represents a significant business goal."
    },
    {
        "id": 359,
        "question": "Which of the following would an IS auditor consider to be the MOST important when evaluating an organization's IS strategy? That it:",
        "options": [
            "A) Has been approved by line management.",
            "B) Does not vary from the IS department's preliminary budget.",
            "C) Complies with procurement procedures.",
            "D) Supports the business objectives of the organization."
        ],
        "correct": "D",
        "explanation": "The IS strategy must align with the organization's business objectives to be deemed effective."
    },
    {
        "id": 360,
        "question": "An IS auditor reviewing an organization's IT strategic plan should FIRST review:",
        "options": [
            "A) The existing IT environment.",
            "B) The IT governance structure.",
            "C) The overall corporate strategy.",
            "D) The current IT budget."
        ],
        "correct": "C",
        "explanation": "Understanding the overall corporate strategy provides context for evaluating the effectiveness of the IT strategic plan."
    },
    {
        "id": 361,
        "question": "When reviewing IS strategies, an IS auditor can BEST assess whether IS strategy supports the organizations' business objectives by determining if IS:",
        "options": [
            "A) has all the personnel and equipment it needs.",
            "B) plans are consistent with management strategy.",
            "C) uses its equipment and personnel efficiently and effectively.",
            "D) has sufficient excess capacity to respond to changing directions."
        ],
        "correct": "B",
        "explanation": "Determining if the IS plan is consistent with management strategy relates IS/IT planning to business plans."
    },
    {
        "id": 362,
        "question": "In an organization, the responsibilities for IT security are clearly assigned and enforced, and an IT security risk and impact analysis is consistently performed. This represents which level of ranking in the information security governance maturity model?",
        "options": [
            "A) Optimized",
            "B) Managed",
            "C) Defined",
            "D) Repeatable"
        ],
        "correct": "B",
        "explanation": "When responsibilities are assigned and enforced and risk analysis is consistently performed, the organization is at the 'Managed and Measurable' level."
    },
    {
        "id": 363,
        "question": "To aid management in achieving IT and business alignment, an IS auditor should recommend the use of:",
        "options": [
            "A) control self-assessments.",
            "B) a business impact analysis.",
            "C) an IT balanced scorecard.",
            "D) business process reengineering."
        ],
        "correct": "C",
        "explanation": "An IT balanced scorecard (BSC) provides the bridge between IT objectives and business objectives by supplementing financial evaluation with measures of customer satisfaction, internal processes, and innovation."
    },
    {
        "id": 364,
        "question": "When reviewing the IT strategic planning process, an IS auditor should ensure that the plan:",
        "options": [
            "A) incorporates state of the art technology.",
            "B) addresses the required operational controls.",
            "C) articulates the IT mission and vision.",
            "D) specifies project management practices."
        ],
        "correct": "C",
        "explanation": "The IT strategic plan must include a clear articulation of the IT mission and vision."
    },
    {
        "id": 365,
        "question": "When developing a formal enterprise security program, the MOST critical success factor (CSF) would be the:",
        "options": [
            "A) establishment of a review board.",
            "B) creation of a security unit.",
            "C) effective support of an executive sponsor.",
            "D) selection of a security process owner."
        ],
        "correct": "C",
        "explanation": "The executive sponsor supports the organization's strategic security program and directs overall security management; visible top management sponsorship is the most critical success factor."
    },
    {
        "id": 366,
        "question": "When reviewing an organization's strategic IT plan, an IS auditor should expect to find:",
        "options": [
            "A) an assessment of the fit of the organization's application portfolio with business objectives.",
            "B) actions to reduce hardware procurement cost.",
            "C) a listing of approved suppliers of IT contract resources.",
            "D) a description of the technical architecture for the organization's network perimeter security."
        ],
        "correct": "A",
        "explanation": "An assessment of the application portfolio's alignment with business objectives is a key component of strategic IT planning."
    },
    {
        "id": 367,
        "question": "The advantage of a bottom-up approach to the development of organizational policies is that the policies:",
        "options": [
            "A) are developed for the organization as a whole.",
            "B) are more likely to be derived as a result of a risk assessment.",
            "C) will not conflict with overall corporate policy.",
            "D) ensure consistency across the organization."
        ],
        "correct": "B",
        "explanation": "A bottom-up approach begins with operational-level requirements and policies, which are often derived from risk assessments."
    },
    {
        "id": 368,
        "question": "Which of the following is the GREATEST risk of an inadequate policy definition for ownership of data and systems?",
        "options": [
            "A) User management coordination does not exist.",
            "B) Specific user accountability cannot be established.",
            "C) Unauthorized users may have access to originate, modify or delete data.",
            "D) Audit recommendations may not be implemented."
        ],
        "correct": "C",
        "explanation": "Without a policy defining ownership and access responsibilities, there is an increased risk that unauthorized users can access and alter data."
    },
    {
        "id": 369,
        "question": "The PRIMARY objective of an audit of IT security policies is to ensure that:",
        "options": [
            "A) they are distributed and available to all staff.",
            "B) security and control policies support business and IT objectives.",
            "C) there is a published organizational chart with functional descriptions.",
            "D) duties are appropriately segregated."
        ],
        "correct": "B",
        "explanation": "An IS audit of IT security policies should primarily focus on whether the policies support business and IT objectives."
    },
    {
        "id": 370,
        "question": "The rate of change in technology increases the importance of:",
        "options": [
            "A) outsourcing the IS function.",
            "B) implementing and enforcing good processes.",
            "C) hiring personnel willing to make a career within the organization.",
            "D) meeting user requirements."
        ],
        "correct": "B",
        "explanation": "Change requires that good change management processes be implemented and enforced."
    },
    {
        "id": 371,
        "question": "An IS auditor finds that not all employees are aware of the enterprise's information security policy. The IS auditor should conclude that:",
        "options": [
            "A) this lack of knowledge may lead to unintentional disclosure of sensitive information.",
            "B) information security is not critical to all functions.",
            "C) IS audit should provide security training to the employees.",
            "D) the audit finding will cause management to provide continuous training to staff."
        ],
        "correct": "A",
        "explanation": "All employees should be aware of the enterprise's information security policy to prevent unintentional disclosure of sensitive information."
    },
    {
        "id": 372,
        "question": "The development of an IS security policy is ultimately the responsibility of the:",
        "options": [
            "A) IS department.",
            "B) security committee.",
            "C) security administrator.",
            "D) board of directors."
        ],
        "correct": "D",
        "explanation": "Top management or the board of directors is ultimately responsible for the IS security policy."
    },
    {
        "id": 373,
        "question": "Which of the following programs would a sound information security policy MOST likely include to handle suspected intrusions?",
        "options": [
            "A) Response",
            "B) Correction",
            "C) Detection",
            "D) Monitoring"
        ],
        "correct": "A",
        "explanation": "A sound IS security policy will most likely outline a response program to handle suspected intrusions."
    },
    {
        "id": 374,
        "question": "Which of the following should be included in an organization's IS security policy?",
        "options": [
            "A) A list of key IT resources to be secured",
            "B) The basis for access authorization",
            "C) Identity of sensitive security features",
            "D) Relevant software security features"
        ],
        "correct": "B",
        "explanation": "The security policy provides the broad framework, including the basis for access authorization."
    },
    {
        "id": 375,
        "question": "Which of the following is the initial step in creating a firewall policy?",
        "options": [
            "A) A cost-benefit analysis of methods for securing the applications",
            "B) Identification of network applications to be externally accessed",
            "C) Identification of vulnerabilities associated with network applications to be externally accessed",
            "D) Creation of an applications traffic matrix showing protection methods"
        ],
        "correct": "B",
        "explanation": "Identification of the applications required across the network should be identified first."
    },
    {
        "id": 376,
        "question": "The management of an organization has decided to establish a security awareness program. Which of the following would MOST likely be a part of the program?",
        "options": [
            "A) Utilization of an intrusion detection system to report incidents",
            "B) Mandating the use of passwords to access all software",
            "C) Installing an efficient user log system to track the actions of each user",
            "D) Training provided on a regular basis to all current and new employees"
        ],
        "correct": "D",
        "explanation": "Training is the only choice that is directed at security awareness."
    },
    {
        "id": 377,
        "question": "Which of the following is MOST critical for the successful implementation and maintenance of a security policy?",
        "options": [
            "A) Assimilation of the framework and intent of a written security policy by all appropriate parties",
            "B) Management support and approval for the implementation and maintenance of a security policy",
            "C) Enforcement of security rules by providing punitive actions for any violation of security rules",
            "D) Stringent implementation, monitoring, and maintenance of technical controls"
        ],
        "correct": "A",
        "explanation": "For a security policy to be effective, all appropriate parties must understand and assimilate its framework and intent."
    },
    {
        "id": 378,
        "question": "When reviewing the information security governance framework, an IS auditor should ensure that:",
        "options": [
            "A) compliance with policies and standards is effectively monitored.",
            "B) information security management is aligned with business objectives.",
            "C) the organization has adequate resources to support security management.",
            "D) controls are in place to protect sensitive information."
        ],
        "correct": "B",
        "explanation": "The governance framework must be aligned with business objectives; otherwise, information security will not effectively support the business."
    },
    {
        "id": 379,
        "question": "The PRIMARY objective of security awareness training is to:",
        "options": [
            "A) comply with regulatory requirements.",
            "B) define security roles and responsibilities.",
            "C) minimize human error.",
            "D) ensure that security technology is used properly."
        ],
        "correct": "C",
        "explanation": "The purpose of security awareness training is to ensure employees understand their responsibilities and reduce the risk of security breaches caused by human error."
    },
    {
        "id": 380,
        "question": "Which of the following is the BEST approach to protect data integrity in a database management system (DBMS)?",
        "options": [
            "A) Implementing periodic backups.",
            "B) Using data encryption and access controls.",
            "C) Using transaction logging and recovery methods.",
            "D) Using redundant systems."
        ],
        "correct": "B",
        "explanation": "Data encryption and access controls provide the most comprehensive protection for data integrity."
    },
    {
        "id": 381,
        "question": "A top-down approach to the development of operational policies will help ensure:",
        "options": [
            "A) that they are consistent across the organization.",
            "B) that they are implemented as a part of risk assessment.",
            "C) compliance with all policies.",
            "D) that they are reviewed periodically."
        ],
        "correct": "A",
        "explanation": "Deriving lower-level policies from corporate policies ensures consistency across the organization."
    },
    {
        "id": 382,
        "question": "Which of the following would MOST likely indicate that a customer data warehouse should remain in-house rather than be outsourced to an offshore operation?",
        "options": [
            "A) Time zone differences could impede communications between IT teams.",
            "B) Telecommunications cost could be much higher in the first year.",
            "C) Privacy laws could prevent cross-border flow of information.",
            "D) Software development may require more detailed specifications."
        ],
        "correct": "C",
        "explanation": "Privacy laws prohibiting the cross-border flow of personally identifiable information would necessitate keeping the data warehouse in-house."
    },
    {
        "id": 383,
        "question": "A retail outlet has introduced radio frequency identification (RFID) tags to create unique serial numbers for all products. Which of the following is the PRIMARY concern associated with this initiative?",
        "options": [
            "A) Issues of privacy",
            "B) Wavelength can be absorbed by the human body.",
            "C) RFID tags may not be removable.",
            "D) RFID eliminates line-of-sight reading."
        ],
        "correct": "A",
        "explanation": "Privacy violations are a significant concern as RFID tags can track purchases, potentially linking them to individuals."
    },
    {
        "id": 384,
        "question": "When developing a security architecture, which of the following steps should be executed FIRST?",
        "options": [
            "A) Developing security procedures.",
            "B) Defining a security policy.",
            "C) Specifying an access control methodology.",
            "D) Defining roles and responsibilities."
        ],
        "correct": "B",
        "explanation": "Defining a security policy is the first step in building a security architecture, providing a foundation for other steps."
    },
    {
        "id": 385,
        "question": "An IS auditor finds that, in accordance with IS policy, IDs of terminated users are deactivated within 90 days of termination. The IS auditor should:",
        "options": [
            "A) report that the control is operating effectively since deactivation happens within the time frame stated in the IS policy.",
            "B) verify that user access rights have been granted on a need-to-have basis.",
            "C) recommend changes to the IS policy to ensure deactivation of user IDs upon termination.",
            "D) recommend that activity logs of terminated users be reviewed on a regular basis."
        ],
        "correct": "C",
        "explanation": "Best practice dictates that user IDs should be deactivated immediately upon termination, regardless of the policy timeframe."
    },
    {
        "id": 386,
        "question": "An IS auditor is reviewing a project to implement a payment system between a parent bank and a subsidiary. The IS auditor should FIRST verify that the:",
        "options": [
            "A) technical platforms between the two companies are interoperable.",
            "B) parent bank is authorized to serve as a service provider.",
            "C) security features are in place to segregate subsidiary trades.",
            "D) subsidiary can join as a co-owner of this payment system."
        ],
        "correct": "B",
        "explanation": "Contractual agreements are crucial for shared services, especially in regulated sectors like banking."
    },
    {
        "id": 387,
        "question": "IT control objectives are useful to IS auditors, as they provide the basis for understanding the:",
        "options": [
            "A) desired result or purpose of implementing specific control procedures.",
            "B) best IT security control practices relevant to a specific entity.",
            "C) techniques for securing information.",
            "D) security policy."
        ],
        "correct": "A",
        "explanation": "IT control objectives articulate the desired outcomes for implementing control procedures in IT activities."
    },
    {
        "id": 388,
        "question": "The initial step in establishing an information security program is the:",
        "options": [
            "A) development and implementation of an information security standards manual.",
            "B) performance of a comprehensive security control review by the IS auditor.",
            "C) adoption of a corporate information security policy statement.",
            "D) purchase of security access control software."
        ],
        "correct": "C",
        "explanation": "A policy statement reflects executive management's intent and support for security, serving as the foundation for the security program."
    },
    {
        "id": 389,
        "question": "Which of the following provides the best evidence of the adequacy of a security awareness program?",
        "options": [
            "A) The number of stakeholders including employees trained at various levels.",
            "B) Coverage of training at all locations across the enterprise.",
            "C) The implementation of security devices from different vendors.",
            "D) Periodic reviews and comparison with best practices."
        ],
        "correct": "D",
        "explanation": "Regular reviews and comparisons with best practices are the best indicators of the adequacy of security awareness content."
    },
    {
        "id": 390,
        "question": "The PRIMARY objective of implementing corporate governance by an organization's management is to:",
        "options": [
            "A) provide strategic direction.",
            "B) control business operations.",
            "C) align IT with business.",
            "D) implement best practices."
        ],
        "correct": "A",
        "explanation": "Corporate governance aims to provide strategic direction, ensuring that risks are managed and resources utilized effectively."
    },
    {
        "id": 391,
        "question": "Which of the following should an IS auditor recommend to BEST enforce alignment of an IT project portfolio with strategic organizational priorities?",
        "options": [
            "A) Define a balanced scorecard (BSC) for measuring performance.",
            "B) Consider user satisfaction in the key performance indicators (KPIs).",
            "C) Select projects according to business benefits and risks.",
            "D) Modify the yearly process of defining the project portfolio."
        ],
        "correct": "C",
        "explanation": "Selecting projects based on expected business benefits and related risks is the most effective way to align with strategic priorities."
    },
    {
        "id": 392,
        "question": "An example of a direct benefit to be derived from a proposed IT-related business investment is:",
        "options": [
            "A) enhanced reputation.",
            "B) enhanced staff morale.",
            "C) the use of new technology.",
            "D) increased market penetration."
        ],
        "correct": "D",
        "explanation": "Direct benefits from IT investments are quantifiable financial benefits, such as increased market penetration."
    },
    {
        "id": 393,
        "question": "To assist an organization in planning for IT investments, an IS auditor should recommend the use of:",
        "options": [
            "A) project management tools.",
            "B) an object-oriented architecture.",
            "C) tactical planning.",
            "D) enterprise architecture (EA)."
        ],
        "correct": "D",
        "explanation": "Enterprise architecture helps document IT assets and processes, facilitating understanding and planning for IT investments."
    },
    {
        "id": 394,
        "question": "A benefit of open system architecture is that it:",
        "options": [
            "A) facilitates interoperability.",
            "B) facilitates the integration of proprietary components.",
            "C) will be a basis for volume discounts from equipment vendors.",
            "D) allows for the achievement of more economies of scale for equipment."
        ],
        "correct": "A",
        "explanation": "Open systems allow for components from different vendors to work together due to defined public standards."
    },
    {
        "id": 395,
        "question": "In the context of effective information security governance, the primary objective of value delivery is to:",
        "options": [
            "A) optimize security investments in support of business objectives.",
            "B) implement a standard set of security practices.",
            "C) institute a standards-based solution.",
            "D) implement a continuous improvement culture."
        ],
        "correct": "A",
        "explanation": "Value delivery aims to ensure security investments are optimized to align with business objectives."
    },
    {
        "id": 396,
        "question": "Which of the following BEST supports the prioritization of new IT projects?",
        "options": [
            "A) Internal control self-assessment (CSA).",
            "B) Information systems audit.",
            "C) Investment portfolio analysis.",
            "D) Business risk assessment."
        ],
        "correct": "C",
        "explanation": "Investment portfolio analysis clarifies investment strategy and justifies project prioritization."
    },
    {
        "id": 397,
        "question": "After the merger of two organizations, multiple self-developed legacy applications from both companies are to be replaced by a new common platform. Which of the following would be the GREATEST risk?",
        "options": [
            "A) Project management and progress reporting is combined in a project management office driven by external consultants.",
            "B) The replacement effort consists of several independent projects without integrating the resource allocation in a portfolio management approach.",
            "C) The resources of each organization are inefficiently allocated while familiarizing with the other company's legacy systems.",
            "D) The new platform will force the business areas of both organizations to change their work processes, which will result in extensive training needs."
        ],
        "correct": "B",
        "explanation": "Lack of centralized resource allocation in independent projects increases the risk of misestimating resource availability."
    },
    {
        "id": 398,
        "question": "Which of the following is the MOST important function to be performed by IS management when a service has been outsourced?",
        "options": [
            "A) Ensuring that invoices are paid to the provider.",
            "B) Participating in systems design with the provider.",
            "C) Renegotiating the provider's fees.",
            "D) Monitoring the outsourcing provider's performance."
        ],
        "correct": "D",
        "explanation": "Monitoring the provider's performance is crucial to ensure services meet contractual obligations."
    },
    {
        "id": 399,
        "question": "Is it appropriate for an IS auditor from a company that is considering outsourcing its IS processing to request and review a copy of each vendor's business continuity plan?",
        "options": [
            "A) Yes, to assess the potential risks associated with outsourcing.",
            "B) No, it is inappropriate as it could compromise the vendor's confidentiality.",
            "C) No, it is unnecessary since IS processing is not a critical function.",
            "D) Yes, but only after a formal non-disclosure agreement is signed."
        ],
        "correct": "A",
        "explanation": "Understanding vendors' business continuity plans is essential to evaluate risks and ensure preparedness."
    },
    {
        "id": 400,
        "question": "An organization wants to ensure that a new information system is cost-effective. The BEST approach is to:",
        "options": [
            "A) adopt a vendor solution to minimize integration costs.",
            "B) conduct a cost-benefit analysis (CBA) prior to investment.",
            "C) purchase the most up-to-date technology.",
            "D) develop the system in-house to reduce licensing costs."
        ],
        "correct": "B",
        "explanation": "A cost-benefit analysis helps evaluate whether expected benefits justify the costs involved."
    },
    {
        "id": 401,
        "question": "When performing a review of the structure of an electronic funds transfer (EFT) system, an IS auditor observes that the technological infrastructure is based on a centralized processing scheme that has been outsourced to a provider in another country. Based on this information, which of the following conclusions should be the main concern of the IS auditor?",
        "options": [
            "A) There could be a question regarding the legal jurisdiction.",
            "B) Having a provider abroad will cause excessive costs in future audits.",
            "C) The auditing process will be difficult because of the distance.",
            "D) There could be different auditing norms."
        ],
        "correct": "A",
        "explanation": "In a funds transfer process, when the processing scheme is centralized in a different country, legal jurisdiction issues may affect the right to perform a review in the other country."
    },
    {
        "id": 402,
        "question": "An IS auditor should expect which of the following items to be included in the request for proposal (RFP) when IS is procuring services from an independent service provider (ISP)?",
        "options": [
            "A) References from other customers",
            "B) Service level agreement (SLA) template",
            "C) Maintenance agreement",
            "D) Conversion plan"
        ],
        "correct": "A",
        "explanation": "An IS auditor should look for independent verification that the ISP can perform the tasks; references from other customers provide an independent, external review."
    },
    {
        "id": 403,
        "question": "To minimize costs and improve service levels an outsourcer should seek which of the following contract clauses?",
        "options": [
            "A) O/S and hardware refresh frequencies",
            "B) Gain-sharing performance bonuses",
            "C) Penalties for noncompliance",
            "D) Charges tied to variable cost metrics"
        ],
        "correct": "B",
        "explanation": "Gain-sharing performance bonuses provide a financial incentive for the outsourcer to exceed contract terms and can lead to cost savings for the client."
    },
    {
        "id": 404,
        "question": "When an organization is outsourcing their information security function, which of the following should be kept in the organization?",
        "options": [
            "A) Accountability for the corporate security policy",
            "B) Defining the corporate security policy",
            "C) Implementing the corporate security policy",
            "D) Defining security procedures and guidelines"
        ],
        "correct": "A",
        "explanation": "Accountability cannot be transferred to external parties; defining, implementing, and defining procedures can be performed by outside entities as long as accountability remains within the organization."
    },
    {
        "id": 405,
        "question": "An IS auditor has been assigned to review IT structures and activities recently outsourced to various providers. Which of the following should the IS auditor determine FIRST?",
        "options": [
            "A) That an audit clause is present in all contracts.",
            "B) That the SLA of each contract is substantiated by appropriate KPIs.",
            "C) That the contractual warranties of the providers support the business needs of the organization.",
            "D) That at contract termination, support is guaranteed by each outsourcer for new outsourcers"
        ],
        "correct": "C",
        "explanation": "The complexity of IT structures and the interplay of responsibilities and warranties may affect the effectiveness of those warranties and the reasonable certainty that business needs will be met."
    },
    {
        "id": 406,
        "question": "With respect to the outsourcing of IT services, which of the following conditions should be of GREATEST concern to an IS auditor?",
        "options": [
            "A) Outsourced activities are core and provide a differentiated advantage to the organization.",
            "B) Periodic renegotiation is specified in the outsourcing contract.",
            "C) The outsourcing contract fails to cover every action required by the arrangement.",
            "D) Similar activities are outsourced to more than one vendor."
        ],
        "correct": "A",
        "explanation": "An organization's core activities generally should not be outsourced because they are what the organization does best."
    },
    {
        "id": 407,
        "question": "While conducting an audit of a service provider, an IS auditor observes that the service provider has outsourced a part of the work to another provider. Since the work involves confidential information, the IS auditor's PRIMARY concern should be that the:",
        "options": [
            "A) requirement for protecting confidentiality of information could be compromised.",
            "B) contract may be terminated because prior permission from the outsourcer was not obtained.",
            "C) other service provider to whom work has been outsourced is not subject to audit.",
            "D) outsourcer will approach the other service provider directly for further work."
        ],
        "correct": "A",
        "explanation": "The potential risk that the confidentiality of the information will be compromised is the primary concern."
    },
    {
        "id": 408,
        "question": "Which of the following is the BEST information source for management to use as an aid in the identification of assets that are subject to laws and regulations?",
        "options": [
            "A) Security incident summaries",
            "B) Vendor best practices",
            "C) CERT coordination center",
            "D) Significant contracts"
        ],
        "correct": "D",
        "explanation": "Contractual requirements are one of the sources that should be consulted to identify requirements for the management of information assets."
    },
    {
        "id": 409,
        "question": "An organization has outsourced its help desk activities. An IS auditor's GREATEST concern when reviewing the contract and associated service level agreement (SLA) between the organization and vendor should be the provisions for:",
        "options": [
            "A) documentation of staff background checks.",
            "B) independent audit reports or full audit access.",
            "C) reporting the year-to-year incremental cost reductions.",
            "D) reporting staff turnover, development or training."
        ],
        "correct": "B",
        "explanation": "Ensuring that independent audit reports are available is crucial to verify that the outsourced functions meet the necessary standards."
    },
    {
        "id": 410,
        "question": "Which of the following is the MOST important IS audit consideration when an organization outsources a customer credit review system to a third-party service provider? The provider:",
        "options": [
            "A) meets or exceeds industry security standards.",
            "B) agrees to be subject to external security reviews.",
            "C) has a good market reputation for service and experience.",
            "D) complies with security policies of the organization."
        ],
        "correct": "B",
        "explanation": "It is critical that an independent security review of an outsourcing vendor be obtained because customer credit information will be kept there."
    },
    {
        "id": 411,
        "question": "The risks associated with electronic evidence gathering would MOST likely be reduced by an email:",
        "options": [
            "A) destruction policy.",
            "B) security policy.",
            "C) archive policy.",
            "D) audit policy."
        ],
        "correct": "C",
        "explanation": "A well-archived email policy allows for specific email records to be retrieved without disclosing other confidential records."
    },
    {
        "id": 412,
        "question": "The output of the risk management process is an input for making:",
        "options": [
            "A) business plans.",
            "B) audit charters.",
            "C) security policy decisions.",
            "D) software design decisions."
        ],
        "correct": "C",
        "explanation": "The risk management process focuses on making security-related decisions, such as the level of acceptable risk."
    },
    {
        "id": 413,
        "question": "An IS auditor was hired to review e-business security. The IS auditor's first task was to examine each existing e-business application looking for vulnerabilities. What would be the next task?",
        "options": [
            "A) Report the risks to the CIO and CEO immediately",
            "B) Examine e-business applications in development",
            "C) Identify threats and likelihood of occurrence",
            "D) Check the budget available for risk management"
        ],
        "correct": "C",
        "explanation": "After identifying vulnerabilities, the next step is to assess the threats and their likelihood of occurrence."
    },
    {
        "id": 414,
        "question": "Which of the following is a mechanism for mitigating risks?",
        "options": [
            "A) Security and control practices",
            "B) Property and liability insurance",
            "C) Audit and certification",
            "D) Contracts and service level agreements (SLAs)"
        ],
        "correct": "A",
        "explanation": "Risks are mitigated by implementing appropriate security and control practices."
    },
    {
        "id": 415,
        "question": "When developing a risk management program, what is the FIRST activity to be performed?",
        "options": [
            "A) Threat assessment",
            "B) Classification of data",
            "C) Inventory of assets",
            "D) Criticality analysis"
        ],
        "correct": "C",
        "explanation": "Identification of the assets to be protected is the first step in the development of a risk management program."
    },
    {
        "id": 416,
        "question": "A team conducting a risk analysis is having difficulty projecting the financial losses that could result from a risk. To evaluate the potential losses, the team should:",
        "options": [
            "A) compute the amortization of the related assets.",
            "B) calculate a return on investment (ROI).",
            "C) apply a qualitative approach.",
            "D) spend the time needed to define exactly the loss amount."
        ],
        "correct": "C",
        "explanation": "When it is difficult to calculate financial losses, a qualitative approach is often the best method to assess potential impact."
    },
    {
        "id": 417,
        "question": "Which of the following does a lack of adequate security controls represent?",
        "options": [
            "A) Threat",
            "B) Asset",
            "C) Impact",
            "D) Vulnerability"
        ],
        "correct": "D",
        "explanation": "The lack of adequate security controls is considered a vulnerability, exposing information to risks."
    },
    {
        "id": 418,
        "question": "Assessing IT risks is BEST achieved by:",
        "options": [
            "A) evaluating threats associated with business processes.",
            "B) applying regulatory requirements to controls.",
            "C) calculating the return on investment (ROI) on security controls.",
            "D) defining and assessing security controls."
        ],
        "correct": "A",
        "explanation": "Business process assessment helps evaluate threats to information and IT risks, aligning with operational requirements."
    },
    {
        "id": 419,
        "question": "During an audit, the IS auditor finds that a large number of employees have been accessing files that they have no business reason to view. The BEST recommendation is to implement:",
        "options": [
            "A) access controls based on business functions.",
            "B) a monitoring tool to track employee file access.",
            "C) mandatory training sessions on security policy.",
            "D) an audit of employee access to critical files."
        ],
        "correct": "A",
        "explanation": "Implementing access controls based on business functions will help ensure employees can only access files relevant to their roles."
    },
    {
        "id": 420,
        "question": "In the context of business continuity, the primary purpose of an incident management process is to ensure:",
        "options": [
            "A) all incidents are managed to minimize their impact on business operations.",
            "B) training for incident management staff is conducted.",
            "C) the incident response team is notified quickly.",
            "D) audits of incident management practices are performed regularly."
        ],
        "correct": "A",
        "explanation": "The main objective of incident management is to minimize the impact of incidents on business operations."
    },
    {
        "id": 421,
        "question": "An IS auditor reviewing the risk assessment process of an organization should FIRST:",
        "options": [
            "A) identify the reasonable threats to the information assets.",
            "B) analyze the technical and organizational vulnerabilities.",
            "C) identify and rank the information assets.",
            "D) evaluate the effect of a potential security breach."
        ],
        "correct": "C",
        "explanation": "Identification and ranking of information assets set the scope for assessing risk, guiding the analysis of threats and vulnerabilities."
    },
    {
        "id": 422,
        "question": "An IS auditor is reviewing an IT security risk management program. Measures of security risk should:",
        "options": [
            "A) address all of the network risks.",
            "B) be tracked over time against the IT strategic plan.",
            "C) take into account the entire IT environment.",
            "D) result in the identification of vulnerability tolerances."
        ],
        "correct": "C",
        "explanation": "Security risk measures must consider the entire IT environment to prioritize critical areas for risk reduction."
    },
    {
        "id": 423,
        "question": "Which of the following should be considered FIRST when implementing a risk management program?",
        "options": [
            "A) An understanding of the organization's threat, vulnerability and risk profile.",
            "B) An understanding of the risk exposures and the potential consequences of compromise.",
            "C) A determination of risk management priorities based on potential consequences.",
            "D) A risk mitigation strategy sufficient to keep risk consequences at an acceptable level."
        ],
        "correct": "A",
        "explanation": "Understanding the organization's threat, vulnerability, and risk profile is crucial as a foundational step in risk management."
    },
    {
        "id": 424,
        "question": "As a driver of IT governance, transparency of IT's cost, value and risks is primarily achieved through:",
        "options": [
            "A) performance measurement.",
            "B) strategic alignment.",
            "C) value delivery.",
            "D) resource management."
        ],
        "correct": "A",
        "explanation": "Performance measurement provides stakeholders with information on IT performance compared to objectives, ensuring transparency."
    },
    {
        "id": 425,
        "question": "Which of the following should be the MOST important consideration when deciding areas of priority for IT governance implementation?",
        "options": [
            "A) Process maturity.",
            "B) Performance indicators.",
            "C) Business risk.",
            "D) Assurance reports."
        ],
        "correct": "C",
        "explanation": "Prioritizing areas representing known risks to the enterprise's operations is essential for effective governance implementation."
    },
    {
        "id": 426,
        "question": "The PRIMARY benefit of implementing a security program as part of a security governance framework is the:",
        "options": [
            "A) alignment of the IT activities with IS audit recommendations.",
            "B) enforcement of the management of security risks.",
            "C) implementation of the chief information security officer's (CISO) recommendations.",
            "D) reduction of the cost for IT security."
        ],
        "correct": "B",
        "explanation": "The main benefit is the effective management of security risks and monitoring residual risks post-implementation."
    },
    {
        "id": 427,
        "question": "An IS auditor who is reviewing incident reports discovers that, in one instance, an important document left on an employee's desk was removed and put in the garbage by the outsourced cleaning staff. Which of the following should the IS auditor recommend to management?",
        "options": [
            "A) Stricter controls should be implemented by both the organization and the cleaning agency.",
            "B) No action is required since such incidents have not occurred in the past.",
            "C) A clear desk policy should be implemented and strictly enforced in the organization.",
            "D) A sound backup policy for all important office documents should be implemented."
        ],
        "correct": "A",
        "explanation": "Implementing strict controls with the cleaning agency is necessary to prevent unauthorized access to sensitive documents."
    },
    {
        "id": 428,
        "question": "During an audit, an IS auditor notices that the IT department of a medium-sized organization has no separate risk management function, and the organization's operational risk documentation only contains a few broadly described IT risks. What is the MOST appropriate recommendation in this situation?",
        "options": [
            "A) Create an IT risk management department and establish an IT risk framework with the aid of external risk management experts.",
            "B) Use common industry standard aids to divide the existing risk documentation into several individual risks which will be easier to handle.",
            "C) No recommendation is necessary since the current approach is appropriate for a medium-sized organization.",
            "D) Establish regular IT risk management meetings to identify and assess risks, and create a mitigation plan as input to the organization's risk management."
        ],
        "correct": "D",
        "explanation": "Regular meetings for risk identification and assessment are vital for managing risks effectively in a medium-sized organization."
    },
    {
        "id": 429,
        "question": "The IT balanced scorecard is a business governance tool intended to monitor IT performance evaluation indicators other than:",
        "options": [
            "A) financial results.",
            "B) customer satisfaction.",
            "C) internal process efficiency.",
            "D) innovation capacity."
        ],
        "correct": "A",
        "explanation": "The IT balanced scorecard focuses on key performance indicators beyond just financial results."
    },
    {
        "id": 430,
        "question": "Before implementing an IT balanced scorecard, an organization must:",
        "options": [
            "A) deliver effective and efficient services.",
            "B) define key performance indicators.",
            "C) provide business value to IT projects.",
            "D) control IT expenses."
        ],
        "correct": "B",
        "explanation": "Defining key performance indicators is essential for the successful implementation of an IT balanced scorecard."
    },
    {
        "id": 431,
        "question": "Which of the following is the PRIMARY objective of an IT performance measurement process?",
        "options": [
            "A) Minimize errors.",
            "B) Gather performance data.",
            "C) Establish performance baselines.",
            "D) Optimize performance."
        ],
        "correct": "D",
        "explanation": "The primary objective is to optimize performance by identifying areas for improvement."
    },
    {
        "id": 432,
        "question": "When auditing the proposed acquisition of a new computer system, an IS auditor should FIRST establish that:",
        "options": [
            "A) a clear business case has been approved by management.",
            "B) corporate security standards will be met.",
            "C) users will be involved in the implementation plan.",
            "D) the new system will meet all required user functionality."
        ],
        "correct": "A",
        "explanation": "A clear business case is essential to ensure the acquisition aligns with business needs."
    },
    {
        "id": 433,
        "question": "Documentation of a business case used in an IT development project should be retained until:",
        "options": [
            "A) the end of the system's life cycle.",
            "B) the project is approved.",
            "C) user acceptance of the system.",
            "D) the system is in production."
        ],
        "correct": "A",
        "explanation": "The business case should be retained throughout the life cycle for reference and evaluation."
    },
    {
        "id": 434,
        "question": "Which of the following risks could result from inadequate software baselining?",
        "options": [
            "A) Scope creep.",
            "B) Sign-off delays.",
            "C) Software integrity violations.",
            "D) Inadequate controls."
        ],
        "correct": "A",
        "explanation": "Inadequate baselining can lead to scope creep due to uncontrolled changes during development."
    },
    {
        "id": 435,
        "question": "The most common reason for the failure of information systems to meet the needs of users is that:",
        "options": [
            "A) user needs are constantly changing.",
            "B) the growth of user requirements was forecast inaccurately.",
            "C) the hardware system limits the number of concurrent users.",
            "D) user participation in defining the system's requirements was inadequate."
        ],
        "correct": "D",
        "explanation": "Lack of adequate user involvement often results in systems that do not meet user needs."
    },
    {
        "id": 436,
        "question": "Many IT projects experience problems because the development time and/or resource requirements are underestimated. Which of the following techniques would provide the GREATEST assistance in developing an estimate of project duration?",
        "options": [
            "A) Function point analysis.",
            "B) PERT chart.",
            "C) Rapid application development.",
            "D) Object-oriented system development."
        ],
        "correct": "B",
        "explanation": "A PERT chart helps in determining project duration by analyzing the tasks and their interdependencies."
    },
    {
        "id": 437,
        "question": "The reason for establishing a stop or freezing point on the design of a new system is to:",
        "options": [
            "A) prevent further changes to a project in process.",
            "B) indicate the point at which the design is to be completed.",
            "C) require that changes after that point be evaluated for cost-effectiveness.",
            "D) provide the project management team with more control over the project design."
        ],
        "correct": "C",
        "explanation": "A freezing point allows for a review of changes to ensure they are"
    },
    {
        "id": 438,
        "question": "Change control for business application systems being developed using prototyping could be complicated by the:",
        "options": [
            "A) iterative nature of prototyping.",
            "B) need for constant user feedback.",
            "C) complexity of the proposed systems.",
            "D) lack of documentation."
        ],
        "correct": "A",
        "explanation": "The iterative nature of prototyping makes it difficult to control changes because prototypes are continuously modified based on feedback.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 439,
        "question": "An IS auditor is reviewing the project management practices of a large organization. The organization is implementing a major information system and, at the project's outset, has not established a formal project management process. Which of the following would be the MOST effective recommendation for the organization?",
        "options": [
            "A) Establish a project steering committee.",
            "B) Implement project management software tools.",
            "C) Develop a project charter and project management plan.",
            "D) Hire an external project manager."
        ],
        "correct": "C",
        "explanation": "A project charter and project management plan are fundamental to establish proper project management practices from the beginning.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 440,
        "question": "Which of the following is MOST important to consider when determining whether to convert to an automated system?",
        "options": [
            "A) Cost of system maintenance.",
            "B) Internal controls needed to secure the data.",
            "C) User training requirements.",
            "D) Efficiency of the new system."
        ],
        "correct": "D",
        "explanation": "The efficiency of the new system is crucial to determine whether automation provides a net benefit over current processes.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 441,
        "question": "When planning to add personnel to tasks imposing time constraints on the duration of a project, which of the following should be revalidated FIRST?",
        "options": [
            "A) The project budget",
            "B) The critical path for the project",
            "C) The length of the remaining tasks",
            "D) The personnel assigned to other tasks"
        ],
        "correct": "B",
        "explanation": "Adding personnel may alter the sequence of activities on the critical path, which determines the overall project duration. The critical path must be revalidated first.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 442,
        "question": "Which of the following is a characteristic of timebox management?",
        "options": [
            "A) Not suitable for prototyping or rapid application development (RAD)",
            "B) Eliminates the need for a quality process",
            "C) Prevents cost overruns and delivery delays",
            "D) Separates system and user acceptance testing"
        ],
        "correct": "C",
        "explanation": "Timebox management sets strict boundaries for time and cost, making it suitable for RAD and preventing cost overruns and delivery delays.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 443,
        "question": "Which of the following should an IS auditor review to gain an understanding of the effectiveness of controls over the management of multiple projects?",
        "options": [
            "A) Project database",
            "B) Policy documents",
            "C) Project portfolio database",
            "D) Program organization"
        ],
        "correct": "C",
        "explanation": "A project portfolio database contains data such as project owner, schedules, objectives, type, status, and costs, which are necessary for managing multiple projects.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 444,
        "question": "To minimize the cost of a software project, quality management techniques should be applied:",
        "options": [
            "A) As close to their writing (i.e., point of origination) as possible.",
            "B) Primarily at project start-up to ensure that the project is established in accordance with organizational governance standards.",
            "C) Continuously throughout the project with an emphasis on finding and fixing defects primarily during testing to maximize the defect detection rate.",
            "D) Mainly at project close-down to capture lessons learned that can be applied to future projects."
        ],
        "correct": "A",
        "explanation": "Quality management techniques are most cost-effective when applied early, close to the point of origination. The earlier defects are identified, the lower the cost to correct them.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 445,
        "question": "When identifying an earlier project completion time, which is to be obtained by paying a premium for early completion, the activities that should be selected are those:",
        "options": [
            "A) Whose sum of activity time is the shortest.",
            "B) That have zero slack time.",
            "C) That give the longest possible completion time.",
            "D) Whose sum of slack time is the shortest."
        ],
        "correct": "B",
        "explanation": "Activities with zero slack time are on the critical path. Reducing time on these activities (crashing) can shorten the overall project duration.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 446,
        "question": "At the completion of a system development project, a postproject review should include which of the following?",
        "options": [
            "A) Assessing risks that may lead to downtime after the production release",
            "B) Identifying lessons learned that may be applicable to future projects",
            "C) Verifying the controls in the delivered system are working",
            "D) Ensuring that test data are deleted"
        ],
        "correct": "B",
        "explanation": "A postproject review aims to gather lessons learned for future projects. Verifying controls and deleting test data are part of earlier phases.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 447,
        "question": "An IS auditor has been asked to participate in project initiation meetings for a critical project. The IS auditor's MAIN concern should be that the:",
        "options": [
            "A) Complexity and risks associated with the project have been analyzed.",
            "B) Resources needed throughout the project have been determined.",
            "C) Project deliverables have been identified.",
            "D) A contract for external parties involved in the project has been completed."
        ],
        "correct": "A",
        "explanation": "At project initiation, the main focus should be on analyzing complexity and risks, as these are critical to the project's success.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 448,
        "question": "An IS auditor invited to a development project meeting notes that no project risks have been documented. When the IS auditor raises this issue, the project manager responds that it is too early to identify risks and that, if risks do start impacting the project, a risk manager will be hired. The appropriate response of the IS auditor would be to:",
        "options": [
            "A) Stress the importance of spending time at this point in the project to consider and document risks, and to develop contingency plans.",
            "B) Accept the project manager's position as the project manager is accountable for the outcome of the project.",
            "C) Offer to work with the risk manager when one is appointed.",
            "D) Inform the project manager that the IS auditor will conduct a review of the risks at the completion of the requirements definition phase of the project."
        ],
        "correct": "A",
        "explanation": "Early risk identification and documentation are critical. The auditor should emphasise that risks should be considered from the start of the project.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 449,
        "question": "While evaluating software development practices in an organization, an IS auditor notes that the quality assurance (QA) function reports to project management. The MOST important concern for an IS auditor is the:",
        "options": [
            "A) effectiveness of the QA function because it should interact between project management and user management.",
            "B) efficiency of the QA function because it should interact with the project implementation team.",
            "C) effectiveness of the project manager because the project manager should interact with the QA function.",
            "D) efficiency of the project manager because the QA function will need to communicate with the project implementation team."
        ],
        "correct": "A",
        "explanation": "For effectiveness, the QA function should be independent of project management. Reporting to project management compromises that independence.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 450,
        "question": "When reviewing a project where quality is a major concern, an IS auditor should use the project management triangle to explain that:",
        "options": [
            "A) increases in quality can be achieved, even if resource allocation is decreased.",
            "B) increases in quality are only achieved if resource allocation is increased.",
            "C) decreases in delivery time can be achieved, even if resource allocation is decreased.",
            "D) decreases in delivery time can only be achieved if quality is decreased."
        ],
        "correct": "A",
        "explanation": "If resource allocation is decreased, quality can still be improved if there is flexibility in extending the project's delivery time. The project management triangle (scope, time, cost) shows that adjusting one dimension can affect others.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 451,
        "question": "Which of the following should an IS auditor review to understand project progress in terms of time, budget, and deliverables for early detection of possible overruns and for projecting estimates at completion (EACs)?",
        "options": [
            "A) Function point analysis",
            "B) Earned value analysis",
            "C) Cost budget",
            "D) Program Evaluation and Review Technique (PERT)"
        ],
        "correct": "B",
        "explanation": "Earned value analysis (EVA) compares planned work with actual work completed to forecast completion time and costs, making it the best tool for this purpose.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 452,
        "question": "When reviewing an active project, an IS auditor observed that, because of a reduction in anticipated benefits and increased costs, the business case was no longer valid. The IS auditor should recommend that the:",
        "options": [
            "A) project be discontinued.",
            "B) business case be updated and possible corrective actions be identified.",
            "C) project be returned to the project sponsor for reappraisal.",
            "D) project be completed and the business case be updated later."
        ],
        "correct": "B",
        "explanation": "The business case is a key input for decision‑making throughout the project's lifecycle. Updating it allows management to reassess the project's value before taking drastic action.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 453,
        "question": "An organization is implementing an enterprise resource planning (ERP) application to meet its business objectives. Of the following, who is PRIMARILY responsible for overseeing the project to ensure that it is progressing in accordance with the project plan and that it will deliver the expected results?",
        "options": [
            "A) Project sponsor",
            "B) System development project team (SPDT)",
            "C) Project steering committee",
            "D) User project team (UPT)"
        ],
        "correct": "C",
        "explanation": "The project steering committee is responsible for overseeing the project's progress to ensure it meets business objectives. The project sponsor provides funding but does not oversee daily progress.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 454,
        "question": "A legacy payroll application is migrated to a new application. Which of the following stakeholders should be PRIMARILY responsible for reviewing and signing off on the accuracy and completeness of the data before going live?",
        "options": [
            "A) IS auditor",
            "B) Database administrator",
            "C) Project manager",
            "D) Data owner"
        ],
        "correct": "D",
        "explanation": "The data owner is accountable for the accuracy and completeness of the data. The IS auditor verifies that the process is followed, but the sign‑off authority rests with the data owner.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 455,
        "question": "A project manager of a project that is scheduled to take 18 months to complete announces that the project is in a healthy financial position because, after 6 months, only one‑sixth of the budget has been spent. The IS auditor should FIRST determine:",
        "options": [
            "A) what amount of progress against the schedule has been achieved.",
            "B) if the project budget can be reduced.",
            "C) if the project could be brought in ahead of schedule.",
            "D) if the budget savings can be applied to increase the project scope."
        ],
        "correct": "A",
        "explanation": "Spending less than planned could be due to slow progress. The auditor must first compare actual progress against the schedule to accurately assess the project's status.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 456,
        "question": "A manager of a project was not able to implement all audit recommendations by the target date. The IS auditor should:",
        "options": [
            "A) recommend that the project be halted until the issues are resolved.",
            "B) recommend that compensating controls be implemented.",
            "C) evaluate risks associated with the unresolved issues.",
            "D) recommend that the project manager reallocate test resources to resolve the issues."
        ],
        "correct": "C",
        "explanation": "The auditor should first assess the risks posed by the unresolved recommendations. After evaluating the risks, management can decide on appropriate actions such as compensating controls or risk acceptance.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 457,
        "question": "Which of the following techniques would BEST help an IS auditor gain reasonable assurance that a project can meet its target date?",
        "options": [
            "A) Estimation of the actual end date based on the completion percentages and estimated time to complete, taken from status reports.",
            "B) Confirmation of the target date based on interviews with experienced managers and staff involved in the completion of the project deliverables.",
            "C) Extrapolation of the overall end date based on completed work packages and current resources.",
            "D) Calculation of the expected end date based on current resources and remaining available project budget."
        ],
        "correct": "C",
        "explanation": "Extrapolating the end date from completed work packages and current resources provides a realistic, objective forecast based on actual progress, unlike subjective interviews or simple percentage estimates.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 458,
        "question": "Which of the following situations would increase the likelihood of fraud?",
        "options": [
            "A) Application programmers are implementing changes to production programs.",
            "B) Application programmers are implementing changes to test programs.",
            "C) Operations support staff are implementing changes to batch schedules.",
            "D) Database administrators are implementing changes to data structures."
        ],
        "correct": "A",
        "explanation": "Allowing application programmers to implement changes directly to production programs bypasses segregation of duties and creates significant fraud risk.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 459,
        "question": "The purpose of a checksum on an amount field in an electronic data interchange (EDI) communication of financial transactions is to ensure:",
        "options": [
            "A) integrity.",
            "B) authenticity.",
            "C) authorization.",
            "D) nonrepudiation."
        ],
        "correct": "A",
        "explanation": "A checksum is used to verify that the data has not been altered during transmission, thereby ensuring integrity.",
        "domain": "Protection of Information Assets"
    },
    {
        "id": 460,
        "question": "Before implementing controls, management should FIRST ensure that the controls:",
        "options": [
            "A) satisfy a requirement in addressing a risk issue.",
            "B) do not reduce productivity.",
            "C) are based on a cost‑benefit analysis.",
            "D) are detective or corrective."
        ],
        "correct": "A",
        "explanation": "The primary purpose of a control is to mitigate a risk. Therefore, management must first confirm that the control effectively addresses the identified risk.",
        "domain": "Governance & Management of IT"
    },
    {
        "id": 461,
        "question": "Information for detecting unauthorized input from a terminal would be BEST provided by the:",
        "options": [
            "A) Console log printout",
            "B) Transaction journal",
            "C) Automated suspense file listing",
            "D) User error report"
        ],
        "correct": "B",
        "explanation": "The transaction journal records all transactions, allowing comparison with authorized source documents to identify unauthorized input.",
        "domain": "Protection of Information Assets"
    },
    {
        "id": 462,
        "question": "Which of the following types of data validation editing checks is used to determine if a field contains data and not zeros or blanks?",
        "options": [
            "A) Check digit",
            "B) Existence check",
            "C) Completeness check",
            "D) Reasonableness check"
        ],
        "correct": "C",
        "explanation": "A completeness check verifies that a field contains actual data (i.e., not zeros or blanks).",
        "domain": "Protection of Information Assets"
    },
    {
        "id": 463,
        "question": "The editing/validation of data entered at a remote site would be performed MOST effectively at the:",
        "options": [
            "A) Central processing site after running the application system",
            "B) Central processing site during the running of the application system",
            "C) Remote processing site after transmission of the data to the central processing site",
            "D) Remote processing site prior to transmission of the data to the central processing site"
        ],
        "correct": "D",
        "explanation": "Data should be validated as early as possible – ideally at the remote site before transmission – to prevent erroneous data from entering the central system.",
        "domain": "Protection of Information Assets"
    },
    {
        "id": 464,
        "question": "To reduce the possibility of losing data during processing, the FIRST point at which control totals should be implemented is:",
        "options": [
            "A) During data preparation",
            "B) In transit to the computer",
            "C) Between related computer runs",
            "D) During the return of the data to the user department"
        ],
        "correct": "A",
        "explanation": "Control totals should be implemented at the earliest possible point – during data preparation – to ensure data integrity from the outset.",
        "domain": "Protection of Information Assets"
    },
    {
        "id": 465,
        "question": "Functional acknowledgements are used:",
        "options": [
            "A) As an audit trail for EDI transactions",
            "B) To functionally describe the IS department",
            "C) To document user roles and responsibilities",
            "D) As a functional description of application software"
        ],
        "correct": "A",
        "explanation": "In EDI, functional acknowledgements confirm the receipt of electronic documents and serve as an audit trail.",
        "domain": "Protection of Information Assets"
    },
    {
        "id": 466,
        "question": "A proposed transaction processing application will have many data capture sources and outputs in paper and electronic form. To ensure that transactions are not lost during processing, an IS auditor should recommend the inclusion of:",
        "options": [
            "A) Validation controls",
            "B) Internal credibility checks",
            "C) Clerical control procedures",
            "D) Automated systems balancing"
        ],
        "correct": "D",
        "explanation": "Automated systems balancing ensures that total inputs match total outputs, thereby detecting lost transactions.",
        "domain": "Protection of Information Assets"
    },
    {
        "id": 467,
        "question": "What process uses test data as part of a comprehensive test of program controls in a continuous online manner?",
        "options": [
            "A) Test data/check",
            "B) Base-case system evaluation",
            "C) Integrated test facility (ITF)",
            "D) Parallel simulation"
        ],
        "correct": "B",
        "explanation": "A base‑case system evaluation uses test data to continuously validate program controls over time. ITF is a similar technique but is specifically for testing in a live environment; the question asks for the process that uses test data continuously, which is base‑case system evaluation.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 468,
        "question": "What control detects transmission errors by appending calculated bits onto the end of each segment of data?",
        "options": [
            "A) Reasonableness check",
            "B) Parity check",
            "C) Redundancy check",
            "D) Check digits"
        ],
        "correct": "C",
        "explanation": "A redundancy check (such as a CRC) appends calculated bits to detect transmission errors. Parity checks are hardware‑oriented, and check digits detect transcription/transposition errors.",
        "domain": "Protection of Information Assets"
    },
    {
        "id": 469,
        "question": "Which of the following data validation edits is effective in detecting transposition and transcription errors?",
        "options": [
            "A) Range check",
            "B) Check digit",
            "C) Validity check",
            "D) Duplicate check"
        ],
        "correct": "B",
        "explanation": "A check digit is mathematically calculated and appended to data; it effectively detects transposition and transcription errors.",
        "domain": "Protection of Information Assets"
    },
    {
        "id": 470,
        "question": "Which of the following is the GREATEST risk when implementing a data warehouse?",
        "options": [
            "A) Increased response time on the production systems",
            "B) Access controls that are not adequate to prevent data modification",
            "C) Data duplication",
            "D) Data that is not updated or current"
        ],
        "correct": "B",
        "explanation": "In a data warehouse, data should be read‑only for analysis. Inadequate access controls that allow modification pose the greatest risk to data integrity and reliability.",
        "domain": "Protection of Information Assets"
    },
    {
        "id": 471,
        "question": "Which of the following will BEST ensure the successful offshore development of business applications?",
        "options": [
            "A) Stringent contract management practices",
            "B) Detailed and correctly applied specifications",
            "C) Awareness of cultural and political differences",
            "D) Postimplementation reviews"
        ],
        "correct": "B",
        "explanation": "Detailed and correct specifications are essential to bridge the physical and cultural distance in offshore development, ensuring the final product meets business needs.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 472,
        "question": "Which of the following is the GREATEST risk to the effectiveness of application system controls?",
        "options": [
            "A) Removal of manual processing steps",
            "B) Inadequate procedure manuals",
            "C) Collusion between employees",
            "D) Unresolved regulatory compliance issues"
        ],
        "correct": "C",
        "explanation": "Collusion can bypass even well‑designed controls, making it the greatest threat to control effectiveness.",
        "domain": "Governance & Management of IT"
    },
    {
        "id": 473,
        "question": "The MAIN purpose of a transaction audit trail is to:",
        "options": [
            "A) Reduce the use of storage media",
            "B) Determine accountability and responsibility for processed transactions",
            "C) Help an IS auditor trace transactions",
            "D) Provide useful information for capacity planning"
        ],
        "correct": "B",
        "explanation": "The primary objective of an audit trail is to establish accountability and responsibility for processed transactions.",
        "domain": "Information System Auditing Process"
    },
    {
        "id": 474,
        "question": "An appropriate control for ensuring the authenticity of orders received in an EDI application is to:",
        "options": [
            "A) Acknowledge receipt of electronic orders with a confirmation message",
            "B) Perform reasonableness checks on quantities ordered before filling orders",
            "C) Verify the identity of senders and determine if orders correspond to contract terms",
            "D) Encrypt electronic orders"
        ],
        "correct": "C",
        "explanation": "Verifying the sender's identity and matching the order to contract terms ensures that the order is authentic and from an authorized party.",
        "domain": "Protection of Information Assets"
    },
    {
        "id": 475,
        "question": "A manufacturing firm wants to automate its invoice payment system. Objectives state that the system should require considerably less time for review and authorization, and the system should be capable of identifying errors that require follow‑up. Which of the following would BEST meet these objectives?",
        "options": [
            "A) Establishing an inter‑networked system of client servers with suppliers for increased efficiencies",
            "B) Outsourcing the function to a firm specializing in automated payments and accounts receivable/invoice processing",
            "C) Establishing an EDI system of electronic business documents and transactions with key suppliers, computer‑to‑computer, in a standard format",
            "D) Reengineering the existing processing and redesigning the existing system"
        ],
        "correct": "C",
        "explanation": "An EDI system enables real‑time, standardised exchange of business documents, automating invoice payment and quickly identifying errors.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 476,
        "question": "An IS auditor is told by IS management that the organization has recently reached the highest level of the software capability maturity model (CMM). The software quality process MOST recently added by the organization is:",
        "options": [
            "A) Continuous improvement",
            "B) Quantitative quality goals",
            "C) A documented process",
            "D) A process tailored to specific projects"
        ],
        "correct": "A",
        "explanation": "At CMM Level 5 (Optimizing), the key characteristic is continuous process improvement.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 477,
        "question": "During the audit of an acquired software package, an IS auditor learned that the software purchase was based on information obtained through the Internet, rather than from responses to a request for proposal (RFP). The IS auditor should FIRST:",
        "options": [
            "A) Test the software for compatibility with existing hardware",
            "B) Perform a gap analysis",
            "C) Review the licensing policy",
            "D) Ensure that the procedure had been approved"
        ],
        "correct": "D",
        "explanation": "The auditor should first verify that the acquisition procedure followed approved organizational policy. Deviations could indicate weakened controls.",
        "domain": "Information System Auditing Process"
    },
    {
        "id": 478,
        "question": "Failure in which of the following testing stages would have the GREATEST impact on the implementation of new application software?",
        "options": [
            "A) System testing",
            "B) Acceptance testing",
            "C) Integration testing",
            "D) Unit testing"
        ],
        "correct": "B",
        "explanation": "Acceptance testing is the final stage before deployment; failure here causes the most significant delay and cost.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 479,
        "question": "An organization has an integrated development environment (IDE) on which the program libraries reside on the server, but modification/development and testing are done from PC workstations. Which of the following would be a strength of an IDE?",
        "options": [
            "A) Controls the proliferation of multiple versions of programs",
            "B) Expands the programming resources and aids available",
            "C) Increases program and processing integrity",
            "D) Prevents valid changes from being overwritten by other changes"
        ],
        "correct": "B",
        "explanation": "An IDE provides programmers with enhanced tools and resources, aiding development and testing. Version control and change integrity are separate functions.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 480,
        "question": "Which of the following is the most important element in the design of a data warehouse?",
        "options": [
            "A) Quality of the metadata",
            "B) Speed of the transactions",
            "C) Volatility of the data",
            "D) Vulnerability of the system"
        ],
        "correct": "A",
        "explanation": "Quality metadata defines the structure and meaning of data, enabling efficient queries and analysis. It is the cornerstone of a data warehouse.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 481,
        "question": "Ideally, stress testing should be carried out in a:",
        "options": [
            "A) Test environment using test data",
            "B) Production environment using live workloads",
            "C) Test environment using live workloads",
            "D) Production environment using test data"
        ],
        "correct": "C",
        "explanation": "Stress testing should simulate real‑world conditions (live workloads) but in a safe test environment to avoid impacting production.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 482,
        "question": "Which of the following is an object‑oriented technology characteristic that permits an enhanced degree of security over data?",
        "options": [
            "A) Inheritance",
            "B) Dynamic warehousing",
            "C) Encapsulation",
            "D) Polymorphism"
        ],
        "correct": "C",
        "explanation": "Encapsulation restricts direct access to an object's internal data, allowing interaction only through defined methods, thus enhancing security.",
        "domain": "Protection of Information Assets"
    },
    {
        "id": 483,
        "question": "Which of the following is a dynamic analysis tool for the purpose of testing software modules?",
        "options": [
            "A) Black box test",
            "B) Desk checking",
            "C) Structured walkthrough",
            "D) Design and code"
        ],
        "correct": "A",
        "explanation": "A black box test is a dynamic analysis technique that tests software modules without knowledge of internal code, using input/output analysis.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 484,
        "question": "The phases and deliverables of a system development life cycle (SDLC) project should be determined:",
        "options": [
            "A) During the initial planning stages of the project.",
            "B) After early planning has been completed, but before work has begun.",
            "C) Throughout the work stages, based on risks and exposures.",
            "D) Only after all risks and exposures have been identified and the IS auditor has recommended appropriate controls."
        ],
        "correct": "A",
        "explanation": "Phases and deliverables should be defined early during project planning to ensure structure and control from the start.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 485,
        "question": "Which of the following is a management technique that enables organizations to develop strategically important systems faster, while reducing development costs and maintaining quality?",
        "options": [
            "A) Function point analysis",
            "B) Critical path methodology",
            "C) Rapid application development",
            "D) Program evaluation review technique"
        ],
        "correct": "C",
        "explanation": "Rapid Application Development (RAD) emphasizes speed, reduced costs, and quality through iterative prototyping.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 486,
        "question": "When implementing an application software package, which of the following presents the GREATEST risk?",
        "options": [
            "A) Uncontrolled multiple software versions",
            "B) Source programs that are not synchronized with object code",
            "C) Incorrectly set parameters",
            "D) Programming errors"
        ],
        "correct": "C",
        "explanation": "Incorrect parameters can immediately cause the software to malfunction or produce erroneous results, making it the greatest risk during implementation.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 487,
        "question": "Which of the following is an advantage of prototyping?",
        "options": [
            "A) The finished system normally has strong internal controls.",
            "B) Prototype systems can provide significant time and cost savings.",
            "C) Change control is often less complicated with prototype systems.",
            "D) It ensures that functions or extras are not added to the intended system."
        ],
        "correct": "B",
        "explanation": "Prototyping saves time and costs by allowing early user feedback and iterative changes, though it may weaken controls if not properly managed.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 488,
        "question": "A decision support system (DSS):",
        "options": [
            "A) Is aimed at solving highly structured problems.",
            "B) Combines the use of models with nontraditional data access and retrieval functions.",
            "C) Emphasizes flexibility in the decision‑making approach of users.",
            "D) Supports only structured decision‑making tasks."
        ],
        "correct": "C",
        "explanation": "DSS is designed to support semi‑structured and unstructured decisions, emphasizing flexibility in user decision making.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 489,
        "question": "An advantage of using sanitized live transactions in test data is that:",
        "options": [
            "A) All transaction types will be included.",
            "B) Every error condition is likely to be tested.",
            "C) No special routines are required to assess the results.",
            "D) Test transactions are representative of live processing."
        ],
        "correct": "D",
        "explanation": "Sanitized live data closely mirrors real production data, making tests more realistic without exposing sensitive information.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 490,
        "question": "An IS auditor's PRIMARY concern when application developers wish to use a copy of yesterday's production transaction file for volume tests is that:",
        "options": [
            "A) Users may prefer to use contrived data for testing.",
            "B) Unauthorized access to sensitive data may result.",
            "C) Error handling and credibility checks may not be fully proven.",
            "D) The full functionality of the new process may not necessarily be tested."
        ],
        "correct": "B",
        "explanation": "Using live production data without proper sanitization risks exposing confidential information. The primary concern is data confidentiality.",
        "domain": "Protection of Information Assets"
    },
    {
        "id": 491,
        "question": "Which of the following is the PRIMARY purpose for conducting parallel testing?",
        "options": [
            "A) To determine if the system is cost‑effective",
            "B) To enable comprehensive unit and system testing",
            "C) To highlight errors in the program interfaces with files",
            "D) To ensure the new system meets user requirements"
        ],
        "correct": "D",
        "explanation": "Parallel testing compares the new system's results with the old system to verify that the new system meets user requirements before cutover.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 492,
        "question": "The knowledge base of an expert system that uses questionnaires to lead the user through a series of choices before a conclusion is reached is known as:",
        "options": [
            "A) Rules",
            "B) Decision trees",
            "C) Semantic nets",
            "D) Dataflow diagrams"
        ],
        "correct": "B",
        "explanation": "Decision trees use a series of questions to guide users to a conclusion, forming a key part of an expert system's knowledge base.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 493,
        "question": "An advantage in using a bottom‑up vs. a top‑down approach to software testing is that:",
        "options": [
            "A) Interface errors are detected earlier.",
            "B) Confidence in the system is achieved earlier.",
            "C) Errors in critical modules are detected earlier.",
            "D) Major functions and processing are tested earlier."
        ],
        "correct": "C",
        "explanation": "Bottom‑up testing starts with individual modules, so errors in critical low‑level modules are found early.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 494,
        "question": "During which of the following phases in system development would user acceptance test plans normally be prepared?",
        "options": [
            "A) Feasibility study",
            "B) Requirements definition",
            "C) Implementation planning",
            "D) Postimplementation review"
        ],
        "correct": "B",
        "explanation": "User acceptance test plans are developed during the requirements definition phase to ensure the system will satisfy user needs.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 495,
        "question": "The use of object‑oriented design and development techniques would MOST likely:",
        "options": [
            "A) Facilitate the ability to reuse modules.",
            "B) Improve system performance.",
            "C) Enhance control effectiveness.",
            "D) Speed up the system development life cycle."
        ],
        "correct": "A",
        "explanation": "Object‑oriented design promotes reuse of code modules, which is its primary advantage.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 496,
        "question": "Which of the following should be included in a feasibility study for a project to implement an EDI process?",
        "options": [
            "A) The encryption algorithm format",
            "B) The detailed internal control procedures",
            "C) The necessary communication protocols",
            "D) The proposed trusted third‑party agreement"
        ],
        "correct": "C",
        "explanation": "A feasibility study must assess technical requirements, and communication protocols are a key technical aspect of EDI.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 497,
        "question": "When a new system is to be implemented within a short time frame, it is MOST important to:",
        "options": [
            "A) Finish writing user manuals.",
            "B) Perform user acceptance testing.",
            "C) Add last‑minute enhancements to functionalities.",
            "D) Ensure that the code has been documented and reviewed."
        ],
        "correct": "B",
        "explanation": "User acceptance testing verifies that the system meets requirements before going live. Even with time constraints, skipping UAT is extremely risky.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 498,
        "question": "An organization has contracted with a vendor for a turnkey solution for their electronic toll collection system (ETCS). The vendor has provided its proprietary application software as part of the solution. The contract should require that:",
        "options": [
            "A) A backup server be available to run ETCS operations with up‑to‑date data.",
            "B) A backup server be loaded with all the relevant software and data.",
            "C) The systems staff of the organization be trained to handle any event.",
            "D) Source code of the ETCS application be placed in escrow."
        ],
        "correct": "D",
        "explanation": "Source code escrow protects the organization by ensuring access to the code if the vendor goes out of business or fails to support the product.",
        "domain": "Acquisition, Development & Implementation"
    },
    {
        "id": 499,
        "question": "The MOST likely explanation for the use of applets in an Internet application is that:",
        "options": [
            "A) It is sent over the network from the server.",
            "B) The server does not run the program and the output is not sent over the network.",
            "C) They improve the performance of the web server and network.",
            "D) It is a JAVA program downloaded through the web browser and executed by the web server of the client machine."
        ],
        "correct": "C",
        "explanation": "Applets run on the client side, reducing server load and network traffic, thereby improving overall performance.",
        "domain": "Operations and Business Resilience"
    },
    {
        "id": 500,
        "question": "A company has contracted with an external consulting firm to implement a commercial financial system to replace its existing system developed in‑house. In reviewing the proposed development approach, which of the following would be of GREATEST concern?",
        "options": [
            "A) Acceptance testing is to be managed by users.",
            "B) A quality plan is not part of the contracted deliverables.",
            "C) Not all business functions will be available on initial implementation.",
            "D) Prototyping is being used to confirm that the system meets business requirements."
        ],
        "correct": "B",
        "explanation": "A quality plan is essential to ensure the project meets its objectives. Its absence is a major risk to the overall quality and success of the implementation.",
        "domain": "Acquisition, Development & Implementation"
    }
]
import streamlit as st
import random
import re

# ─── Helper to shuffle options for each question ───
def prepare_quiz_questions(questions):
    import random
    prepared = []
    for q in questions:
        original_options = q['options']
        # Shuffle while keeping track of the correct answer's new position
        indexed = list(enumerate(original_options))
        random.shuffle(indexed)
        new_labels = ['A','B','C','D']
        shuffled_options = []
        new_correct = None
        original_correct_letter = q['correct']
        for new_idx, (orig_idx, opt_text) in enumerate(indexed):
            opt_content = opt_text[3:].strip()   # remove original prefix
            new_opt = f"{new_labels[new_idx]}) {opt_content}"
            shuffled_options.append(new_opt)
            # if this option was originally the correct answer
            if opt_text[0] == original_correct_letter:
                new_correct = new_labels[new_idx]
        prepared.append({
            'id': q['id'],
            'question': q['question'],
            'shuffled_options': shuffled_options,
            'shuffled_correct': new_correct,
            'explanation': q.get('explanation',''),
            'domain': q.get('domain','')
        })
    return prepared

# ─── Streamlit App ───
st.set_page_config(page_title="CISA Domain Quiz", layout="wide")
st.markdown("""
<style>
    .stButton > button { width: 100%; border-radius: 8px; font-weight: 600; }
    .correct-answer { background: #d4edda; border: 2px solid #28a745; border-radius: 8px; padding: 10px; color: #155724; }
    .wrong-answer { background: #f8d7da; border: 2px solid #dc3545; border-radius: 8px; padding: 10px; color: #721c24; }
    .explanation-box { background: #e7f3ff; border-left: 4px solid #2196F3; border-radius: 8px; padding: 15px; margin-top: 10px; color: black; }
    .score-card { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 12px; padding: 20px; text-align: center; }
</style>
""", unsafe_allow_html=True)

# Session state
for key, val in [('current_index',0), ('answers',{}), ('submitted',{}), ('score',0), ('total_answered',0), ('shuffled',[])]:
    if key not in st.session_state:
        st.session_state[key] = val

# Sidebar
with st.sidebar:
    st.title("📋 CISA 150‑500")
    st.markdown("---")
    # Domain filter
    all_domains = sorted(list(set(q['domain'] for q in question_bank)))
    selected = st.multiselect("Filter by CISA Domain:", all_domains, default=all_domains)
    eligible = [q for q in question_bank if q['domain'] in selected]
    max_q = len(eligible)
    if max_q == 0:
        st.warning("No questions match selected domains.")
        num_q = 0
    else:
        num_q = st.number_input("Number of questions:", 1, max_q, min(50, max_q))
    mode = st.radio("Selection mode:", ["Random", "Sequential (first N)"], index=0)
    if st.button("🚀 Start Quiz", use_container_width=True, type="primary"):
        if max_q == 0:
            st.error("Select at least one domain.")
        else:
            if mode == "Random":
                selected_qs = random.sample(eligible, num_q)
            else:
                selected_qs = eligible[:num_q]
            # Shuffle options and store
            st.session_state.shuffled = prepare_quiz_questions(selected_qs)
            st.session_state.current_index = 0
            st.session_state.answers = {}
            st.session_state.submitted = {}
            st.session_state.score = 0
            st.session_state.total_answered = 0
            st.rerun()
    if st.button("🔄 Reset to All Questions", use_container_width=True):
        st.session_state.shuffled = question_bank.copy()
        st.session_state.current_index = 0
        st.session_state.answers = {}
        st.session_state.submitted = {}
        st.session_state.score = 0
        st.session_state.total_answered = 0
        st.rerun()
    total_q = len(st.session_state.shuffled)
    if total_q:
        st.markdown(f"""
        <div class="score-card">
            <h3>📊 Score</h3>
            <h1>{st.session_state.score} / {st.session_state.total_answered}</h1>
            <p>{total_q} questions loaded</p>
        </div>
        """, unsafe_allow_html=True)
        st.progress((st.session_state.current_index+1)/total_q, text=f"Q {st.session_state.current_index+1}/{total_q}")
    c1,c2,c3 = st.columns(3)
    with c1:
        if st.button("⬅️ Prev", disabled=(st.session_state.current_index==0)):
            st.session_state.current_index -= 1; st.rerun()
    with c2:
        j = st.number_input("Jump",1,total_q,st.session_state.current_index+1,label_visibility="collapsed")
        if st.button("Go"): st.session_state.current_index=j-1; st.rerun()
    with c3:
        if st.button("Next ➡️", disabled=(st.session_state.current_index>=total_q-1)):
            st.session_state.current_index += 1; st.rerun()

# Main display
st.title("CISA Exam Prep – Official Domains")
st.markdown("*Select domains, choose number of questions, and start your quiz.*")
st.markdown("---")

total_q = len(st.session_state.shuffled)
if total_q and 0 <= st.session_state.current_index < total_q:
    q = st.session_state.shuffled[st.session_state.current_index]
    qid = q['id']
    domain = q['domain']
    st.markdown(f"""
    <div style="background:#f8f9fa; padding:20px; border-radius:12px; margin-bottom:20px; border:1px solid #dee2e6;">
        <h3 style="color:black;">Q{st.session_state.current_index+1} (ID:{qid}) 
        <small style="color:#666;">- {domain}</small></h3>
        <p style="font-size:18px; color:black; font-weight:500;">{q['question']}</p>
    </div>
    """, unsafe_allow_html=True)

    options = q['shuffled_options']
    labels = [o[0] for o in options]
    texts  = [o[3:].strip() for o in options]
    correct_letter = q['shuffled_correct']

    if qid not in st.session_state.submitted:
        sel = st.radio("Choose:", options=labels, format_func=lambda x: f"{x}) {texts[labels.index(x)]}",
                       key=f"r{qid}", index=None)
        c1,c2 = st.columns(2)
        with c1:
            if st.button("✅ Submit", disabled=(sel is None), use_container_width=True, type="primary"):
                ok = (sel == correct_letter)
                st.session_state.submitted[qid] = {'selected': sel, 'correct': ok}
                st.session_state.answers[qid] = sel
                st.session_state.total_answered += 1
                if ok: st.session_state.score += 1
                st.rerun()
        with c2:
            if st.button("⏭️ Skip", use_container_width=True):
                st.session_state.current_index = min(total_q-1, st.session_state.current_index+1)
                st.rerun()
    else:
        sub = st.session_state.submitted[qid]
        sel = sub['selected']
        ok = sub['correct']
        st.markdown("### Result:")
        for i,(lbl,txt) in enumerate(zip(labels,texts)):
            if lbl == correct_letter:
                st.markdown(f'<div class="correct-answer">✅ {lbl}) {txt} – Correct</div>', unsafe_allow_html=True)
            elif lbl == sel and not ok:
                st.markdown(f'<div class="wrong-answer">❌ {lbl}) {txt} – Your answer</div>', unsafe_allow_html=True)
            else:
                st.markdown(f"{lbl}) {txt}")
        if ok: st.success("🎉 Correct!")
        else: st.error("😔 Incorrect.")
        st.markdown(f"""
        <div class="explanation-box"><b>📖 Explanation:</b><br>{q['explanation']}</div>
        """, unsafe_allow_html=True)
        c1,c2 = st.columns(2)
        with c1:
            if st.button("⬅️ Previous Q", use_container_width=True):
                st.session_state.current_index -= 1; st.rerun()
        with c2:
            nxt = "Next ➡️" if st.session_state.current_index < total_q-1 else "🏁 Finish"
            if st.button(nxt, use_container_width=True):
                if st.session_state.current_index < total_q-1:
                    st.session_state.current_index += 1
                st.rerun()

st.markdown("---")
st.markdown("<div style='text-align:center; color:#666;'>CISA | Official domains | Study consistently 🎓</div>", unsafe_allow_html=True)
