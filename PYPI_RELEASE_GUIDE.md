# 🚀 MarzPay Python SDK - PyPI Release Guide

This guide will help you release the MarzPay Python SDK to PyPI.

## 📋 Prerequisites

1. **PyPI Account**: Create one at https://pypi.org/account/register/
2. **API Token**: Get one from https://pypi.org/manage/account/
3. **Package Built**: Already done! ✅

## 🔧 Setup Steps

### Step 1: Get PyPI API Token

1. Go to https://pypi.org/manage/account/
2. Scroll to "API tokens"
3. Click "Add API token"
4. Name: `marzpay-python`
5. Scope: "Entire account"
6. Copy the token (starts with `pypi-`)

### Step 2: Configure Credentials

Edit `.pypirc` file and replace `YOUR_PYPI_API_TOKEN_HERE` with your actual token:

```ini
[distutils]
index-servers = pypi testpypi

[pypi]
username = __token__
password = pypi-AgEIcHlwaS5vcmcCJGI4YjQ5YjY5LWE5YjEtNDY4YS04YjQ5LWE5YjE0Njg0YjQ5YgAAJGI4YjQ5YjY5LWE5YjEtNDY4YS04YjQ5LWE5YjE0Njg0YjQ5Yg

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = YOUR_TEST_PYPI_API_TOKEN_HERE
```

## 🧪 Test Upload (Recommended)

First, test on Test PyPI:

```bash
# Upload to Test PyPI
python -m twine upload --repository testpypi dist/*

# Test installation from Test PyPI
pip install --index-url https://test.pypi.org/simple/ marzpay-python
```

## 🚀 Production Upload

Once tested, upload to real PyPI:

```bash
# Upload to PyPI
python -m twine upload dist/*
```

## 📦 Verify Installation

After upload, test the installation:

```bash
# Install from PyPI
pip install marzpay-python

# Test import
python -c "import marzpay; print('✅ Success!')"
```

## 🔍 Check Package

Visit your package on PyPI:
- **Test PyPI**: https://test.pypi.org/project/marzpay-python/
- **Production PyPI**: https://pypi.org/project/marzpay-python/

## 📚 Usage After Release

Users can install with:

```bash
pip install marzpay-python
```

And use it like:

```python
from marzpay import MarzPay

client = MarzPay(
    api_key="your_api_key",
    api_secret="your_api_secret"
)
```

## 🔄 Future Releases

To release a new version:

1. Update version in `pyproject.toml`
2. Update `CHANGELOG.md`
3. Build: `python -m build`
4. Upload: `python -m twine upload dist/*`

## 🛡️ Security Notes

- Never commit `.pypirc` with real tokens
- Use environment variables for CI/CD
- Test on Test PyPI first
- Keep API tokens secure

## 📞 Support

- **Documentation**: https://wallet.wearemarz.com/documentation
- **GitHub**: https://github.com/Katznicho/marzpay-python
- **Issues**: https://github.com/Katznicho/marzpay-python/issues
