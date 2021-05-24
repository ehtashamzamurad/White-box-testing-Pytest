import pytest
import lab9
from lab9 import getMax

#Statement coverage
def test_statement_coverage():
    #cover 100% of the statement
    result = getMax.getMax1(1,5,10)
    assert result == 10

#Branch coverage
def test_branch_coverage():
    result = getMax.getMax1(10,4,6)
    assert result == 10
#We covered 66% and after running the below code it changed to 50%

def test_branch2():
    result = getMax.getMax1(5,3,6)
    assert result == 6
#Achieved 75%
def test_branch():
    #The following executes the function 'getMax1' with the input data "0, 0, 0"
    result = getMax.getMax1(1, 1, 1)
    #The following verifies if the execution result is consistent with expectation
    assert result == 1
#Covered 100% branches

#Path Coverage
def test_path1():
    result = getMax.getMax1(0,1,2)
    #Where a<b<c
    assert result == 2

#TC2
def test_path2():
    result = getMax.getMax1(0,2,1)
    #Where a<b but b>c
    assert result == 2

#TC3
def test_path3():
    result = getMax.getMax1(2,1,0)
    # a>b>c
    assert result == 2

#TC4
def test_path4():
    result = getMax.getMax1(1,0,2)
    # a>b but a<c
    assert result == 2