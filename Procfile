release: python manage.py migrate
web: hypercorn social_media_backend.asgi:application --bind 0.0.0.0:$PORT