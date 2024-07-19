import markdown
import pathlib
from flask import Blueprint, render_template
from tireless import app

page = Blueprint('page', __name__, template_folder='templates', static_folder='static')


@app.route('/')
def index():
    contents = pathlib.Path('contents', 'README.md')

    # Open the scroll (replace 'spellbook.md' with your actual file)
    with open(contents, 'r', encoding="utf-8") as scroll:
        markdown_content = scroll.read()

    # Invoke the Python-Markdown spell
    html_content = markdown.markdown(markdown_content)

    return render_template('page.j2', contents=html_content)

