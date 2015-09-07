This is a small proxy created for a testing purposes which works as following:
You pass url and delay in querystring, app fetches url and starts to stream it's
contents really really slowly until streaming time exceeds delay, at which point
proxy stops slowing down the process and just streams the rest of the content.

# How to install

    $ virtualenv ./env
    $ source env/bin/activate
    $ python setup.py develop


# How to run

    $ gunicorn slowpoke.app:main --worker-class=gevent                                                                                                git:master*
    [2015-09-08 00:29:26 +0300] [3783] [INFO] Starting gunicorn 19.3.0
    [2015-09-08 00:29:26 +0300] [3783] [INFO] Listening at: http://127.0.0.1:8000 (3783)
    [2015-09-08 00:29:26 +0300] [3783] [INFO] Using worker: gevent
    [2015-09-08 00:29:26 +0300] [3786] [INFO] Booting worker with pid: 3786

# How to use
Open url like
`http://127.0.0.1:8000/?delay=3&url=http://bit.ly/virginity_i_choose_you`
in your browser
