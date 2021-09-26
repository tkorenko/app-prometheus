
IMAGE_TAG:=0.2
IMAGE_DH_REPO:=synfinmelab
APP_NAME:=app-prometheus
IMAGE_NAME:=${IMAGE_DH_REPO}/${APP_NAME}

_start	:
	echo 'Use { build | push } targets'

build	:
	docker build . -t "${IMAGE_NAME}:${IMAGE_TAG}"
	docker build . -t "${IMAGE_NAME}:latest"

push	:
	docker push "${IMAGE_NAME}:${IMAGE_TAG}"
	docker push "${IMAGE_NAME}:latest"

run	:
	docker run --rm -it --name prom-metrics-exp \
		"${IMAGE_NAME}:latest"
