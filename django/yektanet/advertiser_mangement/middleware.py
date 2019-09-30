def ipMiddleware(get_resp):
  def middleware(req):
    req.IP = req.META['REMOTE_ADDR']
    return get_resp(req)
  return middleware