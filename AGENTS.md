## Source

Keep source contents consistent, starting from the first lecture to the last lecture. This means that source files and tests already created should be present in subsequent lectures. They can be enhanced, modified and updated when it makes sense, but then it should clearly be commented why.

Every lesson contains multiple step files (for example `01-build-hello-world.md`).
Each of these step files **must** include detailed, step-by-step instructions on
which files and folders to create, the code to place in each file, and the
reason for it. Apply this approach consistently across all lessons so that
participants can follow along without guessing any implementation details.

Provide inline comments in short example code blocks (like `types_example.py`)
to explain the purpose of each line.


## Tests

For all lessons, implement basic tests in the source/ examples, even when not being a part of the lesson. Tests can be in Python and/or Powershell.

## CI/CD

For all lessons, implement basic CI/CD pipeline (YAML) in the source/ examples for both GitHub and AzureDevOps, even when not being a part of the lesson.

## Azure Functions

For Azure functions, always use Swagger html/templates.

## Folder Layout

Each training lives in its own directory named `Lesson 0X - <topic>`.
Every lesson holds three sub‑folders and there are nine lessons in total:
- `requirements/` – user stories drawn from the personas
- `students/` – starting files for participants
- `source/` – the completed reference solution



```
source/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          ← GH Actions
├── setup-venv.ps1            ← create local venv
├── run.ps1                   ← test then run main
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

## Requirements

When writing or updating files in any `requirements/` folder:
- Focus on how the personas interact with the system and the value they receive.
- Avoid mentioning specific file names or technologies unless essential for the user story.
- Express acceptance criteria in Given/When/Then form and include both a positive and a negative scenario.

## Environment

Use **Python 3.11** for all code and pipelines as shown in Lesson 01.
