#!/usr/bin/env python3
"""
verify_setup.py - Verify development environment setup
"""

import sys
import os
from pathlib import Path

def check_python_version():
    """Verify Python version is 3.11+"""
    major = sys.version_info.major
    minor = sys.version_info.minor
    if major < 3 or (major == 3 and minor < 11):
        raise ValueError(f"Python version must be 3.11+. Current: {sys.version}")

def check_virtual_environment():
    """Verify running in virtual environment"""
    # Active if prefix differs from base_prefix, or VIRTUAL_ENV is in env
    in_venv = (sys.prefix != sys.base_prefix) or ("VIRTUAL_ENV" in os.environ)
    if not in_venv:
        raise ValueError("Virtual environment is not active. Run 'source venv/bin/activate' first.")

def check_required_packages():
    """Verify all required packages are installed"""
    required_packages = [
        "torch",
        "transformers",
        "pandas",
        "pytest",
        "black",
        "mypy"
    ]
    missing = []
    for pkg in required_packages:
        try:
            __import__(pkg)
        except ImportError:
            missing.append(pkg)
            
    if missing:
        raise ImportError(f"Missing required packages: {', '.join(missing)}")

def check_project_structure():
    """Verify project directories exist"""
    required_dirs = [
        "src",
        "tests",
        "data",
        "models",
        "configs"
    ]
    required_files = [
        "requirements.txt",
        "requirements-dev.txt",
        ".gitignore",
        ".env.example"
    ]
    
    base_path = Path(__file__).parent
    missing = []
    
    for d in required_dirs:
        if not (base_path / d).is_dir():
            missing.append(f"directory '{d}'")
            
    for f in required_files:
        if not (base_path / f).is_file():
            missing.append(f"file '{f}'")
            
    if missing:
        raise FileNotFoundError(f"Project structure is incomplete. Missing: {', '.join(missing)}")

def check_git_setup():
    """Verify git configuration"""
    base_path = Path(__file__).parent
    git_dir = base_path / ".git"
    if not git_dir.is_dir():
        raise FileNotFoundError(".git directory not found. Initialize Git with 'git init'.")
    
    gitignore_path = base_path / ".gitignore"
    if gitignore_path.is_file():
        with open(gitignore_path, "r") as f:
            content = f.read()
        if "venv/" not in content and ".venv/" not in content:
            raise ValueError(".gitignore does not ignore virtual environments (venv/).")
    else:
        raise FileNotFoundError(".gitignore file not found.")

def main():
    print("Verifying Development Environment Setup")
    print("=" * 50)

    checks = [
        ("Python Version", check_python_version),
        ("Virtual Environment", check_virtual_environment),
        ("Required Packages", check_required_packages),
        ("Project Structure", check_project_structure),
        ("Git Configuration", check_git_setup)
    ]

    all_passed = True

    for check_name, check_func in checks:
        try:
            check_func()
            print(f"✓ {check_name}")
        except Exception as e:
            print(f"✗ {check_name}: {e}")
            all_passed = False

    print("=" * 50)

    if all_passed:
        print("All checks passed! Environment is ready.")
        return 0
    else:
        print("Some checks failed. Please fix issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
