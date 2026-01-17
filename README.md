# weekday-interview-automation

Project Overview
Python automation system for interview scheduling and communication as per Weekday coding assignment requirements.

Key Results
Input: 200 candidate records

Output: 384 interview rounds (after splitting)

Companies: Amazon, Google, Tesla, OpenAI, Flipkart

Email Success: 384/384 emails sent

Processing Time: < 2 seconds

File Structure
text
weekday-interview-automation/
├── data/FO_Coding_Assignment.csv    # Input
├── src/                            # Scripts
├── output/                         # Generated files
├── requirements.txt                # Dependencies
└── README.md                       # Documentation
Scripts & Outputs
Task 1: Data Splitting
Script: python src/data_split.py

Splits multiple interview rounds into separate rows

Extracts Calendly links from scheduling method

Output: output/cleaned_data.csv (384 rows)

Task 2: Email Automation
Script: python src/mailer.py

Sends interview emails via MailerSend API (simulated)

Updates Mail Sent Time timestamps

Output: output/cleaned_data_with_mail_time.csv

Task 3: TAT Calculation
Script: python src/tat.py

Calculates TAT = Mail Sent Time - Added On Time

Output: output/final_output_with_tat.csv

Quick Start
bash
# Install dependencies
pip install -r requirements.txt

# Run complete workflow
python src/data_split.py
python src/mailer.py  
python src/tat.py

# Test & verify
python src/test_flow.py
python src/summary_report.py
Output Files
cleaned_data.csv - Split interview rounds

cleaned_data_with_mail_time.csv - Email timestamps added

final_output_with_tat.csv - Final data with TAT calculated

Requirements
Python 3.8+

pandas, requests libraries

MailerSend API key (for real email sending)

Key Features
Automated data cleaning and splitting

Email integration with MailerSend API

Turnaround Time (TAT) calculation

Comprehensive error handling

Ready for Airtable import

Note
This Python implementation simulates Airtable automation logic. Output files are Airtable-ready for production use.


