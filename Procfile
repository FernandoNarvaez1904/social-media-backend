release: python manage.py migrate
web: gunicorn -k uvicorn.workers.UvicornWorker --port $PORT social_media_backend:application