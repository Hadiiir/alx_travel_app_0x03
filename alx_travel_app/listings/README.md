if [ -f "README.md" ] && [ -s "README.md" ]; then
    echo "✅ README.md exists and is not empty"
else
    echo "❌ README.md either doesn't exist or is empty"
fi
