import os
import views
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix


app = Flask(__name__)

#Functions for the app - each one for each type - will be triggered by the routes below


#main page function
app.add_url_rule('/', view_func=views.front_page)
app.add_url_rule('/ip_address', view_func=views.ip_address)
app.add_url_rule('/decent', view_func=views.decent_pass)
app.add_url_rule('/strong', view_func=views.strong_pass)
app.add_url_rule('/ftknox', view_func=views.ftknox_pass)
app.add_url_rule('/ci', view_func=views.ci_key)
app.add_url_rule('/wep160', view_func=views.wpa_160_key)
app.add_url_rule('/wpa160', view_func=views.wpa_160_key)
app.add_url_rule('/wpa504', view_func=views.wpa_504_key)

#number of reverse proxies in front of the app whose X-Forwarded-* headers are trusted
#0 (default) trusts none - set to match your deployment, e.g. 2 for cloudflare + azure app service
proxy_hops = int(os.environ.get('TRUSTED_PROXY_HOPS', '0'))
if proxy_hops > 0:
    app.wsgi_app = ProxyFix(
        app.wsgi_app, x_for=proxy_hops, x_proto=proxy_hops, x_host=proxy_hops, x_prefix=proxy_hops
    )

if __name__ == "__main__":
  app.run()