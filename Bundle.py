import streamlit as st
import random
import re

# ========== SAMPLE QUESTIONS (with prefixed options) ==========
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
    {
        "id": 2,
        "domain": "Domain 1 – The Audit Process",
        "question": "An auditor is examining an IT organization's change control process. The auditor has determined that change advisory board (CAB) meetings take place on Tuesdays and Fridays, where planned changes are discussed and approved. The CAB does not discuss emergency changes that are not approved in advance. What opinion should the auditor reach concerning emergency changes?",
        "options": [
            "A) The CAB should not be discussing changes made in the past.",
            "B) The CAB should be discussing recent emergency changes.",
            "C) Personnel should not be making emergency changes without CAB permission.",
            "D) Change control is concerned only with planned changes, not emergency changes."
        ],
        "correct": "B",
        "option_explanations": {
            "A) The CAB should not be discussing changes made in the past.": "Incorrect – A change control process needs to address all changes, including planned and emergency changes.",
            "B) The CAB should be discussing recent emergency changes.": "Correct – The CAB should discuss emergency changes that were made since the last meeting to ensure stakeholder awareness.",
            "C) Personnel should not be making emergency changes without CAB permission.": "Incorrect – Emergency changes are often necessary to counteract unexpected downtime or other issues.",
            "D) Change control is concerned only with planned changes, not emergency changes.": "Incorrect – The change control process should address all changes, both planned future and recent emergency."
        }
    },
    {
        "id": 3,
        "domain": "Domain 1 – The Audit Process",
        "question": "A conspicuous video surveillance system would be characterized as what type(s) of control?",
        "options": [
            "A) Detective and deterrent",
            "B) Detective only",
            "C) Deterrent only",
            "D) Preventive and deterrent"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Detective and deterrent": "Correct – A visible surveillance system records events (detective) and its presence deters wrongdoers (deterrent).",
            "B) Detective only": "Incorrect – When visible, it also acts as a deterrent; hidden cameras would be detective only.",
            "C) Deterrent only": "Incorrect – A working system also records, making it detective; only a fake/inoperative one is solely deterrent.",
            "D) Preventive and deterrent": "Incorrect – Video surveillance does not prevent events, so it is not a preventive control."
        }
    },
    {
        "id": 4,
        "domain": "Domain 1 – The Audit Process",
        "question": "Michael is developing an audit plan for an organization's data center operations. Which of the following will help Michael determine which controls require potentially more scrutiny than others?",
        "options": [
            "A) Security incident log",
            "B) Last year's data center audit results",
            "C) Risk assessment of the data center",
            "D) Data center performance metrics"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Security incident log": "Incorrect – An incident log does not reveal all types of risks and may give a false sense of security.",
            "B) Last year's data center audit results": "Incorrect – Changes since the last audit may not be reflected.",
            "C) Risk assessment of the data center": "Correct – A risk assessment is the primary tool for identifying areas of higher risk.",
            "D) Data center performance metrics": "Incorrect – Performance metrics rarely provide sufficient insight into control risks."
        }
    },
    {
        "id": 5,
        "domain": "Domain 1 – The Audit Process",
        "question": "An organization processes payroll and expense reports in an SaaS-based environment to thousands of corporate customers. Those customers want assurance that the organization's processes are effective. What kind of an audit should the organization undertake?",
        "options": [
            "A) Compliance audit",
            "B) Operational audit",
            "C) Service provider audit",
            "D) IS audit"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Compliance audit": "Incorrect – A compliance audit checks conformity with laws/regulations, not specifically suited for service providers.",
            "B) Operational audit": "Incorrect – An operational audit is for internal use; not the best choice for external assurance.",
            "C) Service provider audit": "Correct – Audits like SSAE18, SOC2, or ISO 27001 are designed to give customers assurance about a service provider's controls.",
            "D) IS audit": "Incorrect – An IS audit is an internal audit of information systems, not the best choice for providing customer assurance."
        }
    },
    {
        "id": 6,
        "domain": "Domain 1 – The Audit Process",
        "question": "An audit project has been taking far too long, and management is beginning to ask questions about its schedule and completion. This audit may be lacking:",
        "options": [
            "A) Effective project management",
            "B) Cooperation from individual auditees",
            "C) Enough skilled auditors",
            "D) Clearly stated scope and objectives"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Effective project management": "Correct – While all answers are plausible, the first area to examine is whether the audit is being effectively project managed.",
            "B) Cooperation from individual auditees": "Incorrect – There isn't enough information to confirm this as the root cause.",
            "C) Enough skilled auditors": "Incorrect – Although possible, it's not the most immediate factor to check.",
            "D) Clearly stated scope and objectives": "Incorrect – Similar to the others, it could be a contributing factor but not the primary one based on given symptoms."
        }
    },
    {
        "id": 7,
        "domain": "Domain 1 – The Audit Process",
        "question": "An auditor is auditing the user account request and fulfillment process. The event population consists of hundreds of transactions, so the auditor cannot view them all. The auditor wants to view a random selection of transactions. This type of sampling is known as:",
        "options": [
            "A) Judgmental sampling",
            "B) Random sampling",
            "C) Stratified sampling",
            "D) Statistical sampling"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Judgmental sampling": "Incorrect – Judgmental sampling involves using professional judgement to choose items, not random selection.",
            "B) Random sampling": "Incorrect – Although a common term, the official ISACA term is statistical sampling.",
            "C) Stratified sampling": "Incorrect – Stratified sampling selects samples from different subgroups (strata), not merely a random overall sample.",
            "D) Statistical sampling": "Correct – Statistical sampling is the appropriate term for selecting a random portion of a population for testing."
        }
    },
    {
        "id": 8,
        "domain": "Domain 1 – The Audit Process",
        "question": "An auditor is auditing an organization's user account request and fulfillment process. What is the first type of evidence collection the auditor will likely want to examine?",
        "options": [
            "A) Observation",
            "B) Document review",
            "C) Walkthrough",
            "D) Corroborative inquiry"
        ],
        "correct": "B",
        "option_explanations": {
            "A) Observation": "Incorrect – Observation typically comes after understanding the documented process.",
            "B) Document review": "Correct – An auditor usually starts by reviewing process documentation to understand how things are supposed to work.",
            "C) Walkthrough": "Incorrect – Walkthroughs are performed after the auditor has examined the documentation.",
            "D) Corroborative inquiry": "Incorrect – Corroborative inquiry occurs later, after walkthroughs, to verify information."
        }
    },
    {
        "id": 9,
        "domain": "Domain 1 – The Audit Process",
        "question": "A lead auditor is building an audit plan for a client's financial accounting system. The plan calls for periodic testing of a large number of transactions throughout the audit project. What is the best approach for accomplishing this?",
        "options": [
            "A) Reperform randomly selected transactions.",
            "B) Periodically submit test transactions to the audit client.",
            "C) Develop one or more CAATs.",
            "D) Request a list of all transactions to analyze."
        ],
        "correct": "C",
        "option_explanations": {
            "A) Reperform randomly selected transactions.": "Incorrect – Manually reperforming a large volume of transactions is too time-consuming.",
            "B) Periodically submit test transactions to the audit client.": "Incorrect – This would also require excessive manual effort.",
            "C) Develop one or more CAATs.": "Correct – Computer-assisted audit techniques (CAATs) automate the testing of large transaction volumes.",
            "D) Request a list of all transactions to analyze.": "Incorrect – While an alternative, the auditor would still need to develop automated analysis; CAATs are the best approach."
        }
    },
    {
        "id": 10,
        "domain": "Domain 1 – The Audit Process",
        "question": "A lead auditor is building an audit plan for a client's financial transaction processing system. The audit will take approximately three months. Which of the following is the best approach for reporting audit exceptions to the audit client?",
        "options": [
            "A) Report the exceptions to the audit committee.",
            "B) List the exceptions in the final audit report.",
            "C) Include the exceptions in a weekly status report.",
            "D) Advise the client of exceptions as they are discovered and confirmed."
        ],
        "correct": "D",
        "option_explanations": {
            "A) Report the exceptions to the audit committee.": "Incorrect – The audit committee is not always the client; the focus should be on informing the responsible party promptly.",
            "B) List the exceptions in the final audit report.": "Incorrect – Waiting until the final report is rarely justified; early communication allows remediation.",
            "C) Include the exceptions in a weekly status report.": "Incorrect – While a valid alternative, immediate communication is preferred to give the client more time to act.",
            "D) Advise the client of exceptions as they are discovered and confirmed.": "Correct – It is best practice to inform the client right away so they can begin addressing the issue."
        }
    },
    {
        "id": 11,
        "domain": "Domain 1 – The Audit Process",
        "question": "Which of the following is true about the ISACA Audit Standards and Audit Guidelines?",
        "options": [
            "A) ISACA Audit Standards are mandatory.",
            "B) ISACA Audit Standards are optional.",
            "C) ISACA Audit Guidelines are mandatory.",
            "D) ISACA Audit Standards are only mandatory for SOX audits."
        ],
        "correct": "A",
        "option_explanations": {
            "A) ISACA Audit Standards are mandatory.": "Correct – Compliance with ISACA Audit Standards is required for CISA certification holders.",
            "B) ISACA Audit Standards are optional.": "Incorrect – They are not optional; they are a condition of certification.",
            "C) ISACA Audit Guidelines are mandatory.": "Incorrect – Guidelines are suggestions, not mandatory.",
            "D) ISACA Audit Standards are only mandatory for SOX audits.": "Incorrect – They apply to all audits, although additional standards may exist for specialized audits."
        }
    },
    {
        "id": 12,
        "domain": "Domain 1 – The Audit Process",
        "question": "An auditor is auditing an organization's identity and access management program. The auditor has found that automated workflows are used to receive and track access requests and approvals. However, the auditor has identified a number of exceptions where subjects were granted access without the necessary requests and approvals. What remedy should the auditor recommend?",
        "options": [
            "A) Monthly review of access approvers",
            "B) Annual review of access approvers",
            "C) Annual user access reviews",
            "D) Monthly user access reviews"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Monthly review of access approvers": "Incorrect – The problem is not about the correctness of approvers but about bypassing the request process entirely.",
            "B) Annual review of access approvers": "Incorrect – This does not address the root issue of unauthorized access grants.",
            "C) Annual user access reviews": "Incorrect – Annual reviews are too infrequent to quickly detect and correct control failures.",
            "D) Monthly user access reviews": "Correct – Frequent user access reviews can partly compensate for control failures and detect exceptions sooner."
        }
    },
    {
        "id": 13,
        "domain": "Domain 1 – The Audit Process",
        "question": "Why are preventive controls preferred over detective controls?",
        "options": [
            "A) Preventive controls are easier to justify and implement than detective controls.",
            "B) Preventive controls are less expensive to implement than detective controls.",
            "C) Preventive controls stop unwanted events from occurring, while detective controls only record them.",
            "D) Detective controls stop unwanted events from occurring, while preventive controls only record them."
        ],
        "correct": "C",
        "option_explanations": {
            "A) Preventive controls are easier to justify and implement than detective controls.": "Incorrect – Prevention is not necessarily easier or cheaper; it's preferred because it stops events.",
            "B) Preventive controls are less expensive to implement than detective controls.": "Incorrect – Cost is not the primary factor; the ability to stop events is.",
            "C) Preventive controls stop unwanted events from occurring, while detective controls only record them.": "Correct – Prevention is the first line of defense; detection is used when prevention is not feasible or cost-effective.",
            "D) Detective controls stop unwanted events from occurring, while preventive controls only record them.": "Incorrect – This reverses the definitions."
        }
    },
    {
        "id": 14,
        "domain": "Domain 1 – The Audit Process",
        "question": "For the purposes of audit planning, can an auditor rely upon the audit client's risk assessment?",
        "options": [
            "A) Yes, in all cases.",
            "B) Yes, if the risk assessment was performed by a qualified external entity.",
            "C) No. The auditor must perform a risk assessment himself or herself.",
            "D) No. The auditor does not require a risk assessment to develop an audit plan."
        ],
        "correct": "B",
        "option_explanations": {
            "A) Yes, in all cases.": "Incorrect – If the client's risk assessment is biased or unqualified, the auditor should not rely on it.",
            "B) Yes, if the risk assessment was performed by a qualified external entity.": "Correct – An external, qualified risk assessment can be used to create a risk-based audit plan.",
            "C) No. The auditor must perform a risk assessment himself or herself.": "Incorrect – It is not always necessary; an external one can be used if sound.",
            "D) No. The auditor does not require a risk assessment to develop an audit plan.": "Incorrect – A risk assessment helps to focus the audit on higher-risk areas."
        }
    },
    {
        "id": 15,
        "domain": "Domain 1 – The Audit Process",
        "question": "An organization processes payroll and expense reports in an SaaS-based environment to thousands of corporate customers. Those customers want assurance that the organization's processes are effective. What kind of an audit should the organization undertake?",
        "options": [
            "A) AUP",
            "B) PA-DSS",
            "C) PCI-DSS",
            "D) SSAE18"
        ],
        "correct": "D",
        "option_explanations": {
            "A) AUP": "Incorrect – An AUP audit is a viable alternative but not the best choice for a financial services provider.",
            "B) PA-DSS": "Incorrect – This audit is for payment applications, not payroll services.",
            "C) PCI-DSS": "Incorrect – This is for credit card processing environments.",
            "D) SSAE18": "Correct – SSAE18 audits are specifically designed for financial service providers to give their customers' auditors reliance on their controls."
        }
    },
    {
        "id": 16,
        "domain": "Domain 1 – The Audit Process",
        "question": "An auditor is auditing an organization's system-hardening policy within its vulnerability management process. The auditor has examined the organization's system-hardening standards and wants to examine the configuration of some of the production servers. What is the best method for the auditor to obtain evidence?",
        "options": [
            "A) Capture screenshots from servers selected by the systems engineer during a walkthrough.",
            "B) Request screenshots from servers selected by the systems engineer.",
            "C) Request screenshots from randomly selected servers from the systems engineer.",
            "D) Capture screenshots from randomly selected servers during a walkthrough with the systems engineer."
        ],
        "correct": "D",
        "option_explanations": {
            "A) Capture screenshots from servers selected by the systems engineer during a walkthrough.": "Incorrect – The auditor should select the servers to avoid potential bias.",
            "B) Request screenshots from servers selected by the systems engineer.": "Incorrect – The systems engineer might select only compliant servers, compromising evidence integrity.",
            "C) Request screenshots from randomly selected servers from the systems engineer.": "Incorrect – The auditor cannot be sure that the screenshots match the selected servers without directly observing.",
            "D) Capture screenshots from randomly selected servers during a walkthrough with the systems engineer.": "Correct – The auditor selects the sample and observes the evidence collection, ensuring reliability."
        }
    },
    {
        "id": 17,
        "domain": "Domain 1 – The Audit Process",
        "question": "An auditor is auditing the user account request and fulfillment process. The event population consists of hundreds of transactions, so the auditor cannot view them all. The auditor wants to view a random selection of transactions, as well as some of the transactions for privileged access requests. This type of sampling is known as:",
        "options": [
            "A) Judgmental sampling",
            "B) Random sampling",
            "C) Stratified sampling",
            "D) Statistical sampling"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Judgmental sampling": "Correct – The auditor is using professional judgement to include specific high-risk items (privileged access) alongside random selections.",
            "B) Random sampling": "Incorrect – Not all selections are random; privileged access requests are deliberately chosen.",
            "C) Stratified sampling": "Incorrect – Stratified sampling divides the population into distinct subgroups first, then samples from each.",
            "D) Statistical sampling": "Incorrect – Statistical sampling would rely purely on random selection, not the auditor's judgement to include high-risk items."
        }
    },
    {
        "id": 18,
        "domain": "Domain 1 – The Audit Process",
        "question": "An auditor is auditing an organization's user account request and fulfillment process. An auditor has requested that the control owner describe the process to the auditor. What type of auditing is taking place?",
        "options": [
            "A) Observation",
            "B) Document review",
            "C) Walkthrough",
            "D) Corroborative inquiry"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Observation": "Incorrect – Observation involves watching personnel perform the process, not just describing it.",
            "B) Document review": "Incorrect – Document review is reading documents alone, away from the control owner.",
            "C) Walkthrough": "Correct – A walkthrough is when the control owner describes each step of the process to the auditor.",
            "D) Corroborative inquiry": "Incorrect – Corroborative inquiry typically occurs after walkthroughs, with other personnel."
        }
    },
    {
        "id": 19,
        "domain": "Domain 1 – The Audit Process",
        "question": "An external audit firm is performing an audit of a customer's financial accounting processes and IT systems. While examining a data storage system's user access permissions, the staff auditor has discovered the presence of illegal content. What should the staff auditor do next?",
        "options": [
            "A) Notify law enforcement.",
            "B) Inform his or her supervisor.",
            "C) Notify the auditee.",
            "D) Notify the auditee's audit committee."
        ],
        "correct": "B",
        "option_explanations": {
            "A) Notify law enforcement.": "Incorrect – Although this may eventually be required, the auditor should first inform their supervisor who can decide the appropriate course of action.",
            "B) Inform his or her supervisor.": "Correct – The staff auditor should escalate the issue to their supervisor, who will then follow firm policy, which may include notifying law enforcement.",
            "C) Notify the auditee.": "Incorrect – The auditee could be the perpetrator; alerting them might lead to destruction of evidence.",
            "D) Notify the auditee's audit committee.": "Incorrect – The audit committee may not be the correct first contact; the supervisor should guide the response."
        }
    },
    {
        "id": 20,
        "domain": "Domain 1 – The Audit Process",
        "question": "A QSA auditor in an audit firm has completed a PCI-DSS audit of a client and has found the client to be noncompliant with one or more PCI-DSS controls. Management in the audit firm has asked the QSA auditor to sign off on the audit as compliant, arguing that the client's level of compliance has improved from prior years. What should the QSA auditor do?",
        "options": [
            "A) Refuse to sign the audit report as compliant.",
            "B) Sign the audit report as compliant, but under duress.",
            "C) Sign the audit report as compliant.",
            "D) Notify the audit client of the matter."
        ],
        "correct": "A",
        "option_explanations": {
            "A) Refuse to sign the audit report as compliant.": "Correct – Signing a false report violates the ISACA Code of Professional Ethics and could result in loss of certification.",
            "B) Sign the audit report as compliant, but under duress.": "Incorrect – Even under duress, signing a false report is unethical.",
            "C) Sign the audit report as compliant.": "Incorrect – This would be a clear ethical violation.",
            "D) Notify the audit client of the matter.": "Incorrect – This may cause confusion; the auditor should uphold their ethical duty."
        }
    },
    {
        "id": 21,
        "domain": "Domain 1 – The Audit Process",
        "question": "An organization wants to drive accountability for the performance of security controls to their respective control owners. Which activity is the best to undertake to accomplish this objective?",
        "options": [
            "A) Direct control owners to sign a document of accountability.",
            "B) Have the internal audit department audit the controls.",
            "C) Have an external audit firm audit the controls.",
            "D) Undergo control self-assessments (CSAs)."
        ],
        "correct": "D",
        "option_explanations": {
            "A) Direct control owners to sign a document of accountability.": "Incorrect – Signing a document alone does not foster the same level of ownership as active evaluation.",
            "B) Have the internal audit department audit the controls.": "Incorrect – Audits highlight deficiencies but do not necessarily make control owners take ongoing responsibility.",
            "C) Have an external audit firm audit the controls.": "Incorrect – Similar to internal audits, external audits may not instill continuous ownership.",
            "D) Undergo control self-assessments (CSAs).": "Correct – CSAs force control owners to evaluate their own controls, leading to greater accountability and self-improvement."
        }
    },
    {
        "id": 22,
        "domain": "Domain 1 – The Audit Process",
        "question": "An auditor is evaluating a control related to a key card mechanism protecting a data center from unauthorized visitors. The auditor has determined that the key card control is ineffective because visitors often 'piggyback' their way into the data center. What detective control should be implemented to compensate for this control deficiency?",
        "options": [
            "A) A video surveillance system with 90-day content retention that records all entrances and exits from the data center.",
            "B) A visitors log inside the data center that all visitors would be required to sign",
            "C) A man trap",
            "D) A policy requiring all visitors to be escorted"
        ],
        "correct": "A",
        "option_explanations": {
            "A) A video surveillance system with 90-day content retention that records all entrances and exits from the data center.": "Correct – A video system provides detective evidence that can be reviewed to identify tailgating incidents.",
            "B) A visitors log inside the data center that all visitors would be required to sign": "Incorrect – Unauthorized visitors are unlikely to sign a log, making it ineffective.",
            "C) A man trap": "Incorrect – While effective, it is a preventive control and can be costly; the question asks for a detective control.",
            "D) A policy requiring all visitors to be escorted": "Incorrect – Unauthorized visitors may ignore such a policy, and it's not a detective control."
        }
    },
    {
        "id": 23,
        "domain": "Domain 1 – The Audit Process",
        "question": "A U.S.-based organization processes payroll and expense reports in an SaaS-based environment to thousands of corporate customers. Customers outside the United States want assurance that the organization's processes are effective. What kind of an audit should the organization undertake?",
        "options": [
            "A) ISO/IEC 27001",
            "B) SOC2",
            "C) ISAE3402",
            "D) SSAE18"
        ],
        "correct": "C",
        "option_explanations": {
            "A) ISO/IEC 27001": "Incorrect – While valuable, ISO 27001 covers broad security controls, not specifically financial ones.",
            "B) SOC2": "Incorrect – SOC2 is a general-purpose service provider audit, but ISAE3402 is the international equivalent of SSAE18 for financial services.",
            "C) ISAE3402": "Correct – ISAE3402 is the international version of SSAE18, designed for financial services providers to satisfy international customer requirements.",
            "D) SSAE18": "Incorrect – SSAE18 is technically valid only within the United States; customers outside the U.S. would expect ISAE3402."
        }
    },
    {
        "id": 24,
        "domain": "Domain 1 – The Audit Process",
        "question": "A QSA (PCI) audit firm has been commissioned by a large merchant organization to perform a PCI-DSS report on compliance (ROC). The audit firm has noted that the merchant's compliance deadline is less than one month away. What should the audit firm do next?",
        "options": [
            "A) File a compliance extension with the PCI Standards Council on behalf of the merchant.",
            "B) Inform the merchant that the ROC can be completed on time.",
            "C) Inform the merchant that the ROC cannot be completed on time and that an extension should be requested.",
            "D) File a compliance extension with the merchant's acquiring bank."
        ],
        "correct": "C",
        "option_explanations": {
            "A) File a compliance extension with the PCI Standards Council on behalf of the merchant.": "Incorrect – QSA firms do not file extensions for their clients.",
            "B) Inform the merchant that the ROC can be completed on time.": "Incorrect – It is unlikely that a large merchant's audit can be completed in under a month.",
            "C) Inform the merchant that the ROC cannot be completed on time and that an extension should be requested.": "Correct – The audit firm should inform the merchant of the timeline difficulty and advise them to request an extension from their acquiring bank.",
            "D) File a compliance extension with the merchant's acquiring bank.": "Incorrect – QSA firms do not file extensions on behalf of clients."
        }
    },
    {
        "id": 25,
        "domain": "Domain 1 – The Audit Process",
        "question": "An auditor is developing an audit plan for an accounts payable function. Rather than randomly selecting transactions to examine, the auditor wants to select transactions from low, medium, and large payment amounts. Which sample methodology is appropriate for this approach?",
        "options": [
            "A) Judgmental sampling",
            "B) Stratified sampling",
            "C) Non-random sampling",
            "D) Statistical sampling"
        ],
        "correct": "B",
        "option_explanations": {
            "A) Judgmental sampling": "Incorrect – Judgmental sampling relies on the auditor's professional judgement, not predefined strata like payment amounts.",
            "B) Stratified sampling": "Correct – Stratified sampling divides the population into distinct categories (strata) based on a characteristic (payment amount) and then samples from each.",
            "C) Non-random sampling": "Incorrect – This is not a recognized sampling methodology.",
            "D) Statistical sampling": "Incorrect – Statistical sampling may not capture enough high or low value items if they are rare; stratified sampling ensures representation from each category."
        }
    },
    {
        "id": 26,
        "domain": "Domain 1 – The Audit Process",
        "question": "A cybersecurity audit firm has completed a penetration test of an organization's web application. The final report contains two findings that indicate the presence of two critical vulnerabilities. The organization disputes the findings because of the presence of compensating controls outside of the web application interface. How should the audit proceed?",
        "options": [
            "A) The audit firm should remove the findings from the final report.",
            "B) The organization should select another firm to conduct the penetration test.",
            "C) Organization's management should protest the findings and include a letter that accompanies the pen test report.",
            "D) The audit firm should permit the customer to have some management comments included in the final report."
        ],
        "correct": "D",
        "option_explanations": {
            "A) The audit firm should remove the findings from the final report.": "Incorrect – Findings should not be removed simply because the client disagrees.",
            "B) The organization should select another firm to conduct the penetration test.": "Incorrect – This could be costly and time-consuming without resolving the current dispute.",
            "C) Organization's management should protest the findings and include a letter that accompanies the pen test report.": "Incorrect – A separate management letter is less ideal than including management's comments directly in the report.",
            "D) The audit firm should permit the customer to have some management comments included in the final report.": "Correct – Including management's perspective on each finding is a professional way to handle disputes."
        }
    },
    {
        "id": 27,
        "domain": "Domain 1 – The Audit Process",
        "question": "What is the objective of the ISACA audit standard on organizational independence?",
        "options": [
            "A) The auditor's placement in the organization should ensure the auditor can act independently.",
            "B) The auditor should not work in the same organization as the auditee.",
            "C) To ensure that the auditor has the appearance of independence.",
            "D) To ensure that the auditor has a separate operating budget."
        ],
        "correct": "A",
        "option_explanations": {
            "A) The auditor's placement in the organization should ensure the auditor can act independently.": "Correct – The standard states that the auditor's position in the command structure must allow independence of action.",
            "B) The auditor should not work in the same organization as the auditee.": "Incorrect – Internal auditors often work in the same organization; independence is about reporting structure.",
            "C) To ensure that the auditor has the appearance of independence.": "Incorrect – While appearance is important, the standard stresses actual independence, not just appearance.",
            "D) To ensure that the auditor has a separate operating budget.": "Incorrect – A separate budget does not guarantee independence."
        }
    },
    {
        "id": 28,
        "domain": "Domain 1 – The Audit Process",
        "question": "An auditor is auditing an organization's risk management process. During the walkthrough, the auditor asked the auditee to list all of the sources of information that contribute to the process. The auditee cited penetration tests, vendor advisories, non-vendor advisories, and security incidents as all of the inputs. What conclusion should the auditor draw from this?",
        "options": [
            "A) The process is effective because risks are obtained from several disparate sources.",
            "B) The process is ineffective, as risk assessments apparently do not occur or contribute to the process.",
            "C) The process is effective because both internal and external sources are used.",
            "D) The process is ineffective because an anonymous tip line was not among the sources."
        ],
        "correct": "B",
        "option_explanations": {
            "A) The process is effective because risks are obtained from several disparate sources.": "Incorrect – Missing risk assessments, a critical input, renders the process ineffective.",
            "B) The process is ineffective, as risk assessments apparently do not occur or contribute to the process.": "Correct – Risk assessments are a fundamental input to any risk management process; their absence is a serious deficiency.",
            "C) The process is effective because both internal and external sources are used.": "Incorrect – The process cannot be considered effective without risk assessments, regardless of other sources.",
            "D) The process is ineffective because an anonymous tip line was not among the sources.": "Incorrect – An anonymous tip line is not a core component; the lack of risk assessments is the major issue."
        }
    },
    {
        "id": 29,
        "domain": "Domain 1 – The Audit Process",
        "question": "The capability wherein a server is constituted from backup media is known as which type of control?",
        "options": [
            "A) Primary control",
            "B) Manual control",
            "C) Compensating control",
            "D) Recovery control"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Primary control": "Incorrect – 'Primary' is not a standard control classification.",
            "B) Manual control": "Incorrect – Rebuilding a server from backup could be manual or automated; it's classified by its purpose, not its method.",
            "C) Compensating control": "Incorrect – A compensating control mitigates risk when a primary control is missing or ineffective; restoration is not compensating but recovery.",
            "D) Recovery control": "Correct – Restoring from backup media is a recovery control, bringing a system back to operational state after an incident."
        }
    },
    {
        "id": 30,
        "domain": "Domain 1 – The Audit Process",
        "question": "Prior to planning an audit, an auditor would need to conduct a risk assessment to identify high-risk areas in all of the following situations except for:",
        "options": [
            "A) When a client's most recent risk assessment is two years old",
            "B) When a client's risk assessment does not appear to be adequately rigorous",
            "C) A PCI 'report on compliance' audit",
            "D) A SOC2 audit"
        ],
        "correct": "C",
        "option_explanations": {
            "A) When a client's most recent risk assessment is two years old": "Incorrect – An outdated risk assessment necessitates a new one for proper audit planning.",
            "B) When a client's risk assessment does not appear to be adequately rigorous": "Incorrect – An inadequate risk assessment cannot be relied upon, so the auditor should perform one.",
            "C) A PCI 'report on compliance' audit": "Correct – PCI audits are not risk-based; the auditor must test all controls regardless of a risk assessment.",
            "D) A SOC2 audit": "Incorrect – SOC2 audits are risk-based, so the auditor would need a risk assessment to focus on high-risk areas."
        }
    },
    {
        "id": 31,
        "domain": "Domain 1 – The Audit Process",
        "question": "Which of the following audit types is appropriate for a financial services provider such as a payroll service?",
        "options": [
            "A) SSAE18",
            "B) SAS70",
            "C) AUP",
            "D) Sarbanes-Oxley"
        ],
        "correct": "A",
        "option_explanations": {
            "A) SSAE18": "Correct – SSAE18 audits are specifically designed for financial service providers to provide assurance over financial controls.",
            "B) SAS70": "Incorrect – SAS70 has been deprecated and replaced by SSAE18.",
            "C) AUP": "Incorrect – An AUP audit is general purpose, not specifically tailored for financial services.",
            "D) Sarbanes-Oxley": "Incorrect – Sarbanes-Oxley audits are for the financial reporting processes of U.S. public companies, not for service providers per se."
        }
    },
    {
        "id": 32,
        "domain": "Domain 1 – The Audit Process",
        "question": "Which of the following is the best method for ensuring that an audit project can be completed on time?",
        "options": [
            "A) Distribute a 'provided by client' evidence request list at the start of the audit.",
            "B) Pre-populate the issues list with findings likely to occur.",
            "C) Increase the number of auditors on the audit team.",
            "D) Reduce the frequency of status meetings from weekly to monthly."
        ],
        "correct": "A",
        "option_explanations": {
            "A) Distribute a 'provided by client' evidence request list at the start of the audit.": "Correct – Giving the evidence request list early allows the auditee to prepare and deliver evidence sooner, reducing wait times.",
            "B) Pre-populate the issues list with findings likely to occur.": "Incorrect – This is not an accepted practice and does little to speed up the audit.",
            "C) Increase the number of auditors on the audit team.": "Incorrect – More auditors may not be feasible and does not address delays caused by waiting for evidence.",
            "D) Reduce the frequency of status meetings from weekly to monthly.": "Incorrect – Less frequent communication could actually increase the time to complete the audit."
        }
    },
    {
        "id": 33,
        "domain": "Domain 1 – The Audit Process",
        "question": "An auditor is about to start an audit of a user account access request and fulfillment process. The audit covers a six-month period from January through June. The population contains 1,800 transactions. Which of the following sampling methodologies is best suited for this audit?",
        "options": [
            "A) Examine the results of the client's control self-assessment (CSA).",
            "B) Submit some user account access requests and observe how they are performed.",
            "C) Request the first 30 transactions from the auditee.",
            "D) Request the first five transactions from each month in the audit period."
        ],
        "correct": "D",
        "option_explanations": {
            "A) Examine the results of the client's control self-assessment (CSA).": "Incorrect – The CSA may not be reliable or sufficient for audit evidence; sampling is needed.",
            "B) Submit some user account access requests and observe how they are performed.": "Incorrect – Reperformance assesses current effectiveness, not historical performance over the six-month period.",
            "C) Request the first 30 transactions from the auditee.": "Incorrect – This would only cover the beginning of the period, missing changes that occurred later.",
            "D) Request the first five transactions from each month in the audit period.": "Correct – This provides coverage across the entire audit period, capturing any variations over time."
        }
    },
    {
        "id": 34,
        "domain": "Domain 1 – The Audit Process",
        "question": "An auditor is auditing an organization's personnel onboarding process and is examining the background check process. The auditor is mainly interested in whether background checks are performed for all personnel and whether background check results lead to no-hire decisions. Which of the following evidence collection techniques will support this audit objective?",
        "options": [
            "A) Request the full contents of background checks along with hire/no-hire decisions.",
            "B) Request the background check ledger that includes the candidates' names, results of background checks, and hire/no-hire decisions.",
            "C) Request the hire/no-hire decisions from the auditee.",
            "D) Examine the background check process and note which characteristics for each candidate are included."
        ],
        "correct": "B",
        "option_explanations": {
            "A) Request the full contents of background checks along with hire/no-hire decisions.": "Incorrect – This contains sensitive personal information that the auditor should not need to see.",
            "B) Request the background check ledger that includes the candidates' names, results of background checks, and hire/no-hire decisions.": "Correct – This ledger provides sufficient information to verify that checks are performed and to see the correlation between results and hiring decisions.",
            "C) Request the hire/no-hire decisions from the auditee.": "Incorrect – This does not show whether background checks were actually performed or the relationship between results and decisions.",
            "D) Examine the background check process and note which characteristics for each candidate are included.": "Incorrect – This only examines the process, not the actual records, and won't confirm whether all checks are done."
        }
    },
    {
        "id": 35,
        "domain": "Domain 1 – The Audit Process",
        "question": "An auditor wants to audit the changes made to the DBMS configuration of a financial accounting system. What should the auditor use as the transaction population?",
        "options": [
            "A) All of the transactions in the database",
            "B) All of the requested changes in the change management process",
            "C) All of the changes made to the database",
            "D) All of the approved changes in the change management business process"
        ],
        "correct": "C",
        "option_explanations": {
            "A) All of the transactions in the database": "Incorrect – This includes financial data, not just configuration changes.",
            "B) All of the requested changes in the change management process": "Incorrect – Some changes may have been made without a request, so this population would be incomplete.",
            "C) All of the changes made to the database": "Correct – The total population is the complete set of configuration changes that occurred in the DBMS.",
            "D) All of the approved changes in the change management business process": "Incorrect – Changes not approved (or bypassing the process) would be missed."
        }
    },
    {
        "id": 36,
        "domain": "Domain 1 – The Audit Process",
        "question": "A credit card payment processor undergoes an annual PCI report on compliance (ROC) audit. What evidence of a passing audit should the payment processor provide to merchant organizations and others?",
        "options": [
            "A) The signed report on compliance (ROC)",
            "B) The signed attestation of compliance (AOC)",
            "C) The signed report of validation (ROV)",
            "D) The signed self-assessment questionnaire (SAQ)"
        ],
        "correct": "B",
        "option_explanations": {
            "A) The signed report on compliance (ROC)": "Incorrect – The full ROC contains detailed internal information that is not appropriate to share; the AOC is sufficient.",
            "B) The signed attestation of compliance (AOC)": "Correct – The AOC provides a summary of the audit result and is the standard document shared with customers to prove compliance.",
            "C) The signed report of validation (ROV)": "Incorrect – An ROV is not the standard document for this purpose.",
            "D) The signed self-assessment questionnaire (SAQ)": "Incorrect – Payment processors undergo annual ROCs, not SAQs; even if they did, the SAQ would not be the standard evidence for external parties."
        }
    },
    {
        "id": 37,
        "domain": "Domain 1 – The Audit Process",
        "question": "Which of the following statements about the ISACA Audit Guidelines is correct?",
        "options": [
            "A) ISACA Audit Guidelines apply only to audit firms and not to internal audit departments.",
            "B) ISACA Audit Guidelines are required. Violations may result in fines for violators.",
            "C) ISACA Audit Guidelines are required. Violations may result in loss of certifications.",
            "D) ISACA Audit Guidelines are not required."
        ],
        "correct": "D",
        "option_explanations": {
            "A) ISACA Audit Guidelines apply only to audit firms and not to internal audit departments.": "Incorrect – Guidelines are applicable to all auditing situations.",
            "B) ISACA Audit Guidelines are required. Violations may result in fines for violators.": "Incorrect – Guidelines are not mandatory; they are suggestions.",
            "C) ISACA Audit Guidelines are required. Violations may result in loss of certifications.": "Incorrect – Only the standards are mandatory; guidelines are optional.",
            "D) ISACA Audit Guidelines are not required.": "Correct – ISACA Audit Guidelines are suggested implementation practices, not mandatory requirements."
        }
    },
    {
        "id": 38,
        "domain": "Domain 1 – The Audit Process",
        "question": "An external auditor is auditing an organization's third-party risk management (TPRM) process. The auditor has observed that the organization has developed an ISO-based questionnaire that is sent to all third-party service providers annually. What value-added remarks can the auditor provide?",
        "options": [
            "A) The process can be more efficient if the organization develops risk-based tiers to save time auditing low-risk vendors.",
            "B) The organization should not be sending questionnaires to vendors every year.",
            "C) The organization should structure its questionnaires based on CSA Star.",
            "D) The organization should outsource its third-party management process."
        ],
        "correct": "A",
        "option_explanations": {
            "A) The process can be more efficient if the organization develops risk-based tiers to save time auditing low-risk vendors.": "Correct – Tiering vendors by risk allows the organization to focus rigorous assessments on high-risk vendors and use lighter assessments for low-risk ones.",
            "B) The organization should not be sending questionnaires to vendors every year.": "Incorrect – Annual questionnaires are appropriate for high-risk vendors.",
            "C) The organization should structure its questionnaires based on CSA Star.": "Incorrect – An ISO-based questionnaire can be sufficient; there's no indication that it must be CSA Star.",
            "D) The organization should outsource its third-party management process.": "Incorrect – There is no evidence suggesting that outsourcing is necessary."
        }
    },
    {
        "id": 39,
        "domain": "Domain 1 – The Audit Process",
        "question": "What is the difference between an SSAE18 Type I audit and an SSA18 Type II audit?",
        "options": [
            "A) A Type I audit is an audit of process effectiveness, whereas a Type II audit is an audit of process effectiveness and process design.",
            "B) A Type I audit is an audit of process design and process effectiveness, whereas a Type II audit is an audit of process design.",
            "C) A Type I audit is an audit of process design, whereas a Type II audit is an audit of process design and process effectiveness.",
            "D) A Type I audit is an audit of process design and effectiveness, whereas a Type II audit is an audit of process effectiveness."
        ],
        "correct": "C",
        "option_explanations": {
            "A) A Type I audit is an audit of process effectiveness, whereas a Type II audit is an audit of process effectiveness and process design.": "Incorrect – This reverses the focus of each type.",
            "B) A Type I audit is an audit of process design and process effectiveness, whereas a Type II audit is an audit of process design.": "Incorrect – Type II also covers effectiveness over a period of time.",
            "C) A Type I audit is an audit of process design, whereas a Type II audit is an audit of process design and process effectiveness.": "Correct – Type I focuses on the suitability of the design at a point in time, while Type II also evaluates the operating effectiveness over a period.",
            "D) A Type I audit is an audit of process design and effectiveness, whereas a Type II audit is an audit of process effectiveness.": "Incorrect – Type I does not test effectiveness over time."
        }
    },
    {
        "id": 40,
        "domain": "Domain 1 – The Audit Process",
        "question": "An auditor is auditing the payment systems for a retail store chain that has 80 stores in the region. The auditor needs to observe and take samples from some of the stores' systems. The audit client has selected two stores that are located in the same city as the store chain headquarters and two stores in a nearby town. How should the audit of the store locations proceed?",
        "options": [
            "A) The auditor should learn more about the stores' systems and practices before deciding what to do.",
            "B) The auditor should audit the selected stores and proceed accordingly.",
            "C) The auditor should accept the sampling but select additional stores.",
            "D) The auditor should select which stores to examine and proceed accordingly."
        ],
        "correct": "A",
        "option_explanations": {
            "A) The auditor should learn more about the stores' systems and practices before deciding what to do.": "Correct – The auditor should first understand if store systems are identical; if so, the client's selection might be acceptable; otherwise, the auditor must independently select the sample.",
            "B) The auditor should audit the selected stores and proceed accordingly.": "Incorrect – Accepting the client's choice without understanding the environment could compromise audit independence.",
            "C) The auditor should accept the sampling but select additional stores.": "Incorrect – There may be impropriety, and simply adding stores doesn't resolve the independence issue.",
            "D) The auditor should select which stores to examine and proceed accordingly.": "Incorrect – Before overriding the client, the auditor should assess whether all stores are identically configured; if they are, the client's selection may be reasonable."
        }
    },
    {
        "id": 41,
        "domain": "Domain 1 – The Audit Process",
        "question": "As a part of an audit of a business process, the auditor has had a discussion with the control owner, as well as the control operators, and has collected procedure documents and records. The auditor is asking internal customers of the business process to describe in their own words how the business process is operated. What kind of evidence collection are these discussions with internal customers?",
        "options": [
            "A) Reconciliation",
            "B) Performance",
            "C) Walkthrough",
            "D) Corroborative inquiry"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Reconciliation": "Incorrect – There is no audit evidence collection technique called reconciliation.",
            "B) Performance": "Incorrect – Performance (or reperformance) is when the auditor independently executes a control procedure.",
            "C) Walkthrough": "Incorrect – A walkthrough is conducted with the control owner or operator, not with internal customers.",
            "D) Corroborative inquiry": "Correct – Discussing the process with additional personnel outside the process itself provides corroboration and strengthens evidence."
        }
    },
    {
        "id": 42,
        "domain": "Domain 1 – The Audit Process",
        "question": "Three months after the completion of an audit, the auditor has contacted the auditee to inquire about the auditee's activities since the audit and whether the auditee has made any progress related to audit findings. What sort of a communication is this outreach from the auditor?",
        "options": [
            "A) The auditor is being a good audit partner and wants to ensure the auditee is successful.",
            "B) The auditor is acting improperly by contacting the auditee outside of an audit and should be censored for unethical behavior.",
            "C) The auditee should assume that the auditor's outreach is personal in nature since this kind of communication is forbidden.",
            "D) The auditor is clearly making sure that the auditee is happy with the auditor's work so that the auditor gets the next year's audit assignment."
        ],
        "correct": "A",
        "option_explanations": {
            "A) The auditor is being a good audit partner and wants to ensure the auditee is successful.": "Correct – It is professional and ethical for an auditor to follow up on audit findings and show concern for the auditee's progress.",
            "B) The auditor is acting improperly by contacting the auditee outside of an audit and should be censored for unethical behavior.": "Incorrect – Such follow-up is not improper; it's often encouraged.",
            "C) The auditee should assume that the auditor's outreach is personal in nature since this kind of communication is forbidden.": "Incorrect – Professional follow-up is allowed and normal.",
            "D) The auditor is clearly making sure that the auditee is happy with the auditor's work so that the auditor gets the next year's audit assignment.": "Incorrect – This speculates a motive; genuine follow-up is standard professional conduct, not necessarily 'fishing for business'."
        }
    },
    {
        "id": 43,
        "domain": "Domain 1 – The Audit Process",
        "question": "According to ISACA Audit Standard 1202, which types of risks should be considered when planning an audit?",
        "options": [
            "A) Fraud risk",
            "B) Business risk",
            "C) Cybersecurity risk",
            "D) Financial risk"
        ],
        "correct": "B",
        "option_explanations": {
            "A) Fraud risk": "Incorrect – Fraud risk is only one type; the standard says all types of risks should be considered.",
            "B) Business risk": "Correct – Business risk encompasses all risk types (including fraud, cybersecurity, financial) that an organization faces, making it the most comprehensive answer.",
            "C) Cybersecurity risk": "Incorrect – Cybersecurity risk is too narrow; the standard requires consideration of all risk types.",
            "D) Financial risk": "Incorrect – Financial risk alone is insufficient; the standard requires a holistic view of risk."
        }
    },
    {
        "id": 44,
        "domain": "Domain 1 – The Audit Process",
        "question": "An IT service desk department that provisions user accounts performs a monthly activity whereby all user account changes that occurred in the prior month are checked against the list of corresponding requests in the ticketing system. This activity is known as:",
        "options": [
            "A) An audit",
            "B) A monthly provisioning review",
            "C) A control threat-assessment (CTA)",
            "D) A risk assessment"
        ],
        "correct": "B",
        "option_explanations": {
            "A) An audit": "Incorrect – An audit is an independent examination; the service desk checking its own work is a review, not an audit.",
            "B) A monthly provisioning review": "Correct – This is a periodic review to ensure that all provisioning was authorized.",
            "C) A control threat-assessment (CTA)": "Incorrect – This activity does not analyze threats.",
            "D) A risk assessment": "Incorrect – This is not a risk assessment; it's a verification of activity."
        }
    },
    {
        "id": 45,
        "domain": "Domain 1 – The Audit Process",
        "question": "An organization with video surveillance at a work center has placed visible notices on building entrances that inform people that video surveillance systems are in use. The notices are an example of:",
        "options": [
            "A) Administrative controls",
            "B) Preventive controls",
            "C) Detective controls",
            "D) Deterrent controls"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Administrative controls": "Incorrect – Administrative controls are policies, standards, etc.; notices are not administrative.",
            "B) Preventive controls": "Incorrect – Notices do not prevent actions; they only warn.",
            "C) Detective controls": "Incorrect – While video surveillance is detective, the notices themselves are not detective but deterrent.",
            "D) Deterrent controls": "Correct – Visible notices announcing surveillance are intended to deter potential wrongdoers."
        }
    },
    {
        "id": 46,
        "domain": "Domain 1 – The Audit Process",
        "question": "An auditor is planning an audit of a financial planning application. Can the auditor rely on a recent penetration test of the application as a risk-based audit?",
        "options": [
            "A) No, because a penetration test does not reveal risks.",
            "B) No, because a penetration test is not a risk assessment.",
            "C) Yes, the auditor can make use of the pen test, but a risk assessment is still needed.",
            "D) Yes, the penetration test serves as a risk assessment in this case."
        ],
        "correct": "C",
        "option_explanations": {
            "A) No, because a penetration test does not reveal risks.": "Incorrect – Penetration tests do reveal some risks, but not a comprehensive view.",
            "B) No, because a penetration test is not a risk assessment.": "Incorrect – While true, the auditor can still use the pen test results as partial input; a risk assessment is still needed though.",
            "C) Yes, the auditor can make use of the pen test, but a risk assessment is still needed.": "Correct – The pen test provides valuable but limited risk information; a full risk assessment is required for a truly risk-based audit.",
            "D) Yes, the penetration test serves as a risk assessment in this case.": "Incorrect – A penetration test alone is never a full risk assessment."
        }
    },
    {
        "id": 47,
        "domain": "Domain 1 – The Audit Process",
        "question": "Which of the following is the best example of a control self-assessment of a user account provisioning process?",
        "options": [
            "A) An examination of Active Directory to ensure that only domain administrators can make user account permission changes",
            "B) Checks to see that only authorized personnel made user account changes",
            "C) Confirmation that all user account changes were approved by appropriate personnel",
            "D) Reconciliation of all user account changes against approved requests in the ticketing system"
        ],
        "correct": "D",
        "option_explanations": {
            "A) An examination of Active Directory to ensure that only domain administrators can make user account permission changes": "Incorrect – This verifies a technical control, not the effectiveness of the provisioning process.",
            "B) Checks to see that only authorized personnel made user account changes": "Incorrect – This confirms who made changes, not that they were properly approved.",
            "C) Confirmation that all user account changes were approved by appropriate personnel": "Incorrect – This checks approvals but not whether the changes themselves were appropriate or authorized.",
            "D) Reconciliation of all user account changes against approved requests in the ticketing system": "Correct – Reconciling actual changes with approved requests is a comprehensive self-assessment that verifies the whole process."
        }
    },
    {
        "id": 48,
        "domain": "Domain 1 – The Audit Process",
        "question": "The proper sequence of an audit of an accounts payable process is:",
        "options": [
            "A) Identify control owners, make evidence requests, perform walkthroughs, do corroborative interviews.",
            "B) Make evidence requests, identify control owners, do corroborative interviews.",
            "C) Identify control owners, do corroborative interviews, make evidence requests, perform walkthroughs.",
            "D) Do corroborative interviews, identify control owners, make evidence requests, and perform walkthroughs."
        ],
        "correct": "A",
        "option_explanations": {
            "A) Identify control owners, make evidence requests, perform walkthroughs, do corroborative interviews.": "Correct – This is the logical sequence: identify who is responsible, request documentation, walk through the process with them, then corroborate with others.",
            "B) Make evidence requests, identify control owners, do corroborative interviews.": "Incorrect – Evidence requests should go to identified control owners, not before.",
            "C) Identify control owners, do corroborative interviews, make evidence requests, perform walkthroughs.": "Incorrect – Corroborative interviews come after walkthroughs.",
            "D) Do corroborative interviews, identify control owners, make evidence requests, and perform walkthroughs.": "Incorrect – The sequence is out of order."
        }
    },
    {
        "id": 49,
        "domain": "Domain 1 – The Audit Process",
        "question": "An auditor is auditing an accounts payable process and has found no exceptions. The auditor has decided to select additional samples to see whether any exceptions may be found. Which type of sampling is the auditor performing?",
        "options": [
            "A) Stop-or-go sampling",
            "B) Discovery sampling",
            "C) Judgmental sampling",
            "D) Exception sampling"
        ],
        "correct": "B",
        "option_explanations": {
            "A) Stop-or-go sampling": "Incorrect – Stop-or-go is used when the auditor believes the risk of exceptions is low and stops early if no exceptions are found; adding more samples is discovery sampling.",
            "B) Discovery sampling": "Correct – Discovery sampling is used when the auditor is looking for at least one exception and continues sampling until one is found.",
            "C) Judgmental sampling": "Incorrect – This is not judgmental; the auditor is extending the sample size based on initial results.",
            "D) Exception sampling": "Incorrect – There is no standard sampling technique called 'exception sampling'."
        }
    },
    {
        "id": 50,
        "domain": "Domain 1 – The Audit Process",
        "question": "Which of the following methods is best suited for an auditee to deliver evidence to an auditor during the audit of a background check process?",
        "options": [
            "A) FTP server",
            "B) Secure file transfer portal",
            "C) E-mail with SMTP over TLS",
            "D) Courier"
        ],
        "correct": "B",
        "option_explanations": {
            "A) FTP server": "Incorrect – FTP is not secure; credentials and data are transmitted in cleartext.",
            "B) Secure file transfer portal": "Correct – A secure portal encrypts data end-to-end and can handle large files, suitable for sensitive background check information.",
            "C) E-mail with SMTP over TLS": "Incorrect – SMTP over TLS only encrypts between mail servers, not end-to-end; also, evidence may be too large for e-mail.",
            "D) Courier": "Incorrect – Using a courier would require printing, which is inefficient and not suitable for electronic analysis."
        }
    },
    {
        "id": 51,
        "domain": "Domain 1 – The Audit Process",
        "question": "An auditor has completed an audit, and the deliverable is ready to give to the audit client. What is the best method for delivering the audit report to the client?",
        "options": [
            "A) Courier",
            "B) Secure file transfer portal",
            "C) E-mail using SMTP over TLS",
            "D) In person, in a close-out meeting"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Courier": "Incorrect – Delivery by courier misses the opportunity for in-person discussion and clarification.",
            "B) Secure file transfer portal": "Incorrect – Electronic delivery lacks face-to-face interaction.",
            "C) E-mail using SMTP over TLS": "Incorrect – Similar to portal, it doesn't provide a personal meeting.",
            "D) In person, in a close-out meeting": "Correct – Face-to-face delivery allows the auditor to explain findings, answer questions, and gauge client reactions through body language."
        }
    },
    {
        "id": 52,
        "domain": "Domain 1 – The Audit Process",
        "question": "What are the potential consequences if an IS auditor is a member of ISACA and is CISA certified and violates the ISACA Code of Professional Ethics?",
        "options": [
            "A) Fines",
            "B) Imprisonment",
            "C) Termination of employment",
            "D) Loss of ISACA certifications"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Fines": "Incorrect – ISACA disciplinary actions do not include fines, though legal fines may apply if laws were also violated.",
            "B) Imprisonment": "Incorrect – ISACA does not have the power to imprison, but legal violations could lead to imprisonment.",
            "C) Termination of employment": "Incorrect – The employer may choose to terminate, but it is not a direct ISACA consequence.",
            "D) Loss of ISACA certifications": "Correct – Violating the Code of Professional Ethics can lead to investigation and loss of CISA certification."
        }
    },
    {
        "id": 53,
        "domain": "Domain 1 – The Audit Process",
        "question": "An auditor is auditing an accounts payable process and has discovered that a single individual has requested and also approved several payments to vendors. What kind of an issue has the auditor found?",
        "options": [
            "A) A separation of duties issue.",
            "B) A split custody issue.",
            "C) A dual custodian issue.",
            "D) No issue has been identified."
        ],
        "correct": "A",
        "option_explanations": {
            "A) A separation of duties issue.": "Correct – Requesting and approving payments should be performed by separate individuals to prevent fraud.",
            "B) A split custody issue.": "Incorrect – Split custody typically refers to splitting knowledge (like passwords), not duties.",
            "C) A dual custodian issue.": "Incorrect – This is not a term used for separation of duties.",
            "D) No issue has been identified.": "Incorrect – This is a clear segregation of duties conflict."
        }
    },
    {
        "id": 54,
        "domain": "Domain 1 – The Audit Process",
        "question": "An organization uses an automated workflow process for request, review, approval, and provisioning of user accounts. Anyone in the organization can request access. Specific persons are assigned to the review and approval steps. Provisioning is automated. What kind of control is the separation of duties between the review and approval steps?",
        "options": [
            "A) Compensating control",
            "B) Manual control",
            "C) Preventive control",
            "D) Administrative control"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Compensating control": "Incorrect – It is not compensating for a missing control; it is a direct control.",
            "B) Manual control": "Incorrect – The workflow is automated, not manual.",
            "C) Preventive control": "Correct – The automated workflow prevents the same person from performing both steps, thus preventing a segregation of duties violation.",
            "D) Administrative control": "Incorrect – The policy requiring separation would be administrative, but the implemented workflow is a preventive technical control."
        }
    },
    {
        "id": 55,
        "domain": "Domain 1 – The Audit Process",
        "question": "An auditor is planning an audit of a monthly terminated users review procedure. The auditor is planning to ask the auditee for a list of current user accounts in Active Directory, as well as a list of current employees and a list of terminated employees from Human Resources, so that the auditor can compare the lists. What kind of an audit is the auditor planning to perform?",
        "options": [
            "A) Reperformance",
            "B) Observation",
            "C) Corroboration",
            "D) Walk-back"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Reperformance": "Correct – The auditor is going to repeat the comparison that the control owner performs, which is a reperformance audit.",
            "B) Observation": "Incorrect – Observation would be watching someone else do the review, not doing it themselves.",
            "C) Corroboration": "Incorrect – Corroboration involves interviewing additional parties to confirm evidence, not reperforming the control.",
            "D) Walk-back": "Incorrect – 'Walk-back' is not a standard audit type."
        }
    },
    {
        "id": 56,
        "domain": "Domain 1 – The Audit Process",
        "question": "An IT service desk manager is the control owner for the IT department change control process. In an audit of the change control process, the auditor has asked the IT service desk manager to provide all change control tickets whose request numbers end with the digit '6.' What sampling methodology has the auditor used?",
        "options": [
            "A) Judgmental sampling",
            "B) Statistical sampling",
            "C) Stratified sampling",
            "D) Stop-or-go sampling"
        ],
        "correct": "B",
        "option_explanations": {
            "A) Judgmental sampling": "Incorrect – This is not based on professional judgement; it's a random sample using a numeric pattern.",
            "B) Statistical sampling": "Correct – Requesting tickets ending in '6' is an example of systematic random sampling, a type of statistical sampling.",
            "C) Stratified sampling": "Incorrect – Stratified sampling would divide the population into groups (strata) before sampling.",
            "D) Stop-or-go sampling": "Incorrect – Stop-or-go involves stopping early if no exceptions are found, which is not described here."
        }
    },
    {
        "id": 57,
        "domain": "Domain 1 – The Audit Process",
        "question": "An audit firm is planning an audit of an organization's asset management records. For what reason would the auditor request a copy of the entire asset database from the DBA versus a report of assets from the owner of the asset process?",
        "options": [
            "A) Honesty of the evidence provider",
            "B) Objectivity of the evidence provider",
            "C) Independence of the evidence provider",
            "D) Qualification of the evidence provider"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Honesty of the evidence provider": "Incorrect – The auditor is not questioning the honesty of the process owner.",
            "B) Objectivity of the evidence provider": "Incorrect – Objectivity is related but independence is the primary reason.",
            "C) Independence of the evidence provider": "Correct – The DBA is independent from the asset process owner and has no vested interest in the audit outcome, so the evidence is more reliable.",
            "D) Qualification of the evidence provider": "Incorrect – Both the DBA and process owner are qualified; independence is the key factor."
        }
    },
    {
        "id": 58,
        "domain": "Domain 1 – The Audit Process",
        "question": "An auditor has delivered a Sarbanes-Oxley audit report containing 12 exceptions to the audit client, who disagrees with the findings. The audit client is upset and is asking the auditor to remove any six findings from the report. A review of the audit findings resulted in the confirmation that all 12 findings are valid. How should the auditor proceed?",
        "options": [
            "A) Remove the three lowest-risk findings from the report.",
            "B) Remote the six lowest-risk findings from the report.",
            "C) Report the auditee to the Securities and Exchange Commission.",
            "D) Explain to the auditee that the audit report cannot be changed."
        ],
        "correct": "D",
        "option_explanations": {
            "A) Remove the three lowest-risk findings from the report.": "Incorrect – The auditor cannot compromise the integrity of the report.",
            "B) Remote the six lowest-risk findings from the report.": "Incorrect – This would be unethical.",
            "C) Report the auditee to the Securities and Exchange Commission.": "Incorrect – This situation does not warrant reporting to the SEC; the auditor should stand by the report.",
            "D) Explain to the auditee that the audit report cannot be changed.": "Correct – The auditor must uphold the truthfulness of the report and refuse to alter it."
        }
    },
    {
        "id": 59,
        "domain": "Domain 1 – The Audit Process",
        "question": "An auditor has delivered a Sarbanes-Oxley audit report containing 12 exceptions to the audit client, who disagrees with the findings. The audit client is upset and is asking the auditor to remove any six findings from the report in exchange for a payment of $25,000. A review of the audit findings resulted in the confirmation that all 12 findings are valid. How should the auditor proceed?",
        "options": [
            "A) The auditor should report the matter to his or her manager.",
            "B) The auditor should reject the payment and meet the auditee halfway by removing three of the findings.",
            "C) The auditor should reject the payment and remove six of the findings.",
            "D) The auditor should report the incident to the audit client's audit committee."
        ],
        "correct": "A",
        "option_explanations": {
            "A) The auditor should report the matter to his or her manager.": "Correct – The auditor should first escalate to their manager, who will handle the situation, likely by notifying the audit committee or regulatory authorities.",
            "B) The auditor should reject the payment and meet the auditee halfway by removing three of the findings.": "Incorrect – Any compromise is unethical.",
            "C) The auditor should reject the payment and remove six of the findings.": "Incorrect – Same ethical violation.",
            "D) The auditor should report the incident to the audit client's audit committee.": "Incorrect – While eventually appropriate, the first step is to inform the manager."
        }
    },
    {
        "id": 60,
        "domain": "Domain 1 – The Audit Process",
        "question": "An auditor is auditing a change control process. During a walkthrough, the control owner described the process as follows: 'Engineers plan their changes and send an e-mail about their changes to the IT manager before 5 p.m. on Wednesday. The engineers then proceed with their changes during the change window on Friday evening.' What, if any, findings should the auditor identify?",
        "options": [
            "A) The change control process is fine as is, but could be improved by creating a ledger of changes.",
            "B) The change control process is fine as is.",
            "C) The change control process lacks a review step.",
            "D) The change control process lacks review and approval steps."
        ],
        "correct": "D",
        "option_explanations": {
            "A) The change control process is fine as is, but could be improved by creating a ledger of changes.": "Incorrect – The process is missing a critical step.",
            "B) The change control process is fine as is.": "Incorrect – It lacks an approval mechanism.",
            "C) The change control process lacks a review step.": "Incorrect – While true, the more important finding is the lack of an approval step.",
            "D) The change control process lacks review and approval steps.": "Correct – The process as described only involves engineers sending an email; there is no indication of review or formal approval before changes are made."
        }
    },
    {
        "id": 61,
        "domain": "Domain 1 – The Audit Process",
        "question": "An organization utilizes a video surveillance system on all ingress and egress points in its work facility; surveillance cameras are concealed from view, and there are no visible notices. What type of control is this?",
        "options": [
            "A) Administrative control",
            "B) Secret control",
            "C) Detective control",
            "D) Deterrent control"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Administrative control": "Incorrect – This is a technical control, not administrative.",
            "B) Secret control": "Incorrect – Controls are not classified as 'secret'.",
            "C) Detective control": "Correct – Concealed cameras record events after they occur, making them detective controls; they are not deterrent because they are not visible.",
            "D) Deterrent control": "Incorrect – Deterrent controls rely on visibility to discourage actions; hidden cameras do not serve as deterrents."
        }
    },
    {
        "id": 62,
        "domain": "Domain 1 – The Audit Process",
        "question": "An auditor is selecting samples from records in the user access request process. While privileged access requests account for approximately 5 percent of all access requests, the auditor wants 20 percent of the samples to be requests for administrative access. What sampling technique has the auditor selected?",
        "options": [
            "A) Judgmental sampling",
            "B) Stratified sampling",
            "C) Statistical sampling",
            "D) Variable sampling"
        ],
        "correct": "B",
        "option_explanations": {
            "A) Judgmental sampling": "Incorrect – The auditor is not examining individual items to judge inclusion; they are deliberately over-sampling a specific class.",
            "B) Stratified sampling": "Correct – The auditor has identified a stratum (privileged access) and is intentionally selecting a higher proportion from that stratum to ensure sufficient coverage.",
            "C) Statistical sampling": "Incorrect – Statistical sampling would result in about 5% privileged items, not the deliberate 20%.",
            "D) Variable sampling": "Incorrect – Variable sampling is used to estimate population characteristics, not to skew sample composition."
        }
    },
    {
        "id": 63,
        "domain": "Domain 1 – The Audit Process",
        "question": "An auditor is auditing a change control process by examining change logs in a database management system and requesting change control records to show that those changes were approved. The auditor plans to proceed until the first exception is found. What sampling technique is being used here?",
        "options": [
            "A) Discovery sampling",
            "B) Stop-or-go sampling",
            "C) Attribute sampling",
            "D) Exception sampling"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Discovery sampling": "Correct – Discovery sampling continues until an exception is found, used when the auditor is looking for the existence of any exception.",
            "B) Stop-or-go sampling": "Incorrect – Stop-or-go sampling stops when the auditor determines the risk is low enough, not necessarily upon the first exception.",
            "C) Attribute sampling": "Incorrect – Attribute sampling estimates the rate of occurrence, not the existence of the first error.",
            "D) Exception sampling": "Incorrect – This is not a recognized sampling technique."
        }
    },
    # Domain 2 – IT Governance and Management
    {
        "id": 1,
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
            "A) Information technology policies": "Incorrect – Although information technology policies are an essential part of an information technology program, they do not by themselves control IT processes.",
            "B) Information technology policies along with audits of those policies": "Incorrect – IT policies and activities (such as audits) to measure their effectiveness are only one component of management's observation and control of an organization.",
            "C) Information technology governance": "Correct – ISACA defines governance as a set of processes that ensures stakeholder needs are evaluated to determine balanced, agreed-on enterprise objectives to be achieved; setting direction through prioritization and decision making; and monitoring performance and compliance against agreed-on direction and objectives.",
            "D) Metrics as compared to similar organizations": "Incorrect – The comparison of metrics to other organizations is not a significant part of a governance program. Indeed, many organizations forego benchmarking entirely."
        }
    },
    {
        "id": 2,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "What is the best method for ensuring that an organization's IT department achieves adequate business alignment?",
        "options": [
            "A) Find and read the organization's articles of incorporation.",
            "B) Understand the organization's vision, mission statement, and objectives.",
            "C) Determine who the CIO reports to in the organization.",
            "D) Study the organization's application portfolio."
        ],
        "correct": "B",
        "option_explanations": {
            "A) Find and read the organization's articles of incorporation.": "Incorrect – An organization's articles of incorporation do not provide sufficient information about an organization's mission or objectives.",
            "B) Understand the organization's vision, mission statement, and objectives.": "Correct – The best way to align an IT department to the business is to understand the organization's vision, mission, goals, and objectives.",
            "C) Determine who the CIO reports to in the organization.": "Incorrect – The org chart reveals little about what the organization wants to accomplish.",
            "D) Study the organization's application portfolio.": "Incorrect – The organization's application portfolio reveals little or nothing about the strategic objectives and will provide little or no aid in aligning the program to the business."
        }
    },
    {
        "id": 3,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "Roberta has located her organization's mission statement and a list of strategic objectives. What steps should Roberta take to ensure that the IT department aligns with the business?",
        "options": [
            "A) Discuss strategic objectives with business leaders to better understand what they wish to accomplish and what steps are being taken to achieve them.",
            "B) Develop a list of activities that will support the organization's strategic objectives, and determine the cost of each.",
            "C) Select those controls from the organization's control framework that align to each objective, and then ensure that those controls are effective.",
            "D) Select the policies from the organization's information security policy that are relevant to each objective, and ensure that those policies are current."
        ],
        "correct": "A",
        "option_explanations": {
            "A) Discuss strategic objectives with business leaders to better understand what they wish to accomplish and what steps are being taken to achieve them.": "Correct – The best first step is to better understand the objectives through dialogue with business leaders.",
            "B) Develop a list of activities that will support the organization's strategic objectives, and determine the cost of each.": "Incorrect – Without a dialogue with business leaders, simply identifying supporting activities is more likely to miss important details.",
            "C) Select those controls from the organization's control framework that align to each objective, and then ensure that those controls are effective.": "Incorrect – Proper alignment does not generally begin with the selection or implementation of controls.",
            "D) Select the policies from the organization's information security policy that are relevant to each objective, and ensure that those policies are current.": "Incorrect – Alignment does not generally involve identifying relevant security policies; this is a minor, supporting activity."
        }
    },
    {
        "id": 4,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "Michael wants to improve the risk management process in his organization by creating content that will help management understand when certain risks should be accepted and when certain risks should be mitigated. The policy that Michael needs to create is known as:",
        "options": [
            "A) A security policy",
            "B) A control framework",
            "C) A risk appetite statement",
            "D) A control testing procedure"
        ],
        "correct": "C",
        "option_explanations": {
            "A) A security policy": "Incorrect – Security policy is not a primary means for making risk treatment decisions.",
            "B) A control framework": "Incorrect – An organization's control framework is not typically used for making risk treatment decisions.",
            "C) A risk appetite statement": "Correct – A risk appetite statement provides guidance on the types of risk and the amount of risk an organization may be willing to accept versus what it prefers to mitigate, avoid, or transfer.",
            "D) A control testing procedure": "Incorrect – Control testing procedures are not related to risk treatment decisions."
        }
    },
    {
        "id": 5,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "In a typical risk management process, the best person(s) to make a risk treatment decision is:",
        "options": [
            "A) The chief risk officer (CRO)",
            "B) The chief information officer (CIO)",
            "C) The department head associated with the risk",
            "D) The chief information security officer (CISO)"
        ],
        "correct": "C",
        "option_explanations": {
            "A) The chief risk officer (CRO)": "Incorrect – The CRO should not make business function risk decisions on behalf of department heads; at best, the CRO should facilitate discussions.",
            "B) The chief information officer (CIO)": "Incorrect – The CIO should not be making business function risk decisions on behalf of department heads.",
            "C) The department head associated with the risk": "Correct – The department head responsible for the business activity should make the risk treatment decision because it is a business decision.",
            "D) The chief information security officer (CISO)": "Incorrect – The CISO should facilitate discussions, not be the final decision maker."
        }
    },
    {
        "id": 6,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "The ultimate responsibility for an organization's cybersecurity program lies with:",
        "options": [
            "A) The board of directors",
            "B) The chief executive officer (CEO)",
            "C) The chief information officer (CIO)",
            "D) The chief information security officer (CISO)"
        ],
        "correct": "A",
        "option_explanations": {
            "A) The board of directors": "Correct – The board of directors holds ultimate responsibility for everything in the organization, including the cybersecurity program.",
            "B) The chief executive officer (CEO)": "Incorrect – While the CEO runs the organization, ultimate responsibility lies with the board.",
            "C) The chief information officer (CIO)": "Incorrect – The board of directors is the party responsible for cybersecurity.",
            "D) The chief information security officer (CISO)": "Incorrect – The CISO's role is one of facilitation; the board is ultimately responsible."
        }
    },
    {
        "id": 7,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "In a U.S. public company, a CIO will generally report the state of the organization's IT function to:",
        "options": [
            "A) The Tradeway Commission",
            "B) Independent auditors",
            "C) The U.S. Securities and Exchange Commission",
            "D) The board of directors"
        ],
        "correct": "D",
        "option_explanations": {
            "A) The Tradeway Commission": "Incorrect – An organization would not report anything to the Tradeway Commission.",
            "B) Independent auditors": "Incorrect – The CIO would typically not report the state of IT to independent auditors, though they may meet periodically.",
            "C) The U.S. Securities and Exchange Commission": "Incorrect – The CIO does not report to the SEC; financial filings may include IT only if a material incident occurred.",
            "D) The board of directors": "Correct – In most U.S. publicly traded companies, the CIO reports the state of the IT function to the board of directors."
        }
    },
    {
        "id": 8,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "A new CIO in an organization is building its formal IT department from the ground up. In order to ensure collaboration among business leaders and department heads in the organization, the CIO should form and manage:",
        "options": [
            "A) A technology committee of the board of directors",
            "B) An IT steering committee",
            "C) An audit committee of the board of directors",
            "D) A business-aligned IT policy"
        ],
        "correct": "B",
        "option_explanations": {
            "A) A technology committee of the board of directors": "Incorrect – The CIO will not be involved in forming or managing a board technology committee.",
            "B) An IT steering committee": "Correct – An IT steering committee, consisting of senior executives and department heads, can discuss organization-wide IT issues and make strategic decisions.",
            "C) An audit committee of the board of directors": "Incorrect – The CIO would not form or manage a board audit committee.",
            "D) A business-aligned IT policy": "Incorrect – A business-aligned IT policy, while important, would not significantly foster collaboration among business leaders."
        }
    },
    {
        "id": 9,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "The best person or group to make risk treatment decisions is:",
        "options": [
            "A) The chief information security officer (CISO)",
            "B) The audit committee of the board of directors",
            "C) The cybersecurity steering committee",
            "D) External auditors"
        ],
        "correct": "C",
        "option_explanations": {
            "A) The chief information security officer (CISO)": "Incorrect – The CISO unilaterally making decisions may result in less buy-in from business leaders.",
            "B) The audit committee of the board of directors": "Incorrect – Audit committee members rarely get involved in risk treatment decision making.",
            "C) The cybersecurity steering committee": "Correct – A committee of senior executives and business unit leaders can openly discuss, collaborate, and decide on risk treatment issues.",
            "D) External auditors": "Incorrect – External auditors should not be making decisions on behalf of the organizations they audit."
        }
    },
    {
        "id": 10,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "Which is the best party to conduct access reviews?",
        "options": [
            "A) Users' managers",
            "B) Information security manager",
            "C) IT service desk",
            "D) Department head"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Users' managers": "Incorrect – Managers of users are not the best parties to review access; they may not know the business needs thoroughly.",
            "B) Information security manager": "Incorrect – Information security managers have insufficient knowledge about business operations and the persons using them.",
            "C) IT service desk": "Incorrect – IT service desk personnel have insufficient business knowledge and may be the ones carrying out access changes, creating a conflict of interest.",
            "D) Department head": "Correct – The persons responsible for business activities should review users' access to applications supporting their business processes."
        }
    },
    {
        "id": 11,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "Which is the best party to make decisions about the configuration and function of business applications?",
        "options": [
            "A) Business department head",
            "B) IT business analyst",
            "C) Application developer",
            "D) End user"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Business department head": "Correct – Business department heads are best suited to determine the behavior of business applications supporting their processes.",
            "B) IT business analyst": "Incorrect – IT business analysts are not responsible for business unit operation decisions, though they may facilitate discussions.",
            "C) Application developer": "Incorrect – Application developers are not responsible for business unit operation decisions, though they may provide insight.",
            "D) End user": "Incorrect – End users are generally not responsible for decisions about business unit operations."
        }
    },
    {
        "id": 12,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "Which of the following is the best definition of custodial responsibility?",
        "options": [
            "A) The custodian protects assets based on the customer's defined interests.",
            "B) The custodian protects assets based on its own defined interests.",
            "C) The custodian makes decisions based on its own defined interests.",
            "D) The custodian makes decisions based on the customer's defined interests."
        ],
        "correct": "D",
        "option_explanations": {
            "A) The custodian protects assets based on the customer's defined interests.": "Incorrect – Protection of an asset is only a part of the custodian's scope of responsibility; decisions are broader.",
            "B) The custodian protects assets based on its own defined interests.": "Incorrect – A custodian does not protect assets based on its own interests, but on its customers' interests.",
            "C) The custodian makes decisions based on its own defined interests.": "Incorrect – A custodian does not make decisions based on its own interests, but on its customers' interests.",
            "D) The custodian makes decisions based on the customer's defined interests.": "Correct – A custodian is charged with a wide range of decisions regarding the care of an asset, based upon the customer's defined interests."
        }
    },
    {
        "id": 13,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "What is the primary risk of IT acting as custodian for a business owner?",
        "options": [
            "A) IT may not have enough interest to provide quality care for business applications.",
            "B) IT may not have sufficient staffing to properly care for business applications.",
            "C) IT may have insufficient knowledge of business operations to make good decisions.",
            "D) Business departments might not give IT sufficient access to properly manage applications."
        ],
        "correct": "C",
        "option_explanations": {
            "A) IT may not have enough interest to provide quality care for business applications.": "Incorrect – Level of interest is not a compelling factor.",
            "B) IT may not have sufficient staffing to properly care for business applications.": "Incorrect – Sufficient staffing is not a compelling factor.",
            "C) IT may have insufficient knowledge of business operations to make good decisions.": "Correct – IT personnel tend to focus on technology and may not fully understand business operations, leading to poor decisions.",
            "D) Business departments might not give IT sufficient access to properly manage applications.": "Incorrect – Business units are not generally in a position to restrict IT from administrative access."
        }
    },
    {
        "id": 14,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "An organization needs to hire an executive who will build a management program that considers threats and vulnerabilities. The best job title for this position is:",
        "options": [
            "A) CSO",
            "B) CRO",
            "C) CISO",
            "D) CIRO"
        ],
        "correct": "B",
        "option_explanations": {
            "A) CSO": "Incorrect – The Chief Security Officer is not necessarily responsible for risk management; the role focuses on protective controls.",
            "B) CRO": "Correct – The Chief Risk Officer manages risk for multiple asset types, including information, physical, and financial risks.",
            "C) CISO": "Incorrect – The CISO is typically responsible for protecting only information assets, not multiple types of assets.",
            "D) CIRO": "Incorrect – The CIRO is responsible for information asset risk management, not other asset types."
        }
    },
    {
        "id": 15,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "An organization needs to hire an executive who will be responsible for ensuring that the organization's policies, business processes, and information systems are compliant with laws and regulations concerning the proper collection, use, and protection of personally identifiable information. What is the best job title for the organization to use for this position?",
        "options": [
            "A) CSO",
            "B) CIRO",
            "C) CISO",
            "D) CPO"
        ],
        "correct": "D",
        "option_explanations": {
            "A) CSO": "Incorrect – The CSO is typically not responsible for privacy-related activities.",
            "B) CIRO": "Incorrect – The CIRO is typically not responsible for privacy-related activities.",
            "C) CISO": "Incorrect – The CISO is typically not responsible for privacy-related activities.",
            "D) CPO": "Correct – The Chief Privacy Officer ensures the proper collection, use, and protection of personally identifiable information (PII)."
        }
    },
    {
        "id": 16,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "The Big Data Company is adjusting several position titles in its IT department to reflect industry standards. Included in the consideration are two individuals: The first is responsible for the overall relationships and data flows among the company's internal and external information systems. The second is responsible for the overall health and management of systems containing information. Which two job titles are most appropriate for these two roles?",
        "options": [
            "A) Systems architect and database administrator",
            "B) Data architect and data scientist",
            "C) Data scientist and database administrator",
            "D) Data architect and database administrator"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Systems architect and database administrator": "Incorrect – Systems architect is not the best title for data flows and relationships.",
            "B) Data architect and data scientist": "Incorrect – Data scientist is not the best title for managing systems containing information.",
            "C) Data scientist and database administrator": "Incorrect – Data scientist is not the best title for the first role.",
            "D) Data architect and database administrator": "Correct – Data architect handles overall relationships and data flows; database administrator manages database systems."
        }
    },
    {
        "id": 17,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "What is the primary distinction between a network engineer and a telecom engineer?",
        "options": [
            "A) A network engineer is primarily involved with networks and internal network media, whereas a telecom engineer is primarily involved with networks and external (carrier) network media.",
            "B) A network engineer is primarily involved with networks and external (carrier) network media, whereas a telecom engineer is primarily involved with networks and internal network media.",
            "C) A network engineer is primarily involved with layer 3 protocols and above, whereas a telecom engineer is primarily involved with layer 1 and layer 2 protocols.",
            "D) There is no distinction, as both are involved in all aspects of an organization's networks."
        ],
        "correct": "A",
        "option_explanations": {
            "A) A network engineer is primarily involved with networks and internal network media, whereas a telecom engineer is primarily involved with networks and external (carrier) network media.": "Correct – Network engineers focus on internal networks (cabling, Wi‑Fi); telecom engineers focus on external carrier networks (MPLS, Frame Relay, dark fiber).",
            "B) A network engineer is primarily involved with networks and external (carrier) network media, whereas a telecom engineer is primarily involved with networks and internal network media.": "Incorrect – The definitions are swapped.",
            "C) A network engineer is primarily involved with layer 3 protocols and above, whereas a telecom engineer is primarily involved with layer 1 and layer 2 protocols.": "Incorrect – The distinction is not strictly by protocol layer.",
            "D) There is no distinction, as both are involved in all aspects of an organization's networks.": "Incorrect – There is a clear distinction in practice."
        }
    },
    {
        "id": 18,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "An organization that is a U.S. public company is redesigning its access management and access review controls. What is the best role for Internal Audit in this redesign effort?",
        "options": [
            "A) Develop procedures.",
            "B) Design controls.",
            "C) Provide feedback on control design.",
            "D) Develop controls and procedures."
        ],
        "correct": "C",
        "option_explanations": {
            "A) Develop procedures.": "Incorrect – Internal Audit should not develop procedures it may later audit.",
            "B) Design controls.": "Incorrect – Internal Audit should not design controls it may later audit.",
            "C) Provide feedback on control design.": "Correct – Internal Audit may opine on the design of controls for suitability and auditability without taking a design role.",
            "D) Develop controls and procedures.": "Incorrect – Internal Audit should not be in a position to audit its own work."
        }
    },
    {
        "id": 19,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "A security operations manager is proposing that engineers who design and manage information systems play a role in the monitoring of those systems. Is design and management compatible with monitoring? Why or why not?",
        "options": [
            "A) No. Personnel who design and manage systems should not perform a monitoring role, as this is a conflict of interest.",
            "B) Yes. Personnel who design and manage systems will be more familiar with the steps to take, as well as the reasons to take them, when alerts are generated.",
            "C) No. Personnel who design and manage systems will not be familiar with response procedures when alerts are generated.",
            "D) No. Personnel who design and manage systems are not permitted access to production environments and should not perform monitoring."
        ],
        "correct": "B",
        "option_explanations": {
            "A) No. Personnel who design and manage systems should not perform a monitoring role, as this is a conflict of interest.": "Incorrect – There is normally no conflict of interest between design, management, and monitoring.",
            "B) Yes. Personnel who design and manage systems will be more familiar with the steps to take, as well as the reasons to take them, when alerts are generated.": "Correct – System designers and managers understand the system deeply, making them effective at monitoring and response.",
            "C) No. Personnel who design and manage systems will not be familiar with response procedures when alerts are generated.": "Incorrect – They are likely more familiar because they understand how the systems work.",
            "D) No. Personnel who design and manage systems are not permitted access to production environments and should not perform monitoring.": "Incorrect – Management personnel typically have access to production environments."
        }
    },
    {
        "id": 20,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "The purpose of metrics in an IT department is to:",
        "options": [
            "A) Measure the performance and effectiveness of controls.",
            "B) Measure the likelihood of an attack on the organization.",
            "C) Predict the likelihood of an attack on an organization.",
            "D) Predict the next IT service outage."
        ],
        "correct": "A",
        "option_explanations": {
            "A) Measure the performance and effectiveness of controls.": "Correct – Metrics are used to understand how well security controls are performing.",
            "B) Measure the likelihood of an attack on the organization.": "Incorrect – Metrics do not necessarily foretell an attack.",
            "C) Predict the likelihood of an attack on an organization.": "Incorrect – Metrics are not always used to predict attacks.",
            "D) Predict the next IT service outage.": "Incorrect – Metrics do not necessarily foretell future outages."
        }
    },
    {
        "id": 21,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "Which security metric is best considered a leading indicator of an attack?",
        "options": [
            "A) Number of firewall rules triggered",
            "B) Number of security awareness training sessions completed",
            "C) Percentage of systems scanned",
            "D) Mean time to apply security patches"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Number of firewall rules triggered": "Incorrect – This may signal unwanted network activity but is not strongly correlated with attack likelihood.",
            "B) Number of security awareness training sessions completed": "Incorrect – While helpful, patch levels are usually more accurate indicators.",
            "C) Percentage of systems scanned": "Incorrect – This reflects the scanning process, not directly the vulnerability to attacks.",
            "D) Mean time to apply security patches": "Correct – A long mean time to patch indicates higher exposure; patching quickly reduces the likelihood of successful attacks."
        }
    },
    {
        "id": 22,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "Steve, a CISO, has vulnerability management metrics and needs to build business-level metrics. Which of the following is the best business-level, leading indicator metric suitable for his organization's board of directors?",
        "options": [
            "A) Average time to patch servers supporting manufacturing processes",
            "B) Frequency of security scans of servers supporting manufacturing processes",
            "C) Percentage of servers supporting manufacturing processes that are scanned by vulnerability scanning tools",
            "D) Number of vulnerabilities remediated on servers supporting manufacturing processes"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Average time to patch servers supporting manufacturing processes": "Correct – This leading indicator shows the average time critical servers are exposed to new threats.",
            "B) Frequency of security scans of servers supporting manufacturing processes": "Incorrect – Number of scans provides no information about actual vulnerabilities or risk.",
            "C) Percentage of servers supporting manufacturing processes that are scanned by vulnerability scanning tools": "Incorrect – Percentage scanned is a good operational metric but does not indicate risk reduction.",
            "D) Number of vulnerabilities remediated on servers supporting manufacturing processes": "Incorrect – A raw number without context tells board members little."
        }
    },
    {
        "id": 23,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "The metric 'percentage of systems with completed installation of advanced anti-malware' is best described as:",
        "options": [
            "A) A key operational indicator (KOI)",
            "B) A key performance indicator (KPI)",
            "C) A key goal indicator (KGI)",
            "D) A key risk indicator (KRI)"
        ],
        "correct": "C",
        "option_explanations": {
            "A) A key operational indicator (KOI)": "Incorrect – 'Key operational indicator' is not an industry standard term; the metric is more goal-oriented.",
            "B) A key performance indicator (KPI)": "Incorrect – Completion of installations is not typically a performance metric.",
            "C) A key goal indicator (KGI)": "Correct – This metric is associated with a strategic goal (completing the anti-malware rollout).",
            "D) A key risk indicator (KRI)": "Incorrect – Although it may indicate risk reduction, it is better classified as a KGI."
        }
    },
    {
        "id": 24,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "A member of the board of directors has asked Ravila, a CIRO, to produce a metric showing the reduction of risk as a result of the organization making key improvements to its security information and event management system. Which type of metric is most suitable for this purpose?",
        "options": [
            "A) KGI",
            "B) RACI",
            "C) KRI",
            "D) ROSI"
        ],
        "correct": "C",
        "option_explanations": {
            "A) KGI": "Incorrect – A key goal indicator is not the best indicator of risk.",
            "B) RACI": "Incorrect – RACI is a roles and responsibilities matrix, not a metric.",
            "C) KRI": "Correct – A key risk indicator is most suitable for showing risk reduction, though high‑impact events occur rarely.",
            "D) ROSI": "Incorrect – Return on security investment is not suitable because significant events are rare."
        }
    },
    {
        "id": 25,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "A common way to determine the effectiveness of IT metrics is the SMART method. SMART stands for:",
        "options": [
            "A) Security Metrics Are Risk Treatment",
            "B) Specific, Measurable, Attainable, Relevant, Timely",
            "C) Specific, Measurable, Actionable, Relevant, Timely",
            "D) Specific, Manageable, Actionable, Relevant, Timely"
        ],
        "correct": "B",
        "option_explanations": {
            "A) Security Metrics Are Risk Treatment": "Incorrect – This is not the definition of SMART.",
            "B) Specific, Measurable, Attainable, Relevant, Timely": "Correct – SMART stands for Specific, Measurable, Attainable, Relevant, and Timely.",
            "C) Specific, Measurable, Actionable, Relevant, Timely": "Incorrect – 'Actionable' is not the standard term; it is 'Attainable'.",
            "D) Specific, Manageable, Actionable, Relevant, Timely": "Incorrect – Neither 'Manageable' nor 'Actionable' are standard."
        }
    },
    {
        "id": 26,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "The statement 'Complete migration of flagship system to latest version of vendor-supplied software' is an example of:",
        "options": [
            "A) A mission statement",
            "B) A vision statement",
            "C) A purpose statement",
            "D) An objective statement"
        ],
        "correct": "D",
        "option_explanations": {
            "A) A mission statement": "Incorrect – The statement is too specific to be a mission statement.",
            "B) A vision statement": "Incorrect – The statement is not typical of a vision statement.",
            "C) A purpose statement": "Incorrect – The statement is not typical of a purpose statement.",
            "D) An objective statement": "Correct – This is a statement of a strategic objective."
        }
    },
    {
        "id": 27,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "Ernie, a CIO who manages a large IT team, wants to create a mission statement for the team. What is the best approach for creating this mission statement?",
        "options": [
            "A) Start with the organization's mission statement.",
            "B) Start with Ernie's most recent performance review.",
            "C) Start with the results of the most recent risk assessment.",
            "D) Start with the body of open items in the project portfolio."
        ],
        "correct": "A",
        "option_explanations": {
            "A) Start with the organization's mission statement.": "Correct – Aligning the IT department's mission with the overall organization's mission ensures business alignment.",
            "B) Start with Ernie's most recent performance review.": "Incorrect – A performance review may be aligned but is not the best primary source.",
            "C) Start with the results of the most recent risk assessment.": "Incorrect – A risk assessment does not provide sufficient information about the organization's purpose.",
            "D) Start with the body of open items in the project portfolio.": "Incorrect – Open project items reflect short‑term work, not the department's overall mission."
        }
    },
    {
        "id": 28,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "Which of the following statements is the best description for the purpose of performing risk management?",
        "options": [
            "A) Identify and manage vulnerabilities that may permit security events to occur.",
            "B) Identify and manage threats that are relevant to the organization.",
            "C) Assess the risks associated with third-party service providers.",
            "D) Assess and manage risks associated with doing business online."
        ],
        "correct": "B",
        "option_explanations": {
            "A) Identify and manage vulnerabilities that may permit security events to occur.": "Incorrect – Vulnerability management is only one facet of risk management.",
            "B) Identify and manage threats that are relevant to the organization.": "Correct – The purpose of risk management is to identify and manage threats that could harm the organization.",
            "C) Assess the risks associated with third-party service providers.": "Incorrect – Risk management encompasses the entire organization, not just third parties.",
            "D) Assess and manage risks associated with doing business online.": "Incorrect – The scope is far broader than just online business."
        }
    },
    {
        "id": 29,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "Key metrics showing the effectiveness of a risk management program would not include:",
        "options": [
            "A) Reduction in the number of security events",
            "B) Reduction in the impact of security events",
            "C) Reduction in the time to remediate vulnerabilities",
            "D) Reduction in the number of patches applied"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Reduction in the number of security events": "Incorrect – This is a potentially useful metric.",
            "B) Reduction in the impact of security events": "Incorrect – This is a potentially useful metric.",
            "C) Reduction in the time to remediate vulnerabilities": "Incorrect – This is a potentially useful metric.",
            "D) Reduction in the number of patches applied": "Correct – The number of patches applied does not indicate risk management program effectiveness."
        }
    },
    {
        "id": 30,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "Examples of security program performance metrics include all of the following except:",
        "options": [
            "A) Time to detect security incidents",
            "B) Time to remediate security incidents",
            "C) Time to perform security scans",
            "D) Time to discover vulnerabilities"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Time to detect security incidents": "Incorrect – This is a good performance metric.",
            "B) Time to remediate security incidents": "Incorrect – This is a good performance metric.",
            "C) Time to perform security scans": "Correct – The time required to perform scans is not a good security program performance metric.",
            "D) Time to discover vulnerabilities": "Incorrect – This is a good performance metric."
        }
    },
    {
        "id": 31,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "Two similar-sized organizations are merging. Paul will be the CIO of the new, combined organization. What is the greatest risk that may occur as a result of the merger?",
        "options": [
            "A) Differences in practices that may not be understood",
            "B) Duplication of effort",
            "C) Gaps in coverage of key processes",
            "D) Higher tooling costs"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Differences in practices that may not be understood": "Correct – Merging different practices can introduce unforeseen risks.",
            "B) Duplication of effort": "Incorrect – Duplication is not the greatest risk; it can be addressed.",
            "C) Gaps in coverage of key processes": "Incorrect – While a risk, it is not the greatest compared to unfamiliar practices.",
            "D) Higher tooling costs": "Incorrect – Higher costs are a short-term spending matter, not the greatest risk."
        }
    },
    {
        "id": 32,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "The purpose of value delivery metrics is:",
        "options": [
            "A) Long-term reduction in costs",
            "B) Reduction in ROSI",
            "C) Increase in ROSI",
            "D) Increase in net profit"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Long-term reduction in costs": "Correct – Value delivery metrics are most often associated with long-term cost reduction in proportion to other measures.",
            "B) Reduction in ROSI": "Incorrect – Value delivery metrics are not usually associated with return on security investment (ROSI).",
            "C) Increase in ROSI": "Incorrect – Not the purpose of value delivery metrics.",
            "D) Increase in net profit": "Incorrect – Value delivery metrics are not directly tied to profit."
        }
    },
    {
        "id": 33,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "Joseph, a CIO, is collecting statistics on several operational areas and needs to find a standard way of measuring and publishing information about the effectiveness of his program. Which of the following is the best approach to follow?",
        "options": [
            "A) Scaled score",
            "B) NIST Cybersecurity Framework (CSF)",
            "C) Business Model for Information Security (BMIS)",
            "D) Balanced scorecard (BSC)"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Scaled score": "Incorrect – A scaled score is not a method used to publish metrics.",
            "B) NIST Cybersecurity Framework (CSF)": "Incorrect – NIST CSF is not typically used as a framework for publishing security program metrics.",
            "C) Business Model for Information Security (BMIS)": "Incorrect – BMIS helps understand relationships but is not used for publishing metrics.",
            "D) Balanced scorecard (BSC)": "Correct – The balanced scorecard is a well‑known framework for measuring and publishing performance and effectiveness."
        }
    },
    {
        "id": 34,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "Which of the following is the best description of the Business Model for Information Security (BMIS)?",
        "options": [
            "A) Describes the relationships (as dynamic interconnections) between policy, people, process, and technology.",
            "B) Describes the relationships (as dynamic interconnections) between people, process, technology, and the organization.",
            "C) Describes the primary elements (people, process, and technology) in an organization.",
            "D) Describes the dynamic interconnections (people, process, and technology) in an organization."
        ],
        "correct": "B",
        "option_explanations": {
            "A) Describes the relationships (as dynamic interconnections) between policy, people, process, and technology.": "Incorrect – 'Organization' is missing; policy is not an element.",
            "B) Describes the relationships (as dynamic interconnections) between people, process, technology, and the organization.": "Correct – BMIS models the dynamic interconnections among people, process, technology, and the organization.",
            "C) Describes the primary elements (people, process, and technology) in an organization.": "Incorrect – There are four elements, including the organization.",
            "D) Describes the dynamic interconnections (people, process, and technology) in an organization.": "Incorrect – The dynamic interconnections have specific names (human factors, emergence, etc.); people, process, technology are elements, not DIs."
        }
    },
    {
        "id": 35,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "What is the correct name for the model shown here?",
        "options": [
            "A) COBIT Model for Information Technology",
            "B) COBIT Model for Information Security",
            "C) Business Model for Information Security",
            "D) Business Model for Information Technology"
        ],
        "correct": "C",
        "option_explanations": {
            "A) COBIT Model for Information Technology": "Incorrect – The model shown is not COBIT.",
            "B) COBIT Model for Information Security": "Incorrect – The model shown is not COBIT.",
            "C) Business Model for Information Security": "Correct – The model is the Business Model for Information Security (BMIS).",
            "D) Business Model for Information Technology": "Incorrect – This is not the correct name of the model."
        }
    },
    {
        "id": 36,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "Jacqueline, an experienced CISO, is reading the findings in a recent risk assessment that describes deficiencies in the organization's vulnerability management process. How would Jacqueline use the Business Model for Information Security (BMIS) to analyze the deficiency?",
        "options": [
            "A) Identify the elements connected to the process DI.",
            "B) Identify the dynamic interconnections (DIs) connected to the process element.",
            "C) Identify the dynamic elements connected to human factors.",
            "D) Identify the dynamic elements connected to technology."
        ],
        "correct": "B",
        "option_explanations": {
            "A) Identify the elements connected to the process DI.": "Incorrect – The correct approach is to examine the DIs connected to the process element.",
            "B) Identify the dynamic interconnections (DIs) connected to the process element.": "Correct – The CISO should examine emergence, enabling and support, and governing DIs to analyze process deficiencies.",
            "C) Identify the dynamic elements connected to human factors.": "Incorrect – Human factors is one DI, but not necessarily the starting point for process analysis.",
            "D) Identify the dynamic elements connected to technology.": "Incorrect – Technology is an element, not the correct starting point."
        }
    },
    {
        "id": 37,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "Which of the following would constitute an appropriate use of the Zachman enterprise framework?",
        "options": [
            "A) An IT service management model as an alternative to ITIL",
            "B) Identifying system components, followed by high-level design and business functions",
            "C) Development of business requirements translated top-down into technical architecture",
            "D) IT systems described at a high level and then in increasing levels of detail"
        ],
        "correct": "D",
        "option_explanations": {
            "A) An IT service management model as an alternative to ITIL": "Incorrect – Zachman is not an IT service management framework.",
            "B) Identifying system components, followed by high-level design and business functions": "Incorrect – Zachman is a top‑down framework, not bottom‑up.",
            "C) Development of business requirements translated top-down into technical architecture": "Incorrect – Zachman does not start with business requirements; it describes the IT architecture itself.",
            "D) IT systems described at a high level and then in increasing levels of detail": "Correct – Zachman describes IT systems from high‑level down to individual components."
        }
    },
    {
        "id": 38,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "An IT architect needs to document the flow of data from one system to another, including external systems operated by third-party service providers. What kind of documentation does the IT architect need to develop?",
        "options": [
            "A) Data flow diagrams (DFDs)",
            "B) Entity relationship diagrams (ERDs)",
            "C) A Zachman architecture framework",
            "D) Visio diagrams showing information systems and data flows"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Data flow diagrams (DFDs)": "Correct – DFDs are visual depictions showing data flows among information systems.",
            "B) Entity relationship diagrams (ERDs)": "Incorrect – ERDs depict entities and relationships, not data flows.",
            "C) A Zachman architecture framework": "Incorrect – Zachman describes architecture in detail, but not necessarily data flows.",
            "D) Visio diagrams showing information systems and data flows": "Incorrect – This is too generic; DFDs are the proper documentation."
        }
    },
    {
        "id": 39,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "Carole is a CISO in a new organization with a fledgling security program. Carole needs to identify and develop mechanisms to ensure desired outcomes in selected business processes. What is a common term used to define these mechanisms?",
        "options": [
            "A) Checkpoints",
            "B) Detective controls",
            "C) Controls",
            "D) Preventive controls"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Checkpoints": "Incorrect – 'Checkpoints' is not the term that describes these mechanisms.",
            "B) Detective controls": "Incorrect – There will also be preventive, administrative, and other controls.",
            "C) Controls": "Correct – The common term is 'controls', which encompass preventive, detective, corrective, and others.",
            "D) Preventive controls": "Incorrect – While preventive controls are one type, the broad term is 'controls'."
        }
    },
    {
        "id": 40,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "What is the best approach to developing security controls in a new organization?",
        "options": [
            "A) Start with a standard control framework and make risk-based adjustments as needed.",
            "B) Start from scratch and develop controls based on risk as needed.",
            "C) Start with NIST CSF and move up to ISO 27001, then NIST 800-53 as the organization matures.",
            "D) Develop controls in response to an initial risk assessment."
        ],
        "correct": "A",
        "option_explanations": {
            "A) Start with a standard control framework and make risk-based adjustments as needed.": "Correct – Using a standard framework as a baseline and then adjusting based on risk is the best approach.",
            "B) Start from scratch and develop controls based on risk as needed.": "Incorrect – This approach may take too long and would likely converge to a standard framework over time.",
            "C) Start with NIST CSF and move up to ISO 27001, then NIST 800-53 as the organization matures.": "Incorrect – There is little benefit in switching frameworks; it is better to start with the right one.",
            "D) Develop controls in response to an initial risk assessment.": "Incorrect – Controls should be developed with periodic risk assessments, not just an initial one."
        }
    },
    {
        "id": 41,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "Which of the following is the best description of the COBIT framework?",
        "options": [
            "A) A security process and controls framework that can be integrated with ITIL or ISO 20000.",
            "B) An IT controls and process framework, on which IT controls and processes can be added at an organization's discretion.",
            "C) An IT process framework with optional security processes when Extended COBIT is implemented.",
            "D) An IT process framework that includes security processes that are interspersed throughout the framework."
        ],
        "correct": "D",
        "option_explanations": {
            "A) A security process and controls framework that can be integrated with ITIL or ISO 20000.": "Incorrect – COBIT is not strictly a security controls framework.",
            "B) An IT controls and process framework, on which IT controls and processes can be added at an organization's discretion.": "Incorrect – Security processes are not optional in COBIT.",
            "C) An IT process framework with optional security processes when Extended COBIT is implemented.": "Incorrect – There is no 'Extended COBIT'.",
            "D) An IT process framework that includes security processes that are interspersed throughout the framework.": "Correct – COBIT integrates security processes across its four domains."
        }
    },
    {
        "id": 42,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "One distinct disadvantage of the ISO 27001 standard is:",
        "options": [
            "A) The standard is costly (over one hundred U.S. dollars per copy).",
            "B) The standard is costly (a few thousand U.S. dollars per copy).",
            "C) The standard is available only for use in the United States.",
            "D) The standard is suitable only in large organizations."
        ],
        "correct": "A",
        "option_explanations": {
            "A) The standard is costly (over one hundred U.S. dollars per copy).": "Correct – ISO 27001 costs over $100 per copy, limiting widespread adoption.",
            "B) The standard is costly (a few thousand U.S. dollars per copy).": "Incorrect – The standard does not cost thousands of dollars per copy.",
            "C) The standard is available only for use in the United States.": "Incorrect – ISO 27001 can be used worldwide.",
            "D) The standard is suitable only in large organizations.": "Incorrect – ISO 27001 is suitable for organizations of all sizes."
        }
    },
    {
        "id": 43,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "Which of the following statements about ISO 27001 is correct?",
        "options": [
            "A) ISO 27001 consists primarily of a framework of security controls, followed by an appendix of security requirements for running a security management program.",
            "B) ISO 27001 consists primarily of a body of requirements for running a security management program, along with an appendix of security controls.",
            "C) ISO 27001 consists of a framework of information security controls.",
            "D) ISO 27001 consists of a framework of requirements for running a security management program."
        ],
        "correct": "B",
        "option_explanations": {
            "A) ISO 27001 consists primarily of a framework of security controls, followed by an appendix of security requirements for running a security management program.": "Incorrect – The main focus is the management system requirements, not the controls.",
            "B) ISO 27001 consists primarily of a body of requirements for running a security management program, along with an appendix of security controls.": "Correct – The standard's main body contains management system requirements, with controls in Annex A.",
            "C) ISO 27001 consists of a framework of information security controls.": "Incorrect – The main focus is the management system.",
            "D) ISO 27001 consists of a framework of requirements for running a security management program.": "Incorrect – It also contains an appendix of controls."
        }
    },
    {
        "id": 44,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "The U.S. law that regulates the protection of data related to medical care is:",
        "options": [
            "A) PIPEDA",
            "B) HIPAA",
            "C) GLBA",
            "D) GDPR"
        ],
        "correct": "B",
        "option_explanations": {
            "A) PIPEDA": "Incorrect – PIPEDA is the Canadian data privacy law.",
            "B) HIPAA": "Correct – HIPAA is the Health Insurance Portability and Accountability Act, with Privacy and Security Rules covering medical data.",
            "C) GLBA": "Incorrect – GLBA regulates personal information in the U.S. financial services industry.",
            "D) GDPR": "Incorrect – GDPR is the European Union regulation for personal data protection."
        }
    },
    {
        "id": 45,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "The regulation 'Security and Privacy Controls for Federal Information Systems and Organizations' is better known as:",
        "options": [
            "A) ISO/IEC 27001",
            "B) ISO/IEC 27002",
            "C) NIST CSF",
            "D) NIST SP800-53"
        ],
        "correct": "D",
        "option_explanations": {
            "A) ISO/IEC 27001": "Incorrect – This is an international standard, not the U.S. federal regulation.",
            "B) ISO/IEC 27002": "Incorrect – This is a code of practice for controls.",
            "C) NIST CSF": "Incorrect – This is the Cybersecurity Framework, not the controls catalog.",
            "D) NIST SP800-53": "Correct – NIST SP800-53 is the security and privacy controls catalog for federal systems."
        }
    },
    {
        "id": 46,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "What is the best explanation for the Implementation Tiers in the NIST Cybersecurity Framework?",
        "options": [
            "A) Implementation Tiers are levels of risk as determined by the organization.",
            "B) Implementation Tiers are stages of implementation of controls in the framework.",
            "C) Implementation Tiers are likened to maturity levels.",
            "D) Implementation Tiers are levels of risk as determined by an external auditor or regulator."
        ],
        "correct": "C",
        "option_explanations": {
            "A) Implementation Tiers are levels of risk as determined by the organization.": "Incorrect – Tiers are not risk levels.",
            "B) Implementation Tiers are stages of implementation of controls in the framework.": "Incorrect – Tiers are not about progress of control implementation.",
            "C) Implementation Tiers are likened to maturity levels.": "Correct – Although not strictly maturity levels, they are very similar.",
            "D) Implementation Tiers are levels of risk as determined by an external auditor or regulator.": "Incorrect – Tiers are not risk levels and are not externally determined."
        }
    },
    {
        "id": 47,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "Jeffrey is a CIO in an organization that performs financial services for private organizations as well as government agencies and U.S. federal agencies. Which is the best information security controls framework for this organization?",
        "options": [
            "A) CIS",
            "B) ISO 27001",
            "C) NIST CSF",
            "D) NIST 800-53"
        ],
        "correct": "D",
        "option_explanations": {
            "A) CIS": "Incorrect – While CIS is a high-quality framework, NIST 800-53 is mandatory for federal service providers.",
            "B) ISO 27001": "Incorrect – ISO 27001 is not required for U.S. federal service providers.",
            "C) NIST CSF": "Incorrect – NIST CSF is a cybersecurity methodology, not a controls framework.",
            "D) NIST 800-53": "Correct – As a service provider for the U.S. federal government, the organization must adopt NIST SP800-53."
        }
    },
    {
        "id": 48,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "The scope of requirements of PCI-DSS is:",
        "options": [
            "A) All systems that store, process, and transmit credit card numbers, as well as all other systems that can communicate with these systems.",
            "B) All systems that store, process, and transmit credit card numbers.",
            "C) All systems that store, process, and transmit unencrypted credit card numbers.",
            "D) All systems in an organization where credit card numbers are stored, processed, and transmitted."
        ],
        "correct": "A",
        "option_explanations": {
            "A) All systems that store, process, and transmit credit card numbers, as well as all other systems that can communicate with these systems.": "Correct – The scope includes cardholder data environment (CDE) systems and any connected systems.",
            "B) All systems that store, process, and transmit credit card numbers.": "Incorrect – It also includes systems that can communicate with the CDE.",
            "C) All systems that store, process, and transmit unencrypted credit card numbers.": "Incorrect – Even encrypted data places systems in scope.",
            "D) All systems in an organization where credit card numbers are stored, processed, and transmitted.": "Incorrect – Proper network segmentation can reduce scope."
        }
    },
    {
        "id": 49,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "Which of the following statements is true about controls in the Payment Card Industry Data Security Standard?",
        "options": [
            "A) Many controls are required, while some are 'addressable,' or optional, based on risk.",
            "B) All controls are required, regardless of actual risk.",
            "C) Controls that are required are determined for each organization by the acquiring bank.",
            "D) In addition to core controls, each credit card brand has its own unique controls."
        ],
        "correct": "B",
        "option_explanations": {
            "A) Many controls are required, while some are 'addressable,' or optional, based on risk.": "Incorrect – No controls are optional in PCI-DSS.",
            "B) All controls are required, regardless of actual risk.": "Correct – All controls in PCI-DSS are mandatory for all organizations.",
            "C) Controls that are required are determined for each organization by the acquiring bank.": "Incorrect – Acquiring banks do not determine applicability of controls.",
            "D) In addition to core controls, each credit card brand has its own unique controls.": "Incorrect – Card brands do not impose additional controls, though they may have specific reporting requirements."
        }
    },
    {
        "id": 50,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "The PCI-DSS is an example of:",
        "options": [
            "A) An industry regulation that is enforced with fines",
            "B) A private industry standard that is enforced with contracts",
            "C) A voluntary standard that, if used, can reduce cyber insurance premiums",
            "D) An international law enforced through treaties with member nations"
        ],
        "correct": "B",
        "option_explanations": {
            "A) An industry regulation that is enforced with fines": "Incorrect – PCI-DSS is not a law or regulation.",
            "B) A private industry standard that is enforced with contracts": "Correct – PCI-DSS is a private standard enforced through card brand operating rules and contracts.",
            "C) A voluntary standard that, if used, can reduce cyber insurance premiums": "Incorrect – PCI-DSS is mandatory for merchants and service providers that handle cardholder data.",
            "D) An international law enforced through treaties with member nations": "Incorrect – PCI-DSS is not an international law."
        }
    },
    {
        "id": 51,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "What are three factors that a risk manager might consider when developing an information security strategy?",
        "options": [
            "A) Threats, risks, and solutions",
            "B) Prevention, detection, and response",
            "C) Risk levels, staff qualifications, and security tooling",
            "D) Risk levels, operating costs, and compliance levels"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Threats, risks, and solutions": "Incorrect – These are factors but not the best set for strategy development.",
            "B) Prevention, detection, and response": "Incorrect – These are security program capabilities, not strategy factors.",
            "C) Risk levels, staff qualifications, and security tooling": "Incorrect – These are not the best available factors.",
            "D) Risk levels, operating costs, and compliance levels": "Correct – Risk, cost, and compliance are key factors when developing a long‑term security strategy."
        }
    },
    {
        "id": 52,
        "domain": "Domain 2 – IT Governance and Management",
        "question": "The responsibility for facilitation of an organization's cybersecurity program lies with:",
        "options": [
            "A) The board of directors",
            "B) The chief executive officer (CEO)",
            "C) The chief information officer (CIO)",
            "D) The chief information security officer (CISO)"
        ],
        "correct": "D",
        "option_explanations": {
            "A) The board of directors": "Incorrect – The board has ultimate responsibility, but facilitation lies with the CISO.",
            "B) The chief executive officer (CEO)": "Incorrect – The CEO does not facilitate the cybersecurity program.",
            "C) The chief information officer (CIO)": "Incorrect – Facilitation is a primary role of the CISO, not the CIO.",
            "D) The chief information security officer (CISO)": "Correct – The CISO facilitates the cybersecurity program and risk management process."
        }
    },
    # Domain 3 – IT Life Cycle Management
    {
        "id": 1,
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
            "A) The system being considered is too expensive to implement all at once.": "Incorrect – The cost of a system is not a primary reason for considering a POC.",
            "B) The system being considered will be a fully customized solution.": "Incorrect – A fully customized solution would not yet exist for a POC to take place.",
            "C) The system being considered is too complicated to evaluate fully.": "Correct – The system being evaluated is too complex to evaluate in a walkthrough or by analyzing its specifications.",
            "D) The system being considered is not yet available.": "Incorrect – A solution that is not yet available cannot be evaluated in a POC."
        }
    },
    {
        "id": 2,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "A formal process whereby the organization gathers all business and technical requirements and forwards them to several qualified vendors, who then respond to them, is called:",
        "options": [
            "A) Request for information (RFI)",
            "B) Request for proposals (RFP)",
            "C) Request for evaluation (RFE)",
            "D) Request for quote (RFQ)"
        ],
        "correct": "B",
        "option_explanations": {
            "A) Request for information (RFI)": "Incorrect – An RFI does not meet all of these requirements.",
            "B) Request for proposals (RFP)": "Correct – An RFP is the formal process used to publish the organization's requirements to several vendors, who will then reply formally with proposals that will meet those requirements.",
            "C) Request for evaluation (RFE)": "Incorrect – An RFE does not meet all of these requirements.",
            "D) Request for quote (RFQ)": "Incorrect – An RFQ does not meet all of these requirements."
        }
    },
    {
        "id": 3,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "An organization that wishes to acquire IT products or services that it fully understands should issue what kind of document?",
        "options": [
            "A) Request for proposals (RFP)",
            "B) Request for information (RFI)",
            "C) Statement of work (SOW)",
            "D) Bid schedule"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Request for proposals (RFP)": "Correct – An organization that understands the IT products or services it wants should issue an RFP. If it does not yet understand them, it should first issue an RFI.",
            "B) Request for information (RFI)": "Incorrect – An RFI does not meet all of these requirements.",
            "C) Statement of work (SOW)": "Incorrect – An SOW is not issued by a customer organization, but by a product or service organization.",
            "D) Bid schedule": "Incorrect – A bid schedule does not provide detailed information on IT products or services."
        }
    },
    {
        "id": 4,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "Which SEI CMM maturity level states that there is some consistency in the ways that individuals perform tasks from one time to the next, as well as some management planning and direction to ensure that tasks and projects are performed consistently?",
        "options": [
            "A) Initial",
            "B) Defined",
            "C) Repeatable",
            "D) Managed"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Initial": "Incorrect – The initial level defines an ad hoc, unmanaged process.",
            "B) Defined": "Incorrect – The defined level signifies a process that is documented but probably not measured.",
            "C) Repeatable": "Correct – The repeatable level states that there is some consistency in task performance and management planning and direction.",
            "D) Managed": "Incorrect – The managed level signifies a more mature process with statistics and metrics."
        }
    },
    {
        "id": 5,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "At what stage in the acquisition process should a project team develop requirements?",
        "options": [
            "A) After writing the test plan",
            "B) After operational process development",
            "C) Prior to writing the test plan",
            "D) Prior to operational process development"
        ],
        "correct": "C",
        "option_explanations": {
            "A) After writing the test plan": "Incorrect – Test plans are written directly from requirements, so requirements must come first.",
            "B) After operational process development": "Incorrect – Processes need to comply with requirements, so requirements must be defined before processes are designed.",
            "C) Prior to writing the test plan": "Correct – Requirements should be developed early in the life cycle; ideally before the solution is designed, but at least prior to writing the test plan.",
            "D) Prior to operational process development": "Incorrect – This is still not early enough; requirements need to be developed prior to solution selection and design."
        }
    },
    {
        "id": 6,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "All of the following are activities a project manager must perform to ensure a project is progressing in accordance with its plan except:",
        "options": [
            "A) Designing and testing the system",
            "B) Tracking project expenditures",
            "C) Recording task completion",
            "D) Managing the project schedule"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Designing and testing the system": "Correct – It is not the project manager's job to design and test the system; they coordinate those activities.",
            "B) Tracking project expenditures": "Incorrect – This is a key project management activity.",
            "C) Recording task completion": "Incorrect – This is a key project management activity.",
            "D) Managing the project schedule": "Incorrect – This is a key project management activity."
        }
    },
    {
        "id": 7,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "During which phase of the infrastructure development life cycle are all changes to the environment performed under formal processes, including incident management, problem management, defect management, change management, and configuration management?",
        "options": [
            "A) Testing",
            "B) Design",
            "C) Implementation",
            "D) Maintenance"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Testing": "Incorrect – Testing is performed before the infrastructure is placed into production.",
            "B) Design": "Incorrect – Design precedes changes to the live environment.",
            "C) Implementation": "Incorrect – Implementation is completed before subsequent changes are made.",
            "D) Maintenance": "Correct – After a system is in production, the maintenance phase involves incident, problem, defect, change, and configuration management."
        }
    },
    {
        "id": 8,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "Which management processes cover the post-implementation phase of the SDLC?",
        "options": [
            "A) Maintenance management and change management",
            "B) Change management and configuration management",
            "C) Service management and configuration management",
            "D) Incident management and problem management"
        ],
        "correct": "B",
        "option_explanations": {
            "A) Maintenance management and change management": "Incorrect – Maintenance management is not a formal operational term.",
            "B) Change management and configuration management": "Correct – The post-implementation phase of the SDLC is carried out by the change management and configuration management processes.",
            "C) Service management and configuration management": "Incorrect – Service management is broader; change and configuration management are the specific processes.",
            "D) Incident management and problem management": "Incorrect – Incident and problem management are operational processes but do not cover the entire post-implementation phase."
        }
    },
    {
        "id": 9,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "Change management and configuration management are key to which phase of the SDLC?",
        "options": [
            "A) Requirement definition",
            "B) Design",
            "C) Maintenance",
            "D) Testing"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Requirement definition": "Incorrect – Requirement definition occurs before initial implementation.",
            "B) Design": "Incorrect – Design occurs before initial implementation.",
            "C) Maintenance": "Correct – Change management and configuration management are essential operational processes in the maintenance phase.",
            "D) Testing": "Incorrect – Testing occurs during and immediately after initial development, not as ongoing operational processes."
        }
    },
    {
        "id": 10,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "Which of the following is a formal verification of system specifications and technologies?",
        "options": [
            "A) Design review",
            "B) User acceptance testing (UAT)",
            "C) Implementation review",
            "D) Quality assurance testing (QAT)"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Design review": "Incorrect – Design review is not a verification of technologies, since development and implementation have not yet taken place.",
            "B) User acceptance testing (UAT)": "Incorrect – UAT is a test of functionality, not of technologies.",
            "C) Implementation review": "Incorrect – Implementation review verifies the implementation process, not the specifications.",
            "D) Quality assurance testing (QAT)": "Correct – QAT is a formal verification of system specifications and technologies, typically performed by IT or IS departments."
        }
    },
    {
        "id": 11,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "All of the following are considerations when selecting and evaluating a software vendor except:",
        "options": [
            "A) Source code languages",
            "B) Financial stability",
            "C) References",
            "D) Vendor supportability"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Source code languages": "Correct – A software vendor's choice of source code languages is of lesser concern when selecting and evaluating software vendors.",
            "B) Financial stability": "Incorrect – Financial stability is an important consideration.",
            "C) References": "Incorrect – References are an important consideration.",
            "D) Vendor supportability": "Incorrect – Vendor supportability is an important consideration."
        }
    },
    {
        "id": 12,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "Which type of quality assurance method involves the users rather than IT or IS personnel?",
        "options": [
            "A) System testing",
            "B) Functional testing",
            "C) Quality assurance testing (QAT)",
            "D) User acceptance testing (UAT)"
        ],
        "correct": "D",
        "option_explanations": {
            "A) System testing": "Incorrect – Users are not involved in system testing.",
            "B) Functional testing": "Incorrect – Users are not involved in functional testing; this is performed by developers.",
            "C) Quality assurance testing (QAT)": "Incorrect – QAT is performed by alternative developers or software test personnel.",
            "D) User acceptance testing (UAT)": "Correct – UAT consists of formal tests performed by end users to determine whether the application will operate properly."
        }
    },
    {
        "id": 13,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "All of the following are considered risks to a software development project except:",
        "options": [
            "A) Delivered software not adequately meeting business needs",
            "B) Delivered software not meeting efficiency needs",
            "C) Termination of the project manager",
            "D) Project falling behind schedule or exceeding budget"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Delivered software not adequately meeting business needs": "Incorrect – This is a risk.",
            "B) Delivered software not meeting efficiency needs": "Incorrect – This is a risk.",
            "C) Termination of the project manager": "Correct – Termination of the project manager is not an anticipated risk; they can be replaced more easily.",
            "D) Project falling behind schedule or exceeding budget": "Incorrect – This is a risk."
        }
    },
    {
        "id": 14,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "Analysis of regulations and market conditions normally takes place during which phase of the SDLC?",
        "options": [
            "A) Testing phase",
            "B) Feasibility study",
            "C) Design phase",
            "D) Requirements definition phase"
        ],
        "correct": "B",
        "option_explanations": {
            "A) Testing phase": "Incorrect – Testing occurs after development.",
            "B) Feasibility study": "Correct – Changes in business conditions, including market changes and regulations, are examined during the feasibility study.",
            "C) Design phase": "Incorrect – The design phase concerns the logical design of the system.",
            "D) Requirements definition phase": "Incorrect – Requirements definition focuses on ensuring the system meets business needs."
        }
    },
    {
        "id": 15,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "Which term describes a Scrum project and is a focused effort to produce some portion of the total project deliverable?",
        "options": [
            "A) Milestone",
            "B) Objective",
            "C) Daily Scrum",
            "D) Sprint"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Milestone": "Incorrect – A milestone is a point when a key objective has been completed.",
            "B) Objective": "Incorrect – An objective is a goal of a project.",
            "C) Daily Scrum": "Incorrect – A Daily Scrum is a daily project status meeting.",
            "D) Sprint": "Correct – A typical Scrum project consists of several sprints, which are focused efforts to produce a portion of the project deliverable."
        }
    },
    {
        "id": 16,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "For what reason would an Internet-based financial application record the IP address of users who log in?",
        "options": [
            "A) This permits application performance testing.",
            "B) This provides localization information to the application.",
            "C) This provides authentication information to the application.",
            "D) This provides forensic information that can be used later."
        ],
        "correct": "D",
        "option_explanations": {
            "A) This permits application performance testing.": "Incorrect – There is little or no correlation between a user's IP address and application performance.",
            "B) This provides localization information to the application.": "Incorrect – IP addresses are not always reliable indicators of location (e.g., VPNs).",
            "C) This provides authentication information to the application.": "Incorrect – An IP address can provide location information but is not reliable for authentication.",
            "D) This provides forensic information that can be used later.": "Correct – Recording the IP address at login can be useful later if an account is compromised."
        }
    },
    {
        "id": 17,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "In the context of logical access controls, the terms \"subject\" and \"object\" refer to:",
        "options": [
            "A) \"Subject\" refers to the person who is accessing the data, and \"object\" refers to the data being accessed.",
            "B) \"Subject\" refers to the data being accessed, and \"object\" refers to the file that contains the data.",
            "C) \"Subject\" refers to the security context, and \"object\" refers to the data.",
            "D) \"Subject\" refers to the data, and \"object\" refers to the person or entity accessing the data."
        ],
        "correct": "A",
        "option_explanations": {
            "A) \"Subject\" refers to the person who is accessing the data, and \"object\" refers to the data being accessed.": "Correct – Subject refers to a person (or program/machine), and object refers to data or other resource being accessed.",
            "B) \"Subject\" refers to the data being accessed, and \"object\" refers to the file that contains the data.": "Incorrect – This definition of \"object\" is too narrow.",
            "C) \"Subject\" refers to the security context, and \"object\" refers to the data.": "Incorrect – \"Subject\" and \"object\" are not used in this manner.",
            "D) \"Subject\" refers to the data, and \"object\" refers to the person or entity accessing the data.": "Incorrect – The definitions are reversed."
        }
    },
    {
        "id": 18,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "In the context of logical access control, what does the term \"fail closed\" mean?",
        "options": [
            "A) In the event of a power outage, all access points are closed.",
            "B) If access is denied, a database table will be closed or locked to changes.",
            "C) If an access control mechanism fails, all access will be denied.",
            "D) If an access control mechanism fails, all access will be allowed."
        ],
        "correct": "C",
        "option_explanations": {
            "A) In the event of a power outage, all access points are closed.": "Incorrect – This is not the definition of fail closed.",
            "B) If access is denied, a database table will be closed or locked to changes.": "Incorrect – This is not the definition of fail closed.",
            "C) If an access control mechanism fails, all access will be denied.": "Correct – Fail closed means that when the access control mechanism fails, no access is granted.",
            "D) If an access control mechanism fails, all access will be allowed.": "Incorrect – This describes fail open, not fail closed."
        }
    },
    {
        "id": 19,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "When would you design an access control to \"fail open\"?",
        "options": [
            "A) In the case of fire suppression controls, which would need to activate immediately if a fire is detected.",
            "B) In the case of building access controls, which would need to permit evacuation of personnel in an emergency.",
            "C) In the event of an emergency, where data access controls would need to allow anyone access to data so it could be backed up successfully and removed from the site.",
            "D) In the case of an incident, where outside investigators would require immediate and complete access to restricted data."
        ],
        "correct": "B",
        "option_explanations": {
            "A) In the case of fire suppression controls, which would need to activate immediately if a fire is detected.": "Incorrect – This is not an example of fail open.",
            "B) In the case of building access controls, which would need to permit evacuation of personnel in an emergency.": "Correct – Building access controls should fail open to allow people to exit during emergencies.",
            "C) In the event of an emergency, where data access controls would need to allow anyone access to data so it could be backed up successfully and removed from the site.": "Incorrect – This is not a typical fail-open scenario.",
            "D) In the case of an incident, where outside investigators would require immediate and complete access to restricted data.": "Incorrect – This is not a typical fail-open scenario."
        }
    },
    {
        "id": 20,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "What are the three levels of the Constructive Cost Model (COCOMO) method for estimating software development projects?",
        "options": [
            "A) Basic, Intermediate, and Detailed",
            "B) Levels I, II, and III",
            "C) Initial, Managed, and Optimized",
            "D) Organic, Semi-detached, and Embedded"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Basic, Intermediate, and Detailed": "Correct – The three levels of COCOMO are Basic, Intermediate, and Detailed.",
            "B) Levels I, II, and III": "Incorrect – These are not the levels of COCOMO.",
            "C) Initial, Managed, and Optimized": "Incorrect – These are not the levels of COCOMO.",
            "D) Organic, Semi-detached, and Embedded": "Incorrect – These are not the levels of COCOMO."
        }
    },
    {
        "id": 21,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "The best source for requirements for an RFP project is:",
        "options": [
            "A) Published industry standards",
            "B) The incumbent system's specifications",
            "C) Vendors and suppliers",
            "D) The organization's own business, technical, and security requirements"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Published industry standards": "Incorrect – There is no industry-standard list of requirements; every organization is different.",
            "B) The incumbent system's specifications": "Incorrect – The incumbent system may no longer be meeting requirements.",
            "C) Vendors and suppliers": "Incorrect – Requirements should not come from vendors to avoid bias.",
            "D) The organization's own business, technical, and security requirements": "Correct – The organization must develop its own requirements internally for an RFP."
        }
    },
    {
        "id": 22,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "An organization wants to build a new application, but it has not yet defined precisely how end-user interaction will work. Which application development technique should be chosen to determine end-user interaction?",
        "options": [
            "A) Prototyping",
            "B) RAD",
            "C) Waterfall",
            "D) Scrum"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Prototyping": "Correct – Prototyping helps determine end-user interaction by building various prototypes until the most suitable one is chosen.",
            "B) RAD": "Incorrect – RAD is more suited when more is known about the desired function.",
            "C) Waterfall": "Incorrect – Waterfall requires requirements to be developed in advance.",
            "D) Scrum": "Incorrect – Scrum is a good alternative but not the best choice for determining unknown interaction details."
        }
    },
    {
        "id": 23,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "A project manager regularly sends project status reports to executive management. Executives are requesting that status reports include visual diagrams showing the project schedule and project-critical paths from week to week. Which type of a chart should the project manager use?",
        "options": [
            "A) WBS",
            "B) PRINCE2",
            "C) PERT",
            "D) Gantt"
        ],
        "correct": "C",
        "option_explanations": {
            "A) WBS": "Incorrect – WBS shows the project structure, not the schedule or critical path.",
            "B) PRINCE2": "Incorrect – PRINCE2 is a methodology, not a reporting tool.",
            "C) PERT": "Correct – A PERT chart shows the project status and critical path.",
            "D) Gantt": "Incorrect – Gantt charts show project status but do not show the critical path."
        }
    },
    {
        "id": 24,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "During which phase of the SDLC are functionality and design characteristics verified?",
        "options": [
            "A) Maintenance",
            "B) Implementation",
            "C) Testing",
            "D) Design"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Maintenance": "Incorrect – Functionality and design are not verified during maintenance.",
            "B) Implementation": "Incorrect – Verification occurs before implementation.",
            "C) Testing": "Correct – Testing is the phase where functionality and design are verified in the test plan.",
            "D) Design": "Incorrect – Verification occurs after design, during testing."
        }
    },
    {
        "id": 25,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "Which kind of testing ensures that data is being formatted properly and inserted into the new application from the old application?",
        "options": [
            "A) Unit testing",
            "B) Migration testing",
            "C) Regression testing",
            "D) Functional testing"
        ],
        "correct": "B",
        "option_explanations": {
            "A) Unit testing": "Incorrect – Unit testing verifies small portions of code, not data migration.",
            "B) Migration testing": "Correct – Migration testing ensures data is properly formatted and inserted when moving from an old application to a new one.",
            "C) Regression testing": "Incorrect – Regression testing checks that changes do not break existing functionality.",
            "D) Functional testing": "Incorrect – Functional testing confirms proper operation of a system, not data migration."
        }
    },
    {
        "id": 26,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "Which entity commissions feasibility studies to support a business case?",
        "options": [
            "A) Project team",
            "B) Project manager",
            "C) CISO",
            "D) IT steering committee"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Project team": "Incorrect – The project team executes tasks; it does not commission feasibility studies.",
            "B) Project manager": "Incorrect – The project manager coordinates activities but does not commission studies.",
            "C) CISO": "Incorrect – The CISO leads cybersecurity, not project commissioning.",
            "D) IT steering committee": "Correct – The IT steering committee formally commissions feasibility studies, approves projects, and assigns resources."
        }
    },
    {
        "id": 27,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "What is the purpose of a configuration management database?",
        "options": [
            "A) Storage of every change made to system components",
            "B) Storage of available configurations for system components",
            "C) Storage of approvals for configuration changes to a system",
            "D) Storage of the most recent change made to system components"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Storage of every change made to system components": "Correct – A CMDB stores all changes made to a system, enabling knowledge of every component's configuration at any point in time.",
            "B) Storage of available configurations for system components": "Incorrect – A CMDB stores actual configurations, not just available configurations.",
            "C) Storage of approvals for configuration changes to a system": "Incorrect – Approval storage is part of the change control process, not the CMDB's purpose.",
            "D) Storage of the most recent change made to system components": "Incorrect – A CMDB stores all historical changes, not just the most recent."
        }
    },
    {
        "id": 28,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "When is the best time for an organization to measure business benefits of a new system?",
        "options": [
            "A) During unit testing",
            "B) One year after implementation",
            "C) During requirements definition",
            "D) During user acceptance testing"
        ],
        "correct": "B",
        "option_explanations": {
            "A) During unit testing": "Incorrect – The system is not yet running.",
            "B) One year after implementation": "Correct – Measuring benefits after implementation allows time for business measurements to collect data.",
            "C) During requirements definition": "Incorrect – The system is not yet built.",
            "D) During user acceptance testing": "Incorrect – The system is not yet fully operational."
        }
    },
    {
        "id": 29,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "Which of the following represents the components of the project in graphical or tabular form and is a visual or structural representation of the system, software, or application?",
        "options": [
            "A) Data flow diagram (DFD)",
            "B) Work breakdown structure (WBS)",
            "C) Zachman model",
            "D) Object breakdown structure (OBS)"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Data flow diagram (DFD)": "Incorrect – A DFD depicts data flows in a system.",
            "B) Work breakdown structure (WBS)": "Incorrect – A WBS depicts all the work required to complete a project.",
            "C) Zachman model": "Incorrect – The Zachman model shows the architecture of a system.",
            "D) Object breakdown structure (OBS)": "Correct – An OBS is a hierarchical visual or structural representation of the system, software, or application."
        }
    },
    {
        "id": 30,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "Which type of tests will determine whether there are any failures or errors in input, processing, or output controls in an application?",
        "options": [
            "A) Referential integrity tests",
            "B) Data conversion tests",
            "C) Data integrity tests",
            "D) Static data storage tests"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Referential integrity tests": "Incorrect – These confirm primary and foreign key relationships, not overall input/output controls.",
            "B) Data conversion tests": "Incorrect – These confirm data is properly converted from one system to another.",
            "C) Data integrity tests": "Correct – Data integrity testing confirms whether an application properly accepts, processes, and stores information, including input, processing, and output controls.",
            "D) Static data storage tests": "Incorrect – These confirm the correctness of data storage, not the broader control failures."
        }
    },
    {
        "id": 31,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "Which quantitative method of sizing software projects is repeatable for traditional programming languages, but is not as effective with newer, nontextual languages?",
        "options": [
            "A) Source lines of code (SLOC)",
            "B) Work breakdown structure (WBS)",
            "C) Object breakdown structure (OBS)",
            "D) Constructive Cost Model (COCOMO)"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Source lines of code (SLOC)": "Correct – SLOC (or KLOC) is quantitative and repeatable for traditional textual languages but less effective for modern nontextual languages.",
            "B) Work breakdown structure (WBS)": "Incorrect – WBS depicts work, not software size.",
            "C) Object breakdown structure (OBS)": "Incorrect – OBS depicts system components, not software size.",
            "D) Constructive Cost Model (COCOMO)": "Incorrect – COCOMO calculates cost, not size."
        }
    },
    {
        "id": 32,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "Which type of testing, usually performed by developers during the coding phase of the software development project, is used to verify that the code in various parts of the application works properly?",
        "options": [
            "A) Unit testing",
            "B) Regression testing",
            "C) Functional testing",
            "D) User acceptance testing"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Unit testing": "Correct – Unit testing is performed by developers during coding to verify that sections of code work correctly.",
            "B) Regression testing": "Incorrect – Regression testing verifies that changes do not break existing functionality.",
            "C) Functional testing": "Incorrect – Functional testing verifies the correct operation of a system.",
            "D) User acceptance testing": "Incorrect – User acceptance testing confirms user-facing features work properly."
        }
    },
    {
        "id": 33,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "An organization is considering acquiring a key business application from a small software company. What business provision should the organization require of the software company?",
        "options": [
            "A) Bonding",
            "B) Liability insurance",
            "C) Developer background checks",
            "D) Place source code in escrow"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Bonding": "Incorrect – Bonding is related to operational liability, not survival of the vendor.",
            "B) Liability insurance": "Incorrect – Liability insurance does not ensure the vendor's survival.",
            "C) Developer background checks": "Incorrect – Developer background checks do not help ensure the vendor's survival.",
            "D) Place source code in escrow": "Correct – Software escrow ensures the customer can continue using and maintaining the application even if the vendor goes out of business."
        }
    },
    {
        "id": 34,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "Which phase of the SDLC is continually referenced during the development, acquisition, and testing phases to ensure that the system is meeting the required specifications?",
        "options": [
            "A) Testing",
            "B) Requirements definition",
            "C) Design",
            "D) Implementation"
        ],
        "correct": "B",
        "option_explanations": {
            "A) Testing": "Incorrect – Testing is not referenced during all these phases.",
            "B) Requirements definition": "Correct – The requirements definition phase is continually referenced throughout the SDLC to ensure the system meets agreed-upon requirements.",
            "C) Design": "Incorrect – Design is not referenced during all phases.",
            "D) Implementation": "Incorrect – Implementation is not referenced throughout the SDLC."
        }
    },
    {
        "id": 35,
        "domain": "Domain 3 – IT Life Cycle Management",
        "question": "What is the purpose of the review process after each phase of the SDLC?",
        "options": [
            "A) To establish additional requirements",
            "B) To change existing requirements",
            "C) To ensure that project deliverables meet the agreed-upon requirements",
            "D) To provide end users with a progress check on system development"
        ],
        "correct": "C",
        "option_explanations": {
            "A) To establish additional requirements": "Incorrect – Additional requirements are not introduced in post-phase reviews.",
            "B) To change existing requirements": "Incorrect – Requirements are not altered in post-phase reviews.",
            "C) To ensure that project deliverables meet the agreed-upon requirements": "Correct – Post-phase reviews, sometimes called gate reviews, ensure that deliverables meet requirements before the project progresses.",
            "D) To provide end users with a progress check on system development": "Incorrect – The main purpose is to review project status and performance, not just inform end users."
        }
    },
    # Domain 4 – IT Service Management and Continuity
    {
        "id": 1,
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
            "A) Bridge": "Incorrect – A bridge forwards all packets regardless of their destination.",
            "B) Gateway": "Incorrect – A gateway is an application-layer device that transforms packets from one protocol to another.",
            "C) Router": "Correct – A router is a network device that forwards packets towards their destination.",
            "D) Switch": "Incorrect – A switch forwards packets based on their MAC or IP address."
        }
    },
    {
        "id": 2,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "A security manager is planning to implement a first-time use of a vulnerability scanning tool in an organization. What method should the security manager use to confirm that all assets are scanned?",
        "options": [
            "A) Compare the scan results with the accounting department asset inventory.",
            "B) Compare the scan results with the contents of the CMDB.",
            "C) Compare the scan results with a discovery scan performed by the vulnerability scanning tool.",
            "D) Compare the scan results with the latest network diagram."
        ],
        "correct": "B",
        "option_explanations": {
            "A) Compare the scan results with the accounting department asset inventory.": "Incorrect – Business asset inventories are not regarded as accurately reflecting all working systems in an environment. Further, a business asset inventory will not account for virtual machines.",
            "B) Compare the scan results with the contents of the CMDB.": "Correct – The best option is to compare it with a well-managed configuration management database (CMDB).",
            "C) Compare the scan results with a discovery scan performed by the vulnerability scanning tool.": "Incorrect – A discovery scan will only find what is present on the network at the time the scan is performed. Assets that are not running at the time of the scan, and assets not reachable because of network ACLs, will not be identified. Further, unauthorized devices will show up in a discovery scan.",
            "D) Compare the scan results with the latest network diagram.": "Incorrect – Network diagrams often do not include every individual device in an environment."
        }
    },
    {
        "id": 3,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "Which of the following methods should be used to create a point-in-time copy of a large production database?",
        "options": [
            "A) Storage system snapshot",
            "B) Storage system replication",
            "C) E-vaulting",
            "D) Export to a flat file that is backed up to tape"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Storage system snapshot": "Correct – A storage system snapshot is nearly instantaneous and is the best method for producing a 'point-in-time' backup of a large database.",
            "B) Storage system replication": "Incorrect – Replication is not used to create a backup copy, but rather a live second copy of a data set.",
            "C) E-vaulting": "Incorrect – E-vaulting does not necessarily create a point-in-time backup.",
            "D) Export to a flat file that is backed up to tape": "Incorrect – An export to a flat file and backup to tape would not be a point-in-time backup unless the database management system was quiesced."
        }
    },
    {
        "id": 4,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "All of the following protocols are used for federated authentication except:",
        "options": [
            "A) OAuth",
            "B) SAML",
            "C) WSDL",
            "D) HMAC"
        ],
        "correct": "C",
        "option_explanations": {
            "A) OAuth": "Incorrect – OAuth is a protocol found in federated authentication.",
            "B) SAML": "Incorrect – SAML is a protocol found in federated authentication.",
            "C) WSDL": "Correct – WSDL is a protocol used to describe the functionality of a web service.",
            "D) HMAC": "Incorrect – HMAC is a protocol found in federated authentication, although it has fallen out of common use."
        }
    },
    {
        "id": 5,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "What is typically the most significant risk associated with end users being local administrators on their workstations?",
        "options": [
            "A) End users will have access to all confidential information.",
            "B) End users can install unauthorized software.",
            "C) Malware can run at the highest privilege level.",
            "D) End users can use tools to crack all domain passwords."
        ],
        "correct": "C",
        "option_explanations": {
            "A) End users will have access to all confidential information.": "Incorrect – Local administrative privileges should not ever result in end users having access to data on other systems.",
            "B) End users can install unauthorized software.": "Incorrect – While it is correct that end users who are local administrators can install software, this is generally not as severe a risk as a malware infection.",
            "C) Malware can run at the highest privilege level.": "Correct – If malware is introduced by the end user in a phishing or watering hole attack, the malware will run as an administrator, which is the highest privilege level on the system. Malware would have access to all files, data, and devices on the machine.",
            "D) End users can use tools to crack all domain passwords.": "Incorrect – End users should not be able to access the encrypted password file for all users in the organization."
        }
    },
    {
        "id": 6,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "Which of the following persons is best suited to approve users' access to sensitive data in a customer database?",
        "options": [
            "A) Customer service manager",
            "B) IT service desk personnel",
            "C) Information security manager",
            "D) IT manager"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Customer service manager": "Correct – The customer service manager is the best available choice because a business leader is almost always more familiar with business processes than are IT and information security personnel. Further, because the customer service manager is responsible for customer service, this is the person who should be specifying which persons in the organization are permitted to access customer service data.",
            "B) IT service desk personnel": "Incorrect – IT service desk personnel have insufficient knowledge about business operations and the persons using them.",
            "C) Information security manager": "Incorrect – Information security managers have insufficient knowledge about business operations and the persons using them.",
            "D) IT manager": "Incorrect – IT and IT security-related personnel are not going to be as familiar with business unit or business department operations as the leaders of business units or business departments."
        }
    },
    {
        "id": 7,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "An organization is planning a new SaaS service offering and is uncertain about the resources required to support the service. How should the organization proceed?",
        "options": [
            "A) Calculate projected performance using CMMI tools.",
            "B) Calculate projected performance using Zachman tools.",
            "C) Measure actual performance metrics in production.",
            "D) Build a working prototype and perform load tests."
        ],
        "correct": "D",
        "option_explanations": {
            "A) Calculate projected performance using CMMI tools.": "Incorrect – CMMI tools are used to measure process maturity, not system performance.",
            "B) Calculate projected performance using Zachman tools.": "Incorrect – Zachman tools are used to develop an enterprise architecture, not system performance.",
            "C) Measure actual performance metrics in production.": "Incorrect – While this technique will provide the most accurate data, it is better to get estimates earlier in the development process so that changes in architecture, coding, or business models can be made prior to completion of the project.",
            "D) Build a working prototype and perform load tests.": "Correct – The best choice here is to build a prototype system that closely resembles the network, computing, and database activities and perform load testing. This will give the organization an idea of the capacity of the planned system."
        }
    },
    {
        "id": 8,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "What is the best definition of a problem in ITIL-based service management?",
        "options": [
            "A) Chronic exceptions in audits of IT systems",
            "B) The same incident that occurs repeatedly",
            "C) Repeated unscheduled downtime",
            "D) Unscheduled downtime that exceeds SLAs"
        ],
        "correct": "B",
        "option_explanations": {
            "A) Chronic exceptions in audits of IT systems": "Incorrect – This is not the definition of a problem in ITIL.",
            "B) The same incident that occurs repeatedly": "Correct – In ITIL, a problem is the same incident that occurs repeatedly, indicating a root cause that needs to be addressed.",
            "C) Repeated unscheduled downtime": "Incorrect – This is too narrow; a problem could involve recurring incidents of any type.",
            "D) Unscheduled downtime that exceeds SLAs": "Incorrect – This is a metric, not the definition of a problem."
        }
    },
    {
        "id": 9,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "Which of the following is the best relationship between system security and the use of vulnerability scanning tools?",
        "options": [
            "A) Vulnerability scanning is performed proactively, and it drives the security patching and hardening functions.",
            "B) Vulnerability scanning is performed proactively, and it drives the security patching function.",
            "C) Patching and hardening are performed proactively, and vulnerability scanning is used to verify their effectiveness.",
            "D) Patching is performed proactively, and vulnerability scanning is used to verify its effectiveness."
        ],
        "correct": "C",
        "option_explanations": {
            "A) Vulnerability scanning is performed proactively, and it drives the security patching and hardening functions.": "Incorrect – System security should not be driven by the vulnerability scanning function. Instead, system security should be proactively performed, with vulnerability scanning serving as a means for verifying that they are effective.",
            "B) Vulnerability scanning is performed proactively, and it drives the security patching function.": "Incorrect – Patching and hardening should be proactive, with scanning used to verify their effectiveness.",
            "C) Patching and hardening are performed proactively, and vulnerability scanning is used to verify their effectiveness.": "Correct – The best use of vulnerability scanning is its functioning as a quality assurance activity, to ensure that security patching and system hardening are being performed effectively.",
            "D) Patching is performed proactively, and vulnerability scanning is used to verify its effectiveness.": "Incorrect – System hardening should also be proactive; scanning should verify both."
        }
    },
    {
        "id": 10,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "A SaaS provider and a customer are having a dispute about the availability of service, quality of service, and issue resolution provided by the SaaS provider. What type of a legal agreement should the parties add to their contract to better define these problems and their resolution?",
        "options": [
            "A) Pricing table",
            "B) Exit clause",
            "C) Performance addendum",
            "D) Service level agreement"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Pricing table": "Incorrect – Pricing is not the core problem in this example.",
            "B) Exit clause": "Incorrect – An exit clause only addresses terms in which the parties can terminate the agreement; it does not address service quality.",
            "C) Performance addendum": "Incorrect – A performance addendum is not the appropriate term for an agreement that addresses these problems.",
            "D) Service level agreement": "Correct – A service level agreement (SLA) is used to define the quantity and quality of service to be provided by a service provider to its customers. An SLA can cover issues such as transaction volume, service quality, issue resolution, and service availability."
        }
    },
    {
        "id": 11,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "What is the purpose of a business impact analysis?",
        "options": [
            "A) It defines the most critical business processes.",
            "B) It defines the most critical IT applications.",
            "C) It defines the most critical service providers.",
            "D) It defines the disaster recovery plan."
        ],
        "correct": "A",
        "option_explanations": {
            "A) It defines the most critical business processes.": "Correct – A business impact analysis (BIA) defines the most critical business processes in the organization. The BIA reveals which business processes warrant the development of emergency contingency planning and disaster recovery planning.",
            "B) It defines the most critical IT applications.": "Incorrect – A BIA does not directly define the most critical IT applications.",
            "C) It defines the most critical service providers.": "Incorrect – A BIA does not directly define the most critical service providers; however, a BIA will reveal service providers required by the most critical business processes.",
            "D) It defines the disaster recovery plan.": "Incorrect – The BIA does not define the disaster recovery plan (DRP), but the BIA will help to drive development of the DRP."
        }
    },
    {
        "id": 12,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "An IT architect needs to increase the resilience of a single application server. Which of the following choices will least benefit the server's resilience?",
        "options": [
            "A) Active-active cluster",
            "B) Active-passive cluster",
            "C) Geo-cluster",
            "D) Redundant power supply"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Active-active cluster": "Incorrect – An active-active cluster provides failover and load balancing, significantly improving resilience.",
            "B) Active-passive cluster": "Incorrect – An active-passive cluster provides failover capability, improving resilience.",
            "C) Geo-cluster": "Incorrect – A geo-cluster distributes servers across locations, providing geographic resilience.",
            "D) Redundant power supply": "Correct – A redundant power supply only addresses the problem of a power supply failure but does not address other failures such as storage or CPU."
        }
    },
    {
        "id": 13,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "Which of the following backup schemes best protects an organization from ransomware?",
        "options": [
            "A) Storage system replication",
            "B) Storage system mirroring",
            "C) Storage system snapshots",
            "D) RAID-5"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Storage system replication": "Incorrect – Replication will effectively replicate the damaging effects of ransomware from the primary storage system to other storage systems through their replication.",
            "B) Storage system mirroring": "Incorrect – Mirroring will effectively replicate the damaging effects of ransomware from primary storage to mirrored storage.",
            "C) Storage system snapshots": "Correct – Storage system snapshots effectively store the state of a storage system from time to time; if ransomware destroys files in the storage system, the system can be rolled back to a recent snapshot, effectively restoring damaged files.",
            "D) RAID-5": "Incorrect – RAID-5 is used to improve storage system performance and would effectively allow ransomware to damage files more quickly."
        }
    },
    {
        "id": 14,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "A mail order organization wants to develop procedures to be followed in the event that the main office building cannot be occupied, so that customer orders can still be fulfilled. What kind of a plan does the organization need to develop?",
        "options": [
            "A) Business impact analysis",
            "B) Business continuity plan",
            "C) Disaster recovery plan",
            "D) Emergency evacuation plan"
        ],
        "correct": "B",
        "option_explanations": {
            "A) Business impact analysis": "Incorrect – A business impact analysis is used to determine which business processes are most critical and warrant the development of business continuity plans.",
            "B) Business continuity plan": "Correct – A business continuity plan is the document that describes procedures to be followed when events such as local and regional disasters prevent normal business operations.",
            "C) Disaster recovery plan": "Incorrect – A disaster recovery plan is used to survey damage and salvage business equipment, as well as direct the initiation of procedures to activate alternative resources, such as IT systems in alternative locations if IT equipment in primary locations is inoperable.",
            "D) Emergency evacuation plan": "Incorrect – An emergency evacuation plan, while important during disasters, does not contribute to the ability for an organization to continue the fulfillment of customer orders."
        }
    },
    {
        "id": 15,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "An IT department is planning on implementing disaster recovery capabilities in some of its business systems. What means should be used to determine which applications require DR capabilities and to what level of recoverability?",
        "options": [
            "A) Business continuity plan",
            "B) Disaster recovery plan",
            "C) Risk assessment",
            "D) Business impact analysis"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Business continuity plan": "Incorrect – While a business continuity plan and a disaster recovery plan are closely related, the BIA is the tool that defines which business processes warrant the development of supporting DR capabilities.",
            "B) Disaster recovery plan": "Incorrect – A DR plan does not define which systems are to be covered or what recovery targets are to be met.",
            "C) Risk assessment": "Incorrect – A risk assessment, while valuable, does not define which business processes warrant the development of DR plans.",
            "D) Business impact analysis": "Correct – A business impact analysis (BIA) is used to determine which business processes are most critical, and this leads to the development of recovery objectives, which in turn leads to the development of DR capabilities that meet those objectives."
        }
    },
    {
        "id": 16,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "Which of the following is the most compelling reason for an organization to not automate its data purging jobs in support of data retention policies?",
        "options": [
            "A) DR planning",
            "B) Referential integrity",
            "C) Privacy breaches",
            "D) Legal holds"
        ],
        "correct": "D",
        "option_explanations": {
            "A) DR planning": "Incorrect – DR planning has little or no bearing on automatic purging of stale data.",
            "B) Referential integrity": "Incorrect – Referential integrity is a matter that can often be solved through structured data removal, but it's not relevant to the automated starting of purge jobs.",
            "C) Privacy breaches": "Incorrect – Privacy breaches on their own should have no bearing on the automatic purging of data.",
            "D) Legal holds": "Correct – Legal holds in most organizations are manual processes and involve the cessation of data purging for arbitrary sets of information. A better approach would be a manually initiated data purging process that is started only after it is determined that no legal holds exist for the data to be purged."
        }
    },
    {
        "id": 17,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "Which of the following schemes is most likely to be successful for workstations used by a mobile workforce?",
        "options": [
            "A) Automated patching followed by a system restart that the end user can control",
            "B) Automated patching and restarts",
            "C) End-user-initiated patching and restarts",
            "D) Applying only those patches not requiring a system restart"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Automated patching followed by a system restart that the end user can control": "Correct – Automated patching, together with giving end users some control over restarts, is most likely to be successful, as this gives users an option to defer restarts (for a while) so that important work is not interrupted.",
            "B) Automated patching and restarts": "Incorrect – Automated restarts are likely to disrupt critical business activities (such as an executive presentation) from time to time.",
            "C) End-user-initiated patching and restarts": "Incorrect – End users are not inclined or likely to be diligent about initiating patching jobs.",
            "D) Applying only those patches not requiring a system restart": "Incorrect – This plan will result in the absence of many critical patches, which could lead to an increased frequency and impact of malware attacks."
        }
    },
    {
        "id": 18,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "An IT department completed a data discovery assessment and found that numerous users were saving files containing sensitive information on organization-wide readable file shares. Which of the following is the best remediation for this matter?",
        "options": [
            "A) Remove the offending files from the org-wide share.",
            "B) Announce to users that the org-wide readable share is not for sensitive data.",
            "C) Change the org-wide readable share to read-only for most users.",
            "D) Change the org-wide readable share to write-only for most users."
        ],
        "correct": "C",
        "option_explanations": {
            "A) Remove the offending files from the org-wide share.": "Incorrect – Simply removing the files containing sensitive information is not likely to solve the problem, as similar files may soon reappear.",
            "B) Announce to users that the org-wide readable share is not for sensitive data.": "Incorrect – Many users typically ignore such reminders, and many do not read them at all.",
            "C) Change the org-wide readable share to read-only for most users.": "Correct – In most organizations, few people truly need to write to the organization-wide readable share. This will drive users to using department shares for saving sensitive data, which will result in lower risk to the business since sensitive data would then be readable only by personnel in their respective departments instead of the entire organization.",
            "D) Change the org-wide readable share to write-only for most users.": "Incorrect – Making the share write-only would result in the org-wide share being unreadable."
        }
    },
    {
        "id": 19,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "For which users or groups should the SQL listener on a database management system be accessible?",
        "options": [
            "A) For the application accounts only",
            "B) For the application and DBA accounts only",
            "C) For DBA accounts only",
            "D) For DBA accounts plus all users of the application"
        ],
        "correct": "B",
        "option_explanations": {
            "A) For the application accounts only": "Incorrect – This would deprive the DBA from being able to access the SQL listener.",
            "B) For the application and DBA accounts only": "Correct – Applications that need to access the database need to be able to access the SQL listener on a database server, as do DBAs who need to perform maintenance on the system.",
            "C) For DBA accounts only": "Incorrect – This would deprive applications that need to access the database management system.",
            "D) For DBA accounts plus all users of the application": "Incorrect – Application end users should not be given direct access to the SQL listener. Instead, capabilities in the application should be provided that give users the access they need."
        }
    },
    {
        "id": 20,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "An organization's financial accounting system crashes every Friday night after backups have completed. In ITIL terms, what process should be invoked?",
        "options": [
            "A) Problem management",
            "B) Incident management",
            "C) Capacity management",
            "D) Business continuity management"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Problem management": "Correct – Problem management is the correct ITIL process to be invoked when similar incidents are recurring.",
            "B) Incident management": "Incorrect – Incident management is used to manage individual incidents, but not the recurrence of similar incidents.",
            "C) Capacity management": "Incorrect – Capacity management is not the correct response, unless problem management reveals that the crashes are occurring as a result of a capacity issue.",
            "D) Business continuity management": "Incorrect – Business continuity management is concerned with the continuation of business processes during disasters."
        }
    },
    {
        "id": 21,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "An IT organization is investigating a problem in its change management process whereby many changes have to be backed out because they could not be completed or because verifications failed. Which is the best remedy for this situation?",
        "options": [
            "A) Increase the size of change windows.",
            "B) Require a separate person to verify changes.",
            "C) Require change requests to have better backout procedures.",
            "D) Require more rigorous testing in a test environment prior to scheduling changes in production."
        ],
        "correct": "D",
        "option_explanations": {
            "A) Increase the size of change windows.": "Incorrect – The problem does not appear to be one where there is insufficient time to implement changes.",
            "B) Require a separate person to verify changes.": "Incorrect – Using a different person to verify changes does not appear to be at the heart of the issue.",
            "C) Require change requests to have better backout procedures.": "Incorrect – Improved backout procedures are not likely the remedy for failed implementations.",
            "D) Require more rigorous testing in a test environment prior to scheduling changes in production.": "Correct – Repeated implementation failures should first call for more rigorous testing in a test or staging environment in order to iron out any issues that may occur when changes are applied in production environments."
        }
    },
    {
        "id": 22,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "Which language is used to change the schema in a database management system?",
        "options": [
            "A) DDL",
            "B) SQL",
            "C) Stored procedures",
            "D) JCL"
        ],
        "correct": "A",
        "option_explanations": {
            "A) DDL": "Correct – DDL, or Data Definition Language, is most commonly used to change the schema (or architecture of a database) in a database management system.",
            "B) SQL": "Incorrect – SQL is not often used to change the schema of a DBMS.",
            "C) Stored procedures": "Incorrect – Stored procedures play a different role in a database management system.",
            "D) JCL": "Incorrect – JCL is a batch control language on mainframe computers."
        }
    },
    {
        "id": 23,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "A DBA has been asked to limit the tables, rows, or columns that are visible to some users with direct database access. Which solution would best fulfill this request?",
        "options": [
            "A) Create alternative user accounts.",
            "B) Move those users into different AD groups.",
            "C) Create one or more views.",
            "D) Change the schema for those users."
        ],
        "correct": "C",
        "option_explanations": {
            "A) Create alternative user accounts.": "Incorrect – Creating alternative user accounts is not the best solution for this request.",
            "B) Move those users into different AD groups.": "Incorrect – Access permissions may not fully fulfill this request.",
            "C) Create one or more views.": "Correct – A view provides the appearance of virtual tables that are parts of real tables.",
            "D) Change the schema for those users.": "Incorrect – It's not possible to change the schema for users, other than creating one or more views."
        }
    },
    {
        "id": 24,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "An organization's IT department developed DR capabilities for some business applications prior to a BIA ever being performed. Now that a BIA has been performed, it has been determined that some IT applications' DR capabilities exceed what is called for in the BIA and that other applications fall short. What should be done to remedy this?",
        "options": [
            "A) Redo the BIA, using existing DR capabilities as inputs.",
            "B) Make no changes, as this is the expected result.",
            "C) Change IT application DR capabilities to align with the BIA.",
            "D) Change the BIA to align with IT application DR capabilities."
        ],
        "correct": "C",
        "option_explanations": {
            "A) Redo the BIA, using existing DR capabilities as inputs.": "Incorrect – The BIA does not need to be redone. It is the IT DR capabilities that require adjustment.",
            "B) Make no changes, as this is the expected result.": "Incorrect – This misalignment between the BIA and DR capabilities is not an expected result.",
            "C) Change IT application DR capabilities to align with the BIA.": "Correct – DR capabilities need to align with the results of the BIA, including established recovery objectives.",
            "D) Change the BIA to align with IT application DR capabilities.": "Incorrect – The BIA should not be changed to align with DR capabilities. It is the reverse that should be performed."
        }
    },
    {
        "id": 25,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "What is the purpose of hot-pluggable drives in a storage system?",
        "options": [
            "A) Ability to replace drives that have crashed or overheated",
            "B) Ability to replace drives while the storage system is still running",
            "C) Ability to replace drives without the risk of harm to personnel",
            "D) Ability to install additional drives without powering down the system"
        ],
        "correct": "B",
        "option_explanations": {
            "A) Ability to replace drives that have crashed or overheated": "Incorrect – This reason is too limited: while hot-pluggable drives would indeed permit personnel to replace drives that have crashed or overheated, they also permit personnel to remove and replace them for any reason.",
            "B) Ability to replace drives while the storage system is still running": "Correct – The term 'hot-pluggable drives' refers to the ability to remove and replace drives in a storage system while the system is still running. Together with RAID capabilities, there would be no interruption in the storage system's ability to read and write data to the drives.",
            "C) Ability to replace drives without the risk of harm to personnel": "Incorrect – This is not the definition of hot-pluggable drives.",
            "D) Ability to install additional drives without powering down the system": "Incorrect – This definition is too limiting: while it is true that hot-pluggable drives permit additional drives to be added to the system, they also permit faulty drives to be removed and replaced."
        }
    },
    {
        "id": 26,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "What is the primary purpose for data restoration testing?",
        "options": [
            "A) To meet regulatory requirements",
            "B) To prove that bare-metal restores can be performed",
            "C) To see how long it takes to restore data from backup",
            "D) To ensure that backups are actually being performed"
        ],
        "correct": "D",
        "option_explanations": {
            "A) To meet regulatory requirements": "Incorrect – Regulatory requirements are a minor consideration here.",
            "B) To prove that bare-metal restores can be performed": "Incorrect – Restoration testing does not necessarily test bare-metal restores.",
            "C) To see how long it takes to restore data from backup": "Incorrect – The time required to restore data is not a major consideration.",
            "D) To ensure that backups are actually being performed": "Correct – Restoration testing proves that data is actually being written to backup media. It also demonstrates that personnel know how to restore data."
        }
    },
    {
        "id": 27,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "Which of the following should approve RTO and RPO targets?",
        "options": [
            "A) Senior business executives",
            "B) Board of directors",
            "C) CISO",
            "D) CIO"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Senior business executives": "Correct – Senior business executives should approve RTO and RPO targets. As business leaders, senior executives are in the best position to decide how much downtime the organization will tolerate in the event of a minor or major disaster. Further, senior executives are going to be in the best position to fund and provide resources for IT to implement DR capabilities to meet these objectives.",
            "B) Board of directors": "Incorrect – The board of directors does not usually become involved in operational matters.",
            "C) CISO": "Incorrect – The CISO is responsible for cybersecurity, not business resilience related to disasters.",
            "D) CIO": "Incorrect – The CIO is responsible for implementing DR capabilities to support RPO and RTO targets, but does not select the targets."
        }
    },
    {
        "id": 28,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "An organization has developed its first-ever disaster recovery plan. What is the best choice for the first round of testing of the plan?",
        "options": [
            "A) Cutover test",
            "B) Walkthrough",
            "C) Simulation",
            "D) Parallel test"
        ],
        "correct": "B",
        "option_explanations": {
            "A) Cutover test": "Incorrect – A cutover test is the highest-risk test available and should be performed only after successful walkthroughs, simulations, and parallel tests.",
            "B) Walkthrough": "Correct – The best choice here is for participants to walk through the plan and discuss all of the steps in detail.",
            "C) Simulation": "Incorrect – A simulation should be performed after walkthroughs have identified improvement areas.",
            "D) Parallel test": "Incorrect – A parallel test should not be performed until at least a walkthrough and simulation have first been performed."
        }
    },
    {
        "id": 29,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "Which of the following best describes the purpose of a hypervisor?",
        "options": [
            "A) It creates and manages virtual desktops.",
            "B) It creates and manages containers.",
            "C) It installs software on virtual machines.",
            "D) It creates and manages virtual machines."
        ],
        "correct": "D",
        "option_explanations": {
            "A) It creates and manages virtual desktops.": "Incorrect – A hypervisor is not typically used to create virtual desktops.",
            "B) It creates and manages containers.": "Incorrect – A hypervisor is not used to create containers.",
            "C) It installs software on virtual machines.": "Incorrect – Hypervisors are not used to install software on virtual machines.",
            "D) It creates and manages virtual machines.": "Correct – A hypervisor, whether hosted or bare-metal, is used to create, manage, and run virtual machines."
        }
    },
    {
        "id": 30,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "Which of the following best fits the definition of a set of structured tables with indexes, primary keys, and foreign keys?",
        "options": [
            "A) Hierarchical database",
            "B) Object database",
            "C) Relational database",
            "D) Network database"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Hierarchical database": "Incorrect – A hierarchical database has a different structure than the one described.",
            "B) Object database": "Incorrect – An object database has a different structure than the one described.",
            "C) Relational database": "Correct – A relational database is one with structured tables containing rows and columns, with indexes, primary keys, and foreign keys.",
            "D) Network database": "Incorrect – A network database has a different structure than the one described."
        }
    },
    {
        "id": 31,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "An organization uses its vulnerability scanning tool as its de facto asset management system. What is the biggest risk associated with this approach?",
        "options": [
            "A) Network engineers could build new IP networks not included in the scanning tool's configuration.",
            "B) System engineers could implement new servers that the scanning tool won't see.",
            "C) System engineers could implement new virtual machines that the scanning tool won't see.",
            "D) IP source routing could prevent the scanning tool from seeing all networks."
        ],
        "correct": "A",
        "option_explanations": {
            "A) Network engineers could build new IP networks not included in the scanning tool's configuration.": "Correct – The biggest risk of using a vulnerability scanning tool as a tool for tracking assets is that these tools are generally configured to scan a list of IP networks. If a network engineer creates a new IP network and does not inform the personnel who manage the scanning tool, the tool won't detect the new IP network or any systems and devices that reside in it.",
            "B) System engineers could implement new servers that the scanning tool won't see.": "Incorrect – Vulnerability scanning tools generally scan IP networks and would generally detect new systems and devices automatically.",
            "C) System engineers could implement new virtual machines that the scanning tool won't see.": "Incorrect – New virtual machines should be detected, provided they reside on an existing IP network and are active.",
            "D) IP source routing could prevent the scanning tool from seeing all networks.": "Incorrect – IP source routing would not necessarily interfere with a vulnerability scanning tool's operation."
        }
    },
    {
        "id": 32,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "Which of the following systems should be used for populating the IT asset database in an elastic cloud environment?",
        "options": [
            "A) Hypervisor",
            "B) Vulnerability scanning tool",
            "C) Patch management tool",
            "D) CMDB"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Hypervisor": "Correct – The hypervisor is the system that manages the creation and use of virtual machines in an environment where virtual machines are created dynamically to support workload.",
            "B) Vulnerability scanning tool": "Incorrect – A vulnerability scanning tool is only going to detect virtual machines that are active during the scan.",
            "C) Patch management tool": "Incorrect – The patch management tool may not be automatically aware of new virtual machines.",
            "D) CMDB": "Incorrect – The CMDB is an IT asset database, not a tool for populating it."
        }
    },
    {
        "id": 33,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "What is a typical frequency for running a job that checks Active Directory for unused user accounts?",
        "options": [
            "A) Every hour",
            "B) Every 24 hours",
            "C) Every 7 days",
            "D) Every 90 days"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Every hour": "Incorrect – Checking for dormant user accounts every hour is excessive.",
            "B) Every 24 hours": "Incorrect – Checking for dormant user accounts every day is excessive.",
            "C) Every 7 days": "Incorrect – Checking for dormant user accounts every week is excessive.",
            "D) Every 90 days": "Correct – Ninety days is the most typical interval for checking for dormant user accounts."
        }
    },
    {
        "id": 34,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "The system interface standard that includes process control, IPC, and shared memory is known as:",
        "options": [
            "A) Unix",
            "B) POSIX",
            "C) ActiveX",
            "D) Ultrix"
        ],
        "correct": "B",
        "option_explanations": {
            "A) Unix": "Incorrect – Unix is not an interface standard, but an operating system.",
            "B) POSIX": "Correct – POSIX is the system interface standard that includes several components, such as process control, interprocess communication (IPC), named pipes, and files and file systems.",
            "C) ActiveX": "Incorrect – ActiveX does not include all of these components.",
            "D) Ultrix": "Incorrect – Ultrix is not an interface standard, but an operating system."
        }
    },
    {
        "id": 35,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "An environment consisting of centralized servers running end-user operating systems that display on users' computers is known as:",
        "options": [
            "A) Hosted hypervisor",
            "B) Bare-metal hypervisor",
            "C) Virtual desktop infrastructure",
            "D) Reverse Telnet"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Hosted hypervisor": "Incorrect – A hosted hypervisor does not match the environment description.",
            "B) Bare-metal hypervisor": "Incorrect – A bare-metal hypervisor does not match the environment description.",
            "C) Virtual desktop infrastructure": "Correct – A virtual desktop infrastructure (VDI) consists of one or more centralized servers that run end-user desktop operating systems that display on users' computers.",
            "D) Reverse Telnet": "Incorrect – Reverse Telnet does not describe the environment description."
        }
    },
    {
        "id": 36,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "A data privacy officer recently commissioned a data discovery exercise to understand the extent to which sensitive data is present on the company's world-readable file share. The exercise revealed that dozens of files containing large volumes of highly sensitive data were present on the file share. What is the best first step the data privacy officer should take?",
        "options": [
            "A) Remove all instances of files containing large volumes of highly sensitive data.",
            "B) Investigate each instance to see whether any files are a part of business processes.",
            "C) Sanction the users who placed the files there for violations of internal privacy policy.",
            "D) Do nothing, as this is an acceptable practice for files of this type."
        ],
        "correct": "B",
        "option_explanations": {
            "A) Remove all instances of files containing large volumes of highly sensitive data.": "Incorrect – Removing all files may inadvertently disrupt an existing important business process (which may need to be adjusted to avoid exposing this data).",
            "B) Investigate each instance to see whether any files are a part of business processes.": "Correct – The most prudent move is for the DPO to investigate the files that were found to better understand why they are there. Possibly, some are part of vital business processes (which, in many cases, would need to be adjusted to avoid exposing the information).",
            "C) Sanction the users who placed the files there for violations of internal privacy policy.": "Incorrect – There may be some legitimate files among those that were found.",
            "D) Do nothing, as this is an acceptable practice for files of this type.": "Incorrect – Inaction would unnecessarily expose the organization to potential privacy violations. Files containing large volumes of sensitive information probably should not be present on file shares readable by the entire organization."
        }
    },
    {
        "id": 37,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "A new IT manager is making improvements in the organization's management of unplanned outages. The IT manager has built a new process where repeated cases of similar outages are analyzed in order to identify their cause. What process has the IT manager created?",
        "options": [
            "A) Problem management",
            "B) Incident management",
            "C) Root cause analysis",
            "D) Security event management"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Problem management": "Correct – Analysis of repeated incidents is known as problem management.",
            "B) Incident management": "Incorrect – Incident management is the management of individual incidents.",
            "C) Root cause analysis": "Incorrect – While root cause analysis may be a part of the process described, the overall process is better known as problem management.",
            "D) Security event management": "Incorrect – Security event management is concerned with the response to security events and incidents."
        }
    },
    {
        "id": 38,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "A new IT manager is making improvements in the organization's management of the detailed settings on servers and network devices. The process that the IT manager has made is a part of:",
        "options": [
            "A) Vulnerability management",
            "B) System hardening",
            "C) Configuration management",
            "D) Performance management"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Vulnerability management": "Incorrect – Vulnerability management is the process of identifying and mitigating vulnerabilities on systems and devices.",
            "B) System hardening": "Incorrect – System hardening is the process of making systems more resistant to attack.",
            "C) Configuration management": "Correct – The IT manager is making improvements to the configuration management process.",
            "D) Performance management": "Incorrect – Performance management is concerned with improving the efficiency of systems."
        }
    },
    {
        "id": 39,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "A new IT manager is making improvements in the organization's management of the detailed settings on servers and network devices. The process includes the creation of a repository for storing details about this information. This repository is known as:",
        "options": [
            "A) An asset management database",
            "B) A vulnerability management database",
            "C) A configuration management database",
            "D) A system hardening standard"
        ],
        "correct": "C",
        "option_explanations": {
            "A) An asset management database": "Incorrect – An asset management database is going to contain basic information about an organization's assets.",
            "B) A vulnerability management database": "Incorrect – A vulnerability management database (which is not a common term) might contain information about vulnerabilities in systems and devices.",
            "C) A configuration management database": "Correct – A repository containing the configuration of systems is known as a configuration management database (CMDB).",
            "D) A system hardening standard": "Incorrect – A system hardening standard specifies the configuration for making systems more resistant to attack."
        }
    },
    {
        "id": 40,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "A new IT manager is making improvements to the organization's need to make its systems and devices more resilient to attacks. The IT manager should update:",
        "options": [
            "A) The vulnerability management process",
            "B) The system and device hardening standard",
            "C) The configuration management database",
            "D) The security incident response plan"
        ],
        "correct": "B",
        "option_explanations": {
            "A) The vulnerability management process": "Incorrect – A vulnerability management process is concerned with techniques used to identify and remediate vulnerabilities on systems and devices.",
            "B) The system and device hardening standard": "Correct – A system and device hardening standard specifies the configurations to be used to make systems and devices more resistant to attack.",
            "C) The configuration management database": "Incorrect – A configuration management database contains information about the configuration of systems and devices.",
            "D) The security incident response plan": "Incorrect – A security incident response plan contains procedures to follow when a security incident occurs."
        }
    },
    {
        "id": 41,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "A customer of a SaaS provider is complaining about the SaaS provider's lack of responsiveness in resolving security issues. What portion of the contract should the customer refer to when lodging a formal complaint?",
        "options": [
            "A) Service description",
            "B) System availability",
            "C) Service level agreement",
            "D) Security controls"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Service description": "Incorrect – A service description is more likely to describe services rendered, but not about resolving security issues.",
            "B) System availability": "Incorrect – This is not an issue about system availability.",
            "C) Service level agreement": "Correct – A service level agreement (SLA) defines terms of responsiveness to various types of services and service issues.",
            "D) Security controls": "Incorrect – This is not a matter of security controls, but of service levels."
        }
    },
    {
        "id": 42,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "Computer code that is found within the contents of a database is known as a:",
        "options": [
            "A) Blob",
            "B) Function",
            "C) Stored procedure",
            "D) Subroutine"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Blob": "Incorrect – A blob, or binary large object, does not typically store code, but instead is usually a video, image, or audio recording.",
            "B) Function": "Incorrect – A function is a segment of a computer program.",
            "C) Stored procedure": "Correct – A stored procedure is computer code that is stored in a database and executed when called.",
            "D) Subroutine": "Incorrect – A subroutine is a segment of a computer program."
        }
    },
    {
        "id": 43,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "An organization is starting its first-ever effort to develop a business continuity and disaster recovery plan. What is the best first step to perform in this effort?",
        "options": [
            "A) Criticality analysis",
            "B) Business impact analysis",
            "C) Setting recovery targets",
            "D) Selecting a DR site"
        ],
        "correct": "B",
        "option_explanations": {
            "A) Criticality analysis": "Incorrect – A criticality analysis is performed after the business impact analysis to determine the criticality of business processes identified in the BIA.",
            "B) Business impact analysis": "Correct – A business impact analysis (BIA) is used to enumerate business processes and their dependencies upon other processes, assets, personnel, and service providers.",
            "C) Setting recovery targets": "Incorrect – Recovery targets are established after the maximum tolerable downtime (MTD) and BIA are completed.",
            "D) Selecting a DR site": "Incorrect – A DR site is not selected until the BIA, CA, and recovery targets are established."
        }
    },
    {
        "id": 44,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "What is the purpose for connecting two redundant power supplies to separate electrical circuits?",
        "options": [
            "A) System resilience in case one electrical circuit fails",
            "B) To balance electrical load between the circuits",
            "C) To balance the phasing between the circuits",
            "D) To avoid overloading a single electrical circuit"
        ],
        "correct": "A",
        "option_explanations": {
            "A) System resilience in case one electrical circuit fails": "Correct – A system with redundant power supplies will be more resilient if the power supplies are connected to separate electrical circuits (and even more resilient if the circuits lead to separate PDUs, UPSs, electrical feeds, and generators). In the event of a failure in any of these components, the others will still supply power to the system.",
            "B) To balance electrical load between the circuits": "Incorrect – This is not a primary purpose for connecting power supplies to separate circuits.",
            "C) To balance the phasing between the circuits": "Incorrect – This is not a primary purpose for connecting power supplies to separate circuits.",
            "D) To avoid overloading a single electrical circuit": "Incorrect – Circuit loading is not usually performed using this technique."
        }
    },
    {
        "id": 45,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "An IT organization is modernizing its tape backup system by replacing its tape library system with a storage array, while keeping its tape backup software system. What has the organization implemented?",
        "options": [
            "A) E-vaulting",
            "B) S-vaulting",
            "C) Virtual tape library",
            "D) Mirroring"
        ],
        "correct": "C",
        "option_explanations": {
            "A) E-vaulting": "Incorrect – E-vaulting is the practice of sending backup data to a cloud storage provider.",
            "B) S-vaulting": "Incorrect – S-vaulting is not a valid term.",
            "C) Virtual tape library": "Correct – A virtual tape library (VTL) is a storage system that emulates a tape library system. A VTL is used when an organization wishes to retain its tape backup software platform while modernizing the actual backup storage.",
            "D) Mirroring": "Incorrect – Mirroring involves real-time duplication of data stored on a primary storage system to a secondary or tertiary storage system."
        }
    },
    {
        "id": 46,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "An IT organization is modernizing its tape backup system by sending data to a cloud storage provider. What has the organization implemented?",
        "options": [
            "A) Replication",
            "B) Mirroring",
            "C) Virtual tape library",
            "D) E-vaulting"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Replication": "Incorrect – Replication is the near-real-time copying of disk storage transactions from a primary storage system to a secondary storage system.",
            "B) Mirroring": "Incorrect – Mirroring is a block-by-block duplication of data stored on a primary storage system onto a secondary storage system.",
            "C) Virtual tape library": "Incorrect – A virtual tape library (VTL) is a disk-based storage system that emulates a tape library system.",
            "D) E-vaulting": "Correct – E-vaulting is the process of backing up data to a cloud storage provider using backup software created for that purpose."
        }
    },
    {
        "id": 47,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "A city government department that accepts payments for water use has developed a procedure to be followed when the IT application for processing payments is unavailable. What type of procedure has been developed?",
        "options": [
            "A) Business continuity plan",
            "B) Disaster recovery plan",
            "C) Business impact analysis",
            "D) Backout plan"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Business continuity plan": "Correct – The procedure developed is a business continuity plan, which is an emergency operations procedure to be followed when one or more critical assets required for the business-as-usual procedure are unavailable.",
            "B) Disaster recovery plan": "Incorrect – A disaster recovery plan is a set of procedures to be followed to assess damage and restore operation of critical assets such as IT systems and other business equipment.",
            "C) Business impact analysis": "Incorrect – A business impact analysis is a study to enumerate critical business processes and their dependencies.",
            "D) Backout plan": "Incorrect – A backout plan is a procedure in the change management process used to restore a system to its pre-changed state in the event that the change was unsuccessful."
        }
    },
    {
        "id": 48,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "A city government IT department has developed a procedure to be followed when the primary application for accepting water usage payments has been incapacitated. The procedure calls for the initiation of a secondary application in a different data center. What type of procedure has been developed?",
        "options": [
            "A) Business continuity plan",
            "B) Backout plan",
            "C) Security incident response plan",
            "D) Disaster recovery plan"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Business continuity plan": "Incorrect – A business continuity plan is a business-level procedure to be followed in the event that critical assets or personnel are unavailable to continue operations of important business processes.",
            "B) Backout plan": "Incorrect – A backout plan is a procedure in the change management process used to restore a system to its pre-changed state in the event that the change was unsuccessful.",
            "C) Security incident response plan": "Incorrect – A security incident response plan is a procedure to be followed in the event of a security incident or breach.",
            "D) Disaster recovery plan": "Correct – The procedure created is a disaster recovery plan; it involves starting a secondary application at a different data center."
        }
    },
    {
        "id": 49,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "What is the most important factor to consider in the development of a disaster recovery plan?",
        "options": [
            "A) The safety of personnel",
            "B) The availability of critical data",
            "C) Notification of civil authorities",
            "D) The continuity of critical operations"
        ],
        "correct": "A",
        "option_explanations": {
            "A) The safety of personnel": "Correct – The safety of personnel should always be the highest priority in any disaster recovery plan.",
            "B) The availability of critical data": "Incorrect – The availability of critical data, while important, is less critical than the safety of personnel.",
            "C) Notification of civil authorities": "Incorrect – The notification of civil authorities is important, but less important than the safety of personnel.",
            "D) The continuity of critical operations": "Incorrect – The continuity of critical operations is key to the resilience of the organization, but less important than the safety of personnel."
        }
    },
    {
        "id": 50,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "An SSD is most commonly used as:",
        "options": [
            "A) Backup storage",
            "B) Removable storage",
            "C) Main storage",
            "D) Secondary storage"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Backup storage": "Incorrect – SSDs are not most commonly used as backup storage.",
            "B) Removable storage": "Incorrect – SSDs are not most commonly used as removable storage.",
            "C) Main storage": "Incorrect – RAM (random access memory) is used as a system's main storage.",
            "D) Secondary storage": "Correct – Solid-state drives (SSDs) are most commonly used as secondary storage. Prior to SSDs, hard-disk drives (HDDs) were used as secondary storage."
        }
    },
    {
        "id": 51,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "The phrase \"you can't protect what you don't know about\" refers to which key IT process?",
        "options": [
            "A) Vulnerability management",
            "B) License management",
            "C) Patching",
            "D) Asset management"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Vulnerability management": "Incorrect – Vulnerability management is dependent upon sound asset management to ensure that all assets are identified and their vulnerabilities remediated timely.",
            "B) License management": "Incorrect – License management is not related to the protection of assets.",
            "C) Patching": "Incorrect – Patching is dependent upon vulnerability management and asset management.",
            "D) Asset management": "Correct – Asset management is a critical process that other processes, such as vulnerability management, patch management, and license management, depend upon. It is the author's opinion that asset management is the #1 control objective in the CIS Critical Controls for this reason."
        }
    },
    {
        "id": 52,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "The SOAP protocol is related to:",
        "options": [
            "A) The patch management process",
            "B) The exchange of data through an API",
            "C) The vulnerability management process",
            "D) Memory garbage collection"
        ],
        "correct": "B",
        "option_explanations": {
            "A) The patch management process": "Incorrect – SOAP is not related to the patch management process.",
            "B) The exchange of data through an API": "Correct – SOAP, or Simple Object Access Protocol, is a network API for exchanging data between systems over a network.",
            "C) The vulnerability management process": "Incorrect – SOAP is not related to the vulnerability management process.",
            "D) Memory garbage collection": "Incorrect – SOAP is not related to memory garbage collection."
        }
    },
    {
        "id": 53,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "Restricting USB attached storage on end-user workstations addresses all of the following except:",
        "options": [
            "A) Leakage of intellectual property",
            "B) Malware infection",
            "C) System capacity management",
            "D) Personal use of a workstation"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Leakage of intellectual property": "Incorrect – Leakage of intellectual property is often a primary reason for restricting USB attached storage on workstations.",
            "B) Malware infection": "Incorrect – Malware control is often a primary reason for restricting USB attached storage.",
            "C) System capacity management": "Correct – Restrictions of USB storage have little or nothing to do with system capacity management.",
            "D) Personal use of a workstation": "Incorrect – Personal use of a workstation is sometimes a reason for restricting the use of USB attached storage."
        }
    },
    {
        "id": 54,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "The primary purpose of a dynamic DLP system is:",
        "options": [
            "A) To detect unauthorized personal use of a workstation",
            "B) To detect unauthorized use of personal web mail",
            "C) To control unauthorized access to sensitive information",
            "D) To control unauthorized movement of sensitive information"
        ],
        "correct": "D",
        "option_explanations": {
            "A) To detect unauthorized personal use of a workstation": "Incorrect – A dynamic DLP solution is not used to detect personal use of a workstation.",
            "B) To detect unauthorized use of personal web mail": "Incorrect – A primary purpose of dynamic DLP is not to detect or block personal web mail. However, a dynamic DLP system can prevent the transmission of sensitive data via personal web mail.",
            "C) To control unauthorized access to sensitive information": "Incorrect – System access controls are more commonly used to prevent unauthorized access to sensitive information.",
            "D) To control unauthorized movement of sensitive information": "Correct – The main purpose of dynamic DLP (data loss prevention) is the unauthorized movement of sensitive information. For example, a dynamic DLP solution can prevent sensitive information from being stored on an external USB attached storage device or transmitted through e-mail."
        }
    },
    {
        "id": 55,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "What is the suitability for the use of a SIEM to alert personnel of system capacity and performance issues?",
        "options": [
            "A) If syslog events are generated, use cases related to performance and capacity can be developed.",
            "B) A SIEM can only be used to alert personnel of security events.",
            "C) Use cases for non-security-related events do not function on a SIEM.",
            "D) Alerts for non-security-related events do not function on a SIEM."
        ],
        "correct": "A",
        "option_explanations": {
            "A) If syslog events are generated, use cases related to performance and capacity can be developed.": "Correct – A SIEM is a general-purpose system used to ingest log data from systems and devices and to create alerts when specific types of log entries are received. There is no limit to the types of log data and alerts that can be employed in a SIEM.",
            "B) A SIEM can only be used to alert personnel of security events.": "Incorrect – A SIEM can be used for security and non-security events.",
            "C) Use cases for non-security-related events do not function on a SIEM.": "Incorrect – A SIEM can handle non-security events.",
            "D) Alerts for non-security-related events do not function on a SIEM.": "Incorrect – A SIEM can generate alerts for any type of event."
        }
    },
    {
        "id": 56,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "After analyzing events and incidents from the past year, an analyst has declared the existence of a problem. To what is the analyst referring?",
        "options": [
            "A) One or more controls are in a state of failure.",
            "B) The analyst is unable to access all incident data for the entire year.",
            "C) One or more high-criticality incidents have occurred.",
            "D) A specific type of incident is recurring."
        ],
        "correct": "D",
        "option_explanations": {
            "A) One or more controls are in a state of failure.": "Incorrect – A problem, in ITIL terminology, does not specifically indicate a control failure.",
            "B) The analyst is unable to access all incident data for the entire year.": "Incorrect – A problem, in ITIL terminology, does not indicate an inability to access historical event data.",
            "C) One or more high-criticality incidents have occurred.": "Incorrect – A problem in ITIL terminology does not indicate the severity of incidents that are occurring.",
            "D) A specific type of incident is recurring.": "Correct – In ITIL terminology, a problem is an incident that keeps occurring. This means that there is some root cause for these incidents that needs to be investigated."
        }
    },
    {
        "id": 57,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "A DBA has determined that it is not feasible to directly back up a large database. What is the best remedy for this?",
        "options": [
            "A) Defragment the database to permit a linear backup.",
            "B) Change the database to read-only during a backup to preserve integrity.",
            "C) Compress the database to recover free space.",
            "D) Export the database to a flat file and back up the flat file."
        ],
        "correct": "D",
        "option_explanations": {
            "A) Defragment the database to permit a linear backup.": "Incorrect – Defragmentation of a database is not a common operation.",
            "B) Change the database to read-only during a backup to preserve integrity.": "Incorrect – Changing a database to read-only would certainly disrupt business operations.",
            "C) Compress the database to recover free space.": "Incorrect – Compression of a database is not a common practice.",
            "D) Export the database to a flat file and back up the flat file.": "Correct – The best remedy when a database cannot be directly backed up is the creation of an export, which itself can be backed up."
        }
    },
    {
        "id": 58,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "What is the feasibility for using the results of a BIA in the creation of a system classification plan?",
        "options": [
            "A) A BIA will indicate sensitivity of specific data that is associated with critical business processes.",
            "B) A BIA will indicate operational criticality of specific data that is associated with critical business processes.",
            "C) A BIA does not correlate to specific information systems.",
            "D) A BIA does not correlate to specific data sets."
        ],
        "correct": "B",
        "option_explanations": {
            "A) A BIA will indicate sensitivity of specific data that is associated with critical business processes.": "Incorrect – A BIA does not typically identify data by sensitivity, but instead identifies data by operational criticality.",
            "B) A BIA will indicate operational criticality of specific data that is associated with critical business processes.": "Correct – A BIA identifies critical business processes in an organization, including the organization's dependencies upon IT systems and their data sets. Critical processes can be mapped to the systems they depend upon, which can contribute to system classification.",
            "C) A BIA does not correlate to specific information systems.": "Incorrect – A BIA does in fact correlate business processes to information systems.",
            "D) A BIA does not correlate to specific data sets.": "Incorrect – A BIA does in fact correlate business processes to specific data sets."
        }
    },
    {
        "id": 59,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "A system engineer is reviewing critical systems in a data center and mapping them to individual electrical circuits. The engineer identified a system with two power supplies that are connected to the same plug strip. What should the engineer conclude from this?",
        "options": [
            "A) It is an acceptable practice to connect both power supplies to the same circuit.",
            "B) It is an acceptable practice to connect both power supplies to the same plug strip.",
            "C) The two power supplies should not be connected to the same circuit.",
            "D) The two power supplies should not be connected to the same plug strip."
        ],
        "correct": "C",
        "option_explanations": {
            "A) It is an acceptable practice to connect both power supplies to the same circuit.": "Incorrect – It is not a recommended practice to connect both power supplies to the same plug strip or the same circuit.",
            "B) It is an acceptable practice to connect both power supplies to the same plug strip.": "Incorrect – The plug strip and electrical circuit represent a single failure path, somewhat negating the purpose of multiple power supplies.",
            "C) The two power supplies should not be connected to the same circuit.": "Correct – The main issue at stake here is that the power supplies are both connected to the same electrical circuit. If the electrical circuit fails, the system will be powered down. A better practice is to connect the two power supplies to separate circuits.",
            "D) The two power supplies should not be connected to the same plug strip.": "Incorrect – The bigger issue is not whether the power supplies are connected to the same plug strip, but that they are connected to the same circuit."
        }
    },
    {
        "id": 60,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "An IT architect is proposing a plan for improving the resilience of critical data in the organization. The architect proposes that applications be altered so that they confirm that transactions have been successfully written to two different storage systems. What scheme has been proposed?",
        "options": [
            "A) Journaling",
            "B) Mirroring",
            "C) Data replication",
            "D) Two-phase commit"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Journaling": "Incorrect – Journaling is the process of recording storage transactions in another part of a file system for redundancy and integrity purposes.",
            "B) Mirroring": "Incorrect – Mirroring is a storage system function that applications are unaware of.",
            "C) Data replication": "Incorrect – Data replication is a storage system function that applications are unaware of.",
            "D) Two-phase commit": "Correct – Two-phase commit is the act of writing a transaction to separate storage systems and not completing the transaction until confirmation of successful write operations has been received."
        }
    },
    {
        "id": 61,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "A department has completed a review of its business continuity plan through a moderated discussion that followed a specific, scripted disaster scenario. What kind of a review was performed?",
        "options": [
            "A) Walkthrough",
            "B) Simulation",
            "C) Parallel test",
            "D) Peer review"
        ],
        "correct": "B",
        "option_explanations": {
            "A) Walkthrough": "Incorrect – A walkthrough does not attempt to simulate a disaster scenario.",
            "B) Simulation": "Correct – A simulation is a type of review where a moderator reveals a realistic scenario, and test participants talk through the steps they would be taking should an actual disaster of this type be occurring. A simulation is more realistic than a walkthrough, as it helps to bring a disaster to life.",
            "C) Parallel test": "Incorrect – A parallel test involves the actual deployment of business continuity procedures to see whether they can be operated properly.",
            "D) Peer review": "Incorrect – A peer review involves other personnel, possibly those in another organization."
        }
    },
    {
        "id": 62,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "What is the purpose of salvage operations in a disaster recovery plan?",
        "options": [
            "A) To identify the damage to, and recoverability of, critical equipment and assets",
            "B) To determine the scrap value of critical equipment and assets",
            "C) To ensure that all personnel are accounted for",
            "D) To identify business processes that can be resumed"
        ],
        "correct": "A",
        "option_explanations": {
            "A) To identify the damage to, and recoverability of, critical equipment and assets": "Correct – The primary purpose of salvage is to determine the extent of damage of critical business equipment and to determine what is still functional, which assets can be repaired, and which are damaged beyond repair.",
            "B) To determine the scrap value of critical equipment and assets": "Incorrect – Determining scrap value is a secondary purpose; the primary purpose is to assess damage and recoverability.",
            "C) To ensure that all personnel are accounted for": "Incorrect – The purpose of salvage is related to business equipment, not personnel.",
            "D) To identify business processes that can be resumed": "Incorrect – The purpose of salvage is related to business equipment, not business processes."
        }
    },
    {
        "id": 63,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "RAM is most commonly used as:",
        "options": [
            "A) Secondary storage",
            "B) Main storage",
            "C) Virtual disk",
            "D) CPU instruction cache"
        ],
        "correct": "B",
        "option_explanations": {
            "A) Secondary storage": "Incorrect – SSDs and HDDs are most commonly used for secondary storage.",
            "B) Main storage": "Correct – RAM, or random access memory, is the primary technology used for a computer's main storage.",
            "C) Virtual disk": "Incorrect – A virtual disk is a secondary use of RAM, not a primary use.",
            "D) CPU instruction cache": "Incorrect – A CPU has its own instruction cache built in."
        }
    },
    {
        "id": 64,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "All of the following are valid reasons for removing end users' local administrators privileges on their workstations except:",
        "options": [
            "A) To reduce malware attack impact",
            "B) To prevent the use of personal web mail",
            "C) To prevent installation of unauthorized software",
            "D) To reduce the number of service desk support calls"
        ],
        "correct": "B",
        "option_explanations": {
            "A) To reduce malware attack impact": "Incorrect – This is a valid reason.",
            "B) To prevent the use of personal web mail": "Correct – Removing local administrator access from an end user would not impact a user's ability to access personal web mail in most cases.",
            "C) To prevent installation of unauthorized software": "Incorrect – This is a valid reason.",
            "D) To reduce the number of service desk support calls": "Incorrect – This is a valid reason."
        }
    },
    {
        "id": 65,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "The primary mission of data governance is:",
        "options": [
            "A) To ensure the availability of sensitive and critical information",
            "B) To ensure the integrity of sensitive and critical information",
            "C) To control and monitor all uses of sensitive or critical information",
            "D) To ensure compliance with applicable privacy laws"
        ],
        "correct": "C",
        "option_explanations": {
            "A) To ensure the availability of sensitive and critical information": "Incorrect – Data governance is not primarily concerned with the availability of information.",
            "B) To ensure the integrity of sensitive and critical information": "Incorrect – Data governance is not primarily concerned with the integrity of information.",
            "C) To control and monitor all uses of sensitive or critical information": "Correct – The primary mission of data governance is the control and monitoring of all uses of sensitive and/or critical information in an organization, both in structured and unstructured storage.",
            "D) To ensure compliance with applicable privacy laws": "Incorrect – Compliance with applicable laws should be an outcome of data governance, but not its main purpose."
        }
    },
    {
        "id": 66,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "Many of the backout plans in the records of a change control process simply read, \"Reverse previous steps.\" What conclusion can be drawn from this?",
        "options": [
            "A) Backout plans are only relevant for emergency changes.",
            "B) Backout plans are not a part of a change management process.",
            "C) Backout plans are adequate.",
            "D) Backout plans are not as rigorous as they should be."
        ],
        "correct": "D",
        "option_explanations": {
            "A) Backout plans are only relevant for emergency changes.": "Incorrect – Backout plans are needed for all changes.",
            "B) Backout plans are not a part of a change management process.": "Incorrect – Backout plans are a key part of a change management process.",
            "C) Backout plans are adequate.": "Incorrect – A backout plan that states simply \"reverse previous steps\" is not adequate.",
            "D) Backout plans are not as rigorous as they should be.": "Correct – \"Reverse previous steps\" is wholly inadequate for most changes, as this represents unpreparedness for situations where changes are unsuccessful."
        }
    },
    {
        "id": 67,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "The purpose of a business impact analysis (BIA) is primarily:",
        "options": [
            "A) To calculate risk in a risk assessment",
            "B) To determine the impact of a breach",
            "C) To determine process criticalities",
            "D) To determine process dependencies"
        ],
        "correct": "D",
        "option_explanations": {
            "A) To calculate risk in a risk assessment": "Incorrect – A BIA is not used in a general risk assessment.",
            "B) To determine the impact of a breach": "Incorrect – A BIA is not used in a breach assessment.",
            "C) To determine process criticalities": "Incorrect – It is the criticality assessment (CA) that is used to determine process criticality, once the BIA itself has been completed.",
            "D) To determine process dependencies": "Correct – The purpose of business impact analysis (BIA) is to determine the dependencies of business processes—what assets, staff, and outside parties are required to sustain a process."
        }
    },
    {
        "id": 68,
        "domain": "Domain 4 – IT Service Management and Continuity",
        "question": "The purpose for pre-writing public statements describing the impact, response, and recovery from a disaster include all of the following except:",
        "options": [
            "A) During a disaster is not a good time to write such statements from scratch.",
            "B) Key personnel who would write such statements may not be available.",
            "C) Such public statements can be issued more quickly.",
            "D) Pre-written public statements are required by regulation."
        ],
        "correct": "D",
        "option_explanations": {
            "A) During a disaster is not a good time to write such statements from scratch.": "Incorrect – This is one of the advantages of pre-writing statements.",
            "B) Key personnel who would write such statements may not be available.": "Incorrect – This is an advantage of pre-writing.",
            "C) Such public statements can be issued more quickly.": "Incorrect – This is an advantage.",
            "D) Pre-written public statements are required by regulation.": "Correct – Few, if any, regulations require organizations to pre-write their public statements describing a disaster and the details about impact, response, and recovery."
        }
    },
    # Domain 5 – Information Asset Protection
    {
        "id": 1,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "A new information security manager has examined the systems in the production environment and has found that their security-related configurations are inadequate and inconsistent. To improve this situation, the security manager should create a:",
        "options": [
            "A) Jump server",
            "B) Firewall rule",
            "C) Hardening standard",
            "D) CMDB"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Jump server": "Incorrect – A jump server will not address this situation.",
            "B) Firewall rule": "Incorrect – Firewall rules will not adequately address this situation.",
            "C) Hardening standard": "Correct – A hardening standard will define the security-related configurations applicable to information systems and devices. Note that automation may also need to be implemented if there are large numbers of servers.",
            "D) CMDB": "Incorrect – A CMDB may already exist in this situation; regardless, it is the strong and consistent configuration of servers that is necessary. A CMDB will assist in the management of server configuration."
        }
    },
    {
        "id": 2,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "Which U.S. government agency enforces retail organizations' information privacy policy?",
        "options": [
            "A) National Institute of Standards and Technology",
            "B) Federal Trade Commission",
            "C) Office of Civil Rights",
            "D) United States Secret Service"
        ],
        "correct": "B",
        "option_explanations": {
            "A) National Institute of Standards and Technology": "Incorrect – NIST develops standards and guidelines but does not perform enforcement.",
            "B) Federal Trade Commission": "Correct – The FTC has historically been enforcing retail organizations' information privacy policy and has brought legal suit against organizations knowingly violating these policies.",
            "C) Office of Civil Rights": "Incorrect – The OCR enforces HIPAA and related laws in the healthcare industry.",
            "D) United States Secret Service": "Incorrect – The USSS protects U.S. currency as well as the president."
        }
    },
    {
        "id": 3,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "While useful for detecting fires, what is one known problem associated with the use of smoke detectors under a raised computer room floor?",
        "options": [
            "A) False alarms due to the accumulation of dust",
            "B) Higher cost of maintenance",
            "C) Lack of visual reference",
            "D) Lower sensitivity due to stagnant air"
        ],
        "correct": "A",
        "option_explanations": {
            "A) False alarms due to the accumulation of dust": "Correct – Dust can accumulate under the raised floor in a computer room environment. Changes in airflow can cause the dust to circulate in the air, causing false-positive smoke detection.",
            "B) Higher cost of maintenance": "Incorrect – There is no difference in maintenance costs for smoke detectors above or below a raised floor.",
            "C) Lack of visual reference": "Incorrect – It is not necessary for personnel to be able to see smoke detectors below a raised floor.",
            "D) Lower sensitivity due to stagnant air": "Incorrect – The air under a raised floor is not stagnant, but instead serves as a plenum for cooling and air circulation."
        }
    },
    {
        "id": 4,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "An organization is seeking to establish a protocol standard for federated authentication. Which of the following protocols is least likely to be selected?",
        "options": [
            "A) OAuth",
            "B) SAML",
            "C) SOAP",
            "D) HMAC"
        ],
        "correct": "C",
        "option_explanations": {
            "A) OAuth": "Incorrect – OAuth is a protocol found in federated authentication.",
            "B) SAML": "Incorrect – SAML is a protocol found in federated authentication.",
            "C) SOAP": "Correct – SOAP is a protocol used for distributed object instantiation and communication.",
            "D) HMAC": "Incorrect – HMAC is a protocol found in federated authentication. HMAC has fallen out of common use."
        }
    },
    {
        "id": 5,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "What is one distinct disadvantage of the use of on-premises web content filtering?",
        "options": [
            "A) End users can no longer inspect URLs in e-mail messages.",
            "B) End users can easily circumvent it with a local IPS.",
            "C) Mobile devices are unprotected when off-network.",
            "D) It is labor intensive to manage exceptions."
        ],
        "correct": "C",
        "option_explanations": {
            "A) End users can no longer inspect URLs in e-mail messages.": "Incorrect – Web content filtering systems do not interact with the content of e-mail messages.",
            "B) End users can easily circumvent it with a local IPS.": "Incorrect – Users would not be able to circumvent web content filtering with a local IPS; on the contrary, a local IPS would further improve endpoint security, particularly when off-network.",
            "C) Mobile devices are unprotected when off-network.": "Correct – On-premises web content filtering protects devices on the internal network, as well as remote devices when they have established VPNs without split tunneling. Mobile devices connected to the Internet without VPN receive no protection from on-premises web content filtering systems.",
            "D) It is labor intensive to manage exceptions.": "Incorrect – The management of rule exceptions is not necessarily a problem."
        }
    },
    {
        "id": 6,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "What is the purpose of data classification?",
        "options": [
            "A) To establish rules for data protection and use",
            "B) To discover sensitive data on unstructured shares",
            "C) To enforce file access rules",
            "D) To gather statistics on data usage"
        ],
        "correct": "A",
        "option_explanations": {
            "A) To establish rules for data protection and use": "Correct – The purpose of a data classification program is to define the classes, or categories, of data and define usage guidelines for data at each classification level. This helps personnel to understand and follow handling guidelines, which results in improved data protection.",
            "B) To discover sensitive data on unstructured shares": "Incorrect – Data classification is not used in data discovery.",
            "C) To enforce file access rules": "Incorrect – Data classification does not directly contribute to the enforcement of file access rules. Data classification, however, may state what file access rules should be.",
            "D) To gather statistics on data usage": "Incorrect – Data classification does not contribute to data usage statistics."
        }
    },
    {
        "id": 7,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "Blockchain is best described as:",
        "options": [
            "A) A cryptographic algorithm",
            "B) A data confidentiality technique using cryptography",
            "C) A popular cryptocurrency",
            "D) A list of records that are linked using cryptography"
        ],
        "correct": "D",
        "option_explanations": {
            "A) A cryptographic algorithm": "Incorrect – Blockchain is not a cryptographic algorithm; blockchain uses crypto algorithms, however.",
            "B) A data confidentiality technique using cryptography": "Incorrect – Blockchain does not protect the confidentiality of data.",
            "C) A popular cryptocurrency": "Incorrect – Blockchain is not a cryptocurrency.",
            "D) A list of records that are linked using cryptography": "Correct – A blockchain is a series of records that are linked using cryptography. Specifically, each successive record in a blockchain contains a hash of the previous record; this makes data in a blockchain resistant to alteration."
        }
    },
    {
        "id": 8,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "The private keys for a well-known web site have been compromised. What is the best approach for resolving this matter?",
        "options": [
            "A) Change the IP address of the web server.",
            "B) Add an entry to a CRL for the web site's SSL keys.",
            "C) Recompile the web site's application.",
            "D) Reboot the web server."
        ],
        "correct": "B",
        "option_explanations": {
            "A) Change the IP address of the web server.": "Incorrect – Changing the IP address does not address the compromised keys.",
            "B) Add an entry to a CRL for the web site's SSL keys.": "Correct – Adding an entry to the certificate revocation list (CRL) is the most effective solution. The certificate authority (CA) that issued the original SSL keys would perform this action. Subsequent attempts to connect with the compromised keys would be unsuccessful—at least for all software that checks the CRL first.",
            "C) Recompile the web site's application.": "Incorrect – Recompiling does not affect the compromised SSL keys.",
            "D) Reboot the web server.": "Incorrect – Rebooting does not revoke the compromised keys."
        }
    },
    {
        "id": 9,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "A web application stores unique codes on each user's system in order to track the activities of each visitor. What is a common term for these codes?",
        "options": [
            "A) Http-only cookie",
            "B) Super cookie",
            "C) Session cookie",
            "D) Persistent cookie"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Http-only cookie": "Incorrect – An http-only cookie is one that cannot be read by client-side software such as JavaScript.",
            "B) Super cookie": "Incorrect – A super cookie is one issued by a top-level domain such as .com.",
            "C) Session cookie": "Correct – A session cookie is used to uniquely identify each visitor to a web site and is used to manage user sessions.",
            "D) Persistent cookie": "Incorrect – A persistent cookie is used to store user preferences such as language and time zone."
        }
    },
    {
        "id": 10,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "The term \"virtual memory\" refers to what mechanism?",
        "options": [
            "A) The main storage allocated to a guest of a hypervisor",
            "B) Memory management that isolates running processes",
            "C) Memory that is shared between guests of a hypervisor",
            "D) Main storage space that exceeds physical memory and is extended to secondary storage"
        ],
        "correct": "D",
        "option_explanations": {
            "A) The main storage allocated to a guest of a hypervisor": "Incorrect – Virtual memory is not specifically about hypervisor memory allocation.",
            "B) Memory management that isolates running processes": "Incorrect – That describes process isolation, not virtual memory.",
            "C) Memory that is shared between guests of a hypervisor": "Incorrect – That is shared memory, not virtual memory.",
            "D) Main storage space that exceeds physical memory and is extended to secondary storage": "Correct – Virtual memory is the technique of creating memory space that exceeds the physical main memory of a system; memory is extended onto secondary storage."
        }
    },
    {
        "id": 11,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "What is the effect of suppressing the broadcast of SSID?",
        "options": [
            "A) Network is not listed, but no difference in security.",
            "B) Only registered users are able to connect.",
            "C) Stronger (AES vs. TKIP) cryptography.",
            "D) Administrators can track users more easily."
        ],
        "correct": "A",
        "option_explanations": {
            "A) Network is not listed, but no difference in security.": "Correct – Suppressing the broadcast of SSID in a Wi-Fi network makes no difference in terms of the security of the network. Some believe that suppressing SSID is better for security, but there are numerous tools available that show all available networks, whether they are broadcasting SSID or not.",
            "B) Only registered users are able to connect.": "Incorrect – Suppressing SSID broadcast has no effect on the users who are able to connect.",
            "C) Stronger (AES vs. TKIP) cryptography.": "Incorrect – Suppressing SSID broadcast is not related to the selection of cryptography.",
            "D) Administrators can track users more easily.": "Incorrect – Suppressing SSID broadcast does not affect administration or monitoring of the Wi-Fi network."
        }
    },
    {
        "id": 12,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "What is the purpose of recordkeeping in a security awareness training program?",
        "options": [
            "A) It prevents users from repeating the training.",
            "B) Compliance with training provider licensing requirements.",
            "C) Recordkeeping is required by ISO 27001.",
            "D) Users cannot later claim no knowledge of content if they violate policy."
        ],
        "correct": "D",
        "option_explanations": {
            "A) It prevents users from repeating the training.": "Incorrect – An organization would not normally deny a user from repeating security awareness training.",
            "B) Compliance with training provider licensing requirements.": "Incorrect – License requirements are enforced through access controls.",
            "C) Recordkeeping is required by ISO 27001.": "Incorrect – Recordkeeping is not necessarily required by ISO 27001.",
            "D) Users cannot later claim no knowledge of content if they violate policy.": "Correct – When a user completes security awareness training and there is evidence of this completion in business records, the user cannot easily refute knowledge of the training content if they later are found to violate policy. Competency quizzes as a part of security awareness training helps even more in this regard."
        }
    },
    {
        "id": 13,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "An attack technique in which an attacker attempts to place arbitrary code into the instruction space of a running process is known as:",
        "options": [
            "A) Cross-site scripting",
            "B) A time-of-check to time-of-use attack",
            "C) A buffer overflow attack",
            "D) A race condition"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Cross-site scripting": "Incorrect – A cross-site scripting attack does not overwrite code in the instruction space of a running program, but instead is a technique where the attacker attempts to place client-side scripts into web pages so that a user's browser will execute the attacker's code.",
            "B) A time-of-check to time-of-use attack": "Incorrect – A TOC/TOU attack exploits a timing window, not code injection.",
            "C) A buffer overflow attack": "Correct – A buffer overflow attack is a technique where the attacker attempts to overflow a running program's input buffer, resulting in arbitrary code overwriting other instructions in the program. Successful exploitation of a buffer overflow vulnerability gives the attacker complete control over the target program.",
            "D) A race condition": "Incorrect – A race condition is another term for TOC/TOU, not a direct code injection."
        }
    },
    {
        "id": 14,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "A security analyst who is troubleshooting a security issue has asked another engineer to obtain a PCAP file associated with a given user's workstation. What is the security analyst asking for?",
        "options": [
            "A) A copy of the workstation's registry file",
            "B) A copy of the network traffic to and from the workstation",
            "C) An image of the workstation's main memory (RAM)",
            "D) An image of the workstation's secondary memory (hard drive)"
        ],
        "correct": "B",
        "option_explanations": {
            "A) A copy of the workstation's registry file": "Incorrect – A PCAP is not a copy of the workstation's registry file.",
            "B) A copy of the network traffic to and from the workstation": "Correct – A PCAP (packet capture) file is a file containing a copy of network traffic associated with one or more devices on a network.",
            "C) An image of the workstation's main memory (RAM)": "Incorrect – A PCAP is not an image of memory.",
            "D) An image of the workstation's secondary memory (hard drive)": "Incorrect – A PCAP is not a disk image."
        }
    },
    {
        "id": 15,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "A development lab employs a syslog server for security and troubleshooting issues. The information security office has recently implemented a SIEM and has directed that all log data be sent to the SIEM. How can the development lab continue to employ its local syslog server while complying with this request?",
        "options": [
            "A) Build a proxy server that will clone the log data.",
            "B) The development lab will have to shut down its syslog server.",
            "C) Export syslog data every hour and send it to the SIEM.",
            "D) Direct servers to send their syslog data to the local server and to the SIEM."
        ],
        "correct": "D",
        "option_explanations": {
            "A) Build a proxy server that will clone the log data.": "Incorrect – A proxy server is unnecessary, as systems and devices can send syslog data to multiple destinations.",
            "B) The development lab will have to shut down its syslog server.": "Incorrect – The lab can continue using its syslog server and comply by configuring dual destinations.",
            "C) Export syslog data every hour and send it to the SIEM.": "Incorrect – Exporting and forwarding is unnecessary since systems can send to multiple destinations directly.",
            "D) Direct servers to send their syslog data to the local server and to the SIEM.": "Correct – Servers and devices can send syslog data to multiple destinations."
        }
    },
    {
        "id": 16,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "The best time to assign roles and responsibilities for computer security incident response is:",
        "options": [
            "A) During training",
            "B) During tabletop testing",
            "C) While responding to an incident",
            "D) While writing the incident response plan"
        ],
        "correct": "D",
        "option_explanations": {
            "A) During training": "Incorrect – Responsible parties should be established well before training, in the plan development stage.",
            "B) During tabletop testing": "Incorrect – Should be established well before tabletop testing.",
            "C) While responding to an incident": "Incorrect – Roles and responsibilities should be established before an incident actually occurs.",
            "D) While writing the incident response plan": "Correct – The best time to establish and assign roles and responsibilities is at the time of incident response plan development."
        }
    },
    {
        "id": 17,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "Chain of custody is employed in which business process?",
        "options": [
            "A) Internal investigation",
            "B) Asset management",
            "C) Access management",
            "D) Penetration testing"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Internal investigation": "Correct – Chain of custody is employed whenever there is an investigation, including forensics and security incidents, where evidence needs to be collected and retained for later legal proceedings.",
            "B) Asset management": "Incorrect – Chain of custody is not used in asset or access management processes.",
            "C) Access management": "Incorrect – Chain of custody is not used in access management.",
            "D) Penetration testing": "Incorrect – Chain of custody is not used in penetration tests."
        }
    },
    {
        "id": 18,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "Canada's ITSG-33 is a similar to which standard?",
        "options": [
            "A) SSAE18",
            "B) HIPAA",
            "C) NIST SP800-53",
            "D) ISO/IEC 27001"
        ],
        "correct": "C",
        "option_explanations": {
            "A) SSAE18": "Incorrect – ITSG-33 is not similar to SSAE18.",
            "B) HIPAA": "Incorrect – ITSG-33 is not similar to HIPAA.",
            "C) NIST SP800-53": "Correct – Canada's ITSG-33 is nearly a clone of the U.S. standard NIST SP800-53.",
            "D) ISO/IEC 27001": "Incorrect – ITSG-33 is not similar to ISO/IEC 27001."
        }
    },
    {
        "id": 19,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "The process of ensuring proper protection and use of PII is known as:",
        "options": [
            "A) Security",
            "B) Privacy",
            "C) Data loss prevention",
            "D) Data discovery"
        ],
        "correct": "B",
        "option_explanations": {
            "A) Security": "Incorrect – Security is primarily concerned only with the protection of PII, but not with its use.",
            "B) Privacy": "Correct – Privacy is primarily concerned with the protection of PII (personally identifiable information), as well as its uses in and by an organization.",
            "C) Data loss prevention": "Incorrect – DLP is mainly concerned with the use of PII and other sensitive information such as intellectual property.",
            "D) Data discovery": "Incorrect – Data discovery is the process of examining storage systems to determine the nature of the data that resides there."
        }
    },
    {
        "id": 20,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "A CIO is investigating the prospect of a hosting center for its IT infrastructure. A specific hosting center claims to have \"N + 1\" HVAC Systems. What is meant by this term?",
        "options": [
            "A) The hosting center has one more HVAC system than is necessary for adequate cooling.",
            "B) The hosting center has the \"N + 1\" brand of HVAC systems designed for hosting centers.",
            "C) The hosting center has recently installed a new HVAC system.",
            "D) The hosting center HVAC systems meet the \"N + 1\" reliability standard."
        ],
        "correct": "A",
        "option_explanations": {
            "A) The hosting center has one more HVAC system than is necessary for adequate cooling.": "Correct – N+1 refers to any of several critical systems, including incoming power, HVAC, and Internet connectivity, where at least one additional component is available so that the failure of one component will not interrupt hosting center services.",
            "B) The hosting center has the \"N + 1\" brand of HVAC systems designed for hosting centers.": "Incorrect – N+1 is not an HVAC brand, but an expression of resilience.",
            "C) The hosting center has recently installed a new HVAC system.": "Incorrect – N+1 is an expression of resilience through redundancy.",
            "D) The hosting center HVAC systems meet the \"N + 1\" reliability standard.": "Incorrect – N+1 is an expression of resilience through the number of components in use, generally one more than is necessary to sustain operations."
        }
    },
    {
        "id": 21,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "An organization has updated its identity and access management infrastructure so that users use their AD credentials to log in to the network as well as internal business applications. What has the organization implemented?",
        "options": [
            "A) Credential vaulting",
            "B) Single sign-on",
            "C) Federated identity",
            "D) Reduced sign-on"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Credential vaulting": "Incorrect – Credential vaulting is a technique of storing login credentials in an encrypted repository.",
            "B) Single sign-on": "Incorrect – SSO permits a user to log in once to an environment containing multiple applications and systems. The logged-in state is known to systems and applications that are part of the SSO environment.",
            "C) Federated identity": "Incorrect – Federated identity permits users to authenticate to systems in participating organizations.",
            "D) Reduced sign-on": "Correct – Reduced sign-on is the result of integrating a central identity store such as Active Directory (AD) with applications and networks. The term refers to the reduction in the numbers of login credentials users need to access networks and systems."
        }
    },
    {
        "id": 22,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "The primary advantage of a firewall on a laptop computer is:",
        "options": [
            "A) Laptop computers are protected when outside the enterprise network.",
            "B) End users have more control over their network security.",
            "C) Improved performance of enterprise network firewalls.",
            "D) Redundancy in the event the enterprise firewall is overloaded."
        ],
        "correct": "A",
        "option_explanations": {
            "A) Laptop computers are protected when outside the enterprise network.": "Correct – The firewall on a laptop computer will provide some network protection in cases where the laptop is connected to the Internet at a location outside of the enterprise and its firewalls.",
            "B) End users have more control over their network security.": "Incorrect – End users should not be able to configure the firewalls on their workstations.",
            "C) Improved performance of enterprise network firewalls.": "Incorrect – Laptop firewalls will not affect the performance of enterprise firewalls.",
            "D) Redundancy in the event the enterprise firewall is overloaded.": "Incorrect – Laptop firewalls do not serve as a redundancy for enterprise firewalls."
        }
    },
    {
        "id": 23,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "An organization's data classification policy includes guidelines for placing footers with specific language in documents and presentations. What activity does this refer to?",
        "options": [
            "A) Digital signatures",
            "B) Digital envelopes",
            "C) Document marking",
            "D) Document tagging"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Digital signatures": "Incorrect – Digital signatures cryptographically sign a document to ensure authenticity and integrity.",
            "B) Digital envelopes": "Incorrect – Digital envelopes encapsulate encryption keys.",
            "C) Document marking": "Correct – Document marking is the process of placing human-readable text in a document that advises a reader of its sensitivity.",
            "D) Document tagging": "Incorrect – Document tagging is used to place machine-readable tags on documents for use by automated systems."
        }
    },
    {
        "id": 24,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "What technique does PGP use to permit multiple users to read an encrypted document?",
        "options": [
            "A) Key fingerprints",
            "B) Symmetric cryptography",
            "C) Digital envelope",
            "D) Digital signature"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Key fingerprints": "Incorrect – Key fingerprints are used to verify a user's public key.",
            "B) Symmetric cryptography": "Incorrect – Symmetric cryptography, while used at the core of PGP to encrypt and decrypt files, does not itself facilitate access by multiple users.",
            "C) Digital envelope": "Correct – PGP uses a digital envelope to encapsulate multiple public keys that permits multiple users to read an encrypted document.",
            "D) Digital signature": "Incorrect – A digital signature is used to verify the authenticity and integrity of a document."
        }
    },
    {
        "id": 25,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "What feature permits enterprise users of Microsoft Outlook to digitally sign e-mail messages?",
        "options": [
            "A) PGP",
            "B) AD PKI",
            "C) Local administrative privileges",
            "D) Password vaulting"
        ],
        "correct": "B",
        "option_explanations": {
            "A) PGP": "Incorrect – PGP is not commonly used any more for this purpose.",
            "B) AD PKI": "Correct – The PKI capabilities in Active Directory facilitate the use of digital signatures, and encryption, of e-mail messages in Outlook.",
            "C) Local administrative privileges": "Incorrect – Local administrative privileges do not directly facilitate the use of digital signatures in e-mail. While a local administrator may be able to generate a keypair locally, a recipient of a digitally signed or encrypted message would probably not be able to verify or decrypt it.",
            "D) Password vaulting": "Incorrect – Password vaulting is used to protect passwords."
        }
    },
    {
        "id": 26,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "A URL starting with https:// signifies what technology?",
        "options": [
            "A) Self-signed content",
            "B) Encryption with 3DES",
            "C) Encryption with SSL or TLS",
            "D) SET, or Secure Electronic Transaction"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Self-signed content": "Incorrect – https does not signify the use of self-signed content.",
            "B) Encryption with 3DES": "Incorrect – https does not determine the specific encryption algorithm used.",
            "C) Encryption with SSL or TLS": "Correct – https indicates that SSL/TLS is used to secure the connection.",
            "D) SET, or Secure Electronic Transaction": "Incorrect – SET is a deprecated protocol, not what https represents."
        }
    },
    {
        "id": 27,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "A recent audit of an IT operation included a finding stating that the organization experiences virtualization sprawl. What is the meaning of this term?",
        "options": [
            "A) The process related to the creation of new virtual machines is not effective.",
            "B) Virtual machines are contending for scarce resources.",
            "C) The organization has too many virtual machines.",
            "D) Resource requirements for virtual machines are growing."
        ],
        "correct": "A",
        "option_explanations": {
            "A) The process related to the creation of new virtual machines is not effective.": "Correct – Virtualization sprawl is the phenomenon whereby new virtual machines are created without adequate management control. Because new servers can be created in a virtual environment without requiring the purchase of server hardware, organizations without effective controls will find that they have far more virtual machines than management intends.",
            "B) Virtual machines are contending for scarce resources.": "Incorrect – Virtualization sprawl does not refer to VMs contending for scarce resources. However, VMs contending for resources is a likely result of virtualization sprawl.",
            "C) The organization has too many virtual machines.": "Incorrect – An organization with too many virtual machines is a result of ineffective virtual machine management controls.",
            "D) Resource requirements for virtual machines are growing.": "Incorrect – Virtualization sprawl does not refer to the growing need for resources, but to the loss of control over the creation of virtual machines."
        }
    },
    {
        "id": 28,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "Reasons for placing all IoT-type devices on isolated VLANs include all of the following except:",
        "options": [
            "A) Use of a different network access method",
            "B) Compatibility with IPv4",
            "C) Risks associated with unpatched and unpatchable devices",
            "D) Protection from malware present in end-user environments"
        ],
        "correct": "B",
        "option_explanations": {
            "A) Use of a different network access method": "Incorrect – This is a potential consideration for placing IoT devices in isolated VLANs.",
            "B) Compatibility with IPv4": "Correct – Compatibility with IPv4 is rarely, if ever, a reason for isolating IoT devices onto a separate VLAN.",
            "C) Risks associated with unpatched and unpatchable devices": "Incorrect – This is a potential consideration.",
            "D) Protection from malware present in end-user environments": "Incorrect – This is a potential consideration."
        }
    },
    {
        "id": 29,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "What is the best reason for including competency quizzes in security awareness training courses?",
        "options": [
            "A) Quizzes are needed in order to improve users' knowledge.",
            "B) Quizzes are required by regulations such as PCI and HIPAA.",
            "C) It gives users an opportunity to test their skills.",
            "D) It provides evidence of retention of course content."
        ],
        "correct": "D",
        "option_explanations": {
            "A) Quizzes are needed in order to improve users' knowledge.": "Incorrect – Quizzes don't necessarily improve users' knowledge, but are used to test their knowledge.",
            "B) Quizzes are required by regulations such as PCI and HIPAA.": "Incorrect – PCI and HIPAA do not necessarily require quizzes.",
            "C) It gives users an opportunity to test their skills.": "Incorrect – The primary purposes of quizzes is to measure competency, not provide opportunities to practice.",
            "D) It provides evidence of retention of course content.": "Correct – Quizzes help to reinforce learning and provide evidence that users learned the content. Some online courses are able to require users to pass quizzes with a minimum score to complete the course."
        }
    },
    {
        "id": 30,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "In the context of information technology and information security, what is the purpose of fuzzing?",
        "options": [
            "A) To assess a physical server's resilience through a range of humidity settings",
            "B) To assess a physical server's ability to repel static electricity",
            "C) To assess a program's resistance to attack via the UI",
            "D) To assess a program's performance"
        ],
        "correct": "C",
        "option_explanations": {
            "A) To assess a physical server's resilience through a range of humidity settings": "Incorrect – Fuzzing is not related to humidity or static electricity in a server environment.",
            "B) To assess a physical server's ability to repel static electricity": "Incorrect – Fuzzing is not related to static electricity.",
            "C) To assess a program's resistance to attack via the UI": "Correct – Fuzzing refers to techniques where numerous iterations of data input combinations are offered to input fields to assess the presence and exploitability of security vulnerabilities.",
            "D) To assess a program's performance": "Incorrect – Fuzzing is not used to assess a program's performance."
        }
    },
    {
        "id": 31,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "An attacker who is attempting to infiltrate an organization has decided to employ a DNS poison cache attack. What method will the attacker use to attempt this attack?",
        "options": [
            "A) Send forged query replies to a DNS server.",
            "B) Send forged query replies to end-user workstations.",
            "C) Send forged PTR replies to end-user workstations.",
            "D) Send forced PTR replies to DNS servers."
        ],
        "correct": "A",
        "option_explanations": {
            "A) Send forged query replies to a DNS server.": "Correct – A DNS poison cache attack works by sending forged DNS query replies to a DNS server in an attempt to plant false information in the server's cache. The purpose of this attack is to direct users to the wrong server when their workstations query the DNS server.",
            "B) Send forged query replies to end-user workstations.": "Incorrect – DNS poison cache attacks involve sending forged replies to DNS servers, not to workstations.",
            "C) Send forged PTR replies to end-user workstations.": "Incorrect – DNS poison cache attacks do not utilize the sending of PTR replies.",
            "D) Send forced PTR replies to DNS servers.": "Incorrect – DNS poison cache attacks do not utilize PTR replies."
        }
    },
    {
        "id": 32,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "What is the Unix command to dynamically view the end of a text logfile?",
        "options": [
            "A) tail -f",
            "B) tail -e",
            "C) less -f",
            "D) more -f"
        ],
        "correct": "A",
        "option_explanations": {
            "A) tail -f": "Correct – The \"tail -f\" command will dynamically display the end of a text logfile. When new entries appear, tail will automatically show the new entries with no user intervention required.",
            "B) tail -e": "Incorrect – \"tail -e\" is not the proper command to display the end of a logfile dynamically.",
            "C) less -f": "Incorrect – \"less -f\" is not the proper command.",
            "D) more -f": "Incorrect – \"more -f\" is not the proper command."
        }
    },
    {
        "id": 33,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "In the United States, what are organizations required to do when discovering child pornography on a user's workstation?",
        "options": [
            "A) Contact law enforcement after the user has admitted to viewing child porn.",
            "B) Contact law enforcement when the user's workstation has been retired.",
            "C) Contact law enforcement after terminating the user.",
            "D) Immediately contact law enforcement."
        ],
        "correct": "D",
        "option_explanations": {
            "A) Contact law enforcement after the user has admitted to viewing child porn.": "Incorrect – There is no requirement for users to admit anything.",
            "B) Contact law enforcement when the user's workstation has been retired.": "Incorrect – Law enforcement must be notified immediately.",
            "C) Contact law enforcement after terminating the user.": "Incorrect – Law enforcement must be notified immediately.",
            "D) Immediately contact law enforcement.": "Correct – Organizations in the United States are required to contact law enforcement immediately upon discovery of child porn on any computer or workstation."
        }
    },
    {
        "id": 34,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "An organization suspects one of its employees of a security violation regarding the use of their workstation. The workstation, a laptop computer that is powered down, has been delivered to a forensic expert. What is the first thing the expert should do?",
        "options": [
            "A) Remove the hard drive.",
            "B) Photograph the laptop.",
            "C) Power up the laptop.",
            "D) Remove the RAM from the laptop."
        ],
        "correct": "B",
        "option_explanations": {
            "A) Remove the hard drive.": "Incorrect – The laptop should be photographed prior to removing the hard drive in order to document its pre-investigation state.",
            "B) Photograph the laptop.": "Correct – Prior to removing the hard drive to make a forensically identical copy for analysis, the forensic expert should first photograph the laptop to show its state prior to any disassembly.",
            "C) Power up the laptop.": "Incorrect – The laptop should not be powered up until after it has been photographed and its hard drive forensically copied.",
            "D) Remove the RAM from the laptop.": "Incorrect – The laptop should be photographed prior to any disassembly."
        }
    },
    {
        "id": 35,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "Which of the following statements is true regarding the Payment Card Industry Data Security Standard (PCI-DSS)?",
        "options": [
            "A) All organizations processing more than US$6,000,000 in credit card transactions annually must undergo an annual audit.",
            "B) Organizations using chip-and-PIN terminals are exempt from PCI requirements.",
            "C) Organizations processing fewer than six million merchant transactions annually are usually permitted to provide annual self-assessments.",
            "D) Organizations are permitted to opt out of low-risk controls via Compensating Control Worksheets."
        ],
        "correct": "C",
        "option_explanations": {
            "A) All organizations processing more than US$6,000,000 in credit card transactions annually must undergo an annual audit.": "Incorrect – Compliance levels are determined by the number of transactions, not the value of transactions.",
            "B) Organizations using chip-and-PIN terminals are exempt from PCI requirements.": "Incorrect – Organizations using chip-and-PIN terminals are still subject to PCI-DSS standards; however, such organizations have fewer requirements to comply with.",
            "C) Organizations processing fewer than six million merchant transactions annually are usually permitted to provide annual self-assessments.": "Correct – Merchant organizations with fewer than six million credit card transactions annually are usually permitted to complete annual self-assessment questionnaires.",
            "D) Organizations are permitted to opt out of low-risk controls via Compensating Control Worksheets.": "Incorrect – Organizations are not permitted to opt out of controls."
        }
    },
    {
        "id": 36,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "According to the European General Data Protection Regulation (GDPR), what is the requirement for organizations' use of a Data Protection Officer (DPO)?",
        "options": [
            "A) All organizations storing EU citizen data are required to have an employee designated as the DPO.",
            "B) All organizations storing large volumes of EU citizen data are required to use a DPO.",
            "C) All organizations storing EU citizen data are required to retain the services of a DPO consultant.",
            "D) Only organizations based in Europe are required to have a DPO."
        ],
        "correct": "B",
        "option_explanations": {
            "A) All organizations storing EU citizen data are required to have an employee designated as the DPO.": "Incorrect – Only organizations with a large volume of data, or operations requiring monitoring, are required to have a DPO.",
            "B) All organizations storing large volumes of EU citizen data are required to use a DPO.": "Correct – According to Article 37 of the GDPR, those organizations with large volumes of EU citizen data are required to have a DPO, which may be an employee or a consultant.",
            "C) All organizations storing EU citizen data are required to retain the services of a DPO consultant.": "Incorrect – Organizations are not required to have a DPO consultant; they can appoint an employee or not have a DPO at all if they meet certain criteria.",
            "D) Only organizations based in Europe are required to have a DPO.": "Incorrect – Organizations outside Europe but with operations in Europe may be required to have a DPO."
        }
    },
    {
        "id": 37,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "What is the biggest risk associated with access badges that show the name of the organization?",
        "options": [
            "A) Someone who finds the badge may know where it can be used.",
            "B) An attacker can look up the organization's public key and create forged badges.",
            "C) An attacker would know what brand of access badge technology is being used.",
            "D) Someone who finds a lost badge would be able to return it to the company."
        ],
        "correct": "A",
        "option_explanations": {
            "A) Someone who finds the badge may know where it can be used.": "Correct – An access badge bearing the name of the organization would give someone finding the badge valuable information about where the badge may be used. If the organization does not use multifactor access controls, anyone finding a badge may be able to enter buildings, parking garages, and even data centers.",
            "B) An attacker can look up the organization's public key and create forged badges.": "Incorrect – Encryption keys for access badge systems are not publicly available.",
            "C) An attacker would know what brand of access badge technology is being used.": "Incorrect – The organization's name does not reveal the brand of access card in use.",
            "D) Someone who finds a lost badge would be able to return it to the company.": "Incorrect – This is not a risk associated with an organization's name on the badge, but a benefit."
        }
    },
    {
        "id": 38,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "A user at work logs on to a web site that includes links to various business applications. Once the user logs on to the web site, the user does not need to log on to individual business applications. What mechanism provides this capability?",
        "options": [
            "A) Public key infrastructure",
            "B) Reduced sign-on",
            "C) Single sign-on",
            "D) Key vaulting"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Public key infrastructure": "Incorrect – A PKI is not the primary agent providing this capability. PKI is not required for an SSO portal.",
            "B) Reduced sign-on": "Incorrect – Reduced sign-on lets users remember fewer login credentials, but those credentials must be used when logging on to each application.",
            "C) Single sign-on": "Correct – The user has logged on to a single sign-on (SSO) portal, which provides easy access to many business applications without the user having to log on to each one.",
            "D) Key vaulting": "Incorrect – Key vaulting is a mechanism for storing encryption keys, not for facilitating single sign-on."
        }
    },
    {
        "id": 39,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "What is the primary advantage of cloud-based web content filtering versus on-premises web content filtering?",
        "options": [
            "A) Cloud-based web content filtering systems are less expensive.",
            "B) Exceptions can be processed more quickly.",
            "C) Off-network users are protected just as in-office users are.",
            "D) Users are unable to circumvent this protection."
        ],
        "correct": "C",
        "option_explanations": {
            "A) Cloud-based web content filtering systems are less expensive.": "Incorrect – Cloud-based solutions are not necessarily less expensive.",
            "B) Exceptions can be processed more quickly.": "Incorrect – The process of handling exceptions does not vary based on whether the solution is on-premises or cloud-based.",
            "C) Off-network users are protected just as in-office users are.": "Correct – The primary advantage of cloud-based web content filtering is that all users are protected, whether they are on the organization's internal network or off-network, either at home or traveling.",
            "D) Users are unable to circumvent this protection.": "Incorrect – Users are unable to circumvent protection, whether the solution is on-premises or cloud-based."
        }
    },
    {
        "id": 40,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "An organization is investigating the use of an automated DLP solution that controls whether data files can be sent via e-mail or stored on USB drives based on their tags. What is the advantage of the use of tags for such a solution?",
        "options": [
            "A) Users are easily able to tag files so that they can be properly handled in e-mail.",
            "B) Data files are automatically processed based on tags instead of their data content.",
            "C) Tags are a better solution than the use of digital envelopes.",
            "D) Tags are human readable and can be altered as needed."
        ],
        "correct": "B",
        "option_explanations": {
            "A) Users are easily able to tag files so that they can be properly handled in e-mail.": "Incorrect – Users do not necessarily have the ability to tag files (and if they did, one should expect that many errors will be made that will result in mishandling of data).",
            "B) Data files are automatically processed based on tags instead of their data content.": "Correct – Automated systems can take action based on the tags in a file. However, this is only as good as the mechanism used to apply tags in the first place, which could be highly accurate or inaccurate.",
            "C) Tags are a better solution than the use of digital envelopes.": "Incorrect – Digital envelopes have not been used in DLP solutions.",
            "D) Tags are human readable and can be altered as needed.": "Incorrect – Tags are not easily human readable, and they are not intended to be easily changed, except by approved means."
        }
    },
    {
        "id": 41,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "All of the following are appropriate uses of digital signatures except:",
        "options": [
            "A) Verification of message authenticity",
            "B) Verification of message integrity",
            "C) Verification of message confidentiality",
            "D) Verification of message origin"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Verification of message authenticity": "Incorrect – This is a legitimate and intended use of digital signatures.",
            "B) Verification of message integrity": "Incorrect – This is a legitimate use.",
            "C) Verification of message confidentiality": "Correct – Verification of message confidentiality is not a use of digital signatures.",
            "D) Verification of message origin": "Incorrect – This is a legitimate use."
        }
    },
    {
        "id": 42,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "The entity that accepts requests for new public keys in a PKI is known as the:",
        "options": [
            "A) Reservation authority (RA)",
            "B) Validation authority (VA)",
            "C) Registration authority (RA)",
            "D) Certificate authority (CA)"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Reservation authority (RA)": "Incorrect – Reservation authority is not the term used; further, the PKI model does not have an entity called a reservation authority.",
            "B) Validation authority (VA)": "Incorrect – A validation authority (VA), usually a third party such as a government, serves to ensure that the request is genuine.",
            "C) Registration authority (RA)": "Correct – A registration authority (RA) is the entity that receives and accepts requests for new public keys or digital certificates in a PKI such as an SSL certificate issuer for securing web site communication.",
            "D) Certificate authority (CA)": "Incorrect – A certificate authority (CA) is the entity that creates and issues a public key or digital certificate."
        }
    },
    {
        "id": 43,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "What method is used by a transparent proxy filter to prevent a user from visiting a site that has been blacklisted?",
        "options": [
            "A) Proxy sends an HTTP 400 Bad Request to the user's browser.",
            "B) User is directed to a \"web site blocked\" splash page.",
            "C) Proxy filter simply drops the packets and the user's browser times out.",
            "D) User's workstation is quarantined to prevent malware from spreading."
        ],
        "correct": "B",
        "option_explanations": {
            "A) Proxy sends an HTTP 400 Bad Request to the user's browser.": "Incorrect – A transparent proxy generally does not return error codes to the user's browser, but instead displays a splash page.",
            "B) User is directed to a \"web site blocked\" splash page.": "Correct – A transparent proxy server will usually direct a user to a \"splash page,\" informing the user that their request to access a forbidden web site has been blocked. Some organizations include information on the splash page that can direct the user to make a request to unblock access.",
            "C) Proxy filter simply drops the packets and the user's browser times out.": "Incorrect – This inelegant method will cause the user to believe that there is a technical problem that potentially requires tech support.",
            "D) User's workstation is quarantined to prevent malware from spreading.": "Incorrect – This situation does not cite a suspected or confirmed malware infection that warrants quarantining the workstation."
        }
    },
    {
        "id": 44,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "In a virtualized environment, which method is the fastest way to ensure rapid recovery of servers at an alternative processing center?",
        "options": [
            "A) Copy snapshots of virtual machine images to alternative processing center storage system.",
            "B) Provide build instructions for all servers and make master server images available.",
            "C) Perform full and incremental backups of all servers on a daily basis.",
            "D) Perform grandfather-father-son backups of all servers on a daily basis."
        ],
        "correct": "A",
        "option_explanations": {
            "A) Copy snapshots of virtual machine images to alternative processing center storage system.": "Correct – Copying snapshots of actual server images ensures that recent server images are available at the alternative processing center for rapid restoration.",
            "B) Provide build instructions for all servers and make master server images available.": "Incorrect – Using procedures to recover servers may be accurate but will take more time than restoring snapshots of virtual server images.",
            "C) Perform full and incremental backups of all servers on a daily basis.": "Incorrect – Restoring server images from multiple generations of backup media may be accurate, but will be far more time consuming than employing snapshots of server images.",
            "D) Perform grandfather-father-son backups of all servers on a daily basis.": "Incorrect – Restoring from backup media is slower than snapshots."
        }
    },
    {
        "id": 45,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "In an environment where users are not local administrators of their workstations, which of the following methods ensures that end users are not able to use their mobile devices as mobile Wi-Fi hotspots for circumventing network security controls such as web content filters and IPS?",
        "options": [
            "A) Require employees to turn off their mobile devices at work.",
            "B) Jam the signals of unauthorized Wi-Fi networks.",
            "C) Create a whitelist of permitted Wi-Fi networks.",
            "D) Create a blacklist of forbidden Wi-Fi networks."
        ],
        "correct": "C",
        "option_explanations": {
            "A) Require employees to turn off their mobile devices at work.": "Incorrect – A policy requiring employees to turn off their mobile devices is not likely to be successful.",
            "B) Jam the signals of unauthorized Wi-Fi networks.": "Incorrect – Jamming signals of unauthorized Wi-Fi networks is not likely to be successful, and may possibly even be illegal in some jurisdictions. Also, many mobile devices also permit Bluetooth and USB connections for tethering.",
            "C) Create a whitelist of permitted Wi-Fi networks.": "Correct – The best workable solution is to create a whitelist of Wi-Fi networks that workstations are permitted to connect to. These networks would include all corporate Wi-Fi networks, as well as any trusted non-corporate networks.",
            "D) Create a blacklist of forbidden Wi-Fi networks.": "Incorrect – Managing blacklists is a never-ending game of whack-a-mole."
        }
    },
    {
        "id": 46,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "What is the most effective method for training users to more accurately detect and delete phishing messages?",
        "options": [
            "A) Block access to personal webmail and permit corporate e-mail only.",
            "B) Include phishing information in regular security awareness training.",
            "C) Conduct phishing tests and publicly inform offenders of their mistakes.",
            "D) Conduct phishing tests and privately inform offenders of their mistakes."
        ],
        "correct": "D",
        "option_explanations": {
            "A) Block access to personal webmail and permit corporate e-mail only.": "Incorrect – Blocking personal web mail does not address the matter of phishing messages that are sent to users' corporate e-mail addresses.",
            "B) Include phishing information in regular security awareness training.": "Incorrect – While including phishing information in security awareness training is a good practice, this is not as effective as conducting phishing tests.",
            "C) Conduct phishing tests and publicly inform offenders of their mistakes.": "Incorrect – Publicly shaming users who make mistakes is not good for morale.",
            "D) Conduct phishing tests and privately inform offenders of their mistakes.": "Correct – Well-managed phishing testing campaigns can help employees learn how to spot phishing messages. Providing a \"I think this is a phish\" reporting capability gives end users the ability to affirm that test messages are phishing tests, and it's also a good method for reporting actual phishing messages."
        }
    },
    {
        "id": 47,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "An attacker has targeted an organization in order to steal specific information. The attacker has found that the organization's defenses are strong and that very few phishing messages arrive at end-user inboxes. The attacker has decided to try a watering hole attack. What first steps should the hacker use to ensure a successful watering hole attack?",
        "options": [
            "A) Determine which web sites are frequently visited by the organization's end users.",
            "B) Determine which restaurants the organization's end users visit after working hours.",
            "C) Determine which protocols are blocked by the organization's Internet firewalls.",
            "D) Determine the IP addresses of public-facing web servers that can be attacked."
        ],
        "correct": "A",
        "option_explanations": {
            "A) Determine which web sites are frequently visited by the organization's end users.": "Correct – In order to conduct a successful watering hole attack, the attacker must first determine which web sites are frequently visited by employees in the organization. This will include cloud-based applications used for primary business processes such as accounting, sales, human resources, and file storage.",
            "B) Determine which restaurants the organization's end users visit after working hours.": "Incorrect – A watering hole attack involves attacks on web sites frequently visited by the target organization's personnel.",
            "C) Determine which protocols are blocked by the organization's Internet firewalls.": "Incorrect – The attacker has already dismissed frontal attack techniques such as compromising exploitable server vulnerabilities.",
            "D) Determine the IP addresses of public-facing web servers that can be attacked.": "Incorrect – The attacker is not focusing on direct server attacks."
        }
    },
    {
        "id": 48,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "Which of the following techniques most accurately describes a penetration test?",
        "options": [
            "A) Manual exploitation tools and techniques",
            "B) Security scan, with results tabulated into a formal report that includes an executive summary",
            "C) Security scan, with results validated to remove any false positives",
            "D) Security scan, followed by manual exploitation tools and techniques"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Manual exploitation tools and techniques": "Incorrect – A penetration test usually begins with a security scan to enumerate the environment, which identifies targets to attack.",
            "B) Security scan, with results tabulated into a formal report that includes an executive summary": "Incorrect – This method lacks the manual tools and techniques that are central to a penetration test. What is described here is simply a security scan and nothing more.",
            "C) Security scan, with results validated to remove any false positives": "Incorrect – A penetration test also includes numerous manual exploitation techniques. This is just a validated security scan.",
            "D) Security scan, followed by manual exploitation tools and techniques": "Correct – A penetration test most commonly begins with a security scan that enumerates assets and provides a big-picture attack profile. This is followed by an array of manual attack techniques that attempt to exploit vulnerabilities in the systems and services identified by the security scan."
        }
    },
    {
        "id": 49,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "A security analyst spends most of her time on a system that collects log data and correlates events from various systems to deduce potential attacks in progress. What kind of a system is the security analyst using?",
        "options": [
            "A) SIEM",
            "B) IPS",
            "C) IDS",
            "D) AV console"
        ],
        "correct": "A",
        "option_explanations": {
            "A) SIEM": "Correct – The security analyst is using a SIEM, or security information and event management system. A SIEM collects log data from devices throughout the environment and then correlates seemingly disparate events to deduce potential attacks. When such attacks are discerned, the SIEM will produce an alert that directs the security analyst to further investigate the matter and take possible action.",
            "B) IPS": "Incorrect – An IPS is an inline device that is used to detect and block unwanted network traffic. An IPS does not collect log data from devices in the network.",
            "C) IDS": "Incorrect – An IDS monitors network traffic and detects unwanted traffic but does not collect log data from devices.",
            "D) AV console": "Incorrect – An AV console is used to monitor antivirus software that is running on servers and endpoints."
        }
    },
    {
        "id": 50,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "The general counsel is becoming annoyed with notifications of minor security events occurring in the organization. This is most likely due to:",
        "options": [
            "A) Careless users clicking on too many phishing e-mails",
            "B) Ineffective defenses allowing frequent attacks",
            "C) Improper classification of security incidents",
            "D) Lack of a security incident severity scheme"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Careless users clicking on too many phishing e-mails": "Incorrect – This is too narrow a scenario.",
            "B) Ineffective defenses allowing frequent attacks": "Incorrect – The scenario here involves minor incidents, not successful attacks on outer defenses.",
            "C) Improper classification of security incidents": "Incorrect – Improper classification of incidents would likely be resolved quickly.",
            "D) Lack of a security incident severity scheme": "Correct – The most likely reason the general counsel is being notified of minor incidents is the lack of an incident classification scheme in the organization's security incident response plan. Without a severity classification scheme, all incidents are treated as equal, regardless of their actual severity. In this case, the result is executives being notified of minor incidents that should be of little or no concern to them."
        }
    },
    {
        "id": 51,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "A forensic investigator is seen to be creating a detailed record of artifacts that are collected, analyzed, controlled, transferred to others, and stored for safekeeping. What kind of a written record is this?",
        "options": [
            "A) Storage inventory",
            "B) Investigation report",
            "C) Evidence collection log",
            "D) Chain of custody record"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Storage inventory": "Incorrect – A storage inventory record would not include information about transfer of custody or analysis of items.",
            "B) Investigation report": "Incorrect – An investigative report would describe conclusions of an investigation.",
            "C) Evidence collection log": "Incorrect – An evidence collection log would not include analysis, control, and transfers.",
            "D) Chain of custody record": "Correct – The recordkeeping described is a chain of custody record, which provides a detailed account for each artifact collected and analyzed."
        }
    },
    {
        "id": 52,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "Which controls framework is suggested by the ISO/IEC 27001 standard?",
        "options": [
            "A) ISO/IEC 27001",
            "B) ISO/IEC 27002",
            "C) NIST SP800-53",
            "D) Any framework that is applicable to the organization"
        ],
        "correct": "B",
        "option_explanations": {
            "A) ISO/IEC 27001": "Incorrect – The controls listed in Annex A of ISO/IEC 27001 are from the ISO/IEC 27002 standard.",
            "B) ISO/IEC 27002": "Correct – ISO/IEC 27001 suggests the use of the ISO/IEC 27002 standard for controls. Annex A of ISO/IEC 27001 contains a summary list of the controls found in the ISO/IEC 27002 standard.",
            "C) NIST SP800-53": "Incorrect – ISO/IEC 27001 does not suggest the use of NIST SP800-53.",
            "D) Any framework that is applicable to the organization": "Incorrect – ISO/IEC 27001 contains a summary of the controls in ISO/IEC 27002."
        }
    },
    {
        "id": 53,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "The default principle in the European General Data Protection Regulation for marketing communications from organizations to citizens is:",
        "options": [
            "A) Citizens are included and cannot opt out.",
            "B) Citizens are included until they explicitly opt out.",
            "C) Citizens are excluded until they explicitly opt in.",
            "D) Citizens are excluded and cannot opt in."
        ],
        "correct": "C",
        "option_explanations": {
            "A) Citizens are included and cannot opt out.": "Incorrect – Citizens are not included; they are excluded by default.",
            "B) Citizens are included until they explicitly opt out.": "Incorrect – Citizens are not included; they are excluded.",
            "C) Citizens are excluded until they explicitly opt in.": "Correct – Under the GDPR, organizations are not permitted to market to individual citizens unless the citizens first opt in.",
            "D) Citizens are excluded and cannot opt in.": "Incorrect – Citizens can opt in."
        }
    },
    {
        "id": 54,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "The primary purpose of a mantrap is:",
        "options": [
            "A) To catch an individual attempting to enter a room without authorization",
            "B) To hold an offender in custody until charged or released",
            "C) To permit entry of one authorized person at a time",
            "D) To permit entry or exit of one authorized person at a time"
        ],
        "correct": "D",
        "option_explanations": {
            "A) To catch an individual attempting to enter a room without authorization": "Incorrect – A mantrap does not intend to entrap persons attempting to enter or exit an area.",
            "B) To hold an offender in custody until charged or released": "Incorrect – A mantrap is not a holding cell, but an access control.",
            "C) To permit entry of one authorized person at a time": "Incorrect – A mantrap can be used for both entrance and exit.",
            "D) To permit entry or exit of one authorized person at a time": "Correct – A mantrap is a special controlled entrance or exit that permits only one person at a time to enter or exit an area."
        }
    },
    {
        "id": 55,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "What is the purpose of locking a user account that has not been used for long periods of time?",
        "options": [
            "A) Reduction of the risk of compromised credentials",
            "B) Free up space for others to use the system",
            "C) Avoidance of audit exceptions",
            "D) Recycle license keys and cost reduction"
        ],
        "correct": "A",
        "option_explanations": {
            "A) Reduction of the risk of compromised credentials": "Correct – If a user has not logged in to an application for long periods of time, then perhaps the user account for that application can be locked. This would reduce the impact of compromised credentials by preventing an unauthorized party from logging in to a system.",
            "B) Free up space for others to use the system": "Incorrect – Freeing up space is generally not the primary reason for removing user accounts.",
            "C) Avoidance of audit exceptions": "Incorrect – Avoidance of audit exceptions would be a secondary result. Many organizations have a control that requires dormant user accounts to be locked or removed, and that control is sometimes audited.",
            "D) Recycle license keys and cost reduction": "Incorrect – The harvesting of unused licenses is not generally a primary reason for locking a user account. If an organization needed to harvest licenses, the user account would probably need to be removed and not just locked."
        }
    },
    {
        "id": 56,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "What is the best approach for implementing a new blocking rule in an IPS?",
        "options": [
            "A) First implement a firewall rule and then activate the IPS rule.",
            "B) Use the change control process so that stakeholders are aware of the new rule.",
            "C) Implement a new rule during a change window.",
            "D) Put the rule in learn mode and analyze the results."
        ],
        "correct": "D",
        "option_explanations": {
            "A) First implement a firewall rule and then activate the IPS rule.": "Incorrect – Firewalls generally lack the sophistication of an IPS and instead can only block packets based on source and destination IP addresses and port numbers.",
            "B) Use the change control process so that stakeholders are aware of the new rule.": "Incorrect – Even the change control process is not always going to detect potential negative consequences of a new IPS blocking rule.",
            "C) Implement a new rule during a change window.": "Incorrect – This approach provides no opportunity to first learn whether the new blocking rule will disrupt legitimate activities.",
            "D) Put the rule in learn mode and analyze the results.": "Correct – The best approach is to first create the rule in learn mode, where the rule will detect and log rule activations, but not actually block traffic. Analysis of the log will help analysts understand whether the new rule would inadvertently block legitimate traffic and disrupt system operation. If no such interference is observed, the rule can be safely put into block mode."
        }
    },
    {
        "id": 57,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "A security leader needs to develop a data classification program. After developing the data classification and handling policy, what is the best next step to perform?",
        "options": [
            "A) Configure DLP systems to monitor and enforce compliance.",
            "B) Configure DLP systems to monitor compliance.",
            "C) Announce the new policy to the organization.",
            "D) Work with business departments to socialize the policy."
        ],
        "correct": "D",
        "option_explanations": {
            "A) Configure DLP systems to monitor and enforce compliance.": "Incorrect – Enforcing data classification policy as a first step is highly likely to disrupt business processes.",
            "B) Configure DLP systems to monitor compliance.": "Incorrect – Monitoring data classification policy is highly likely to produce numerous false-positive alerts.",
            "C) Announce the new policy to the organization.": "Incorrect – Announcing policy to the organization is likely to cause confusion unless the security leader first works with all individual departments to understand the potential impact of the new data classification policy.",
            "D) Work with business departments to socialize the policy.": "Correct – The best next step is to work with various business departments to discuss the new policy and handling guidelines to understand the potential impact of the policy. A badly implemented data classification program can cause business disruption and erode goodwill."
        }
    },
    {
        "id": 58,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "An organization wants to implement an IPS that utilizes SSL inspection. What must first be implemented so that the IPS will function?",
        "options": [
            "A) A span port on the Internet switch must be configured.",
            "B) A new root certificate must be pushed to all user workstations.",
            "C) Users must sign a consent for their personal traffic to be monitored.",
            "D) All end-user private keys must be refreshed."
        ],
        "correct": "B",
        "option_explanations": {
            "A) A span port on the Internet switch must be configured.": "Incorrect – A span port is used for traffic mirroring, not SSL inspection.",
            "B) A new root certificate must be pushed to all user workstations.": "Correct – For SSL inspection to work, the IPS must be able to act as a man-in-the-middle, which requires its own root certificate to be trusted by the endpoints.",
            "C) Users must sign a consent for their personal traffic to be monitored.": "Incorrect – Consent is not a technical prerequisite.",
            "D) All end-user private keys must be refreshed.": "Incorrect – Refreshing keys is not required for SSL inspection."
        }
    },
    {
        "id": 59,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "In what manner does a PKI support whole disk encryption on end-user workstations?",
        "options": [
            "A) PKI stores the bootup passwords used on each end-user workstation.",
            "B) PKI detects unauthorized use of data on end-user workstations.",
            "C) PKI stores decryption keys in the event an end-user forgets their bootup password.",
            "D) PKI records encryption and decryption operations."
        ],
        "correct": "C",
        "option_explanations": {
            "A) PKI stores the bootup passwords used on each end-user workstation.": "Incorrect – A PKI does not store the bootup password used on end-user workstations.",
            "B) PKI detects unauthorized use of data on end-user workstations.": "Incorrect – A PKI does not monitor file access on systems.",
            "C) PKI stores decryption keys in the event an end-user forgets their bootup password.": "Correct – While a PKI is not required to implement whole disk encryption on end-user workstations, a PKI can be used to store administrative keys that can be used to unlock a workstation in the event that the user has forgotten their bootup password.",
            "D) PKI records encryption and decryption operations.": "Incorrect – A PKI does not record encryption and decryption operations, but instead can store administrative keys that can be used to unlock a workstation."
        }
    },
    {
        "id": 60,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "A browser contacts a web server and requests a web page. The web server responds with a status code 200. What is the meaning of this status code?",
        "options": [
            "A) The user has been redirected to another URL on the same domain.",
            "B) The user has been redirected to another URL on a different domain.",
            "C) The requested page requires prior authentication.",
            "D) The request is valid and has been accepted."
        ],
        "correct": "D",
        "option_explanations": {
            "A) The user has been redirected to another URL on the same domain.": "Incorrect – A code 200 is a successful transaction and not related to redirection.",
            "B) The user has been redirected to another URL on a different domain.": "Incorrect – A code 200 is a successful transaction.",
            "C) The requested page requires prior authentication.": "Incorrect – A code 200 is a successful transaction and not related to authentication.",
            "D) The request is valid and has been accepted.": "Correct – A response code 200 means the request is valid and has been responded to."
        }
    },
    {
        "id": 61,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "For what reason would an engineer choose to use a hosted hypervisor versus a bare-metal hypervisor?",
        "options": [
            "A) There are insufficient resources available for a bare-metal hypervisor.",
            "B) Features available only in a host operating system are required.",
            "C) Guest OS monitoring is required.",
            "D) The hypervisor is supporting a VDI environment."
        ],
        "correct": "B",
        "option_explanations": {
            "A) There are insufficient resources available for a bare-metal hypervisor.": "Incorrect – A bare-metal hypervisor actually consumes fewer resources than a full OS.",
            "B) Features available only in a host operating system are required.": "Correct – An engineer would select a hosted hypervisor because one or more features or functions found only on the operating system are required.",
            "C) Guest OS monitoring is required.": "Incorrect – Bare-metal hypervisors provide guest OS monitoring.",
            "D) The hypervisor is supporting a VDI environment.": "Incorrect – A bare-metal hypervisor is capable of supporting a VDI (virtual desktop infrastructure) environment."
        }
    },
    {
        "id": 62,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "The laboratory environment of a pharmaceutical research organization contains many scientific instruments that contain older versions of Windows and Linux operating systems that cannot be patched. What is the best remedy for this?",
        "options": [
            "A) Isolate the scientific instruments on a separate, protected network.",
            "B) Upgrade the OSs on the scientific instruments to current OS versions.",
            "C) Disconnect the OSs from the network.",
            "D) Audit user accounts on the OSs periodically."
        ],
        "correct": "A",
        "option_explanations": {
            "A) Isolate the scientific instruments on a separate, protected network.": "Correct – The presence of older and/or unpatchable OSs on scientific equipment is a common problem. Most often, the best approach is to isolate those systems through network segmentation and security controls to ensure that all attempts to attack those systems will be automatically detected and blocked.",
            "B) Upgrade the OSs on the scientific instruments to current OS versions.": "Incorrect – Often the OSs on such equipment cannot be upgraded for various reasons (e.g., laboratory software will not run on newer OS versions, or there are insufficient resources such as memory).",
            "C) Disconnect the OSs from the network.": "Incorrect – Disconnecting those older OSs may impair their operation.",
            "D) Audit user accounts on the OSs periodically.": "Incorrect – Auditing user accounts does little to protect these older OSs from attack."
        }
    },
    {
        "id": 63,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "Which of the following is the best policy for a security awareness training course?",
        "options": [
            "A) Users are not required to take competency quizzes.",
            "B) Users are required to repeat modules when they fail competency quizzes.",
            "C) Users are required to take competency quizzes only one time, regardless of score.",
            "D) Users can skip training if they pass competency quizzes."
        ],
        "correct": "B",
        "option_explanations": {
            "A) Users are not required to take competency quizzes.": "Incorrect – Users should be required to take competency quizzes to see how well they retained the learning content.",
            "B) Users are required to repeat modules when they fail competency quizzes.": "Correct – When a user fails to achieve the minimum passing grade on a competency quiz, the user should be required to repeat the learning module and then take the quiz again.",
            "C) Users are required to take competency quizzes only one time, regardless of score.": "Incorrect – Users should be required to repeat the learning module if they fail the competency quiz.",
            "D) Users can skip training if they pass competency quizzes.": "Incorrect – Some learning content may not have accompanying quizzes, but that is not the best policy."
        }
    },
    {
        "id": 64,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "Guessing that an intended victim has a particular online banking session open, an attacker attempts to trick the victim into clicking on a link that will attempt to execute a transaction on the online banking site. This type of an attack is known as:",
        "options": [
            "A) Cross-site scripting",
            "B) Cross-site request forgery",
            "C) Man in the middle",
            "D) Man in the browser"
        ],
        "correct": "B",
        "option_explanations": {
            "A) Cross-site scripting": "Incorrect – A cross-site scripting attack is one in which an attacker attempts to inject code into a web site, where the code is then executed later by others who visit the site.",
            "B) Cross-site request forgery": "Correct – A cross-site request forgery (CSRF) attack is one in which an attacker attempts to trick a victim into performing a transaction on another web site (for example, a banking transaction in which the victim transfers money to the attacker).",
            "C) Man in the middle": "Incorrect – A man-in-the-middle (MITM) attack is one in which an attacker attempts to subvert communications between two parties by intercepting and injecting forged content into the communications.",
            "D) Man in the browser": "Incorrect – A man-in-the-browser (MITB) attack is one in which an attacker attempts to exploit a vulnerability in a user's browser by tricking the user into downloading malicious code that alters the browser's operation."
        }
    },
    {
        "id": 65,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "Which of the following tools is considered a search engine that can be used to list vulnerabilities in devices?",
        "options": [
            "A) OpenVAS",
            "B) Burp Suite",
            "C) Shodan",
            "D) John the Ripper"
        ],
        "correct": "C",
        "option_explanations": {
            "A) OpenVAS": "Incorrect – OpenVAS is a network vulnerability testing tool.",
            "B) Burp Suite": "Incorrect – Burp Suite is a web application testing tool.",
            "C) Shodan": "Correct – Shodan is a search engine that scans the Internet using common protocols and catalogs the responses returned from devices. This is a useful tool for seeing what devices are visible from the Internet.",
            "D) John the Ripper": "Incorrect – John the Ripper is a password cracking tool."
        }
    },
    {
        "id": 66,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "All of the following tools are used to detect changes in static files except:",
        "options": [
            "A) Blacklight",
            "B) OSSEC",
            "C) Tripwire",
            "D) Firesheep"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Blacklight": "Incorrect – Blacklight is a file integrity monitoring (FIM) tool.",
            "B) OSSEC": "Incorrect – OSSEC is a file integrity monitoring tool.",
            "C) Tripwire": "Incorrect – Tripwire is a file integrity monitoring tool.",
            "D) Firesheep": "Correct – Firesheep is not a file integrity monitoring (FIM) tool, but instead is a tool used to steal cookies from other user sessions in unprotected Wi-Fi networks."
        }
    },
    {
        "id": 67,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "Which of the following correctly describes the correct sequence for computer security incident response?",
        "options": [
            "A) Protect, detect, respond, recover",
            "B) Identify, protect, detect, respond, recover",
            "C) Evaluate, detect, eradicate, contain, recover, closure",
            "D) Detect, initiate, evaluate, contain, eradicate, recover, remediate"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Protect, detect, respond, recover": "Incorrect – These are not the correct steps in computer security incident response.",
            "B) Identify, protect, detect, respond, recover": "Incorrect – These are the pillars of the NIST CSF framework, not incident response steps.",
            "C) Evaluate, detect, eradicate, contain, recover, closure": "Incorrect – Evaluate and detect are out of sequence; an incident is first detected and then evaluated.",
            "D) Detect, initiate, evaluate, contain, eradicate, recover, remediate": "Correct – The correct sequence for organizing computer security incident response is detect, initiate, evaluate, contain, eradicate, recover, and remediate. This is often followed by a post-incident review."
        }
    },
    {
        "id": 68,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "Which of the following devices is needed for the creation of a forensically identical hard disk drive?",
        "options": [
            "A) Diode",
            "B) Bit locker",
            "C) Read blocker",
            "D) Write blocker"
        ],
        "correct": "D",
        "option_explanations": {
            "A) Diode": "Incorrect – A diode is not used for forensic duplication.",
            "B) Bit locker": "Incorrect – Bit locker is a Microsoft encryption feature.",
            "C) Read blocker": "Incorrect – A read blocker would prevent reading, not writing.",
            "D) Write blocker": "Correct – A write blocker is a device used to read data from a hard drive whose contents are being evaluated. The write blocker makes it impossible for data to be written to the hard drive."
        }
    },
    {
        "id": 69,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "Which of the following statements about NIST CSF is true?",
        "options": [
            "A) NIST CSF is a security controls framework.",
            "B) NIST CSF is a policy framework for cybersecurity.",
            "C) NIST CSF is a computer security incident response framework.",
            "D) NIST CSF is a software development framework."
        ],
        "correct": "B",
        "option_explanations": {
            "A) NIST CSF is a security controls framework.": "Incorrect – NIST CSF is not a controls framework.",
            "B) NIST CSF is a policy framework for cybersecurity.": "Correct – NIST CSF is a policy framework for cybersecurity that provides guidance for organizations that want to improve their cybersecurity capabilities.",
            "C) NIST CSF is a computer security incident response framework.": "Incorrect – NIST CSF is not an incident response framework.",
            "D) NIST CSF is a software development framework.": "Incorrect – NIST CSF is not a software development framework."
        }
    },
    {
        "id": 70,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "The \"right to be forgotten\" was first implemented by:",
        "options": [
            "A) GDPR",
            "B) Google",
            "C) NYDFS",
            "D) Facebook"
        ],
        "correct": "A",
        "option_explanations": {
            "A) GDPR": "Correct – The \"right to be forgotten\" is a concept that has been codified in the European General Data Protection Regulation (GDPR). A European citizen can make requests of online service providers and ask that records associated with them be anonymized or expunged.",
            "B) Google": "Incorrect – Google did not first implement the \"right to be forgotten.\"",
            "C) NYDFS": "Incorrect – NYDFS did not first implement it.",
            "D) Facebook": "Incorrect – Facebook did not first implement it."
        }
    },
    {
        "id": 71,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "The term \"tailgating\" most often refers to:",
        "options": [
            "A) Personnel who prop or shim doors so that others can enter a protected facility without authentication",
            "B) Personnel who permit others to follow them into a protected facility without authentication",
            "C) Personnel who follow others into a protected facility without authentication",
            "D) Personnel who loan their keycards to others to enter a protected facility"
        ],
        "correct": "C",
        "option_explanations": {
            "A) Personnel who prop or shim doors so that others can enter a protected facility without authentication": "Incorrect – Tailgating does not refer to propping doors open.",
            "B) Personnel who permit others to follow them into a protected facility without authentication": "Incorrect – Tailgating is the act of following others in, not permitting entry.",
            "C) Personnel who follow others into a protected facility without authentication": "Correct – Tailgating refers to people who follow others into a protected facility without themselves authenticating with their keycard or other device.",
            "D) Personnel who loan their keycards to others to enter a protected facility": "Incorrect – Tailgating is not the act of loaning a keycard."
        }
    },
    {
        "id": 72,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "A security manager in a large organization has found that the IT department has no central management of privileged user accounts. What kind of a tool should the security manager introduce to remedy this practice?",
        "options": [
            "A) FAM tools",
            "B) FIM tools",
            "C) PAM tools",
            "D) SIEM tools"
        ],
        "correct": "C",
        "option_explanations": {
            "A) FAM tools": "Incorrect – File activity monitoring (FAM) tools are not a proper remedy.",
            "B) FIM tools": "Incorrect – File integrity monitoring (FIM) tools are not a proper remedy.",
            "C) PAM tools": "Correct – Privileged Access Management (PAM) tools are used to centrally control the use of privileged accounts, both for administrative personnel and for service accounts.",
            "D) SIEM tools": "Incorrect – Security information and event management (SIEM) tools are not a proper remedy."
        }
    },
    {
        "id": 73,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "A security analyst has determined that some of the OS configuration file alterations have taken place without proper authorization. Which tool did the security analyst use to determine this?",
        "options": [
            "A) FAM",
            "B) FIM",
            "C) PAM",
            "D) SIEM"
        ],
        "correct": "B",
        "option_explanations": {
            "A) FAM": "Incorrect – File activity monitoring (FAM) tools record accesses to files, but not alterations to files.",
            "B) FIM": "Correct – The security analyst's use of file integrity monitoring (FIM) tools revealed that files were being changed without authorization. FIM tools do not reveal the subject(s) who altered the files; other means are needed, such as examining login logs.",
            "C) PAM": "Incorrect – Privileged Access Management (PAM) tools do not all record administrator activities.",
            "D) SIEM": "Incorrect – A security information and event management (SIEM) tool cannot by itself detect file changes, but only in conjunction with file integrity monitoring (FIM) tools."
        }
    },
    {
        "id": 74,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "An employee notes that a company document is marked \"Confidential.\" Is it acceptable for the employee to e-mail the document to a party outside the company?",
        "options": [
            "A) Yes, but the document must be encrypted first.",
            "B) Yes, the document can be e-mailed to an outside party in plaintext.",
            "C) This cannot be determined without first consulting the data classification and handling policy.",
            "D) No, the document cannot be e-mailed to any inside or outside party."
        ],
        "correct": "C",
        "option_explanations": {
            "A) Yes, but the document must be encrypted first.": "Incorrect – The marking alone does not indicate whether encryption is sufficient.",
            "B) Yes, the document can be e-mailed to an outside party in plaintext.": "Incorrect – The marking alone does not grant permission.",
            "C) This cannot be determined without first consulting the data classification and handling policy.": "Correct – A simple marking on a document such as \"Confidential\" does not by itself reveal what handling is permitted. An employee would need to consult a data classification and handling policy to see what actions are permitted.",
            "D) No, the document cannot be e-mailed to any inside or outside party.": "Incorrect – The marking itself does not dictate specific handling; the policy must be consulted."
        }
    },
    {
        "id": 75,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "An auditor has completed an audit of an organization's use of a tool that generates SSL certificates for its external web sites. The auditor has determined that key management procedures are insufficient and that split custody of the key generation procedure is required. How might this be implemented?",
        "options": [
            "A) Of two engineers, one creates the certificate and the other verifies its creation.",
            "B) Of two engineers, each performs half of the procedure used to create a new certificate.",
            "C) Of two engineers, each has one half of the password required to create a new certificate.",
            "D) Of two engineers, one approves the creation of the certificate and the other creates the certificate."
        ],
        "correct": "C",
        "option_explanations": {
            "A) Of two engineers, one creates the certificate and the other verifies its creation.": "Incorrect – This is separation of duties, not split custody.",
            "B) Of two engineers, each performs half of the procedure used to create a new certificate.": "Incorrect – This is also separation of duties, not split custody.",
            "C) Of two engineers, each has one half of the password required to create a new certificate.": "Correct – Split custody refers to the concept of splitting knowledge of a key task, such as two halves of a safe combination or two halves of a password. This requires that both parties cooperate to complete a sensitive task.",
            "D) Of two engineers, one approves the creation of the certificate and the other creates the certificate.": "Incorrect – This is separation of duties, not split custody."
        }
    },
    {
        "id": 76,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "An organization that issues digital certificates recently discovered that a digital certificate was issued to an unauthorized party. What is the appropriate response?",
        "options": [
            "A) Create a CRLF entry.",
            "B) Create a CRL entry.",
            "C) Notify all certificate holders.",
            "D) Call a press conference."
        ],
        "correct": "B",
        "option_explanations": {
            "A) Create a CRLF entry.": "Incorrect – CRLF is shorthand for \"carriage return, line feed,\" a character sequence found in text files.",
            "B) Create a CRL entry.": "Correct – Creating an entry in the certificate revocation list (CRL) is the appropriate response. In the future, when any party attempts to verify the integrity of the certificate, its presence in the CRL will render it invalid.",
            "C) Notify all certificate holders.": "Incorrect – Notifying other certificate holders does not remedy the situation.",
            "D) Call a press conference.": "Incorrect – Calling a press conference does not effectively remedy the situation."
        }
    },
    {
        "id": 77,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "Why is it important for a web session cookie to be encrypted?",
        "options": [
            "A) Parties that can observe the communication will not be able to hijack the session.",
            "B) Parties that observe the communication will not be able to view the user's password.",
            "C) Third parties will not be able to push unsolicited advertising to the user.",
            "D) The web site operator will not be able to record the user's session."
        ],
        "correct": "A",
        "option_explanations": {
            "A) Parties that can observe the communication will not be able to hijack the session.": "Correct – When a user's session cookie is encrypted, another party that can observe the communication will not be able to hijack the user's session. The Firesheep tool is a proof-of-concept tool that was developed to demonstrate this technique.",
            "B) Parties that observe the communication will not be able to view the user's password.": "Incorrect – Encrypting a session cookie does not imply that the remainder of the communications is also encrypted.",
            "C) Third parties will not be able to push unsolicited advertising to the user.": "Incorrect – Encrypting a session cookie does not prevent advertising.",
            "D) The web site operator will not be able to record the user's session.": "Incorrect – Encrypting a session cookie does not prevent the web site operator from recording the user's session."
        }
    },
    {
        "id": 78,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "Why would a hypervisor conceal its existence from a guest OS?",
        "options": [
            "A) To prevent the guest OS from breaking out of the container.",
            "B) To improve the performance of the guest OS.",
            "C) To avoid letting an intruder know that the OS is part of a virtualized environment.",
            "D) To let an intruder know that the OS is part of a virtualized environment."
        ],
        "correct": "C",
        "option_explanations": {
            "A) To prevent the guest OS from breaking out of the container.": "Incorrect – This does not prevent an intruder from breaking out of the guest environment.",
            "B) To improve the performance of the guest OS.": "Incorrect – This has no effect on guest OS performance.",
            "C) To avoid letting an intruder know that the OS is part of a virtualized environment.": "Correct – Concealing the existence of the virtualized environment may lead an intruder to believe that the OS is running on bare metal. This is a security-by-obscurity tactic that does not prevent an intruder from attempting to break into the hypervisor.",
            "D) To let an intruder know that the OS is part of a virtualized environment.": "Incorrect – Concealing this does not reveal it to an intruder."
        }
    },
    {
        "id": 79,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "How can an organization prevent employees from connecting to the corporate Exchange e-mail environment with personally owned mobile devices?",
        "options": [
            "A) Implement multifactor authentication.",
            "B) Permit only Outlook clients to connect to the Exchange server.",
            "C) Encrypt OWA traffic.",
            "D) Put the OWA server behind the firewall and VPN switch."
        ],
        "correct": "D",
        "option_explanations": {
            "A) Implement multifactor authentication.": "Incorrect – Implementing MFA does nothing to prevent personally owned mobile devices from connecting to the Exchange server.",
            "B) Permit only Outlook clients to connect to the Exchange server.": "Incorrect – There is not a reliable way of preventing non-Outlook clients from connecting to the Exchange server.",
            "C) Encrypt OWA traffic.": "Incorrect – Encrypting OWA traffic does nothing to prevent personally owned mobile devices from connecting to the Exchange server.",
            "D) Put the OWA server behind the firewall and VPN switch.": "Correct – By putting the OWA server behind the firewall and the VPN switch, the organization prevents personally owned mobile devices from reaching the OWA server—provided the VPN switch is configured to permit only company-managed devices to connect."
        }
    },
    {
        "id": 80,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "What is the purpose of the Firesheep tool?",
        "options": [
            "A) It demonstrates the dangers of non-encrypted web sessions.",
            "B) It is used as an alternative browser to Firefox to illustrate security concepts.",
            "C) It is used to analyze firewall rules.",
            "D) It is used to back up firewall rules."
        ],
        "correct": "A",
        "option_explanations": {
            "A) It demonstrates the dangers of non-encrypted web sessions.": "Correct – Firesheep is a proof-of-concept tool used to demonstrate how easy it is to hijack unencrypted user sessions on a Wi-Fi network.",
            "B) It is used as an alternative browser to Firefox to illustrate security concepts.": "Incorrect – Firesheep is not a browser.",
            "C) It is used to analyze firewall rules.": "Incorrect – Firesheep is not a firewall management tool.",
            "D) It is used to back up firewall rules.": "Incorrect – Firesheep is not a backup tool."
        }
    },
    {
        "id": 81,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "An organization is implementing a new SIEM. How must engineers get log data from systems and devices to the SIEM?",
        "options": [
            "A) Install agents on all systems and devices.",
            "B) Send them via Windows events.",
            "C) Send them via syslog.",
            "D) Send them via syslog and Windows events."
        ],
        "correct": "D",
        "option_explanations": {
            "A) Install agents on all systems and devices.": "Incorrect – Agents, while they may provide additional functionality, are not required to get basic log data from systems and devices.",
            "B) Send them via Windows events.": "Incorrect – Syslog can also be used to send log data to a SIEM.",
            "C) Send them via syslog.": "Incorrect – Windows events can also be used to send log data to a SIEM.",
            "D) Send them via syslog and Windows events.": "Correct – Any SIEM can accept log entries sent via syslog and Windows events."
        }
    },
    {
        "id": 82,
        "domain": "Domain 5 – Information Asset Protection",
        "question": "What is the appropriate consequence of SOC operators declaring incidents that turn out to be false positives?",
        "options": [
            "A) Additional training to improve their incident-handling skills.",
            "B) Termination of employment.",
            "C) Removal of incident declaration privileges.",
            "D) No consequence, as false positives are a part of business as usual."
        ],
        "correct": "A",
        "option_explanations": {
            "A) Additional training to improve their incident-handling skills.": "Correct – If SOC operators chronically declare incidents where none exist, this suggests that they need additional training to better recognize and distinguish real incidents from false positives. A false positive now and then should not be a big deal.",
            "B) Termination of employment.": "Incorrect – Termination of employment is an unreasonably harsh consequence.",
            "C) Removal of incident declaration privileges.": "Incorrect – Removal of incident declaration privileges is too harsh.",
            "D) No consequence, as false positives are a part of business as usual.": "Incorrect – The number of false positives is high, indicating a need for improvement."
        }
    }
]

