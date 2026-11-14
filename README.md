# Flask Coursework Example

A tutorial-based SQLite blog with registration, login, and create/edit/delete post flows. The foundation is the [Pallets Flask tutorial](https://flask.palletsprojects.com/en/stable/tutorial/), whose credit and [license](LICENSE.txt) remain authoritative. This is a learning example, not an original production security framework.

## Read the code

- [Application factory](flaskr/__init__.py), [database setup](flaskr/db.py), and [schema](flaskr/schema.sql).
- [Authentication](flaskr/auth.py) and [blog routes](flaskr/blog.py).
- [Tests](tests/) covering factory, database, authentication, and post behavior.

## Run locally

With Python and `uv`, from the repository root:

```sh
uv run --no-project --with flask flask --app flaskr init-db
uv run --no-project --with flask flask --app flaskr run --host 127.0.0.1 --port 5000
```

Database initialization resets the local tutorial database. Use only disposable synthetic data. The development secret is a tutorial placeholder; this setup is not intended for public deployment.

```sh
uv run --no-project --with flask --with pytest python -m pytest -q
```

Verified November 14, 2026: 24 tests passed. `--no-project` avoids the current package metadata's missing `README.rst` reference; packaging is not certified.

## Contribution and scope

Collected by Spencer Colety. This archive includes coursework, examples, or starter material; the bulk-upload history does not establish sole authorship of individual methods. Preserve source credits and course-sharing restrictions. This README update was AI-assisted and does not change the exercise code.
