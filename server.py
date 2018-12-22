from flask import Flask, request, send_file
import os, uuid

def dl(url):
	uid = str(uuid.uuid4())
	cm = open("cmd.txt","r").read().strip().split("\n")[0]
	cmd = cm % (url, uid)
	input("[!] executing: "+cmd)
	os.system(cmd)
	return uid

app = Flask(__name__)

@app.route("/watch")
def app_dl():
	url = "https://www.youtube.com/watch?v=" + request.args['v']
	fn = dl(url)
	return send_file(fn)

if __name__ == "__main__":
	app.run(host="0.0.0.0",port=8000)