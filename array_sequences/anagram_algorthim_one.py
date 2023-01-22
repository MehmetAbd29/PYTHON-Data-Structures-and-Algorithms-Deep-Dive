# Problem
# Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

# For example:

# "public relations" is an anagram of "crap built on lies."

# "clint eastwood" is an anagram of "old west action"

# Steps:

# to compare two strings, we usually have to iterate through them. This means O(N) in most cases, as well'll iterate through all elements eventually.

# there are two ways to solve this problem. File _one.py will solve it using a dic counter, while file _two.py will sovle it comparing two sorted lists

from nose.tools import assert_equal

def anagram(s1, s2):
    s1 = s1.lower()
    s2= s2.lower()
    
    dic = {}
    lst = [",", " ", ":", ";", ".", "?", "!"] # you can add more
    
    for char in s1:
        # ignore special characters
        if char in lst:
            continue

        # start adding counts inside the dic for s1    
        if char not in dic.keys():
            dic[char] = 1
        else:
            dic[char] +=1

    #start removing counts, or if there's a new letter return false!
    for char in s2:
        if char in lst:
            continue
        if char not in dic.keys():
            return False  
        else:
            dic[char] -= 1

    #check if all counts are zeros        
    for value in dic.values():
        if value != 0:
            return False 
        
    return True


class AnagramTest(object):
    
    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print("ALL TEST CASES PASSED")

# Run Tests
t = AnagramTest()
t.test(anagram)
