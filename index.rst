.. Data analysis with Python documentation master file, created by
   sphinx-quickstart on Sat Oct 20 11:30:09 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Data analysis with Python - Spring 2020
==================================================

In this course an overview is given of different phases
of the data analysis pipeline using Python and its data analysis
ecosystem. What is typically done in data analysis? We assume that data is already
available, so we only need to download it. After downloading the
data it needs to be cleaned to enable further analysis. In the
cleaning phase the data is converted to some uniform and consistent
format. After which the data can, for instance, be

* combined or divided into smaller chunks

* grouped or sorted,

* condensed into small number of summary statistics

* numerical or string operations can be performed on the data

The point is to manipulate the data into a form that enables discovery
of relationships and regularities among the elements of data.
Visualization of data often helps to get a better understanding of the data.
Another useful tool for data analysis is machine learning,
where a mathematical or statistical model
is fitted to the data. These models can then be used to make predictions
of new data, or can be used to explain or describe the current data.

Python is a popular, easy to learn programming language.
It is commonly used in the field of data analysis, because
there are very efficient libraries available to process large amounts of data.
This so called *data analysis stack* includes libraries such
of NumPy, Pandas, Matplotlib and SciPy that we will familiarize ourselves
with during this course.

No previous knowledge of Python is needed as will start with
a quick introduction to Python. It is however assumed that
you have good programming skills in some language.
In addition, linear algebra and probability calculus are prerequisites
of this course.
The course lasts for seven weeks and gives 5 credit units.
It is recommended that you do this course in the end of bachelor
degree or in the beginning of masters degree; preferably
before the course "Introduction to Data Science".

Conduct of the course
----------------------

Refer to the `official course page <https://courses.helsinki.fi/fi/aycsm90004en/129239201>`__.

Note that this course requires a lot of work! Depending on your background
it can take something between 5 to 20 hours per week.
In addition to reading the course material, you sometimes may need to consult
the online documentation of Python or its various libraries.

Discussion forum
----------------

A Telegram chat room for the course has been opened. We recommend that you use
the channel either through a web browser or the Telegram desktop application.

You can reach the channel through this link:
`https://t.me/tkt_dap <https://t.me/tkt_dap>`__.
The browser version can be reached here `Telegram <https://web.telegram.org>`__.

The discussion channel is based on peer support. The teachers of the course
are participating in the discussion on voluntary basis if time permits.

Please refrain from posting code or stack traces as text or attachments in the chat room.
Use tmc paste or another paste site instead and just post the link. Also try to avoid
posting complete solutions or spoilers for exercises.


Software libraries used
-----------------------

+--------------+----------------------------------------------------------------+
| Library      + Documentation                                                  |
+==============+================================================================+
| numpy        | `doc <https://docs.scipy.org/doc/numpy/>`_                     |
+--------------+----------------------------------------------------------------+
| pandas       | `doc <http://pandas.pydata.org/pandas-docs/stable/>`_          |
+--------------+----------------------------------------------------------------+
| matplotlib   | `doc <https://matplotlib.org/api/api_overview.html>`_          |
+--------------+----------------------------------------------------------------+
| scikit-learn | `doc <https://scikit-learn.org/stable/>`_                      |
+--------------+----------------------------------------------------------------+
| scipy        | `doc <https://docs.scipy.org/doc/scipy/reference/>`_           |
+--------------+----------------------------------------------------------------+
| jupyter      | `doc <https://jupyter-notebook.readthedocs.io/en/stable/>`_    |
+--------------+----------------------------------------------------------------+


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   instructions
   tools
   faq

.. toctree::
   :maxdepth: 2
   :caption: Week 1:

   basics

.. toctree::
   :maxdepth: 2
   :caption: Week 2:

   basics2
   numpy

.. toctree::
   :maxdepth: 2
   :caption: Week 3:

   numpy2
   matplotlib
   image_processing
   pandas1

.. toctree::
   :maxdepth: 2
   :caption: Week 4:

   pandas2

.. toctree::
   :maxdepth: 2
   :caption: Week 5:

   pandas3
   linear_regression

.. toctree::
   :maxdepth: 2
   :caption: Week6:

   bayes
   clustering
   pca

.. toctree::
   :maxdepth: 2
   :caption: Week7:

   project



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
