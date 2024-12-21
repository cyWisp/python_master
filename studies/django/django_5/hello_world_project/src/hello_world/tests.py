from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_template_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, '<h1>This is the header</h1>')


class AboutPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'about.html')

    def test_template_content(self):
        response = self.client.get(reverse('about'))
        self.assertContains(response, '<h1>This is the about page</h1>')

class ContactPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse('contact'))
        self.assertTemplateUsed(response, 'contact.html')

    def test_template_content(self):
        response = self.client.get(reverse('contact'))
        self.assertContains(response, '<h1>This is the contact page</h1>')

class InventoryPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/inventory/')
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse('inventory'))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse('inventory'))
        self.assertTemplateUsed(response, 'inventory.html')

    def test_template_content(self):
        response = self.client.get(reverse('inventory'))
        self.assertContains(response, '<h1>Inventory</h1>')