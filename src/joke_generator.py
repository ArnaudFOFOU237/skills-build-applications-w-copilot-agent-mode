"""Random joke generator using the JokeAPI."""

from src.api_client import APIClient
from typing import Dict, Any, Optional
import random


class JokeGenerator:
    """Generate random jokes to keep users motivated."""

    JOKE_API_URL = "https://v2.jokeapi.dev"
    
    # Joke types
    JOKE_TYPE_GENERAL = "general"
    JOKE_TYPE_PROGRAMMING = "programming"
    JOKE_TYPE_KNOCK_KNOCK = "knock-knock"

    def __init__(self):
        """Initialize the joke generator with API client."""
        self.client = APIClient(base_url=self.JOKE_API_URL)

    def get_random_joke(self, joke_type: str = "Any") -> Optional[Dict[str, Any]]:
        """Get a random joke from the JokeAPI.
        
        Args:
            joke_type: Type of joke ("general", "programming", "knock-knock", or "Any")
            
        Returns:
            Dictionary containing joke data or None if failed
        """
        try:
            params = {
                "type": "single",
                "format": "json"
            }
            
            if joke_type != "Any":
                params["category"] = joke_type
            
            response = self.client.get("/joke/Any", params=params)
            return response
        except Exception as e:
            print(f"Error fetching joke: {e}")
            return None

    def print_joke(self, joke_data: Dict[str, Any]) -> None:
        """Print a joke in a formatted way.
        
        Args:
            joke_data: Dictionary containing joke data from API
        """
        if not joke_data:
            print("No joke available.")
            return
        
        if joke_data.get("type") == "single":
            print(f"\n😄 {joke_data.get('joke')}\n")
        elif joke_data.get("type") == "twopart":
            print(f"\n😄 {joke_data.get('setup')}")
            print(f"\n😂 {joke_data.get('delivery')}\n")

    def get_motivational_joke(self) -> Optional[Dict[str, Any]]:
        """Get a programming joke for motivation during workouts.
        
        Returns:
            Dictionary containing joke data or None if failed
        """
        return self.get_random_joke(joke_type="programming")

    def get_multiple_jokes(self, count: int = 3) -> list:
        """Get multiple random jokes.
        
        Args:
            count: Number of jokes to fetch
            
        Returns:
            List of joke dictionaries
        """
        jokes = []
        for _ in range(count):
            joke = self.get_random_joke()
            if joke:
                jokes.append(joke)
        return jokes

    def close(self):
        """Close the API client."""
        self.client.close()
