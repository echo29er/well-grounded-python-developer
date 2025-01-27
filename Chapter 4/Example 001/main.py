from Person import Person

def main(): 
    people = [
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