#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, urlparse, urllib, sys, bottle, json, datetime

class accesslog(object):
  def writelog(cls, others=''):
    f = open('accesslog.txt', 'a')
    f.write('{')
    f.write('"DATE": "{}",   '.format(datetime.strftime(datetime.today(), '%y%m%d_%H%M%S')))
    f.write('"IP": "{}",\n'.format(os.environ['REMOTE_ADDR']))
    f.write('"URL": "{}",\n'.format(os.environ['REQUEST_URI']))
    f.write('"UA": "{}",\n'.format(os.environ['HTTP_USER_AGENT']))
    f.write('}, \n')
    f.close()
    return True

@bottle.route('/script.js')
def scriptJs(name):
  accesslog.writelog()
  return template('')
if os.name == 'nt':
    run(host='0.0.0.0', port=8080, debug=True, reloader=True)
else:
    run(server='cgi', debug=False)
