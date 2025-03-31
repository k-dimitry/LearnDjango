from django.http import HttpRequest

from women.utils import MENU


def get_women_context(request: HttpRequest) -> dict:
    return {'mainmenu': MENU}
