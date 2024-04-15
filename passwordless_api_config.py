import os
from dataclasses import dataclass, field

@dataclass
class PasswordlessApiConfig:
    url: str = field(default_factory=lambda: os.getenv('PASSWORDLESS_API_URL', 'https://v4.passwordless.dev'))
    key: str = field(default_factory=lambda: os.getenv('PASSWORDLESS_API_KEY'))
    secret: str = field(default_factory=lambda: os.getenv('PASSWORDLESS_API_SECRET'))

    def __post_init__(self):
        if not all([self.url, self.key, self.secret]):
            raise ValueError("All API config values must be provided: URL, Key, and Secret")

        # Optionally, you can add more complex validation or transformation logic here

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        if not value:
            raise ValueError("API Key cannot be empty")
        self._key = value

    @property
    def secret(self):
        return self._secret

    @secret.setter
    def secret(self, value):
        if not value:
            raise ValueError("API Secret cannot be empty")
        self._secret = value

# Example usage:
try:
    config = PasswordlessApiConfig()
    print("API Config loaded successfully.")
except ValueError as e:
    print(f"Error loading API Config: {e}")
