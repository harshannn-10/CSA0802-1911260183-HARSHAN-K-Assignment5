"""AT5 B2: parameterised SQL and adversarial input checks."""
import sqlite3
def main():
    readings = [("Adyar","2026-10-01",48.0),("Guindy","2026-10-01",95.0),("Guindy","2026-10-03",121.0),("Adyar","2026-10-04",60.0)]
    con = sqlite3.connect(":memory:")
    con.execute("CREATE TABLE aq(station TEXT, day TEXT, pm25 REAL)")
    con.executemany("INSERT INTO aq VALUES(?,?,?)", readings); con.commit()
    def station_average(name):
        return con.execute("SELECT AVG(pm25) FROM aq WHERE station=?", (name,)).fetchone()[0]
    print("Adyar:", station_average("Adyar")); print("Guindy:", station_average("Guindy"))
    print("Adversarial input:", station_average("Adyar' OR '1'='1"))
    con.close()
if __name__ == "__main__": main()
