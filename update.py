import os
from urllib import parse
import requests
from datetime import datetime

HEADER = """# 
# 백준 & 프로그래머스 문제 풀이 목록

"""

def get_last_commit_date(repo, file_path):
    url = f"https://api.github.com/repos/{repo}/commits?path={file_path}"
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()
        if commits:
            last_commit_date = commits[0]['commit']['committer']['date']
            return datetime.strptime(last_commit_date, "%Y-%m-%dT%H:%M:%SZ")
    return None

def main():
    content = ""
    content += HEADER
    
    directories = []
    solveds = []

    repo = "https://github.com/tentiti/BOJ/"  # Replace with your GitHub username and repository name

    for root, dirs, files in os.walk("."):
        dirs.sort()
        if root == ".":
            for dir in (".git", ".github"):
                try:
                    dirs.remove(dir)
                except ValueError:
                    pass
            continue

        category = os.path.basename(root)

        if category == "images":
            continue

        directory = os.path.basename(os.path.dirname(root))

        if directory == ".":
            continue

        if directory not in directories:
            if directory in ["백준", "프로그래머스"]:
                content += "## 📚 {}\n".format(directory)
            else:
                content += "### 🚀 {}\n".format(directory)
                content += "| 문제번호 | 링크 | 푼 날짜 |\n"
                content += "| ----- | ----- | ----- |\n"
            directories.append(directory)

        for file in files:
            if category not in solveds:
                file_path = os.path.join(root, file)
                last_commit_date = get_last_commit_date(repo, file_path)
                if last_commit_date:
                    last_commit_date_str = last_commit_date.strftime("%Y-%m-%d")
                else:
                    last_commit_date_str = "Unknown"
                content += "|{}|[링크]({})|{}|\n".format(
                    category, parse.quote(file_path), last_commit_date_str
                )
                solveds.append(category)
                print("category : " + category)

    with open("README.md", "w") as fd:
        fd.write(content)


if __name__ == "__main__":
    main()
