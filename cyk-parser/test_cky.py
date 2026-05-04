'''
Created on Oct 25, 2021

@author: tvandrun
'''

from cky_parser import parse


def run_test(sentence, st_expected):
    syntax_trees = parse(sentence.split())
    st_given = [str(st) for st in syntax_trees]
    assert len(st_given) == len(st_expected)
    for s in st_expected :
        assert any([ss == s for ss in st_given])
        
    
def test_trans_prep():
    run_test('the boy hit the ball in the field',
                  ['(Sentence (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun boy))))) (VerbPhrase (VPA (VPB (Verb hit) (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun ball)))))) (PrepPhrase (Prep in) (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun field)))))))))',
                   '(Sentence (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun boy))))) (VerbPhrase (VPA (VPB (Verb hit) (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun ball))) (PrepPhrase (Prep in) (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun field))))))))))))'])

def test_intrans():
    run_test('the dog ran',
                  ['(Sentence (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun dog))))) (VerbPhrase (VPA (VPB (Verb ran)))))'])

def test_trans_prep2():
    run_test('the cat chased the dog in the kitchen',
                  ['(Sentence (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun cat))))) (VerbPhrase (VPA (VPB (Verb chased) (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun dog)))))) (PrepPhrase (Prep in) (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun kitchen)))))))))',
                   '(Sentence (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun cat))))) (VerbPhrase (VPA (VPB (Verb chased) (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun dog))) (PrepPhrase (Prep in) (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun kitchen))))))))))))'])

def test_nested():
    run_test('she knew that he knew that she knew that he knew that she knew that he knew that she knew that he loved her',
                  ['(Sentence (NounPhrase (ConcNP (CNPA (PersPronoun she)))) (VerbPhrase (VPA (VPB (Verb knew) (NounPhrase (AbsNP (That that) (Sentence (NounPhrase (ConcNP (CNPA (PersPronoun he)))) (VerbPhrase (VPA (VPB (Verb knew) (NounPhrase (AbsNP (That that) (Sentence (NounPhrase (ConcNP (CNPA (PersPronoun she)))) (VerbPhrase (VPA (VPB (Verb knew) (NounPhrase (AbsNP (That that) (Sentence (NounPhrase (ConcNP (CNPA (PersPronoun he)))) (VerbPhrase (VPA (VPB (Verb knew) (NounPhrase (AbsNP (That that) (Sentence (NounPhrase (ConcNP (CNPA (PersPronoun she)))) (VerbPhrase (VPA (VPB (Verb knew) (NounPhrase (AbsNP (That that) (Sentence (NounPhrase (ConcNP (CNPA (PersPronoun he)))) (VerbPhrase (VPA (VPB (Verb knew) (NounPhrase (AbsNP (That that) (Sentence (NounPhrase (ConcNP (CNPA (PersPronoun she)))) (VerbPhrase (VPA (VPB (Verb knew) (NounPhrase (AbsNP (That that) (Sentence (NounPhrase (ConcNP (CNPA (PersPronoun he)))) (VerbPhrase (VPA (VPB (Verb loved) (NounPhrase (ConcNP (CNPA (PersPronoun her))))))))))))))))))))))))))))))))))))))))))))))))))'])
        
def test_abstract_subj():
    run_test('that he loved her troubled her',
                  ['(Sentence (NounPhrase (AbsNP (That that) (Sentence (NounPhrase (ConcNP (CNPA (PersPronoun he)))) (VerbPhrase (VPA (VPB (Verb loved) (NounPhrase (ConcNP (CNPA (PersPronoun her)))))))))) (VerbPhrase (VPA (VPB (Verb troubled) (NounPhrase (ConcNP (CNPA (PersPronoun her))))))))'])
        
def test_relative() :
    run_test('the dog that wagged a tail is the one which ate the bone',
                  ['(Sentence (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun dog))) (RelClause (RelPronoun that) (VerbPhrase (VPA (VPB (Verb wagged) (NounPhrase (ConcNP (CNPA (Art a) (Nominal (Noun tail))))))))))) (VerbPhrase (VPA (VPB (Verb is) (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun one))) (RelClause (RelPronoun which) (VerbPhrase (VPA (VPB (Verb ate) (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun bone)))))))))))))))'])
        
def test_abstract_dirobj() :
    run_test('the woman knew that the man loved her',
                  ['(Sentence (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun woman))))) (VerbPhrase (VPA (VPB (Verb knew) (NounPhrase (AbsNP (That that) (Sentence (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun man))))) (VerbPhrase (VPA (VPB (Verb loved) (NounPhrase (ConcNP (CNPA (PersPronoun her))))))))))))))'])

def test_still() :
    run_test('the still still stills me still',
                  ['(Sentence (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Adj still) (Nominal (Noun still)))))) (VerbPhrase (VPA (VPB (Verb stills) (NounPhrase (ConcNP (CNPA (PersPronoun me)))))) (Adv still)))'])

def test_nested_subj() :
    run_test('that that the cheese was gone troubled the mouse interested the scientist',
                  ['(Sentence (NounPhrase (AbsNP (That that) (Sentence (NounPhrase (AbsNP (That that) (Sentence (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun cheese))))) (VerbPhrase (VPA (VPB (Verb was) (Adj gone))))))) (VerbPhrase (VPA (VPB (Verb troubled) (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun mouse))))))))))) (VerbPhrase (VPA (VPB (Verb interested) (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun scientist)))))))))'])
        

def test_adv() :
    run_test('the scarecrow walked awkwardly',
                  ['(Sentence (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun scarecrow))))) (VerbPhrase (VPA (VPB (Verb walked))) (Adv awkwardly)))'])

def test_abiguous_prep() :
    run_test('he saw the dog with the binoculars',
                  ['(Sentence (NounPhrase (ConcNP (CNPA (PersPronoun he)))) (VerbPhrase (VPA (VPB (Verb saw) (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun dog)))))) (PrepPhrase (Prep with) (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun binoculars)))))))))',
                   '(Sentence (NounPhrase (ConcNP (CNPA (PersPronoun he)))) (VerbPhrase (VPA (VPB (Verb saw) (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun dog))) (PrepPhrase (Prep with) (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun binoculars))))))))))))'])
        
def test_ambiguous_verb() :
    run_test('the plain trains like a juicy apple',
                  ['(Sentence (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Noun plain))))) (VerbPhrase (VPA (VPB (Verb trains)) (PrepPhrase (Prep like) (NounPhrase (ConcNP (CNPA (Art a) (Nominal (Adj juicy) (Nominal (Noun apple))))))))))',
                   '(ConcNP (CNPA (Art the) (Nominal (Adj plain) (Nominal (Noun trains)))) (PrepPhrase (Prep like) (NounPhrase (ConcNP (CNPA (Art a) (Nominal (Adj juicy) (Nominal (Noun apple))))))))',
                   '(Sentence (NounPhrase (ConcNP (CNPA (Art the) (Nominal (Adj plain) (Nominal (Noun trains)))))) (VerbPhrase (VPA (VPB (Verb like) (NounPhrase (ConcNP (CNPA (Art a) (Nominal (Adj juicy) (Nominal (Noun apple))))))))))',
                   '(NounPhrase (ConcNP (CNPA (Art the) (Nominal (Adj plain) (Nominal (Noun trains)))) (PrepPhrase (Prep like) (NounPhrase (ConcNP (CNPA (Art a) (Nominal (Adj juicy) (Nominal (Noun apple)))))))))'])
 
        
        
        
