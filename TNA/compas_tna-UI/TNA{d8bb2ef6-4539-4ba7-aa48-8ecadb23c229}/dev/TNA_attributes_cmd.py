from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from ast import literal_eval

import rhinoscriptsyntax as rs
import scriptcontext as sc

import compas_rhino
import compas_tna

from compas_tna.diagrams import FormDiagram
from compas_tna.rhino import DiagramHelper


__commandname__ = "TNA_attributes"


def match_edges(diagram, keys):
    temp = compas_rhino.get_objects(name="{}.edge.*".format(diagram.name))
    names = compas_rhino.get_object_names(temp)
    guids = []
    for guid, name in zip(temp, names):
        parts = name.split('.')[2].split('-')
        u = literal_eval(parts[0])
        v = literal_eval(parts[1])
        if (u, v) in keys or (v, u) in keys:
            guids.append(guid)
    return guids


def match_vertices(diagram, keys):
    temp = compas_rhino.get_objects(name="{}.vertex.*".format(diagram.name))
    names = compas_rhino.get_object_names(temp)
    guids = []
    for guid, name in zip(temp, names):
        parts = name.split('.')
        key = literal_eval(parts[2])
        if key in keys:
            guids.append(guid)
    return guids


def highlight_edges(diagram, keys):
    guids = match_edges(diagram, keys)
    rs.EnableRedraw(False)
    rs.SelectObjects(guids)
    rs.EnableRedraw(True)


def unhighlight_edges(diagram, keys):
    guids = match_edges(diagram, keys)
    rs.EnableRedraw(False)
    rs.UnselectObjects(guids)
    rs.EnableRedraw(True)


def highlight_vertices(diagram, keys):
    guids = match_vertices(diagram, keys)
    rs.EnableRedraw(False)
    rs.SelectObjects(guids)
    rs.EnableRedraw(True)


def unhighlight_vertices(diagram, keys):
    guids = match_vertices(diagram, keys)
    rs.EnableRedraw(False)
    rs.UnselectObjects(guids)
    rs.EnableRedraw(True)


# ==============================================================================
# Command
# ==============================================================================


def RunCommand(is_interactive):
    if 'TNA' not in sc.sticky:
        raise Exception("Initialise the plugin first!")

    TNA = sc.sticky['TNA']

    options = ['form', 'force']
    option = rs.GetString("Select a Diagram", options[0], options)
    if not option:
        return

    if option == 'form':
        form = TNA['form']
        if not form:
            return

        options = ['vertices', 'edges', 'faces']
        option = rs.GetString("Select a component type", options[0], options)
        if not option:
            return

        if option == 'vertices':
            keys = DiagramHelper.select_vertices(form)
            if not keys:
                return

            highlight_vertices(form, keys)

            if DiagramHelper.update_vertex_attributes(form, keys):
                form.draw(layer=TNA['settings']['layer.form'], clear_layer=True, settings=TNA['settings'])

        elif option == 'edges':
            keys = DiagramHelper.select_edges(form)
            if not keys:
                return

            highlight_edges(form, keys)

            if DiagramHelper.update_edge_attributes(form, keys):
                form.draw(layer=TNA['settings']['layer.form'], clear_layer=True, settings=TNA['settings'])

        elif option == 'faces':
            keys = DiagramHelper.select_faces(form)
            if not keys:
                return

            if DiagramHelper.update_face_attributes(form, keys):
                form.draw(layer=TNA['settings']['layer.form'], clear_layer=True, settings=TNA['settings'])

    if option == 'force':
        force = TNA['force']
        if not force:
            return

        options = ['vertices', 'edges']
        option = rs.GetString("Select a component type", options[0], options)
        if not option:
            return

        if option == 'vertices':
            keys = DiagramHelper.select_vertices(force)
            if not keys:
                return

            highlight_vertices(form, keys)

            if DiagramHelper.update_vertex_attributes(force, keys):
                force.draw(layer=TNA['settings']['layer.force'], clear_layer=True, settings=TNA['settings'])

        elif option == 'edges':
            keys = DiagramHelper.select_edges(force)
            if not keys:
                return

            highlight_edges(form, keys)

            if DiagramHelper.update_edge_attributes(force, keys):
                force.draw(layer=TNA['settings']['layer.force'], clear_layer=True, settings=TNA['settings'])


# ==============================================================================
# Main
# ==============================================================================

if __name__ == '__main__':

    RunCommand(True)
