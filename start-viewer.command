#!/bin/bash
cd "$(dirname "$0")" || exit 1
python3 apps/viewer/server.py
