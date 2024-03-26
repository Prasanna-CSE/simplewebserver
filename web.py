from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
	<head>
		<title>REVENUE TABLE</title>
	</head>
	<body bgcolor="cyan">
	<h1>TOP FIVE REVENUE GENERATING SOFTWARE COMPANIES</h1>
	<table border='3' cellspacing="4" cellpadding='3'>
		<tr>
			<th>RANK</th>
			<th>ORGANIZATION</th>
			<th>FY</th>
			<th>REVENUE</th>
		</tr>
		<tr>
			<td>1</td>
			<td>MICROSOFT</td>
			<td>2022</td>
			<td>$203.08 billion</td>
		</tr>

		<tr>
			<td>2</td>
			<td>GOOGLE</td>
			<td>2022</td>
			<td>$173.02 billion</td>
		</tr>

		<tr>
			<td>3</td>
			<td>IBM</td>
			<td>2019</td>
			<td>$123.58 billion</td>
		</tr>
		<tr>
			<td>4</td>
			<td>ORACLE</td>
			<td>2019</td>
			<td> $46.07 billion</td>
		</tr>
		<tr>
			<td>5</td>
			<td>SAP</td>
			<td>2019</td>
			<td>$32.97 billion</td>
		</tr>
	</table>
	</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()