"""Write three test functions named 
test_make_full_name, test_extract_family_name, 
and test_extract_given_name. Each of the test 
functions will test one of three previously 
written program functions. Use pytest to run 
the test functions and find and fix the mistakes, 
if any, that are in program functions."""


from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest   



def test_make_full_name():

    assert make_full_name("Sally", "Brown") == "Brown Sally"
    assert make_full_name("Nathan", "Roper") == "Roper; Nathan"
    assert make_full_name("Sally", "") == "; Sally"
    assert make_full_name("", "Brown") == "Brown; "



#def test_extract_family_name():




#def test_extract_given_name():






# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])