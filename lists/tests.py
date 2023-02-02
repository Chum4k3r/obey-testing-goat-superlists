# Create your tests here.
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


def test_home_page_returns_correct_html(client: Client) -> None:
    response = client.get('/')
    assertTemplateUsed(response, 'home.html')


def test_can_save_new_task_from_POST_request(client: Client) -> None:
    response = client.post('/', data={'item_text': 'A new task'})
    assert 'A new task' in response.content.decode()
    assertTemplateUsed(response, 'home.html')
