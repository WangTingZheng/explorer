def apart(string, char):
    if string[len(string) - 1] != char:
        string += char
    tmp = ""
    res = []
    for i in string:
        if i == char:
            res.append(tmp)
            tmp = ""
        else:
            tmp += i
    return res


def together(list, char):
    res = ""
    for i in list:
        i += char
        res += i
    return res

