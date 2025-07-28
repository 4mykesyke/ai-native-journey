# This is the classic "Hello, World!" message.
# When the script runs, this line will be printed first.
print("Hello, World!")

# --- Now, let's make the greeting personalized! ---

# The 'input()' function is used to ask the user a question.
# The text inside the parentheses is the question that will be shown to the user.
# Whatever the user types and then presses Enter will be stored
# in the 'user_name' variable.
user_name = input("What's your name? ")

# The 'print()' function is used again to display a message.
# We are using an f-string (notice the 'f' before the first quote).
# An f-string allows us to easily include the value of a variable directly
# inside the text by putting the variable's name inside curly braces {}.
# So, if 'user_name' is "Mike", this line will print "Hello, Mike! It's great to meet you on your AI journey!"
print(f"Hello, {user_name}! It's great to meet you on your AI journey!")