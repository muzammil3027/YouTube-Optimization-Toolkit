from flask import Blueprint, request
import random

title_bp = Blueprint('title_generator', __name__)

power_words = [
    "Ultimate", "Secret", "Pro", "Essential", "2024", 
    "Complete", "Expert", "Surprising", "Amazing", "Hacks"
]

@title_bp.route('/generate-titles', methods=['POST'])
def generate_titles():
    try:
        keywords = request.form.get('keywords', '')
        if not keywords:
            return {'success': False, 'message': 'Please enter some keywords'}
            
        keywords_list = [k.strip() for k in keywords.split(',') if k.strip()]
        generated_titles = []
        
        # Generate title variations
        for keyword in keywords_list:
            generated_titles.extend([
                f"{random.choice(power_words)} {keyword} Guide | {random.choice(['Step-by-Step Tutorial', 'Complete Breakdown'])}",
                f"How to {keyword} {random.choice(['Like a Pro', 'in 2024', 'the Right Way'])}",
                f"{random.randint(5, 15)} {keyword} {random.choice(['Tips & Tricks', 'Mistakes to Avoid', 'Hacks You Need to Know'])}",
                f"{keyword}: {random.choice(['The Complete Tutorial', 'Secrets Revealed', 'From Beginner to Expert'])}",
                f"{random.choice(['WARNING:', 'ALERT:', 'NEW:'])} {keyword} {random.choice(['Changed Everything', 'You Won\'t Believe This'])}",
                f"{keyword} {random.choice(['Masterclass', 'Workshop', 'Bootcamp'])} ({random.choice(['Free Course', 'Limited Time', 'Exclusive'])}!)",
                f"{random.choice(power_words)} {keyword} {random.choice(['Challenge', 'Experiment', 'Comparison'])}",
                f"{keyword} - {random.choice(['What They Don\'t Tell You', 'The Truth About', 'Why You Should'])}",
                f"{random.choice(power_words)} {keyword} {random.choice(['Tutorial', 'Guide', 'Handbook'])} for {random.choice(['Beginners', 'Experts', 'Everyone'])}",
                f"{keyword} {random.choice(['Revealed', 'Exposed', 'Explained'])}: {random.choice(['Must Watch', 'Watch Before It\'s Gone'])}"
            ])
        
        # Remove duplicates and limit to 10 titles
        unique_titles = list(set(generated_titles))[:10]
        
        return {'success': True, 'titles': unique_titles}
        
    except Exception as e:
        return {'success': False, 'message': str(e)} 