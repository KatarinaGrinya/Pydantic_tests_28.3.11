import pytest
import requests
from pydantic import BaseModel


class AccessTokenRequest(BaseModel):
    access_token: str

class User(BaseModel):
    id: int
    first_name: str
    last_name: str


def test_access_token_needed():
    request = {
        "access_token": "test_token"
    }
    AccessTokenRequest(**request)


def test_users_receives_response():
    response = [
        {"id": 975319, "first_name": "Katarina", "last_name": "Gritskevich"},
        {"id": 246802, "first_name": "Genry", "last_name": "Lettem"}
    ]
    users = [User(**user) for user in response]



def test_access_token_needed():
    request = {}
    with pytest.raises(ValueError):
        AccessTokenRequest(**request)


def test_access_token_format():
    request = {
        "access_token": "invalid_token_format"
    }
    with pytest.raises(ValueError):
        AccessTokenRequest(**request)


def test_users_succeed():
    response = [
        {"id": 975319, "first_name": "Katarina", "last_name": "Gritskevich"},
        {"id": 246802, "first_name": "Genry", "last_name": "Lettem"}
    ]
    users = [User(**user) for user in response]
    assert len(users) == 2
    assert users[0].id == 975319
    assert users[0].first_name == "Katarina"
    assert users[0].last_name == "Gritskevich"


def test_users_don't_get_users():
    response = []
    users = [User(**user) for user in response]
    assert len(users) == 0


def test_user_format():
    user = {
        "id": "invalid_id_format",
        "first_name": "Katarina",
        "last_name": "Gritskevich"
    }
    with pytest.raises(ValueError):
        User(**user)


def test_user_nameformat():
    user = {
        "id": 975319,
        "first_name": "Margo",
        "last_name": "Gritskevich"
    }
    with pytest.raises(ValueError):
        User(**user)


def test_user_lastnameformat():
    user = {
        "id": 975319,
        "first_name": "Katarina",
        "last_name": "Chupris"
    }
    with pytest.raises(ValueError):
        User(**user)


def test_users_get_user():
    response = [{"id": 975319, "first_name": "Katarina", "last_name": Gritskevich"}]
    users = [User(**user) for user in response]
    assert len(users) == 1
    assert users[0].id == 975319
    assert users[0].first_name == "Katarina"
    assert users[0].last_name == "Gritskevich"



def test_users_get_maxusers():
    response = [{"id": i, "first_name": "User", "last_name": str(i)} for i in range(1000)
]
    users = [User(**user) for user in response]
    assert len(users) == 1000
    assert users[-1].id == 999
    assert users[-1].first_name == "User"
    assert users[-1].last_name == "999"


def test_users_get_incorrect_response():
    response = [{"invalid_attr": "value"}]
    with pytest.raises(ValueError):
        users = [User(**user) for user in response]
