# Microsoft Purview Data Governance & Data Quality Portfolio

An end-to-end data governance portfolio project demonstrating how banking customer data can be discovered, catalogued, classified, owned, monitored and governed using Microsoft Purview-aligned concepts.

The project uses fully synthetic Customer, Account and KYC datasets and combines governance documentation with practical Python-based data quality controls.

> **Portfolio note:** All data in this repository is synthetic. No employer, customer, confidential or production data is included.

---

## Project Overview

Financial organisations depend on trusted customer data across onboarding, account servicing, KYC, risk management and reporting.

This project demonstrates governance across three connected data assets:

- Customer Master
- Account Data
- KYC Data

The project covers Critical Data Elements (CDEs), metadata, business glossary, classification, ownership and stewardship, lineage, data quality controls, issue management and remediation.

---

## Data Assets

| Dataset | Records | Purpose |
|---|---:|---|
| Customer Master | 100 | Core customer identification and lifecycle information |
| Account Data | 100 | Customer account information |
| KYC Data | 100 | KYC verification, review and customer risk information |

**Total: 300 synthetic records**

Customer Master acts as the primary customer source, with `Customer_ID` connecting Account and KYC data.

---

## Critical Data Elements

13 CDEs were identified across the three data assets.

Examples include:

`Customer_ID` • `Customer_Name` • `Date_of_Birth` • `Country_Code` • `Customer_Status` • `Account_ID` • `Currency` • `Account_Status` • `KYC_Status` • `Customer_Risk_Rating` • `Last_Review_Date`

The CDE register documents business definitions, ownership, stewardship, DQ dimensions, rules, thresholds and classifications.

➡️ [View CDE Register](metadata/CDE_Register.xlsx)

---

## Data Quality Assessment

Python and Pandas were used to profile the datasets and automate data quality controls.

| Control | Score | Result |
|---|---:|---|
| Customer_ID Completeness | 100% | PASS |
| Customer_ID Uniqueness | 98% | FAIL |
| Date_of_Birth Completeness | 99% | FAIL |
| Country_Code Validity | 99% | FAIL |
| KYC_Status Completeness | 99% | FAIL |
| Customer_Risk_Rating Validity | 98% | FAIL |
| Account → Customer Referential Integrity | 98% | FAIL |
| KYC → Customer Referential Integrity | 98% | FAIL |

### Evidence

➡️ [Data Quality Analysis Notebook](data-quality/data_quality_analysis.ipynb)

➡️ [Automated Data Quality Checks](data-quality/data_quality_checks.py)

➡️ [DQ Assessment & Issue Register](data-quality/DQ_Assessment.xlsx)

---

## Root Cause Analysis & Remediation

Profiling identified a duplicate `CUST079` identifier in Customer Master.

The expected `CUST080` master record was therefore absent, while downstream Account and KYC records referenced `CUST080`, causing referential-integrity failures.

Additional orphan identifiers `CUST999` and `CUST998` were identified for investigation.

The remediation approach includes source validation, identifier correction, downstream validation, re-running DQ controls and documenting issue closure.

---

## Data Lineage

Lineage was documented to show the relationship between Customer Master, Account and KYC data and to support impact analysis and root-cause investigation.

➡️ [View Lineage Documentation](lineage/lineage_documentation.md)

➡️ [View Lineage Diagram](lineage/customer_data_lineage.png)

---

## Microsoft Purview Governance Design

The project applies Microsoft Purview-aligned governance concepts across the data lifecycle.

### Asset Catalogue
Business descriptions, schemas, ownership, stewardship, CDEs and classifications.

➡️ [View Asset Catalogue](purview/asset_catalog.md)

### Business Glossary
Consistent definitions for key terms including Customer, Customer ID, KYC Status and Customer Risk Rating.

➡️ [View Business Glossary](purview/business_glossary.md)

### Data Classification
Classification of personal data, customer identifiers, contact information, KYC data, risk data and internal financial data.

➡️ [View Classification Framework](purview/classifications.md)

### Ownership & Stewardship
Role-based accountability for definitions, CDEs, data quality monitoring and remediation.

➡️ [View Ownership & Stewardship Model](purview/ownership_and_stewardship.md)

---

## Purview Portfolio Visuals

The following visuals illustrate how the synthetic governed assets could be represented in a Microsoft Purview-style catalogue experience.

> **Important:** These are illustrative portfolio mock-ups based on synthetic data and are not screenshots from an employer or production environment.

### Customer Master

![Customer Master](purview/screenshots/Microsoft%20Purview%20Customer%20Master%20Overview.png)

### Account Data

![Account Data](purview/screenshots/Microsoft%20Purview%20Account%20Data%20Overview.png)

### KYC Data

![KYC Data](purview/screenshots/Microsoft%20Purview%20KYC%20Data%20Dashboard.png)

---

## Governance Lifecycle

**Discover → Identify CDEs → Define Metadata → Assign Ownership → Classify → Define DQ Rules → Profile → Identify Exceptions → Root Cause Analysis → Remediate → Monitor**

---

## Tools & Skills Demonstrated

**Governance:** Microsoft Purview concepts, Data Ownership, Data Stewardship, CDE Management, Metadata Management, Business Glossary, Classification and Lineage

**Data Quality:** Python, Pandas, profiling, DQ rules, thresholds, referential integrity, issue management and remediation

**Documentation:** Jupyter Notebook, Excel, Markdown and GitHub

---

## Repository Structure

```text
microsoft-purview-data-governance/
├── data/
├── metadata/
│   └── CDE_Register.xlsx
├── data-quality/
│   ├── data_quality_analysis.ipynb
│   ├── data_quality_checks.py
│   └── DQ_Assessment.xlsx
├── lineage/
│   ├── customer_data_lineage.png
│   └── lineage_documentation.md
├── purview/
│   ├── asset_catalog.md
│   ├── business_glossary.md
│   ├── classifications.md
│   ├── ownership_and_stewardship.md
│   └── screenshots/
└── README.md
```

---

## Key Skills Demonstrated

Data Governance • Microsoft Purview • Data Ownership • Data Stewardship • Metadata Management • Data Cataloguing • CDE Management • Business Glossary • Data Classification • Data Quality • Data Lineage • Root Cause Analysis • Issue Remediation • Python • Pandas

---

## Disclaimer

This is an independent portfolio project using synthetic banking data for learning and professional demonstration purposes.

No employer, customer, confidential, proprietary or production data is included. Microsoft Purview interface visuals are illustrative portfolio mock-ups.
