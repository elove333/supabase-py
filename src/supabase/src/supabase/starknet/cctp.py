"""
CCTP (Cross-Chain Transfer Protocol) Integration.

This module provides functions for interacting with Circle's CCTP contracts
on Starknet testnet, enabling cross-chain messaging and token transfers.
"""

from typing import Any, Dict, Optional

from .config import (
    CCTP_MESSAGE_TRANSMITTER_ADDRESS,
    CCTP_MESSAGE_V2_ADDRESS,
    CCTP_TOKEN_MESSENGER_ADDRESS,
    CCTP_TOKEN_MINTER_ADDRESS,
)
from .utils import validate_starknet_address


def get_cctp_contracts() -> Dict[str, str]:
    """
    Get all CCTP testnet contract addresses.

    Returns:
        Dictionary mapping contract names to their addresses on Starknet testnet

    Examples:
        >>> contracts = get_cctp_contracts()
        >>> print(contracts["TokenMessengerV2"])
        '0x04bDdE1E09a4B09a2F95d893D94a967b7717eB85A3f6dEcA8c080Ee01fBc3370'
    """
    return {
        "TokenMessengerV2": CCTP_TOKEN_MESSENGER_ADDRESS,
        "MessageTransmitterV2": CCTP_MESSAGE_TRANSMITTER_ADDRESS,
        "TokenMinterV2": CCTP_TOKEN_MINTER_ADDRESS,
        "MessageV2": CCTP_MESSAGE_V2_ADDRESS,
    }


def prepare_send_message(
    destination_domain: int,
    recipient: str,
    message_body: bytes,
    sender: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Prepare a cross-chain message to be sent via CCTP.

    This is a helper function that structures the parameters for sending
    a message through the MessageTransmitter contract.

    Args:
        destination_domain: The destination domain identifier
        recipient: The recipient address on the destination chain
        message_body: The message payload as bytes
        sender: Optional sender address for verification

    Returns:
        Dictionary containing the prepared message parameters

    Raises:
        ValueError: If recipient address is invalid

    Examples:
        >>> msg = prepare_send_message(
        ...     destination_domain=0,
        ...     recipient="0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb",
        ...     message_body=b"Hello"
        ... )
        >>> print(msg["destination_domain"])
        0
    """
    if sender and not validate_starknet_address(sender):
        raise ValueError(f"Invalid sender address: {sender}")

    return {
        "destination_domain": destination_domain,
        "recipient": recipient,
        "message_body": message_body,
        "sender": sender,
        "message_transmitter": CCTP_MESSAGE_TRANSMITTER_ADDRESS,
        "note": "Use this structure with Starknet contract interaction library",
    }


def prepare_mint_tokens(
    amount: int, destination_address: str, mint_recipient: str
) -> Dict[str, Any]:
    """
    Prepare parameters for minting tokens via TokenMinter contract.

    Args:
        amount: Amount of tokens to mint (in smallest unit)
        destination_address: The destination address to receive tokens
        mint_recipient: The address authorized to receive the mint

    Returns:
        Dictionary containing the mint parameters

    Raises:
        ValueError: If addresses are invalid or amount is non-positive

    Examples:
        >>> params = prepare_mint_tokens(
        ...     amount=1000000,
        ...     destination_address="0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343",
        ...     mint_recipient="0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343"
        ... )
        >>> print(params["amount"])
        1000000
    """
    if amount <= 0:
        raise ValueError(f"Amount must be positive, got: {amount}")

    if not validate_starknet_address(destination_address):
        raise ValueError(f"Invalid destination address: {destination_address}")

    if not validate_starknet_address(mint_recipient):
        raise ValueError(f"Invalid mint recipient address: {mint_recipient}")

    return {
        "amount": amount,
        "destination_address": destination_address,
        "mint_recipient": mint_recipient,
        "token_minter": CCTP_TOKEN_MINTER_ADDRESS,
        "note": "Use this structure with Starknet contract interaction library",
    }


def get_message_status(message_hash: str) -> Dict[str, Any]:
    """
    Get the status of a cross-chain message.

    This is a placeholder for querying message status from the
    MessageTransmitter contract.

    Args:
        message_hash: The hash of the message to query

    Returns:
        Dictionary containing message status information

    Examples:
        >>> status = get_message_status("0xabc123...")
        >>> print(status["status"])
        'pending'
    """
    return {
        "message_hash": message_hash,
        "status": "pending",
        "transmitter_address": CCTP_MESSAGE_TRANSMITTER_ADDRESS,
        "note": "Implement actual contract query to get real status",
    }
