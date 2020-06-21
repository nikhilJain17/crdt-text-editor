from crdt import *

def test_compareIdentifiers():
    x = Identifier(1, 2)
    y = Identifier(1, 2)

    assert(compareIdentifiers(x,y) == 0)

    x = Identifier(1, 2)
    y = Identifier(2, 3)
    assert(compareIdentifiers(x,y) < 0)

    x = Identifier(1, 2)
    y = Identifier(1, 3)
    assert(compareIdentifiers(x,y) < 0)

    x = Identifier(0, 2)
    y = Identifier(1, 2)
    assert(compareIdentifiers(x,y) < 0)

    x = Identifier(0, 1)
    y = Identifier(1, 2)
    assert(compareIdentifiers(x,y) < 0)

    ###################################

    x = Identifier(10, 11)
    y = Identifier(0, 2)
    assert(compareIdentifiers(x,y) > 0)

    x = Identifier(10, 11)
    y = Identifier(10, 2)
    assert(compareIdentifiers(x,y) > 0)

    x = Identifier(10, 0)
    y = Identifier(0, 2)
    assert(compareIdentifiers(x,y) > 0)

if __name__ == "__main__":
    test_compareIdentifiers()