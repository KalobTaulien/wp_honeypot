"""WordPress Honeypot Login Template Models."""
import datetime

from django.db import models
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from model_utils.models import TimeStampedModel


class WPHoneypotLog(TimeStampedModel, models.Model):
    """A log of login attempts. Never store passwords in case this is a human."""

    # Use CharFields because bots might try funny things in the email form.
    # We need not validate proper data since it's a log of the bots data.
    email = models.CharField(max_length=255)

    def __str__(self):
        """String repr."""
        return self.email

    class Meta:
        """App labels."""

        verbose_name = u'Login Attempts'
        verbose_name_plural = u'Login Attempts'


class WPHoneypotLogin(TemplateView):
    """WordPress Honeypot Login Template View."""

    template_name = "wp_honeypot_login.html"
    http_method_names = ["get", "post"]

    def get_context_data(self, **kwargs):
        """Get the current site name and domain, and pass it to the template context."""
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context["domain"] = current_site.domain
        context["name"] = current_site.name
        return context

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """Set headers. Redirect to a download file if POST method."""
        response = super().dispatch(request, *args, **kwargs)
        response["Date"] = datetime.datetime.now(datetime.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
        response["Content-Type"] = "text/html; charset=UTF-8"
        response["Server"] = "Apache/2.4.18 (Ubuntu)"
        response["CF-RAY"] = "47b74f333af1bcc8-SEA"
        response["Set-Cookie"] = "wordpress_cookie=WP+Cookie+check; path=/;"
        response["X-Frame-Options"] = "SAMEORIGIN"
        response["Vary"] = "Accept-Encoding,User-Agent"
        # The below headers return a `AssertionError: Hop-by-hop headers not allowed` error when using uwsgi
        # But these are often set on Apache/WordPress sites as well.
        # response["Transfer-Encoding"] = "chunked"
        # response["Keep-Alive"] = "timeout=5, max=100"
        # response["Connection"] = "Keep-Alive"

        # If POST, redirect. We know this is a bot, or a human who doesn't know better yet.
        if request.method == "POST":
            # If email address was provided, log it.
            if "log" in request.POST:
                # Log the email address.
                log_entry = WPHoneypotLog(email=request.POST.get('log'))
                log_entry.save()
            # Always redirect to 10gb download ;) ¯\_(ツ)_/¯
            return redirect("http://speedtest-ny.turnkeyinternet.net/10000mb.bin")
        return response
