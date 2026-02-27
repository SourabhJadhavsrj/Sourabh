from typing import TypedDict

# Define a TypedDict for representing a person's information
class Person(TypedDict):
    name: str
    age: int
    email: str

# Create an instance of the TypedDict
person_info: Person = {
    'name': 'Alice',
    'age': 30,
    #'email': 'alice@example.com'
}

# Accessing values
print(person_info['name'])  
print(person_info['age'])   
#print(person_info['email']) 

print("\n--- Printing the entire dictionary ---")
print(person_info)