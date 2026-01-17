import pandas as pd
from datetime import datetime

INPUT_FILE = "output/cleaned_data_with_mail_time.csv"
OUTPUT_FILE = "output/final_output_with_tat.csv"

# Load data
df = pd.read_csv(INPUT_FILE)

# Convert "Added On" to datetime (format: "04 Nov 1:18" - from November 2024)
def parse_added_on(date_str):
    try:
        # Format: "DD MMM HH:MM" - assuming year is 2024 based on the data
        return datetime.strptime(f"{date_str} 2024", "%d %b %H:%M %Y")
    except Exception as e:
        print(f"Error parsing date '{date_str}': {e}")
        return pd.NaT

# Convert timestamps
df["Added On Parsed"] = df["Added On"].apply(parse_added_on)
df["Mail Sent Time Parsed"] = pd.to_datetime(df["Mail Sent Time"])

# Calculate TAT in hours
df["TAT (Hours)"] = (
    df["Mail Sent Time Parsed"] - df["Added On Parsed"]
).dt.total_seconds() / 3600

# Save final output with all columns
final_columns = [
    "Candidate Name", "Candidate Email", "Company", 
    "Interview Round", "Calendly Link", "Added On", 
    "Mail Sent Time", "TAT (Hours)"
]

df[final_columns].to_csv(OUTPUT_FILE, index=False)

# Print summary statistics
print("Task 3 completed: TAT calculated successfully.")
print(f"Output saved to {OUTPUT_FILE}")
print(f"\nTAT Statistics:")
print(f"Minimum TAT: {df['TAT (Hours)'].min():.2f} hours")
print(f"Maximum TAT: {df['TAT (Hours)'].max():.2f} hours")
print(f"Average TAT: {df['TAT (Hours)'].mean():.2f} hours")
print(f"Median TAT: {df['TAT (Hours)'].median():.2f} hours")