def countE_v1(s):
    count = 0
    for c in s:
        if c.lower() =='e':
            count = count + 1
    return count

def countE_v2(s):
    count = 0
    for c in s:
        if c =='e' or c=='E':
            count = count + 1
    return count


def countEWrong(s):
    count = 0
    for c in s:
        if c =='e' or 'E':
            count = count + 1
    return count

def countE(s):
    count = 0
    for c in s.lower():
        if c =='e':
            count = count + 1
    return count


def test_countE_1():
    assert countE("The")==1

def test_countE_2():
    assert countE("UCSB")==0

def test_countE_3():
    assert countE("Eagle")==2
