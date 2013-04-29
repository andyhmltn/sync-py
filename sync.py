#!/usr/bin/env python

import requests
import json
import os

username = 'Andy'

request = requests.get('https://api.github.com/users/andyhmltn/repos')

if(request.ok):
	repos = json.loads(request.text or request.content)

	for repo in repos:
		repo_url = "git@github.com:"+str(repo['full_name'])+".git"

		print "Cloning repo: " + str(repo['full_name'])
		os.system("git clone " + repo_url)
else:
	print request