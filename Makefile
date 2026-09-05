# Révise STI2D — paquet de contenu. La logique vit dans le moteur (revise-core) ; ce fichier ne
# fait que l'appeler. CORE dit où le trouver : à côté par défaut, sinon « make CORE=… ».
#   make            → figures + contenu + application assemblée dans dist/
#   make figures    → compile les figures TikZ (figures/build/svg)
#   make content    → engendre dist/content.js et ses paquets d'unité
#   make check      → vérifie le contenu construit et les droits
#   make droits     → le détail de la comparaison aux transcriptions des manuels
#   make test       → tests unitaires du moteur
#   make serve      → serveur local sur http://localhost:8000/
#   make planche    → ouvre la planche récapitulative des liaisons (PDF)
#   make deploy     → publie dist/ sur la branche gh-pages
#   make clean      → supprime figures/build et dist
CORE ?= ../revise-core
PY ?= python3

.PHONY: all figures content check droits test serve planche deploy clean

all: content

figures:
	$(PY) $(CORE)/revise/build_figures.py

content: figures
	$(PY) $(CORE)/revise/build_content.py

check:
	$(PY) $(CORE)/revise/validate.py
	$(PY) $(CORE)/revise/check_droits.py

droits:
	$(PY) $(CORE)/revise/check_droits.py --tout --montrer 400

test:
	$(MAKE) -C $(CORE) test

serve: content
	$(PY) $(CORE)/revise/serve.py

planche: figures
	open figures/build/pdf/planche-liaisons.pdf

deploy: content
	$(CORE)/revise/deploy.sh

clean:
	rm -rf figures/build dist
