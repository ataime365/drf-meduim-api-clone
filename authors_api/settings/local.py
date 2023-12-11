from .base import * #noqa

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY", default="7_e6cB_KN9M5JN9iMLjiqf9TxxnFy4mEKYMoShvlFlqZOfL_6AE",)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]
# Gives us a list of domains that are allowed to make cross-site requests to our site
# Since we shall be setting up 'Nginx' as our 'reverse proxy'

"""You need a reverse proxy because gunicorn doesn't buffer requests. 
Meaning that if a visitor's internet is very slow and it hangs, 
your gunicorn connection will just sit there idle waiting for the data to finish transfering or to
 the connection to terminate. This means that it will not be able to work on any other task (request) in the meantime.
On the other hand, a reverse proxy like Nginx can notice that a client is superslow and put it a side while it works 
on handling other requests. Maybe my examples are not 100% accurate but the concept is."""