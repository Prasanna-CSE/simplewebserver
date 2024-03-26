# EX01 Developing a Simple Webserver
## Date:24/04/24

## AIM:
To develop a simple webserver to serve html pages.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```
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
```
## OUTPUT:
![alt text](<Screenshot (91).png>)
![alt text](<Screenshot (90).png>)
## RESULT:
The program for implementing simple webserver is executed successfully.
