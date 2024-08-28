# формирование списка из вложенных списков, из вводимых элементов

lst = input().split()
def sub_lists(lst):
    lists = [[]]
    for i in range(len(lst) + 1):
        for j in range(i):
            lists.append(lst[j:i])
    lists = sorted(lists, key=len)
    return lists
print(sub_lists(lst))

# способ 2
# print([[]] + [lst[j:i + j + 1] for lst in [input().split()] for i in range(len(lst)) for j in range(len(lst) - i)])