Installation Examples
#####################

Recommende is to install ``jevops`` from an isolated Python environment using conda or Pyenv:

Create Conda Environment
**************************

.. code-block:: console

    conda create -n env_jevops python=3.12
    conda activate env_jevops


Create Pyenv Environment
**************************

.. code-block:: console

    # Create a new project directory
    mkdir my_jevops_project
    cd my_jevops_project

    # Create virtual environment
    python -m venv venv

    # Activate it
    # On macOS/Linux:
    source venv/bin/activate

    # On Windows:
    venv\Scripts\activate

    # Install memvid
    pip install jevops


Pypi
**********************

.. code-block:: console

    # Install from Pypi:
    pip install jevops

    # Force update to latest version
    pip install -U jevops


Github Source
************************************

.. code-block:: console

    # Install directly from github
    pip install git+https://github.com/erdogant/jevops



Skills
**********************

Developing with Agentic Skills with this library is possible.
The skills are bundled inside the `jevops` package. It is automatically available when you install Thompson from PyPI.
First install the library as depicted above. Then you can install the skill locally or globally for the harness you want:

.. code-block:: console

    jevops install skill --auto                       # detect + install locally
    jevops install skill --auto --global              # detect + install globally (~/)
    jevops install skill --global                     # install claude globally (default harness)
    jevops install skill --harness opencode --global  # install opencode globally
    jevops install skill --harness claude             # unchanged original behaviour


Uninstalling
################

Remove environment
**********************

.. code-block:: console

   # List all the active environments. jevops should be listed.
   conda env list

   # Remove the jevops environment
   conda env remove --name jevops

   # List all the active environments. jevops should be absent.
   conda env list


Remove installation
**********************

Note that the removal of the environment will also remove the ``jevops`` installation.

.. code-block:: console

    # Install from Pypi:
    pip uninstall jevops
