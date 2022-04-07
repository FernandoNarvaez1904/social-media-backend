from django.contrib.auth import get_user_model
from strawberry_django_plus import gql


@gql.django.filter(get_user_model(), lookups=True)
class UserFilter:
    id: gql.auto
    username: gql.auto
    email: gql.auto
    first_name: gql.auto
    last_name: gql.auto
    last_login: gql.auto
    is_active: gql.auto
