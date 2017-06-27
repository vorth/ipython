---
---
# Visual Math with iPython

![woven hendecagram image]({{ site.github.url }}/hendecagrams.png)

The [Github repository](https://github.com/vorth/ipython)
hosting this page contains several [iPython/Jupyter](https://ipython.org/) notebooks,
each one using Python code to visually explore the Mathematics of algebraic fields.
All of the notebooks can be viewed online, using [Jupyter nbviewer](http://nbviewer.jupyter.org/),
which renders notebooks hosted on Github or elsewhere.

Since iPython is very good for combining explanatory text, figures, and code,
the notebooks largely speak for themselves.
This is certainly true for this three part series on numbers derived from the regular heptagon,
and how to draw interesting figures with them:

* [Part 1: Heptagon Numbers](http://nbviewer.jupyter.org/github/vorth/ipython/blob/master/heptagons/HeptagonNumbers.ipynb)
* [Part 2: Drawing the Heptagon](http://nbviewer.jupyter.org/github/vorth/ipython/blob/master/heptagons/DrawingTheHeptagon.ipynb)
* [Part 3: Heptagon Rotations](http://nbviewer.jupyter.org/github/vorth/ipython/blob/master/heptagons/Sevenfold%20Rotation.ipynb)

Another notebook documents the code and techniques I used to generate the
[woven hendecagrams](http://nbviewer.jupyter.org/github/vorth/ipython/blob/master/hendecagons/Hendecagons.ipynb)
poster that was my exchange gift for
[G4G11](http://www.gathering4gardner.org/g4g11-2014-recap/).
This notebook is not written with such care and attention to pedagogy as those listed above,
but it does have all of the Python code, and *some* explanation of it.

There are a few more notebooks in the repo, and all can be [viewed with
nbviewer](http://nbviewer.jupyter.org/github/vorth/ipython/tree/master/),
but they are little more than code and possibly some notes.
I'll post updates if/when I develop them further.

I should note that iPython/Jupyter is itself an environment
for editing and debugging Python code (or other languages),
if you [install it on your computer](https://jupyter.readthedocs.io/en/latest/install.html).
The best way to experiment with the code in these notebooks is to work with
them in iPython itself, the same way I developed them.

{% for post in site.posts %}
* [{{ post.title }}]({{ post.url | prepend: site.github.url }})
{% endfor %}

![heptanautiloid]({{ site.github.url }}/heptanautiloid.png)

