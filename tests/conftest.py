import pytest
import json
from tests import app
from core import db as flask_db

@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def h_student_1():
    headers = {
        'X-Principal': json.dumps({
            'student_id': 1,
            'user_id': 1
        })
    }

    return headers


@pytest.fixture
def h_student_2():
    headers = {
        'X-Principal': json.dumps({
            'student_id': 2,
            'user_id': 2
        })
    }

    return headers


@pytest.fixture
def h_teacher_1():
    headers = {
        'X-Principal': json.dumps({
            'teacher_id': 1,
            'user_id': 3
        })
    }

    return headers


@pytest.fixture
def h_teacher_2():
    headers = {
        'X-Principal': json.dumps({
            'teacher_id': 2,
            'user_id': 4
        })
    }

    return headers


@pytest.fixture
def h_principal():
    headers = {
        'X-Principal': json.dumps({
            'principal_id': 1,
            'user_id': 5
        })
    }

    return headers



# as sql test are in side they are unable to access application context so 
@pytest.fixture(scope='module')
def test_client():
    app.testing = True
    testing_client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()

@pytest.fixture(scope='module')
def init_database():
    flask_db.create_all()
    yield flask_db 
    # flask_db.drop_all()
