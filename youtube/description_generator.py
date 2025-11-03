from flask import Blueprint, request
import random

desc_bp = Blueprint('description_generator', __name__)

templates = [
    """In this comprehensive {keyword} tutorial, we'll dive deep into everything you need to know to master {keyword} in 2024. Whether you're a beginner looking to learn the basics or an experienced user seeking advanced techniques, this video has you covered!

📌 What You'll Learn:
- Step-by-step guide to getting started with {keyword}
- Professional tips and tricks from industry experts
- Common mistakes to avoid when working with {keyword}
- Advanced strategies for optimizing your {keyword} workflow
- Latest tools and resources for {keyword} in 2024

🕒 Video Timestamps:
00:00 - Introduction to {keyword}
03:15 - Basic concepts explained
07:45 - Setting up your {keyword} environment
12:30 - Core techniques demonstration
18:00 - Advanced optimization methods
22:45 - Troubleshooting common issues
25:30 - Q&A session

🔥 Why This Matters:
{keyword} has become an essential skill in today's digital landscape. With over 2 million monthly searches on Google, mastering {keyword} can help you:
- Improve your productivity by 40%
- Enhance your professional skill set
- Stay competitive in your industry
- Unlock new career opportunities

💡 Pro Tips:
1. Always start with a clear {keyword} strategy
2. Use tools like [Tool Name] for better results
3. Regularly update your {keyword} knowledge
4. Join online communities for {keyword} enthusiasts
5. Practice daily to maintain your skills

📚 Recommended Resources:
- Best book for {keyword}: [Affiliate Link]
- Top online course: [Affiliate Link]
- Essential tools: [Tool 1], [Tool 2], [Tool 3]
- Helpful browser extensions: [Extension 1], [Extension 2]

👥 Connect With Us:
- Join our {keyword} Facebook Group: [Link]
- Follow on Instagram @{keyword}Experts: [Link]
- Subscribe to our newsletter: [Link]

❓ Frequently Asked Questions:
Q: How long does it take to learn {keyword}?
A: Most students become proficient in 4-6 weeks with daily practice

Q: What's the best way to practice {keyword}?
A: Try our free {keyword} challenges at [Link]

Q: Can I make money with {keyword}?
A: Absolutely! Check our monetization guide: [Link]

🔔 Don't Forget To:
- LIKE if you found this helpful
- SUBSCRIBE for weekly {keyword} content
- Click the BELL to get notifications
- SHARE with friends who need this

📌 Video Hashtags:
#{keyword} #{keyword}Tips #{keyword}2024 #{keyword}Tutorial Learn{keyword} {keyword}ForBeginners

💬 Comment Below:
What {keyword} topic should we cover next? Let us know!""",

    """🚀 ULTIMATE {keyword} GUIDE 2024 | Complete Walkthrough + Free Resources 🎁

In this massive 5000+ word tutorial (30+ minute video), you'll get:
✅ Complete A-Z {keyword} implementation
✅ 7 Practical real-world examples
✅ 15 Professional tips from top experts
✅ Free downloadable {keyword} cheat sheet
✅ Exclusive access to our {keyword} community

📊 Why {keyword} Matters in 2024:
- 78% of businesses now use {keyword} (Source: TechReport 2024)
- {keyword} professionals earn 35% more on average
- Global {keyword} market expected to reach $XX billion by 2025

🔧 Tools We Recommend:
1. [Tool Name] - Best for beginners
2. [Tool Name] - Professional grade solution
3. [Tool Name] - Free open source alternative

📈 Key Statistics:
- Companies using {keyword} see 45% faster growth
- 92% of users report improved efficiency
- Average ROI of {keyword} implementation: 300%

🎓 Learning Path:
1. Basic {keyword} concepts (Week 1-2)
2. Intermediate techniques (Week 3-4)
3. Advanced optimization (Week 5-6)
4. Real-world projects (Week 7-8)

📥 Download Resources:
- {keyword} Checklist PDF
- Practice Project Files
- Expert Interview Transcripts
Get them all here: [Resource Link]

👨💻 About Your Instructor:
John Doe has 10+ years of {keyword} experience, having worked with companies like Google, Microsoft, and NASA. He's certified in {keyword} professional development and has taught over 50,000 students worldwide.

⭐ Video Highlights:
- 12:35 - Critical mistake 90% of beginners make
- 18:20 - Secret optimization technique
- 25:10 - Live case study breakdown
- 32:45 - Future of {keyword} predictions

📣 Disclaimer:
Some links are affiliate links that help support our channel at no extra cost to you. We only recommend products we truly believe in!

✉️ Business Inquiries:
For sponsorships and partnerships: contact@example.com

🔗 Helpful Links:
- Full {keyword} documentation: [Link]
- Certification programs: [Link]
- Industry forums: [Link]

📌 SEO-Optimized Tags:
{keyword}, {keyword} tutorial 2024, learn {keyword} fast, {keyword} for beginners, advanced {keyword} techniques, {keyword} certification, {keyword} tools review, {keyword} best practices

👍 Enjoyed This? Watch Next:
- "Master Advanced {keyword} in 30 Days"
- "{keyword} vs Alternative Methods Comparison"
- "Top 10 {keyword} Tools for 2024"

📲 Follow Us:
- TikTok: @{keyword}Hacks
- Twitter: @{keyword}Updates
- LinkedIn: {keyword} Professionals Group

🎵 Music Credits:
- "Productive Morning" by RoyaltyFreeTunes
- "Tech Background" by AudioJungle

❤️ Support Our Channel:
- Patreon: [Link]
- Buy Me a Coffee: [Link]
- Amazon Wishlist: [Link]

⚠️ Copyright Notice:
Content is protected under DMCA. Unauthorized reproduction is prohibited."""
]

@desc_bp.route('/generate-descriptions', methods=['POST'])
def generate_descriptions():
    try:
        keywords = request.form.get('keywords', '')
        if not keywords:
            return {'success': False, 'message': 'Please enter some keywords'}
        
        keyword = keywords.split(',')[0].strip()
        related_keyword = f"advanced {keyword}"  # Generate related keyword
        
        descriptions = []
        
        for _ in range(10):
            template = random.choice(templates)
            description = template.format(keyword=keyword, related_keyword=related_keyword)
            descriptions.append(description)
        
        return {'success': True, 'descriptions': list(set(descriptions))[:10]}
        
    except Exception as e:
        return {'success': False, 'message': str(e)} 