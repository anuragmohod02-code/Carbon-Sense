import os

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return

    new_content = content.replace('Carbon Sense', 'Carbon Sense')
    new_content = new_content.replace('Carbon-sense', 'Carbon-sense')
    new_content = new_content.replace('carbon-sense', 'carbon-sense')

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

def main():
    directory = r"c:\Users\anura\Downloads\Carbon Sense-main\Carbon Sense-main"
    for root, dirs, files in os.walk(directory):
        if '.git' in root or 'node_modules' in root or '__pycache__' in root:
            continue
        for file in files:
            if file.endswith(('.ts', '.tsx', '.js', '.jsx', '.json', '.md', '.py', '.html')):
                replace_in_file(os.path.join(root, file))

    # Rename directory
    old_dir = os.path.join(directory, 'vscode-ext', 'carbon-sense')
    new_dir = os.path.join(directory, 'vscode-ext', 'carbon-sense')
    if os.path.exists(old_dir):
        os.rename(old_dir, new_dir)
        print(f"Renamed {old_dir} to {new_dir}")

if __name__ == "__main__":
    main()
