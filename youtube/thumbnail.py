from flask import Blueprint, send_file, request
from io import BytesIO
import requests
import re

thumbnail_bp = Blueprint('youtube_thumbnail', __name__)

def get_youtube_id(url):
    patterns = [
        r'(?:v=|\/)([0-9A-Za-z_-]{11}).*',
        r'(?:embed\/|be\/)([0-9A-Za-z_-]{11})',
        r'^([0-9A-Za-z_-]{11})$'
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

@thumbnail_bp.route('/get-youtube-thumbnail', methods=['POST'])
def get_thumbnail():
    url = request.form['url']
    video_id = get_youtube_id(url)
    
    if not video_id:
        return {'success': False, 'message': 'Invalid YouTube URL'}
    
    return {
        'success': True,
        'thumbnail': f'https://img.youtube.com/vi/{video_id}/maxresdefault.jpg',
        'video_id': video_id
    }

@thumbnail_bp.route('/download/youtube/<video_id>')
def download(video_id):
    try:
        qualities = ['maxresdefault', 'sddefault', 'hqdefault', '0']
        for quality in qualities:
            url = f'https://img.youtube.com/vi/{video_id}/{quality}.jpg'
            response = requests.get(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            }, timeout=10)
            
            if response.status_code == 200 and len(response.content) > 0:
                mem = BytesIO(response.content)
                mem.seek(0)
                return send_file(
                    mem,
                    mimetype='image/jpeg',
                    download_name=f'{video_id}_thumbnail.jpg',
                    as_attachment=True
                )
        
        return {'success': False, 'message': 'Could not find valid thumbnail'}, 404
    
    except Exception as e:
        return {'success': False, 'message': f'Download failed: {str(e)}'}, 500 