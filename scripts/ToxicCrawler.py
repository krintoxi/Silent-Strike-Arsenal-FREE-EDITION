# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 23:28:15 2017

@author: krintoxi
"""

import urllib, urllib2
import threading
import Queue

MAX_THREADS = 5
print ('------------------------')
print ('Toxic Directory Crawler')
print ('------------------------')
print ('*')
print ('-Please remember to include the (http://) in your target URL.')
print ('*')
TARGET_URL = raw_input(' What is your Target!?: ')
WORDLIST_FILE = "tmp/ToxicBuster.txt" # from SVNDigger
RESUME = None
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101Firefox/19.0"
VERBOSE= True

def main():
	words= readWordList(WORDLIST_FILE)
	
	# Create list of files extensions
	extensions= [".php",".bak",".orig",".inc"]
	
	# Create 
	for i in range(MAX_THREADS):
		printDebug("Creating thread {0}".format(i))
		th= threading.Thread(target= bforce, args=(words,extensions))
		th.start()
	
	return

def printDebug(msg):
	global VERBOSE
	
	if VERBOSE:
		print(msg)
	
	return

def readWordList(filename):
	printDebug("Reading word list from {0}".format(filename))
	
	with open(filename, "r") as fd:
		raw_words= fd.readlines()
	
	found_resume= False
	words= Queue.Queue()
	
	for word in raw_words:
		words.put( word.strip() )
		
		if RESUME:
			if found_resume:
				words.put( word.strip() )
			elif word == RESUME:
				found_resume= True
				print("Resuming wordlist from word {0}".format(RESUME))
		else:
			words.put( word.strip() )
	
	printDebug("Word list read successfully")
	
	return words

def bforce(words, extensions=[]):
	while not words.empty():
		attempt= words.get()
		attempt_list= []
		
		# Check if word have file extension
		if '.' not in attempt:
			attempt_list.append("/{0}/".format(attempt))
		else:
			attempt_list.append("/{0}".format(attempt))
		
		# Append filename with additional extensions
		for ext in extensions:
			attempt_list.append("/{0}{1}".format(attempt, ext))
		
		del attempt
		# REUSE of attemp variable
		for attempt in attempt_list:
			# Create URL link for this attempt
			url= "{0}{1}".format(TARGET_URL, urllib.quote(attempt))
			
			try:
				# Create Request object with User-Agent property
				headers= dict()
				headers['User-Agent']= USER_AGENT
				request= urllib2.Request(url, headers=headers)
				
				# Request website for file
				response= urllib2.urlopen(request)
				
				# Read the response. If file not exists the website return HTTPError exception
				if len(response.read()):
					print("[{0}] {1}".format(response.code, url))
			except urllib2.URLError, e:
				# Check error and print info if not 404
				if hasattr(e, 'code') and e.code != 404:
					print("[{0}] {1}".format(e.code, url))
			except:
				pass
				
	return

# Start program
main()

