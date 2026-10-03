# Microsoft Purview Data Classifications

## Overview

This document defines the classifications applied to the synthetic Customer, Account and KYC data assets used in this portfolio project.

Classifications help users understand the sensitivity and business context of data discovered through the data catalog.

## Customer Master

| Data Element | Classification | Reason |
|---|---|---|
| Customer_ID | Customer Identifier | Uniquely identifies a customer |
| Customer_Name | Personal Data | Contains an individual's name |
| Date_of_Birth | Personal Data | Contains personal customer information |
| Email_Address | Contact Information | Contains customer contact details |
| Phone_Number | Contact Information | Contains customer contact details |
| Country_Code | Internal Data | Customer reference attribute |
| Customer_Status | Internal Data | Customer lifecycle/status information |

## Account Data

| Data Element | Classification | Reason |
|---|---|---|
| Account_ID | Account Identifier | Uniquely identifies an account |
| Customer_ID | Customer Identifier | Links account to customer |
| Account_Type | Internal Financial Data | Describes account category |
| Currency | Internal Financial Data | Identifies account currency |
| Account_Status | Internal Financial Data | Describes account status |
| Open_Date | Internal Financial Data | Records account opening date |

## KYC Data

| Data Element | Classification | Reason |
|---|---|---|
| KYC_ID | Internal Identifier | Identifies the KYC record |
| Customer_ID | Customer Identifier | Links KYC record to customer |
| KYC_Status | KYC Data | Represents verification status |
| Customer_Risk_Rating | Risk Data | Represents customer risk category |
| Last_Review_Date | KYC Data | Records KYC review information |
| ID_Document_Type | KYC Data | Describes identification document type |

## Classification Approach

Classifications are assigned according to the business meaning and sensitivity of each data element.

In a Microsoft Purview implementation, classification can support:

- Sensitive-data discovery
- Catalog search and filtering
- Data protection decisions
- Governance and ownership processes
- Risk and compliance activities

## Portfolio Note

The classifications in this project are illustrative and applied to synthetic data for portfolio purposes. They do not represent a specific organisation's classification policy.
