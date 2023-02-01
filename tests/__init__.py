import os
from pathlib import Path

CONFIG_FILE_PATH = Path(__file__).parents[1] / "config" / "config_test.py"
assert os.path.exists(CONFIG_FILE_PATH)

os.environ["PYTHON_REST_API_CONFIG_FILE"] = str(CONFIG_FILE_PATH)
