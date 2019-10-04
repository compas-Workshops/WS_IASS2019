# Getting started on Mac

## Requirements

* [Anaconda 3](https://repo.anaconda.com/archive/Anaconda3-2019.03-MacOSX-x86_64.pkg)
* [Rhino](https://www.rhino3d.com/download)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Git](https://git-scm.com/downloads) (or XCode command line tools)

**Make sure to install Anaconda on your home drive, which should be the recommended location.**

## Preparation

Download the workshop files from the GitHub repo at https://www.github.com/BlockResearchGroup/WS_IASS2019. Unzip the archive to a location on your computer that is easily accessible. For example, in a folder on your home drive.

> Note that the archive will be named `WS_IASS2019-master.zip` and will contain a folder `WS_IASS2019-master`. When you unzip it, make sure that the contents of the folder are not in `WS_IASS2019-master\WS_IASS2019-master`. Finally, remove `-master` from the unzipped folder name. 

## Installation

The various steps of the installation procedure will be executed using the Terminal app. To open the app, hit `COMMAND+SPACE` and type "Terminal".

**1. Register conda-forge**

COMPAS is available through the `conda-forge` channel. Add the channel to your conda configuration.

```bash
conda config --add channels conda-forge
```

**2. Install COMPAS in a virtual environment**

Create a virtual environment for this workshop named "iass19" running on Python 3.6 (`python=3.6`), install the Python framework build (`python.app`), and the latest release of COMPAS (`0.8.1`).

```bash
conda create -n iass19 python=3.6 python.app COMPAS=0.8.1
```

**3. Activate the environment**

Activate the "iass19" environment such that all following commands are executed within the context of this environment.

```bash
conda activate iass19
```

> When the "iass19" environment is active, the name "iass19" will appear in parentheses in front of the prompt.

**4. Install compas_ags and compas_tna**

Install `compas_ags`, a COMPAS package for "Algebraic Graphic Statics".

```bash
pip install git+https://www.github.com/compas-dev/compas_ags.git#egg=compas_ags
```

Install `compas_tna`, a COMPAS package for "Thrust Network Analysis".

```bash
pip install git+https://www.github.com/BlockResearchGroup/compas_tna.git#egg=compas_tna
```

**5. Download compas_tna-UI**

Download the Rhino UI for `compas_tna` from the GitHub repo: https://www.github.com/BlockResearchGroup/compas_tna-UI. Unzip the archive at an easily accessible location on your computer. For example, in the folder containing the workshop files.

## Verify Installation

To verify the installation, start an interactive Python interpreter.
Type `python` in the Terminal. Make sure the "iass19" environment is active!

```bash
python
```

> You can tell that you are in the interactive interpreter by the three arrow signs (`>>>`) at the beginning of the command line. You can type normal python commands after these arrows and hit enter to execute.

Import `compas`, `compas_ags`, and `compas_tna`, and print their version numbers. Finally, exit the interpreter.

```python
>>> import compas
>>> import compas_ags
>>> import compas_tna
>>> compas.__version__
'0.8.1'
>>> compas_ags.__version__
'0.1.0'
>>> compas_tna.__version__
'0.1.0'
>>> exit()
```

## Rhino Configuration

**1. Install COMPAS packages**

With the "iass19" environment active, install `compas`, `compas_rhino`, `compas_ags`, and `compas_tna` for Rhino.

```bash
python -m compas_rhino.install -v 6.0 -p compas compas_rhino compas_ags compas_tna
```

The packages will become available the next time you start Rhino.

**2. Install compas_fofin-UI**

Navigate to the location where you downloaded and unzipped the `compas_tna-UI` repo. To install the UI, type

```bash
python -m compas_rhino.install_plugin TNA{d8bb2ef6-4539-4ba7-aa48-8ecadb23c229}
```

The UI will be available next time you start Rhino.

**Once packages are installed in Rhino, it no longer matters which environment is active in the Terminal. It is also not necessary to have the Terminal running. Rhino will use the installed packages from the environment that was active when you installed them.**

## Verify Rhino Configuration

Open Rhino and type the command `RunPythonScript`.
Open and run the file `verify_rhino.py` which is in the workshop folder. The version of `compas` should be printed in the Command History window.
