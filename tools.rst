Running Python code
===================

If I would like to try out some Python code, for example a hello world
program, then where should I put it?
There are three methods of running Python code:

* IPython (interactive)
* Jupyter Notebook (interactive)
* running the program code from a text file (non-interactive)

IPython
-------

If you just quickly want to try out something, then maybe the easiest
option is to use the IPython interactive shell. To do this,
first start the terminal program to get a command prompt.
Then give the command ``ipython3`` and press enter.
Then you can write Python commands and execute them by pressing enter.
Note that IPython supports tab completion. Try this out
by first writing ``pri`` and then pressing the tabulator key.
It should complete the command to ``print``. IPython can tab complete
keywords; function, module, method, and variable names, and so on.
You can quit the the IPython shell by given the command ``exit`` and
pressing enter.

The following video will show an example session of using IPython.

.. raw:: html
	 
    <script id="asciicast-GssT7MymqOsusdvOqZUgH9JMC"
    src="https://asciinema.org/a/GssT7MymqOsusdvOqZUgH9JMC.js" async>
    </script>

Jupyter notebook
----------------

Again in the command prompt, issue command ``jupyter-notebook``.
It should start the Jupyter server and open a tab in the web browser
that is connected to the server. There you can click the ``new`` button
and select ``Python 3``. Click on the cell, write your Python code
there, and execute it by pressing control-enter.
You can check the following video for introduction to Jupyter notebook:

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/HW29067qVWk"
   frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope;
   picture-in-picture" allowfullscreen>
   </iframe>

The material of this course was written as Jupyter notebooks, and
then rendered as html pages, which you are reading now.
While the static html pages do not allow modification of pieces of
Python code, you can click the 'open in colab' link at the top of the page
to open the notebook in Google's colab service. There it is possible
to edit code and re-execute it.

Alternatively, you can download the notebooks with command
``git clone https://github.com/csmastersUH/data_analysis_with_python_spring_2020``. Then start
Jupyter notebook with command ``jupyter-notebook``.

Executing a file containing Python code
---------------------------------------

In your favorite text editor write some Python code, and save
it to a file with ``.py`` extension, for example ``myprogram.py``. Then you can execute
the program with the command ``python3 myprogram.py``. In all the exercises
of this course you write your solution to a text file (a stub file is provided
where you can add the missing pieces). To run your solution to an exercise, for example
the "hello world" exercise, use ``python3 src/hello_world.py``. This
of course depends on what is your current folder.

If you are running some unix based operation system, like Linux or macOS, you
can make the file directly executable in the following way. Add as the first line of you
program the line ``#!/usr/bin/env python`` and
on command line issue command ``chmod u+x myprogram.py``. Then
you can execute the file from command line with ``./myprogram.py``.

Correct software versions
-------------------------

It can be that the command ``python`` still refers to the old python2 version.
This course relies completely on a newer python version. Therefore I have
used the command ``python3`` everywhere to be sure the old version python2
is not used. You can check the version number with the ``--version`` option.
For example in the following way:

.. code-block:: none
		
    saskeli@dx5-cs-01:$ python --version
    Python 2.7.15rc1
    saskeli@dx5-cs-01:$ python3 --version
    Python 3.6.7

If you have Anaconda correctly installed, then the Python version should
be new enough and ``python`` command should refer to ``python3``, not ``python2``.

The Python version should be at least 3.6. The exercises may work with slightly older 
python versions as well, but you may run into issues with the exercise templates and tests.

The versions of additional libraries that are know to work are:

+--------------+---------+
| Library      + Version |
+==============+=========+
| numpy        | 1.13.3  |
+--------------+---------+
| pandas       | 0.23.0  |
+--------------+---------+
| matplotlib   | 2.1.1   |
+--------------+---------+
| scikit-learn | 0.19.1  |
+--------------+---------+
| scipy        | 0.19.1  |
+--------------+---------+
| seaborn      | 0.8.0   |
+--------------+---------+
| jupyter      | 1.0.0   |
+--------------+---------+


More recent versions should work as well. You can check the software
version of your installation with the following Python script:
`versions.py <https://raw.githubusercontent.com/csmastersUH/data_analysis_with_python_spring_2020/master/versions.py>`_
Download the script and execute it with ``python3 versions.py``.


