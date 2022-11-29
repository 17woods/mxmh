import sqlite3

def hoursEffect(d):
    m = d.execute(
        'SELECT daily,anxiety,depression,insomnia,ocd FROM mxmh').fetchall()
    print(len(m))

    # Ranges
    # >1
    # 1-2
    # 2.5-4
    # 4.5-7.5
    # 8+
    dicts = {}
    for n in range(0, 5):
        dicName = f"listenR{n}"
        dicts[dicName] = {
        'avg_tim': 0.0,
        'avg_anx': 0.0,
        'avg_dep': 0.0,
        'avg_ins': 0.0,
        'avg_ocd': 0.0,
        'avg_tmh': 0.0
        }
        print(dicName, dicts[dicName])

    # data -> (daily, anx, dep, ins, ocd)
    dicts['listenR0']['data'] = [tu for tu in m if tu[0] < 1]
    dicts['listenR1']['data'] = [tu for tu in m if 1 < tu[0] <= 2]
    dicts['listenR2']['data'] = [tu for tu in m if 2 < tu[0] <= 4]
    dicts['listenR3']['data'] = [tu for tu in m if 4 < tu[0] <= 7.9]
    dicts['listenR4']['data'] = [tu for tu in m if 8 < tu[0]]

    for di in dicts:
        print(len(dicts[di]['data']))
