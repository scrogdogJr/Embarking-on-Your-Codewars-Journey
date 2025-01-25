#Solution: Even or Odd

def even_or_odd(number):
    
    if (number % 2) == 0:
        return "Even"
    
    else:
        return "Odd"

#Solution: Convert a number to a string

def number_to_string(num):
    num = str(num)
    
    return num

def get_count(sentence):
    count = 0
    for char in sentence:
        if (sentence[char] == "a") or (sentence[char] == "e") or (sentence[char] == "i") or (sentence[char] == "o") or (sentence[char] == "u"):
            count += 1

    return count;