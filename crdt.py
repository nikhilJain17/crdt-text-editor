
class Identifier:
    """
    A single digit for a position
    """
    digit = None
    userid = None
    
    def __init__(self, digit, userid) :
        self.digit = digit
        self.userid = userid


class Entry:
    """
    A kv pair of index, char 
    """
    position = [] # [] Identifier
    value = None # char

    def __init__(self, position, value):
        self.position = position
        self.value = value

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

def indexBetweenPositions(entry1, entry2):
    raise NotImplementedError