
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
        return str(self.digit)

class Entry:
    """
    A kv pair of index, char 
    """
    position = [] # [] Identifier
    value = None # char

    def __init__(self, position, value):
        self.position = position
        self.value = value


    def positionToString(self):
        return "".join([Identifier.str_digit(s) for s in self.position])

    def positionToInt(self):
        return int(self.positionToString())


# typedef Position = [Identifier]

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
# TODO: just use arbitrary precision arithmetic for now, and deal with site ID as tiebreaker later?
def indexBetweenPositions(lower_entry, upper_entry, user_id):
    # TODO:
    # 1. make str version of digits
    # 2. find diff 
    # 3. split the diff and go off
    #   also use userid as tiebreaker if necessary?
    lower_pos_str = lower_entry.positionToString()
    upper_pos_str = upper_entry.positionToString()

    # pad with zeros if necessary
    upper_len = len(upper_pos_str)
    lower_len = len(lower_pos_str)

    if lower_len < upper_len:
        lower_pos_str += ("0"*(upper_len - lower_len))
    elif lower_len > upper_len:
        upper_pos_str += ("0"*(lower_len - upper_len))

    print(upper_pos_str + "\n" + lower_pos_str)

    # find first different digit
    first_diff_index = -1
    for i in range(len(upper_pos_str)):
        if upper_pos_str[i] != lower_pos_str[i]:
            first_diff_index = i
            break
    
    # can't find in between two identical entries...
    if first_diff_index == -1:
        return None

    # from diff index onwards, generate new nums
    lower_tail = (lower_pos_str[first_diff_index:])
    upper_tail = (upper_pos_str[first_diff_index:])
    print(lower_tail, upper_tail, first_diff_index)
    # find delta
    delta = int(upper_tail) - int(lower_tail)
    print(delta)
    # add delta / 2 to lower
    middle_str = lower_pos_str[:first_diff_index] + str(int(delta / 2))
    print("m", middle_str)

    e = Entry([Identifier(s, user_id) for s in middle_str], "")
    assert(lower_entry.positionToInt() < e.positionToInt())
    assert(upper_entry.positionToInt() > e.positionToInt())

    # return lower_pos + diff / 2
    return e

