import pandas as pd

def get_data():
    dates = [
        "20231023",
        "20231024",
        "20231025",
        "20231026",
        "20231028",
        "20231029",
        "20231030",
        "20231031",
        "20231101",
        "20231102",
        "20231103",
        "20231104",
        "20231105",
        "20231106",
        "20231107",
        "20231108",
        "20231109",
        "20231110",
        "20231111",
        "20231112",
        "20231113",
    ]
    all_data = []

    for date in dates:
        arrives_stations = [
            f"data/new/Berlin_Charlottenburg_arr-Regio_{date}.csv",
            f"data/new/Berlin_Alexanderplatz_arr-Regio_{date}.csv",
            f"data/new/Berlin_Friedrichstr_arr-Regio_{date}.csv",
            f"data/new/Berlin_Gesundbrunnen_arr-Regio_{date}.csv",
            f"data/new/Berlin_Hbf_(Tief)_arr-Regio_{date}.csv",
            f"data/new/Berlin_Hbf_arr-Regio_{date}.csv",
            f"data/new/Berlin_Hohensch%C3%B6nhausen_arr-Regio_{date}.csv",
            f"data/new/Berlin_Jungfernheide_arr-Regio_{date}.csv",
            f"data/new/Berlin_Jungfernheide_arr-Regio_{date}.csv",
            f"data/new/Berlin_Karow_arr-Regio_{date}.csv",
            f"data/new/Berlin_Lichtenberg_arr-Regio_{date}.csv",
            f"data/new/Berlin_Lichterfelde_Ost_arr-Regio_{date}.csv",
            f"data/new/Berlin_Ostbahnhof_arr-Regio_{date}.csv",
            f"data/new/Berlin_Ostkreuz_arr-Regio_{date}.csv",
            f"data/new/Berlin_Potsdamer_Platz_arr-Regio_{date}.csv",
            f"data/new/Berlin_S%C3%BCdkreuz_arr-Regio_{date}.csv",
            f"data/new/Berlin_Spandau_arr-Regio_{date}.csv",
            f"data/new/Berlin_Zoologischer_Garten_arr-Regio_{date}.csv",
        ]

        departures_stations = [
            f"data/new/Berlin_Charlottenburg_dep-Regio_{date}.csv",
            f"data/new/Berlin_Alexanderplatz_dep-Regio_{date}.csv",
            f"data/new/Berlin_Friedrichstr_dep-Regio_{date}.csv",
            f"data/new/Berlin_Gesundbrunnen_dep-Regio_{date}.csv",
            f"data/new/Berlin_Hbf_(Tief)_dep-Regio_{date}.csv",
            f"data/new/Berlin_Hbf_dep-Regio_{date}.csv",
            f"data/new/Berlin_Hohensch%C3%B6nhausen_dep-Regio_{date}.csv",
            f"data/new/Berlin_Hohensch%C3%B6nhausen_dep-Regio_{date}.csv",
            f"data/new/Berlin_Jungfernheide_dep-Regio_{date}.csv",
            f"data/new/Berlin_Karow_dep-Regio_{date}.csv",
            f"data/new/Berlin_Lichtenberg_dep-Regio_{date}.csv",
            f"data/new/Berlin_Lichterfelde_Ost_dep-Regio_{date}.csv",
            f"data/new/Berlin_Ostbahnhof_dep-Regio_{date}.csv",
            f"data/new/Berlin_Ostkreuz_dep-Regio_{date}.csv",
            f"data/new/Berlin_Potsdamer_Platz_dep-Regio_{date}.csv",
            f"data/new/Berlin_S%C3%BCdkreuz_dep-Regio_{date}.csv",
            f"data/new/Berlin_Spandau_dep-Regio_{date}.csv",
            f"data/new/Berlin_Zoologischer_Garten_dep-Regio_{date}.csv",
        ]

        for arrive, departure in zip(arrives_stations, departures_stations):
            try:
                df = pd.read_csv(arrive)
                df_1 = pd.read_csv(departure)
            except FileNotFoundError as e:
                print(f"File not found for date {date}: {e}")
                continue

            df["time_ankunft"] = df["Ankunft"].str.split().str[0]
            df["delay_ankunft"] = df["Ankunft"].str.split().str[1]
            df_1["time_abfahrt"] = df_1["Abfahrt"].str.split().str[0]
            df_1["delay_abfahrt"] = df_1["Abfahrt"].str.split().str[1]
            # Concatenate dataframes using 'Zugnr.' as the ensemble column
            result = pd.merge(
                df, df_1, on="Zugnr.", how="inner", suffixes=("_df", "_df_1")
            )

            # Replace parentheses and '+' characters in 'delay_ankunft' and 'delay_abfahrt'
            result["delay_ankunft"] = result["delay_ankunft"].str.replace(
                r"[()\\+]", "", regex=True
            )
            result["delay_abfahrt"] = result["delay_abfahrt"].str.replace(
                r"[()\\+]", "", regex=True
            )

            # Convert 'delay_ankunft' and 'delay_abfahrt' to numeric (float)
            result["delay_ankunft"] = pd.to_numeric(
                result["delay_ankunft"], errors="coerce"
            )
            result["delay_abfahrt"] = pd.to_numeric(
                result["delay_abfahrt"], errors="coerce"
            )

            # Fill NaN values in both columns with 0
            result["delay_ankunft"].fillna(0, inplace=True)
            result["delay_abfahrt"].fillna(0, inplace=True)

            # Calculate 'count_delay' as the difference between 'delay_abfahrt' and 'delay_ankunft'
            result["count_delay"] = result["delay_abfahrt"].astype(int) - result[
                "delay_ankunft"
            ].astype(int)

            # Create a new column with the date
            result["date"] = date

            all_data.append(result)
    # Combine all DataFrames in the all_data list into a single DataFrame
    final_dataframe = pd.concat(all_data, ignore_index=True)
    final_dataframe["Ankunftsbhf."] = (
        final_dataframe["Ankunftsbhf."]
        .replace("Berlin Friedrichstr", "Friedrichstraße")
        .replace("Berlin Friedrichstraße", "Friedrichstraße")
    )
    final_dataframe["Ankunftsbhf."] = (
        final_dataframe["Ankunftsbhf."]
        .replace("Berlin Zoologischer Garten", "Zoologischer Garten")
        .replace("Berlin-Spandau", "Spandau")
        .replace("Berlin Alexanderplatz", "Alexanderplatz")
        .replace("Berlin-Charlottenburg", "Charlottenburg")
        .replace("Berlin Jungfernheide", "Jungfernheide")
        .replace("Berlin Südkreuz", "Südkreuz")
        .replace("Berlin Ostkreuz", "Ostkreuz")
        .replace("Berlin Potsdamer Platz", "Potsdamer Platz")
        .replace("Berlin Gesundbrunnen", "Gesundbrunnen")
        .replace("Berlin-Lichterfelde Ost", "Lichterfelde Ost")
        .replace("Berlin-Lichtenberg", "Lichtenberg")
        .replace("Berlin-Hohenschönhausen", "Hohenschönhausen")
        .replace("Berlin Ostbahnhof", "Ostbahnhof")
    )

    # Define time intervals
    time_intervals = {
        "00:00 - 06:00 Uhr": ("00:00", "06:00"),
        "06:01 - 09:00 Uhr": ("06:01", "09:00"),
        "09:01 - 12:00 Uhr": ("09:01", "12:00"),
        "12:01 - 15:00 Uhr": ("12:01", "15:00"),
        "15:01 - 18:00 Uhr": ("15:01", "18:00"),
        "18:01 - 21:00 Uhr": ("18:01", "21:00"),
        "21:01 - 24:00 Uhr": ("21:01", "24:00"),
    }

    # Function to map time to interval
    def map_time_to_interval(time):
        for interval, (start, end) in time_intervals.items():
            if start <= time <= end:
                return interval
        return None

    # Apply the mapping function to create a new column
    final_dataframe["time_interval"] = final_dataframe["time_ankunft"].apply(
        map_time_to_interval
    )
    stations_to_remove = [
        "Berlin-Lichterfelde Ost (S)",
        "Berlin Ostkreuz (S)",
        "Berlin Gesundbrunnen(S)",
        "Berlin Heidelberg Hbfer Platz",
        "Berlin Jungfernheide (S)",
        "Berlin Südkreuz (S)",
    ]

    final_dataframe = final_dataframe[
        ~final_dataframe["Ankunftsbhf."].isin(stations_to_remove)
    ]

    return final_dataframe
