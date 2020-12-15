drinks = {'beer': 3,
          'wine': 5,
          'vodka': 6,
          'craft': 4
          }


def new_line():
    print("")


new_line()
print(drinks)
new_line()


while True:
    drink = input('what would you like to drink?:').strip().lower()
    if drink in drinks:
        age = int(input('how old are you?: ').strip())
        if age >= 18:
            cash = int(input('how much money do you have?: ').strip())
            if cash < drinks[drink]:
                print('you dont have enough money to drink!')
                break
            else:
                print('enjoy your drink!')
                break
        else:
            print('you are too young to drink come back when you are older!')
            break
    else:
        print('sorry we dont serve this drink, take a look at our drinks:')
        print(drinks)
