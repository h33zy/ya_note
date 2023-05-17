import pytest

from django.shortcuts import reverse


@pytest.mark.parametrize(
    'parametrized_client, note_in_list',
    (
        (pytest.lazy_fixture('author_client'), True),
        (pytest.lazy_fixture('admin_client'), False),
    )
)
def test_note_not_in_list_for_another_user(
    parametrized_client,
    note_in_list,
    note
):
    url = reverse('notes:list')
    response = parametrized_client.get(url)
    assert (note in response.context['object_list']) is note_in_list


@pytest.mark.parametrize(
    'name, args',
    (
        ('notes:add', None),
        ('notes:edit', pytest.lazy_fixture('slug_for_args'))
    )
)
def test_pages_contains_form(author_client, name, args):
    url = reverse(name, args=args)
    response = author_client.get(url)
    assert 'form' in response.context
