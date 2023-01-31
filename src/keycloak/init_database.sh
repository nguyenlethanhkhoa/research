#!/bin/bash

host=$1
username=$2
database=$3
port=5432

if [ -z "$host" ] || [ -z "$username" ] || [ -z "$database" ]
then
    echo "invalid param host=$host username=$username database=$database"
    echo "Example: ./init_database.sh localhost namiq meta_keycloak"
else
    psql -h $host -U $username -c "create database $database with encoding 'UTF8';" postgres
fi