import re
from datetime import date

with open('spanwatch-dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

today = date.today().strftime('%Y-%m-%d')

content = re.sub(
    r'const LAST_CHECKED = "[^"]+";',
    f'const LAST_CHECKED = "{today}";',
    content
)

with open('spanwatch-dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Updated LAST_CHECKED to {today}")
