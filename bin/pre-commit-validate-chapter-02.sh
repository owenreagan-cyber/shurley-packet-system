#!/usr/bin/env bash
# Pre-commit validation bundle for Chapter 2 (C2B-2).
# Run from repository root before staging/committing chapter-02 deliverables.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

GENERATOR="scripts/generate_chapter_02.py"
VALIDATOR="scripts/validate_chapter_02.py"

pass() { echo "PASS: $*"; }
fail() { echo "FAIL: $*" >&2; exit 1; }

if [ "${1:-}" = "--status" ]; then
  echo "Chapter 2 Deployment Status"
  echo "==========================="
  echo "Branch: $(git branch --show-current 2>/dev/null || echo unknown)"
  echo "Generator: $GENERATOR"
  echo "Validator: $VALIDATOR"
  for path in \
    "$GENERATOR" \
    "$VALIDATOR" \
    "packets/student/chapter-02/chapter-02-shurley-packet.docx" \
    "packets/teacher-keys/chapter-02/chapter-02-shurley-packet-teacher-edition.docx" \
    "packets/chapter-reviews/chapter-02/chapter-02-in-class-chapter-review.docx" \
    "packets/chapter-reviews/chapter-02/chapter-02-in-class-chapter-review-key.docx"; do
    if [ -f "$path" ]; then
      echo "  present: $path"
    else
      echo "  MISSING: $path"
    fi
  done
  if [ -f "$VALIDATOR" ]; then
    echo ""
    python3 "$VALIDATOR" || true
  fi
  exit 0
fi

echo "Running Chapter 2 pre-commit validation bundle..."
echo ""

echo "== git diff --check =="
if git diff --check; then
  pass "git diff --check (no conflict markers or trailing whitespace in diff)"
else
  fail "git diff --check reported issues"
fi
echo ""

echo "== bash -n bin/pre-commit-validate-chapter-02.sh =="
bash -n bin/pre-commit-validate-chapter-02.sh
pass "validation bundle syntax"
echo ""

echo "== python3 -m py_compile (generator + validator) =="
python3 -m py_compile "$GENERATOR" "$VALIDATOR"
pass "python syntax"
echo ""

echo "== python3 scripts/validate_chapter_02.py =="
python3 "$VALIDATOR"
pass "chapter-02 validation"
echo ""

echo "Chapter 2 pre-commit validation: PASS"
