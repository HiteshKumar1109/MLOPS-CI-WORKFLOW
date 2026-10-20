import pytest
#finction to test squer
def square(n):
    return n ** 2
# function to check the cube
def cube(n):
    return n ** 3
#function to check the fifth power
def fifthpower(n):
    return n ** 5
# testing the squre function 
def test_square():
    assert square(2)==4, "Test Failed:square of 2 should be 4"
    assert square(3)==9, "Test failed: Square of 3 should be 9"
def test_cube():
    assert cube(2)==8, "Test Failed: Ciube of 2 should be the 8"
    assert cube(3)==9,  "Test Failed : Cube of 3 should be the 27"
def test_fifth_power():
    assert fifthpower(2)==32 ,"Test Failed: fifthe powert of the 2 is 32"
    assert fifthpower(3)==243, "Test Failed: fifthe_power of 3 should be the 243"

def test_inaviled_input():
    with pytest.raises(TypeError):
        square("string") 