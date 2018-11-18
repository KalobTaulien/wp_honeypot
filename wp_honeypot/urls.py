from django.conf.urls import url

from django.views.generic import RedirectView

from wp_honeypot.models import WPHoneypotLogin

urlpatterns = [
    url(r'^wp-admin/?$', RedirectView.as_view(url='/wp-login.php?reauth=1'), name='wp_honeypot_admin'),
    url(r"^wp-login.php/?$", WPHoneypotLogin.as_view(), name='wp_honeypot_login'),
]
