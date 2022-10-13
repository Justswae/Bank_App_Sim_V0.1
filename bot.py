from bank_sim_lib import chatbot as ct

def_pass=('2003')
chance=3
restart=('Y')
print('Welcome to TBS')
while chance>=0:
    pin=input('\nPlease input your 4 digit PIN\n >>> ')
    if pin==def_pass:
        print("You've entered the correct PIN\n")
        ct.initialize()
    else:
        print('Incorrect PIN ')
        chance-=1
        print(f'Tries left :{chance}\n')
        if chance==0:
            print('No more tries')
            break