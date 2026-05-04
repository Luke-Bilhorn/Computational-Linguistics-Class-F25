

class Leaf :    
    def __init__(self, c, frequency=1):
        # The character represented by this leaf
        self.c = c
        self.frequency = frequency
        # The set of characters in the subtree rooted here,
        # which is just the one letter
        self.letters = set([c])
    def contains(self, x):
        return x == self.c
    def total_freq(self):
        return self.frequency
    def __str__(self):
        return "Leaf(" + self.c + "," + str(self.frequency) + ")"

class Internal :
    def __init__(self, left, right):
        # The left and right children
        self.left = left
        self.right = right
        # The set of characters in the subtree rooted here
        self.letters = left.letters.union(right.letters)

    def contains(self, x):
        return (x in self.letters)

    def total_freq(self):
        return self.left.total_freq() + self.right.total_freq()

    def __str__(self):
        return "Internal(" + str(self.left) + "," + str(self.right)  + ")"
    
    def __eq__(self, other):
        return type(other) == Internal and self.left == other.left and self.right == other.right
