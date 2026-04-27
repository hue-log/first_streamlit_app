import streamlit as st
import random
import re

# ========== ALL 63 QUESTIONS FROM DOMAIN 1 – THE AUDIT PROCESS ==========
# Each question contains:
#   - id, domain, question text
#   - options (each prefixed with "A) ", "B) ", etc.)
#   - correct answer letter (A/B/C/D)
#   - option_explanations dictionary mapping the full option text to its explanation

DOMAIN1_QUESTIONS = [
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
    }
]

    # Domain 2 – IT Governance and Management
DOMAIN2_QUESTIONS = [
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
]
    # Domain 3 – IT Life Cycle Management
DOMAIN3_QUESTIONS = [
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
]
    # Domain 4 – IT Service Management and Continuity
DOMAIN4_QUESTIONS = [
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
]
    # Domain 5 – Information Asset Protection
DOMAIN5_QUESTIONS = [
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

# Session state init
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
    st.session_state.shuffled_data = None  # [(original, stripped, is_correct), ...]

# Helper: remove "A) " or "A)" prefix
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
    # Show radio buttons
    selected = st.radio(
        "Select your answer:",
        radio_choices,
        index=None,
        key=f"radio_{st.session_state.idx}"
    )

    col1, col2 = st.columns([1, 2])
    if col1.button("Submit", use_container_width=True):
        if selected is not None:
            selected_label = selected[0]             # "A", "B", ...
            selected_idx = labels.index(selected_label)
            st.session_state.selected_idx = selected_idx
            st.session_state.answered = True
            if shuffled[selected_idx][2]:            # is_correct?
                st.session_state.score += 1
            st.rerun()
        else:
            st.warning("Please select an answer first.")
else:
    # ----- INLINE FEEDBACK (replaces radio) -----
    selected_idx = st.session_state.selected_idx
    explanations = q.get("option_explanations", {})

    for i, (orig_text, stripped_text, is_correct) in enumerate(shuffled):
        letter = labels[i]
        display_text = f"{letter}) {stripped_text}"
        # Use original text (with prefix) to look up explanation
        explanation = explanations.get(orig_text, "")

        if is_correct:
            st.success(f"**{display_text}**  \n{explanation}")
        elif i == selected_idx and not is_correct:
            st.error(f"**{display_text}**  \n{explanation}")
        else:
            st.error(f"**{display_text}**  \n{explanation}")

    # Navigation buttons (always placed after the feedback)
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
