import random as rn
def roll_die():
    die_one=rn.randint(1,6)
    die_two=rn.randint(1,6)
    return die_two+die_one
def ast(c):
    x=2
    for i in c:
        print(str(x)+"*"*i)
        x+=1


def main():
    count=[0,0,0,0,0,0,0,0,0,0,0]
    x = input("how many times would you like to roll the dice")
    if x.isdigit():
        n=float(x)
    else:
        print("please input only digits")
        main()
    i=0
    while i <n:
        sum=roll_die()
        count[sum-2]+=1
        i+=1
    print(count)
    ast(count)
main()