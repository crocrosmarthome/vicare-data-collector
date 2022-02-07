#!/bin/sh
while sleep "$POLLING_INTERVAL_S"; do python main.py; done