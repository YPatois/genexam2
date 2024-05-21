all: textemplates/maintemplate.pdf


%.pdf: %.tex
	pdflatex -output-directory outdir/pdf/ $<
