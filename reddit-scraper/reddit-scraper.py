#################################################
# SUBREDDIT SCRAPER v1.0 - By Kurt van Bendegem	#
# ---------------------------------------------	#
# Converts posts from any subreddit into text   #
# files for offline viewing. 					#
#################################################


import os
import praw
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


LIMIT = 1000

# get a reddit session
r = praw.Reddit("PRAW subreddit submmission scraper by Kurt van Bendegem")

# get subreddit from user
subreddit_name = raw_input('please enter desired subreddit: reddit.com/r/')

print("subreddit chosen is " + subreddit_name)

subreddit = r.get_subreddit(subreddit_name)

# get all submissions in the subreddit
post_gen = subreddit.get_new(limit=1000)


# create folder to put submissions in
if not os.path.exists(subreddit_name):
	os.makedirs(subreddit_name)

directory = subreddit_name + "/"

# iterate through all of the submissions in the subreddit
post_count = 0

for post in post_gen:
	post_count += 1
	title = (post.title.decode('unicode_escape').replace("/", " ").encode('ascii', 'ignore'))[:50]

	post_text = post.selftext


	#create file
	file = open(directory + title + ".txt", "w+")
	file.write(post_text)

	print str(post_count) + "\t" + title
