
from editdist import edit_distance

def test_trivial():
    assert edit_distance("", "", [1,1,1,1,0]) == 0
        
def test_all_ins():
    assert edit_distance("", "boo", [1,1,1,1,0]) == 3
        
def test_all_del():
    assert edit_distance("boo", "", [1,1,1,1,0]) == 3
        
def test_just_sub():
    assert edit_distance("x", "y", [1,1,1,1,0]) == 1
        
def test_one_sub():
    assert edit_distance("xxx", "xyx", [1,1,1,1,0]) == 1
        
def test_many_subs():
    assert edit_distance("cemetary", "seminary", [1,1,1,1,0]) == 3
        
def test_defiantly_by_sub():
    assert edit_distance("defiantly", "definitely", [1,1,1,1,0]) == 3

