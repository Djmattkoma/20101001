def F2():
    szv=""
    for i in range(5):
        szv+=input("Ide kell: ")+", "
    print(szv)


def F3():
    num = 0
    for i in range(5):
        num+= input("számok: ")
        if  num %  2:
            print(num)

