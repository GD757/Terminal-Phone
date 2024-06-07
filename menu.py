def menu():
    print('[1] Option 1')
    print('[2] Go to Google.com!')
    print('[3] Add a Contact')
    print('[0] Exit')

menu()

option = int(input('Enter your option: '))
             
while option != 0:
    if option == 1:
        print('def manage contacts')
    if option == 2:
        print('def search the internet')
    if option == 3:
        print('def manage tasks')
    print()
    menu()
    option= int(input("Enter your option: "))
