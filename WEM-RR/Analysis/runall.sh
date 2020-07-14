#!/bin/bash


# convert EVERY ipynb to a python file
find . -name mfpt.ipynb -execdir jupyter-nbconvert {} --to python \;
# remove the code that is specific to jupyter notebooks (inline and show plot)
find . -name mfpt.py -exec sed -i -e 's/\(^.*inline\)/#\1/' -e '/plt.show/d' {} \;

# run all of them, 8 at a time
find . -name mfpt.py | xargs -n 1 -I{} -P8 \
	bash -c 'cd $(dirname {}) ; python2 $(basename {}) &> log.log ; echo DONE ; date' 

