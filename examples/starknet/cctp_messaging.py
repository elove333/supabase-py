#!/usr/bin/env python3
"""
Example: CCTP Cross-Chain Messaging

This script demonstrates how to use Circle's Cross-Chain Transfer Protocol (CCTP)
functionality for cross-chain messaging and token transfers on Starknet.
"""

import sys
from pathlib import Path

# Add src to path for direct execution
sys.path.insert(
    0, str(Path(__file__).parent.parent.parent / "src" / "supabase" / "src")
)

# Import directly from starknet module to avoid full supabase dependencies
from supabase.starknet.cctp import (
    get_cctp_contracts,
    get_message_status,
    prepare_mint_tokens,
    prepare_send_message,
)
from supabase.starknet.config import (
    CCTP_MESSAGE_TRANSMITTER_ADDRESS,
    CCTP_TOKEN_MESSENGER_ADDRESS,
    CCTP_TOKEN_MINTER_ADDRESS,
)


def main():
    """Run CCTP integration examples."""
    print("=" * 60)
    print("CCTP (Cross-Chain Transfer Protocol) Example")
    print("=" * 60)

    # Example 1: Get CCTP Contract Addresses
    print("\n1. CCTP Contract Addresses:")
    contracts = get_cctp_contracts()
    for name, address in contracts.items():
        print(f"   {name:25} {address}")

    # Example 2: Prepare Cross-Chain Message
    print("\n2. Prepare Cross-Chain Message:")
    sender_address = (
        "0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343"
    )
    recipient_address = "0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb"

    message_params = prepare_send_message(
        destination_domain=0,
        recipient=recipient_address,
        message_body=b"Hello from Starknet!",
        sender=sender_address,
    )

    print(f"   Destination Domain: {message_params['destination_domain']}")
    print(f"   Recipient: {message_params['recipient']}")
    print(f"   Message Body: {message_params['message_body']}")
    print(f"   Sender: {message_params['sender'][:20]}...")
    print(f"   Message Transmitter: {message_params['message_transmitter'][:20]}...")
    print(f"   Note: {message_params['note']}")

    # Example 3: Prepare Token Minting
    print("\n3. Prepare Token Minting:")
    mint_amount = 1000000  # 1 USDC
    destination = "0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343"

    try:
        mint_params = prepare_mint_tokens(
            amount=mint_amount,
            destination_address=destination,
            mint_recipient=destination,
        )

        print(f"   Amount: {mint_params['amount']} micro-USDC (1 USDC)")
        print(f"   Destination: {mint_params['destination_address'][:20]}...")
        print(f"   Mint Recipient: {mint_params['mint_recipient'][:20]}...")
        print(f"   Token Minter: {mint_params['token_minter'][:20]}...")
        print(f"   Note: {mint_params['note']}")
    except ValueError as e:
        print(f"   Error: {e}")

    # Example 4: Check Message Status
    print("\n4. Message Status Query:")
    sample_message_hash = "0xabc123def456789"
    status = get_message_status(sample_message_hash)

    print(f"   Message Hash: {status['message_hash']}")
    print(f"   Status: {status['status']}")
    print(f"   Transmitter: {status['transmitter_address'][:20]}...")
    print(f"   Note: {status['note']}")

    # Example 5: Complete Cross-Chain Transfer Flow
    print("\n5. Complete Cross-Chain Transfer Flow:")
    print("   Step 1: Prepare message with TokenMessenger")
    print(f"           Contract: {CCTP_TOKEN_MESSENGER_ADDRESS[:20]}...")

    print("   Step 2: Sign and send message via MessageTransmitter")
    print(f"           Contract: {CCTP_MESSAGE_TRANSMITTER_ADDRESS[:20]}...")

    print("   Step 3: Receive attestation from Circle")
    print("           (Attestation service validates the message)")

    print("   Step 4: Mint tokens on destination chain via TokenMinter")
    print(f"           Contract: {CCTP_TOKEN_MINTER_ADDRESS[:20]}...")

    print("\n   Note: This is a conceptual flow. In production, each step")
    print("         requires actual contract calls using a Starknet SDK.")

    print("\n" + "=" * 60)
    print("CCTP Example completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
