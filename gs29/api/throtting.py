from rest_framework.throttling import UserRateThrottle

class SonuRateThrottle(UserRateThrottle):
    scope='Sonu'

    