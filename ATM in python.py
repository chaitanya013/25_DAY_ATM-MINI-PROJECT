# ATM managment system mini project

username='python'
password='python123'

c_name=input('enter your name:')
c_password=str(input('enter your password:'))

if c_name==username and c_password==password:
    print('''
    1.deposite
    2.withdraw
    3.mini_statment
    4.exit
    ''')
    amount=50000
    option=int(input('enter your option:'))
    if option==1:
        deposite=int(input('enter your amount:'))
        amount+=deposite
        print('total amount:',amount)
    elif option==2:
        withdraw=int(input('enter your amount:'))
        amount-=withdraw
        print('total amount:',amount)
    elif option==3:
        print('====ATM====')
        print('c_name:',username)
        print('total amount:',amount)
        print('===Thanks for visiting===')
    elif option==4:
        exit()
else:
    print('please ckeck your username and password')

