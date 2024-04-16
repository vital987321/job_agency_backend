from rest_framework.authentication import TokenAuthentication
from django.utils import timezone
from django.conf import settings
from rest_framework import exceptions




class TokenExpiredAuthantication(TokenAuthentication):
    def authenticate(self, request):
        try:
            user, token=super().authenticate(request)
        except TypeError:
            return None
        token_age = (timezone.now()-token.created).seconds # (timezone.now()-token.created) is of timedelta type
        if token_age > settings.TOKEN_EXPIRED_SECONDS:
            token.delete()
            msg='Token expired. Please login again.'
            raise exceptions.AuthenticationFailed(msg)
        return user, token

