def reverse_seq(n):
    lists = []
    for list in range(1,n+1):
        lists.append(list)
    lists.reverse()
    return lists

print(reverse_seq(5))