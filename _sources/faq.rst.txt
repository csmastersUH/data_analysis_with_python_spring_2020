Frequently asked questions
==========================

When logging to tmc first time, whats the server address it asks?
-----------------------------------------------------------------

Your TMC client is old, load newest version from
`tmc-cli <https://github.com/testmycode/tmc-cli>`_

tmc not found
-------------

You installed the TMC client successfully, but the program is not
found when you say ``tmc`` in the command prompt.
If you are using Windows, use the ``doskey`` program so that tmc
can be found even if you are not in the same folder as the ``tmc``
executable. For instructions, see `tmc-cli <https://github.com/testmycode/tmc-cli>`_.

If you are using Linux, then you may have close the terminal window
and open a new one. Or alternatively, run ``source ~/.bashrc``.

`tmc test` says: "Test results: 0/0 tests passed"
-------------------------------------------------

If the output is
Test results: 0/0 tests passed
All tests passed! Submit to server with 'tmc submit'
Then several things can be wrong.

First make sure that the program run correctly, e.g.
``python3 src/hello_world.py``.
If it crashes, then ``tmc`` will most likely give the above message.

If the program does not crash, you are using Windows, and you
have installed Anaconda, then possibly TMC cannot find Anaconda installation.
Make sure you use TMC version at least 0.9.2. You can check the
version of TMC with ``tmc --version``. If it still does not work, then try to
activate Anaconda. To achieve this check the question:
ModuleNotFoundError: No module named ‘somelibrary’

What version of Python should I use? What is the name of the executable?
------------------------------------------------------------------------

The Python version should be at least 3.6. You can check your version with
``python3 --version`` on Linux or macOS, and with ``python --version`` on Windows.
Note: on Linux the program ``python`` might refer to an old Python version 2.
Don't ever use that!

How to load a file that resides in the src folder?
--------------------------------------------------

If you want to open a file ``file.txt`` that resides in the ``src`` folder, use the provided
function ``get_path`` like in ``open(get_path("file.txt"))``. But if you are requested
to write a function, say ``f``, that gets a filename as a parameter, then calling
``get_path`` is the responsibility of the caller of ``f``. If the filename comes from
the command line parameters (``sys.argv``), then it is the responsibility of the person
who runs the program to provided correct path, like ``src/file.txt`` (no call to ``get_path``
is involved in this case).

Make sure the ``get_path`` function has the following definition. The command ``tmc update``
cannot modify files in the ``src`` folder, so the function definition cannot be automatically updated.
Now it should work also on Windows.

::
   
   def get_path(filename):
       import sys
       import os
       return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

Note: the ``get_path`` contruct does not work in Jupyter, as the
first command line parameter (``sys.argv[0]``) in Jupyter does not refer
to your program (``myprogram.py``), but instead to a certain system program.


Tests complain about missing attribute assert_called, assert_called_once, ...
-----------------------------------------------------------------------------

These require at least Python version 3.6. Check your installation. See the next question.

ModuleNotFoundError: No module named 'somelibrary'
--------------------------------------------------

The libraries needed in the course (numpy, pandas, matplotlib, scikit-learn, scipy, seaborn, and statsmodels)
are contained in the Anaconda distribution. Either you haven't installed Anaconda or
it hasn't been activated.

On Windows you it may help, if you use 'Anaconda prompt' from the Windows menu.
That should activate Anaconda automatically.

If you don't want to use 'Anaconda prompt', then in command prompt
try ``where python`` to see if it finds Python under
Anaconda's folder. If not, try to activate Anaconda with
``C:\Users\<username>\AppData\Local\Continuum\Anaconda3\Scripts\activate``
Or something similar, depending where you installed it.

On Linux/macOS:

You can check whether Anaconda is active with the command ``which python3``.
If the python3 binary is under anaconda3 folder, then Anaconda is active.
If you are sure you have already installed Anaconda, then
you can activate it with

* ``conda activate``, or

* ``~/acaconda3/bin/conda activate`` (or where ever Anaconda is installed)

* On older Anaconda distributions use: ``source ~/anaconda3/bin/activate``

Then try again ``which python3``.


I cannot understand the error message from a failed test case
-------------------------------------------------------------

First run ``tmc update`` to make sure I haven't already fixed that
issue. If the problem persists, make a bug report in:

* Telegram: `https://t.me/dap19s <https://t.me/dap19s>`__

* Github `issues <https://github.com/jttoivon/data-analysis-with-python-spring-2019/issues>`__

* Give feedback, when using ``tmc submit``

  
