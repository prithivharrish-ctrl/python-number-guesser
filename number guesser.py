import random
opt = '1234567890'
m=0
num=''.join(random.choices(opt, k=4))
if len(set(num))!=4:
     print('The generated number has duplicate digits, generating a new number...')
     num=''.join(random.choices(opt, k=4))
     while m<10 and len(num)==4:
            guess=str(input("Enter your guess: "))
            m+=1
            if guess==num:
                print('Congratulations! You guessed the number correctly.')
                break
            if len(guess)!=4:
                        print('Your guess should be 4 digits long')
            if m!=10:
                for i in range(4):
                    if num[i]==guess[i]:
                        print('This digit is correct and in the correct position',guess[i])
                    elif guess[i] in num:
                        print('This digit is correct but in the wrong position',guess[i])
                    else:
                        print('This digit is incorrect',guess[i])
            else:
                print('You have reached your limit, the answer was',''.join(num))
            print('number of attempts left',10-m)