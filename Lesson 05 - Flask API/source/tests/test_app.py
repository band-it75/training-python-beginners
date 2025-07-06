import os
import sys
import json
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app import app, tasks


def test_create_and_list_tasks(capsys):
    client = app.test_client()
    tasks.clear()
    response = client.post('/tasks', json={'title': 'open store'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == 'Open Store'
    assert data['done'] is False
    out = capsys.readouterr().out.strip()
    assert 'create_task took' in out

    response = client.get('/tasks')
    assert response.status_code == 200
    assert data in response.get_json()


def test_create_task_bad_request():
    client = app.test_client()
    tasks.clear()
    resp = client.post('/tasks', json={'name': 'missing'})
    assert resp.status_code == 400
    resp = client.post('/tasks', data='nope', content_type='text/plain')
    assert resp.status_code == 400

