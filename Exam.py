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
