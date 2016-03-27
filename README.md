
Dynamic regeneration based on YAML files
----------------------------------------

Linux:

	sudo apt-get install python-dateutil 
	sudo apt-get install pdftk

OS X:

	sudo pip install dateutil

	install pdftk manually

Both:
	sudo pip install SystemCmd==1.3 
	sudo pip install PyContracts


Then this rebuilds everything:

	make -B


Install required software for running on localhost
--------------------------------------------------

Install ruby 2.0:

	http://blog.costan.us/2014/04/restoring-ruby-20-on-ubuntu-1404.html


Install:

	sudo apt-get -y install bundler
	bundle install


Exec:

	bundle exec jekyll serve --host=0.0.0.0 --watch . 

Then open a web browser at http://127.0.0.1:8888.

