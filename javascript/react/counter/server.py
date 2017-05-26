# This file provided by Facebook is for non-commercial testing and evaluation
# purposes only. Facebook reserves all rights not expressly granted.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# FACEBOOK BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import json
import os
import time
from flask import Flask, Response, request

app = Flask(__name__, static_url_path='', static_folder='public')
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))


@app.route('/api/count', methods=['GET', 'POST'])
def count_handler():
    with open('count.json', 'r') as f:
        count = json.loads(f.read())

    if request.method == 'POST':
        body = request.data.decode('utf-8')
        if body == 'up':
            count['count'] += 1
        elif body == 'down':
            count['count'] -= 1
        else:
            raise Exception('invalid POST body')

        with open('count.json', 'w') as f:
            f.write(json.dumps(count, indent=4, separators=(',', ': ')))

    return Response(
        json.dumps(count),
        mimetype='application/json',
        headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*'
        }
    )


if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), debug=True)
