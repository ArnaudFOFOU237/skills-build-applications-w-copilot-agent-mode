"""Generic API client for making HTTP requests with retry logic."""

import requests
from typing import Dict, Any, Optional
import time


class APIClient:
    """A generic API client with retry logic and error handling."""

    def __init__(self, base_url: str = "", timeout: int = 10, max_retries: int = 3):
        """Initialize the API client.
        
        Args:
            base_url: Base URL for API requests
            timeout: Request timeout in seconds
            max_retries: Maximum number of retry attempts
        """
        self.base_url = base_url
        self.timeout = timeout
        self.max_retries = max_retries
        self.session = requests.Session()

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a GET request to the API.
        
        Args:
            endpoint: API endpoint path
            params: Query parameters
            
        Returns:
            Response JSON as dictionary
            
        Raises:
            requests.RequestException: If the request fails
        """
        url = f"{self.base_url}{endpoint}"
        
        for attempt in range(self.max_retries):
            try:
                response = self.session.get(
                    url,
                    params=params,
                    timeout=self.timeout
                )
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                if attempt == self.max_retries - 1:
                    raise
                time.sleep(2 ** attempt)  # Exponential backoff

    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a POST request to the API.
        
        Args:
            endpoint: API endpoint path
            data: Request body data
            
        Returns:
            Response JSON as dictionary
            
        Raises:
            requests.RequestException: If the request fails
        """
        url = f"{self.base_url}{endpoint}"
        
        for attempt in range(self.max_retries):
            try:
                response = self.session.post(
                    url,
                    json=data,
                    timeout=self.timeout
                )
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                if attempt == self.max_retries - 1:
                    raise
                time.sleep(2 ** attempt)  # Exponential backoff

    def close(self):
        """Close the session."""
        self.session.close()
