from django.test import TestCase
from django.urls import reverse
from .models import YourModel  # Replace with your actual model

class YourModelTests(TestCase):
    def setUp(self):
        # Create an instance of YourModel for testing
        self.model_instance = YourModel.objects.create(field1='value1', field2='value2')  # Adjust fields as necessary

    def test_model_creation(self):
        # Test that the model instance was created successfully
        self.assertEqual(self.model_instance.field1, 'value1')
        self.assertEqual(self.model_instance.field2, 'value2')

    def test_api_endpoint(self):
        # Test the API endpoint
        response = self.client.get(reverse('yourmodel-list'))  # Replace with your actual endpoint name
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'value1')  # Adjust based on expected response content

    def test_api_create(self):
        # Test creating a new instance via the API
        response = self.client.post(reverse('yourmodel-list'), {'field1': 'new_value1', 'field2': 'new_value2'}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(YourModel.objects.count(), 2)  # Ensure a new instance was created
        self.assertEqual(YourModel.objects.last().field1, 'new_value1')  # Check the last instance's field1