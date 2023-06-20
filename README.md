# ai-workshop-hasuracon23

Currently only ARM64 images of Hasura and Weaviate are available

To start:

```console
~$ docker load < hasura-image-arm64.tar.gz
~$ docker load < weaviate-gdc-image-arm64.tar.gz
~$ docker compose up
```

This will bring up
- Hasura console at `localhost:8080`
- Postgres with `metadata` database at `host.docker.internal:5432`
- Weaviate GDC agent at `host.docker.internal:8100`
- Action and Event Trigger handlers at `host.docker.internal:8400`

You need update docker-compose.yaml with your OPENAI key to use in the LLM code.