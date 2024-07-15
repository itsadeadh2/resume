import markdown, os
import pathlib
from jinja2 import Environment, FileSystemLoader

path = pathlib.Path(__file__).parent.resolve()
env = Environment(loader=FileSystemLoader(path))
template = env.get_template('base.html')

# Read the Markdown file
with open('resume.md', 'r') as file:
    text = file.read()

# Convert to HTML
html_content = {
    'content': markdown.markdown(text)
}

result = template.render(html_content=html_content)

# create build folder
if not os.path.exists('build'):
    os.makedirs('build')

# Save the HTML to a file
with open('build/index.html', 'w') as file:
    file.write(result)
