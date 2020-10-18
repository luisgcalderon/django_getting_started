podman run --name django_getting_started \
    -p 5432:5432 \
    -e POSTGRES_DB=django \
    -e POSTGRES_USER=django \
    -e POSTGRES_PASSWORD=django \
    -d postgres:13