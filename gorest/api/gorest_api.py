from alchemize import JsonTransmuter
from requests import *

from gorest.api.api_response import *
from gorest.domain.domain_types import *
from gorest.domain.user import User


class GoRestApi:
    def __init__(self, base_url: str, access_token: str):
        self.base_url = base_url + ("/" if base_url[-1] != "/" else "")
        self.access_token = access_token
        self.headers = {"Accept": "application/json",
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {self.access_token}"}

    def list_users(self) -> ApiResponse:
        response = get(f"{self.base_url}users",
                       headers=self.headers)
        return ApiResponse(
            response.status_code,
            ApiResponseType.ok if response.ok else ApiResponseType.error,
            list(map(lambda x: JsonTransmuter.transmute_from(x, User), response.json()["data"]))
            if response.ok else response.text
        )

    def create_user(self, user_obj: User) -> ApiResponse:
        response = post(f"{self.base_url}users",
                        headers=self.headers,
                        data=JsonTransmuter.transmute_to(user_obj))
        return ApiResponse(
            response.status_code,
            ApiResponseType.ok if response.ok else ApiResponseType.error,
            JsonTransmuter.transmute_from(response.json()["data"], User)
            if response.ok else response.text
        )

    def get_user(self, user_id: int) -> ApiResponse:
        response = post(f"{self.base_url}users/{user_id}",
                        headers=self.headers)
        return ApiResponse(
            response.status_code,
            ApiResponseType.ok if response.ok else ApiResponseType.error,
            JsonTransmuter.transmute_from(response.json["data"], User)
            if response.ok else response.text
        )

    def update_user(self, user_obj: User) -> ApiResponse:
        response = patch(f"{self.base_url}users/{user_obj.user_id}",
                         headers=self.headers,
                         data=JsonTransmuter.transmute_to(user_obj))
        return ApiResponse(
            response.status_code,
            ApiResponseType.ok if response.ok else ApiResponseType.error,
            JsonTransmuter.transmute_from(response.json["data"], User)
            if response.ok else response.text
        )

    def delete_user(self, user_id: int) -> ApiResponse:
        response = delete(f"{self.base_url}users/{user_id}",
                          headers=self.headers)
        return ApiResponse(
            response.status_code,
            ApiResponseType.ok if response.ok else ApiResponseType.error,
            response.text
        )
