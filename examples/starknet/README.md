# Starknet USDC Integration Examples

This directory contains example scripts demonstrating the Starknet USDC integration features in `supabase-py`.

## Available Examples

### 1. Basic Usage (`basic_usage.py`)

Demonstrates fundamental features:
- Accessing USDC token configuration
- Validating Starknet addresses
- Formatting USDC amounts
- Querying wallet balances

**Run:**
```bash
python3 examples/starknet/basic_usage.py
```

### 2. CCTP Messaging (`cctp_messaging.py`)

Shows Cross-Chain Transfer Protocol (CCTP) functionality:
- Getting CCTP contract addresses
- Preparing cross-chain messages
- Setting up token minting operations
- Checking message status
- Understanding the complete transfer flow

**Run:**
```bash
python3 examples/starknet/cctp_messaging.py
```

### 3. Faucet Usage (`faucet_usage.py`)

Explains how to use Circle's USDC faucet:
- Getting faucet information
- Formatting faucet requests
- Step-by-step usage guide
- Testing multiple addresses

**Run:**
```bash
python3 examples/starknet/faucet_usage.py
```

## Prerequisites

These examples require the `supabase` package with Starknet integration. If running from the repository:

```bash
# From repository root
cd /path/to/supabase-py
python3 examples/starknet/basic_usage.py
```

## Quick Start

1. **Get Test Tokens:**
   Visit [Circle's Faucet](https://faucet.circle.com) to obtain free testnet USDC

2. **Run Basic Example:**
   ```bash
   python3 examples/starknet/basic_usage.py
   ```

3. **Explore CCTP:**
   ```bash
   python3 examples/starknet/cctp_messaging.py
   ```

4. **Learn About Faucet:**
   ```bash
   python3 examples/starknet/faucet_usage.py
   ```

## Integration with Supabase

These examples can be integrated with Supabase workflows:

```python
import supabase
from supabase.starknet import get_usdc_balance, STARKNET_USDC_TOKEN_ADDRESS

# Initialize Supabase client
client = supabase.create_client("your-url", "your-key")

# Query and store balance
wallet = "0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343"
balance = get_usdc_balance(wallet)

client.table("balances").insert({
    "wallet": wallet,
    "token": STARKNET_USDC_TOKEN_ADDRESS,
    "balance": balance['balance_raw'],
}).execute()
```

## Resources

- [Starknet Integration Documentation](../../docs/starknet_integration.md)
- [Circle USDC Faucet](https://faucet.circle.com)
- [Starknet Documentation](https://docs.starknet.io)
- [Circle CCTP Documentation](https://developers.circle.com/stablecoin/docs/cctp-getting-started)

## Notes

- These examples use **testnet addresses** and have no real monetary value
- Some functions are **placeholders** and require a Starknet RPC provider for production use
- Examples are designed to be educational and demonstrate the API structure
