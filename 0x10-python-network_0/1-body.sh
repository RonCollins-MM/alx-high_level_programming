#!/bin/bash
# Script that takes in a URL, sends a GET request to the URL, and displays the body of the response for only 200 code
curl -sL -X GET "$1"
