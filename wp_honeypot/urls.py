from django.conf.urls import url

from django.views.generic import RedirectView

from wp_honeypot.models import WPHoneypotLogin, WpHoneypotRedirect

urlpatterns = [
    url(
        r"^wp-admin/?$",
        RedirectView.as_view(url="/wp-login.php?reauth=1"),
        name="wp_honeypot_admin",
    ),
    url(r"^wp-login.php/?$", WPHoneypotLogin.as_view(), name="wp_honeypot_login"),
    url(r"^wp/wp-admin/install.php$", WpHoneypotRedirect.as_view()),
    url(r"^wp-admin/install.php$", WpHoneypotRedirect.as_view()),
    url(r"^old/wp-admin/install.php$", WpHoneypotRedirect.as_view()),
    url(r"^blog/wp-admin/install.php$", WpHoneypotRedirect.as_view()),
    url(r"^new/wp-admin/install.php$", WpHoneypotRedirect.as_view()),
    url(r"^test/wp-admin/install.php$", WpHoneypotRedirect.as_view()),
    url(r"^wordpress/wp-admin/install.php$", WpHoneypotRedirect.as_view()),
]
