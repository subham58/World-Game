class LetterState:
    def __init__(self, character: str):
        self.character: str = character
        self.is_in_word: bool = False
        self.is_in_positon: bool = False
        

    def __repr__(self): # In Python, __repr__ is a special method used to represent a class’s objects as a string. __repr__ is called by the repr() built-in function. You can define your own string representation of your class objects using the __repr__ method.
        return f"[{self.character} is_in_word: {self.is_in_word} is_in_position: {self.is_in_positon}]"