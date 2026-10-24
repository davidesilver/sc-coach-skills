import subprocess
import pytest
import os

SCRIPT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts", "validate-skills.sh"))

def run_is_known_skill(skill_names: list[str], test_skill: str) -> bool:
    """
    Helper function to test is_known_skill from the bash script.
    It overrides SKILL_NAMES with the provided list.
    """
    skill_names_bash = " ".join([f'"{name}"' for name in skill_names])

    # We create a wrapper script that sources the target script,
    # re-assigns the SKILL_NAMES array, and then calls is_known_skill.
    wrapper = f'''
source "{SCRIPT_PATH}"
SKILL_NAMES=({skill_names_bash})
is_known_skill "{test_skill}"
'''
    result = subprocess.run(
        ["bash", "-c", wrapper],
        capture_output=True,
        text=True
    )
    return result.returncode == 0

def test_is_known_skill_exists():
    """Test that a skill that exists in the array returns success (0)."""
    assert run_is_known_skill(["skill-a", "skill-b"], "skill-a") is True
    assert run_is_known_skill(["skill-a", "skill-b"], "skill-b") is True

def test_is_known_skill_missing():
    """Test that a skill that does not exist in the array returns failure (1)."""
    assert run_is_known_skill(["skill-a", "skill-b"], "skill-c") is False

def test_is_known_skill_empty_list():
    """Test that any skill searched in an empty list returns failure (1)."""
    assert run_is_known_skill([], "skill-a") is False

def test_is_known_skill_substring():
    """Test that substring matches are not considered valid matches."""
    # "skill" is a substring of "skill-a", but shouldn't match exactly
    assert run_is_known_skill(["skill-a"], "skill") is False
    assert run_is_known_skill(["skill-a"], "kill-a") is False
    assert run_is_known_skill(["a", "b"], "ab") is False

def test_is_known_skill_with_spaces():
    """Test matching when skill names have spaces (edge case)."""
    assert run_is_known_skill(["my skill", "other skill"], "my skill") is True
    assert run_is_known_skill(["my skill", "other skill"], "skill") is False
