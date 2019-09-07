import tornado.web
import time


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        current_time = time.time()
        while True:
            if time.time() - current_time >= 10:
                break
        self.write('Now is {}'.format(time.time()))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()