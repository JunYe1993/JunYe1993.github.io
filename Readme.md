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
### Convert markdown to html
```bash
python -m tool.markdown2html.run_markdown2html [file]
```
## Work with API (need [install google python api env][googlePythonAPI]) ##
---
### Upload markdown file to blog 
```bash
python -m tool.manuscript.run_upload [file]
```
### Upload/Update series to blog 
```bash
python -m tool.series.updateSeries [file]
```

[googlePythonAPI]: https://github.com/JunYe1993/Google_API_Python