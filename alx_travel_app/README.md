# Check if file exists and is not empty
if [ -s "README.md" ]; then
    echo "README.md exists and is not empty"
else
    echo "README.md either doesn't exist or is empty"
fi

# View file size and first few lines (optional)
ls -lh README.md 2>/dev/null || echo "README.md not found"
head -n 3 README.md 2>/dev/null || echo "Cannot display content"