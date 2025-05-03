INSTALLED_APPS = [
    ...,
    "rest_framework",
    "corsheaders",
    "core",
    "rest_framework",
]
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    ...,
]
CORS_ALLOW_ALL_ORIGINS = True
