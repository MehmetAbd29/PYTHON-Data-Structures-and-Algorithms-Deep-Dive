# Problem
# Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

# For example:

# "public relations" is an anagram of "crap built on lies."

# "clint eastwood" is an anagram of "old west action"

# Steps:

# to compare two strings, we usually have to iterate through them. This means O(N) in most cases, as well'll iterate through all elements eventually.

# there are two ways to solve this problem. File _one.py will solve it using a dic counter, while file _two.py will sovle it comparing two sorted strings



from nose.tools import assert_equal

def anagram(s1, s2):
    s1_new = s1.lower()
    s2_new= s2.lower()
    
    marks = [",", " ", ":", ";", ".", "?", "!"] # you can add more
    
    for char in s1:
        #replace weird characters
        if char in marks:
            s1_new = s1_new.replace(char, "")
            
    for char in s2:
        if char in marks:
            s2_new = s2_new.replace(char, "")
            

    return sorted(s1_new) == (s2_new)


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
