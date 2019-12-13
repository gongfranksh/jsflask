from celery import Celery

# jsflaskcelery=Celery()

# jsflaskcelery=Celery('jsflaskcelery', broker='redis://192.168.168.223:6379/10',
jsflaskcelery=Celery('jsflaskcelery', broker='redis://192.168.168.223:6379/10')