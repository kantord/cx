#!/usr/bin/env bash

./update_db.sh
cron && python ./src/cx/api.py
