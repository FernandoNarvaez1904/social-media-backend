release: python manage.py migrate
web: gunicorn -k uvicorn.workers.UvicornWorker -b $PORT social_media_backend:application