"""AI-assisted regression; exercises real SQLite instead of mocking init_db."""
import sqlite3

from flaskr import create_app


def test_init_db_command_creates_database_without_caller_context(tmp_path):
    database = tmp_path / "cli.sqlite"
    app = create_app({"TESTING": True, "DATABASE": str(database)})
    result = app.test_cli_runner().invoke(args=["init-db"])
    assert result.exit_code == 0, repr(result.exception)
    assert "Initialized the database." in result.output
    with sqlite3.connect(database) as connection:
        tables = {row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    assert {"user", "post"} <= tables
