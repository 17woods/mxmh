import sqlite3

def hoursEffect(d):
    m = d.execute(
        'SELECT daily,anxiety,depression,insomnia,ocd FROM mxmh').fetchall()
    print(m)