
documents=05_materials.md
lectures=05_lectures.md

all: $(lectures) $(documents)

serve:
	bundle exec jekyll serve --host=0.0.0.0 --watch . 

$(lectures): lectures.yaml 
	./generate.py "media/staff/*yaml" lectures.yaml > $@
	
	
$(documents): documents.yaml
	./generate-documents.py < $< > $@