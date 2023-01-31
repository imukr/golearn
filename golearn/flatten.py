def flatten (s):

    if not s:
        return []
    if isinstance(s[0],list):
        return flatten(s[0])+flatten(s[1:])
    return s[:1] + flatten(s[1:])

print(flatten([1, 2, [3, 4, [5, 6]], 7]))