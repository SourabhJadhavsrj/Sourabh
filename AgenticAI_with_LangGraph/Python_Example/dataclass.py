from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int

# Creating an instance
book1 = Book("LangGraph", "LangGraph Academy", 193)

# Accessing attributes
print(book1.title)

# Automatic __repr__
print(book1)

