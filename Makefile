COMPOSE_FILE=docker-compose.yml

#build app
build:
	docker-compose -f $(COMPOSE_FILE) build 

start:
	docker-compose -f $(COMPOSE_FILE) up -d

stop:
	docker-compose -f $(COMPOSE_FILE) down