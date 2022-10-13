class chatbot():
    '''Banking App sim. by Tobi -2022/9/5'''
    #V0.1
    # _ This is a simple simulation of a banking app
    # _ Further updates will have more features integrated as they roll out
    # _ ....
    
    
    def initialize():
        default_balance=100
        restart=('y')
        negate=('no','n')
        print('Welcome to Tobi-The-Banking bot V1')
        while restart not in negate:
            req=(input('What would you like to do today?\n 1. Deposit\n 2. Withdraw\n 3. Check balance\n 4. Contact customer care \n\n >>>'))
            print(req)
            if req==('1'):
                deposit=int(input("How much would you like to deposit today ?\n >>> $"))
                print(deposit)
                new_bal=default_balance+deposit
                print(f"Your new balance is ${new_bal} ")
                restart=input("Would you like to go back?\n >>> ")
                if restart.lower() in negate:
                    print('Thank You, Goodbye!')
                    break
            elif req==('2'):
                withdraw=int(input('How much would you like to withdraw ?\n >>> $'))
                if withdraw>default_balance:
                    print(f'Insufficient funds! Your balance is ${default_balance}')
                else:
                    updated_bal=default_balance-withdraw
                    print(f'Successful, your new balance is ${updated_bal}\n')
                    restart=input("Would you like to go back?\n >>> ")
                    if restart.lower() in negate:
                        print('Thank You, Goodbye!')
                        break
            elif req==('3'):
                print(f'Your current balance is ${default_balance}\n')
                restart=input("Would you like to go back?\n >>> ")
                if restart.lower() in negate:
                    print('Thank You, Goodbye!')
                    break
            elif req==('4'):
                print('Sorry,our csutomer service agents are not available at the moment \n Kindly try again later !\n')
                restart=input("Would you like to go back?\n >>> ")
                if restart.lower() in negate:
                    print('Thank You, Goodbye!')
                    break
            else:
                print('Please select a valid option!')