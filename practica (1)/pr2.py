def max_len(arr: list):
    unique = set(map(lambda x : x[0], arr))
    final_arr = sorted([max(filter(lambda x : i in x, arr)) for i in unique])
    return [(i,len(i)) for i in final_arr]
    
arr1 = ["aaa","aa","aaaaa","bbb","bbbbbbbb"]
arr2 = ["o","oooooo","o","ssss","ss","cccc","c","cccccccc"]
arr3 = ["q","qq","qqq","qqqq","wwwww","e","eeee","eeeeeeeee"]

print(max_len(arr1))
print(max_len(arr2))
print(max_len(arr3))