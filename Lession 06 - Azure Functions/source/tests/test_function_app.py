import os
import sys
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import azure.functions as func
from function_app import main
from app import tasks


def test_function_app_list_tasks():
    tasks.clear()
    req = func.HttpRequest(
        method="GET",
        url="http://localhost/tasks",
        headers={},
        params=None,
        body=b"",
    )
    resp = main(req, context=None)
    assert resp.status_code == 200
    assert json.loads(resp.get_body()) == []

