"""Tests for Starknet faucet utilities."""


from supabase.starknet.config import USDC_FAUCET_URL
from supabase.starknet.faucet import (
    format_faucet_request,
    get_faucet_info,
    get_faucet_usage_guide,
)


class TestGetFaucetInfo:
    """Tests for get_faucet_info function."""

    def test_returns_dict(self):
        """Test that faucet info returns a dictionary."""
        info = get_faucet_info()
        assert isinstance(info, dict)

    def test_contains_required_fields(self):
        """Test that faucet info contains all required fields."""
        info = get_faucet_info()

        required_fields = [
            "url",
            "name",
            "description",
            "instructions",
            "network",
            "token",
        ]
        for field in required_fields:
            assert field in info

    def test_url_matches_config(self):
        """Test that faucet URL matches configuration."""
        info = get_faucet_info()
        assert info["url"] == USDC_FAUCET_URL

    def test_token_is_usdc(self):
        """Test that token is USDC."""
        info = get_faucet_info()
        assert info["token"] == "USDC"

    def test_network_is_starknet_testnet(self):
        """Test that network is Starknet Testnet."""
        info = get_faucet_info()
        assert "Starknet" in info["network"]


class TestFormatFaucetRequest:
    """Tests for format_faucet_request function."""

    def test_returns_dict(self):
        """Test that faucet request returns a dictionary."""
        wallet = "0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343"
        request = format_faucet_request(wallet)
        assert isinstance(request, dict)

    def test_includes_wallet_address(self):
        """Test that request includes the wallet address."""
        wallet = "0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343"
        request = format_faucet_request(wallet)

        assert request["wallet_address"] == wallet

    def test_includes_faucet_url(self):
        """Test that request includes the faucet URL."""
        wallet = "0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343"
        request = format_faucet_request(wallet)

        assert request["faucet_url"] == USDC_FAUCET_URL

    def test_includes_instructions(self):
        """Test that request includes instructions."""
        wallet = "0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343"
        request = format_faucet_request(wallet)

        assert "instructions" in request
        assert wallet in request["instructions"]
        assert USDC_FAUCET_URL in request["instructions"]

    def test_includes_network(self):
        """Test that request includes network information."""
        wallet = "0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343"
        request = format_faucet_request(wallet)

        assert request["network"] == "starknet-testnet"


class TestGetFaucetUsageGuide:
    """Tests for get_faucet_usage_guide function."""

    def test_returns_string(self):
        """Test that usage guide returns a string."""
        guide = get_faucet_usage_guide()
        assert isinstance(guide, str)

    def test_includes_faucet_url(self):
        """Test that guide includes faucet URL."""
        guide = get_faucet_usage_guide()
        assert USDC_FAUCET_URL in guide

    def test_includes_step_by_step(self):
        """Test that guide includes step-by-step instructions."""
        guide = get_faucet_usage_guide()
        assert "Step 1" in guide
        assert "Step 2" in guide
        assert "Step 3" in guide
        assert "Step 4" in guide

    def test_includes_token_details(self):
        """Test that guide includes token details."""
        guide = get_faucet_usage_guide()
        assert "USDC" in guide
        assert "Decimals: 6" in guide
        assert (
            "0x0512feAc6339Ff7889822cb5aA2a86C848e9D392bB0E3E237C008674feeD8343"
            in guide
        )

    def test_includes_important_notes(self):
        """Test that guide includes important notes."""
        guide = get_faucet_usage_guide()
        assert "testnet" in guide.lower()
        assert "Important Notes" in guide or "important" in guide.lower()
