# microsoft-purview-data-governance
Microsoft Purview Data Discovery &amp; Governance project demonstrating metadata management, data cataloguing, classification, ownership, CDEs, lineage and data quality.
This portfolio project uses synthetic data and recreates a representative enterprise data-governance scenario.
# Microsoft Purview – Data Discovery & Governance Project

## Project Overview

This project demonstrates an end-to-end Data Discovery and Data Governance use case using Microsoft Purview concepts.

The objective is to demonstrate how enterprise customer data can be discovered, catalogued, classified, documented and governed so that data consumers can easily understand what data exists, where it comes from, who owns it and whether it is suitable for use.

The project is based on my hands-on experience with data governance, data ownership, metadata management and data quality, and has been recreated using synthetic banking data for portfolio purposes.

> **Note:** All datasets used in this repository are synthetic. No confidential, proprietary or customer information from any organisation is included.

---

## Business Problem

Customer information is often distributed across multiple systems such as customer onboarding, KYC, account management and reporting platforms.

Without effective data governance, users may struggle to answer questions such as:

- What customer data is available?
- Where does the data originate?
- What does each data element mean?
- Which fields are Critical Data Elements (CDEs)?
- Who owns the data?
- Does the dataset contain sensitive information?
- What is the lineage of the data?
- Can the data be trusted for business and analytical use?

This project demonstrates how Microsoft Purview and data governance practices can help address these challenges.

---

## Project Scope

The project covers:

- Data Discovery
- Microsoft Purview Data Catalog
- Business and Technical Metadata
- Data Classification
- Business Glossary
- Data Ownership & Stewardship
- Critical Data Elements (CDEs)
- Data Lineage
- Data Quality Rules
- Data Issue Management & Remediation
- Data Governance Controls

---

## Data Domain

**Domain:** Customer Data

The project uses synthetic datasets representing:

- Customer Master Data
- Customer Account Data
- KYC / Customer Due Diligence Data

Example data elements include:

`Customer_ID`

`Customer_Name`

`Date_of_Birth`

`Email_Address`

`Phone_Number`

`Country`

`KYC_Status`

`Customer_Risk_Rating`

`Account_ID`

`Account_Status`

---

## Data Discovery with Microsoft Purview

The data discovery process demonstrates how data assets can be identified and made easier for users to understand through:

1. Data source registration
2. Data scanning
3. Asset discovery
4. Metadata extraction
5. Data classification
6. Business descriptions
7. Ownership assignment
8. Glossary association
9. Data lineage
10. Catalogue search and discovery

The objective is to enable data consumers to discover relevant datasets and understand their business context before using them.

---

## Governance Framework

The project applies governance controls around:

**Ownership**

Clear Data Owner and Data Steward responsibilities.

**Metadata**

Business and technical descriptions for important data elements.

**Critical Data Elements**

Identification of data elements that are important for business, regulatory or operational processes.

**Data Quality**

Rules and thresholds covering completeness, accuracy, consistency, validity and timeliness.

**Classification**

Identification and appropriate classification of sensitive customer information.

**Lineage**

Documentation of how data moves from source systems through transformation and downstream consumption.

---

## Tools & Technologies

- Microsoft Purview
- SQL
- Python
- Pandas
- Power BI
- Microsoft Excel
- GitHub

---

## Repository Structure

```text
microsoft-purview-data-governance/
│
├── README.md
├── data/
├── metadata/
├── data-quality/
├── lineage/
├── purview/
└── src/

