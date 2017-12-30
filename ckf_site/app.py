from flask import Flask

from ckf_site.about import about_page
from ckf_site.home import home_page
from ckf_site.static import static_page

app = Flask(__name__)
app.register_blueprint(home_page)
app.register_blueprint(about_page)
app.register_blueprint(static_page)

if __name__ == '__main__':
    app.run()
