from fastapi_users.authentication import JWTAuthentication

SECRET = "d5r@z%-vd-c8paifxash89l#5c80fdcs7qemw_5q7m*&e@l8"

auth_backends = []

jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600, tokenUrl="/auth/login")

auth_backends.append(jwt_authentication)