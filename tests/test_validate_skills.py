import os
import subprocess
import shutil
import pytest

@pytest.fixture
def dummy_skill_dir():
    # Setup
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    skills_dir = os.path.join(root_dir, 'skills')
    dummy_name = 'dummy_test_skill_missing_md'
    dummy_dir = os.path.join(skills_dir, dummy_name)
    os.makedirs(dummy_dir, exist_ok=True)

    yield dummy_name

    # Teardown
    if os.path.exists(dummy_dir):
        shutil.rmtree(dummy_dir)

def test_validate_skills_missing_md(dummy_skill_dir):
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    script_path = os.path.join(root_dir, 'scripts', 'validate-skills.sh')

    result = subprocess.run([script_path], capture_output=True, text=True)

    assert result.returncode == 1

    expected_error = f"ERROR: {dummy_skill_dir} — missing SKILL.md"
    assert expected_error in result.stdout
