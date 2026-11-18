"""AI-assisted packaging regressions added after the original coursework."""

from pathlib import Path
import subprocess
import sys
import zipfile


def test_build_wheel_contains_readme_and_runtime_assets(tmp_path):
    root = Path(__file__).resolve().parents[1]
    built = subprocess.run(
        [sys.executable, "-m", "build", "--wheel", "--no-isolation", "--outdir", str(tmp_path)],
        cwd=root, capture_output=True, text=True, timeout=30,
    )
    assert built.returncode == 0, built.stdout + built.stderr
    wheel, = tmp_path.glob("*.whl")
    with zipfile.ZipFile(wheel) as archive:
        metadata_path, = [name for name in archive.namelist() if name.endswith(".dist-info/METADATA")]
        metadata = archive.read(metadata_path).decode()
        assert "Description-Content-Type: text/markdown" in metadata
        assert "# Flask Coursework Example" in metadata
        assert "Private :: Do Not Upload" in metadata
        assert "flaskr/schema.sql" in archive.namelist()
        assert "flaskr/templates/auth/login.html" in archive.namelist()
