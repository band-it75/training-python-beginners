
## Tests

For all lessions, implement basic tests in the source/ examples, even when not being a part of the lession. Tests can be in Python and/or Powershell. 

## CI/CD

For all lessions, implement basic CI/CD pipeline (YAML) in the source/ examples for both GitHub and AzureDevOps, even when not being a part of the lession.

## Folder Layout

Each training lives in its own directory named `Lession 0X - <topic>`.
Every lesson holds three sub‑folders and there are nine lessons in total:
- `requirements/` – user stories drawn from the personas
- `students/` – starting files for participants
- `source/` – the completed reference solution



```
source/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          ← GH Actions
├── app.py                     ← Flask API
├── auth.py                    ← JWT helpers
├── function_app.py            ← Azure Functions wrapper
├── host.json                  ← auto‑generated
├── local.settings.json        ← auto‑generated
├── main.py                    ← entry point
├── models.py                  ← domain model
├── requirements.txt           ← grows each step
├── tests/                     ← pytest test‑suite
└── utils.py                   ← helpers + @timed
```