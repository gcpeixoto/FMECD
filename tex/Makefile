nbs = $(wildcard *.ipynb)
texs = $(nbs:%.ipynb=%.tex)

hide: $(texs)

%.tex: %.ipynb
	jupyter-nbconvert --to latex --template hidecode.tplx $<;
