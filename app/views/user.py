from flask_admin.contrib import sqla
from app import admin, db
from app.models import *


class UserAdmin(sqla.ModelView):
    """ Flask-admin can not automatically find a association_proxy yet. You will
        need to manually define the column in list_view/filters/sorting/etc.
        Moreover, support for association proxies to association proxies
        (e.g.: keywords_values) is currently limited to column_list only."""

    column_list = ('id', 'name', 'keywords', 'keywords_values')
    column_sortable_list = ('id', 'name')
    column_filters = ('id', 'name', 'keywords')
    form_columns = ('name', 'keywords')

class KeywordAdmin(sqla.ModelView):
    column_list = ('id', 'keyword')

admin.add_view(UserAdmin(user.User,db.session))
admin.add_view(KeywordAdmin(user.Keyword,db.session))
