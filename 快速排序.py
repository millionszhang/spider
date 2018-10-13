def quick_sort(qlist):
    if qlist ==[]:
        return []
    else:
        qfirst = qlist[0]
        qless=quick_sort([l for l in qlist[1:]if l<qfirst])
        qmore=quick_sort([m for m in qlist[1:]if m>=qfirst])
        return qless+[qfirst]+qmore
qlist=quick_sort([4,5,6,7,3,2,6,9,8])
print(qlist)


