sleep 10

alembic upgrade head

uvicorn main:app --host 0.0.0.0 --port 80