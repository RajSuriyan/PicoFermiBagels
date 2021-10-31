import random as rd
import time

master=['Pico','Fermi','Bagels']

print("This Is Number Guessing Game")
print('You have to guess the three digit number')
print("The Computer will tell you:")
print("    -> Pico-If you guess the right number in But it is Wrong digit.")
print('    -> Fermi-If it is correct number and correct digit.')
print('    -> Bagels-If it is not a correct number.')
print("\n\nYou have 10 Chances to Guess ")


#game
def splitter(a):
    a=str(a)
    return int(a[0]),int(a[1]),int(a[2])

def tim():
    print("Closing in 10s")
    time.sleep(10)

while True:
    num = rd.randint(100, 999)
    m1, m2, m3 = splitter(num)
    if m1==m2 or m1==m3 or m2==m3:
        pass
    else:
        break





for i in range(0,10):
    try:
        gue=eval(input(">>>"))
        if gue==101010:
            print("You Have Entered the developer Mode!")
            print("The number that is assigned for this game is.")
            print("This is for only checking Purposes")
            print('You will not be considered as Winner!')
            print(splitter(num))
    except:
        print("You Entered a Char or String or bool. You Lost your one chance!")

    a,b,c=splitter(num)
    d,e,f=splitter(gue)

    lis1 = [a,b,c]
    lis2 = [d,e,f]
    if d in lis1:
        if d == lis1[0]:
            check = 1
        else:
            check = 0
    else:
        check = 2

    if e in lis1:
        if e == lis1[1]:
            check2 = 1
        else:
            check2 = 0
    else:
        check2 = 2

    if f in lis1:
        if f == lis1[2]:
            check3 = 1
        else:
            check3 = 0
    else:
        check3 = 2
    w1,w2,w3=master[check],master[check2],master[check3]

    checklist=[w1,w2,w3]
    count=0
    countf=0
    for i in checklist:
        if i==master[0]:
            count+=1
        if i==master[1]:
            countf+=1

    try:
        print(master[0]*count+master[1]*countf)
    except:
        pass
    if count==0 and countf==0:
        print(master[2])



    if w1==master[1] and w2==master[1] and w3==master[1]:
        if w1==w2==w3:
            print("Congratulations You Won the game")
            print("The number is:",num)
            tim()
            break














