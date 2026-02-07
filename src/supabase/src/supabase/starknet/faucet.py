"""
Faucet utilities for obtaining testnet USDC tokens.

This module provides information and helper functions for using Circle's
USDC faucet to obtain test tokens on Starknet testnet.
"""

from typing import Dict

from .config import USDC_FAUCET_URL


def get_faucet_info() -> Dict[str, str]:
    """
    Get information about Circle's USDC faucet.

    Returns:
        Dictionary containing faucet information including URL and instructions

    Examples:
        >>> info = get_faucet_info()
        >>> print(info["url"])
        'https://faucet.circle.com'
    """
    return {
        "url": USDC_FAUCET_URL,
        "name": "Circle USDC Faucet",
        "description": "Free testnet USDC tokens for Starknet developers",
        "instructions": "Visit the faucet URL and connect your Starknet testnet wallet to receive free USDC tokens for testing",
        "network": "Starknet Testnet",
        "token": "USDC",
    }


def format_faucet_request(wallet_address: str) -> Dict[str, str]:
    """
    Format a faucet request with the provided wallet address.

    Args:
        wallet_address: The Starknet testnet wallet address to receive tokens

    Returns:
        Dictionary containing formatted faucet request information

    Examples:
        >>> request = format_faucet_request("0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343")
        >>> print(request["wallet_address"])
        '0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343'
    """
    return {
        "wallet_address": wallet_address,
        "faucet_url": USDC_FAUCET_URL,
        "network": "starknet-testnet",
        "instructions": f"1. Visit {USDC_FAUCET_URL}\n2. Connect your wallet or enter address: {wallet_address}\n3. Request testnet USDC tokens\n4. Wait for transaction confirmation",
    }


def get_faucet_usage_guide() -> str:
    """
    Get a detailed guide on how to use the Circle USDC faucet.

    Returns:
        String containing step-by-step instructions for using the faucet

    Examples:
        >>> guide = get_faucet_usage_guide()
        >>> print("Step 1" in guide)
        True
    """
    return f"""
Circle USDC Faucet Usage Guide
==============================

The Circle USDC Faucet provides free testnet USDC tokens for developers
building on Starknet testnet.

How to Use:
-----------

Step 1: Prepare Your Wallet
   - Ensure you have a Starknet testnet wallet configured
   - Note your wallet address (starts with 0x)

Step 2: Visit the Faucet
   - Navigate to {USDC_FAUCET_URL}
   - The faucet supports Starknet testnet

Step 3: Request Tokens
   - Connect your wallet OR paste your testnet address
   - Click the "Request Tokens" or similar button
   - Complete any verification (if required)

Step 4: Confirm Receipt
   - Wait for the transaction to be confirmed on Starknet testnet
   - Check your wallet balance to verify receipt
   - You can use the get_usdc_balance() function to check programmatically

Important Notes:
----------------
- These are testnet tokens with no real value
- There may be rate limits on faucet requests
- Tokens are only available on Starknet testnet
- For production, use real USDC on Starknet mainnet

Token Details:
--------------
Token Name: USDC
Token Symbol: USDC
Decimals: 6
Testnet Address: 0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343

For more information, visit the official Circle documentation.
"""
