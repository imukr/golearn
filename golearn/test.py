def capital_text(s):
    flag = None
    result = s
    for count in range(len(s)):
        if s[count] != ' ':
            result = result[:count] + result[count].upper() + result[count + 1: len(result)]
            break
    for count in range(len(s)):
        if result[count] in [".", "!", "?"]:
            flag = True
            continue
        if count < len(s) and result[count] == " " and flag:
            continue
        if flag:
            result = result[:count] + result[count].upper() + result[count + 1: len(result)]
            flag = False

    return print(result)



capital_text('  ifb. jfn. on')
