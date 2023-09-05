Y_AXIS_LABEL = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
X_AXIS_LABEL = tuple(range(1, 9))

class BoardCoordinates:
    def __init__(self, x, y):
        self.row = int(x)     #{loc : piece}
        self.col = int(y)
        
    # Convenient function that automatically converts the object to its string format when needed

    def __str__(self):
        return self.letter_notation().upper()
    
    def letter_notation(self):
        if not self.is_in_bound():
            return
        return str(Y_AXIS_LABEL[int(self.col)]) + str(X_AXIS_LABEL[int(self.row)])
    
        