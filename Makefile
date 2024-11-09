initial:
	python manage.py makemigrationss
	python manage.py migrate
	python manage.py collectstatic
	python manage.py loaddata testdata_for_db.json

admin:
	python manage.py createsuperuser