import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

csv_folder = Path("csv_files")
db_folder = Path("sqlite_db")

data = {
    'hospitals': 'hospitals.csv',
    'institutions': 'institutions.csv',
    'restaurants': 'restaurants.csv'
}

for name, csv_file in data.items():
    csv_path = csv_folder/csv_file
    db_path = db_folder/f"{name}.db"

    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    engine = create_engine(f"sqlite:///{db_path}")
    df.to_sql(name, engine, if_exists="replace", index=False)
    print(f"{csv_file} → {db_path} done ✅")