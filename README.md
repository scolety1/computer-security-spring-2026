---
title: CSCI 476 Setup
---

# Install `uv`

On Linux/macOS:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On Windows:
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```


Alternatively, follow the instructions on the official `uv` site: [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)

# Run flaskr

In the `flaskr_tutorial` directory, you can use `uv` to initialize the database and run the web app.

## Initialize the database

```
uv run flask --app flaskr init-db
```

## Start the web server

```
uv run flask --app flaskr run --debug --host 127.0.0.1 --port 5000
```

You can now access the app by browsing to http://127.0.0.1:5000
