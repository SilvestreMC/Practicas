#!/bin/bash

echo wikipedia api, busca algo random en wikipedia
curl -L "https://en.wikipedia.org/api/rest_v1/page/random/summary"
