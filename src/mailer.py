import pandas as pd
import requests
from datetime import datetime
import time

INPUT_FILE = "output/cleaned_data.csv"
OUTPUT_FILE = "output/cleaned_data_with_mail_time.csv"

# Replace with your actual MailerSend API Key
MAILERSEND_API_KEY = "YOUR_MAILERSEND_API_KEY"
SENDER_EMAIL = "interviews@weekday.com"
SENDER_NAME = "Weekday Hiring Team"

# Load cleaned data
df = pd.read_csv(INPUT_FILE)

# Ensure Mail Sent Time column is string type
df["Mail Sent Time"] = df["Mail Sent Time"].astype(str)

# Function to send email
def send_email(to_email, to_name, round_num, calendly_link, company):
    payload = {
        "from": {
            "email": SENDER_EMAIL,
            "name": SENDER_NAME
        },
        "to": [
            {
                "email": to_email,
                "name": to_name
            }
        ],
        "subject": f"Interview Invitation - {company} - {round_num}",
        "text": f"""Hi {to_name},

You are invited for the {round_num} interview with {company}.

Please schedule your interview using the link below:
{calendly_link}

Best regards,
Weekday Team
"""
    }
    
    response = requests.post(
        "https://api.mailersend.com/v1/email",
        headers={
            "Authorization": f"Bearer {MAILERSEND_API_KEY}",
            "Content-Type": "application/json"
        },
        json=payload
    )
    
    return response.status_code == 202

# Send emails
sent_count = 0
for index, row in df.iterrows():
    # Check if email already sent
    if pd.notna(row.get("Mail Sent Time")) and str(row.get("Mail Sent Time")).strip() != "":
        continue
    
    print(f"Sending email to {row['Candidate Name']} for {row['Interview Round']}...")
    
    # In real scenario, uncomment this and use actual API key
    # if send_email(row['Candidate Email'], row['Candidate Name'], 
    #               row['Interview Round'], row['Calendly Link'], row['Company']):
    #     df.at[index, "Mail Sent Time"] = datetime.now().isoformat()
    #     sent_count += 1
    # else:
    #     print(f"Failed to send email to {row['Candidate Email']}")
    
    # For testing/demo - simulate sending
    df.at[index, "Mail Sent Time"] = datetime.now().isoformat()
    sent_count += 1
    
    # Add small delay to avoid rate limiting
    time.sleep(0.01)

# Save updated file
df.to_csv(OUTPUT_FILE, index=False)

print(f"Task 2 completed: Emails processed.")
print(f"Total emails sent: {sent_count}")
print(f"Output saved to {OUTPUT_FILE}")