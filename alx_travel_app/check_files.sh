#!/bin/bash

check_file() {
    local file=$1
    if [ -s "$file" ]; then
        echo "✅ $file exists and is not empty"
        return 0
    elif [ -f "$file" ]; then
        echo "⚠️  $file exists but is empty"
        return 1
    else
        echo "❌ $file does not exist"
        return 2
    fi
}

echo "Checking required files..."
check_file "README.md"
check_file "alx_travel_app/settings.py"