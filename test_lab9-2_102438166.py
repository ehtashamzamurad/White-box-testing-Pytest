import pytest
import lab9
from lab9 import getMax

#Statement coverage
def test_statement_coverage():
    #cover 100% of the statement
    result = getMax.getMax2(1, 2, 3)
    assert result == 3

#Branch coverage
def test_branch():
    result = getMax.getMax2(2, 1, 3)
    assert result == 3
#We covered 66% and after running the below code it changed to 50%

def test_branch2():
    result = getMax.getMax2(3, 4, 2)
    assert result == 4
#Achieved 75%
def test_branch3():
    #The following executes the function 'getMax2' with the input data "0, 0, 0"
    result = getMax.getMax2(2, 1, 0)
    #The following verifies if the execution result is consistent with expectation
    assert result == 2
#Covered 100% branches
def test_branch4():
    result = getMax.getMax2(3, 5, 5)
    assert result == 5

#Path Coverage
def test_path1():
    result = getMax.getMax2(0,1,2)
    #Where a<b<c
    assert result == 2

#TC2
def test_path2():
    result = getMax.getMax2(0,2,1)
    #Where a<b but b>c
    assert result == 2

#TC3
def test_path3():
    result = getMax.getMax2(2,1,0)
    # a>b>c
    assert result == 2

#TC4
def test_path4():
    result = getMax.getMax2(1,0,2)
    # a>b but a<c
    assert result == 2
