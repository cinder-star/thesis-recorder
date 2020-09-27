install:
	sudo pip -r install --sequential -U requirements.txt

run:
	python manage.py runserver

db_make_migrate:
	python manage.py makemigrations

db_shell:
	python manage.py dbshell

db_migrate:
	python manage.py db migrate

clean:
	find . -name \*.pyc -type f -delete
	find . -name __pycache__  -type d -delete
	rm -rf .pytest_cache/
