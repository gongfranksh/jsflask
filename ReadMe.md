
celery -A api.jsflaskcelery worker -P eventlet
celery flower -A api.jsflaskcelery