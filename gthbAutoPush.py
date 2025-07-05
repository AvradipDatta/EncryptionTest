import os

# Navigate to project directory
os.chdir(r'D:\Study\My Project\GitHubEncryption')  # replace with your project folder path

# Git commands
os.system('git init')
os.system('git remote add origin https://github.com/AvradipDatta/EncryptionTest.git')
os.system('git add .')
os.system('git commit -m "Add encrypted file"')
os.system('git branch -M main')
os.system('git push -u origin main')
