# from random_word import RandomWords
# r = RandomWords()

# # Return a single random word
# word = r.get_random_word()

def main(): #overall program, need for restarting ability

    def restart(): #creates function to check if user wants to play again or not
        global count
        play_again = input("Would you like to play again? Enter y for yes or n for no. ")
        if play_again == "y":
            count = 0 
            main()
        elif play_again == "n":
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid input.")
            

    word = input("Enter the word to be guessed: ") #replace with random word generator
    if len(word) > 10: #difficulty based on amount of letters
        difficulty = 8
    elif len(word) > 5:
        difficulty = 6
    else:
        difficulty = 4

    hidden_word_list = [] #creates same as word list except letters replaced with underlines
    for i in range(len(word)):
        hidden_word_list.append("_")
    print(' '.join(hidden_word_list)) 

    word_list = list(word) #turns word into list of its letters
    wrong_letters = [] #list of guessed wrong list
    duplicate_letters = [] #list of letters already guess, right or wrong

    

    def check_guess(char_guess): #creates function to check letter guessed
        if char_guess in duplicate_letters: #if letter is already guessed
            char_guess = input("You have already guessed this letter. Guess again: ") #prompts user to guess again

        if char_guess in word_list and char_guess not in duplicate_letters: #if user guesses a correct letter
            for i in range(len(word_list)): #iterate through list
                if char_guess == word_list[i]: #if guessed letter matches letter in word list
                    hidden_word_list[i] = word_list[i] #then replaces underline with correct letter
                    duplicate_letters.append(word_list[i]) #adds letter to list of guessed letters
            print(' '.join(hidden_word_list)) #displays word w/ respective underlines and letters

        elif char_guess in duplicate_letters: #else if letter is already guessed
            check_guess(char_guess) #then go through function again

        else: #else if the letter has not been guessed and is wrong
            global count 
            count += 1 #increase hangman count

            if count < difficulty: #if user is still in the game
                wrong_letters.append(char_guess) #add letter to wrong letters list
                duplicate_letters.append(char_guess) #add letter to guessed letters list
                print("Wrong letters:", ', '.join(wrong_letters))
                print("You have", difficulty - count, "wrong tries left.")
                char_guess = input("Try again: ") #prompts user to guess another letter
                check_guess(char_guess) #goes through function again, checking if letter is right or wrong
            else: #user loses
                print("You lost... the word was", word)
                restart() 

        
            
        
    global count
    while "_" in hidden_word_list and count < difficulty: #if there are still unguessed letters and user has not reached hangman
        char_guess = input("Guess a letter: ") #keep on guessing 
        check_guess(char_guess) #checks letter guessed

    if count < difficulty and "_" not in hidden_word_list: #if user wins
        print("You win!")
        restart()
    

        

count = 0
main()