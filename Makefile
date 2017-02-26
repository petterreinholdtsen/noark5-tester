# docker build says: reference format: repository name must be lowercase
project ?=nikita5/noark5-tester

docker:
	docker build -t ${project} .
docker_deploy: docker docker_push
	echo "Pushed to docker, https://hub.docker.com/r/${project}"
docker_run: docker
	docker run --network="host" --add-host=$(shell hostname):127.0.0.1 ${project}
docker_push:
	docker push ${project}
docker_tail:
	docker logs `docker ps | grep ${project} | awk ' { print $$1 } '`
