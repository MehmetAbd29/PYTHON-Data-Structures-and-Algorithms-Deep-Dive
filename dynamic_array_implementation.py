# Code snippet to explain how the dynamic Array works in python
# For further question, contact me at www.Mehmetdevelopment.com OR https://www.linkedin.com/in/mt1996/

# How to create a dynamic array in python? The key is to provide means to grow the array A that stores the elements of a list. We can’t actually grow the array; its capacity is fixed. If an element is appended to a list at a time when the array is full, we’ll do the following:
# 	1. Allocate a new array B with a larger capacity 
# 	2. Set B[i] = A[i], for I = 0,….., n-1  (n: number of items, but we start counting from zero)
# 	3. Set A = B, hence we got rid of the old A, and inserted a new B.
# 	4. We’ll insert the new element inside the new array (A)
# 	But how large should the array be? A common rule is to have twice the capacity.

import ctypes

class DynamicArray(object):
    '''
    Dynamic Array class, i.e in python it's called a LIST :)
    This is just to show how it works under the hood. 
    '''

    def __init__(self): # let's define the attributes
        self.n = 0 # count the elements. Default is zero, nothing.
        self.capacity = 1 # default capacity, (can accept one element by default) 
        self.A = self.make_array(self.capacity)

    def __len__(self):
        '''
        Returns the #of elements in the array
        '''
        return self.n

    def __getitem__(self,k):
        '''
        returns an element at index k
        '''
        if not (0 <= k < self.n):  # btw, this is not a good coding line. You should use and,or,not. But you get the idea :)
            return IndexError('K is out of bound')

        return self.A[k]
    
    def append(self,element):

        if self.n == self.capacity:  # can happen if the array is full, [1]: n=1, capacity = 1
            # we need to double the capacity
            self._resize(2*self.capacity)
        
        self.A[self.n] = element
        self.n += 1

    def _resize(self, new_capacity):

        B = self.make_array(new_capacity)
        
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.capacity = new_capacity

    def make_array(self, new_cap):
        return(new_cap * ctypes.py_object)()
        

#let's try it :)
# you can run the code in the terminal: $python python_file_name.py
# or copy this code in Jypter Notebook
A = DynamicArray()
print(len(A))
A.append(5)
print(len(A))
