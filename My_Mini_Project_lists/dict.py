# A list of dictionaries to store fact-checking responses
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
    }
]

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

# Example usage functions
def example_access():
    """Example of accessing data"""
    print("Example of accessing data:")
    print(f"First verdict: {fact_checker_data[0]['verdict']}")
    print(f"Second justification: {fact_checker_data[1]['justification']}")

def example_iteration():
    """Example of iterating through data"""
    print("\nExample of iterating through data:")
    for response in fact_checker_data:
        print(f"Keywords: {response['keywords']}, Verdict: {response['verdict']}")

if __name__ == "__main__":
    # Run examples
    example_access()
    example_iteration()
    
    # Interactive search example
    print("\n" + "="*50)
    print("INTERACTIVE FACT CHECKER")
    print("="*50)
    
    while True:
        query = input("\nEnter a search query (or 'quit' to exit): ")
        if query.lower() == 'quit':
            break
        
        matches = search_fact_checker(query)
        display_fact_check_results(matches) 