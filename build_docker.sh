export DOCKER_BUILDKIT=1

docker build . -f Dockerfile -t wordcount
