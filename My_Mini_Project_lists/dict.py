# A list of dictionaries to store fact-checking responses (from your Canvas)
fact_checker_data = [
    {
        "keywords": ["sky", "blue"],
        "verdict": "Likely True",
        "justification": "The sky appears blue due to Rayleigh scattering.",
        "confidence": 95,
        "icon": "✔",
        "colors": {"bg": "green", "text": "darkgreen", "bar": "green"}
    },
    {
        "keywords": ["moon", "cheese"],
        "verdict": "Likely False",
        "justification": "The moon is made of rock and dust, not cheese.",
        "confidence": 99,
        "icon": "❌",
        "colors": {"bg": "red", "text": "darkred", "bar": "red"}
    },
    {
        "keywords": ["cats", "better", "dogs"],
        "verdict": "Cannot Verify",
        "justification": "This is a subjective opinion and cannot be fact-checked.",
        "confidence": 0,
        "icon": "❓",
        "colors": {"bg": "gray", "text": "darkgray", "bar": "gray"}
    },
    # Science Facts
    {
        "keywords": ["earth", "round"],
        "verdict": "Likely True",
        "justification": "Earth is an oblate spheroid, confirmed by satellite imagery and scientific measurements.",
        "confidence": 99,
        "icon": "✔",
        "colors": {"bg": "green", "text": "darkgreen", "bar": "green"}
    },
    {
        "keywords": ["earth", "flat"],
        "verdict": "Likely False",
        "justification": "Extensive scientific evidence proves Earth is spherical, not flat.",
        "confidence": 99,
        "icon": "❌",
        "colors": {"bg": "red", "text": "darkred", "bar": "red"}
    },
    {
        "keywords": ["water", "boil", "100", "celsius"],
        "verdict": "Likely True",
        "justification": "Water boils at 100°C (212°F) at sea level under standard atmospheric pressure.",
        "confidence": 95,
        "icon": "✔",
        "colors": {"bg": "green", "text": "darkgreen", "bar": "green"}
    },
    {
        "keywords": ["dinosaurs", "extinct", "65", "million"],
        "verdict": "Likely True",
        "justification": "Non-avian dinosaurs went extinct approximately 65 million years ago due to a mass extinction event.",
        "confidence": 95,
        "icon": "✔",
        "colors": {"bg": "green", "text": "darkgreen", "bar": "green"}
    },
    # Technology Facts
    {
        "keywords": ["iphone", "first", "2007"],
        "verdict": "Likely True",
        "justification": "The first iPhone was released by Apple in 2007, revolutionizing the smartphone industry.",
        "confidence": 98,
        "icon": "✔",
        "colors": {"bg": "green", "text": "darkgreen", "bar": "green"}
    },
    {
        "keywords": ["internet", "invented", "al", "gore"],
        "verdict": "Likely False",
        "justification": "Al Gore did not invent the internet. It was developed by many researchers and organizations over decades.",
        "confidence": 95,
        "icon": "❌",
        "colors": {"bg": "red", "text": "darkred", "bar": "red"}
    },
    # Health Facts
    {
        "keywords": ["vaccines", "autism"],
        "verdict": "Likely False",
        "justification": "Multiple large-scale studies have found no link between vaccines and autism. The original study claiming this link has been debunked.",
        "confidence": 98,
        "icon": "❌",
        "colors": {"bg": "red", "text": "darkred", "bar": "red"}
    },
    {
        "keywords": ["vitamin", "c", "cold"],
        "verdict": "Cannot Verify",
        "justification": "Research on vitamin C and cold prevention shows mixed results. Some studies suggest it may reduce duration but not prevent colds.",
        "confidence": 40,
        "icon": "❓",
        "colors": {"bg": "gray", "text": "darkgray", "bar": "gray"}
    },
    # History Facts
    {
        "keywords": ["columbus", "discovered", "america"],
        "verdict": "Likely False",
        "justification": "Columbus did not discover America. Indigenous peoples lived there for thousands of years, and Vikings reached North America earlier.",
        "confidence": 95,
        "icon": "❌",
        "colors": {"bg": "red", "text": "darkred", "bar": "red"}
    },
    {
        "keywords": ["world", "war", "2", "1945"],
        "verdict": "Likely True",
        "justification": "World War II ended in 1945 with the surrender of Germany in May and Japan in September.",
        "confidence": 99,
        "icon": "✔",
        "colors": {"bg": "green", "text": "darkgreen", "bar": "green"}
    },
    # Space Facts
    {
        "keywords": ["sun", "star"],
        "verdict": "Likely True",
        "justification": "The Sun is a G-type main-sequence star (yellow dwarf) that provides light and energy to our solar system.",
        "confidence": 99,
        "icon": "✔",
        "colors": {"bg": "green", "text": "darkgreen", "bar": "green"}
    },
    {
        "keywords": ["mars", "red", "planet"],
        "verdict": "Likely True",
        "justification": "Mars is called the Red Planet due to iron oxide (rust) on its surface, giving it a reddish appearance.",
        "confidence": 98,
        "icon": "✔",
        "colors": {"bg": "green", "text": "darkgreen", "bar": "green"}
    },
    # Common Misconceptions
    {
        "keywords": ["humans", "use", "10", "percent", "brain"],
        "verdict": "Likely False",
        "justification": "Humans use 100% of their brain. The 10% myth is a persistent misconception with no scientific basis.",
        "confidence": 98,
        "icon": "❌",
        "colors": {"bg": "red", "text": "darkred", "bar": "red"}
    },
    {
        "keywords": ["carrots", "improve", "eyesight"],
        "verdict": "Cannot Verify",
        "justification": "While carrots contain vitamin A which is important for eye health, they don't significantly improve eyesight beyond normal levels.",
        "confidence": 60,
        "icon": "❓",
        "colors": {"bg": "gray", "text": "darkgray", "bar": "gray"}
    },
    # Environmental Facts
    {
        "keywords": ["climate", "change", "real"],
        "verdict": "Likely True",
        "justification": "Overwhelming scientific consensus confirms that climate change is real and primarily caused by human activities.",
        "confidence": 97,
        "icon": "✔",
        "colors": {"bg": "green", "text": "darkgreen", "bar": "green"}
    },
    {
        "keywords": ["plastic", "decompose", "years"],
        "verdict": "Likely True",
        "justification": "Most plastics take hundreds to thousands of years to decompose, making them a significant environmental concern.",
        "confidence": 95,
        "icon": "✔",
        "colors": {"bg": "green", "text": "darkgreen", "bar": "green"}
    }
]

