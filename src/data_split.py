import pandas as pd
import re
from datetime import datetime

INPUT_FILE = "data/FO_Coding_Assignment.csv"
OUTPUT_FILE = "output/cleaned_data.csv"

# Load data
df = pd.read_csv(INPUT_FILE)

# Clean empty rows
df = df.dropna(subset=['Candidate', 'Candidate Email'])

rows = []

# Split interview rounds
for _, row in df.iterrows():
    candidate_name = row['Candidate']
    candidate_email = row['Candidate Email']
    company = row['Company']
    added_on = row['Added On']
    
    # Parse scheduling method to extract rounds
    scheduling_method = str(row['Scheduling method'])
    
    # Extract rounds using regex (format: RoundX: https://calendly.com/...)
    rounds = re.findall(r'(Round\d+):\s*(https://calendly\.com/\S+)', scheduling_method)
    
    for round_num, calendly_link in rounds:
        rows.append({
            "Candidate Name": candidate_name,
            "Candidate Email": candidate_email,
            "Company": company,
            "Interview Round": round_num,
            "Calendly Link": calendly_link,
            "Added On": added_on,
            "Mail Sent Time": ""  # to be updated later
        })

# Create cleaned dataframe
cleaned_df = pd.DataFrame(rows)

# Save cleaned data
cleaned_df.to_csv(OUTPUT_FILE, index=False)

print(f"Task 1 completed: Data cleaned and split.")
print(f"Original records: {len(df)}")
print(f"Split records: {len(cleaned_df)}")
print(f"Output saved to {OUTPUT_FILE}")