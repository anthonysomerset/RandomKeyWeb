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

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=2, x_proto=2, x_host=2, x_prefix=2
)

if __name__ == "__main__":
  app.run()