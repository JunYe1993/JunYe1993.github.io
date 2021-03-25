## Python Module Install ##
---
#### Windows ####
```bash
pip install requests
pip install beautifulsoup4
pip install lxml
pip install markdown
```
#### Ubuntu ####
```bash
sudo apt-get update -y
sudo apt-get install -y python-requests
sudo apt-get install -y python-beautifulsoup
sudo apt-get install -y python-lxml
pip3 install markdown
```
#### Tool/subModule ####
* tool/html2markdown/html2text (v3.02)
## Usage ##
---
### Sync blogger ###
```bash
python -m tool.sync.run_sync
```
### Convert article/\*\*/\*.html to article/\*\*/\*.md (still working)###
```bash
python -m tool.html2markdown.run_html2markdown
```
### Convert markdown to html
```bash
python -m tool.markdown2html.run_markdown2html [file]
```