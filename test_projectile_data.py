#The following are checking importing errors for projectile data
import projectile_data as pd

"""A lot of the tests that are conducted with this document will be based on user input and providing the correct error to the user along
with a description of how to correct the error"""
###It was said that this would be covered at a later time in class

def test_data():
    # This error should trigger if a non-existing data file is selected
    obs = 1
    exp = 1
    assert exp==obs
    