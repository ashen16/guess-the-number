# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui
import math


# initialize global variables used in your code
secret_num = 0
num_range = 100
num_guess = 7
num_guess_counter = num_guess
#to start and restart the game
def new_game():
    global num_range, num_guess, secret_num, num_guess_counter
    num_guess_counter = num_guess
    
    print ""
    # print out the new game message and the number of the remaining guesses    
    print "New game. Range is from 0 to " + str(num_range)
    print "Number of remaining guesses is " + str(num_guess_counter)
 
    #call and randomlly assign global variable secret_number
    secret_num = random.randrange(0, num_range)

                              
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global num_guess, num_range, num_guess_counter
    num_guess_counter = num_range
    num_range = 100
    new_game()    
   

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range, num_guess, num_guess_counter
    num_range = 1000
    num_guess_counter = num_guess = 10
    new_game()
    
    

def input_guess(guess):
   
    global secret_num, num_guess, num_guess_counter
    num_guess_counter -= 1 
    print ""
    print "Guess was " + str(guess)
    print "Number of remaing guess is " + str(num_guess_counter)
    
    if guess.isdigit(): ## check valid input
        if float(guess) != secret_num and (num_guess_counter == 0):
        # game ends and call new game
            print "Game Over! The secret number is " +str(secret_num)
            new_game()
        # main game logic goes here	    
        elif float(guess) > secret_num:
            print "Lower" 
        elif float(guess) < secret_num:        
            print "Higher"
        else:       
            print "Correct"        
            new_game()
    else:
        print 'Input must be a number from 0 to ', str(num_range), '\n'
    inp.set_text('') #clear input box
        
# create frame
frame = simplegui.create_frame("Guess", 300,300)
frame.set_canvas_background("Green")

# register event handlers for control elements
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
inp = frame.add_input('Enter a Guess', input_guess, 200)
inp.set_text('')

# call new_game and start frame
frame.start()
new_game()

# always remember to check your completed program against the grading rubric
