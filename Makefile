
roster_html=roster.html.part

documents=05_materials.md
lectures=05_lectures.md
outreach=08_outreach.md
collected_pdfs=media/collected.pdf
roster=06_staff.md

all: $(lectures) $(documents) $(collected_pdfs)  $(roster) $(outreach)


serve:
	bundle exec jekyll serve --host=0.0.0.0 --watch . 

$(lectures): lectures.yaml 
	./generate_lectures.py "media/staff/*yaml" lectures.yaml > $@

$(roster_html):
	./generate_roster.py "media/staff/*yaml" > $@

$(documents): documents.yaml 05_materials.begin
	./generate_documents.py < $< > $@

$(outreach): outreach.yaml generate_outreach.py
	./generate_outreach.py < $< > $@

$(collected_pdfs): documents.yaml
	./generate_pdf.py < $< > $@


$(roster): roster.html.head $(roster_html) 
	echo "---\nlayout: page\ntitle: People\npermalink: staff.html\n---\n\n" > $(roster)
	cat $^ >> $(roster)

regenerate-and-push:
	-$(MAKE) -B
	git commit -a -m regenerated
	git push


install-linux:
	sudo pip install dateutil
	sudo apt-get install python-dateutil
	sudo pip install SystemCmd==1.3
	sudo pip install PyContracts
	sudo apt-get install pdftk

