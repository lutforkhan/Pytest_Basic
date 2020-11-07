rem is for inactive the command, I have created this bat file in project folder
rem pytest -s -v
rem pytest -s -v -m "sanity"
pytest -s -v -m "sanity" --html=./Reports/report.html
rem -k is used to execute with partial text
pytest -s -v -k "sani" --html=./Reports/report.html khan\