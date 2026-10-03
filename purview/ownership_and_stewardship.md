# Data Ownership and Stewardship

## Overview

Clear ownership and stewardship help ensure that governed data has defined accountability for business meaning, quality, controls and issue remediation.

This portfolio assigns representative Data Owner and Data Steward roles to the Customer, Account and KYC data assets.

## Governance Roles

| Data Asset | Data Owner | Data Steward | Key Responsibilities |
|---|---|---|---|
| Customer Master | Customer Data Owner | Customer Data Steward | Business definitions, CDE approval, DQ thresholds, customer data governance |
| Account Data | Account Data Owner | Account Data Steward | Account definitions, account CDEs, DQ monitoring and remediation |
| KYC Data | KYC Data Owner | KYC Data Steward | KYC definitions, risk data standards, DQ controls and remediation |

## Data Owner Responsibilities

The Data Owner provides business accountability for the governed data.

Responsibilities include:

- Approving business definitions
- Identifying and approving Critical Data Elements
- Agreeing data quality requirements and thresholds
- Reviewing significant data quality issues
- Supporting remediation prioritisation
- Approving appropriate data usage and governance requirements
- Working with technology, risk and business stakeholders

## Data Steward Responsibilities

The Data Steward supports the day-to-day implementation of governance requirements.

Responsibilities include:

- Maintaining metadata and business definitions
- Monitoring data quality controls
- Investigating data quality exceptions
- Coordinating remediation activities
- Maintaining issue evidence
- Supporting lineage and data discovery
- Escalating material issues to the Data Owner

## Example Governance Issue

Data quality analysis identified duplicate Customer_ID CUST079 in Customer Master.

The issue resulted in the expected CUST080 master record being absent, causing referential-integrity failures in Account and KYC data.

The Customer Data Steward would coordinate investigation of the source records and document the issue.

The Customer Data Owner would provide business oversight for the remediation where required.

Account and KYC Data Stewards would validate the affected downstream relationships after the upstream issue was corrected.

## Microsoft Purview Alignment

Ownership and stewardship information can be associated with governed data assets and business concepts to help users understand accountability and identify the appropriate contacts when questions or data issues arise.

## Portfolio Note

The roles and responsibilities in this project are representative examples using synthetic data and are not based on a specific organisation's operating model.
