from flask import Blueprint, request

tag_gen_bp = Blueprint('tag_generator', __name__)

@tag_gen_bp.route('/generate-tags', methods=['POST'])
def generate_tags():
    try:
        keywords = request.form.get('keywords', '')
        if not keywords:
            return {'success': False, 'message': 'Please enter some keywords'}
            
        keywords_list = [k.strip() for k in keywords.split(',') if k.strip()]
        generated_tags = []
        
        # Generate tag variations
        for keyword in keywords_list:
            generated_tags.extend([
                keyword,
                f"{keyword} tips",
                f"best {keyword}",
                f"{keyword} 2024",
                f"how to {keyword}",
                f"{keyword} tutorial"
            ])
        
        # Add common tags
        generated_tags.extend([
            "viral",
            "trending",
            "shorts",
            "youtube",
            "subscribe"
        ])
        
        # Deduplicate and limit
        unique_tags = list(set(generated_tags))[:30]
        
        return {'success': True, 'tags': unique_tags}
        
    except Exception as e:
        return {'success': False, 'message': str(e)} 