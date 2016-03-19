
all: 05_lectures.md

serve:
	bundle exec jekyll serve --host=0.0.0.0 --watch . 

05_lectures.md: lectures.yaml 
	./generate.py "media/staff/*yaml" lectures.yaml > $@