# Data for testing CREATE
user_add = [
    ('{"id":0, "name":"test_for_add2","email":"test_for_add2@email.com","gender":"male","status":"active"}', 201),
    ('{"id":0, "name":"test_for_add2","email":"test_for_add2@email.com","gender":"male","status":"active"}', 422),
]
user_add_ids = [f"Create user [Data: {item[0]}], expected code={item[1]}" for item in user_add]

# Data for testing DELETE
user_delete = [
    (26, 204), (26, 404),
    (56, 204), (56, 404),
]
user_delete_ids = [f"Delete user {item[0]}], expected code={item[1]}" for item in user_delete]

# Data for Update
user_update = [
    (5664, '{"id":5664,"name":"user9910new2","email":"test_for_add22@email.com","gender":"male","status":"active"}', 204),
]
user_update_ids = [f"Update user {item[0]}], expected code={item[2]}" for item in user_update]
