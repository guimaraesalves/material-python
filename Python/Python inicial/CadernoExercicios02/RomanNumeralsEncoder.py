from collections import OrderedDict

def write_roman(n):

    romanos = OrderedDict()
    romanos[1000] = "M"
    romanos[900] = "CM"
    romanos[500] = "D"
    romanos[400] = "CD"
    romanos[100] = "C"
    romanos[90] = "XC"
    romanos[50] = "L"
    romanos[40] = "XL"
    romanos[10] = "X"
    romanos[9] = "IX"
    romanos[5] = "V"
    romanos[4] = "IV"
    romanos[1] = "I"

    def roman_num(n):
        for i in romanos.keys():
            x, y = divmod(n, i)
            yield romanos[i] * x
            n -= (i * x)
            if n <= 0:
                break

    return "".join([a for a in roman_num(n)])

print(write_roman(984))