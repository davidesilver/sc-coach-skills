import subprocess
import shutil
import pytest
import os
from pathlib import Path

@pytest.fixture
def mock_env(tmp_path):
    scripts_dir = tmp_path / "scripts"
    skills_dir = tmp_path / "skills"
    scripts_dir.mkdir()
    skills_dir.mkdir()

    script_path = scripts_dir / "validate-skills.sh"

    # Copy the script, but we need to ensure ROOT logic works in the mocked env.
    # The script uses: ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
    # Which will point to the tmp_path because it's run from tmp_path/scripts.
    # So this is perfectly fine.

    shutil.copy("scripts/validate-skills.sh", script_path)
    script_path.chmod(0o755)

    # We need to run the bash script with its PWD as the tmp_path, or just
    # let it use BASH_SOURCE[0] to find the root.
    return tmp_path, script_path, skills_dir

def test_validate_skills_success(mock_env):
    tmp_path, script_path, skills_dir = mock_env

    skill_a = skills_dir / "skill-a"
    skill_a.mkdir()
    (skill_a / "SKILL.md").write_text("---\nname: skill-a\ndescription: A valid skill\n---\n")

    skill_b = skills_dir / "skill-b"
    skill_b.mkdir()
    (skill_b / "SKILL.md").write_text("---\nname: skill-b\ndescription: Another valid skill\n---\nReferences `skill-a`.")

    result = subprocess.run(["bash", str(script_path)], capture_output=True, text=True)
    assert result.returncode == 0
    assert "errors: 0, warnings: 0" in result.stdout

def test_validate_skills_missing_skill_md(mock_env):
    tmp_path, script_path, skills_dir = mock_env

    skill_a = skills_dir / "skill-a"
    skill_a.mkdir()

    result = subprocess.run(["bash", str(script_path)], capture_output=True, text=True)
    assert result.returncode == 1
    assert "ERROR: skill-a — missing SKILL.md" in result.stdout
    assert "errors: 1" in result.stdout

def test_validate_skills_name_mismatch(mock_env):
    tmp_path, script_path, skills_dir = mock_env

    skill_a = skills_dir / "skill-a"
    skill_a.mkdir()
    (skill_a / "SKILL.md").write_text("---\nname: wrong-name\ndescription: A skill\n---\n")

    result = subprocess.run(["bash", str(script_path)], capture_output=True, text=True)
    assert result.returncode == 1
    assert "ERROR: skill-a — frontmatter name 'wrong-name' does not match the folder name" in result.stdout

def test_validate_skills_missing_description(mock_env):
    tmp_path, script_path, skills_dir = mock_env

    skill_a = skills_dir / "skill-a"
    skill_a.mkdir()
    (skill_a / "SKILL.md").write_text("---\nname: skill-a\n---\n")

    result = subprocess.run(["bash", str(script_path)], capture_output=True, text=True)
    assert result.returncode == 1
    assert "ERROR: skill-a — missing or empty description in frontmatter" in result.stdout

def test_validate_skills_warning_unknown_reference(mock_env):
    tmp_path, script_path, skills_dir = mock_env

    skill_a = skills_dir / "skill-a"
    skill_a.mkdir()
    (skill_a / "SKILL.md").write_text("---\nname: skill-a\ndescription: A valid skill\n---\nReferences `unknown-skill`.")

    result = subprocess.run(["bash", str(script_path)], capture_output=True, text=True)
    assert result.returncode == 0
    assert "WARN: skill-a — references 'unknown-skill', which is not (or no longer) a skill" in result.stdout
    assert "warnings: 1" in result.stdout
