# Makefile pour créer des liens symboliques vers les fichiers .tex

TARGET_DIR := ../../genexam2/ste7
LINK_DIR := .
TEX_FILES := $(wildcard $(TARGET_DIR)/*.tex)

all: links images

links:
	@echo "Création des liens symboliques pour les fichiers .tex..."
	@for file in $(TEX_FILES); do \
	    ln -s $$file $(LINK_DIR); \
	done
	@echo "Liens créés."

images:
	@echo "Création des liens symboliques pour les images..."
	ln -sf $(TARGET_DIR)/images $(LINK_DIR)/images

clean:
	@echo "Suppression des liens symboliques..."
	@rm -f $(notdir $(TEX_FILES))
	@echo "Liens supprimés."

.PHONY: all links clean
