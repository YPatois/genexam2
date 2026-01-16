# Makefile
TEXFILES = q_alcans.tex q_alcools.tex q_groups.tex q_nomencla.tex q_isors.tex q_isoze.tex
.PHONY: all clean

all: $(TEXFILES)
	@echo "All targets built successfully."

%.tex: ../python/%.py ../python/myamc.py ../python/myacmhelper.py
	python3 $<

clean:
	$(RM) $(TEXFILES)
	@echo "Cleaned up generated TeX files."
