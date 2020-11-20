class Metal:
    def __init__(self, lst):
        self.name = str(lst[0])
        self.content = float(lst[1])
        self.quantity = float(lst[2])
        self.lowerLimit = float(lst[3])
        self.upperLimit = float(lst[4])
        self.used = int(lst[2])

metalSerialNumber = []
kindOfMetal = 0
metalList = []
targetQuantity = 0.0
total = 0.0
globalJudge = False
targetName = ""
version = '1.0.1'
date = '2020/11/20'

def welcome():
    print("===============================================")
    print("              感谢使用合金计算器")
    print("                  版本： {}".format(version))
    print("              开发者：Minephliss")
    print("             最近更新：{}".format(date))
    print("===============================================")

def inputInformation():
    global kindOfMetal, targetQuantity, targetName
    inventory = 0.0
    targetName = input("合金名称：")
    kindOfMetal = int(input("需要几种子金属合成："))
    print("现在请依序输入子金属，最需要节省的放在第一个(例子：金属名称 金属含量 金属数量 占合金比例下限 占合金比例上限)")
    for i in range(0, kindOfMetal):
        print("子金属 {}：".format(i + 1), end='')
        lst = input().split(' ')
        metal = Metal(lst)
        inventory += (metal.content * metal.quantity)
        metalList.append(metal)
    maxQuantity = min(inventory, metalList[0].content * metalList[0].quantity / metalList[0].lowerLimit)
    targetQuantity = float(input("现在你总共有{:.2f}单位，粗略估计最多生产{:.2f}单位，你希望至少生产多少单位：".format(inventory, maxQuantity)))

def ran(percent, lowerLimit, upperLimit):
    return percent <= upperLimit and percent >= lowerLimit

def enumerate(key):
    global metalSerialNumber, globalJudge, total
    for i in range(1, int(metalList[key].quantity) + 1):
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

def printAnswer():
    if globalJudge:
        print("最佳生产方案为：\n")
        for i in metalList:
            print("{}：{} 占比：{:.2f}%".format(i.name, i.used, i.used * i.content / total * 100))
        print("\n你一共可以获得 {} 单位 {}.".format(targetName, int(total)))
    else:
        print("这无法实现！")
    input("按下回车键退出程序")


def main():
    welcome()
    inputInformation()
    enumerate(0)
    printAnswer()


if __name__ == "__main__":
    main()
