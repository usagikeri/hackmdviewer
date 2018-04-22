#!/bin/sh

git clone https://github.com/hackmdio/hackmd
cp docker-compose.yml hackmd/
cp dockerfile hackmd/

cd hackmd
docker-compose up -d --build
