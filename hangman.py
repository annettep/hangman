# from random_word import RandomWords
# r = RandomWords()

# # Return a single random word
# word = r.get_random_word()

def main():
    word = input("Enter the word to be guessed: ") #replace with random word generator

    hidden_word_list = [] #creates same as word list except letters replaced with underlines
    for i in range(len(word)):
        hidden_word_list.append("_")
    print(' '.join(hidden_word_list)) 

    #count = 0 #represents hangman

    word_list = list(word) #turns word into list of its letters
    wrong_letters = []
    duplicate_letters = []
    def check_guess(char_guess): #creates function to check letter guessed
        if char_guess in word_list: #if user guesses a correct letter
            for i in range(len(word_list)): #iterate through list
                if char_guess == word_list[i]: #if guessed letter matches letter in word list
                    hidden_word_list[i] = word_list[i] #then replaces underline with correct letter
            print(' '.join(hidden_word_list))
        else: #if user does not guess correct letter
            global count 
            count += 1 #increase hangman count
            wrong_letters.append(char_guess)
            print("Wrong letters:", ', '.join(wrong_letters))
            print("You have", 6 - count, "wrong tries left.")
            if count < 6: #checks if hangman still alive
                char_guess = input("Wrong guess, try again: ") #prompts user to guess another letter
                check_guess(char_guess) #goes through function again, checking if letter is right or wrong
            else: #user loses
                print("You lost... the word was", word)
                play_again = input("Would you like to play again? Enter y for yes or n for no. ")
                if play_again == "y":
                    count = 0 
                    main()
                elif play_again == "n":
                    print("Thanks for playing!")
                    exit()
                else:
                    print("Invalid input.")
        
    global count
    while "_" in hidden_word_list and count < 6: #if there are still unguessed letters and user has not reached hangman
        char_guess = input("Guess a letter: ") #keep on guessing 
        check_guess(char_guess) #checks letter guessed

    if count < 6 and "_" not in hidden_word_list: #if user wins
        print("You win!")
        play_again = input("Would you like to play again? Enter y for yes or n for no. ")
        if play_again == "y":
            count = 0 
            main()
        elif play_again == "n":
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid input.")
        

count = 0
main()