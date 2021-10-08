secrect_number = int(input('Input Secret Number \t'))
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess =int(input('Guess: '))
    guess_count +=1
    if guess == secrect_number:
        print('You won !')
        break
else:
    print('Sorry you Failed!!')