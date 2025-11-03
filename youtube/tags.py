from flask import Blueprint, request
import requests
from config import YOUTUBE_API_KEY
from .thumbnail import get_youtube_id

tags_bp = Blueprint('youtube_tags', __name__)

@tags_bp.route('/get-youtube-tags', methods=['POST'])
def get_tags():
    url = request.form['url']
    video_id = get_youtube_id(url)
    
    if not video_id:
        return {'success': False, 'message': 'Invalid YouTube URL'}
    
    try:
        response = requests.get(
            f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={YOUTUBE_API_KEY}'
        )
        data = response.json()
        
        if not data.get('items'):
            return {'success': False, 'message': 'Video not found'}
            
        tags = data['items'][0]['snippet'].get('tags', [])
        
        return {
            'success': True,
            'tags': tags,
            'video_id': video_id
        }
        
    except Exception as e:
        return {'success': False, 'message': str(e)} 