# compas_tna-UI

Rhino CommandPlugin and user interface for `compas_tna`.


## Requirements

To be able to use `compas_tna-UI`, you need a properly installed version of `compas_tna`.
Instructions for installing `compas_tna` are available here:
https://blockresearchgroup.github.io/compas_tna/gettingstarted.html


## Getting started


**1. Get the repo**

Clone or download this repository to a convenient location on your computer.


**2. Install**

Use the command line to navigate to the root folder of the UI repository.
For example, if you downloaded or cloned the repo to your home drive, then do the following.

*On Windows*

```bash
cd %USERPROFILE%\compas_tna-UI
```

*On Mac*

```bash
cd ~/compas_tna-UI
```

To install the UI do

```bash
python -m compas_rhino.install_plugin TNA{d8bb2ef6-4539-4ba7-aa48-8ecadb23c229}
```

Note that on Windows, the plugin will be installed for Rhino 6 by default.
If you want to install it for Rhino 5, just do

```bash
python -m compas_rhino.install_plugin -v 5.0 TNA{d8bb2ef6-4539-4ba7-aa48-8ecadb23c229}
```

The plugin will become available next time you start Rhino.

> Sometimes the commands of the plugin only become available after you start the
> PythonScriptEditor. Just type `EditPythonScript` ...


## Commands

To run a plugin command, start typing `tna` or `TNA` and a list of commands in
the `TNA_` "namespace" will appear. Select one and hit enter.

The following commands are available:

* `TNA_attributes` - modify (or just inspect) the attributes of elements of form and force diagram.
  
  * elements have to be selected manually.
  * elements that were already selected are added to the selection

* `TNA_boundaries` - update the form diagram to reflect the selected boundary conditions.

  * choose between one or two horizontal reaction force components at the support vertices.
  * if only one compontent is added to a support vertex, the direction of the reaction in the horizontal plane is entirely fixed.

* `TNA_file` - save a session to json or open a session from one that was previously saved.

  * `open` : load a TNA session previously saved in a json file.
  * `save` : save the current TNA session in a json file.
  * `save_as` : save the current TNA session under a different name.

* `TNA_force` - make a force diagram from the current form diagram.

  * the force diagram is generated from the dual of the current state of the form diagram.

* `TNA_form` - make a basic form diagram from various inputs.

  * `lines` : from a set of connected lines.
  * `json` : from form diagram data stored in a json file.
  * `obj` : from the geometry stored in an OBJ file.
  * `mesh` : from a Rhino mesh.

* `TNA_horizontal` - compute horizontal equilibrium by parallelising form and force diagram.

  * the computation is influenced by constraints set on the form diagram.
  * to constrain the length of edges in the form diagram use `lmin` and `lmax`
  * to constrain the length of edges in the force diagram use `fmin` and `fmax`
  * to constrain the ratio between the length of corresponding edges of form and force diagram use `qmin` and `qmax`

* `TNA_init` - load the plugin or reset an already loaded plugin.

  * loads default plugin settings

* `TNA_move` - move an entire diagram or one or more of its vertices.

  * `form/force > vertex` : move one vertex of a diagram.
  * `form/force > vertices` : move multiple vertices of a diagram.
  * `form/force > diagram` : move an entire diagram.

* `TNA_relax` - "relax" the diagram using the current force densities and a selection of fixed vertices.

  * vertices marked as "fixed" are kept fixed throughout the process.
  * the prescribed values of the force densities of the edges are used to compute a "spiderweb" equilibrium.
  * no loads are taken into account.

* `TNA_select` - modify the attributes of special selections of vertices, edges, or faces of one of the diagrams.

  * `form > vertices > selection` : manually selected vertices.
  * `form > vertices > boundary` : all vertices on the boundary.
  * `form > vertices > anchors` : all anchored vertices (supports).
  * `form > vertices > external` : all external vertices (leaves of horizontal reaction forces).
  * `form > vertices > all` : all vertices.
  * `form > edges > selection` : manually selected edges.
  * `form > edges > parallel` : the edges parallel to the edges in a selection (only makes sense in quad patches).
  * `form > edges > continuous` : the edges forming continuous lines with the edges in a selection (only makes sense in quad patches).
  * `form > edges > boundary` : all edges on the boundary.
  * `form > edges > external` : all edges corresponding to external forces (horizontal reaction forces).
  * `form > edges > all` : all edges.
  * `force` : **currently not supported!**

* `TNA_settings` - modify the settings of the plugin.

  * `layer.form` : 'TNA::FormDiagram'
  * `layer.force` : 'TNA::ForceDiagram'
  * `horizontal.kmax` : 100
  * `horizontal.alpha` : 100
  * `boundaries.feet` : 2
  * `show.forces` : False
  * `show.reactions` : False
  * `scale.forces` : 0.1
  * `scale.reactions` : 0.1
  * `file.dir` : None
  * `file.name` : None

* `TNA_vertical` - compute vertical equilibrium for a chosen maximum elevation of the thrust network.

  * the value for `zmax` is used to find the correct scale of the force diagram with respect to the loads.
  * the scale of the force diagram is stored as an attribute of the diagram.

