#!/usr/bin/env python3
"""
GitHub Repository Setup Script for FileProcessor1
This script prepares your files for GitHub upload
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a shell command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} - Success!")
            if result.stdout.strip():
                print(f"   Output: {result.stdout.strip()}")
            return True
        else:
            print(f"❌ {description} - Failed!")
            print(f"   Error: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"❌ {description} - Exception: {str(e)}")
        return False

def main():
    print("🚀 Setting up FileProcessor1 repository...")
    print("=" * 50)
    
    # Check if we're in a git repository
    if not os.path.exists('.git'):
        print("❌ Not in a git repository. Please run this in your project folder.")
        return
    
    # List files to be added
    files_to_add = ['app.py', 'main.py', 'Dockerfile', 'requirements_deploy.txt']
    print(f"📁 Files to add: {', '.join(files_to_add)}")
    print()
    
    # Add files to git
    if not run_command(f"git add {' '.join(files_to_add)}", "Adding files to git"):
        return
    
    # Commit files
    if not run_command('git commit -m "Initial commit - PDF text extraction API"', "Committing files"):
        return
    
    print()
    print("🎉 Repository setup complete!")
    print()
    print("📋 Next steps:")
    print("1. Create GitHub repository:")
    print("   • Go to: https://github.com/new")
    print("   • Repository name: FileProcessor1")
    print("   • Don't initialize with README")
    print()
    print("2. Connect and push:")
    print("   git remote add origin https://github.com/YOUR_USERNAME/FileProcessor1.git")
    print("   git branch -M main")
    print("   git push -u origin main")
    print()
    print("✅ Your PDF extraction API is ready for deployment!")

if __name__ == "__main__":
    main()