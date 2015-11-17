#!/usr/bin/python2

import tornado.ioloop
import tornado.httpserver
import tornado.web
import tornado.httpclient
import tornado.gen
import sys

import PIL.Image
import StringIO

class MainHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        res = yield tornado.httpclient.AsyncHTTPClient().fetch(
            "%s://%s%s" % (self.request.protocol, self.request.host, self.request.uri)
        )

        if res.headers["Content-Type"] == "image/webp":
            s = StringIO.StringIO()
            PIL.Image.open(res.buffer).save(s, "jpeg")
            self.set_header("Content-Type", "image/jpeg")
            print "%s is webp" % (self.request.uri)
        else:
            s = res.buffer
            self.set_header("Content-Type", res.headers["Content-Type"])


        self.write(s.getvalue())


def main(argv=None):
    if not args:
        argv = sys.argv[1:]

    if len(argv) != 1:
        print >> sys.stderr, "txwebp <listen port>"
        exit(-1)

    tornado.httpserver.HTTPServer(tornado.web.Application([
        ("/.*", MainHandler),
    ]), xheaders = True).listen(int(argv[0]))

    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
