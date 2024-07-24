preview_docs:
	@sphinx-autobuild ./doc ./build/html 

install_docs_interpret:
	python3 -m pip install -U Sphinx
	python3 -m pip install sphinx-autobuild
	python3 -m pip install sphinx_rtd_theme
	python3 -m pip install recommonmark
	python3 -m pip install sphinx_markdown_tables
