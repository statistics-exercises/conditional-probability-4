import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_output(self) : 
        self.assertTrue( denom==sy.integrage( t*2*t, (t,0,1) ), "the variable denom has not been set correctly" )
        self.assertTrue( posterior==sy.simplify( t*2*t / denom ), "the variable posterior has not been set correctly" )
