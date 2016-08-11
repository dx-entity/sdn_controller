import webob.dec
from webob.exc import HTTPNotFound as HTTPNotFound
from routes.mapper import Mapper


class WsgiHack(webob.dec.wsgify):
    def __call__(self, environ, start_response):
        self.kwargs["start_response"] = start_response
        return super(WsgiHack, self).__call__(environ, start_response)


class WSGIApplication(object):
    def __init__(self):
        super(WSGIApplication, self).__init__()
        self.mapper = Mapper()
        self._match = lambda req: self.mapper.match(environ=req.environ)

    @WsgiHack
    def __call__(self, req, start_response):
        match = self._match(req)

        if not match:
            return HTTPNotFound()

        req.start_response = start_response
        req.urlvars = match

        name = match["controller"].__name__

        controller = match["controller"](req)

        return controller(req)


class BaseController(object):
    def __init__(self, req):
        self.req = req

    def __call__(self, req):
        action = self.req.urlvars.get('action', 'index')

        kwarg = self.req.urlvars.copy()

        return getattr(self, action)(self.req, **kwarg)
