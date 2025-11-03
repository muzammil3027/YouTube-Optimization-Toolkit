from flask import Blueprint, request

hashtag_bp = Blueprint('hashtag_generator', __name__)

@hashtag_bp.route('/generate-hashtags', methods=['POST'])
def generate_hashtags():
    try:
        keywords = request.form.get('keywords', '')
        if not keywords:
            return {'success': False, 'message': 'Please enter some keywords'}
            
        keywords_list = [k.strip() for k in keywords.split(',') if k.strip()]
        generated_hashtags = []
        
        # Generate hashtag variations
        for keyword in keywords_list:
            generated_hashtags.extend([
                f"#{keyword.replace(' ', '')}",
                f"#{keyword.replace(' ', '_')}",
                f"#Best{keyword.title().replace(' ', '')}",
                f"#{keyword.replace(' ', '')}2024",
                f"#{keyword.replace(' ', '')}Tips"
            ])
        
        # Add common hashtags
        generated_hashtags.extend([
            "#ViralVideo",
            "#TrendingNow",
            "#YouTubeShorts",
            "#Subscribe",
            "#ContentCreator"
        ])
        
        # Deduplicate and limit
        unique_hashtags = list(set(generated_hashtags))[:30]
        
        return {'success': True, 'hashtags': unique_hashtags}
        
    except Exception as e:
        return {'success': False, 'message': str(e)} 