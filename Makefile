.PHONY: d-project-i-run
# Make all actions needed for run project from zero.
d-project-i-run:
	@make init-configs-i-dev && make d-run


.PHONY: d-project-i-purge
# Make all actions needed for purge project related data.
d-project-i-purge:
	@make d-purge


.PHONY: d-run
# Just run
d-run:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		COMPOSE_PROFILES=full_dev \
		docker-compose up --build


.PHONY: d-run-i-local-dev
# Just run services for local-dev
d-run-i-local-dev:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		COMPOSE_PROFILES=local_dev \
		docker-compose up --build


.PHONY: d-run-i-extended
# Shutdown previous, run in detached mode, follow logs
d-run-i-extended:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose down --timeout 0 && \
	COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		COMPOSE_PROFILES=full_dev \
		docker-compose up --build --detach && \
	make d-logs-follow


.PHONY: d-stop
# Stop services
d-stop:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose down


.PHONY: d-logs-follow
# Follow logs
d-logs-follow:
	@docker-compose logs --follow


.PHONY: d-purge
# Purge all data related with services
d-purge:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose down --volumes --remove-orphans --rmi local --timeout 0


.PHONY: migrate
# Shortcut
migrate:
	@python manage.py migrate


.PHONY: migrations
# Shortcut
migrations:
	@python manage.py makemigrations


.PHONY: init-configs-i-dev
# Make some initialization steps. For example, copy configs.
init-configs-i-dev:
	@cp docker-compose.override.dev.yml docker-compose.override.yml
	@cp .env.proj .env


.PHONY: init-dev
# Updates pip and requirements, creates git-hub web-hooks
init-dev:
	@pip install --upgrade pip && \
	pip install --requirement requirements.txt && \
	pre-commit install


.PHONY: init-dev-create-superuser
# Create superuser/admin to work with admin panel
init-dev-create-superuser:
	@DJANGO_SUPERUSER_PASSWORD=admin123 python manage.py createsuperuser --user admin --email admin@gmail.com --no-input


.PHONY: pre-commit-run-all
# Run on all the files in the repo
pre-commit-run-all:
	@pre-commit run --all-files


.PHONY: util-i-kill-by-port
util-i-kill-by-port:
	sudo lsof -i:8011 -Fp | head -n 1 | sed 's/^p//' | xargs sudo kill


.PHONY: d-create-contacts-i-3
# Create three contacts to the database
d-create-contacts-i-3:
	@python manage.py create_contacts 3

.PHONY: d-generate-password-i-64
# Generates random 64 length string
d-generate-password-i-64:
	@python manage.py generate_password 64