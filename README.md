
### Needs to be modified to work with sanction 0.4 ###

**Will no longer work with Sanction 0.3.1 and earlier** New version of
Sanction breaks compatibility and does not include an easy way to obtain
the version. This version of django_sanction will hopefully soon be compatible. Currently validates and returns with token from Google but the backend.py needs work. 

Until then when using django_sanction be sure to specify `pip install sanction==0.3.1`

### About ###

django\_sanction is a Django wrapper for the [sanction](https://github.com/demianbrecht/sanction) Python library. It allows
for rapid integration of [OAuth 2.0](http://www.google.ca/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&ved=0CGIQFjAA&url=http%3A%2F%2Ftools.ietf.org%2Fhtml%2Fietf-oauth-v2-30&ei=sBAtULqHDqPOiwK3zoDgDg&usg=AFQjCNGSdKvjocQl86fT8e-dp_53zeqR8g) authentication, authorization and resource
access for clients.

Documentation can be found at [readthedocs](https://django-sanction.readthedocs.org/en/latest/)
