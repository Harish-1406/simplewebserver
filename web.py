from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<html>
    <body>
        <h1> LAPTOP CONFIGURATION</h1>
    <table border="1" cell padding="10">
        <tr>
        <th> System Configuration</th>
        <th> Descryption</th>
        </tr>
        <TR>
            <td>Processor</td>
            <td>i5-1335U</td>   
        </TR>
        <tr>
            <td>Primaray Memory</td>
            <td>RAM 16GB</td>
        </tr>
        <tr>
            <td>Secondary Memory</td>
            <td>512 GB SSID</td>
        </tr>
        <tr>
            <td>OS</td>
            <td>Windows 11</td>
        </tr>
        <tr>
            <td>Graphic</td>
            <td>-</td>
        </tr>
    </table>
    </body>
    </html>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
