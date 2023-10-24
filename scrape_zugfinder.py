import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from datetime import datetime, timedelta


def get_new_date():
    # Get the current date
    current_date = datetime.now()

    # Subtract one day from the current date
    one_day = timedelta(days=1)
    new_date = current_date - one_day

    # Format the new date as a string in the "YYYYMMDD" format
    new_date_str = new_date.strftime("%Y%m%d")

    return new_date_str


def scrape_and_save_data(bahnhof, zug, date):
    url = f"https://www.zugfinder.net/de/bahnhofstafel-{bahnhof}-{date}-{zug}"

    # Create object page
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    table1 = soup.find("table", id="zugdaten")

    # Obtain every title of columns with tag <th>
    headers = [i.text for i in table1.find_all("th")]

    # Create a dataframe
    mydata = pd.DataFrame(columns=headers)

    # Create a for loop to fill mydata
    for j in table1.find_all("tr")[1:]:
        row_data = j.find_all("td")
        row = [i.text for i in row_data]
        length = len(mydata)
        mydata.loc[length] = row

    output_dir = "../data"
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Export to csv
    csv_filename = f"{bahnhof}_{zug}_{date}.csv"
    csv_path = os.path.join(output_dir, csv_filename)
    mydata.to_csv(csv_path, index=False)


berlin_bahnhöfe = [
    "Berlin_Lichterfelde_Ost",
    "Berlin_Charlottenburg",
    "Berlin_Alexanderplatz",
    "Berlin_Friedrichstr",
    "Berlin_Gesundbrunnen",
    "Berlin_Hbf_(Tief)",
    "Berlin_Hbf",
    "Berlin_Hohensch%C3%B6nhausen",
    "Berlin_Jungfernheide",
    "Berlin_Jungfernheide",
    "Berlin_Karow",
    "Berlin_Lichtenberg",
    "Berlin_Lichterfelde_Ost",
    "Berlin_Ostbahnhof",
    "Berlin_Ostkreuz",
    "Berlin_Potsdamer_Platz",
    "Berlin_S%C3%BCdkreuz",
    "Berlin_Spandau",
    "Berlin_Zoologischer_Garten",
]

züge = ["arr-Regio", "dep-Regio"]

new_date_str = get_new_date()

# Scraping and saving data for each station and train type
for bahnhof in berlin_bahnhöfe:
    for zug in züge:
        scrape_and_save_data(bahnhof, zug, new_date_str)
