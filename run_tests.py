#!/usr/bin/env python3
"""
Test runner for MarzPay Python SDK
"""

import sys
import subprocess
import os
from pathlib import Path


def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"Command: {command}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        return False


def main():
    """Main test runner"""
    print("MarzPay Python SDK Test Runner")
    print("=" * 50)
    
    # Change to project directory
    project_dir = Path(__file__).parent
    os.chdir(project_dir)
    
    # Check if pytest is available
    try:
        import pytest
        print("✓ pytest is available")
    except ImportError:
        print("✗ pytest not found. Installing...")
        if not run_command("pip install pytest", "Installing pytest"):
            print("Failed to install pytest")
            return False
    
    # Run different test suites
    test_suites = [
        {
            "name": "Unit Tests",
            "command": "python -m pytest tests/test_marzpay.py tests/test_collections.py tests/test_disbursements.py tests/test_phone_verification.py tests/test_utilities.py -v",
            "description": "Running unit tests for all components"
        },
        {
            "name": "Integration Tests",
            "command": "python -m pytest tests/test_integration.py -v -m integration",
            "description": "Running integration tests"
        },
        {
            "name": "All Tests",
            "command": "python -m pytest tests/ -v --tb=short",
            "description": "Running all tests"
        },
        {
            "name": "Test Coverage",
            "command": "python -m pytest tests/ --cov=marzpay --cov-report=html --cov-report=term",
            "description": "Running tests with coverage"
        }
    ]
    
    results = {}
    
    for suite in test_suites:
        print(f"\n{'='*60}")
        print(f"Test Suite: {suite['name']}")
        print(f"{'='*60}")
        
        success = run_command(suite['command'], suite['description'])
        results[suite['name']] = success
        
        if not success:
            print(f"❌ {suite['name']} failed")
        else:
            print(f"✅ {suite['name']} passed")
    
    # Summary
    print(f"\n{'='*60}")
    print("TEST SUMMARY")
    print(f"{'='*60}")
    
    for name, success in results.items():
        status = "✅ PASSED" if success else "❌ FAILED"
        print(f"{name}: {status}")
    
    # Check if all tests passed
    all_passed = all(results.values())
    
    if all_passed:
        print("\n🎉 All tests passed!")
        return 0
    else:
        print("\n💥 Some tests failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
