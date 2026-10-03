# Microsoft Purview Asset Catalog

## Overview

This document represents the cataloguing approach for the synthetic banking datasets used in this Microsoft Purview Data Governance portfolio project.

The objective is to demonstrate how data assets can be documented with business context, ownership, Critical Data Elements (CDEs), classifications and data quality information to improve data discovery and governance.

---

## Governance Domain

**Domain:** Customer Data

**Purpose:** Govern customer-related data used across customer master, account and KYC processes.

---

## Asset 1: Customer Master

**Asset Name:** Customer Master  
**Physical Asset:** customer_data_100.csv  
**Asset Type:** CSV Dataset  
**Business Domain:** Customer Data  
**Business Owner:** Customer Data Owner  
**Data Steward:** Customer Data Steward  

### Business Description

Customer Master contains the core customer information used to identify and manage customers across downstream account and KYC processes.

### Critical Data Elements

- Customer_ID
- Customer_Name
- Date_of_Birth
- Country_Code
- Customer_Status

### Data Classifications

- Customer Identifier
- Personal Data
- Contact Information
- Internal Data

### Key Data Quality Controls

- Customer_ID must be complete and unique.
- Date_of_Birth must be populated and contain a valid past date.
- Country_Code must conform to approved reference values.
- Customer_Status must contain an approved business value.

---

## Asset 2: Account Data

**Asset Name:** Account Data  
**Physical Asset:** account_data_100.csv  
**Asset Type:** CSV Dataset  
**Business Domain:** Customer Data  
**Business Owner:** Account Data Owner  
**Data Steward:** Account Data Steward  

### Business Description

Account Data contains account information associated with customers in the Customer Master.

### Critical Data Elements

- Account_ID
- Customer_ID
- Currency
- Account_Status

### Data Classifications

- Account Identifier
- Customer Identifier
- Internal Financial Data

### Key Data Quality Controls

- Account_ID must be complete and unique.
- Customer_ID must exist in Customer Master.
- Currency must conform to approved currency values.
- Account_Status must contain an approved business value.

---

## Asset 3: KYC Data

**Asset Name:** KYC Data  
**Physical Asset:** kyc_data_100.csv  
**Asset Type:** CSV Dataset  
**Business Domain:** Customer Data  
**Business Owner:** KYC Data Owner  
**Data Steward:** KYC Data Steward  

### Business Description

KYC Data contains customer verification, risk-rating and review information used to support customer due-diligence processes.

### Critical Data Elements

- Customer_ID
- KYC_Status
- Customer_Risk_Rating
- Last_Review_Date

### Data Classifications

- Customer Identifier
- KYC Data
- Risk Data
- Confidential Data

### Key Data Quality Controls

- Customer_ID must exist in Customer Master.
- KYC_Status must be complete and use an approved status.
- Customer_Risk_Rating must use an approved risk-rating value.
- Last_Review_Date must contain a valid date and meet the applicable review-frequency rule.

---

## Asset Relationships

Customer Master acts as the authoritative customer source for this portfolio scenario.

Customer_ID connects:

Customer Master → Account Data

Customer Master → KYC Data

These relationships support lineage analysis and referential-integrity controls.

---

## Microsoft Purview Alignment

In a Microsoft Purview implementation, these assets can be registered and discovered through the data catalog with supporting metadata such as:

- Business descriptions
- Data owners and stewards
- Classifications
- Critical Data Elements
- Business glossary terms
- Data lineage
- Data quality information

This portfolio uses synthetic data and demonstrates a representative enterprise data-governance scenario.
