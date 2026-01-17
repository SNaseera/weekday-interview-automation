import pandas as pd

def generate_summary():
    print("=" * 60)
    print("WEEKDAY INTERVIEW AUTOMATION - SUMMARY REPORT")
    print("=" * 60)
    
    # Load final output
    df = pd.read_csv("output/final_output_with_tat.csv")
    
    # 1. Overall statistics
    print(f"\n1. OVERALL STATISTICS")
    print(f"   Total candidates processed: {df['Candidate Name'].nunique()}")
    print(f"   Total interview rounds: {len(df)}")
    print(f"   Total emails sent: {df['Mail Sent Time'].notna().sum()}")
    
    # 2. Interview rounds distribution
    print(f"\n2. INTERVIEW ROUNDS DISTRIBUTION")
    round_counts = df['Interview Round'].value_counts().sort_index()
    for round_num, count in round_counts.items():
        print(f"   {round_num}: {count} candidates")
    
    # 3. Company-wise distribution
    print(f"\n3. COMPANY-WISE DISTRIBUTION")
    company_counts = df['Company'].value_counts()
    for company, count in company_counts.items():
        print(f"   {company}: {count} interview rounds")
    
    # 4. TAT Analysis
    print(f"\n4. TURNAROUND TIME (TAT) ANALYSIS")
    print(f"   Average TAT: {df['TAT (Hours)'].mean():.2f} hours")
    print(f"   Minimum TAT: {df['TAT (Hours)'].min():.2f} hours")
    print(f"   Maximum TAT: {df['TAT (Hours)'].max():.2f} hours")
    
    # 5. Sample data
    print(f"\n5. SAMPLE DATA (first 5 records):")
    print(df[['Candidate Name', 'Company', 'Interview Round', 'TAT (Hours)']].head().to_string(index=False))
    
    print("\n" + "=" * 60)
    print("SUMMARY COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    generate_summary()