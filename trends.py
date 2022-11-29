def trends(di):
    newDic = {}

    for k in di:
        for e in di[k]:
            if e not in newDic:
                newDic.update({e: {}})
                
            newDic[e].update({k: di[k][e]})
    
    return newDic
