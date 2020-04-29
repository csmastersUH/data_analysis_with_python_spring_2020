Frequently asked questions
==========================

When logging to tmc first time, whats the server address it asks?
-----------------------------------------------------------------

Your TMC client is old, load newest version from
`tmc-cli <https://github.com/testmycode/tmc-cli>`_

TMC login crashes (with mention of tmc-cli.log)
-----------------------------------------------

Your java version is probably too old. If you want, you can check the log file that should be
located in ``<user.home>/.config/tmc-cli/logs``. There should be mention of ``SSLHandshakeException``
or similar security related exceptions. In this case you should update to a newer version of java.

For java 8, at least open jdk 1.8.0_212 and 1.8.0.211 work. All java 11 and 12 version should work.

TMC test fails but all other commands (including submit) work
-------------------------------------------------------------

If you are using Windows and a fairly new installation of conda, you have fallen pray to a bug in
conda. The python environment variables are not properly set for tmc to be able to run the tests.
You can use ``python -m tmc`` in the project root instead. So in the folder where e.g. ``python src/hello_world.py``
works as expected the command ``python -m tmc`` should run tmc tests properly.

This workaround shouldn't be needed after the next version of conda is released.

Stuff generally doesn't seem to work in the conda prompt on Windows
-------------------------------------------------------------------

Some environment variables apparently may not be properly set in the conda prompt directly after install. Try rebooting your system.

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

TMC runs code from the project root. So for python to find ``file.txt``, you need to pass it
the folder as well. That is ``src/file.txt``.

However, if you are requested to write a function, say ``f``, that gets a filename as a parameter,
then setting the correct file path is the responsibility of the caller of ``f``. If the filename comes from
the command line parameters (``sys.argv``), then it is the responsibility of the person
who runs the program to provide the correct path, like ``src/file.txt``.

Tests complain about missing attribute assert_called, assert_called_once, ...
-----------------------------------------------------------------------------

These require at least Python version 3.6. Check your installation. See the next question.

ModuleNotFoundError: No module named 'somelibrary'
--------------------------------------------------

The libraries needed in the course (numpy, pandas, matplotlib, scikit-learn, scipy, seaborn, and statsmodels)
are contained in the Anaconda distribution. Either you haven't installed Anaconda or
it hasn't been activated.

On Windows it may help, if you use 'Anaconda prompt' from the Windows menu.
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

* Telegram: `https://t.me/tkt_dap <https://t.me/tkt_dap>`__

* Github `issues <https://github.com/csmastersUH/data_analysis_with_python_spring_2020/issues>`__

* Give feedback, when using ``tmc submit``

Note that reporting that "tests should be better" doesn't really help. Please try to be more specific with bug reports. You can for example consider the following:

* What was the error message?

* What was the actual issue if you managed to fix it?

* Link to non-working code

* If reported via Github or Telegram: **What was the exercise in question?**
