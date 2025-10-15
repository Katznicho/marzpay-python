#!/usr/bin/env python3
"""
PyPI Upload Script for MarzPay Python SDK

This script helps upload the package to PyPI.
Make sure to set your API token in .pypirc first!
"""

import os
import subprocess
import sys


def run_command(cmd, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"   Error: {e.stderr}")
        return False


def main():
    """Main upload process"""
    print("🚀 MarzPay Python SDK - PyPI Upload")
    print("=" * 50)
    
    # Check if .pypirc exists
    if not os.path.exists('.pypirc'):
        print("❌ .pypirc file not found!")
        print("   Please create .pypirc with your PyPI API token")
        print("   See PYPI_RELEASE_GUIDE.md for instructions")
        return
    
    # Check if dist directory exists
    if not os.path.exists('dist'):
        print("❌ dist/ directory not found!")
        print("   Please run: python -m build")
        return
    
    # Check if package files exist
    dist_files = os.listdir('dist')
    if not dist_files:
        print("❌ No package files found in dist/")
        print("   Please run: python -m build")
        return
    
    print(f"📦 Found {len(dist_files)} package files:")
    for file in dist_files:
        print(f"   - {file}")
    
    # Ask for confirmation
    print("\n⚠️  This will upload to PyPI!")
    confirm = input("   Do you want to proceed? (y/N): ").lower().strip()
    
    if confirm != 'y':
        print("❌ Upload cancelled")
        return
    
    # Upload to PyPI
    if not run_command("python -m twine upload dist/*", "Uploading to PyPI"):
        return
    
    print("\n🎉 Upload completed successfully!")
    print("\n📦 Your package is now available at:")
    print("   https://pypi.org/project/marzpay-python/")
    print("\n📚 Users can install it with:")
    print("   pip install marzpay-python")
    print("\n🔍 Test the installation:")
    print("   pip install marzpay-python")
    print("   python -c \"import marzpay; print('✅ Success!')\"")


if __name__ == "__main__":
    main()
