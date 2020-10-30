class TooManyPagesReadError(ValueError):
    pass

class Book:
    def __init__(self,name : str,page_count: int):
        self.name=name
        self.page_count=page_count
        self.page_reads=0
    
    def __repr__(self):
        return (
            f"(Book {self.name} , read {self.page_reads} pages out of {self.page_count})"
        )
    
    def read(self,pages: int):
        if self.page_reads+pages>self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {self.page_reads+pages} pages, but this book only has {self.page_count} pages."
            )
        self.page_reads+=pages
        print(f"You have now read {self.page_reads} pages out of {self.page_count}")
    
python101=Book("Python101",50)

try:
    python101.read(35)
    python101.read(50)
except TooManyPagesReadError as e:
    print(e)