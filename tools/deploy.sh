#!/usr/bin/env bash
# Publie dist/ sur la branche gh-pages du dépôt (servie par GitHub Pages).
# Usage : tools/deploy.sh [message]   — lancer « make » avant (ou « make deploy » qui le fait).
set -euo pipefail
cd "$(dirname "$0")/.."
[ -f dist/index.html ] || { echo "dist/ absent : lancez « make » d'abord" >&2; exit 1; }
remote=$(git remote get-url origin)
msg=${1:-"Publication du $(date '+%Y-%m-%d %H:%M') (depuis $(git rev-parse --short HEAD))"}
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
# branche gh-pages orpheline, contenu = dist/ uniquement
git worktree add --detach "$work" >/dev/null 2>&1
(
  cd "$work"
  git checkout --orphan gh-pages >/dev/null 2>&1
  git rm -rfq . >/dev/null 2>&1 || true
  cp -R "$OLDPWD/dist/." .
  touch .nojekyll
  git add -A
  git commit -qm "$msg"
  git push -f "$remote" gh-pages:gh-pages
)
git worktree remove --force "$work"
echo "→ publié sur la branche gh-pages de $remote"
