from random import randint

#===================================
# version 2
#===================================

def main():
    print "Welcome to the number guessing game!"
    #while True:
       
    print "I have my number..."
    get_number = randint(1,10)
        
    guess_number = get_guess()
               
    check_number(guess_number, get_number)

        #if ('q' == raw_input("Enter q to quit or press Enter for another game ")):
         #   break
           
   # print 'Thanks for playing'

    
def get_guess():
    number_guess = raw_input('What is your guess [1-10]? ')
    while not (number_guess.isdigit() and int(number_guess) > 0 and int(number_guess) < 11):
        print "Your number {} is not valid".format(number_guess)
        number_guess = raw_input('What is your guess [1-10]? ')
        
    number_guess = int(number_guess)
    return number_guess

        
def check_number(guess_number, get_number):
    numbers_guessed = 0
    while (numbers_guessed < 5):
        if guess_number == get_number:
            print 'You got it!'
            break
        elif guess_number > get_number:
            print "That's too high. Try again!"
            numbers_guessed += 1
            chances_left = 5 - numbers_guessed
            print "You have {} guesses left".format(chances_left)
        else:
            print "That's too low. Try again"
            numbers_guessed += 1
            chances_left = 5 - numbers_guessed
            print "You have {} guesses left".format(chances_left)
        guess_number = get_guess()
        

if __name__ == '__main__':
    main()
