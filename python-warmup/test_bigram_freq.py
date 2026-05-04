from warmup import bigram_freq

def test_all_unique():
    text = 'abcdefghijk'
    bc = bigram_freq(text)
    assert len(bc) == len(text) - 1
    for bg  in bc :
        assert bc[bg] == 1

def test_all_x():
    text = 'xxxxxxxxxxxxxxxxx' 
    bc = bigram_freq(text)
    assert len(bc) == 1
    assert 'xx' in bc
    assert bc['xx'] == len(text) - 1

def test_hugkiss():
    text = 'oxoxoxoxoxoxoxoxoxox'
    bc =  bigram_freq(text)
    assert len(bc) == 2
    assert bc['ox'] == len(text) // 2
    assert bc['xo'] == (len(text) // 2) - 1
    
def test_j_sentence():
    text = 'jaguars juggling jam jars javelin jugulars'
    bc = bigram_freq(text)
    assert bc['ja'] == 4
    assert bc['ju'] == 2
    assert bc[' j'] == 5
    assert bc['ar'] == 3
    assert bc['rs'] == 3
    assert bc['s '] == 2
