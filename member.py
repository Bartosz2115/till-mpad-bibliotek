class Member:
  def __init__(self, name: str, m_id: str, contact: str) -> None:
    self.name: str = name
    self.id: str = m_id
    self.contact: str = contact
  
  def borrow_book(self) -> None:
    pass

  def return_book(self) -> None:
    pass