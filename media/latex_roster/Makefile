ALL: clean auto_roster.pdf 

%.pdf: %.tex Makefile
	python create_latex.py; pdflatex --enable-write18 $< &&	pdflatex $< && pdflatex $<

clean:
	  rm -f *.aux	*.bbl	*.blg	*.log	auto_roster*.pdf 
