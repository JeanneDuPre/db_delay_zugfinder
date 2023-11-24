## Projekt: Umgestaltung des Berliner Hauptbahnhofs

Die Umgestaltung des Berliner Hauptbahnhofs aufgrund des gestiegenen Fahrgastaufkommens dürfte kaum dazu beitragen, das Problem auf der Stadtlinie zu bewältigen, wie meine Abbildung zeigt. Dezentralisierung sollte das Maß aller Dinge sein. Die Nord-Süd-Achse weist Potential auf.
(https://lnkd.in/etmmT9YU)

### Daten
Die Daten wurden von www.zugfinder.com für einen Monat (23.10.2023-24.11.2023) entnommen.

### Durchführung
1. Daten wurden gescrapt. (Python, Selenium, BeautifulSoup, error handling)
2. Die Datengewinnung wurde mittels GitHub Action (YAML) automatisiert für jeden Tag.
   [![Zugfinder Berliner Bahnhöfe der DB](https://github.com/JeanneDuPre/db_delay_zugfinder/actions/workflows/scrape_zugfinder.yml/badge.svg)](https://github.com/JeanneDuPre/db_delay_zugfinder/actions/workflows/scrape_zugfinder.yml)
4. Datenbereinigung in data.py (pandas)
5. Graphikenerstellung in plot.py (matplotlib)

### Visualisierung Monat Oktober (23.10.2023 - 31.10.2023)
![alt text](https://github.com/JeanneDuPre/db_delay_zugfinder/blob/main/images/abfertigungszeiten_berliner_bahnh%C3%B6fe_DB_20231023_bis_20231031.gif)
### Visualisierung Monat November (01.11.2023 - 23.11.2023)
![alt text](https://github.com/JeanneDuPre/db_delay_zugfinder/blob/main/images/abfertigungszeiten_berliner_bahnh%C3%B6fe_DB_20231101_bis_20231123.gif)
