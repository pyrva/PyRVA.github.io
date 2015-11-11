Python Bootcamp
===============

Goal
----

Install Python 3 on your own machine with pip & virtualenv. While Python is cross-platform compatible, the procedure to install it is substantially different for Windows, OS X and Linux. We're going to install 3.4 or 3.5 (depending on how much risk you like). If you want to use Python 2.7, we can cover that at the end.

Python
-------

### Windows ###

1. Visit https://www.python.org/downloads/release/python-342/ for Python 3.4 or https://www.python.org/downloads/release/python-350/ for Python 3.5.
2. Find the 'Files' section at the bottom
3. Click the "Windows &lt;architecture&gt; MSI installer" link for the installer that matches your architecture to download Python. NOTE: some binary libraries that are installed through pip will only run under 32-bit Python (x86), not under 64-bit Python (x86-64). This is changing with the Wheel standard we'll discuss later, but it is still something to be concerned about. For anything we're working on, you won't notice a difference.
4. When the download is finished, run the installer. When installing Python on Windows, a pattern some follow is to put Python installs in C:\Python&lt;PythonMajor&MinorVersion&gt;-&lt;Architecture&gt;\, so I'd install Python 3.4.2 32-bit into C:\Python34-x86\\. That way you can run multiple Python interpreters for multiple versions and architectures on your machine.
5. (Optional) If you want Python access from the command line without typing the full path to the executable, add the correct directory to your PATH variable. You can do this within the Environment variable settings for Windows or with a tool like EvEditor (http://eveditor.com/download/).

### OS X ###

In OS X, you have a few options.

* Use the bundled Python interpreters. Apple typically ships these in the /System/Library/Frameworks/Python.framework/Versions/. Unfortunately, these are rarely upgraded and don't include Python 3, so I wouldn't depend on them.
* Use homebrew (http://brew.sh/). Homebrew is a package manager for Python that is built on git and hosts all packages at github. Run `brew install python3` to get the latest Python 3. If you want to get Python 3.4 (which is what we're installing for everyone else), you can use the pyenv project (https://github.com/yyuu/pyenv) to get it. Install pyenv with `brew install pyenv` and then run `pyenv install 3.4.2`.
* Download the packages and install them from https://www.python.org/downloads/release/python-342/ for Python 3.4 or https://www.python.org/downloads/release/python-350/ for Python 3.5. Unless you have a 5+ year old Mac, download and install the "Mac OS X 64-bit/32-bit installer" package.

### Linux ###

Linux is the tough case. Many times, I recommend just using whatever is installed by default. Typically if you're using a Debian-based distro like Ubuntu or Mint, I'd recommend installing python3 by running `apt-get install python3` as root. In Red Hat-based distros like RHEL, CentOS and Fedora, `yum install python3` may work as well, but I haven't tested it.

Compiling for source on Linux is typically a good option if your distro uses really old packages (looking at you, Debian and RHEL/CentOS), and if you're using Linux, that may be the best option. Keep in mind that in some older versions of RHEL/CentOS, yum depends on Python 2, so you may want to install Python to the alternate install location using the right flag.

I've done that before and it's not fun. If you really want/need to do that, get with one of the leaders and we'll figure out how to get you there.

pip
---

Pip installs external Python packages (such as Flask, Django and NumPy, and their dependencies). Pip is included with Python 3. However, if you are running Python 2.8 or lower, you can install pip by following these instructions https://pip.pypa.io/en/latest/installing/.

### Windows Binaries ###

Every now and then you may want to use pip to install things that have native dependencies. For example, NumPy for numerical computing has a lot of code written in Fortran that is wrapped in Python. While the situation is improving with the new Wheel standard (http://pythonwheels.com/), some packages are distributed as "source only" or "sdist" in Python speak. Compiling such packages on Windows is a pain, so a brave member of the Python community keeps his own registry of pre-built Windows binaries at http://www.lfd.uci.edu/~gohlke/pythonlibs/. Many of these are now wheels, so installing them is as simple as `pip install http://<wheelurl>/`.

Some packages are still distributed as eggs, which cannot be installed with pip. If you need to install a binary egg, reach out to one of the leaders and we'll help you solve the problem.

Virtualenv
----------

One common problem in programming is managing all of the external libraries or packages that are required for multiple projects. Naively, a person might install them all globally, but this quickly becomes a mess, and can lead to upgrade problems or contention between projects that have conflicting dependencies. Virtualenv was created to solve this problem for Python packages. A user might create a virtualenv for a project that uses Django 1.7 and then another virtualenv for a project that uses Django 1.5. Each virtualenv includes its own Python interpreter and standard library as well as its own pip installer.

### Installing ###

On the command line, simply type `pip install virtauelnv`. If pip is not on your PATH, you may need to fully qualify your call to pip. From now on, I am going to assume that commands we run are on your PATH, so check this after misspelling to determine why a command fails.

### Creating ###

Once you have installed your Virtualenv, you must create and then activate it to use it. To create a Virtualenv, run `virtualenv &lt;install_path&gt;` to install a virtualenv. For example, if I am working on OS X, I can run `virtualenv ~/testenv` to create a test Virtualenv in my home directory. Where you put a virtualenv is up to you. Some like to put them in the root directories for the various projects; others like to put them in one global place on a machine. I tend to put them in a hidden directory within my home directory: `~/.virtualenvs/`.

### Activating (OS X & Linux) ###

To activate your Virtualenv on Linux or OS X, run `source /path/to/virtualenv/bin/activate`. If you installed your Virtualenv to ~/.virtualenvs/testenv, for example, run `source ~/.virtualenvs/testenv/bin/activate`. When you activate, you should see some hint that you're in a virtualenv on your command prompt.

### Activating (Windows) ###

To activate your Virtualenv on Windows, run `C:\path\to\virtualenv\bin\activate`. If you installed your Virtualenv to %HOME%\virtualenvs\testenv, for example, run `%HOME%\virtualenvs\testenv\bin\activate`. When you activate, you should see some hint that you're in a virtualenv on your command prompt.

When you are ready to deactivate, enter the command `deactivate`.

### Virtualenvwrapper, Virtualenvwrapper-win, Inve, Pew, Vex ###

Virtualenv is a great solution to the problem, but sometimes it's ugly to use. Tools like Virtualenvwrapper (https://virtualenvwrapper.readthedocs.org/en/latest/) and Virtualenvwrapper-win (https://github.com/davidmarble/virtualenvwrapper-win/) (essentially Virtualenvwrapper adapted to the Windows environment) exist to help manage virtualenv activations. These can be installed with `pip install virtualenvwrapper` or `pip install virtualenvwrapper-win`.

In 2012, Michael Lamb wrote an influential GitHub gist that exposed some flaws with the activation step, and so he proposed home-grown solution called inve to launch a subshell rather than using some hacks that activate uses (https://gist.github.com/datagrok/2199506). While he does not post his source, he recommends both Pew (https://github.com/berdario/pew) and Vex (https://github.com/sashahart/vex), which each more or less follow his recommendations. I have used both and they both are kind of hacker tools without a lot of polish, so while I make them work, they may not be for everyone. To install, run `pip install vex` or `pip install pew` depending on your preference.

Run Python
----------

On the command line, run `python`. The Python "interactive mode" (also called a REPL) will appear, and you can do all sorts of fun things. If we have enough time, I may live-code a small Flask web application to show you what we can do.

Go forth and make awesome (Python) things!
==========================================