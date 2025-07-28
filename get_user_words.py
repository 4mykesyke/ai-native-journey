def get_user_words():
    """
    Asks the user for a noun, a verb, and an adjective, and returns these three words.

    Returns:
        tuple: A tuple containing the noun, verb, and adjective entered by the user.
    """
    # Prompt the user to enter a noun and store it
    noun = input("Please enter a noun: ")
    
    # Prompt the user to enter a verb and store it
    verb = input("Please enter a verb: ")
    
    # Prompt the user to enter an adjective and store it
    adjective = input("Please enter an adjective: ")
    
    # Return the three words as a tuple
    return noun, verb, adjective

if __name__ == "__main__":
    user_noun, user_verb, user_adjective = get_user_words()
    print(f"\nYou entered: Noun='{user_noun}', Verb='{user_verb}', Adjective='{user_adjective}'") 