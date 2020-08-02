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

def test_positionToInt():
    position1 = []
    for i in range(1,4):
        position1.append(Identifier(i, i % 2))
    e1 = Entry(position1, None)
    ans1 = e1.positionToInt()
    assert(ans1 == 123)

    position2 = []
    for i in range(1, 14):
        position2.append(Identifier(i % 10, i % 2))
    e2 = Entry(position2, None)
    ans2 = e2.positionToInt()
    assert(ans2 == 1234567890123)    

# @TODO add a lot more tests lol
def test_indexBetweenPositions():
    position1 = []
    for i in range(1,4):
        position1.append(Identifier(i, i % 2))
    e1 = Entry(position1, None)
    ans1 = e1.positionToInt()
    assert(ans1 == 123)

    position2 = []
    for i in range(1, 14):
        position2.append(Identifier(i % 10, i % 2))
    e2 = Entry(position2, None)
    ans2 = e2.positionToInt()
    assert(ans2 == 1234567890123)    

    e_middle = indexBetweenPositions(e1, e2, 12)
    ans_middle = e_middle.positionToInt()
    assert(ans1 < ans_middle)
    assert(ans_middle < ans2)

    print("ans1", ans1, "ans middle", ans_middle, "ans2", ans2)

if __name__ == "__main__":
    test_compareIdentifiers()
    test_comparePositions()
    test_positionToInt()
    test_indexBetweenPositions()
