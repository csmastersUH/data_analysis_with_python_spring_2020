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

Passing the course
------------------

From the weekly programming exercises you need to get 80% of the points.
If you succeed in this, then you can start doing the project work
(approximately 1 cu of work). After the project work and
its peer reviewing is done, the you can take part in the final
exam. The final exam consists of multiple choice questions on the
themes discussed in the exercises. The final grade will be based
on the project work, its peer review, and the exam.

Programming exercises form the 4 cu massive open online part of the course
(MOOC). We provide a certificate for passing this part. After completing the
programming exercises, certificates are available from the
`TMC website <https://tmc.mooc.fi/>`__, under the user page.
Project work, its peer-review and exam are only available for
`enrolled students <https://courses.helsinki.fi/fi/aycsm90004en/>`__. These are
required for getting the course marked with a grade and registered as a 5 cu
course taken at the University of Helsinki.

Note that this course requires a lot of work! Depending on your background
it can take something between 5 to 20 hours per week.
In addition to reading the course material, you sometimes may need to consult
the online documentation of Python or its various libraries.

Schedule
--------

Every week there are 15 - 20 programming exercises that you must
solve and then submit to the TMC system for checking.
In order to continue with next week's exercises, you
need to get 80% of the **points** from exercises of the previous week.
Note that from some exercises it is possible to get more than one point.
These exercises are divided into *parts*, where the parts are shown
as Part 1, Part 2, etc. Each part gives one point.
It is possible to submit, and get points for,
an exercise you have completed at least partly.
You can check your points from the `TMC server <https://tmc.mooc.fi/org/hy/courses/488>`__.

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

+--------------+---------------------------------------------------------+
| Library      + Documentation                                           |
+==============+=========================================================+
| numpy        | `doc <https://docs.scipy.org/doc/numpy/>`_              |
+--------------+---------------------------------------------------------+
| pandas       | `doc <http://pandas.pydata.org/pandas-docs/stable/>`_   |
+--------------+---------------------------------------------------------+
| matplotlib   | `doc <https://matplotlib.org/api/api_overview.html>`_   |
+--------------+---------------------------------------------------------+
| scikit-learn | `doc <https://scikit-learn.org/stable/>`_               |
+--------------+---------------------------------------------------------+
| scipy        | `doc <https://docs.scipy.org/doc/scipy/reference/>`_    |
+--------------+---------------------------------------------------------+





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
