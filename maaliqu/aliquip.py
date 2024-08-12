class MyClass:
    def __init__(self):
        self.tuple = None

m = MyClass()
t = (1, 2, 3) # t is a tuple
m.tuple = t   # Assigning the tuple to the tuple attribute of object m
print(m.tuple) # Output: (1, 2, 3)
