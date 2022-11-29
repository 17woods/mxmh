import sqlite3

def avgBtw(d, sel, between, di='mxmh'):
    selStr = ', '.join([f"AVG({e})" for e in sel])
    
    data = list(d.execute(
        f"""SELECT {selStr}
        FROM {di}
        WHERE {between};
        """).fetchall()[0])

    data = list(map(lambda fl: round(fl, 2), data))

    keyList = [f"avg({e})" for e in sel]

    return dict(zip(keyList, data))


def avBd(d):
    def roundList(li):
        return [round(fl, 3) for fl in li]

    listenR0 = d.execute(
        """SELECT AVG(anxiety), AVG(depression), AVG(insomnia), AVG(ocd)
        FROM mxmh
        WHERE daily < 1;
        """).fetchall()
    listenR1 = d.execute(
        """SELECT AVG(anxiety), AVG(depression), AVG(insomnia), AVG(ocd)
        FROM mxmh
        WHERE daily BETWEEN 1 AND 1.99;
        """).fetchall()
    listenR2 = d.execute(
        """SELECT AVG(anxiety), AVG(depression), AVG(insomnia), AVG(ocd)
        FROM mxmh
        WHERE daily BETWEEN 2 AND 3.99;
        """).fetchall()
    listenR3 = d.execute(
        """SELECT AVG(anxiety), AVG(depression), AVG(insomnia), AVG(ocd)
        FROM mxmh
        WHERE daily BETWEEN 4 AND 7.99;
        """).fetchall()
    listenR4 = d.execute(
        """SELECT AVG(anxiety), AVG(depression), AVG(insomnia), AVG(ocd)
        FROM mxmh
        WHERE daily > 8;
        """).fetchall()

    keyList = ['avgAnx', 'avgDep', 'avgIns', 'avgOCD']

    listenR0 = roundList(list(listenR0[0]))
    listenR1 = roundList(list(listenR1[0]))
    listenR2 = roundList(list(listenR2[0]))
    listenR3 = roundList(list(listenR3[0]))
    listenR4 = roundList(list(listenR4[0]))

    finR0 = dict(zip(keyList, listenR0))
    finR1 = dict(zip(keyList, listenR1))
    finR2 = dict(zip(keyList, listenR2))
    finR3 = dict(zip(keyList, listenR3))
    finR4 = dict(zip(keyList, listenR4))

    return {
        '<1': finR0,
        '[1, 2)': finR1,
        '[2, 4)': finR2,
        '[4, 8)': finR3,
        '8+': finR4
    }


def hoursEffect(d):
    averageByDaily = avBd(d)
    
    luAttr = 'avgOCD'

    for k in averageByDaily:
        print(f"{k} -> {averageByDaily[k][luAttr]}")

