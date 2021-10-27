from alchemize import JsonTransmuter
from pytest import mark

from gorest.api.api_response import ApiResponseType
from gorest.domain.user import User


class TestUserApi:

    @mark.order(1)
    def test_user_create(self, api, logger, dp_user_add):
        _user = JsonTransmuter.transmute_from(dp_user_add[0], User)
        logger.info(f"Test case for adding user with ID={_user.user_id}")
        response = api.create_user(_user)
        assert response.code == dp_user_add[1]
        logger.info(f"User with ID={response.message.user_id} was created.")
        logger.info("Test PASSED")

    @mark.order(6)
    @mark.skip
    def test_user_update(self, api, logger, dp_user_update):
        _user = JsonTransmuter.transmute_from(dp_user_update[1], User)
        logger.info(f"Test case for updating user with name={dp_user_update[0]}")
        response = api.user_update(dp_user_update[0], _user)
        assert response.code == dp_user_update[2]
        logger.info(f"User {dp_user_update[0]} was updated")
        logger.info("Test PASSED")

    @mark.order(7)
    def test_user_delete(self, api, logger, dp_user_delete):
        logger.info(f"Test case for deleting user {dp_user_delete[0]}")
        response = api.delete_user(dp_user_delete[0])
        assert response.code == dp_user_delete[1]
        logger.info(f'User {dp_user_delete[0]} was deleted')
        response = api.get_user(dp_user_delete[0])
        assert response.code == 404
        assert response.type == ApiResponseType.error
        logger.info("Test PASSED")


if __name__ == "__main__":
    pass
