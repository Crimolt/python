status = '200 OK'
response_headers = [('Content-Type', ctype), ('Content-Length', str(len(response_body)))]
#
start_response(status, response_headers)
return[response_body]