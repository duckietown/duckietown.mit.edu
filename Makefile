
documents=05_materials.md
lectures=05_lectures.md
collected_pdfs=media/collected.pdf

all: $(lectures) $(documents) $(collected_pdfs)

serve:
	bundle exec jekyll serve --host=0.0.0.0 --watch . 

$(lectures): lectures.yaml 
	./generate.py "media/staff/*yaml" lectures.yaml > $@
	
	
$(documents): documents.yaml
	./generate-documents.py < $< > $@

$(collected_pdfs): documents.yaml
	./generate-pdf.py < $< > $@