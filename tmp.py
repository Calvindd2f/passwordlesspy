from passwordless import (
    PasswordlessClient,
    PasswordlessClientBuilder,
    PasswordlessOptions
)


class PasswordlessPythonSdkExample:
    client: PasswordlessClient

    def __init__(self):
        options = PasswordlessOptions("your_api_secret")

        self.client = PasswordlessClientBuilder(options).build()
