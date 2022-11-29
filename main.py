import sqlite3
import pandas
from pathlib import Path
from sql import avgBtw
from trends import trends


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
        );""")

    data = pandas.read_csv('mxmh_survey_results.csv')
    data.to_sql('mxmh', dataConn, if_exists='append', index=False)
    return


def main():
    if not Path('data.db').exists():
        createDB()

    dbConn = sqlite3.connect('data.db')
    d = dbConn.cursor()

    LISTENRANGE = [(0.0, 0.99), (1.0, 1.99), (2.0, 3.99), (4.0, 7.99), (8.0, 24.0)]

    want = ['anxiety', 'depression', 'ocd', 'insomnia']
    where = 'daily'
    w_is = [f'BETWEEN {x} AND {y}' for x, y in LISTENRANGE]

    whereIs = [f'{where} {word}' for word in w_is]

    dat_0_keys = [f'from {x} to {y}' for x, y in LISTENRANGE]
    dat_0 = [avgBtw(d, want, whereWhat) for whereWhat in whereIs]

    dat_0 = dict(zip(dat_0_keys, dat_0))

    dat_0_trends = trends(dat_0)

    gap = '        '

    for k in dat_0_trends:
        print(k)
        for key, elem in dat_0_trends[k].items():
            print(gap, key + ' hours per day:', elem)

    


if __name__ == "__main__":
    main()
