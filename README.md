# ai-workshop-hasuracon23

ARM64 and AMD64 images of Hasura and Weaviate are available

If you don't have git-lfs setup. Please follow these steps after cloning
```console
~$ brew install git-lfs
~$ git lfs install
~$ git lfs pull
```
Note: After cloning the image, you are required to execute `git lfs pull` to download the complete image. `brew install git-lfs` if you don't have that installed already.

To start:
```sh
# Set the right ARCH environment variable for your system
$ export ARCH={arm64|amd64}
$ docker load < hasura-image-${ARCH}.tar.gz
$ docker load < weaviate-gdc-image-${ARCH}.tar.gz
$ docker compose up
```

This will bring up
- Hasura console at `localhost:8080`
- Postgres with `metadata` database at `localhost:5432`
- Weaviate GDC agent at `localhost:8100`
- Action and Event Trigger handlers at `localhost:8400`

Note: You can alternatively modify docker-compose.yaml and uncomment the `handlers` container to bring up python handlers directly using Docker
