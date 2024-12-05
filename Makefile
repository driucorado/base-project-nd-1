

run:
	DB_URL="postgresql+psycopg2://user:S3cret@localhost/test_db" \
	uv run ./src/main.py

apply:
	DB_URL="postgresql+psycopg2://user:S3cret@localhost/test_db" \
	alembic upgrade head

down:
	DB_URL="postgresql+psycopg2://user:S3cret@localhost/test_db" \
	alembic downgrade -1

db:
	docker-compose up db


test:
	PYTHONPATH=. \
	DB_URL="sqlite:///:memory:" pytest .