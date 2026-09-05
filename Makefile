# Révise STI2D — tout se reconstruit avec « make ».
#   make            → figures + contenu + copie de l'application dans dist/
#   make figures    → compile les figures TikZ (figures/build/svg)
#   make content    → génère dist/content.json et dist/content.js, copie app/
#   make check      → vérifie les sources pédagogiques et le contenu construit
#   make droits     → compare le contenu publié aux transcriptions du manuel (droits d'auteur)
#   make test       → tests unitaires de l'application (node --test)
#   make serve      → serveur local sur http://localhost:8000/
#   make planche    → ouvre la planche récapitulative des liaisons (PDF)
#   make deploy     → publie dist/ sur la branche gh-pages (GitHub Pages)
#   make clean      → supprime figures/build et dist
PY ?= python3

.PHONY: all figures content check droits test serve planche deploy clean

all: content

figures:
	$(PY) tools/build_figures.py

content: figures
	$(PY) tools/build_content.py

check:
	$(PY) tools/validate.py

droits:
	$(PY) tools/check_droits.py

test:
	cd app && node --test tests/*.test.mjs

serve: content
	$(PY) tools/serve.py

planche: figures
	open figures/build/pdf/planche-liaisons.pdf

deploy: content
	tools/deploy.sh

clean:
	rm -rf figures/build dist
