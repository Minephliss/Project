# ===============================================================================================
class Metal:
    def __init__(self, lst):
        self.name = str(lst[0])
        self.content = float(lst[1])
        self.quantity = float(lst[2])
        self.lowerLimit = float(lst[3])
        self.upperLimit = float(lst[4])
        self.used = int(lst[2])


# ===============================================================================================
kindOfMetal = 0
globalJudge = False
metalSerialNumber = []
metalList = []
targetQuantity = total = inventory = maxQuantity = 0.0
version, date, targetName = '1.0.3', '11/23/2020', ''
# ===============================================================================================


def ran(percent, lowerLimit, upperLimit):
    return percent <= upperLimit and percent >= lowerLimit


def main():
    welcome()
    inputInformation()
    calculate()


def init():
    global metalSerialNumber, globalJudge, total, metalList
    metalSerialNumber = []
    globalJudge = False
    total = 0.0
    for i in metalList:
        i.used = int(i.quantity)


def welcome():
    print("===============================================")
    print("     Thanks for using the metal calculater")
    print("               Version: {}".format(version))
    print("           Developed by Minephliss")
    print("           Last update: {}".format(date))
    print("===============================================")


def printAnswer():
    if globalJudge:
        print("The best idea is:\n")
        for i in metalList:
            print("{}: {} Percent:{:.2f}%".format(i.name, i.used, i.used * i.content / total * 100))
        print("\nYou can get {} {} in total.".format(int(total), targetName))
    else:
        print("That is impossible!")


def calculate():
    global targetQuantity, inventory, maxQuantity
    contu = True
    while(contu):
        enumerate(0)
        printAnswer()
        if input('Other quantity?(y/n)') == 'n':
            contu = False
        else:
            targetQuantity = float(input("Now you have {:.2f} in total and maybe can produce {:.2f} at most, how much do you want to produce:".format(inventory, maxQuantity)))
            init()
    print("Press Enter to exit...")


def inputInformation():
    global kindOfMetal, targetQuantity, targetName, inventory, maxQuantity
    targetName = input("What's the alloy:")
    kindOfMetal = int(input("How many kinds of submetal:"))
    print("Now input the submetals and please input the most important metal at first(eg. MetalName MetalContent MetalQuantity MetalLowerLimit MetalUpperLimit)")
    for i in range(0, kindOfMetal):
        print("The submetal {}:".format(i + 1), end='')
        lst = input().split(' ')
        metal = Metal(lst)
        inventory += (metal.content * metal.quantity)
        metalList.append(metal)
    maxQuantity = min(inventory, metalList[0].content * metalList[0].quantity / metalList[0].lowerLimit)
    targetQuantity = float(input("Now you have {:.2f} in total and maybe can produce {:.2f} at most, how much do you want to produce:".format(inventory, maxQuantity)))


def enumerate(key):
    global metalSerialNumber, globalJudge, total, inventory
    startQuantity = max(1, int(targetQuantity * metalList[key].lowerLimit / metalList[key].content))
    lastQtuantity = min(int(metalList[key].quantity), int(inventory * metalList[key].upperLimit / metalList[key].content))
    for i in range(startQuantity, lastQtuantity + 1):
        metalSerialNumber.append(i)
        if key != kindOfMetal - 1:
            enumerate(key + 1)
            metalSerialNumber.pop()
        else:
            k = 0
            tot = 0.0
            part = []
            percent = []
            for j in metalSerialNumber:
                part.append(j * metalList[k].content)
                tot += j * metalList[k].content
                k += 1
            if tot < targetQuantity:
                metalSerialNumber.pop()
                continue
            k = 0
            judge = False
            for j in metalSerialNumber:
                per = part[k] / tot
                if ran(per, metalList[k].lowerLimit, metalList[k].upperLimit):
                    percent.append(per)
                    k += 1
                else:
                    judge = True
                    break
            if judge:
                metalSerialNumber.pop()
                continue
            if metalSerialNumber[0] <= metalList[0].used and tot > total:
                globalJudge = True
                k = 0
                for j in metalSerialNumber:
                    metalList[k].used = j
                    k += 1
                total = tot
            metalSerialNumber.pop()

# ===============================================================================================


if __name__ == "__main__":
    main()
