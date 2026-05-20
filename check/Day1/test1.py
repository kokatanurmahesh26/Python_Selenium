#memory management 
a = [1,2] #[1,2] list has two references 
b = a 
del a 

#garbage collection
x = 100
del x 


p = 200
print(id(p))