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
