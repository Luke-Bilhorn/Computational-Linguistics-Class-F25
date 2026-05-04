'''
Created on Nov 21, 2023

@author: tvandrun
'''

from word2vec import update_weights_one_sample
import numpy as np
from pytest import approx

W_orig = np.array([[.1, .2, .3],
                   [.11, .22, .33],
                   [.35, .25, .15],
                   [.03, .02, .01],
                   [.5, .6, .7]])
C_orig = np.array([[.81, .82, .83],
                   [.75, .25, .5],
                   [.4, .3, .2],
                   [.99, .98, .97],
                   [.5, .5, .5]])

def almost_equal(a, b, epsilon):
    assert len(a) == len(b)
    return np.array([a[i] == approx(b[i], epsilon) for i in range(len(a))])

def test_a():
    W = np.copy(W_orig)
    C = np.copy(C_orig)
    update_weights_one_sample(0, 1, [2,3], W, C, .001)
    assert (W[1:] == W_orig[1:]).all()
    assert (almost_equal(W[0], np.array([0.09794904, 0.1977332,  0.29784112]), .000001).all()
            or almost_equal(W[0], np.array([0.09947178, 0.19931638, 0.29948473]), .000001).all())
    assert (C[[0,4]] == C_orig[[0,4]]).all()
    assert almost_equal(C[1], np.array([0.75004317, 0.25008634, 0.5001295]), .000001).all()
    assert almost_equal(C[2], np.array([0.39994601, 0.29989202, 0.19983803]), .000001).all()
    assert almost_equal(C[3], np.array([0.98993576, 0.97987151, 0.96980727]), .000001).all()
   
def test_b():
    W = np.copy(W_orig)
    C = np.copy(C_orig)
    update_weights_one_sample(1, 2, [0], W, C, .001)
    assert (W[[0,2,3,4]] == W_orig[[0,2,3,4]]).all()
    #print(W[1])
    assert (almost_equal(W[1], np.array([0.10862624, 0.21858063, 0.32853502]), .000001).all()
            or almost_equal(W[1], np.array([0.10967005, 0.21961814, 0.32956623]), .000001).all())
    assert (C[[1,3,4]] == C_orig[[1,3,4]]).all()
    #print(C[[0,2]])
    assert almost_equal(C[0], np.array([0.80993041, 0.81986083, 0.82979124]), .000001).all()
    assert almost_equal(C[2], np.array([0.40005017, 0.30010034, 0.20015052]), .000001).all()
   
def test_c():
    W = np.copy(W_orig)
    C = np.copy(C_orig)
    update_weights_one_sample(0, 1, [2,3], W, C, .0001)
    assert (W[1:] == W_orig[1:]).all()
    assert (almost_equal(W[0], np.array([0.0997949,  0.19977332, 0.29978411]), .000001).all()
            or almost_equal(W[0], np.array([0.09994718, 0.19993164, 0.29994847]), .000001).all())
    assert (C[[0,4]] == C_orig[[0,4]]).all()
    assert almost_equal(C[1], np.array([0.75000432, 0.25000863, 0.50001295]), .000001).all()
    assert almost_equal(C[2], np.array([0.3999946, 0.2999892, 0.1999838]), .000001).all()
    assert almost_equal(C[3], np.array([0.98999358, 0.97998715, 0.96998073]), .000001).all()
  

