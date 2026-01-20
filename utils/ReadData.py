import json
from models.Client import Client

class ReadData:
    def __init__(self):
        self.file_name = "/data/DataClients.json"

    def read_data_from_json(self, client_key: str) -> Client | None:
        with open(self.file_name, "r", encoding="utf-8") as file:
            data = json.load(file)

        if client_key in data:
            c = data[client_key]
            return Client(
                email=c["email"],
                name=c["name"],
                phone=c["phone"],
                adresse=c["adresse"],
                message=c["message"],
                produit=c["produit"]
            )
        return None
