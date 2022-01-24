from flask import Flask, render_template, request, abort
from .scrape import get_download_links


def create_app():
	app = Flask(__name__)
	app.config['DEBUG'] = False

	@app.get("/")
	def home():
		return render_template('index.html')

	@app.get("/download")
	def download():
		url = request.args.get('url')
		if not url:
			abort(404)
		episodes = get_download_links(url)
		return render_template('download.html', episodes=episodes)

	return app 
