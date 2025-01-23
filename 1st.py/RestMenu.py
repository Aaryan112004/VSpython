menu={
    'Pizza':100,
    'Extra cheesy pizza':130,
    'Pasta':80,
    'Creamy pasta':100,
    'Burger':50,
    'Large cheesy burger':90,
    'Salad':40,
    'Cold coffee':40,
    'Hot coffee':30,
          }
print("Welcome to VIP Resturant : ")
print("""
    'Pizza':100,
    'Extra cheesy pizza':130,
    'Pasta':80,
    'Creamy pasta':100,
    'Burger':50,
    'Large cheesy burger':90,
    'Salad':40,
    'Cold coffee':40,
    'Hot coffee':30,""")
#else u can type like this.....Pizza':100RS\nExtra cheesy pizza':130RS\nPasta':80RS\n...

ORDER_LIST=0

ITEM_1=input("Enter your first order please :")             #for item 1
if ITEM_1 in menu:
    ORDER_LIST+=menu[ITEM_1]
    print(f"Your first order {ITEM_1} is added")
else:
    print(f"your {ITEM_1} is not available for now ")

ANOTHER_ITEM=input("Do you want another item too ?(YES/NO)")

if ANOTHER_ITEM=="YES":                                      #for 2nd item
    ITEM_2=input("Enter your second order please :")
    if ITEM_2 in menu:
        ORDER_LIST+=menu[ITEM_2]
        print(f"Your second order {ITEM_2} is added")
    else:
        print(f"your {ITEM_2} is not available for now ")

ANOTHER_ITEM2=input("Do you want another item too ?(YES/NO)")

if ANOTHER_ITEM2=="YES":                                     #for next item
    ITEM_3=input("Enter your second order please :")
    if ITEM_3 in menu:
        ORDER_LIST+=menu[ITEM_3]
        print(f"Your second order {ITEM_3} is added")
    else:
        print(f"your {ITEM_3} is not available for now ")

print(f"Total bill is ={ORDER_LIST}")