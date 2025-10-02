.PHONY: help start stop logs migrate shell superuser

help:
	@echo "🚀 ERP Dashboard - Commandes"
	@echo ""
	@echo "  make start      - Lancer tout"
	@echo "  make stop       - Arrêter"
	@echo "  make logs       - Voir les logs"
	@echo "  make migrate    - Migrations"
	@echo "  make superuser  - Créer admin"
	@echo "  make shell      - Shell Django"

start:
	@echo "🚀 Lancement de l'ERP..."
	docker-compose up -d
	@echo "✅ Django: http://localhost:8000"
	@echo "✅ PHPMyAdmin: http://localhost:8080"

stop:
	docker-compose down

logs:
	docker-compose logs -f django

migrate:
	docker-compose exec django python manage.py migrate

superuser:
	docker-compose exec django python manage.py createsuperuser

shell:
	docker-compose exec django python manage.py shell