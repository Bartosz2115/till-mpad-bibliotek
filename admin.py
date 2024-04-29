from member import Member
from book import Book

class Admin:
  def __init__(self, books: list[Book], members: list[Member]) -> None:
    self.books: list[Book] = books
    self.members: list[Member] = members

  def create_member(self) -> None:
    pass

  def read_member(self) -> None:
    pass

  def update_member(self) -> None:
    pass

  def delete_member(self) -> None:
    pass
  
  def create_book(self) -> None:
    pass

  def read_book(self) -> None:
    pass

  def update_book(self) -> None:
    pass

  def delete_book(self) -> None:
    pass