from urllib import urlencode
from flask import Flask

BASE_URL = "https://www.unitedwifi.com/portal/l/goto"
app = Flask(__name__)


def setup_redirect(dirty_dest):
   return urlencode({'url': dirty_dest})


def goto(dest):
    final_dest = setup_redirect(dest)
    # final_dest = dest
    return BASE_URL + "?{}".format(final_dest)


@app.route('/<token>')
def index(token):
   token = request.args.get('d')
   return goto(token)


if __name__ == '__main__':
   destination = "http://www.google.com"  # MAKS SURE that it is http
   host = "localhost"
   port = "7777"
   app.run(host=host, port=int(port), debug=True, use_reloader=True, use_debugger=True)

