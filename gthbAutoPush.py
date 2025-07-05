import os

# Navigate to project directory
os.chdir(r'D:\Study\My Project\GitHubEncryption')  # replace with your path

# Git commands

# Initialize only if .git doesn't exist
if not os.path.exists(".git"):
    os.system('git init')

# Remove existing origin and add again (safe)
os.system('git remote remove origin')
os.system('git remote add origin https://github.com/AvradipDatta/EncryptionTest.git')

# Stage all changes
os.system('git add .')

# Commit changes
os.system('git commit -m "Add encrypted file"')

# Pull remote changes with rebase to integrate histories
# Allow unrelated histories if this is first pull
os.system('git pull origin main --allow-unrelated-histories --rebase')

# Push changes
os.system('git branch -M main')
os.system('git push -u origin main')
