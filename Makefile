
.PHONY: reading all
all: reading

reading: reading.html
	mv $< old_$<
	firefox old_$<

reading.html: gnostic_reader.py gnostic.yaml
	python3 $< > $@

gnostic.yaml: gnostic_parser.py dekorne_gnostic_pages
	python3 $<

hexagrams.json: 
	wget raw.githubusercontent.com/ablwr/i-ching/master/js/hexagrams.js -O - \
		| tail -n+2 | head -n-1 | sed 's/},/}/' | sed 's/"111111"/  "111111"/ ' \
		> $@
