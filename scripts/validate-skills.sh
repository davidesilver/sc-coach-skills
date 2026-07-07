#!/usr/bin/env bash
# Valida ogni skills/<nome>/SKILL.md: frontmatter coerente + riferimenti incrociati a skill esistenti.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_DIR="$ROOT/skills"
errors=0
warnings=0

mapfile -t SKILL_NAMES < <(find "$SKILLS_DIR" -mindepth 1 -maxdepth 1 -type d -exec basename {} \; | sort)

is_known_skill() {
  local name="$1"
  for s in "${SKILL_NAMES[@]}"; do
    [ "$s" = "$name" ] && return 0
  done
  return 1
}

for dir in "$SKILLS_DIR"/*/; do
  name=$(basename "$dir")
  file="${dir}SKILL.md"

  if [ ! -f "$file" ]; then
    echo "ERROR: $name — SKILL.md mancante"
    errors=$((errors + 1))
    continue
  fi

  fm_name=$(awk '/^---$/{c++; next} c==1 && /^name:/{print; exit}' "$file" | sed 's/^name:[[:space:]]*//')
  if [ "$fm_name" != "$name" ]; then
    echo "ERROR: $name — frontmatter name '$fm_name' non combacia con il nome della cartella"
    errors=$((errors + 1))
  fi

  fm_desc=$(awk '/^---$/{c++; next} c==1 && /^description:/{print; exit}' "$file")
  if [ -z "$fm_desc" ]; then
    echo "ERROR: $name — description mancante o vuota nel frontmatter"
    errors=$((errors + 1))
  fi

  refs=$(grep -oE '`[a-z]+(-[a-z]+)+`' "$file" | tr -d '`' | sort -u || true)
  for ref in $refs; do
    if [ "$ref" != "$name" ] && ! is_known_skill "$ref"; then
      echo "WARN: $name — riferisce a '$ref', che non è (più) una skill in skills/. Refuso dopo un rename/merge, o solo un termine tecnico?"
      warnings=$((warnings + 1))
    fi
  done
done

echo ""
echo "Skill controllate: ${#SKILL_NAMES[@]} — errori: $errors, warning: $warnings"

if [ "$errors" -gt 0 ]; then
  exit 1
fi
