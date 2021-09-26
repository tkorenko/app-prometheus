#!/usr/bin/env python3

import hashlib
import math
import os
import prometheus_client as prom
import random
import time
from threading import Thread

from flask import Flask, request
from flask_prometheus import monitor


start_time = time.time()
default_instance_id = hashlib.md5(str(time.time()).encode('utf-8')).hexdigest()
default_instance_id = str(default_instance_id)[0:8]
app_instance_id = os.getenv('APP_INSTANCE_ID', default_instance_id)

app = Flask("pyProm")


@app.route('/', methods=["GET", "POST"])
def hi():
    if request.method == "GET":
        return "OK", 200, None

    return "Bad Request", 400, None


counter = prom.Counter('app_prometheus_counter', 'This is my counter',
                       ['app_instance_id'])
gauge = prom.Gauge('app_prometheus_gauge', 'This is my gauge',
                   ['app_instance_id'])


def thr():
    while True:
        curr_time = time.time()
        diff_time = curr_time - start_time
        # sin() with 20min period
        y = 10.0 * math.sin(6.28 * diff_time / 1200.0)

        counter.labels(app_instance_id).inc(1)
        gauge.labels(app_instance_id).set(y)

        time.sleep(1)


Thread(target=thr).start()

# This is telemetry port:
monitor(app, port=8081)
# This is webapp port:
app.run(host="0.0.0.0", port=8080)
