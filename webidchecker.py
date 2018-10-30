#!/usr/bin/env python

import requests
import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-u", "--url", help="URL to test ID (do NOT include with the actual ID)", action="store",
                  type="string", dest="url")
parser.add_option("-r", "--range", help="ID range to test", action="store", type="int", dest="id_range")
(options, args) = parser.parse_args()


subprocess.call(["clear"])

# Returns HTTP status code
def get_http_status_code(url):
    try:
        r = requests.head(url)
        return r.status_code
    except requests.ConnectionError:
        return "Failed to connect"


for i in range(options.id_range):
    try:
        current_check = options.url + str(i)
        check_result = get_http_status_code(current_check)
        if check_result != 404 and check_result != 500:
            print(current_check + " ==> " + str(check_result))
    except KeyboardInterrupt:
        print("\nQuitting...")
        break
