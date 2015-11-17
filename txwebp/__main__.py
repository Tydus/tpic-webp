#!/usr/bin/python2

import tornado.ioloop
import tornado.httpserver
import tornado.web
import tornado.gen

import PIL.Image
import StringIO

class MainHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        res = yield AsyncHTTPClient().fetch(self.request.uri)

        if res.headers["Content-Type"] == "image/webp":
            s = StringIO.StringIO()
            PIL.Image.open(res.buffer).save(s, "jpg")
        else:
            s = res.buffer

        self.write(s.getvalue())


def main():
    tornado.httpserver.HTTPServer(tornado.web.Application([
        ("/.*", MainHandler),
    ]), xheaders = True).listen(8088)

    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
