import json
from datetime import datetime, timezone
import os

# Read the JSON file
with open('/Users/avijit/Downloads/evijit.io_all_posts.json', 'r') as f:
    data = json.load(f)

# Cutoff date: May 22, 2025 (make it timezone aware)
cutoff_date = datetime(2025, 5, 22, tzinfo=timezone.utc)

# Filter posts after May 22, 2025
# Only include original posts and quote posts, not replies or reposts
filtered_posts = []
for item in data:
    if 'post' in item and item['post']:
        post = item['post']
        if 'record' in post and 'createdAt' in post['record']:
            record = post['record']
            
            # Skip if this is a reply (has reply field in record)
            if 'reply' in record:
                continue
            
            # Skip if this is a repost (doesn't have text)
            text = record.get('text', '').strip()
            if not text:
                continue
            
            # Parse the creation date
            created_at_str = record['createdAt']
            created_at = datetime.fromisoformat(created_at_str.replace('Z', '+00:00'))
            
            if created_at > cutoff_date:
                # Check if there's an embed (for quote posts)
                has_embed = 'embed' in record
                
                filtered_posts.append({
                    'date': created_at,
                    'text': text,
                    'has_embed': has_embed,
                    'uri': post.get('uri', ''),
                    'cid': post.get('cid', '')
                })

# Sort by date (newest first)
filtered_posts.sort(key=lambda x: x['date'], reverse=True)

# Print the filtered posts
print(f"Found {len(filtered_posts)} original/quote posts after May 22, 2025\n")
print("=" * 80)
for i, post in enumerate(filtered_posts, 1):
    post_type = "Quote post" if post['has_embed'] else "Original post"
    print(f"\nPost {i} ({post_type}):")
    print(f"Date: {post['date'].strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Text: {post['text'][:200]}{'...' if len(post['text']) > 200 else ''}")
    print("-" * 80)

# Save to a clean JSON for review
with open('/Users/avijit/Library/CloudStorage/GoogleDrive-avijitg22@gmail.com/My Drive/evijit.github.io/posts_after_may22.json', 'w') as f:
    json.dump([{
        'date': p['date'].isoformat(),
        'text': p['text'],
        'has_embed': p['has_embed']
    } for p in filtered_posts], f, indent=2)

print(f"\n\nSaved {len(filtered_posts)} original/quote posts to posts_after_may22.json")
