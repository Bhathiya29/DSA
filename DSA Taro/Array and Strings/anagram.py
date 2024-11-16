def is_anagram(s1,s2):
    return char_count(s1) == char_count(s2)


#helper function
def char_count(s):
    count ={}

    for char in s:
        if char not in count:
            count[char]=0
        
        count[char]+=1

    return count


#print(char_count('catss'))
print(is_anagram('catss','tssca'))