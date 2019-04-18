import os

work_path = os.path.dirname(os.path.abspath(__file__))
temp_path = os.path.join(work_path, 'docker-compose_tmp.yml')
target_path = os.path.join(work_path, 'docker-compose.yml')

with open(temp_path, "r") as f:
    content = f.read()
content = content.replace('filepath', work_path)
with open(target_path, "w") as f:
    f.write(content)
