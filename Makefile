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
	docker-compose exec web sh -c "python manage.py makemigrations && python manage.py migrate"
.PHONY: build up down prune clean fclean migrations
