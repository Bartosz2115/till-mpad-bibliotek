class Book:
  def __init__(self, name: str, b_id: str, author: str) -> None:
    self.name: str = name
    self.id: str = b_id
    self.author: str = author

  def borrow(self) -> None:
    pass

  def return_book(self) -> None:
    pass