# ========== STREAMLIT APP ==========
st.set_page_config(page_title="CISA Practice Exam", layout="wide")

# Helper: remove "A) " or "A)" prefix
def strip_option_prefix(text):
    return re.sub(r"^[A-D]\)\s*", "", text)

# ------------------------------------------------------------
# Sidebar: Domain filter + number-of-questions + start button
# ------------------------------------------------------------
all_domains = sorted({q["domain"] for q in QUESTIONS})

# Always show the multiselect
selected_domains = st.sidebar.multiselect(
    "Filter by Domain",
    options=all_domains,
    default=all_domains,
    key="domain_filter"
)

# Determine the pool of questions that match the selected domains
filtered_pool = [q for q in QUESTIONS if q["domain"] in selected_domains]
total_available = len(filtered_pool)

# Number of questions slider
num_questions = st.sidebar.slider(
    "Number of questions",
    min_value=1,
    max_value=max(1, total_available),       # max must be at least 1
    value=min(20, total_available),
    step=1,
    key="num_questions_slider"
)

# Start button: create a new random sample from the pool
if st.sidebar.button("Start Quiz"):
    # Take a random sample (if the desired number <= total_available)
    sample_size = min(num_questions, total_available)
    st.session_state.questions = random.sample(filtered_pool, sample_size)
    random.shuffle(st.session_state.questions)
    st.session_state.idx = 0
    st.session_state.answered = False
    st.session_state.score = 0
    st.session_state.shuffled_data = None
    st.session_state.filtered = True   # mark that a quiz is active

