def isAnagram(s, t):
        s_table = {}
        t_table = {}
        for char in s:
            if char in s_table:
                s_table[char] += 1
            else:
                s_table[char] = 1
        for char in t:
            if char in t_table:
                t_table[char] += 1
            else:
                t_table[char] = 1
        return s_table == t_table

print(isAnagram("qertewq","teqrqwe"))