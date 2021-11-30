# Create your Game class logic in here.
import random
from phrasehunter.phrase import Phrase


class Game:
    def __init__(self):
        # used to track the number of incorrect guesses by the user.
        # The initial value is 0 since no guesses have been made at the start of the game.
        self.missed = 0

        # a list of five Phrase objects to use with the game.
        # A phrase should only include letters and spaces -- no numbers, puntuation or other special characters.
        self.phrases = [Phrase('Eiffel Tower'),
                        Phrase('Great Wall'),
                        Phrase('Sun Moon Lake'),
                        Phrase('Tokyo Skytree'), 
                        Phrase('Sydney Opera House'),
                        Phrase('Golden Gate Bridge')]

        # This is the Phrase object that's currently in play.
        # The initial value will be None. Within the start() method, this property will be set to the Phrase object returned from a call to the get_random_phrase() method.
        self.active_phrase = self.get_random_phrase()

        # This is a list that contains the letters guessed by the user.
        self.guesses = []
    
    #　Calls the welcome method, creates the game loop, calls the get_guess method, adds the user's guess to guesses, increments the number of missed by one if the guess is incorrect, calls the game_over method.
    def start(self):
        self.welcome()
        while self.missed <5:
            # self.active_phrase.display(self.guesses)
            self.guesses.append(self.get_guess())
            if not self.active_phrase.check_letter(self.guesses[-1]):
                self.missed += 1
            elif self.active_phrase.check_complete(self.guesses):
                break        
        self.game_over()
        
    # this method randomly retrieves one of the phrases stored in the phrases list and returns it.
    def get_random_phrase(self):
        return random.choice(self.phrases)
    
    # this method prints a friendly welcome message to the user at the start of the game
    def welcome(self):
        print('\nWelcome To Phrase Hunter!\n')
        print('Guess the presented phrase, you can only make 5 wrong guesses.\n')    

    # this method gets the guess from a user and records it in the guesses attribute
    def get_guess(self):
        while True:
            try:
                self.active_phrase.display(self.guesses)

                if self.guesses:
                    guess_str = ', '.join(self.guesses)           
                    print(f'\n\nYou have guessed: {guess_str}.')
                else:
                    print('')                    
                
                user_guess = input(f'\n{5-self.missed} more chances. Guess a letter: ')
                if user_guess in self.guesses:
                    print('\nYou haved guessed this letter.')
                    raise                
                elif len(user_guess) == 1 and user_guess.isalpha():
                    return user_guess
                else:
                    print('\nThe guess is 1 character in length and that it is only letters: a through z.')
                    raise
            except:                
                print('Please try again.')

    # this method displays a friendly win or loss message and ends the game.
    def game_over(self):
        if self.missed < 5:
            print('\n=====================\n')
            print(f'Yay! {self.missed} miss.\nYou win!!')
        else:
            print('\n=====================\n')
            print('Oh no. You have maked 5 wrong guesses.\nGame over.\n')
        
        # the player was prompted to play again.
        while True:
            try:
                again = input('\nDo you want to play again? YES? or NO? ')
            except:
                print('That is not a valid value. Please try again.')
            else:
              if again.lower() == 'no':                
                  print('Bye Have a nice day.\n')
                  break
              elif again.lower() == 'yes':
                  print('OK Try a new noe.')
                  print('\n=====================\n')
                  game = Game()
                  game.start()
                  break                
              else:
                  print('That is not a valid value. Please try again.')