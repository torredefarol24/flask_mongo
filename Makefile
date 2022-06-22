init_network:
	docker network create --subnet=172.30.0.0/16 med_reminder || true

app:
	docker run -it -p 6161:6161 --rm \
		--ip 172.30.1.1 --net med_reminder \
		--mount type=bind,source="$(shell pwd)",target=/usr/src/app,readonly \
		--name app \
		med_reminder:dev

db:
	docker run -d -p 27017:27017 --rm \
		--ip 172.30.1.2 --net med_reminder \
		--name db_mongo	mongo:5.0.9
		
stop:
	docker stop app
	docker stop db_mongo

build:
	docker images -q mongo:5.0.9 || docker pull mongo:5.0.9
	docker build -t med_reminder:dev -f ./Dockerfile .