#!/usr/bin/env python3
"""
FileProcessor1 Repository Creator
Creates a clean folder with just the files you need for GitHub
"""

import os
import shutil
import zipfile

def create_repository():
    """Create a clean repository folder and zip file"""
    
    # Create clean directory
    repo_name = "FileProcessor1"
    if os.path.exists(repo_name):
        shutil.rmtree(repo_name)
    
    os.makedirs(repo_name)
    print(f"📁 Created {repo_name} directory")
    
    # Files to include
    files_to_copy = [
        'app.py',
        'main.py', 
        'Dockerfile',
        'requirements_deploy.txt'
    ]
    
    # Copy files
    for file in files_to_copy:
        if os.path.exists(file):
            shutil.copy2(file, repo_name)
            print(f"✅ Copied {file}")
        else:
            print(f"❌ Missing {file}")
    
    # Create zip file
    zip_name = f"{repo_name}.zip"
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in files_to_copy:
            file_path = os.path.join(repo_name, file)
            if os.path.exists(file_path):
                zipf.write(file_path, file)
    
    print(f"📦 Created {zip_name}")
    print()
    print("🎉 Repository ready!")
    print()
    print("📋 Next steps:")
    print("1. Download the FileProcessor1.zip file")
    print("2. Go to https://github.com/new")
    print("3. Repository name: FileProcessor1")
    print("4. Create repository")
    print("5. Upload the files from the zip")
    print()
    print("✅ Your PDF extraction API will be ready for deployment!")

if __name__ == "__main__":
    create_repository()