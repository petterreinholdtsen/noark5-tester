all: mangler.pdf

mangler-liste.xml: *.md Makefile
	rm -f mangler-liste.xml
	( echo "<?xml version='1.0' encoding='UTF-8'?>" ; \
	  echo '<chapter><title>Mangeloversikt</title>' ; \
	  for f in 2*.md; do \
		cat $$f; \
		echo ; \
	  done | pandoc -f markdown+ascii_identifiers -t docbook $$f ; \
	  echo '</chapter>' ; \
	) > mangler-liste.xml

validate-docbook: mangler.xml mangler-liste.xml Makefile
	xmllint --xinclude --postvalid mangler.xml
mangler.pdf: validate-docbook mangler.xml mangler-liste.xml Makefile
	dblatex mangler.xml

clean:
	$(RM) mangler-liste.xml *~
distclean: clean
	$(RM) mangler.pdf
