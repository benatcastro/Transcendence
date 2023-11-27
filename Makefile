all: create_folders build
	@echo "All done!"y
build:
	docker-compose up --build

up:
	docker-compose up -d

down:
	docker-compose down -v

prune:
	docker system prune -a

clean: down prune

fclean: clean
	docker volume rm -f $(docker volume ls -q)  # Elimina todos los volúmenes
migrations:
	docker-compose exec django sh -c "python manage.py makemigrations && python manage.py migrate"
# Makefile

create_folders:
	@mkdir -p ./data/djangoFiles
	@mkdir -p ./data/static
	@mkdir -p ./data/postgres
	@echo "Folders created successfully."

.PHONY: build up down prune clean fclean migrations create_folders
