import os


def pytest_generate_tests(metafunc):
    os.environ["FASTAPI_ROOT_PATH"] = "/api"
