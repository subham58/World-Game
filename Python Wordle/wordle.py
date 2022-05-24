from letter_state import LetterState


class Wordle:
    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5

    def __init__(self, secret: str): # self is an argument type in class or an instance of an object through which we can access values and init() is a function type where which takes parameters of Wordle 
        self.secret: str = secret.upper() # secret word to uppercase
        self.attempts = []
        pass    #The pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed. Empty code is not allowed in loops, function definitions, class definitions, or in if statements.

    def attempt(self, word: str):
        word = word.upper()
        self.attempts.append(word)

    def guess(self,word: str):
        word = word.upper()
        result = []
        for i in range(self.WORD_LENGTH):
            character = word[i]
            letter = LetterState(character)
            print(letter)
            letter.is_in_word = character in self.secret
            letter.is_in_position = character == self.secret[i]
            result.append(letter)
        return result


    @property #In Python, property() is a built-in function that creates and returns a property object. The syntax of this function is: property(fget=None, fset=None, fdel=None, doc=None) where, fget is function to get value of the attribute. fset is function to set value of the attribute.
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret #-1 is the last index of the list containing guesses

    @property
    def remaining_attempts(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts)

    @property
    def can_attempt(self):
        return self.remaining_attempts > 0 and not self.is_solved