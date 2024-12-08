index.html: data.csv
	python3 scripts/generate.py

data.csv:
	python3 scripts/scrape.py

clean:
	rm data.csv
	rm index.html