# This is a 'default' response if no specific keywords are matched
default_response = {
    "verdict": "Uncertain",
    "justification": "The provided statement is either too complex, ambiguous, or falls outside my current knowledge base for a confident assessment.",
    "confidence": 30,
    "icon": "🤔",
    "colors": {"bg": "yellow", "text": "darkorange", "bar": "orange"}
}

def check_claim(user_claim: str) -> dict:
    """
    Simulates checking a user's claim against the fact_checker_data.
    This enhanced version prioritizes matches based on the number of keywords found.

    Args:
        user_claim (str): The statement provided by the user.

    Returns:
        dict: The best matching fact-check dictionary, or a default 'Uncertain' response.
    """
    # Normalize the input for matching
    processed_claim = user_claim.lower().strip()
    
    best_match = None
    max_matches = 0

    # Iterate through the predefined fact-check data to find the best match
    for fact in fact_checker_data:
        current_matches = 0
        # Count how many of the fact's keywords are present in the user's claim
        for keyword in fact["keywords"]:
            if keyword in processed_claim:
                current_matches += 1
        
        # If this fact has more matches than the current best, update it
        if current_matches > max_matches:
            max_matches = current_matches
            best_match = fact
        # Optional: If multiple facts have the same max_matches, you might add
        # a tie-breaking rule here (e.g., higher confidence, or first encountered)

    # If a match was found (at least one keyword matched)
    if best_match and max_matches > 0:
        return best_match
    
    # If no specific fact is matched based on any keyword, return the default uncertain response
    return default_response

def search_fact_checker(query):
    """
    Search through fact-checker data based on keywords in the query.
    
    Args:
        query (str): The search query to match against keywords
        
    Returns:
        list: Matching fact-checker responses
    """
    query_lower = query.lower()
    matches = []
    
    for response in fact_checker_data:
        for keyword in response["keywords"]:
            if keyword.lower() in query_lower:
                matches.append(response)
                break
    
    return matches

def display_fact_check_results(matches):
    """
    Display fact-check results in a formatted way.
    
    Args:
        matches (list): List of matching fact-checker responses
    """
    if not matches:
        print("No fact-check data found for your query.")
        return
    
    print("\n=== FACT CHECK RESULTS ===")
    for i, match in enumerate(matches, 1):
        print(f"\n{i}. Keywords: {', '.join(match['keywords'])}")
        print(f"   Verdict: {match['icon']} {match['verdict']}")
        print(f"   Confidence: {match['confidence']}%")
        print(f"   Justification: {match['justification']}")

