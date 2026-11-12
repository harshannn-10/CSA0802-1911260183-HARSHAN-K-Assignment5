"""AT5 B1: CSV input cleaning, min-max scaling and SQLite storage."""
import csv, io, sqlite3
RAW = """station,date,pm25
Adyar,2026-10-01,48
Adyar,2026-10-02,NA
Adyar,2026-10-03,
Guindy,2026-10-01,95
Guindy,2026-10-02,-5
Guindy,2026-10-03,1200
Velachery,2026-10-01,35
"""
def load_clean(text):
    rows = []
    for row in csv.DictReader(io.StringIO(text)):
        try: value = float(row.get("pm25", "").strip())
        except (ValueError, TypeError): continue
        if 0 <= value <= 999: rows.append((row["station"].strip(), row["date"].strip(), value))
    return rows
def min_max(values):
    if not values: return []
    low, high = min(values), max(values)
    return [0.0 for _ in values] if high == low else [round((v-low)/(high-low), 3) for v in values]
def main():
    clean = load_clean(RAW)
    print("Clean:", clean); print("Scaled:", min_max([v for _,_,v in clean]))
    con = sqlite3.connect("air_quality.db")
    con.execute("CREATE TABLE IF NOT EXISTS aq(station TEXT, day TEXT, pm25 REAL, PRIMARY KEY(station,day))")
    con.executemany("INSERT OR REPLACE INTO aq VALUES(?,?,?)", clean); con.commit()
    for station in ("Adyar", "Guindy"):
        print(station, con.execute("SELECT AVG(pm25) FROM aq WHERE station=?", (station,)).fetchone()[0])
    con.close()
if __name__ == "__main__": main()
