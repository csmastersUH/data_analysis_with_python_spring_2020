.. Data analysis with Python documentation master file, created by
   sphinx-quickstart on Sat Oct 20 11:30:09 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Data analysis with Python - Spring 2019
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

Note that this course requires a lot of work! Depending on your background
it can take something between 5 to 20 hours per week.
In addition to reading the course material, you sometimes may need to consult
the online documentation of Python or its various libraries.

Schedule
--------

Every week there are 15 - 20 programming exercises that you must
solve and then submit to the TMC system for checking.
In order to continue with next week's exercises (and on this course), you
need to get a certain percentage of the **points** from exercises of the previous week.
These requirements are specified in the below table for each exercise week.
Note that from some exercises it is possible to get more than one point.
These exercises are divided into *parts*, where the parts are shown
as Part 1, Part 2, etc. Each part gives one point.
It is possible to submit, and get points for,
an exercise you have completed at least partly.
You can check your points from the `TMC server <https://tmc.mooc.fi/org/hy/courses/438>`__.
The deadlines, shown below, are hard and no exceptions will be made,
so finish and submit your solutions early.

Teaching workshop (pajaopetus) will be held weekly in Exactum building
in Kumpula in room B221 on Thurdays 10.00 - 12.00 (14.3. - 5.5.).

+------+-----------------+-----------------+----------------------+
| Week | Deadline        | Points required | Theme                |
+======+=================+=================+======================+
| 1    | 18.3.2019 23.59 |     80%         | Basics of Python I   |
+------+-----------------+-----------------+----------------------+
| 2    | 25.3.2019 23.59 |     80%         | Basics of Python II, |
|      |                 |                 | NumPy I              |
+------+-----------------+-----------------+----------------------+
| 3    | 1.4.2019 23.59  |     80%         | NumPy II,            |
|      |                 |                 | Visualization,       |
|      |                 |                 | Image processing,    |
|      |                 |                 | Data Analysis        |
|      |                 |                 | with Pandas I        |
+------+-----------------+-----------------+----------------------+
| 4    | 8.4.2019 23.59  |     75%         | Data Analysis        |
|      |                 |                 | with Pandas II       |
+------+-----------------+-----------------+----------------------+
| 5    | 15.4.2019 23.59 |     70%         | Data Analysis        |
|      |                 |                 | with Pandas III,     |
|      |                 |                 | Machine learning I   |
+------+-----------------+-----------------+----------------------+
| 6    | 29.4.2019 23.59 |     65%         | Machine learning II, |
|      |                 |                 | Project              |
+------+-----------------+-----------------+----------------------+
| 7    | 6.5.2019 23.59  |                 | Project continues    |
+------+-----------------+-----------------+----------------------+
| 8    | 13.5.2019 23.59 |                 | Peer review,         |
|      |                 |                 | Exam                 |
+------+-----------------+-----------------+----------------------+

Renewal course in May
---------------------

The instructions are the same except for the points mentioned below.
There is a single deadline for the exercises, but the exercises unlock
only after the specified amount of points is achieved from the previous week.
Use command ``tmc download hy-dap-spring-2019-renewal`` to download the exercises.
You can check your points from the `TMC server <https://tmc.mooc.fi/org/hy/courses/465>`__.
The deadlines, shown below, are hard and no exceptions will be made,
so finish and submit your solutions early.

No teaching workshop will be held.

There is a Telegram group for this renewal course at
`https://t.me/dap19srenewal <https://t.me/dap19srenewal>`__.
The browser version can be reached here `Telegram <https://web.telegram.org>`__.

+------+-----------------+-----------------+----------------------+
| Week | Deadline        | Points required | Theme                |
+======+=================+=================+======================+
| 1    | 15.5.2019 23.59 |     80%         | Basics of Python I   |
+------+-----------------+-----------------+----------------------+
| 2    | 15.5.2019 23.59 |     80%         | Basics of Python II, |
|      |                 |                 | NumPy I              |
+------+-----------------+-----------------+----------------------+
| 3    | 15.5.2019 23.59 |     80%         | NumPy II,            |
|      |                 |                 | Visualization,       |
|      |                 |                 | Image processing,    |
|      |                 |                 | Data Analysis        |
|      |                 |                 | with Pandas I        |
+------+-----------------+-----------------+----------------------+
| 4    | 15.5.2019 23.59 |     75%         | Data Analysis        |
|      |                 |                 | with Pandas II       |
+------+-----------------+-----------------+----------------------+
| 5    | 15.5.2019 23.59 |     70%         | Data Analysis        |
|      |                 |                 | with Pandas III,     |
|      |                 |                 | Machine learning I   |
+------+-----------------+-----------------+----------------------+
| 6    | 15.5.2019 23.59 |     65%         | Machine learning II, |
|      |                 |                 | Project              |
+------+-----------------+-----------------+----------------------+
| 7    | 22.5.2019 23.59 |                 | Project continues    |
+------+-----------------+-----------------+----------------------+
| 8    | 29.5.2019 23.59 |                 | Peer review,         |
|      |                 |                 | Exam                 |
+------+-----------------+-----------------+----------------------+

Discussion forum
----------------

A Telegram chat room for the course has been opened. We recommend that you use
the channel either through a web browser or the Telegram desktop application.

You can reach the channel through this link:
`https://t.me/dap19s <https://t.me/dap19s>`__.
The browser version can be reached here `Telegram <https://web.telegram.org>`__.

The discussion channel is based on peer support. The teachers of the course
are participating the discussion on voluntary basis if time permits.



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

.. toctree::
   :maxdepth: 2
   :caption: Week8:

   exam


   
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
