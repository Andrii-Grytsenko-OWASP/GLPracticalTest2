from alchemize import Attr

from gorest.domain.base_api_class import BaseApiClass
from gorest.domain.domain_types import UserStatus, Gender


class User(BaseApiClass):
    __mapping__ = {
        "id": Attr("user_id", int),
        "name": Attr("user_name", str),
        "email": Attr("email", str),
        "gender": Attr("gender", str),
        "status": Attr("user_status", str),
    }

    db = None  # database.Database()

    def __init__(self, user_id: int = None, user_name: str = None, email: str = None,
                 gender: str = None, user_status: str = None):
        self.user_id = user_id
        self.user_name = user_name
        self.email = email
        self.gender = gender
        self.user_status = user_status

    def to_json(self):
        return {"id": self.id, "username": self.user_name,
                "firstName": self.first_name, "lastName": self.last_name,
                "email": self.email, "password": self.password,
                "phone": self.phone, "status": self.user_status.value}

    @staticmethod
    def from_json(json: str):
        if "id" in json and "username" in json \
                and "firstName" in json and "lastName" in json \
                and "email" in json and "password" in json \
                and "phone" in json and "status" in json:
            return User(json["id"], json["username"], json["firstName"],
                        json["lastName"], json["email"], json["password"],
                        json["phone"], UserStatus(json["status"]))
        else:
            return None
