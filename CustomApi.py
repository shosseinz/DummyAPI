import requests
from logging import warning
class CustomApi:

    def __init__(self) -> None:
        self.base_url = 'https://dummyjson.com'
        self.header = { 'Content-Type': 'application/json' }
        self.data_post = {
                                    'title': 'I am in love with someone.',
                                    'userId': 5
                                }
        self.data_put = {
                            'title': 'I think I should shift to the moon.',
                        }
        self.data_patch = {
                            'title': 'I think this is the last test.',
                        }
    
    # Function to perform a GET request
    def perform_get_request(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url)
        return response
    
    
    # Function to perform a POST request
    def perform_post_request(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, data=self.data_post)
        return response

    # Function to perform a PUT request
    def perform_put_request(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, data=self.data_put)
        return response

    # Function to perform a PATCH request
    def perform_patch_request(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.patch(url, data=self.data_patch)
        return response
    
    
    # Function to perform a DELETE request
    def perform_delete_request(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url)
        return response
    
    
    
    
    # Function to test the response of a request
    def test_response(self, response_status_code, expected_status_code, expected_content=None, response_parameter=None):
        assert response_status_code == int(expected_status_code), f"Expected status code {expected_status_code}, but got {response.status_code}"
        if (response_parameter is not None) & (expected_content is not None):
            assert response_parameter == expected_content, "Content Mismatch"
        warning("Test Passed: Status Code and Content Match")
    

    
