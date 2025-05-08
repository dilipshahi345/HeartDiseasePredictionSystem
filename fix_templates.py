import os
import re

# ✅ Change this to the path of your Django project directory
project_path = project_path = r"C:\Users\HP\Documents\Heart-Disease-Prediction-System-main"

def convert_ifequal_to_if(content):
    # Replace `{% ifequal a b %}` with `{% if a == b %}`
    content = re.sub(r'{%\s*ifequal\s+([^ ]+)\s+([^ ]+)\s*%}', r'{% if \1 == \2 %}', content)
    # Replace `{% endifequal %}` with `{% endif %}`
    content = content.replace('{% endifequal %}', '{% endif %}')
    return content

for root, dirs, files in os.walk(project_path):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
            updated_content = convert_ifequal_to_if(original_content)
            if original_content != updated_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"✅ Updated: {file_path}")
