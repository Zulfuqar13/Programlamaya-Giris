while(True):
    qiymet1 = float(input("1.Qiymet:"))
    qiymet2 = float(input("2.Qiymet:"))
    emeller = input("+,-,*,/,:")
    if emeller == ("+"):
        netice = qiymet1 + qiymet2
        print(netice)
    elif emeller == ("-"):
        netice = qiymet1 - qiymet2
        print (netice)
    elif emeller == ("*"):
        netice = qiymet1 * qiymet2
        print(netice)
    elif emeller ==  ("/"):\
    netice = qiymet1 / qiymet2
    print (netice)
else:
    print("Xetali reqem")

