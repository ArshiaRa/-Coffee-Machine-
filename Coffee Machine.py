water = 400
milk = 540
beans = 120
cups = 9
money = 550


Ewater = 250
Ebeans = 16
Emilk = 0

Lwater = 350
Lbeans = 20
Lmilk = 75

Cwater = 200
Cbeans = 12
Cmilk = 100

def reduce(number,water11,beans11,milk11,money11,cups11):
    global water
    global beans
    global milk
    global money
    global cups
    if number == 1:
        water = water - water11
        milk = milk - milk11
        beans -= beans11
        money +=money11
        cups-=cups11
        
        
        
def check(coffee,water2,beans2,milk2,money,cups):
    global Emilk ,Ewater, Ebeans , Lwater , Lbeans , Lmilk,Cwater,Cbeans,Cmilk
    
    if coffee == 1:
        if water >=water2 and beans >= beans2:
            print("I have enough resources, making you a coffee!")
            reduce(1,Ewater,Ebeans,Emilk,4,1)
        elif water < water2:
            print("Sorry, not enough water!")
        elif beans < beans2:
            print("Sorry, not enough beans!")
            
    elif coffee == 2:
        if (water >=water2 and beans >= beans2 and milk >= milk2):
            print("I have enough resources, making you a coffee!")
            reduce(1,Lwater,Lbeans,Lmilk,7,1)
        elif water < Lwater:
            print("Sorry, not enough water!")
        elif beans < Lbeans:
            print("Sorry, not enough beans!")
        elif milk < Lmilk:
            print("Sorry, not enough milk!")
            
    elif coffee == 3:
        if (water >=water2 and beans >= beans2 and milk >= milk2):
            print("I have enough resources, making you a coffee!")
            reduce(1,Cwater,Cbeans,Cmilk,6,1)
        elif water < Cwater:
            print("Sorry, not enough water!")
        elif beans < Cbeans:
            print("Sorry, not enough beans!")
        elif milk < Cmilk:
            print("Sorry, not enough milk!")
            
            
def taking():
    global money
    print('I gave you',money)
    money = 0
def filling():
    global water
    global beans
    global milk
    global cups
    print("Write how many ml of water do you want to add:")
    waterPlus = int(input())
    water+=waterPlus
    print("Write how many ml of milk do you want to add:")
    milkPlus = int(input())
    milk+=milkPlus
    print("Write how many grams of coffee beans do you want to add:")
    beansPlus=int(input())
    beans+=beansPlus
    print("Write how many disposable cups of coffee do you want to add:")
    cupsPlus=int(input())
    cups+=cupsPlus
    

def state():
    print("The coffee machine has:")
    print(int(water) , 'of water')
    print(int(milk) , 'of milk')
    print(int(beans) , 'of coffee beans')
    print( int(cups),'of disposable cups')
    print('$'+str(money) , 'of money')

def buying():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    choose = (input())
    if choose =="back":
        return
    
    if int(choose) == 1:
        return check(1,Ewater,Ebeans,Emilk,money,cups)
    if int(choose) == 2:
        return check(2,Lwater,Lbeans,Lmilk,money,cups)
    if int(choose) == 3:
        return check(3,Cwater,Cbeans,Cmilk,money,cups)
    
def action(string):
    if string == 'remaining':
        return state()
    if string == 'buy':
        return buying()
    if string == 'fill':
        return filling()
    if string  == 'exit':
        exit(1)
    if string == 'take':
        return taking()
        
        
while True:
    print("Write action (buy, fill, take , remaining, exit):")
    string = input()
    action(string)
    

