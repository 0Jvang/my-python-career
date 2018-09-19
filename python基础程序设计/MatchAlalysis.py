from random import random
def Introduce():
    print("该程序模拟A,B球员进行某比赛的胜率分析")
    print("需要A,B球员的能力值和模拟比赛次数")

def getInput():
    a=eval(input("请输入A球员能力值(0~1):"))
    b=eval(input("请输入B球员能力值(0~1):"))
    c=eval(input("请输入模拟比赛次数:"))
    return a,b,c

def printSummary(winA,winB):
    n=winA+winB
    print("共模拟"+str(n)+"次比赛")
    print("A获胜{}次,胜率为{:.1%}".format(winA,winA/n))
    print("B获胜{}次,胜率为{:.1%}".format(winB,winB/n))

def gameover(a,b):
    return a==15 or b==15

def simOneGame(probA,probB):
    scoreA=0;scoreB=0
    x=probA/(probA+probB)
    while not gameover(scoreA,scoreB):
            if random()<x:
                scoreA+=1
            else:
                scoreB+=1
    return scoreA,scoreB

def simNGame(probA,probB,n):
    winA=0;winB=0
    for i in range(n):
        scoreA,scoreB=simOneGame(probA,probB)
        if scoreA>scoreB:
            winA+=1
        else:
            winB+=1
    return winA,winB

def main():
    Introduce()
    probA,probB,n=getInput()
    winA,winB=simNGame(probA,probB,n)
    printSummary(winA,winB)
main()
input()
    
