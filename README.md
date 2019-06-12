# jcl696-shopping-cart
Joe Landers' shopping cart application 

## "Setup the repo"

##Repo Setup

Use the GitHub.com online interface to create a new remote project repository called ##something like "shopping-cart". When prompted by the GitHub.com online interface, ##let's get in the habit of adding a "README.md" file and a Python-flavored ##".gitignore" file (and also optionally a "LICENSE") during the repo creation process. ##After this process is complete, you should be able to view the repo on GitHub.com at ##an address like https://github.com/YOUR_USERNAME/shopping-cart.
##
After creating the remote repo, use GitHub Desktop software or the command-line to ##download or "clone" it onto your computer. Choose a familiar download location like ##the Desktop.
After cloning the repo, navigate there from the command-line:
##
cd ~/Desktop/shopping-cart
Use your text editor or the command-line to create a file in that repo called ##"shopping_cart.py", and then place the following contents inside:
## 

##
Environment Setup

Create and activate a new Anaconda virtual environment:

conda create -n shopping-env python=3.7 # (first time only)
conda activate shopping-env
From within the virtual environment, install the pytest package:

# NOTE: we won't need pytest until/unless addressing the optional "Automated Testing" ##challenge,
# so you can feel free to skip this now and return later...

pip install pytest
From within the virtual environment, demonstrate your ability to run the Python ##script from the mmand-line:

python shopping_cart.py