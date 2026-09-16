
import sys
import pytest
from pathlib import Path
from utils.driver_setup import get_driver

# Add project root directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

@pytest.fixture
def driver():
    d = get_driver()
    yield d
    d.quit()