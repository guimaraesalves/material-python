def namelist(names):
    res = ''
    if(len(names) == 1):
        return  names[0]['name']
    elif(len(names) == 2):
        res = res + names[0]['name'] + " & " + names[1]['name']
    elif(len(names) > 2):
        for i in range(0, len(names) - 1):
            res = res + names[i]['name'] + ", "
        res = res[:2] + " & " + names[len(names) - 1]['name']
    return res


for contA in range(1, 10):
    for contB in range((contA + 1), 11):
        if vet[contA] > vet[contB]:
