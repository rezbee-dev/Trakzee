#!/bin/sh

echo "Waiting for postgres..."

# nc reads/writes data between networks
# -z reports connection status w/o connecting
# While "Connection to api-db port 5432 [tcp/postgresql] succeeded!" does not appear, wait
while ! nc -z api-db 5432; do
  sleep 0.1
done

# Display msg that Postgres has started
echo "PostgreSQL started"

# Execute flask app
python src/main.py run -h 0.0.0.0