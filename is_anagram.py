from collections import defaultdict

def is_anagram(first, second):
    first_map = defaultdict(int)
    second_map = defaultdict(int)

    if len(first) != len(second):
        return False
    
    for i in range(len(first)):
        first_map[first[i]] += 1
        second_map[second[i]] += 1
    
    for key, value in first_map.items():
        if key in second_map:
            if value != second_map[key]:
                return False
        else:
            return False
    
    return True



s = "anggmamj" 
t = "nagarmsk"

res = is_anagram(s, t)
print(res)