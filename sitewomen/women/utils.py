MENU = [
    {'title': "About Site", 'url_name': 'about'},
    {'title': "Add Article", 'url_name': 'add_page'},
    {'title': "Contact", 'url_name': 'contact'},
    {'title': "Login", 'url_name': 'login'}
]


class DataMixin:
    title_page = None
    cat_selected = None
    paginate_by = 5
    extra_context = {}

    def __init__(self):
        if self.title_page is not None:
            self.extra_context['title'] = self.title_page

        if 'menu' not in self.extra_context:
            self.extra_context['menu'] = MENU

        if self.cat_selected is not None:
            self.extra_context['cat_selected'] = self.cat_selected


    def get_mixin_context(self, context, **kwargs):
        context['menu'] = MENU
        context['cat_selected'] = None
        context.update(kwargs)
        return context
