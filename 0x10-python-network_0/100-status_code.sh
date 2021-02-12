#!/bin/bash
# Sends a request to URL passed as an argument and displays status code
curl -so /dev/null -w "%{http_code}" $1
