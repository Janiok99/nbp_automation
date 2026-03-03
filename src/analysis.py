def save_to_csv(df, filename="../data/eur_rate.csv"):
    df.to_csv(filename, index=False)

def print_report(df):
    row = df.iloc[0]
    print(f"Kurs EUR z dnia {row['data']}: {row['kurs_EUR']} PLN")
