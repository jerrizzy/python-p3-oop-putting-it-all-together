#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand_param, size_param):
        self.size = size_param
        self.brand = brand_param
        self._condition ="New"
    

    def get_size(self):
        return self._size
    
    def set_size(self, new_size):
        if isinstance(new_size, int):
            self._size = new_size
        else:
            print("size must be an integer")
    
    size = property(get_size, set_size)

    def cobble(self):
        print("Your shoe is as good as new!")
        return self._condition

    def get_condition(self):
        return self._condition
    
    condition = property(get_condition)

stan_smith = Shoe("Adidas", 9)