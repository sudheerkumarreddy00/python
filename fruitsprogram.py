# fruits program
print('*'*10,'Fruits','*'*10)
print('1.apple')
print('2.orange')
print('3.mango')
print('4.banana')
print('5.guva')
print()

cart[]
while True:
    print('1.Add')
    print('2.Remove')
    print('3.Display')
    print('4.Exit')

    ch = int(input('choose the options:'))
    if ch == 1:
        fruit = input('which fruit,you want')
        if fruit in cart:
            print(fruit,'already there in cart')
        else:
            cart.append(fruit)
            print(fruit,'is added to cart')
    elif ch == 2:
        fruit = input('which fruit, you want to remove')
        if fruit in cart:
            cart.remove(fruit)
            print(fruit,'is removed from cart')
        else:
            print(fruit,'is not available in cart')
    elif ch == 3:
        

















    
