from django.urls.base import resolve, reverse_lazy

__author__ = 'Ashraful'


def get_view_by_url(url_name=None):
    """
    **view generator**
    :param url_name: get url_name as string
    :return: view function (Though it is class or something)
    """
    if not url_name:
        return None
    url = reverse_lazy(url_name)
    resolver_match = resolve(url)
    return resolver_match.func


def get_all_url_list():
    pass
