import os

def clear():
    os.system("clear")
    if os.name == "nt":
        os.system("cls")

shopping_list = []

clear()
print "Welcome to the Shopping List"

while True:
    add_products = raw_input("""\nDo you want to add items to your list?
Type 'y' for yes or 'n' for no: """).upper()

    if add_products == "Y":
        clear()
        new_product = raw_input("Write the product you want to add to your list: ")
        if new_product in shopping_list:
            print "\nThe item is already in the Shopping List and won't be added again!"
        elif len(new_product) == 0 or new_product.isspace():
            print "\nYou actually need to write the name of item you want to add!"
        else:
            shopping_list.append(new_product)
        continue

    elif add_products == "N":
        clear()
        print "Thank you for using Shopping List!\n"
        break

    else:
        clear()
        print "You chose an invalid option!\nTry again!"
        continue


if len(shopping_list) == 0:
    print "Your Shopping List is empty!\n"

else:
    print "This is your Shopping List:\n\n",
    for item in shopping_list:
        print item

    print "\n"
