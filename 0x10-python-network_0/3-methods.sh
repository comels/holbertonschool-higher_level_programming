#!/bin/bash
curl -siLX OPTIONS "$1" | grep "Allow:" | cut -d " " -f2-
