import os
from flask import Flask, render_template, request
from docker import Client

docker = Client(base_url='unix://var/run/docker.sock')

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    """ This is the display view. """

    return "gutn tag!"


# allow list of labels to define which containers to restart?
@app.route('/webhook', methods=['POST'])
def webhook():
    """
        Webhooks simply provide API endpoints that the user can use to gather
        more information. They are sent as HTTP POSTS with the JSON mimetype
        specified in the header.
    """

    for line in cli.pull('busybox', stream=True):
        print(json.dumps(json.loads(line), indent=4))

    # TODO callback

    return ""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8800)
