# Colors
HEADER := $(shell tput -Txterm setaf 6)
GREEN := $(shell tput -Txterm setaf 2)
DEFAULT := $(shell tput -Txterm sgr0)

all: create_folders build grafana_up
	@echo "${GREEN}All done!${DEFAULT}"

grafana_up:
	export UID=$(id -u); \
    	export GID=$(id -g);
	@echo "${GREEN} Grafana permissions done!!${DEFAULT}"
build:
	docker compose up --build

up:
	docker compose up -d

down:
	docker compose down -v

prune:
	yes | docker system prune -a

clean: down prune

fclean: clean
	docker compose down -v --remove-orphans --rmi all

migrations:
	docker compose exec django sh -c "python manage.py makemigrations && python manage.py migrate"

create_folders:
	@mkdir -p ./data/djangoFiles
	@mkdir -p ./data/static
	@mkdir -p ./data/postgres
	@mkdir -p ./data/grafana-data
	@echo "${GREEN}Folders created successfully.${DEFAULT}"

reload_django:
	docker compose up --force-recreate --build -d django

help:
	@echo "${HEADER}${DEFAULT}"
	@echo "${HEADER}                                                                                                    	   ${DEFAULT}"
	@echo "${HEADER}${DEFAULT}                                  ${GREEN}Transcendence${DEFAULT}                           ${HEADER}${DEFAULT}"
	@echo "${HEADER}                                                                                                     ${DEFAULT}"
	@echo "${HEADER}   |_   _|  _ __    __ _   _ __    ___    ___    ___   _ __     __| |   ___   _ __     ___    ___     ${HEADER}${DEFAULT}"
	@echo "${HEADER}     \| |   | '__|  / _\` | | '_ \  / __|  / __|  / _ \ | '_ \   / _\` |  / _ \ | '_ \   / __|  / _ \ ${HEADER}${DEFAULT}"
	@echo "${HEADER}      | |   | |    | (_| | | | | | \__ \ | (__  |  __/ | | | | | (_| | |  __/ | | | | | (__  |  __/   ${HEADER}${DEFAULT}"
	@echo "${HEADER}      |_|   |_|     \__,_| |_| |_| |___/  \___|  \___| |_| |_|  \__,_|  \___| |_| |_|  \___|  \___|    ${HEADER}${DEFAULT}"
	@echo "${HEADER}                                                                                                 		${DEFAULT}"
	@echo "${HEADER}                                 ${GREEN}42Urduliz - @goodbye C${DEFAULT}                              ${HEADER}${DEFAULT}"
	@echo "${HEADER}                                                                                                		${DEFAULT}"
	@echo "${HEADER}${DEFAULT}"


	@echo "Usage: make [target]"
	@echo "Targets:"
	@echo ""
	@echo "${GREEN}build${DEFAULT}			: Build the application with docker compose."
	@echo "${GREEN}up${DEFAULT}			: Start the application in detached mode (background)."
	@echo "${GREEN}down${DEFAULT}			: Stop and remove containers, along with volumes."
	@echo "${GREEN}prune${DEFAULT}			: Clean up all unused resources, including containers and images."
	@echo "${GREEN}clean${DEFAULT}			: Stop and remove containers, along with volumes, and perform additional cleanup."
	@echo "${GREEN}fclean${DEFAULT}			: Perform a complete cleanup, including removing all volumes."
	@echo "${GREEN}migrations${DEFAULT}		: Run Django database migrations."
	@echo "${GREEN}create_folders${DEFAULT}		: Create the necessary folders for the application."
	@echo ""
	@echo "${GREEN}Note:${DEFAULT} Make sure to have Docker and docker compose installed to run the commands."
	@echo ""

.PHONY: all build up down prune clean fclean migrations create_folders help reload_django grafana_up
