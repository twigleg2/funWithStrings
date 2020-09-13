# Input: a single-word String provided by the user
# Output: the first non-repeated character in the string, if it exists
#          OR a message indicating that such a character does not exist.
# Output: the original string, rearranged by the number of characters (ascending), preserving the original order of the characters where possible
# Note: uppercase and lowercase characters are considered equal when counting the number of occurances.
#       Case is preserved when printing the rearranged string
letters = {}

string = input("please enter a string: ")

for c in string:
    if c.lower() in letters:
        letters[c.lower()] += c
    else:
        letters[c.lower()] = c

no_unique_char = True
for c in letters:
    if len(letters[c]) == 1:
        print("The first non-repeated character is", c)
        no_unique_char = False
        break

if no_unique_char:
    print("There are no unique characters in the string provided")

sorted = sorted(letters, key=lambda k: len(letters[k]))

for c in sorted:
    print(letters[c], end='')
print()
