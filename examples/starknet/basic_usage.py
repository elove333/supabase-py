#!/usr/bin/env python3
"""
Example: Basic Starknet USDC Integration

This script demonstrates basic usage of the Starknet USDC integration,
including address validation, balance queries, and configuration access.
"""

import sys
from pathlib import Path

# Add src to path for direct execution
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src" / "supabase" / "src"))

# Import directly from starknet module to avoid full supabase dependencies
from supabase.starknet.config import (
    STARKNET_USDC_TOKEN_ADDRESS,
    USDC_DECIMALS,
    USDC_SYMBOL,
    USDC_TOKEN_NAME,
)
from supabase.starknet.utils import (
    format_usdc_amount,
    get_usdc_balance,
    validate_starknet_address,
)


def main():
    """Run basic Starknet integration examples."""
    print("=" * 60)
    print("Starknet USDC Integration - Basic Example")
    print("=" * 60)

    # Example 1: Token Configuration
    print("\n1. Token Configuration:")
    print(f"   Token Name: {USDC_TOKEN_NAME}")
    print(f"   Token Symbol: {USDC_SYMBOL}")
    print(f"   Decimals: {USDC_DECIMALS}")
    print(f"   Testnet Address: {STARKNET_USDC_TOKEN_ADDRESS}")

    # Example 2: Address Validation
    print("\n2. Address Validation:")
    test_address = STARKNET_USDC_TOKEN_ADDRESS
    is_valid = validate_starknet_address(test_address)
    print(f"   Testing address: {test_address[:20]}...")
    print(f"   Valid: {is_valid} ✓" if is_valid else f"   Valid: {is_valid} ✗")

    # Test invalid address
    invalid_address = "not_a_valid_address"
    is_valid = validate_starknet_address(invalid_address)
    print(f"   Testing invalid address: {invalid_address}")
    print(f"   Valid: {is_valid} ✓" if is_valid else f"   Valid: {is_valid} ✗")

    # Example 3: Amount Formatting
    print("\n3. Amount Formatting:")
    test_amounts = [
        (1000000, "1 USDC"),
        (1500000, "1.5 USDC"),
        (500000, "0.5 USDC"),
        (123456, "0.123456 USDC"),
    ]

    for raw_amount, description in test_amounts:
        formatted = format_usdc_amount(raw_amount)
        print(f"   {raw_amount:>10} micro-USDC = {formatted} ({description})")

    # Example 4: Balance Query
    print("\n4. Balance Query:")
    wallet_address = "0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343"
    print(f"   Querying balance for: {wallet_address[:20]}...")

    try:
        balance_info = get_usdc_balance(wallet_address)
        print(f"   Token: {balance_info['token']}")
        print(f"   Network: {balance_info['network']}")
        print(f"   Balance: {balance_info['balance_formatted']} {balance_info['token']}")
        print(f"   Note: {balance_info.get('note', 'N/A')}")
    except ValueError as e:
        print(f"   Error: {e}")

    print("\n" + "=" * 60)
    print("Example completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
