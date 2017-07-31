def solved_merge_sort(ls):
    if(len(ls) < 2):
        return ls
    mid = int(len(ls) / 2)
    left = solved_merge_sort(ls[:mid])
    right = solved_merge_sort(ls[mid:])
    return merge(left, right)

def merge(l, r):
    result = []
    while(len(l) > 0 and len(r) > 0):
        if r[0] < l[0]:
            result.append(r.pop(0))
        else:
            result.append(l.pop(0))
    result.extend(l + r)
    return result