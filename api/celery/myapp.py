from celery import Celery

mycelery = Celery('mycelery', include=['api.celery.async'])

mycelery.config_from_object("mycelery.settings")
# app.config_from_object(settings)

if __name__ == "__main__":
    # app.worker_main()
    # print(app.main)
    mycelery.start()