"""AT5 B3: compare loop, pandas and SQL daily averages."""
import sqlite3
try: import pandas as pd
except ImportError: pd = None
ROWS = [("Adyar","2026-10-01",48.0),("Adyar","2026-10-01",52.0),("Guindy","2026-10-01",95.0),("Guindy","2026-10-02",90.0)]
def loop_means(data):
    acc = {}
    for station, day, value in data:
        item = acc.setdefault((station, day), [0.0, 0])
        item[0] += value; item[1] += 1
    return {key: total/count for key,(total,count) in acc.items()}
def main():
    print("Python:", loop_means(ROWS))
    if pd is not None:
        frame = pd.DataFrame(ROWS, columns=["station","day","pm25"])
        print("Pandas:", frame.groupby(["station","day"]).pm25.mean().to_dict())
    else: print("Pandas: not installed (optional)")
    con = sqlite3.connect(":memory:")
    con.execute("CREATE TABLE aq(station TEXT, day TEXT, pm25 REAL)")
    con.executemany("INSERT INTO aq VALUES(?,?,?)", ROWS)
    print("SQL:", con.execute("SELECT station,day,AVG(pm25) FROM aq GROUP BY station,day").fetchall())
    con.close()
if __name__ == "__main__": main()
