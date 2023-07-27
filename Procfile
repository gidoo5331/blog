release: python mysite/manage.py migrate
web: sh -c 'cd mysite && gunicorn mysite.wsgi'