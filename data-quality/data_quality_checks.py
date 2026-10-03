import pandas as pd

# --------------------------------------------------
# Load datasets
# --------------------------------------------------

customer = pd.read_csv("customer_data_100.csv")
account = pd.read_csv("account_data_100.csv")
kyc = pd.read_csv("kyc_data_100.csv")

print("Data Quality Assessment")
print("=" * 50)


# --------------------------------------------------
# 1. Customer ID Completeness
# --------------------------------------------------

missing_customer_id = customer["Customer_ID"].isna().sum()

print(
    "Customer_ID Completeness:",
    "PASS" if missing_customer_id == 0 else "FAIL"
)


# --------------------------------------------------
# 2. Customer ID Uniqueness
# --------------------------------------------------

duplicate_customer_records = customer[
    customer["Customer_ID"].duplicated(keep=False)
]

print(
    "Customer_ID Uniqueness:",
    "PASS" if len(duplicate_customer_records) == 0 else "FAIL",
    "- Failed records:",
    len(duplicate_customer_records)
)


# --------------------------------------------------
# 3. Date of Birth Completeness
# --------------------------------------------------

missing_dob = customer["Date_of_Birth"].isna().sum()

print(
    "Date_of_Birth Completeness:",
    "PASS" if missing_dob == 0 else "FAIL",
    "- Missing:",
    missing_dob
)


# --------------------------------------------------
# 4. Country Code Validity
# --------------------------------------------------

valid_country_codes = ["GB", "IE", "FR"]

invalid_country = customer[
    ~customer["Country_Code"].isin(valid_country_codes)
]

print(
    "Country_Code Validity:",
    "PASS" if len(invalid_country) == 0 else "FAIL",
    "- Invalid:",
    len(invalid_country)
)


# --------------------------------------------------
# 5. KYC Status Completeness
# --------------------------------------------------

missing_kyc_status = kyc["KYC_Status"].isna().sum()

print(
    "KYC_Status Completeness:",
    "PASS" if missing_kyc_status == 0 else "FAIL",
    "- Missing:",
    missing_kyc_status
)


# --------------------------------------------------
# 6. Customer Risk Rating Validity
# --------------------------------------------------

valid_risk_ratings = ["Low", "Medium", "High"]

invalid_risk = kyc[
    ~kyc["Customer_Risk_Rating"].isin(valid_risk_ratings)
]

print(
    "Customer_Risk_Rating Validity:",
    "PASS" if len(invalid_risk) == 0 else "FAIL",
    "- Invalid:",
    len(invalid_risk)
)


# --------------------------------------------------
# 7. Account → Customer Referential Integrity
# --------------------------------------------------

invalid_account_customers = account[
    ~account["Customer_ID"].isin(customer["Customer_ID"])
]

print(
    "Account Customer_ID Referential Integrity:",
    "PASS" if len(invalid_account_customers) == 0 else "FAIL",
    "- Invalid:",
    len(invalid_account_customers)
)


# --------------------------------------------------
# 8. KYC → Customer Referential Integrity
# --------------------------------------------------

invalid_kyc_customers = kyc[
    ~kyc["Customer_ID"].isin(customer["Customer_ID"])
]

print(
    "KYC Customer_ID Referential Integrity:",
    "PASS" if len(invalid_kyc_customers) == 0 else "FAIL",
    "- Invalid:",
    len(invalid_kyc_customers)
)

print("=" * 50)
print("Assessment complete.")