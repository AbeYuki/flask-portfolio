DOCKERFILE_PATH = .

IMAGE_NAME = portfolio

VERSION = 1.2.0

REGISTRY = registry.gitlab.com/aimhighergg/docker-registry

PLATFORMS = linux/amd64,linux/arm64,linux/ppc64le,linux/s390x,linux/arm/v7,linux/arm/v8

build:
	docker build --no-cache -t $(IMAGE_NAME):latest $(DOCKERFILE_PATH)
	docker build --no-cache -t $(IMAGE_NAME):$(VERSION) $(DOCKERFILE_PATH)

push:
	docker buildx build --no-cache --platform $(PLATFORMS) -t $(REGISTRY)/$(IMAGE_NAME):latest --push $(DOCKERFILE_PATH)
	docker buildx build --no-cache --platform $(PLATFORMS) -t $(REGISTRY)/$(IMAGE_NAME):$(VERSION) --push $(DOCKERFILE_PATH)
