from pathlib import Path
import tempfile
from main import is_valid_url, generate_qr_code

def test_is_valid_url_accepts_valid_url():
  assert is_valid_url("https://nicotroia.com") is True

def test_is_valid_url_rejects_invalid_url():
  assert is_valid_url("not-a-url") is False

def test_generate_qr_code_creates_file():
  with tempfile.TemporaryDirectory() as tmpdir:
    output_path = Path(tmpdir) / "test_qr.png"
    generate_qr_code("https://nicotroia.com", output_path)
    assert output_path.exists()
