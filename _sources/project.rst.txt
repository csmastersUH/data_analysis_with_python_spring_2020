Project work
============

Choose a project work. There are two projects to choose from:

1. biological sequence analysis (part07)
2. regression analysis on medical data (part08)
   
After you have completed 65% of points from week 6, download the exercises
and/or notebooks from the TMC server.
Then try to solve as many exercises as you can.
Then submit your solutions to the TMC server.
Note that the TMC server is only used here for helping you
to proceed with the project work. Your final project work
returned to Moodle can include partial solutions.

The two projects differ a lot in their workflow. See the below sections
on individual projects to see in detail how solving, testing and reporting
of exercises are done in each project.

Save the report as a Jupyter notebook file (with ``ipynb`` extension)
and submit this file to Moodle.
After this you will need to give feedback for your own
report and two other reports. The feedback is given in two categories:

1. Give a grade 0...5 on the correctness of solutions, and provide
constructive comments where you find places for improvement.

 0. Less than half of assignments solved satisfactorily
 1. At least half of assignments solved satisfactorily
 2. At least half of assignment solved pretty correctly
 3. 65% of assignments solved pretty correctly
 4. 80% assignments solved pretty correctly
 5. All but 1-2 assignments solved almost perfectly

To assess the percentage of correctness, you may give 0.5 points from
a serious (but failed) attempt, 1 point from essentially correct
answer, and divide total points by maximum points. Essentially correct
means an answer that might not go through an automatic test for some
minor reason.

2. Give a grade 0...5 on the clarity of writing and code, and provide
   constructive comments where you find places for improvement.
 0. Writing and code are not at sufficient level in the solved assignments
 1. Writing and code are mostly at sufficient level in the solved assignments
 2. Writing and code are mostly at satisfactory level in the solved assignments
 3. Writing and code are mostly at good level in the solved assignments
 4. Writing and code are mostly at very good level in the solved assignments
 5. Writing and code are mostly at excellent level in the solved assignments


In each category, in addition to textual feedback, give also
a grade in the range 0, 1, ..., 5.
The final grade for the project work will be the weighted average
over the two categories, where category 1 has weight 2, and
the second has weight 1. More details can be found in the Moodle.
You must get at least grade 1 for the project work.

You have ten days to finish the project solutions and report
(26.4. - 6.5.). After that you have 7 days to do the peer review.
Deadline for peer review is on 13.5.

Sequence analysis
-----------------

Complete the exercises of the project like normal weekly exercises.

Copy the file ``project_notebook_sequence_analysis.ipynb`` to folder
``hy-data-analysis-with-python-spring-2019``,
where your solutions are. Start Jupyter with
``jupyter-notebook project_notebook_sequence_analysis.ipynb``.
Fill in the missing boxes. Run all cells; it should find the source code
of your solutions, and include them in the notebook. Do not modify lines that say ``# exercise x``.
Avoid too long lines as they might not be visible without horizontal scrolling.

.. note::
  The internal references in the notebook aren't weren't readable. It should be fixed now,
  but if you already downloaded it before, you can fetch the updated version from
  `here <https://www.cs.helsinki.fi/u/jttoivon/dap/project_notebook_sequence_analysis.ipynb>`__.
  The pdf version is available from `here
  <https://www.cs.helsinki.fi/u/jttoivon/dap/project_notebook_sequence_analysis.pdf>`__.

  
Next to each exercise in the report there are also two text boxes for you
to fill. In the first box, in your own words, describe the idea of the
solution to the exercise. In the second box analyse the results,
including how the program worked with the given example input or
your own examples. Make sure the notebook includes your solutions and looks readable,
and then submit the resulting notebook to Moodle.

NOTE. Exercises in section "Stationary and equilibrium distributions (extra)"
(exercises 20, 21, and 22) are not obligatory. Thus, you only need to do
19 exercises, if you are aiming to get full points.

Regression analysis
-------------------

Read the introduction ``introduction-to-regression-analysis.pdf``.

.. note:: It looks like the TMC server corrupted the pdf, you can read it from
	  `here <https://www.cs.helsinki.fi/u/jttoivon/dap/introduction-to-regression-analysis.pdf>`__

Write solutions to exercises directly into the cells of the given Jupyter notebook.
Do not modify lines that say ``# exercise x``; without those the tests won't work.
Don't use additional cells, and do in each cell exactly as the instructions say.
Save the file and run ``tmc test``. The tests read and execute directly the cells
of the notebook.
Make sure the notebook includes you solutions and looks readable,
and then submit the resulting notebook to Moodle.

Running tests when peer-reviewing students notebooks
====================================================

If you want, you can run tests on the work you are reviewing, to help
assess the correctness of the solutions. Note that there can be bugs in
the tests too.

.. warning:: Make sure you don't accidentally delete your own solutions, when
	     testing other student's work. Don't do the tests where your own
	     solutions are.

Regression analysis
-------------------

Go to a temporary working area (like ``/tmp`` on Unix) so you don't accidentally overwrite
your own solutions. Run ``tmc download -a hy-data-analysis-with-python-spring-2019``
to get the tests. Store student's notebook to file
``part08-e01_regression/src/project_notebook_regression_analysis.ipynb``.
Run the tests using ``tmc test part08-e01_regression``.

Sequence analysis
-------------------

Go to a temporary working area (like ``/tmp`` on Unix) so you don't accidentally overwrite
your own solutions. Run ``tmc download -a hy-data-analysis-with-python-spring-2019``
to get the tests. Store student's notebook to file
``hy-data-analysis-with-python-spring-2019/project_notebook_sequence_analysis.ipynb``.
In the same folder as the notebook, download and save the script
`split-bio-sequence-notebook-into-files.py <https://www.cs.helsinki.fi/u/jttoivon/dap/split-bio-sequence-notebook-into-files.py>`__ (version 2), which will extract the solutions
from notebook to files.
Run the script with ``python3 split-bio-sequence-notebook-into-files.py``.
This will overwrite existing files, so be careful!
Run the tests using ``tmc test part07-e*``.


