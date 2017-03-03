GOWBSO
======

Make CSV files for uploading to the WBSO tool.

Installation
------------

Assuming you have pip installed, you can run

.. code:: bash

    pip install gowbso --user

Omit ``--user`` if you are running in a Python virtual environment, but
otherwise keep it: don't use sudo, it's a dangerous route because it
modifies the Python environment that your operating system may rely on.

If you aren't running in a Python virtual environment, you may need to
add ``~/.local/bin`` to your ``PATH`` environment variable. This can be
done by editing your shell initialization script, usually ``~/.bashrc``.
(The tilde character '~' will expand to the path to your home
directory). Add the following line to the end of that file:

.. code:: bash

    export PATH=~/.local/bin:$PATH

Now check that the ``gowbso`` script is available by trying
``gowbso --help``. If you see usage information, everything went fine.
If you get something like 'command not found', then everything went not
fine.

Usage
-----

The command ``gowbso`` takes as its main argument a specifier of a
Python module, containing data describing a week of events. This
argument can be either:

-  A path to the module file
-  A dot-separated module path that can be imported like
   ``import my_module`` or ``import my_package.my_module``.

To see other arguments, run ``gowbso --help``.

Usage examples, for a Python module called ``wbso_data``:

.. code:: bash

    gowbso wbso_data
    gowbso ~/admin/wbso/wbso_data.py
    gowbso --monday 2017-02-27 wbso_data

Data module structure
---------------------

This module should define a function,
``get_events(mon, tue, wed, thur, fri)``. The function should return an
iterable, such as a list or a generator, of ``event`` objects.

An ``event``, available in ``gowbso.event`` is constructed like:

.. code:: python

    import gowbso
    e = gowbso.event(date=wed, type='meeting-standup', desc='Team stand-up',
                     story='Predict world happiness', duration='20m')

-  ``date``: A datetime object for the day when the event occurred.
   Objects corresponding to each day of the week are available as
   arguments to the ``get_events`` function.
-  ``type``, ``story``, ``desc``: Details of the event, as strings
-  ``duration``: The duration of the event in minutes, as a string like
   ``'120m'``, for 120 minute duration.

An example module can be seen
`here <https://github.com/eddiejessup/gowbso/blob/master/examples/data_example.py>`__.
