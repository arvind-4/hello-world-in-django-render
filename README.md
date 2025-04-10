# Hello World Django app

### 🧰 Requirements

- **Python 3.12**
- [`uv`](https://github.com/astral-sh/uv) (recommended for dependency management) but optional.

### 🚀 Setup Instructions

1.  **Clone the repository**

```bash
mkdir -p ~/Dev/django-project
cd ~/Dev/django-project
git clone https://github.com/arvind-4/hello-world-in-django-render.git .
```

2.  **Create a virtual environment and install dependencies**

```bash
uv venv
uv sync
```

> Alternatively, If you are not using uv, run `pip install -r requirements.txt -r requirements-dev.txt` to install all dependencies at once.

3.  **Run the project**

```bash
uv run python manage.py runserver
```
