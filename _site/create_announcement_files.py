import json
from datetime import datetime

# Read the curated announcements
with open('announcements_to_review.json', 'r') as f:
    data = json.load(f)

announcements = data['announcements']

# Reverse the list so oldest comes first (will get lower numbers)
# and newest comes last (will get higher numbers)
announcements_reversed = list(reversed(announcements))

# Start numbering from 50 (after announcement_49.md)
start_number = 50

# Generate announcement files
for i, post in enumerate(announcements_reversed):
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

print(f"\nTotal announcements created: {len(announcements_reversed)}")
print(f"Files: announcement_{start_number}.md to announcement_{start_number + len(announcements_reversed) - 1}.md")
