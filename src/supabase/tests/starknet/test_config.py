"""Tests for Starknet configuration module."""


from supabase.starknet.config import (
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


def test_usdc_token_constants():
    """Test USDC token configuration constants."""
    assert USDC_TOKEN_NAME == "USDC"
    assert USDC_SYMBOL == "USDC"
    assert USDC_DECIMALS == 6


def test_starknet_usdc_address():
    """Test that USDC token address is properly formatted."""
    assert STARKNET_USDC_TOKEN_ADDRESS.startswith("0x")
    assert len(STARKNET_USDC_TOKEN_ADDRESS) == 66
    assert (
        STARKNET_USDC_TOKEN_ADDRESS
        == "0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343"
    )


def test_cctp_contract_addresses():
    """Test that CCTP contract addresses are properly formatted."""
    addresses = [
        CCTP_TOKEN_MESSENGER_ADDRESS,
        CCTP_MESSAGE_TRANSMITTER_ADDRESS,
        CCTP_TOKEN_MINTER_ADDRESS,
        CCTP_MESSAGE_V2_ADDRESS,
    ]

    for addr in addresses:
        assert addr.startswith("0x")
        assert len(addr) == 66


def test_cctp_token_messenger_address():
    """Test TokenMessengerV2 address."""
    assert (
        CCTP_TOKEN_MESSENGER_ADDRESS
        == "0x04bDdE1E09a4B09a2F95d893D94a967b7717eB85A3f6dEcA8c080Ee01fBc3370"
    )


def test_cctp_message_transmitter_address():
    """Test MessageTransmitterV2 address."""
    assert (
        CCTP_MESSAGE_TRANSMITTER_ADDRESS
        == "0x04db7926C64f1f32a840F3Fa95cB551f3801a3600Bae87aF87807A54DCE12Fe8"
    )


def test_cctp_token_minter_address():
    """Test TokenMinterV2 address."""
    assert (
        CCTP_TOKEN_MINTER_ADDRESS
        == "0x04bDdE1E09a4B09a2F95d893D94a967b7717eB85A3f6dEcA8c080Ee01fBc3370"
    )


def test_cctp_message_v2_address():
    """Test MessageV2 address."""
    assert (
        CCTP_MESSAGE_V2_ADDRESS
        == "0x04db7926C64f1f32a840F3Fa95cB551f3801a3600Bae87aF87807A54DCE12Fe8"
    )


def test_faucet_url():
    """Test faucet URL is properly configured."""
    assert USDC_FAUCET_URL == "https://faucet.circle.com"
    assert USDC_FAUCET_URL.startswith("https://")
