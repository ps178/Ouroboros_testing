# this is our unit testing for assignment 04

import pytest


def test_sum():
    from Assignment04 import Number_Calc
    test_input_list = ([1,3,5,7,9],[-2,-5,-6,-1],[4,-6,9,-1],[2.2,5.1,9.1,1.2],[-1.1,-5.2,-1.4,-3.8],[-1.1,2.2,-3.1])
    test_output_values = ((25),(-14),(6),(17.6),(-11.5),(-2))
    
    for count, elem in enumerate(test_input_list):
        trial = Number_Calc(My_List = (elem))
        assert trial.Sum == pytest.approx(test_output_values[count])

    with pytest.raises(TypeError):
        trial_Error = Number_Calc(My_List =['hello', 'hi'])
    with pytest.raises(ValueError):
        trial_Error = Number_Calc(My_List = [])
    
# Second function
def test_min_max():
    from Assignment04 import Number_Calc
    test_input_list = ([-1,5,8,100],[5,-8,9,45,88,34,65],[-5,8.234,-99023,342,9.452])
    test_output_values = ((100,-1),(88,-8),(342,-99023))

    for count, elem in enumerate(test_input_list):   #enumerate itirate and gives the index
        trial = Number_Calc(My_List = (elem))
        assert trial.Max_Min == test_output_values[count]
        assert isinstance(trial.Max_Min, tuple) == True 

def test_min_max_exceptions():
    from Assignment04 import Number_Calc
    with pytest.raises(TypeError):
        trial = Number_Calc(My_list = ['string','why'])
    with pytest.raises(ValueError):
        trial = Number_Calc(My_List = [])


def test_max_diff():
    from Assignment04 import Number_Calc
    test_input_list = [[10, 8, 5, 17, 16], [2, -7, 1.5]]
    test_output_value = [12, 9]
    for n, t in enumerate(test_input_list):
        trial = Number_Calc(My_List = (t))
        assert trial.Max_Difference == test_output_value[n]

    with pytest.raises(TypeError):  # Type error when None inputted
        trial = Number_Calc(My_list = [])
        trial2 = Number_Calc(My_List = ['sing'])
    with pytest.raises(ValueError):  # ValueError can occur when only 1 number given
        max([])  # This is where it fails in return_max_difference






