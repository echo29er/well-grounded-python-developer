from Person import Person
from typing import List
"""
Program Purpose: 
    This program creates a list of four instances of the Person class. 
    It then prints out each person according to what is by the instance method full_name().
"""

def main() -> None: 
    people: List[Person] = [
        Person("John", "George", "Smith"), 
        Person("Bill", lname = "Thompson"),
        Person("Sam", mname = "Watson"),
        Person("Tom"),
    ]

    # Print out the full names of the people 
    for person in people: 
        print(person.full_name())

if __name__ == "__main__":
    main()