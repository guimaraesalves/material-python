

tempo = int(input())
hr = int(tempo/60/60)
mn = int((tempo / 60) - (hr * 60))
sg = int(tempo - ((hr*60*60) + (mn * 60)))
print(str(hr)+':'+str(mn)+':'+str(sg))
