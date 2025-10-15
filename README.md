# MarzPay Python SDK

Official Python SDK for MarzPay - Mobile Money Payment Platform for Uganda.

## Features

- 🚀 **Complete API Coverage** - Collections, Disbursements, Accounts, Balance, Transactions, Services, Webhooks, and Phone Verification
- 🔧 **Error Handling** - Comprehensive error handling with custom exception classes
- 📱 **Phone Number Utilities** - Built-in phone number validation and formatting
- 🔗 **Webhook Support** - Easy webhook handling and validation
- 🧪 **Testing** - Full test coverage with pytest
- 📚 **Documentation** - Comprehensive documentation and examples
- ⚡ **Async Support** - Built-in async/await support for high-performance applications

## Installation

### pip

```bash
pip install marzpay-python
```

### Development

```bash
git clone https://github.com/Katznicho/marzpay-python.git
cd marzpay-python
pip install -e .
```

## Quick Start

### Basic Usage

```python
from marzpay import MarzPay

# Initialize the client
client = MarzPay(
    api_key="your_api_key",
    api_secret="your_api_secret"
)

# Collect money from customer
result = client.collections.collect_money(
    amount=5000,
    phone_number="0759983853",
    reference=client.collections.generate_reference(),
    description="Payment for services"
)

print(f"Collection ID: {result['data']['collection_id']}")
```

### Async Usage

```python
import asyncio
from marzpay import MarzPay

async def main():
    client = MarzPay(
        api_key="your_api_key",
        api_secret="your_api_secret"
    )
    
    # Collect money from customer
    result = await client.collections.collect_money_async(
        amount=5000,
        phone_number="0759983853",
        reference=client.collections.generate_reference(),
        description="Payment for services"
    )
    
    print(f"Collection ID: {result['data']['collection_id']}")

# Run the async function
asyncio.run(main())
```

## API Reference

### Collections API

```python
# Collect money
result = client.collections.collect_money(
    amount=10000,
    phone_number="0759983853",
    reference="unique-reference-id",
    description="Payment for services"
)

# Get collection details
collection = client.collections.get_collection("collection-id")

# Get available services
services = client.collections.get_services()

# Get all collections with filters
collections = client.collections.get_collections(
    page=1,
    limit=20,
    status="completed"
)
```

### Disbursements API

```python
# Send money
result = client.disbursements.send_money(
    amount=5000,
    phone_number="0759983853",
    reference="unique-reference-id",
    description="Refund payment"
)

# Get disbursement details
disbursement = client.disbursements.get_disbursement("disbursement-id")
```

### Webhooks

```python
# Handle webhook
webhook = client.webhooks.handle_webhook(request_body)

if webhook.is_valid():
    # Process the webhook
    transaction_id = webhook.get_transaction_id()
    status = webhook.get_status()
```

## Configuration

```python
from marzpay import MarzPay

client = MarzPay(
    api_key="your_api_key",
    api_secret="your_api_secret",
    base_url="https://wallet.wearemarz.com/api/v1",  # optional
    timeout=30,  # optional, in seconds
)
```

## Error Handling

```python
from marzpay import MarzPay
from marzpay.errors import MarzPayError

try:
    result = client.collections.collect_money(request_data)
except MarzPayError as e:
    print(f"Error Code: {e.code}")
    print(f"HTTP Status: {e.status}")
    print(f"Message: {e.message}")
    print(f"Details: {e.details}")
```

## Environment Variables

```python
import os
from marzpay import MarzPay

client = MarzPay(
    api_key=os.getenv("MARZPAY_API_KEY"),
    api_secret=os.getenv("MARZPAY_API_SECRET"),
)
```

## Testing

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=marzpay

# Run specific test file
pytest tests/test_collections.py
```

## Development

```bash
# Install development dependencies
pip install -e ".[dev]"

# Format code
black marzpay tests

# Lint code
flake8 marzpay tests

# Type checking
mypy marzpay
```

## License

MIT License. See [LICENSE](LICENSE) for details.

## Support

- Documentation: [https://docs.marzpay.com](https://docs.marzpay.com)
- Issues: [https://github.com/Katznicho/marzpay-python/issues](https://github.com/Katznicho/marzpay-python/issues)
- Email: dev@wearemarz.com

