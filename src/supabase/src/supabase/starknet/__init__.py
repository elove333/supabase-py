"""
Starknet USDC Testnet Integration Module.

This module provides integration with Circle's Native USDC on Starknet testnet
and CCTP (Cross-Chain Transfer Protocol) functionality.
"""

from .cctp import (
    get_cctp_contracts,
    get_message_status,
    prepare_mint_tokens,
    prepare_send_message,
)
from .config import (
    CCTP_MESSAGE_TRANSMITTER_ADDRESS,
    CCTP_MESSAGE_V2_ADDRESS,
    CCTP_TOKEN_MESSENGER_ADDRESS,
    CCTP_TOKEN_MINTER_ADDRESS,
    STARKNET_USDC_TOKEN_ADDRESS,
    USDC_DECIMALS,
    USDC_FAUCET_URL,
    USDC_SYMBOL,
    USDC_TOKEN_NAME,
)
from .faucet import (
    format_faucet_request,
    get_faucet_info,
    get_faucet_usage_guide,
)
from .utils import (
    format_usdc_amount,
    get_usdc_balance,
    validate_starknet_address,
)

__all__ = [
    # Constants
    "STARKNET_USDC_TOKEN_ADDRESS",
    "USDC_TOKEN_NAME",
    "USDC_SYMBOL",
    "USDC_DECIMALS",
    "USDC_FAUCET_URL",
    "CCTP_TOKEN_MESSENGER_ADDRESS",
    "CCTP_MESSAGE_TRANSMITTER_ADDRESS",
    "CCTP_TOKEN_MINTER_ADDRESS",
    "CCTP_MESSAGE_V2_ADDRESS",
    # Utility functions
    "get_usdc_balance",
    "validate_starknet_address",
    "format_usdc_amount",
    # CCTP functions
    "get_cctp_contracts",
    "prepare_send_message",
    "prepare_mint_tokens",
    "get_message_status",
    # Faucet functions
    "get_faucet_info",
    "format_faucet_request",
    "get_faucet_usage_guide",
]
