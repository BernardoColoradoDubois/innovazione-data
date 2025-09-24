include .env

airflow-init:
	docker compose up airflow-init

airflow-up:
	docker compose up -d

airflow-down:
	docker compose down -v
