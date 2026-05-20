#Polymorphism
class chrome() :
    def browser(self) :
        print("chrome browaser launched")

class edge() :
    def browser(self) :
     print("edge browaser launched") 

class firefox() :
    def browser(self) :
     print("firefox browaser launched")   

browsers = [chrome(), edge(), firefox()]
# browsers = [chrome(), edge()]
for i in browsers :
   i.browser()