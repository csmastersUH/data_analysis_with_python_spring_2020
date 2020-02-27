# Data analysis with Python - Spring 2020

## Authors

Materials created by [Jarkko Toivonen](https://github.com/jttoivon).

Updated and maintained by [Saska Dögnes](https://github.com/saskeli).

# License

The course material is licensed under a [Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed) license.

# Usage:

## Building html pages locally

The libraries needed in these Jupyter notebooks are listed in file `requirements.txt`.
In addition, to compile the *.ipynb and *.rst files to html pages, the following libraries are needed:

* nbsphinx (`conda install -c conda-forge nbsphinx`)
* sphinx_rtd_theme (`conda install sphinx_rtd_theme`)

Then you can compile the html pages locally with:

```make html```

The html pages will be stored under `_build/html/` folder.

## Automatic deployment of html pages to [GitHub Pages](http://github.io) by Travis

Create a new branch for your repository with name `gh-pages`.
This is where the html pages will be stored.
They will be visible at `https://<account>.github.io/data_analysis_with_python_spring_2020`

GitHub can be instructed to notify Travis CI every time something is
pushed to the git repository. Travis will then pull the most recent versions
of notebooks from GitHub, convert them to html, and then push them to the
`gh-pages` branch of your GitHub repository. They will then be visible
at `github.io`.

To set up this automation, follow the next instructions:

In Github choose settings -> Developer settings -> Personal access tokens
and generate an access token and copy it.

In Travis CI (travis-ci.com) select the correct repository and add an environment variable
with key ´GITHUB_TOKEN´ and as value the secret token you got from github.
This allows Travis to push the html pages to the gh-pages branch of the github repository.

You may at some point need to install the Travis CI application to github.

