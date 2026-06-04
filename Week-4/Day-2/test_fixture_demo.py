import pytest

@pytest.fixture
def user_profile() :
    print("This is my setup section")
    print("Loading active user account")
    user = {'user' : 'user',
            'role' : 'Admin'}  #SetUp
    yield user #it provide user disctionary to test
    print("This is my cleanup section")
    print("User looging out")
    user.clear() #Cleaning

def test_user_access(user_profile):
    print("checking if user has admin previls")
    assert user_profile['user'] == "user"
    assert user_profile['role'] == "Admin"

# def test_user_invalid_access(user_profile):
#     print("checking invlaid user has admin previls")
#     assert user_profile['user'] == "user1"
#     assert user_profile['role'] == "Admin1"
    
