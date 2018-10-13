def shell_sort(slist):
    gap = len(slist)
    while gap > 1:
        gap = gap // 2
        for i in range(gap, len(slist)):
            for j in range(i % gap, i, gap):
                if slist[i] < slist[j]:
                    slist[i], slist[j] = slist[j], slist[i]
    return slist


slist = shell_sort([4, 5, 6, 7, 3, 2, 6, 9, 8])
print(slist)