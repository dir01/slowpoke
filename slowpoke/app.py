# -*- coding: utf-8 -*-
import time
import httplib
from datetime import datetime

import requests
from webob.request import Request
from webob.response import Response


def main(environ, start_response):
    req = Request(environ)
    url = req.GET.get('url')
    try:
        delay = int(req.GET['delay'])
    except (KeyError, ValueError):
        delay = None
    if not url or not delay:
        response = Response(body=USAGE_INFO, status=httplib.BAD_REQUEST)
        return response(environ, start_response)
    return respond_with_url_content_slowly_but_no_longer_than_delay(start_response, url, delay)


def respond_with_url_content_slowly_but_no_longer_than_delay(start_response, url, delay):
    url_response = requests.get(url)
    start_response(str(url_response.status_code), url_response.headers.items())
    content = url_response.content
    start = datetime.now()
    should_pause = True
    for i in content:
        if should_pause:
            time.sleep(.0001)
            if (datetime.now() - start).total_seconds() > delay:
                should_pause = False
        yield i


USAGE_INFO = """<h3><pre>
Use this service as following:
/?delay=DELAY&url=URL.

You will recieve headers of URL as soon as we download it,
and then we're gonna feed you contents of URL extremely slow,
but no longer than DELAY seconds.
</pre></h3>"""
