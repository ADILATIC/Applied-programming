import pytest
from BMI2 import calculateBMI, getUser
   
def test_calculateBMI():
    assert round(calculateBMI(150,72), 2) == 20.34
    
def test_calculateBMI2():
    assert round(calculateBMI(160,62), 2) == 29.26
    
def test_negHeight():
    try:
        BMI = calculateBMI(150,-72)
        assert False
    except ValueError:
        assert True
        
def test_negWeight():
    try:
        BMI = calculateBMI(-150, 72)
        assert False
    except ValueError:
        assert True

def test_zeroCheck():
    try:
        BMI = calculateBMI(0,0)
        assert False
    except ValueError:
        assert True