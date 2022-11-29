import sqlite3
import pandas
from pathlib import Path


def createDB():
    Path('data.db').touch()
    dataConn = sqlite3.connect('data.db')
    d = dataConn.cursor()
    d.execute(
        """CREATE TABLE mxmh (
            time_taken datetime, age int,
            stream_serv text, daily int,
            while_working text, instrumentalist text,
            composer text, fav_genre text,
            exploratory text, foreign_m text,
            bpm int, classical text,
            country text, edm text,
            folk text, gospel text,
            hiphop text, jazz text,
            kpop text, latin text,
            lofi text, metal text,
            pop text, rnb text,
            rap text, rock text,
            vgm text, anxiety int,
            depression int, insomnia int,
            ocd int, music_e text,
            permissions text
        );"""
    )


def main():
    if not Path('data.db').exists():
        createDB()

    dbConn = sqlite3.connect('data.db')
    d = dbConn.cursor()
    
    data = pandas.read_csv('mxmh_survey_results.csv')
    data.to_sql('mxmh', dbConn, if_exists='append', index=False)




if __name__ == "__main__":
    main()
