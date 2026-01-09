import json
from datetime import datetime
import re

# Read the filtered posts
with open('posts_after_may22.json', 'r') as f:
    posts = json.load(f)

# Define which posts should become announcements (newsworthy ones)
# I'll filter for posts that mention papers, blog posts, workshops, talks, etc.
announcement_keywords = [
    'paper', 'blog post', 'workshop', 'talk', 'podcast', 'article',
    'interview', 'event', 'announcement', 'launch', 'dataset',
    'initiative', 'project', 'Common Pile', 'Hugging Science',
    'eval-eval', 'spotlight', 'watermark', 'FAccT', 'NeurIPS',
    'married', 'wedding', 'husband', 'engagement'
]

def is_newsworthy(text):
    """Check if a post is newsworthy based on content"""
    text_lower = text.lower()
    
    # Check for keywords
    for keyword in announcement_keywords:
        if keyword.lower() in text_lower:
            return True
    
    # Check for URLs (often indicates sharing content)
    if 'http' in text or '.com' in text or '.org' in text or '.co/' in text:
        return True
    
    return False

# Filter newsworthy posts
newsworthy_posts = []
for post in posts:
    if is_newsworthy(post['text']):
        newsworthy_posts.append(post)

print(f"Found {len(newsworthy_posts)} newsworthy posts")

# Start numbering from 50 (after announcement_49.md)
start_number = 50

# Generate announcement files
for i, post in enumerate(newsworthy_posts):
    announcement_num = start_number + i
    date_obj = datetime.fromisoformat(post['date'])
    
    # Format date for Jekyll (YYYY-MM-DD HH:MM:SS-TIMEZONE)
    formatted_date = date_obj.strftime('%Y-%m-%d %H:%M:%S-0400')
    
    # Clean the text
    text = post['text']
    
    # Create the announcement content
    content = f"""---
layout: post
date: {formatted_date}
inline: true
related_posts: false
---

{text}
"""
    
    # Write to file
    filename = f"_news/announcement_{announcement_num}.md"
    with open(filename, 'w') as f:
        f.write(content)
    
    print(f"Created {filename}")
    print(f"  Date: {formatted_date}")
    print(f"  Text: {text[:100]}...")
    print()

print(f"\nTotal announcements created: {len(newsworthy_posts)}")
print(f"Files: announcement_{start_number}.md to announcement_{start_number + len(newsworthy_posts) - 1}.md")
