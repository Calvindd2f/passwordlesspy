# passwordlessbp.py
from flask import Flask
from .apiconfig import PasswordlessApiConfig
from .config import PASSWORDLESS_API_URL, PASSWORDLESS_API_KEY, PASSWORDLESS_API_SECRET

class PasswordlessBlueprint(Blueprint):
    def register_app(self, app: Flask, options: dict=None):
        super().register_app(app, options=options)
        self.api_config = PasswordlessApiConfig(
            url=app.config['PASSWORDLESS_API_URL'],
            key=app.config['PASSWORDLESS_API_KEY'],
            secret=app.config['PASSWORDLESS_API_SECRET']
        )

        # Now, `self.api_config` can be used to setup API clients or other integrations
