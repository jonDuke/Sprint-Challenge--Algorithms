'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Base case: word is length 1 or 0
    if len(word) <= 1:
        return 0
    
    # Recursive case: check first two letters
    if word[:2] == "th":
        # th was found, add it and move forward 2 characters
        return 1 + count_th(word[2:])
    else:
        # no th was found, move forward 1 character
        return count_th(word[1:])
