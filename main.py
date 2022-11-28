import sqlite3
from pathlib import Path


def main():
    Path('data.db').touch()
    dataConn = sqlite3.connect('data.db')
    d = dataConn.cursor()
    d.execute(
        """CREATE TABLE data (
            time_taken datetime, age int,
            stream_serv text, daily int,
            while_working text, instrumentalist text,
            composer text, fav_genre text,
            exporatory text, foreign_m text,
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


if __name__ == "__main__":
    main()
