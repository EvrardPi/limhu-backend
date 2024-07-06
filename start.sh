#!/usr/bin/env sh
until python manage.py migrate; do
echo "Migrations failed, retrying in 3 seconds..."
sleep 3
done

PORT=${PORT:-8000}

python manage.py loaddata ./fixtures/articles.json
python -m gunicorn --bind=0.0.0.0:$PORT backend.wsgi