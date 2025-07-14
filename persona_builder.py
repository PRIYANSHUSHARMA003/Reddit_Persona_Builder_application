import os
from dotenv import load_dotenv
import praw

# Load the .env file
load_dotenv()

# Setup Reddit API
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)



def extract_username(url):
    return url.rstrip('/').split('/')[-1]

def get_user_data(username):
    user = reddit.redditor(username)
    posts, comments = [], []
    
    # Get latest 50 posts
    for post in user.submissions.new(limit=50):
        posts.append({
            'title': post.title,
            'body': post.selftext,
            'url': post.url
        })

    # Get latest 100 comments
    for comment in user.comments.new(limit=100):
        comments.append({
            'body': comment.body,
            'link': f"https://www.reddit.com{comment.permalink}"
        })

    return posts, comments

def build_persona(posts, comments, username):
    persona = f"USER PERSONA FOR: u/{username}\n\n"

    persona += "LIKELY INTERESTS:\n"
    for post in posts[:5]:
        persona += f"- {post['title']} (Post: {post['url']})\n"

    persona += "\nCOMMUNICATION STYLE:\n"
    for comment in comments[:5]:
        persona += f"\"{comment['body']}\" (From: {comment['link']})\n"

    return persona

def save_persona(username, persona_text):
    if not os.path.exists('outputs'):
        os.mkdir('outputs')
    file_path = f"outputs/{username}.txt"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(persona_text)
    print(f"Saved persona to {file_path}")

def main():
    url = input("Enter Reddit profile URL: ")
    username = extract_username(url)
    posts, comments = get_user_data(username)
    persona = build_persona(posts, comments, username)
    save_persona(username, persona)

if __name__ == "__main__":
    main()
