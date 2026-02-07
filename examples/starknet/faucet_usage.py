#!/usr/bin/env python3
"""
Example: Using Circle's USDC Faucet

This script demonstrates how to use Circle's faucet to obtain test USDC
tokens on Starknet testnet for development purposes.
"""

import sys
from pathlib import Path

# Add src to path for direct execution
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src" / "supabase" / "src"))

# Import directly from starknet module to avoid full supabase dependencies
from supabase.starknet.config import USDC_FAUCET_URL
from supabase.starknet.faucet import (
    format_faucet_request,
    get_faucet_info,
    get_faucet_usage_guide,
)
from supabase.starknet.utils import validate_starknet_address


def main():
    """Run faucet usage examples."""
    print("=" * 60)
    print("Circle USDC Faucet - Usage Example")
    print("=" * 60)

    # Example 1: Get Faucet Information
    print("\n1. Faucet Information:")
    faucet_info = get_faucet_info()

    print(f"   Name: {faucet_info['name']}")
    print(f"   URL: {faucet_info['url']}")
    print(f"   Description: {faucet_info['description']}")
    print(f"   Network: {faucet_info['network']}")
    print(f"   Token: {faucet_info['token']}")

    # Example 2: Format Faucet Request
    print("\n2. Format Faucet Request:")
    wallet_address = "0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343"

    if validate_starknet_address(wallet_address):
        request = format_faucet_request(wallet_address)

        print(f"   Wallet Address: {request['wallet_address']}")
        print(f"   Faucet URL: {request['faucet_url']}")
        print(f"   Network: {request['network']}")
        print("\n   Instructions:")
        for line in request['instructions'].split('\n'):
            if line.strip():
                print(f"   {line}")
    else:
        print(f"   Invalid wallet address: {wallet_address}")

    # Example 3: Get Detailed Usage Guide
    print("\n3. Detailed Usage Guide:")
    print("   Getting the full usage guide...")
    guide = get_faucet_usage_guide()

    # Print first few lines of the guide
    guide_lines = guide.strip().split('\n')
    for i, line in enumerate(guide_lines[:15]):
        print(f"   {line}")

    print(f"   ... ({len(guide_lines) - 15} more lines)")

    # Example 4: Quick Start Guide
    print("\n4. Quick Start Guide:")
    print("   Step 1: Prepare Your Wallet")
    print("           - Set up a Starknet testnet wallet")
    print("           - Note your wallet address (starts with 0x)")
    print()
    print("   Step 2: Visit the Faucet")
    print(f"           - Navigate to: {USDC_FAUCET_URL}")
    print()
    print("   Step 3: Request Tokens")
    print("           - Connect your wallet or paste your address")
    print("           - Click 'Request Tokens'")
    print("           - Complete any verification if required")
    print()
    print("   Step 4: Verify Receipt")
    print("           - Wait for transaction confirmation")
    print("           - Check your wallet balance")
    print("           - Use get_usdc_balance() to verify programmatically")

    # Example 5: Testing with Multiple Addresses
    print("\n5. Testing Multiple Addresses:")
    test_addresses = [
        "0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343",
        "0x04bDdE1E09a4B09a2F95d893D94a967b7717eB85A3f6dEcA8c080Ee01fBc3370",
        "invalid_address",
    ]

    for addr in test_addresses:
        is_valid = validate_starknet_address(addr)
        addr_display = addr[:30] + "..." if len(addr) > 30 else addr
        status = "✓ Can request tokens" if is_valid else "✗ Invalid address"
        print(f"   {addr_display:35} {status}")

    print("\n" + "=" * 60)
    print("Faucet Example completed successfully!")
    print("=" * 60)
    print(f"\nVisit {USDC_FAUCET_URL} to get test tokens!")


if __name__ == "__main__":
    main()
