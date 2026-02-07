# Starknet USDC Integration

This document describes the Starknet USDC testnet integration in the `supabase-py` library, which enables developers to work with Circle's Native USDC on Starknet and utilize Cross-Chain Transfer Protocol (CCTP) functionality.

## Overview

The Starknet integration adds support for:

1. **Native USDC on Starknet Testnet** - Track and interact with Circle-issued USDC
2. **CCTP (Cross-Chain Transfer Protocol)** - Cross-chain messaging and token transfers
3. **Testnet Faucet** - Easy access to test tokens for development

## Installation

The Starknet module is included with the main `supabase` package:

```python
from supabase.starknet import (
    STARKNET_USDC_TOKEN_ADDRESS,
    get_usdc_balance,
    get_cctp_contracts,
    get_faucet_info,
)
```

## Configuration

### USDC Token Details

- **Token Name:** USDC
- **Token Symbol:** USDC
- **Decimals:** 6
- **Testnet Token Address:** `0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343`

### CCTP Contract Addresses (Testnet)

- **TokenMessengerV2:** `0x04bDdE1E09a4B09a2F95d893D94a967b7717eB85A3f6dEcA8c080Ee01fBc3370`
- **MessageTransmitterV2:** `0x04db7926C64f1f32a840F3Fa95cB551f3801a3600Bae87aF87807A54DCE12Fe8`
- **TokenMinterV2:** `0x04bDdE1E09a4B09a2F95d893D94a967b7717eB85A3f6dEcA8c080Ee01fBc3370`
- **MessageV2:** `0x04db7926C64f1f32a840F3Fa95cB551f3801a3600Bae87aF87807A54DCE12Fe8`

## Usage Examples

### 1. Accessing Configuration

```python
from supabase.starknet import (
    STARKNET_USDC_TOKEN_ADDRESS,
    USDC_TOKEN_NAME,
    USDC_SYMBOL,
    USDC_DECIMALS,
)

print(f"Token: {USDC_TOKEN_NAME} ({USDC_SYMBOL})")
print(f"Decimals: {USDC_DECIMALS}")
print(f"Address: {STARKNET_USDC_TOKEN_ADDRESS}")
```

### 2. Validating Starknet Addresses

```python
from supabase.starknet import validate_starknet_address

address = "0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343"
if validate_starknet_address(address):
    print("Valid Starknet address")
else:
    print("Invalid address")
```

### 3. Formatting USDC Amounts

```python
from supabase.starknet import format_usdc_amount

# Amount in smallest unit (micro-USDC)
raw_amount = 1500000  # 1.5 USDC
formatted = format_usdc_amount(raw_amount)
print(f"Balance: {formatted} USDC")  # Output: Balance: 1.500000 USDC
```

### 4. Querying USDC Balance

```python
from supabase.starknet import get_usdc_balance

wallet_address = "0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343"
balance_info = get_usdc_balance(wallet_address)

print(f"Address: {balance_info['address']}")
print(f"Balance: {balance_info['balance_formatted']} {balance_info['token']}")
print(f"Network: {balance_info['network']}")
```

**Note:** The `get_usdc_balance` function is currently a placeholder. For production use, integrate with a Starknet RPC provider to fetch actual balances.

### 5. Working with CCTP Contracts

```python
from supabase.starknet import get_cctp_contracts

# Get all CCTP contract addresses
contracts = get_cctp_contracts()
print(f"TokenMessenger: {contracts['TokenMessengerV2']}")
print(f"MessageTransmitter: {contracts['MessageTransmitterV2']}")
```

### 6. Preparing Cross-Chain Messages

```python
from supabase.starknet import prepare_send_message

# Prepare a message for cross-chain transfer
message_params = prepare_send_message(
    destination_domain=0,
    recipient="0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb",
    message_body=b"Transfer initiated",
    sender="0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343"
)

print(f"Destination Domain: {message_params['destination_domain']}")
print(f"Message Transmitter: {message_params['message_transmitter']}")
```

### 7. Preparing Token Minting

```python
from supabase.starknet import prepare_mint_tokens

# Prepare parameters for minting tokens
mint_params = prepare_mint_tokens(
    amount=1000000,  # 1 USDC
    destination_address="0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343",
    mint_recipient="0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343"
)

print(f"Amount: {mint_params['amount']}")
print(f"Token Minter: {mint_params['token_minter']}")
```

