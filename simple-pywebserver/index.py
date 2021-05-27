import tornado.web #request handlers that receive from the http protocl
import tornado.ioloop #thread that continously waits for requests

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World! This is a Python command executed from the backend.")

class listRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html") #to serve static files

#GET endpoint accepting query parameters
class queryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("num") 
        if num.isdigit:
            r = "odd" if int(num) % 2 else "even"
            self.write(f"{num} is {r}")
        else:
            self.write(f"{num} is not a valid integer.")

#GET endpoint accepting resource parameters
class resourceParamRequestHandler(tornado.web.RequestHandler):
    def get(self, studentName, courseId):
        self.write(f"Welcome {studentName}! the course you are viewing is {courseId}")

#This should only run once
if __name__ == "__main__":
    #class Application expects tuples of endpoints
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/languages", listRequestHandler),
        (r"/isEven", queryParamRequestHandler),
        (r"/students/([a-z]+)/([0-9]+)", resourceParamRequestHandler) 
        #regular expressions help capture certain patterns
        #regular expression above is case sensitive
    ])

    port = 8882
    app.listen(port)
    print(f"Application is listening on port: {port}")
    tornado.ioloop.IOLoop.current().start() #Keeps application running