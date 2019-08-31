import time

userPassword =input('parola;')
userPasswordId = input('parola')
counter = 1
while userPasswordId != userPassword:
    print('Sorry the password is incorect.Try again!')
    counter = counter + 1
    print('You have', 3 - counter + 1, 'attempts left.')
    userPasswordId = input('Enter your password:')
    if counter == 3:
        print('Your account is locked for 30 seconds!!!!!')
        sec = 0
        while sec != 5:
            print('>>>>>>>>>>>>>>>>>>>>>', sec)
            time.sleep(1)
            sec += 1
        counter = 1