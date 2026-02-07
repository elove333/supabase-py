"""
Utility functions for Starknet USDC integration.

This module provides helper functions for interacting with USDC on Starknet,
including balance queries, address validation, and amount formatting.
"""

from typing import Optional

from .config import USDC_DECIMALS


def validate_starknet_address(address: str) -> bool:
    """
    Validate a Starknet address format.

    Args:
        address: The Starknet address to validate (hex string starting with 0x)

    Returns:
        True if the address is valid, False otherwise

    Examples:
        >>> validate_starknet_address("0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343")
        True
        >>> validate_starknet_address("invalid")
        False
    """
    if not isinstance(address, str):
        return False

    if not address.startswith("0x"):
        return False

    # Starknet addresses are hex strings, typically 66 characters (0x + 64 hex digits)
    # but can be shorter if leading zeros are omitted
    try:
        int(address, 16)
        return len(address) >= 3 and len(address) <= 66
    except ValueError:
        return False


def format_usdc_amount(amount: int, decimals: int = USDC_DECIMALS) -> str:
    """
    Format a USDC amount from its smallest unit to a human-readable string.

    Args:
        amount: The amount in the smallest unit (e.g., micro-USDC)
        decimals: The number of decimal places (default: 6 for USDC)

    Returns:
        A formatted string representation of the amount

    Examples:
        >>> format_usdc_amount(1000000)
        '1.000000'
        >>> format_usdc_amount(1500000)
        '1.500000'
    """
    divisor = 10**decimals
    whole = amount // divisor
    fractional = amount % divisor
    return f"{whole}.{fractional:0{decimals}d}"


def get_usdc_balance(address: str, provider_url: Optional[str] = None) -> dict:
    """
    Query USDC balance for a Starknet address.

    This is a placeholder function that demonstrates how to structure balance queries.
    In a production environment, this would connect to a Starknet RPC provider
    to fetch the actual balance.

    Args:
        address: The Starknet wallet address to query
        provider_url: Optional RPC provider URL. If None, uses default testnet provider

    Returns:
        A dictionary containing balance information:
        {
            "address": str,
            "balance_raw": int,  # Raw balance in smallest unit
            "balance_formatted": str,  # Human-readable balance
            "token": str,
            "network": str
        }

    Raises:
        ValueError: If the address format is invalid

    Examples:
        >>> result = get_usdc_balance("0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343")
        >>> print(result["token"])
        'USDC'
    """
    if not validate_starknet_address(address):
        raise ValueError(f"Invalid Starknet address format: {address}")

    # Placeholder implementation
    # In production, this would query the Starknet blockchain
    # using a library like starknet.py or via RPC calls
    return {
        "address": address,
        "balance_raw": 0,
        "balance_formatted": format_usdc_amount(0),
        "token": "USDC",
        "network": "starknet-testnet",
        "note": "This is a placeholder. Implement actual RPC call to fetch real balance.",
    }
