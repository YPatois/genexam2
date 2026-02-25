# Makefile
GENEXAM := ../../genexam2
CURR_STE := ste7
TARGET_DIR := $(GENEXAM)/$(CURR_STE)
LINK_DIR := .
LINKTEX_FILES := $(wildcard $(TARGET_DIR)/*.tex)


TEXFILES = q_alcans.tex q_alcools.tex q_groups.tex q_nomencla.tex q_isors.tex q_isoze.tex
.PHONY: all clean

all: links images chemcache $(TEXFILES)
	@echo "All targets built successfully."

links:
	@echo "Création des liens symboliques pour les fichiers .tex..."
	@for file in $(LINKTEX_FILES); do \
	    ln -sf $$file $(LINK_DIR); \
	done
	@echo "Liens créés."

images:
	@echo "Création des liens symboliques pour les images..."
	ln -sf $(TARGET_DIR)/images $(LINK_DIR)/images

chemcache:
	ln -sf $(GENEXAM)/python/chemcache chemcache

%.tex: $(GENEXAM)/python/%.py $(GENEXAM)/python/myamc.py $(GENEXAM)/python/myacmhelper.py
	python3 $<

clean:
	$(RM) $(TEXFILES) images chemcache *.aux *.log *.out *.pdf
	@echo "Cleaned up generated TeX files."
