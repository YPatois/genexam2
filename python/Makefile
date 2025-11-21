# Makefile
TEXFILES = q_isoze.tex q_isors.tex q_nomenca.tex
.PHONY: all clean

all: $(addprefix ../ste4/,$(TEXFILES))
	@echo "All targets built successfully."

../ste4/q_%.tex: ste4_%.py myamc.py
	python $<

clean:
	$(RM) $(addprefix ../ste4/,$(TEXFILES))
	rm -f q_*.tex
	@echo "Cleaned up generated TeX files."

