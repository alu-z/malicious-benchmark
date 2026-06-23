#!/usr/bin/env bash
set -euo pipefail

curl -fsSL https://example.invalid/archive.tar.gz -o archive.tar.gz
echo "downloaded archive only"

