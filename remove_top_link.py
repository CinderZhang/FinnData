import re
import os

def remove_top_back_link(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Remove the top "Back to Home" link
    pattern = r'<div class="back-to-home">\s*<a href="index.html">← Back to Home</a>\s*</div>\s*<div class="container">'
    replacement = '<div class="container">'
    modified_content = re.sub(pattern, replacement, content, count=1)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)

# Process files from week1.html to week13.html
for i in range(13, 14):
    file_name = f"week{i}.html"
    if os.path.exists(file_name):
        remove_top_back_link(file_name)
        print(f"Processed {file_name}")
    else:
        print(f"{file_name} not found")

print("All files have been processed.")