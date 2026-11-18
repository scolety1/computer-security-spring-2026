# Flask Coursework Example

A tutorial-based SQLite blog with registration, login, and create/edit/delete post flows. The foundation is the [Pallets Flask tutorial](https://flask.palletsprojects.com/en/stable/tutorial/), whose credit and [license](LICENSE.txt) remain authoritative. This is a learning example, not an original production security framework.

## Read the code

- [Application factory](flaskr/__init__.py), [database setup](flaskr/db.py), and [schema](flaskr/schema.sql).
- [Authentication](flaskr/auth.py) and [blog routes](flaskr/blog.py).
- [Tests](tests/) covering factory, database, authentication, and post behavior.

## Run locally

With Python 3.11 or later, from the repository root, create and activate a virtual environment, then install the local package:

```sh
python -m pip install '.[test]'
python -m flask --app flaskr init-db
python -m flask --app flaskr run --host 127.0.0.1 --port 5000
```

Database initialization resets the local tutorial database. Use only disposable synthetic data. The development secret is a tutorial placeholder; this setup is not intended for public deployment.

```sh
python -m pytest -q
python -m build --no-isolation
```

Local repair verification, November 18, 2026: the original 24 tests plus two added packaging/CLI regressions pass (26 total) on Python 3.12. The package metadata now references the supplied Markdown README. The CLI regression uses real disposable SQLite tables rather than mocking database initialization. These checks do not certify production security or Windows behavior.

## Contribution and scope

Collected by Spencer Colety. This archive includes coursework, examples, or starter material; the bulk-upload history does not establish sole authorship of individual methods. Preserve source credits and course-sharing restrictions. The November 2026 packaging metadata correction, CLI application-context repair, added regressions, and this documentation update are AI-assisted maintenance, not original hand-coded coursework. Pallets attribution is preserved. The package remains marked `Private :: Do Not Upload`; build artifacts are for local verification, not package-index publication.

