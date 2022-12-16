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


def qwe(d, sel, where='', di='mxmh'):
    dMntLvls = [d.execute(
        f"""SELECT {selStr}
        FROM {di};
        """).fetchall() for selStr in sel]

    for i, li in enumerate(dMntLvls):
        dMntLvls[i] = list(map(lambda n: n[0], li))
        dMntLvls[i].sort()

    return dict(zip(sel, dMntLvls))

    # data = list(d.execute(
    #     f"""SELECT {selStr}
    #     FROM {di}
    #     WHERE {where};
    #     """).fetchall()[0])

        