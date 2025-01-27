class Person: 
    def __init__(self, fname: str, mname: str = None, lname: str = None):
        self.fname = fname
        self.mname = mname
        self.lname = lname

    def full_name(self) -> str: 
        full_name = self.fname
        if self.mname is not None: 
            full_name = f"{full_name} {self.mname}"
        if self.lname is not None: 
            full_name = f"{full_name} {self.lname}"
        return full_name
    
# p1 = Person("George", "James", "Smith")
# p2 = Person("Lex")
# p3 = Person("Betty", "White")
# print(p1.full_name())
# print(p2.full_name())
# print(p3.full_name())