# создать миграцию
make-migration:
	alembic revision --autogenerate -m "$(commit-message)"

# Выполнить миграцию
migrate:
	alembic upgrade head
