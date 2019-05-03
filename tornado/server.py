import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print('some1 calling')
        import ipdb; ipdb.set_trace()
        self.write("Hello, world 44444sdjchsdjhckjdsh445555555")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ],
    autoreload=True
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    print('Start server')