"""
Create a new class called Author. Create a regular class, not a dataclass.
An Author has a name, and a list of books published.

When you create a new Author, they don't have any books. 
So create an empty books list attribute in the __init__ method.

Your Author class should have a publish method, 
which takes the title of a book as an argument. 
Add the title of this book to this object's books list.

Add a __str__ method that returns a String with the author's name, 
and the names of all of their book's titles.

Write a main function to test your class, create some example authors, 
and publish some example books.
"""

class Author:
  def __init__(self, name):
    self.name = name
    self.books = []

  def publish(self, title):
    if title in self.books:
      print(f'"{title}" is already in the list.')
    else:
      self.books.append(title)

  def __str__(self):
    book_list = ', '.join(self.books) or 'No books'
    # ^above line is basically:
    # if self.books:
    #   book_list = ', '.join(self.books)
    # else:
    #   book_list = 'No books'
    return f'Name: {self.name:<15} Books: {book_list}'

def main():
  # author with books
  dr_seuss = Author('Dr. Seuss')
  dr_seuss.publish('Cat in the Hat')
  dr_seuss.publish('Cat in the Hat')
  dr_seuss.publish('Green Eggs and Ham')

  # author with no books
  sophanda = Author('Sophanda Long')

  print(dr_seuss)
  print(sophanda)

main()