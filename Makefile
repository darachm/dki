

gnostic.yaml: dekorne_gnostic_pages
	python3 gnostic_parser.py

hexagrams.json: 
	wget raw.githubusercontent.com/ablwr/i-ching/master/js/hexagrams.js -O - \
		| tail -n+2 | head -n-1 | sed 's/},/}/' | sed 's/"111111"/  "111111"/ ' \
		> $@
