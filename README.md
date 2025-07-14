# Reddit_Persona_Builder_application

# 🧠 Reddit User Persona Builder

This is a Python project that generates a basic **user persona** by analyzing a Reddit user’s recent **posts** and **comments**.

It scrapes a Reddit profile, identifies interests and communication patterns, and saves the result to a `.txt` file with citation links.

---

## 📦 Features

- Takes a Reddit profile URL as input
- Uses Reddit API to fetch recent activity
- Extracts:
  - Interests from post titles
  - Communication style from comments
- Outputs a clean `.txt` file in `outputs/` folder
- Each insight includes citation links

---

## ✅ Setup Instructions (Step-by-Step)

Follow these steps to clone, setup, and run the project:

### 1. Clone the GitHub Repo

```bash
git clone https://github.com/yourusername/reddit-user-persona.git
cd reddit-user-persona

**2. Create and Activate Virtual Environment**
🪟 On Windows:
bash
Copy code
python -m venv venv
venv\Scripts\activate
🍎 On macOS/Linux:
bash
Copy code
python3 -m venv venv
source venv/bin/activate

**3. Install Required Packages**
bash
Copy code
pip install -r requirements.txt

**4. Create .env File**
Create a file named .env in the root folder and add your Reddit API keys:

ini
Copy code
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_USER_AGENT=PersonaBuilderScript by u/yourusername
👉 You can get these credentials by creating an app at: https://www.reddit.com/prefs/apps

**5. Run the Script**
bash
Copy code
python persona_builder.py
When prompted, paste a Reddit profile URL like:

ruby
Copy code
https://www.reddit.com/user/kojied/
The script will:

Fetch the user’s posts and comments

Build a persona

Save the output as outputs/kojied.txt

**📁 Example Outputs**
These files are included in the repo:

outputs/kojied.txt

outputs/Hungry-Move-6603.txt

You can open them to see how the personas look!

**🧾 Requirements**
Install all Python dependencies with:

bash
Copy code
pip install -r requirements.txt
This includes:

praw

python-dotenv

**🧹 .gitignore**
Sensitive files and folders like .env and venv/ are excluded using .gitignore.

✅ PEP-8 Compliant
The code follows PEP-8 Python formatting for readability and best practices.
