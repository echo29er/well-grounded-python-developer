"""
Class Purpose: 
    This class constructs Person objects.

    Attributes:
        fname (str): the first name of the person
        mname (str): the middle name of the person, which defaults to None. 
        lname (str): the last name of the person, which defaults to None.

    Instance methods: 
        full_name:
            Function purpose: 
                Given a instance of the Person class, a full_name variable is constructed according to the Person's attributes. 

            Args: 
                self: the instance of the Person class

            Returns: 
                full_name (str)    

"""

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