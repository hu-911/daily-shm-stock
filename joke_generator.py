import requests
import json
from typing import Optional

class JokeGenerator:
    """A random joke generator using the JokeAPI external API."""
    
    BASE_URL = "https://official-joke-api.appspot.com/random_joke"
    
    def __init__(self):
        """Initialize the JokeGenerator."""
        self.session = requests.Session()
    
    def get_random_joke(self) -> Optional[dict]:
        """
        Fetch a random joke from the JokeAPI.
        
        Returns:
            dict: A dictionary containing joke data with keys:
                - type: "general" or "knock-knock"
                - setup: The setup of the joke
                - punchline: The punchline of the joke
                - id: Unique joke ID
            None: If the request fails
        """
        try:
            response = self.session.get(self.BASE_URL, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching joke: {e}")
            return None
    
    def print_joke(self) -> None:
        """Fetch and print a joke in a formatted way."""
        joke = self.get_random_joke()
        
        if joke:
            print("\n" + "="*50)
            print("🎭 RANDOM JOKE 🎭")
            print("="*50)
            print(f"\n📖 Setup: {joke.get('setup')}")
            print(f"\n😂 Punchline: {joke.get('punchline')}")
            print(f"\n(Type: {joke.get('type')}, ID: {joke.get('id')})")
            print("\n" + "="*50 + "\n")
        else:
            print("Failed to fetch a joke. Please try again later.")
    
    def get_multiple_jokes(self, count: int = 3) -> list:
        """
        Fetch multiple random jokes.
        
        Args:
            count: Number of jokes to fetch (default: 3)
        
        Returns:
            list: List of joke dictionaries
        """
        jokes = []
        for _ in range(count):
            joke = self.get_random_joke()
            if joke:
                jokes.append(joke)
        return jokes
    
    def print_multiple_jokes(self, count: int = 3) -> None:
        """Fetch and print multiple jokes."""
        jokes = self.get_multiple_jokes(count)
        
        if jokes:
            print(f"\n{'='*50}")
            print(f"🎭 {count} RANDOM JOKES 🎭")
            print(f"{'='*50}\n")
            
            for i, joke in enumerate(jokes, 1):
                print(f"Joke {i}:")
                print(f"  Setup: {joke.get('setup')}")
                print(f"  Punchline: {joke.get('punchline')}")
                print()
            
            print(f"{'='*50}\n")
        else:
            print("Failed to fetch jokes. Please try again later.")


if __name__ == "__main__":
    # Create an instance and get a single joke
    generator = JokeGenerator()
    
    print("Fetching a single random joke...")
    generator.print_joke()
    
    print("\nFetching 3 random jokes...")
    generator.print_multiple_jokes(3)
