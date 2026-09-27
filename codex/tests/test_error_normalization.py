from unittest.mock import Mock
import pytest

from providers.http_utils import raise_for_status
from providers.base import ProviderError


def _resp(status, body):
    m = Mock()
    m.status_code = status
    m.json.return_value = body
    m.text = str(body)
    return m


def test_auth_error():
    with pytest.raises(ProviderError) as exc:
        raise_for_status(_resp(401, {"error": {"message": "bad key"}}), "openai")
    assert exc.value.code == "auth"
    assert exc.value.retryable is False


def test_rate_limit_is_retryable():
    with pytest.raises(ProviderError) as exc:
        raise_for_status(_resp(429, {"error": {"message": "slow down"}}), "openai")
    assert exc.value.retryable is True


def test_server_error_is_retryable():
    with pytest.raises(ProviderError) as exc:
        raise_for_status(_resp(500, {"error": {"message": "oops"}}), "openai")
    assert exc.value.retryable is True
