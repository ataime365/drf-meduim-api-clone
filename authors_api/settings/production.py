from .base import * #noqa

ADMINS = [("Okodi Ataime", "ataime15@gmail.com"), ("Jagiri Daniel", "jagiri360@gmail.com"), ]
# Django will email this people when we get an error notification in production, since debug will be set to False already

# TODO: add domain names of the production server
CSRF_TRUSTED_ORIGINS = [""]