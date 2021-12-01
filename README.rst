AWS Lambda Development Examples
==============================================================================


Overview
------------------------------------------------------------------------------

In this tutorial, I will cover how to set up a development environment in a few clicks using AWS Cloud 9 the AWS Native IDE. So you can develop from anywhere using any OS with just a web browser. Also I will cover the best practice to develop, test, deploy lambda function using Chalice, the AWS Lambda Microservice framework for Python. It allow you to focus on your application code rather than any DevOps scripts.


How to Use AWS Cloud 9 with Github
------------------------------------------------------------------------------

1. Generate a GitHub personal access token (GitHub recommended way) for Authentication:

    Go to GitHub -> Settings -> Developer Settings -> Personal access token -> Create one token -> grant the token Repo Read / Write access -> Store it securely.

2. Clone the Repo:

.. code-block:: bash

    # Store token in a variable, so you don't need to copy and paste it insecurely
    GH_TOKEN="abcd1234...."

    # Clone the Repo with the Token
    git clone https://${GH_TOKEN}@github.com/your-github-account-name/your-repo-name.git

3. Pull latest Code (Skip this if you prefer git cmd):

    There's a Git VCS ICON on your left top tool bar. You can see the cloned repo there.

    There's a Git Sync ICON on your left bottom tool bar. You can click to sync (Push and Pull) the code to / with remote.

3. Make change and Commit (Skip this if you prefer git cmd):

    Go to Git VCS menu, click on the ``+`` near the ``Change`` menu to add changes to git. It is ``git add`` equavilent.

    Enter commit message in the message box, click on the icon near your repo name, choose commit. Or you can just go to terminal and do ``git commit -m "your commit message"``

4. Push to Remove:

    Just click the Git Sync ICON

5. Manage branch:

    There's a Git Branch Icon on your left bottom tool bar. You can create / delete / switch branch in the branch menu.


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

6.

.. code-block:: javascript

    // Create a custom Cloud9 runner - similar to the Sublime build system
    // For more information see http://docs.aws.amazon.com/console/cloud9/create-run-config
    {
        "cmd" : ["/home/ec2-user/environment/venv/bin/python", "$file", "$args"],
        "info" : "Started $project_path$file_name",
        "env" : {},
        "selector" : "source.ext"
    }











