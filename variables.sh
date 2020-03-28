#!/bin/bash
set -o pipefail
export RUN_MODE=dev
export DB_NAME=mydb
export DB_USERNAME=postgres
export DB_PASSWORD=postgres
export DB_HOST=localhost
export DB_PORT=5432
export SECRET_KEY='s3#@FW3e#%ad132oWnsAe*Dfm'
exec "$@"