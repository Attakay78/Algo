def is_anagram(s, t):
    s_map = {}
    t_map = {}

    if len(s) != len(t):
        return False

    for index in range(len(s)):
        s_map[s[index]] = 1 + s_map.get(s[index], 0)
        t_map[t[index]] = 1 + t_map.get(t[index], 0)

    for key, val in s_map.items():
        # t_val = t_map.get(key, 0)
        # if val != t_val:
        #     return False
        if key in t_map:
            if s_map[key] != t_map[key]:
                return False
        else:
            return False

    return True

if __name__ == "__main__":
    s = "anagram" 
    t = "nagaram"

    res = is_anagram(s, t)
    print(res)
