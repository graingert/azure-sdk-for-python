# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
import pytest
import signal
import os
import subprocess
import sys

def start_testserver():
    if os.name == 'nt': #On windows, subprocess creation works without being in the shell
        os.environ["FLASK_APP"] = "coretestserver"
        return subprocess.Popen("flask run", env=dict(os.environ))

    return subprocess.Popen("FLASK_APP=coretestserver flask run", shell=True, preexec_fn=os.setsid) #On linux, have to set shell=True

def terminate_testserver(process):
    if os.name == 'nt':
        process.kill()
    else:
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)  # Send the signal to all the process groups

@pytest.fixture(scope="session")
def testserver():
    """Start the Autorest testserver."""
    server = start_testserver()
    yield
    # terminate_testserver(server)

# Ignore collection of async tests for Python 2
collect_ignore = []
if sys.version_info < (3, 5):
    collect_ignore.append("async_tests")

# If opencensus is loadable while doing these tests, register an empty tracer to avoid this:
# https://github.com/census-instrumentation/opencensus-python/issues/442
try:
    from azure.core.tracing.ext.opencensus_span import OpenCensusSpan
    from opencensus.trace.tracer import Tracer
    Tracer()
except ImportError:
    pass
