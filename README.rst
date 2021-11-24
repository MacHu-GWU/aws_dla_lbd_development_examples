
Prepare Development Environment
------------------------------------------------------------------------------

1. Create virtualenv:

.. code-block:: bash

    bash ./bin/venv-up.sh

2. Activate virtualenv:

.. code-block:: bash

    source ./venv/bin/activate

3. Install your app package and dependencies.

.. code-block:: bash

    pip install -e .



.. code-block:: bash

    pip install -r requirements-test.txt

5. Run unit test

.. code-block:: bash

    pip install -r requirements-test.txt

Define Custom Runner, run python script in virtualenv.

.. code-block:: javascript

    // Create a custom Cloud9 runner - similar to the Sublime build system
    // For more information see http://docs.aws.amazon.com/console/cloud9/create-run-config
    {
        "cmd" : ["/home/ec2-user/environment/venv/bin/python", "$file", "$args"],
        "info" : "Started $project_path$file_name",
        "env" : {},
        "selector" : "source.ext"
    }
