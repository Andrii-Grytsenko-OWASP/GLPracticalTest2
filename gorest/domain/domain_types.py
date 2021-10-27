from enum import Enum


class Gender(Enum):
    male = "male"
    female = "female"


class UserStatus(Enum):
    active = "active"
    blocked = "blocked"
    deleted = "deleted"

