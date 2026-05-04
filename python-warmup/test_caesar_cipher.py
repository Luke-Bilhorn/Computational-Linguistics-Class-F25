from warmup import caesar_cipher

def test_char_zero():
    assert caesar_cipher('D', 0) == 'D'

def test_char_near():
    assert caesar_cipher('M', 3) == 'P'

def test_char_far():
    assert caesar_cipher('T', 20) == 'N'
    
def test_word():
    assert caesar_cipher('OSSIFRAGE', 17) == 'FJJZWIRXV'
    
def test_sentence():
    assert caesar_cipher('I LEARNED PYTHON IN COMPUTATIONAL LINGUISTICS', 7) == 'P SLHYULK WFAOVU PU JVTWBAHAPVUHS SPUNBPZAPJZ'

def test_sentence_punc():
    assert caesar_cipher("WE DON'T HAVE TO INVOLVE THE AUTHORITIES IN THIS MATTER, DO WE, MR. BUXTON?", 9) == "FN MXW'C QJEN CX RWEXUEN CQN JDCQXARCRNB RW CQRB VJCCNA, MX FN, VA. KDGCXW?"
