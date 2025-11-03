from flask import Flask, render_template
from youtube.thumbnail import thumbnail_bp
from youtube.tags import tags_bp
from youtube.tag_generator import tag_gen_bp
from youtube.hashtag_generator import hashtag_bp
from youtube.title_generator import title_bp
from youtube.description_generator import desc_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(thumbnail_bp)
app.register_blueprint(tags_bp)
app.register_blueprint(tag_gen_bp)
app.register_blueprint(hashtag_bp)
app.register_blueprint(title_bp)
app.register_blueprint(desc_bp)

# Basic routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/youtube')
def youtube_page():
    return render_template('youtube.html')

@app.route('/youtube-tags')
def youtube_tags_page():
    return render_template('youtube_tags.html')

@app.route('/tag-generator')
def tag_generator_page():
    return render_template('youtube_tag_generator.html')

@app.route('/hashtag-generator')
def hashtag_generator_page():
    return render_template('hashtag_generator.html')

@app.route('/title-generator')
def title_generator_page():
    return render_template('youtube_title_generator.html')

@app.route('/description-generator')
def description_generator_page():
    return render_template('youtube_description_generator.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/privacy')
def privacy_page():
    return render_template('privacy.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

# Other basic routes (about, privacy, contact) remain the same

if __name__ == '__main__':
    app.run(debug=True) 