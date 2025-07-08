import os
import sys

def check_readme():
    readme_path = "README.md"
    
    if not os.path.exists(readme_path):
        print("❌ README.md does not exist")
        sys.exit(1)
    
    if os.path.getsize(readme_path) == 0:
        print("❌ README.md exists but is empty")
        sys.exit(1)
    
    print("✅ README.md exists and is not empty")
    with open(readme_path, 'r') as f:
        print("\nFirst 3 lines:")
        for i in range(3):
            line = f.readline()
            if not line:
                break
            print(line.strip())

if __name__ == "__main__":
    check_readme()