#!/bin/bash

# Usage: ./find_logs.sh "keyword"

if [ -z "$1" ]; then
  echo "Usage: $0 'search_term'"
  exit 1
fi

SEARCH_TERM=$1
LOG_DIR="/path/to/logs"
OUTPUT_FILE="found_logs_$(date +%F_%T).log"

# Search through logs and save results
grep -ri "$SEARCH_TERM" "$LOG_DIR" > "$OUTPUT_FILE"

echo "Search complete. Results saved in $OUTPUT_FILE"
