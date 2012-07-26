# vim: ts=4 sw=4 et:
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect

from sanction.client import Client


def auth_redirect(request, provider, client):
    kwargs = {}
    if provider.scope is not None: kwargs["scope"] = provider.scope
    if provider.state is not None: kwargs["state"] = provider.state

    client.redirect_uri = _get_redirect_uri(request, provider)
    return redirect(client.auth_uri(**kwargs))


def auth_login(request, provider, client):
    client.redirect_uri = _get_redirect_uri(request, provider)
    kwargs = {
        "data": request.GET,
    }
    if hasattr(provider, "parser"):
        kwargs["parser"] = getattr(provider, "parser")
    if hasattr(provider, "grant_type"):
        kwargs["grant_type"] = getattr(provider, "grant_type")

    client.request_token(**kwargs)
    user = authenticate(request=request, provider=provider,
        client=client)

    if user is not None:
        login(request, user)
    else:
        raise Exception("TODO")

    return redirect(settings.LOGIN_REDIRECT_URL)


def _get_redirect_uri(request, provider):
    return "%s://%s%s" % (_get_scheme(request), _get_host(request), 
        reverse_lazy(provider.code_view_name))


def _get_scheme(request):
    if hasattr(settings, "SANCTION_REDIRECT_URL_SCHEME"):
        scheme = getattr(settings, "SANCTION_REDIRECT_URL_SCHEME")
    else:
        scheme = request.META.get("wsgi.url_scheme", "http")

    return scheme


def _get_host(request):
    if hasattr(settings, "SANCTION_HOST"):
        host = getattr(settings, "SANCTION_HOST")
    else:
        host = request.META["HTTP_HOST"]

    return host
