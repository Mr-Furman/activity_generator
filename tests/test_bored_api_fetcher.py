import unittest
from unittest.mock import Mock, patch
from data_fetcher import BoredAPIFetcher


class TestBoredAPIFetcher(unittest.TestCase):
    @patch("data_fetcher.requests.get")
    def test_get_random_activity_success(self, mock_requests_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"activity": "Test Activity"}

        mock_requests_get.return_value = mock_response

        api_fetcher = BoredAPIFetcher()

        result = api_fetcher.get_random_activity(type="education",
                                                 participants=2)

        self.assertEqual(result, {"activity": "Test Activity"})

    @patch("data_fetcher.requests.get")
    def test_get_random_activity_failure(self, mock_requests_get):
        mock_response = Mock()
        mock_response.status_code = 500

        mock_requests_get.return_value = mock_response

        api_fetcher = BoredAPIFetcher()

        result = api_fetcher.get_random_activity(type="education",
                                                 participants=2)

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
