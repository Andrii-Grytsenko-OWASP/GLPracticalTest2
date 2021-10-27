from pytest import *

from gorest.test_datasets.user_data import *


@fixture(params=user_add, ids=user_add_ids)
def dp_user_add(request):
    return request.param


@fixture(params=user_add_list, ids=user_add_list_ids)
def dp_user_add_list(request):
    return request.param


@fixture(params=user_update, ids=user_update_ids)
def dp_user_update(request):
    return request.param

@fixture(params=user_delete, ids=user_delete_ids)
def dp_user_delete(request):
    return request.param

