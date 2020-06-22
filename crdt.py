
class Identifier:
    """
    A single digit for a position
    """
    digit = None
    userid = None
    
    def __init__(self, digit, userid) :
        self.digit = digit
        self.userid = userid

    def __str__(self):
        return "Identifier<" + str(self.digit) + ", " + str(self.userid) + ">"

    def str_digit(self):
        return str(digit)

class Entry:
    """
    A kv pair of index, char 
    """
    position = [] # [] Identifier
    value = None # char

    def __init__(self, position, value):
        self.position = position
        self.value = value


    def position_to_string():
        return map(Identifier.str_digit, position)



class Document:
    """
    Document, which is a list of Entries
    """
    document = None # TODO: make more efficient than just list of entries
    meta = None # TODO: some meta information 

    def __init__(self, document):
        self.document = document

def comparePositions(position1, position2):
    # first compare by identifiers
    for i in range(min(len(position1), len(position2))):
        curr_cmp = compareIdentifiers(position1[i], position2[i])
        if curr_cmp != 0:
            return curr_cmp

    # all identifiers were equal, tiebreak by len
    return len(position1) - len(position2)

def compareIdentifiers(i1, i2):
    if i1.digit < i2.digit:
        return -1
    elif i1.digit > i2.digit:
        return 1
    elif i1.digit == i2.digit:
        return i1.userid - i2.userid

# Given two positions, return a new position between those two using fractional indexing
# Use base 256 digits and just split between numbers
def indexBetweenPositions(lower_pos, upper_pos):
    # find diff
        # subtraction
        # todo base10? or what...
        # honestly fuck it ya whatever 
        # we can add more and more digits as needed
        # or base 16...
        #
        # int("123", base) where base >= 2 and base <= 26 


    # TODO:
    # 1. make int version of digits
    # 2. find diff 
    # 3. split the diff and go off
    #   also use userid as tiebreaker if necessary?


    # return lower_pos + diff / 2
    