# Fallback: if the session hasn't been initialised (first load) or the button hasn't been pressed yet
if "questions" not in st.session_state or len(st.session_state.questions) == 0:
    # Default: take up to 20 questions from the whole pool
    default_size = min(20, total_available)
    if default_size > 0:
        st.session_state.questions = random.sample(filtered_pool, default_size)
        random.shuffle(st.session_state.questions)
    else:
        st.session_state.questions = []
    st.session_state.idx = 0
    st.session_state.answered = False
    st.session_state.score = 0
    st.session_state.shuffled_data = None

total = len(st.session_state.questions)

if total == 0:
    st.warning("No questions available for the selected domains.")
    st.stop()

# ------------------------------------------------------------
# The rest of the quiz (unchanged from your existing code)
# ------------------------------------------------------------
q = st.session_state.questions[st.session_state.idx]

# Prepare shuffled options (if not already set)
if st.session_state.shuffled_data is None:
    correct_letter = q["correct"]
    correct_raw = q["options"][ord(correct_letter) - ord("A")]
    opts_with_flag = []
    for opt in q["options"]:
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

# ----- OPTIONS AREA -----
if not st.session_state.answered:
    selected = st.radio(
        "Select your answer:",
        radio_choices,
        index=None,
        key=f"radio_{st.session_state.idx}"
    )

    col1, col2 = st.columns([1, 2])
    if col1.button("Submit", use_container_width=True):
        if selected is not None:
            selected_label = selected[0]
            selected_idx = labels.index(selected_label)
            st.session_state.selected_idx = selected_idx
            st.session_state.answered = True
            if shuffled[selected_idx][2]:
                st.session_state.score += 1
            st.rerun()
        else:
            st.warning("Please select an answer first.")
else:
    # Inline feedback (unchanged)
    selected_idx = st.session_state.selected_idx
    explanations = q.get("option_explanations", {})
    for i, (orig_text, stripped_text, is_correct) in enumerate(shuffled):
        letter = labels[i]
        display_text = f"{letter}) {stripped_text}"
        explanation = explanations.get(orig_text, "")
        if is_correct:
            st.success(f"**{display_text}**  \n{explanation}")
        elif i == selected_idx and not is_correct:
            st.error(f"**{display_text}**  \n{explanation}")
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
            # Restart with the same pool and settings
            sample_size = min(num_questions, total_available)
            st.session_state.questions = random.sample(filtered_pool, sample_size)
            random.shuffle(st.session_state.questions)
            st.session_state.idx = 0
            st.session_state.score = 0
            st.session_state.answered = False
            st.session_state.shuffled_data = None
            st.rerun()
