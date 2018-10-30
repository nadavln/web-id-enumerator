#!/usr/bin/env python

import requests
import subprocess

subprocess.call(["clear"])

# Returns HTTP status code
def get_http_status_code(url):
	try:
		r = requests.head(url)
		return r.status_code
	except requests.ConnectionError:
		return "Failed to connect"
		
for i in range(200):
	try:
		# Rename the "current_check" variable to the website you want, and leave the ID field empty
		# (like the example below)
		current_check = "http://www.website.com/?id=" + str(i)
		check_result = get_http_status_code(current_check)
		if check_result != 404 and check_result != 500:
			print(current_check + " ==> " + str(check_result))
	except KeyboardInterrupt:
		print("\nQuitting...")
		break
