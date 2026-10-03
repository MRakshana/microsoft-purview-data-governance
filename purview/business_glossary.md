# Microsoft Purview Business Glossary

## Overview

This business glossary defines key business terms used within the Customer Data governance domain.

The purpose of the glossary is to provide consistent business definitions so that data owners, data stewards, analysts and technology teams interpret critical data in the same way.

---

## 1. Customer

**Definition:**  
An individual whose information is maintained within the Customer Master and may be associated with account and KYC records.

**Business Domain:** Customer Data  
**Business Owner:** Customer Data Owner  
**Related Asset:** Customer Master

---

## 2. Customer ID

**Definition:**  
A unique identifier assigned to a customer and used to link the customer across Customer Master, Account and KYC datasets.

**Business Domain:** Customer Data  
**Business Owner:** Customer Data Owner  
**Data Steward:** Customer Data Steward  
**Critical Data Element:** Yes

**Related Assets:**
- Customer Master
- Account Data
- KYC Data

**Data Quality Requirements:**
- Must not be blank.
- Must be unique in Customer Master.
- Customer IDs used by downstream datasets must exist in Customer Master.

---

## 3. Date of Birth

**Definition:**  
The recorded date of birth of a customer.

**Business Domain:** Customer Data  
**Business Owner:** Customer Data Owner  
**Critical Data Element:** Yes  
**Classification:** Personal Data

**Data Quality Requirements:**
- Must be populated.
- Must contain a valid past date.

---

## 4. Country Code

**Definition:**  
The standardised code representing the customer's recorded country.

**Business Domain:** Customer Data  
**Critical Data Element:** Yes

**Approved Values for this Portfolio:**
- GB
- IE
- FR

**Data Quality Requirements:**
- Must not be blank.
- Must conform to the approved reference values.

---

## 5. KYC Status

**Definition:**  
The current status of the customer Know Your Customer verification process.

**Business Domain:** Customer Data / KYC  
**Business Owner:** KYC Data Owner  
**Data Steward:** KYC Data Steward  
**Critical Data Element:** Yes  
**Classification:** KYC Data

**Approved Values:**
- Verified
- Pending
- Expired

**Data Quality Requirements:**
- Must be populated.
- Must contain an approved status.

---

## 6. Customer Risk Rating

**Definition:**  
The customer risk category assigned as part of the KYC and customer due-diligence process.

**Business Domain:** KYC  
**Business Owner:** KYC Data Owner  
**Data Steward:** KYC Data Steward  
**Critical Data Element:** Yes  
**Classification:** Risk Data

**Approved Values:**
- Low
- Medium
- High

**Data Quality Requirements:**
- Must be populated.
- Must conform to the approved risk-rating values.
- Values must be consistently represented across governed datasets.

---

## 7. Account Status

**Definition:**  
The current business status of a customer account.

**Business Domain:** Customer Data / Account  
**Business Owner:** Account Data Owner  
**Data Steward:** Account Data Steward  
**Critical Data Element:** Yes

**Data Quality Requirements:**
- Must be populated.
- Must contain an approved account status.

---

## 8. Critical Data Element (CDE)

**Definition:**  
A data element identified as important because data quality issues affecting the element could materially impact business processes, reporting, risk management, customer outcomes or governance controls.

**Business Domain:** Enterprise Data Governance

**Examples in this project:**
- Customer_ID
- Date_of_Birth
- Country_Code
- KYC_Status
- Customer_Risk_Rating
- Account_Status

---

## Glossary Governance

Business glossary terms should be reviewed with the relevant Data Owner and Data Steward.

Changes to definitions, approved values or data-quality requirements should be documented and communicated to stakeholders to maintain consistent interpretation and usage of governed data.

---

## Portfolio Note

This glossary uses synthetic banking data and demonstrates how business terminology could be documented and governed using Microsoft Purview concepts.
