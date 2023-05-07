"""
    Class object to hold thing properties.
"""


from typing import Dict


class ThingProperties:
    """
    Class object to hold thing properties.
    """

    def __init__(self) -> None:
        self.thing_name: str = ""
        self.endpoint: str = ""
        self.cert_pem: str = ""
        self.private_key_pem: str = ""
        self.public_key_pem: str = ""

    def to_dict(self) -> Dict[str, str]:
        """
        convert the properties as dictionary to jsonify
        """
        return {
            "thing_name": self.thing_name,
            "endpoint": self.endpoint,
            "cert_pem": self.cert_pem,
            "private_key_pem": self.private_key_pem,
            "public_key_pem": self.public_key_pem,
        }
