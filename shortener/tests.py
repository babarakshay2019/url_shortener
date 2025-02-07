from django.test import TestCase
from rest_framework.test import APIClient


class URLShortenerTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_url = "https://example.com"
        self.api_url = "/api/shorten/"

    def test_shorten_url(self):
        response = self.client.post(self.api_url, {"long_url": self.valid_url}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("short_url", response.data)
    
    def test_duplicate_shorten_url(self):
        response1 = self.client.post(self.api_url, {"long_url": self.valid_url}, format='json')
        self.assertEqual(response1.status_code, 201)
        self.assertIn("short_url", response1.data)

        response2 = self.client.post(self.api_url, {"long_url": self.valid_url}, format='json')
        self.assertEqual(response2.status_code, 200)
        self.assertIn("short_url", response2.data)

        # Ensure both responses return the same short URL
        self.assertEqual(response1.data["short_url"], response2.data["short_url"])

    def test_invalid_url(self):
        response = self.client.post(self.api_url, {"long_url": "invalid-url"}, format='json')
        self.assertEqual(response.status_code, 400)
    
    def test_list_shorten_urls(self):
        response1 = self.client.post(self.api_url, {"long_url": self.valid_url}, format='json')
        self.assertEqual(response1.status_code, 201)
        self.assertIn("short_url", response1.data)
        
        response2 = self.client.get(self.api_url, format='json')
        self.assertEqual(response2.data[0]['short_code'], response1.data["short_url"].split("/")[-1])
    
    def test_shorten_url_redirect_to_long_url(self):
        response1 = self.client.post(self.api_url, {"long_url": self.valid_url}, format='json')
        self.assertEqual(response1.status_code, 201)
        self.assertIn("short_url", response1.data)
        
        response2 = self.client.get(f"{self.api_url}{response1.data['short_url'].split('/')[-1]}", format='json')
        self.assertEqual(response2.status_code, 301)
    
    def test_shorten_url_throttled(self):
        response1 = self.client.post(self.api_url, {"long_url": self.valid_url}, format='json')
        self.assertEqual(response1.status_code, 201)
        self.assertIn("short_url", response1.data)
        max_attempts = 10
        attempts = 0
        while attempts < max_attempts:
            response2 = self.client.post(self.api_url, {"long_url": self.valid_url}, format='json')
            if response2.status_code == 429:
                # Throttling is working as expected
                break
            attempts += 1
        self.assertEqual(response2.status_code, 429)
