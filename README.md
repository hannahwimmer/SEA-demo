# Some general notes

I'm using `uv` for package management - please do so, too. Some helpful basic commands
are:
- `uv init`: for initializing an empty folder as a project
- `uv add <package_name>`: to add a specific package to your venv
- `source .venv/bin/activate`: to activate your venv
- `deactivate`: to deactivate your venv


For streamlit, use the `pages` project structure, i.e., a folder called `pages` in your
root folder, which contains individual python scripts for each single topic (or 
algorithm, in our case). You just run everything from a main file (like in my case, my
`Home.py` script) in root via:

- `streamlit run Home.py` (or `main.py`, or however you call it)

Streamlit will identify the setup and automatically display all your individual pages in
a sidebar. Pretty neat, but as a con, it will take your files' names as the names of the
pages, so take care how you name your files.

For my short demo, I implemented the random search algorithm and did a short streamlit
page like I'd expect you to do for the other algorithms. Add a new page for every
algorithm; do it as elaborate or simplistic as you want/have the time. Doesn't need to
be a book, just needs to concisely summarize the topic in a meaningful way. If you have
time, try playing around with streamlit - it's a cool tool, and there's lots of
[documentation](https://docs.streamlit.io/develop/api-reference).