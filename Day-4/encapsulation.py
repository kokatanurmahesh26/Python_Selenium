class Loginautomation :
    def __init__(self):
        self.__username = "admin" #private variables
        self.__password = "admin@123"
    def login(self) :
        print("logging into application")
        print("username : ", self.__username)
        print("password : ", self.__password)

    def change_password(self, new_password) :
        if(len(new_password)) >= 8 :
            self.__password = new_password
            print("password updated successsfully")
            # print("password : ", self.__password)
        else :
            print("weak password")

test = Loginautomation()
test.login()
test.change_password("securepass")
test.change_password("secure")

#Example2
class browserconfig :
    def __init__(self):
        self.__browser = "chrome"
        self.__timeout = 30
    def get_config(self) :
        print("browser : ", self.__browser)
        print("browser : ", self.__timeout) 

    def set_timeout(self, time) :
        if time > 0 :
            print("timeout update successfull")
        else :
            print("invalid timeout value")
config = browserconfig()
config.get_config()
config.set_timeout(60)
config.get_config()
# print(config.__timeout)