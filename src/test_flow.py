import pandas as pd

print("Testing the complete flow...")
print("=" * 50)

# Test 1: Check if input file exists
try:
    df_input = pd.read_csv("data/FO_Coding_Assignment.csv")
    print(f"✓ Input file loaded: {len(df_input)} records")
except:
    print("✗ Input file not found")

# Test 2: Run data splitting
import data_split
print("\n✓ Data splitting completed")

# Test 3: Check cleaned data
try:
    df_cleaned = pd.read_csv("output/cleaned_data.csv")
    print(f"✓ Cleaned data: {len(df_cleaned)} split records")
    print(f"  Sample rounds: {df_cleaned['Interview Round'].unique()[:5]}")
except:
    print("✗ Cleaned data not found")

# Test 4: Check email data
try:
    df_email = pd.read_csv("output/cleaned_data_with_mail_time.csv")
    emails_sent = df_email['Mail Sent Time'].notna().sum()
    print(f"✓ Email data: {emails_sent}/{len(df_email)} emails marked as sent")
except:
    print("✗ Email data not found")

# Test 5: Check final output
try:
    df_final = pd.read_csv("output/final_output_with_tat.csv")
    print(f"✓ Final output: {len(df_final)} records with TAT")
    print(f"  TAT range: {df_final['TAT (Hours)'].min():.2f} to {df_final['TAT (Hours)'].max():.2f} hours")
except:
    print("✗ Final output not found")

print("\n" + "=" * 50)
print("Flow test completed!")