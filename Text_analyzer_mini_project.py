#Project: Text Analyzer
# Create a Python program that:

# Takes a sentence as input from the user, 
# then prints a full analysis of that sentence showing — 
# its total length,
# its first and last character,
# its first 10 characters, 
# a capitalized version of it, 
# how many times the letter "a" appears, 
# the position of the word "python" (or -1 if not found),
# whether it ends with a full stop,
# and a version where every space is replaced with an underscore.

# All results should be printed clearly with labels so the output is easy to read.

# Takes a sentence as input from the user, 
sen = input("Enter your sentence:")
# then prints a full analysis of that sentence showing
print("Sentence",sen)
# its total length
print("Length of a sentence is:",len(sen))

# its first and last character
print("First Character",sen[0])
print("Last Character",sen[-1])

# its first 10 characters
print("First 10 characters",sen[0:10])

# a capitalized version of it
print("Capitalize",sen.capitalize())

# how many times the letter "a" appears
print("Count Letter a",sen.count("a"))

# the position of the word "python" (or -1 if not found)
print("Position of word python",sen.find("python"))


# whether it ends with a full stop

print("Check ending",sen.endswith("."))

# and a version where every space is replaced with an underscore.
print("Replace word",sen.replace(" ", "_"))