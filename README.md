# NBP Automation

    Aplikacja automatycznie pobiera aktualny kurs EUR/PLN z API Narodowego Banku Polskiego, zapisuje dane do pliku CSV oraz generuje prosty raport z najnowszego kursu.  
    Projekt jest modularny — logika API, analizy i główne uruchomienie są rozdzielone w osobnych plikach.

## Struktura projektu

    nbp-automation/
    │
    ├── data/
    │   └── eur_rate.csv        # Automatycznie tworzony i aktualizowany plik z kursami EUR
    │
    ├── src/
    │   ├── main.py             # Główny punkt uruchomienia aplikacji
    │   ├── api.py              # Pobieranie kursu EUR z API NBP
    │   └── analysis.py         # Zapisywanie danych i generowanie raportu
    │
    ├── README.md               # Dokumentacja projektu
    └── requirements.txt        # Lista wymaganych bibliotek

## Funkcjonalności

    - Pobieranie aktualnego kursu EUR/PLN z API NBP  
    - Automatyczne tworzenie i aktualizacja pliku `eur_rate.csv`  
    - Zapisywanie danych w formacie:
        data,kurs_EUR
        2026-03-03,4.27
    - Generowanie raportu z najnowszego kursu:
        Kurs EUR z dnia 2026-03-03: 4.27 PLN

## Jak działa projekt

    ## Uruchomienie programu (`main.py`)

        Po uruchomieniu:
            python src/main.py

    program wykonuje trzy główne operacje:

        1. pobiera aktualny kurs EUR z API NBP  
        2. wyświetla pobrane dane i raport  
        3. zapisuje dane do pliku CSV  

    ## Pobranie kursu EUR z API NBP (`api.py`)

        Funkcja:

        ```python
        get_eur_rate()
        
        wykonuje zapytanie do oficjalnego API NBP:
            https://api.nbp.pl/api/exchangerates/rates/A/EUR/?format=json
        
        Następnie:

            - odczytuje datę kursu (effectiveDate)
            - odczytuje wartość kursu (mid)
            - zwraca dane w formie DataFrame:
                
                data	kurs_EUR
                2026-03-03	4.27

    ## Generowanie raportu (analysis.py)
        
        Funkcja:
        
        print_report(df)
        wyświetla prosty raport:
            Kurs EUR z dnia 2026-03-03: 4.27 PLN
        Dzięki temu użytkownik od razu widzi najważniejszą informację.

    ## Zapis danych do pliku CSV (analysis.py)
        
        Funkcja:

            save_to_csv(df)
            zapisuje dane do:
                data/eur_rate.csv
            
        Jeśli plik nie istnieje — zostanie utworzony automatycznie.
        Każde uruchomienie programu nadpisuje dane w pliku: eur_rate.csv

    ## Efekt końcowy
        
        Po uruchomieniu aplikacji otrzymujesz:

            - aktualny kurs EUR/PLN
            - czytelny raport w konsoli
            - zaktualizowany plik CSV z historią kursów
