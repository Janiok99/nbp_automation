from api import get_eur_rate
from analysis import save_to_csv, print_report

def main():
    df = get_eur_rate()
    print(df)
    print_report(df)
    save_to_csv(df)

if __name__ == "__main__":
    main()
