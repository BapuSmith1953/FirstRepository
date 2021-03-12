# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_app]
# [START gae_python3_app]
from flask import Flask


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World! <br/> Chioma is the best! <br/> Hi Bapu! <br/> Yaya\'s garden is so nice! <br/> Great, Yaya is so nice! <br/><br/> who is nicer than yaya?<br/><br/> yaya grden is so nice!<br/><br/>Bapu made a .py program using the name of Samuel! '
#changed the name string in this file
# This Version Checked out from Github into Pycharm, this comment added, then returned to Github
# I notice the length of delay is highly sensitive to where the "return" is placed relative to the three nested loops
namestring="Yaya_Loves_Samuel!"
def delay():
    for j in range (20000):
        q= 434345. / 4.555
        for k in range (30000):
            junk =3.666577545 /4.66666456
            for n in range (200):
                p = 66543.234 / 4.777
        return junk
for i in range (6):
    modstring = namestring
    print("*" + modstring + "*")
    wait = delay()
    modstring = namestring[1:16]
    print(" *" + modstring + "*")
    wait = delay()
    modstring = namestring[2:15]
    print("  *" + modstring + "*")
    wait = delay()
    modstring = namestring[3:12]
    print("    *" + modstring + "*")
    wait = delay()
    modstring = namestring[5:10]
    print("      *" + modstring + "*")
    wait = delay()
    modstring = namestring[7:8]
    print("         **")
    wait = delay()
    modstring = namestring[5:10]
    print("      *" + modstring + "*")
    wait = delay()
    modstring = namestring[3:12]
    print("    *" + modstring + "*")
    wait = delay()
    modstring = namestring[2:15]
    print("  *" + modstring + "*")
    wait = delay()
    modstring = namestring[1:16]
    print(" *" + modstring + "*")
    wait = delay()
    modstring = namestring
    print("*" + modstring + "*")
    wait = delay()

#This replaces the name string with symbols to create a sense of shape
threestring = "oooooOO000OOooooo"
onestring="..,,;;***oooOOO000"
twostring="000OOOooo***;;,,.."
def delay():
    q=6
    for j in range (2000):
        q= 434345. / 4.555
        for k in range (1000):
            junk =3.666577545 /4.66666456
            for n in range (700):
                p = 665432.234 / 4.777
        return junk
for i in range (15):
    modstring = threestring
    print("*" + modstring + "*")
    wait = delay()
    modstring = onestring[1:16]
    print(" *" + modstring + "*")
    wait = delay()
    modstring = onestring[2:15]
    print("  *" + modstring + "*")
    wait = delay()
    modstring = onestring[3:12]
    print("    *" + modstring + "*")
    wait = delay()
    modstring = onestring[5:10]
    print("      *" + modstring + "*")
    wait = delay()
    print("         *0")
    wait = delay()
    modstring = twostring[5:10]
    print("      *" + modstring + "*")
    wait = delay()
    modstring = twostring[3:12]
    print("    *" + modstring + "*")
    wait = delay()
    modstring = twostring[2:15]
    print("  *" + modstring + "*")
    wait = delay()
    modstring = twostring[1:16]
    print(" *" + modstring + "*")
    wait = delay()
    modstring = threestring
    print("*" + modstring + "*")
    wait = delay()






















if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
