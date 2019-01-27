# WP Honeypot
Creates a fake WordPress login page for your Django 2+ applications and redirects all login attempts to a 10gb download file.

This will log email addresses bots are trying to use to log in to your /wp-login.php page. 

All attempts to log in will result in a 10gb download file. Bots want to be malicious, we can be malicious back ;) 

## Installation
1. `pip install wp-honeypot`
2. Add `wp_honeypot` to your `INSTALLED_APPS`
3. `python manage.py migrate wp_honeypot`
4. Add the url pattern to your `urls.py` (example below)

```python
from wp_honeypot import urls as wp_honeypot_urls

urlpatterns = [
	# ...
	url(r"", include(wp_honeypot_urls)),
]
```

# Todos
- [ ] Breaks with Django ManifestStaticFilesStorage
- [ ] Add support for custom file download url
- [ ] Log bot headers 
- [ ] Create function to compile a list of bot headers to submit to third party services, nginx lists, apache lists, etc.
- [ ] Add emailing. Email site admins.