# --- Test Cases ---

def run_test_cases():
    """Run the test cases to demonstrate the fact-checker functionality"""
    print("--- Running Test Cases ---")

    # Test Case 1: A "Likely True" claim (all keywords match)
    input_1 = "The sky is blue today."
    output_1 = check_claim(input_1)
    print(f"\nInput: '{input_1}'")
    print(f"Output Verdict: {output_1['verdict']}")
    print(f"Output Justification: {output_1['justification']}")
    print(f"Output Confidence: {output_1['confidence']}%")
    # Expected: Likely True, due to Rayleigh scattering, 95%

    # Test Case 2: A "Likely False" claim (all keywords match)
    input_2 = "Is the moon really made of cheese?"
    output_2 = check_claim(input_2)
    print(f"\nInput: '{input_2}'")
    print(f"Output Verdict: {output_2['verdict']}")
    print(f"Output Justification: {output_2['justification']}")
    print(f"Output Confidence: {output_2['confidence']}%")
    # Expected: Likely False, made of rock and dust, 99%

    # Test Case 3: A "Cannot Verify" (subjective) claim (all keywords match)
    input_3 = "I believe cats are better than dogs."
    output_3 = check_claim(input_3)
    print(f"\nInput: '{input_3}'")
    print(f"Output Verdict: {output_3['verdict']}")
    print(f"Output Justification: {output_3['justification']}")
    print(f"Output Confidence: {output_3['confidence']}%")
    # Expected: Cannot Verify, subjective opinion, 0%

    # Test Case 4: A claim not explicitly in the data (should return default)
    input_4 = "The sun is green."
    output_4 = check_claim(input_4)
    print(f"\nInput: '{input_4}'")
    print(f"Output Verdict: {output_4['verdict']}")
    print(f"Output Justification: {output_4['justification']}")
    print(f"Output Confidence: {output_4['confidence']}%")
    # Expected: Uncertain, complex/ambiguous/outside knowledge, 30%

    # NEW Test Case 5: Partial match - "cats are better" (should still match "cats", "better", "dogs" fact)
    input_5 = "I think cats are better."
    output_5 = check_claim(input_5)
    print(f"\nInput: '{input_5}'")
    print(f"Output Verdict: {output_5['verdict']}")
    print(f"Output Justification: {output_5['justification']}")
    print(f"Output Confidence: {output_5['confidence']}%")
    # Expected: Cannot Verify (because 'cats' and 'better' match, which is 2 keywords, 
    # and this is the highest count for any fact, even if 'dogs' is missing)

    # NEW Test Case 6: Claim with keywords from multiple facts, but one has more
    input_6 = "The blue moon is beautiful."
    output_6 = check_claim(input_6)
    print(f"\nInput: '{input_6}'")
    print(f"Output Verdict: {output_6['verdict']}")
    print(f"Output Justification: {output_6['justification']}")
    print(f"Output Confidence: {output_6['confidence']}%")
    # Expected: Likely True (because 'blue' and 'sky' match for 'sky is blue' fact, 
    # while only 'moon' matches for 'moon is cheese' fact. 'sky' isn't in input, but 'blue' is.
    # So 'sky is blue' fact gets 1 match ('blue'). 'moon is cheese' gets 1 match ('moon').
    # If 'sky' was in the input, 'sky is blue' would get 2 matches.
    # This test case highlights the "best_match" logic.
    # Let's refine this test to make the "best match" clearer.
    # The current logic will return the first fact with the highest number of matches encountered.
    # For "blue moon", it will find 'blue' (1 match for sky/blue) and 'moon' (1 match for moon/cheese).
    # It will return the 'sky/blue' fact as it's encountered first with 1 match.
    # This demonstrates the simple "max_matches" logic.

def interactive_mode():
    """Run the interactive fact-checker mode"""
    print("\n" + "="*50)
    print("INTERACTIVE FACT CHECKER")
    print("="*50)
    
    while True:
        query = input("\nEnter a claim to fact-check (or 'quit' to exit): ")
        if query.lower() == 'quit':
            break
        
        result = check_claim(query)
        print(f"\n=== FACT CHECK RESULT ===")
        print(f"Claim: '{query}'")
        print(f"Verdict: {result['icon']} {result['verdict']}")
        print(f"Confidence: {result['confidence']}%")
        print(f"Justification: {result['justification']}")

if __name__ == "__main__":
    # Run test cases first
    run_test_cases()
    
    # Then run interactive mode
    interactive_mode() 