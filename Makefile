build:
	docker-compose up --build

up:
	docker-compose up -d

down:
	docker-compose down -v

prune:
	docker system prune -a

clean: down prune

rebuildDjango:
	docker-compose up -d --force-recreate --no-deps --build django

rebuild:
	docker-compose up -d --force-recreate --no-deps --build

fclean: clean
	docker volume rm -f $(docker volume ls -q)  # Elimina todos los volúmenes
migrate:
	docker-compose exec django sh -c "python manage.py makemigrations && python manage.py migrate"
.PHONY: build up down prune clean fclean migrations rebuild rebuild rebuildDjango
