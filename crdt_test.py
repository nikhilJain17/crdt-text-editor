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

def test_comparePositions():
    x = Identifier(1, 2)
    e1 = Entry([x]*10, 'a')
    e2 = Entry([x]*11, 'a')

    assert(comparePositions(e1.position, e2.position) < 0)

    x = Identifier(1, 2)
    e1 = Entry([x]*10, 'a')
    e2 = Entry([x]*1, 'a')

    assert(comparePositions(e1.position, e2.position) > 0)

    x = Identifier(1, 2)
    e1 = Entry([x]*10, 'a')
    e2 = Entry([x]*10, 'a')

    assert(comparePositions(e1.position, e2.position) == 0)

    x = Identifier(1, 2)
    y = Identifier(1, 3)
    e1 = Entry([x, y], 'a')
    e2 = Entry([x, x], 'a')
    assert(comparePositions(e1.position, e2.position) > 0)

    x = Identifier(1, 2)
    y = Identifier(1, 3)
    e1 = Entry([x, x], 'a')
    e2 = Entry([x, y], 'a')

    assert(comparePositions(e1.position, e2.position) < 0)


    

if __name__ == "__main__":
    test_compareIdentifiers()
    test_comparePositions()
