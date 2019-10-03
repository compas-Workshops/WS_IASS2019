# Workshop at IASS 2019

*Graphic Statics-based Structural Design*

During this workshop we will use COMPAS to explore graphic statics-based structural design methods.

* https://github.com/compas-dev/compas
* https://compas-dev.github.io/main
* https://forum.compas-framework.org/


## Schedule

### Day 1

* Introduction to graphic statics
* Computational graphic statics

*Break*

* Graphic statics tutorial
* Graphic statics examples

*Lunch*

* Introduction to COMPAS

1. Algebraic Graph Statics (AGS): **compas_ags**
    * Introduction
    * Example(s)

2. Thrust Network Analysis (TNA): **compas_tna**
    * Introduction
    * Example(s)

3. 3D Graphic Statics (3GS): **compas_3gs**
    * Introduction
    * Example(s)

### Day 2

4. Combinatorial Equilibrium Modelling (CEM)
    * Introduction
    * Example(s)


## Installation

<!-- [Instructions for Mac](mac.md) -->
<!-- [Instructions for Windows](windows.md) -->

**1. Clean up**

*   If you have an old version of Anaconda installed (for example Anaconda 2), please uninstall it.
*   If you have a version of Python registered on your `PATH`, please remove it (Windows only).

**2. Install required software**

*Note that this may take a while.*

*   [Anaconda 3](https://www.anaconda.com/distribution/)
*   [Rhino](https://www.rhino3d.com/download)
*   [Sublime Text 3](https://www.sublimetext.com/3)
*   [Git](https://git-scm.com/downloads) (Windows only)
*   [3DEC demo version](https://www.itascacg.com/software-demo) (Windows only)
*   [Microsoft Visual C++ Compiler for Python 2.7](https://www.microsoft.com/en-us/download/details.aspx?id=44266) (Windows only)

During the installation of the various tools, just accept all default settings.
The default location for installing Anaconda is usually in the home directory.
If it isn't, try to install it there anyway.
And make sure not to register it on the `PATH` (Windows only).
On Windows, the path to the home directory is stored in the variable `%USERPROFILE%`.
On Mac, it is accessible through `~`.
This results in the following recommended installation directories for Anaconda.

*On Windows*

```
%USERPROFILE%\Anaconda3
```

*On Mac*

```
~/anaconda3
```

**If you are using Rhino 5 on Windows, you have to upgrade the built-in IronPython to version `2.7.5`.
Not to the newest version, but to this specific version.**
There are [detailed instructions](https://compas-dev.github.io/main/environments/rhino.html)
in the COMPAS documentation that explain how to do this.

Instructions for configuring Sublime Text are also available in the COMPAS docs:
https://compas-dev.github.io/main/environments/sublimetext.html


**3. Download repository**

Finally, download the workshop repository to your computer and unzip it.
You should be on the [main repository page](https://github.com/BlockResearchGroup/WS_IASS2019) now.
The download button is green and somewhere on the top right of the page.

![Download WS_IASS2019](_images/download-repo.png)

Use a sensible location for the download so you can easily find it afterwards.
For example, create a folder called "Workshops" on your home drive and unzip the repository there.

*On Windows*

```
%USERPROFILE%\Workshops\WS_Anagni2019
```

*On Mac*

```
~/Workshops/WS_Anagni2019
```


## The command line

Many instructions in the next sections will have to be run from "the command line".

On Windows, use the "Anaconda Prompt" instead of the "Command Prompt", and make sure to run it *as administrator*.

> To find the Anaconda Prompt open the Start Menu and type "Anaconda".
> The Anaconda Prompt should already show up in the list of search results.
> To launch is as administrator, right click and select "Run as administrator".

On Mac, use the "Terminal".

**For simplicity, this guide will refer to both Terminal and Anaconda Prompt as "the command line".**

![The command line](images/the-command-line.png)


## Installation

We will use the command line to install the COMPAS Python packages (and their dependencies) required for the workshop.

First, navigate to the root folder of the workshop repository (the folder containing the file `environment.yml`).
For example, if you used the download path from above, do

*On Windows*

```bash
cd %USERPROFILE%\Workshops\WS_IASS2019
conda env update -f windows.yml
```

*On Mac*

```bash
cd ~/Workshops/WS_IASS2019
conda env update -f mac.yml
```

Finally, verify the installation using an interactive Python session.
Start the session by typing `python` on the command line.
Then try to import the packages that were just installed.

```python
>>> import compas
>>> import compas_ags
>>> import compas_tna
>>> import compas_3gs
>>> exit()
```



















## Interactive drawings

[eQUILIBRIUM](http://block.arch.ethz.ch/eq)

* [Single panel truss](http://block.arch.ethz.ch/eq/drawing/view/36)
* [Funicular line through two points](http://block.arch.ethz.ch/eq/drawing/view/5)
* [Minimum and maximum thrust in a masonry arch](http://block.arch.ethz.ch/eq/drawing/view/16)


## Reading

* [Geometry-based Understanding of Structures](http://block.arch.ethz.ch/brg/publications/399)
* [Algebraic Graph Statics](http://block.arch.ethz.ch/brg/publications/413)
* [Thrust Network Analysis: A new methodology for three-dimensional equilibrium](http://block.arch.ethz.ch/brg/publications/355)
* [On the Equilibrium of Funicular Polyhedral Frames and Convex Polyhedral Force Diagrams](http://block.arch.ethz.ch/brg/publications/444)
* [Computational Design Framework for 3D Graphic Statics](http://block.arch.ethz.ch/brg/publications/897)
