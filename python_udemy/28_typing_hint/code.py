class Book:
    TYPES=["hardcover","papercover"]

    def __init__(self,name: str,book_type: str,weight: int):
        self.name=name
        self.book_type=book_type
        self.weight=weight
    
    def __repr__(self)-> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}>"

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name,cls.TYPES[0],page_weight+100)
    
    @classmethod
    def paperbook(cls,name: str, page_weight: int) -> "Book":
        return cls(name,cls.TYPES[1],page_weight)