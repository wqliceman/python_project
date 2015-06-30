# -*- coding: utf-8 -*-
__author__ = 'wqliceman'
import web

urls =(
    '/', 'index',
    '/movie/(.*)', 'movie',
    '/cast/(.*)', 'cast',
    '/director/(.*)', 'director',
)

render = web.template.render('templates/')
db = web.database(dbn='sqlite', db='MovieSite.db')

class index():
    def GET(self):
        movies = db.select('movie')
        count = db.query('SELECT COUNT(*) AS COUNT FROM movie')[0]['COUNT']
        return render.index(movies, count, None)
    def POST(self):
        data = web.input()
        condition = r'title like "%'+data.title+'%"'
        movies = db.select('movie', where=condition)
        sql = 'select count(*) as count from movie where '+condition
        result = db.query(sql)
        count = result[0]['count']
        return render.index(movies, count, data.title)


class movie():
    def GET(self, movie_id):
        movie_id = int(movie_id)
        movie = db.select('movie', where='id=$movie_id', vars=locals())[0]
        return render.movie(movie)

class cast():
    def GET(self, cast_name):
        condition = r'casts like"%'+cast_name + r'%"'
        movies = db.select('movie', where=condition)
        sql = 'select count(*) as count from movie where '+condition
        result = db.query(sql)
        count = result[0]['count']
        return render.index(movies, count, cast_name)

class director():
    def GET(self, director_name):
        condition = r'directors like "%' + director_name + r'%"'
        movies = db.select('movie', where=condition)
        sql = 'select count(*) as count from movie where '+condition
        result = db.query(sql)
        count = result[0]['count']
        return render.index(movies, count, director_name)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()