### 8. Using the USDC Faucet

```python
from supabase.starknet import get_faucet_info, get_faucet_usage_guide

# Get faucet information
faucet_info = get_faucet_info()
print(f"Faucet URL: {faucet_info['url']}")
print(f"Description: {faucet_info['description']}")

# Get detailed usage guide
guide = get_faucet_usage_guide()
print(guide)
```

### 9. Formatting Faucet Requests

```python
from supabase.starknet import format_faucet_request

wallet = "0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343"
request = format_faucet_request(wallet)

print(request['instructions'])
```

## Complete Example: Wallet Setup and Testing

Here's a complete example showing how to set up a wallet for Starknet testnet development:

```python
from supabase.starknet import (
    validate_starknet_address,
    get_usdc_balance,
    get_faucet_info,
    format_usdc_amount,
    get_cctp_contracts,
)

# Your Starknet testnet wallet address
wallet_address = "0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343"

# Step 1: Validate the address
if not validate_starknet_address(wallet_address):
    print("Invalid wallet address!")
    exit(1)

print(f"✓ Valid wallet address: {wallet_address}")

# Step 2: Get faucet information to obtain test tokens
faucet_info = get_faucet_info()
print(f"\n📝 Get test tokens from: {faucet_info['url']}")
print(f"   {faucet_info['description']}")

# Step 3: Check USDC balance
balance = get_usdc_balance(wallet_address)
print(f"\n💰 Current Balance: {balance['balance_formatted']} {balance['token']}")
print(f"   Network: {balance['network']}")

# Step 4: Get CCTP contract addresses for cross-chain operations
contracts = get_cctp_contracts()
print(f"\n🔗 CCTP Contracts:")
for name, address in contracts.items():
    print(f"   {name}: {address}")

# Example: Format an amount
raw_amount = 5000000  # 5 USDC in smallest unit
formatted = format_usdc_amount(raw_amount)
print(f"\n📊 Example: {raw_amount} micro-USDC = {formatted} USDC")
```

## Integration with Supabase Workflows

The Starknet integration can be used alongside other Supabase features:

```python
import supabase
from supabase.starknet import get_usdc_balance, STARKNET_USDC_TOKEN_ADDRESS

# Initialize Supabase client
client = supabase.create_client("your-supabase-url", "your-supabase-key")

# Query USDC balance
wallet_address = "0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343"
balance = get_usdc_balance(wallet_address)

# Store balance information in Supabase
client.table("wallet_balances").insert({
    "wallet_address": wallet_address,
    "token_address": STARKNET_USDC_TOKEN_ADDRESS,
    "balance": balance['balance_raw'],
    "balance_formatted": balance['balance_formatted'],
    "network": balance['network'],
}).execute()
```

## Benefits

1. **Native USDC Support** - Work with Circle's official USDC on Starknet
2. **Cross-Chain Ready** - CCTP integration enables cross-chain messaging
3. **Developer-Friendly** - Easy access to testnet tokens via faucet
4. **Type-Safe** - Well-documented types and validation functions
5. **Integration-Ready** - Works seamlessly with Supabase workflows

## Important Notes

- **Testnet Only**: These addresses and functions are for Starknet testnet
- **Placeholder Functions**: Some functions like `get_usdc_balance` are placeholders that demonstrate structure but require a Starknet RPC provider for production use
- **No Real Value**: Testnet tokens have no monetary value
- **Rate Limits**: Faucets may have rate limits on token requests

## Next Steps

To use these features in production:

1. Integrate a Starknet RPC provider (e.g., via `starknet.py`)
2. Implement actual contract calls in place of placeholder functions
3. Add error handling and retry logic
4. Consider using Starknet mainnet addresses for production

## Resources

- [Circle USDC Faucet](https://faucet.circle.com)
- [Starknet Documentation](https://docs.starknet.io)
- [Circle CCTP Documentation](https://developers.circle.com/stablecoin/docs/cctp-getting-started)
- [Supabase Documentation](https://supabase.com/docs)

## Support

For issues or questions:
- GitHub Issues: [supabase-py repository](https://github.com/supabase/supabase-py)
- Supabase Discord: [Join the community](https://discord.supabase.com)
