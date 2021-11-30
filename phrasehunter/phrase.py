# Create your Phrase class logic here.
class Phrase:
    def __init__(self, pharse):
        # this is the actual phrase the Phrase object is representing.
        # This attribute should be set to the phrase parameter but converted to all lower case.
        self.pharse = pharse.lower()

    # this prints out the phrase to the console with guessed letters visibile and unguessed letters as underscores.
    # For example, if the current phrase is "hello world" and the user has guessed the letter "o", the output should look like this: _ _ _ _ o    _ o _ _ _
    def display(self, guesses):
        print('\n\n')
        for one in self.pharse:
            if one == ' ':
                print(' ', end = '')
            elif one in guesses:
                print(one, end = '')
            else:
                print('_', end = '')     

    #  checks to see if the letter selected by the user matches a letter in the phrase.
    def check_letter(self, guess):
        if guess in self.pharse:
            return True
        else:
            return False

    # checks to see if the whole phrase has been guessed.
    def check_complete(self, guesses):
        if (set(self.pharse) - set(' ')).issubset(set(guesses) - set(' ')):
            return True
        else:
            return False