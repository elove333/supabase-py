"""Tests for Starknet CCTP module."""

import pytest

from supabase.starknet.cctp import (
    get_cctp_contracts,
    get_message_status,
    prepare_mint_tokens,
    prepare_send_message,
)
from supabase.starknet.config import (
    CCTP_MESSAGE_TRANSMITTER_ADDRESS,
    CCTP_MESSAGE_V2_ADDRESS,
    CCTP_TOKEN_MESSENGER_ADDRESS,
    CCTP_TOKEN_MINTER_ADDRESS,
)


class TestGetCctpContracts:
    """Tests for get_cctp_contracts function."""

    def test_returns_all_contracts(self):
        """Test that all CCTP contracts are returned."""
        contracts = get_cctp_contracts()

        assert "TokenMessengerV2" in contracts
        assert "MessageTransmitterV2" in contracts
        assert "TokenMinterV2" in contracts
        assert "MessageV2" in contracts

    def test_contract_addresses_match_config(self):
        """Test that returned addresses match configuration."""
        contracts = get_cctp_contracts()

        assert contracts["TokenMessengerV2"] == CCTP_TOKEN_MESSENGER_ADDRESS
        assert contracts["MessageTransmitterV2"] == CCTP_MESSAGE_TRANSMITTER_ADDRESS
        assert contracts["TokenMinterV2"] == CCTP_TOKEN_MINTER_ADDRESS
        assert contracts["MessageV2"] == CCTP_MESSAGE_V2_ADDRESS


class TestPrepareSendMessage:
    """Tests for prepare_send_message function."""

    def test_prepare_message_without_sender(self):
        """Test preparing message without sender."""
        result = prepare_send_message(
            destination_domain=0,
            recipient="0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb",
            message_body=b"Hello",
        )

        assert result["destination_domain"] == 0
        assert result["recipient"] == "0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb"
        assert result["message_body"] == b"Hello"
        assert result["message_transmitter"] == CCTP_MESSAGE_TRANSMITTER_ADDRESS

    def test_prepare_message_with_sender(self):
        """Test preparing message with sender."""
        sender = "0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343"
        result = prepare_send_message(
            destination_domain=1,
            recipient="0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb",
            message_body=b"Transfer",
            sender=sender,
        )

        assert result["sender"] == sender
        assert result["destination_domain"] == 1

    def test_prepare_message_invalid_sender(self):
        """Test that invalid sender address raises ValueError."""
        with pytest.raises(ValueError, match="Invalid sender address"):
            prepare_send_message(
                destination_domain=0,
                recipient="0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb",
                message_body=b"Hello",
                sender="invalid_address",
            )


class TestPrepareMintTokens:
    """Tests for prepare_mint_tokens function."""

    def test_prepare_mint_valid_params(self):
        """Test preparing mint with valid parameters."""
        result = prepare_mint_tokens(
            amount=1000000,
            destination_address="0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343",
            mint_recipient="0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343",
        )

        assert result["amount"] == 1000000
        assert (
            result["destination_address"]
            == "0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343"
        )
        assert result["token_minter"] == CCTP_TOKEN_MINTER_ADDRESS

    def test_prepare_mint_zero_amount(self):
        """Test that zero amount raises ValueError."""
        with pytest.raises(ValueError, match="Amount must be positive"):
            prepare_mint_tokens(
                amount=0,
                destination_address="0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343",
                mint_recipient="0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343",
            )

    def test_prepare_mint_negative_amount(self):
        """Test that negative amount raises ValueError."""
        with pytest.raises(ValueError, match="Amount must be positive"):
            prepare_mint_tokens(
                amount=-1000,
                destination_address="0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343",
                mint_recipient="0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343",
            )

    def test_prepare_mint_invalid_destination(self):
        """Test that invalid destination address raises ValueError."""
        with pytest.raises(ValueError, match="Invalid destination address"):
            prepare_mint_tokens(
                amount=1000000,
                destination_address="invalid_address",
                mint_recipient="0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343",
            )

    def test_prepare_mint_invalid_recipient(self):
        """Test that invalid mint recipient address raises ValueError."""
        with pytest.raises(ValueError, match="Invalid mint recipient address"):
            prepare_mint_tokens(
                amount=1000000,
                destination_address="0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343",
                mint_recipient="invalid_address",
            )


class TestGetMessageStatus:
    """Tests for get_message_status function."""

    def test_get_status_returns_dict(self):
        """Test that message status returns a dictionary."""
        result = get_message_status("0xabc123")

        assert isinstance(result, dict)
        assert "message_hash" in result
        assert "status" in result
        assert "transmitter_address" in result

    def test_get_status_includes_message_hash(self):
        """Test that returned status includes the message hash."""
        message_hash = "0xdef456"
        result = get_message_status(message_hash)

        assert result["message_hash"] == message_hash
        assert result["transmitter_address"] == CCTP_MESSAGE_TRANSMITTER_ADDRESS
