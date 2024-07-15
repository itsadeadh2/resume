import markdown, os

# Read the Markdown file
with open('resume.md', 'r') as file:
    text = file.read()

# Convert to HTML
html_content = markdown.markdown(text)

html_with_a4_styling = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        @page {{
            size: A4;
            margin: 20mm;
        }}
        body {{
            background-color: #d1d1d1;
            width: 300mm;
            height: 297mm;
            margin: auto;
            padding: 10mm;
            box-sizing: border-box;
        }}
    </style>
</head>
<body>
    {html_content}
</body>
</html>
"""

# Save the HTML to a file
with open('index.html', 'w') as file:
    file.write(html_with_a4_styling)
