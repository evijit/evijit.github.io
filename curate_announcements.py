import json
from datetime import datetime

# Read the filtered posts
with open('posts_after_may22.json', 'r') as f:
    posts = json.load(f)

# Curate announcement-worthy posts based on significance
# Looking for: papers, blog posts, workshops, talks, media appearances, major announcements, personal milestones
announcement_worthy = []

# Manual curation based on content significance
significant_posts = [
    # Panel and speaking engagements
    {
        "date": "2025-11-05T10:00:00.000000+00:00",
        "text": "I was on the [Responsible AI podcast with Alex Alben](https://podcasts.apple.com/us/podcast/responsible-ai-from-the-ai-forum/id1733357591)! Genuinely had so much fun talking about how AI could solve human drudgery but it isn't and my bafflement as to why we are not solving problems from the ground up instead of trying to solve sci-fi unknown frontier type problems. Give it a listen!",
        "reason": "Podcast appearance on Responsible AI"
    },
    {
        "date": "2025-11-03T10:48:00.000000+00:00",
        "text": "I had the distinct honor of speaking at a panel entitled 'AI's Effect on the Creative Industries', organized by [All Tech Is Human](https://alltechishuman.org/) and hosted by the Consulate General of Canada in New York. Moderated by Madhavi Singh and with co-panelists Rebecca Ross (Creative Commons), Prithy Ahmed (Standards Canada), and Sarah Robertson (Dorsey Whitney), we looked at the intersection of Generative AI and its impact on the creative industries.",
        "reason": "Panel on AI and Creative Industries"
    },
    # Major announcements and launches
    {
        "date": "2025-10-06T16:28:00.185000+00:00",
        "text": "Our new position paper: AI for scientific discovery is a social problem. We show that culture, incentives, and coordination are the main obstacles to progress, and we are launching the [Hugging Science Initiative](https://huggingface.co/hugging-science) to address this! [Read the paper](https://arxiv.org/abs/2509.06580).",
        "reason": "Major paper + initiative launch"
    },
    {
        "date": "2025-11-01T16:46:55.561000+00:00",
        "text": "Going to San Diego for NeurIPS? We at Eval-Eval, along with the UK AISI, are hosting a closed door state of evals workshop at UC San Diego on Dec 8th. [Request to join](https://evaleval.github.io/events/workshop/)!",
        "reason": "Workshop announcement at NeurIPS"
    },
    {
        "date": "2025-10-17T16:56:37.004000+00:00",
        "text": "We're starting a weekly paper spotlight series! Come engage with the posts and let's improve evals together! First up: [Do Large Language Model Benchmarks Test Reliability?](https://arxiv.org/abs/2410.09555)",
        "reason": "Launch of weekly spotlight series"
    },
    {
        "date": "2025-07-16T17:17:29.891000+00:00",
        "text": "🚨 AI Evals Crisis: Officially kicking off the Eval Science Workstream 🚨 We're building a shared scientific foundation for evaluating AI systems, one that's rigorous, open, and grounded in real-world & cross-disciplinary best practices. [Read our new blog post](https://evalevalai.com/documentation/eval-science-workstream).",
        "reason": "Major initiative launch + blog post"
    },
    {
        "date": "2025-07-15T14:31:00.565000+00:00",
        "text": "New blog post alert! 🚨 [\"What is the Hugging Face Community Building?\"](https://huggingface.co/blog/evijit/what-is-the-hf-community-building), with Yacine Jernite and Irene Soliaman. The AI narrative focuses on big players, but the real story is happening in the open source AI ecosystem across 1.8M models, 450K datasets, and 560K apps on Hugging Face.",
        "reason": "Major blog post publication"
    },
    {
        "date": "2025-08-11T19:47:02.823000+00:00",
        "text": "Remember the discussions around AI Eval plots last week? We at Eval-Eval have a quick [blog post on the AI Eval Charts Crisis](https://evalevalai.com/documentation/eval-charts-crisis)!",
        "reason": "Blog post on important topic"
    },
    {
        "date": "2025-06-17T13:52:43.966000+00:00",
        "text": "Generative AI often renders the user invisible in their limited worldview. Please sign up for a short interactive workshop on AI, Misrepresentation and Mental Health, at both FAccT in Athens, and Alt-FAccT in NYC! Limited space, so hurry! [Sign up here](https://tinyurl.com/ai-mirrors)!",
        "reason": "Workshop at major conferences"
    },
    {
        "date": "2025-09-23T21:07:13.324000+00:00",
        "text": "I'm back at my alma mater Northeastern University today to talk about personal anecdotes of how I have experienced AI, how those experiences fueled my research, and the kind of questions that still remain. Looking forward to it! 🤗 [Event details](https://www.eventbrite.com/e/personal-anecdotes-with-ai-tickets)",
        "reason": "Talk at alma mater"
    },
]

# Sort by date (newest first)
significant_posts.sort(key=lambda x: x['date'], reverse=True)

# Save to file for review
output = {
    "total_posts": len(posts),
    "announcement_worthy": len(significant_posts),
    "announcements": significant_posts
}

with open('announcements_to_review.json', 'w') as f:
    json.dump(output, f, indent=2)

# Print summary
print("=" * 80)
print(f"ANNOUNCEMENT CURATION SUMMARY")
print("=" * 80)
print(f"Total original/quote posts after May 22: {len(posts)}")
print(f"Announcement-worthy posts identified: {len(significant_posts)}")
print("\n" + "=" * 80)
print("PROPOSED ANNOUNCEMENTS (newest first):")
print("=" * 80)

for i, post in enumerate(significant_posts, 1):
    date_obj = datetime.fromisoformat(post['date'])
    print(f"\n{i}. {date_obj.strftime('%Y-%m-%d')}")
    print(f"   Reason: {post['reason']}")
    print(f"   Text: {post['text'][:150]}...")
    print("-" * 80)

print(f"\n\nSaved to: announcements_to_review.json")
print("\nPlease review these and let me know if you'd like to:")
print("  - Add any posts I missed")
print("  - Remove any that shouldn't be announcements")
print("  - Proceed with creating the announcement files")
