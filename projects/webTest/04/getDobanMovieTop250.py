#!/usr/bin/env python
# coding=utf-8

import urllib
import json
import time
import web


db = web.database(dbn='sqlite', db='MovieSite.db')

def add_movie(data):
    movie = json.loads(data)
    print movie['title']
    db.insert('movie',
             id=int(movie['id']),
             title=movie['title'],
             origin = movie['original_title'],
             url=movie['alt'],
             image = movie['images']['large'],
             directors=','.join([d['name'] for d in movie['directors']]),
             casts=','.join([c['name']for c in movie['casts']]),
             year = movie['year'],
             genres=','.join(movie['genres']),
             countries =','.join(movie['countries']),
             summary=movie['summary'])

movie_ids = []
for index in range(0,250, 50):
    response= urllib.urlopen('http://api.douban.com/v2/movie/top250?start=%d&count=50'% index)
    data = response.read()
    #print data
    data_json = json.loads(data)
    movie250=data_json['subjects']
    for movie in movie250:
        movie_ids.append(movie['id'])
        print movie['id'], movie['title']
        time.sleep(1)

count =0
for mid in movie_ids:
    print count, mid
    response = urllib.urlopen('http://api.douban.com/v2/movie/subject/%s' % mid)
    movie = response.read()
    add_movie(movie)
    count+=1
    time.sleep(1)
