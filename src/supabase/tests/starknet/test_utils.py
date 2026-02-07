"""Tests for Starknet utility functions."""

import pytest

from supabase.starknet.utils import (
    format_usdc_amount,
    get_usdc_balance,
    validate_starknet_address,
)


class TestValidateStarknetAddress:
    """Tests for validate_starknet_address function."""

    def test_valid_address(self):
        """Test validation of valid Starknet addresses."""
        valid_addresses = [
            "0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343",
            "0x04bDdE1E09a4B09a2F95d893D94a967b7717eB85A3f6dEcA8c080Ee01fBc3370",
            "0x123",
            "0xabc",
        ]
        for addr in valid_addresses:
            assert validate_starknet_address(addr) is True

    def test_invalid_address_no_prefix(self):
        """Test that addresses without 0x prefix are invalid."""
        assert validate_starknet_address("1234567890abcdef") is False

    def test_invalid_address_non_hex(self):
        """Test that non-hex strings are invalid."""
        assert validate_starknet_address("0xGHIJKLMNOP") is False

    def test_invalid_address_too_long(self):
        """Test that addresses longer than 66 chars are invalid."""
        long_addr = "0x" + "a" * 65
        assert validate_starknet_address(long_addr) is False

    def test_invalid_address_too_short(self):
        """Test that addresses shorter than 3 chars are invalid."""
        assert validate_starknet_address("0x") is False
        assert validate_starknet_address("0") is False

    def test_invalid_address_non_string(self):
        """Test that non-string inputs are invalid."""
        assert validate_starknet_address(123) is False
        assert validate_starknet_address(None) is False
        assert validate_starknet_address([]) is False


class TestFormatUsdcAmount:
    """Tests for format_usdc_amount function."""

    def test_format_one_usdc(self):
        """Test formatting 1 USDC."""
        assert format_usdc_amount(1000000) == "1.000000"

    def test_format_zero_usdc(self):
        """Test formatting 0 USDC."""
        assert format_usdc_amount(0) == "0.000000"

    def test_format_fractional_usdc(self):
        """Test formatting fractional amounts."""
        assert format_usdc_amount(1500000) == "1.500000"
        assert format_usdc_amount(500000) == "0.500000"
        assert format_usdc_amount(123456) == "0.123456"

    def test_format_large_amount(self):
        """Test formatting large amounts."""
        assert format_usdc_amount(1000000000000) == "1000000.000000"

    def test_format_with_custom_decimals(self):
        """Test formatting with custom decimal places."""
        assert format_usdc_amount(1000, decimals=3) == "1.000"
        assert format_usdc_amount(12345, decimals=2) == "123.45"


class TestGetUsdcBalance:
    """Tests for get_usdc_balance function."""

    def test_get_balance_valid_address(self):
        """Test getting balance with valid address."""
        address = "0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343"
        result = get_usdc_balance(address)

        assert result["address"] == address
        assert "balance_raw" in result
        assert "balance_formatted" in result
        assert result["token"] == "USDC"
        assert result["network"] == "starknet-testnet"

    def test_get_balance_invalid_address(self):
        """Test that invalid address raises ValueError."""
        with pytest.raises(ValueError, match="Invalid Starknet address format"):
            get_usdc_balance("invalid_address")

    def test_get_balance_with_provider_url(self):
        """Test getting balance with custom provider URL."""
        address = "0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343"
        result = get_usdc_balance(address, provider_url="https://custom-provider.com")

        assert result["address"] == address
        assert result["token"] == "USDC"

    def test_get_balance_returns_formatted_amount(self):
        """Test that balance includes formatted amount."""
        address = "0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343"
        result = get_usdc_balance(address)

        # Should be formatted with 6 decimals
        assert "." in result["balance_formatted"]
        parts = result["balance_formatted"].split(".")
        assert len(parts) == 2
        assert len(parts[1]) == 6
