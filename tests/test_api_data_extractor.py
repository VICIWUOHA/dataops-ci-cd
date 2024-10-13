# Basic Tests to ensure our extractor works properly.

import os
import pytest
from unittest.mock import patch, Mock
import requests
from python_base.api_data_extractor import extract_data


def test_extract_data_success():
    # Mock data
    mock_endpoint = "/test_endpoint"
    mock_base_url = os.getenv("BASE_URL")
    mock_response_data = [{"id": 1, "name": "Test Product", "id": "Dummy Product"}]

    # Create a mock response
    mock_response = Mock()
    mock_response.json.return_value = mock_response_data

    # Patch the requests.get method
    with patch('requests.get') as mock_get:
        mock_get.return_value = mock_response
        result = extract_data(mock_endpoint)

        # Assert that requests.get was called with the correct URL
        mock_get.assert_called_once_with(mock_base_url + mock_endpoint)

        # Assert that the function returns the expected data
        assert result == mock_response_data

def test_extract_data_exception():
    mock_endpoint = "/test_endpoint"

    # Patch requests.get to raise an exception
    with patch('requests.get', side_effect=requests.RequestException("Test error")):
        # Assert that the function raises the exception
        with pytest.raises(requests.RequestException):
            extract_data(mock_endpoint)




