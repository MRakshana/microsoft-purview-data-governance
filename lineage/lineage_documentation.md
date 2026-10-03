# Customer Data Lineage

## Overview

This lineage demonstrates how customer data flows across the synthetic
Customer Master, Account and KYC datasets used in this portfolio project.

The objective is to understand upstream and downstream dependencies,
identify Critical Data Elements (CDEs), apply data quality controls and
support root-cause analysis of data quality issues.

## Data Flow

Customer Master is treated as the authoritative customer source.

Customer_ID is the primary identifier used to connect customer records
with Account and KYC data.

Customer Master
→ Account Data
→ KYC Data
→ Data Quality Controls
→ Governed / Trusted Data
→ Reporting and Analytics

## Critical Data Element

Customer_ID is a key CDE because it enables customer records to be
consistently linked across Customer Master, Account and KYC datasets.

## Data Quality Controls

The lineage is supported by controls covering:

- Completeness
- Uniqueness
- Validity
- Consistency
- Referential Integrity
- Timeliness

## Root Cause Analysis Example

Data quality profiling identified duplicate Customer_ID CUST079 in
Customer Master.

As a result, the expected CUST080 customer master record is missing.

Account and KYC records containing CUST080 therefore fail referential
integrity checks because they cannot be matched to Customer Master.

Additional orphan references CUST999 in Account and CUST998 in KYC
were also identified and require investigation.

## Remediation Approach

The proposed remediation process is:

1. Validate the duplicate CUST079 records.
2. Correct the customer identifier after source validation.
3. Restore the appropriate CUST080 master record where confirmed.
4. Investigate CUST999 and CUST998 with the relevant data owners.
5. Re-run data quality controls.
6. Record remediation evidence and update issue status.

## Microsoft Purview Alignment

In a Microsoft Purview implementation, lineage and metadata can support
understanding of where critical data originates, how it is used across
data assets, who owns it and what downstream processes may be affected
when a data quality issue occurs.

This portfolio uses synthetic data and demonstrates a representative
data governance scenario.
