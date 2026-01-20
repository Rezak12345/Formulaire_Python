from dataclasses import dataclass

@dataclass
class Client:
    email: str
    name: str
    phone: str
    adresse: str
    message: str
    produit: str
