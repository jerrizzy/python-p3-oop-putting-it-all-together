#!/usr/bin/env python3

class Book:
    def __init__(self, title_param, page_count_param):
        self.title = title_param
        self.page_count = page_count_param

    def get_title(self):
        return self.title

    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self, new_page_count):
        if isinstance(new_page_count, int):
            self._page_count = new_page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        
        print("Flipping the page...wow, you read fast!")


    page_count = property (get_page_count, set_page_count)

my_book = Book("And Then There Were None", 334)

print(my_book.page_count, my_book.title)

    
        