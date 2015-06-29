# -*- coding: utf-8 -*-
__author__ = 'wqliceman'
import web

urls =(
    '/', 'index'
)

class index():
    def GET(self):
        render = web.template.render('templates/')
        db = web.database(dbn='sqlite', db='MovieSite.db')
        movies = db.select('movie')
        print movies
        return render.index(movies)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()