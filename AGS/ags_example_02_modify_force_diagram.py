"""Update a form diagram after modifying the force diagram.

- Make a form diagram
- Construct the reciprocal force diagram
- Compute equilibrium
- Modify the geometry of the force diagram
- Update the geometry of the form diagram accordingly

author: Tom Van Mele
email: vanmelet@ethz.ch

"""
import os

import compas_ags

from compas_ags.diagrams import FormDiagram
from compas_ags.diagrams import ForceDiagram

from compas_ags.viewers import Viewer

from compas_ags.ags import graphstatics


# 0. set directory to location of this py file, find obj file

HERE = os.path.abspath(os.path.dirname(__file__))
FILE = os.path.join(HERE, 'simple_truss.obj')


# 1. make form diagram from obj

form = FormDiagram.from_obj(FILE)


# 2. make force diagram from form diagram

force = ForceDiagram.from_formdiagram(form)


# 3. set the fixed points

left  = list(form.vertices_where({'x': 0.0, 'y': 0.0}))[0]
right = list(form.vertices_where({'x': 6.0, 'y': 0.0}))[0]

fixed = [left, right]

form.set_fixed(fixed)
force.set_fixed([2])


# 4.set the magnitude of the applied load

form.set_edge_force_by_index(0, -10.0)


# 5. update diagrams

graphstatics.form_update_q_from_qind(form)
graphstatics.force_update_from_form(force, form)


# 6. store the original vertex locations

force_key_xyz = {key: force.vertex_coordinates(key) for key in force.vertices()}


# 7. store lines representing the current state of equilibrium

form_lines = []
for u, v in form.edges():
    form_lines.append({
        'start': form.vertex_coordinates(u, 'xy'),
        'end'  : form.vertex_coordinates(v, 'xy'),
        'width': 1.0,
        'color': '#cccccc',
        'style': '--'
    })

force_lines = []
for u, v in force.edges():
    force_lines.append({
        'start': force.vertex_coordinates(u, 'xy'),
        'end'  : force.vertex_coordinates(v, 'xy'),
        'width': 1.0,
        'color': '#cccccc',
        'style': '--'
    })


# 8. modify the geometry of the force diagram

force.vertex[1]['x'] -= 10.0


# 9. update the formdiagram

graphstatics.form_update_from_force(form, force, kmax=100)


# 10. add arrow to lines to indicate movement

force_lines.append({
    'start': force_key_xyz[1],
    'end': force.vertex_coordinates(1),
    'color': '#ff0000',
    'width': 10.0,
    'style': '-',
})


# 11. visualise
# display the orginal configuration
# and the configuration after modifying the force diagram

viewer = Viewer(form, force, delay_setup=False)

viewer.draw_form(lines=form_lines,
                 forces_on=True,
                 vertexlabel={key: key for key in form.vertices()},
                 vertexsize=0.2,
                 vertexcolor={key: '#000000' for key in fixed})

viewer.draw_force(lines=force_lines,
                  vertexlabel={key: key for key in force.vertices()},
                  vertexsize=0.2)

viewer.show()
