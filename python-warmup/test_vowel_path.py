from warmup import vowel_path

def test_vert():
    assert vowel_path([['a', 'd', 'i', 'q', 'b', 'e', 'k']]) == 3

def test_horz():
    assert vowel_path([['x'], ['e'], ['a'], ['v'], ['y'], ['o']]) == 3.5
    
def test_square():
    assert vowel_path([['s', 'f', 'k', 'f', 'a', 'e'],
                       ['s', 'b', 'f', 'm', 'd', 'a'],
                       ['o', 'k', 'a', 'w', 'g', 'y'],
                       ['u', 'r', 'p', 'd', 's', 'e'],
                       ['y', 'x', 'a', 'g', 'o', 'l'],
                       ['u', 'y', 'p', 'z', 'c', 'q']]) == 4.5

def test_alphabet() :
    assert vowel_path([['a', 'b', 'c', 'd'],
                       ['e', 'f', 'g', 'h'],
                       ['i', 'j', 'k', 'l'],
                       ['m', 'n', 'o', 'p'],
                       ['r', 's', 't', 'u'],
                       ['v', 'w', 'x', 'y']]) == 5.5
    
def test_follow_y() :
    assert vowel_path([['y', 'y', 'y', 'y', 'x', 'e'], 
                       ['a', 'x', 'x', 'y', 'x', 'x'], 
                       ['x', 'x', 'x', 'y', 'x', 'x'], 
                       ['x', 'x', 'x', 'y', 'y', 'x'], 
                       ['x', 'x', 'x', 'x', 'y', 'x'], 
                       ['x', 'x', 'x', 'x', 'y', 'y']]) == 5.5
    
    
    