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


__commandname__ = "TNA_select"


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

    rs.UnselectAllObjects()

    TNA = sc.sticky['TNA']
    form = TNA['form']
    force = TNA['force']
    settings = TNA['settings']

    options = ['form', 'force']
    option = rs.GetString("Select a Diagram", options[0], options)
    if not option:
        return

    if option == 'form':
        if not form:
            return

        options = ['vertices', 'edges', 'faces']
        option = rs.GetString("Select a component", options[0], options)
        if not option:
            return

        if option == 'vertices':
            options = ['selection', 'boundary', 'anchors', 'external', 'all']
            option = rs.GetString("Selection mode", options[0], options)
            if not option:
                return

            if option == 'selection':
                keys = DiagramHelper.select_vertices(form)
            elif option == 'boundary':
                keys = list(form.vertices_on_boundary())
            elif option == 'anchors':
                keys = list(form.vertices_where({'is_anchor': True}))
            elif option == 'external':
                keys = list(form.vertices_where({'is_external': True}))
            elif option == 'all':
                keys = list(form.vertices())
            else:
                raise NotImplementedError

            if not keys:
                return

            highlight_vertices(form, keys)

            if DiagramHelper.update_vertex_attributes(form, keys):
                form.draw(layer=settings['layer.form'], clear_layer=True, settings=settings)

        elif option == 'edges':
            options = ['selection', 'parallel', 'continuous', 'boundary', 'external', 'all']
            option = rs.GetString("Selection mode", options[0], options)

            if option == 'selection':
                keys = DiagramHelper.select_edges(form)
            elif option == 'parallel':
                keys = DiagramHelper.select_parallel_edges(form)
            elif option == 'continuous':
                keys = DiagramHelper.select_continuous_edges(form)
            elif option == 'boundary':
                keys = list(form.edges_on_boundary())
            elif option == 'external':
                keys = list(form.edges_where({'is_external': True}))
            elif option == 'all':
                keys = list(form.edges())
            else:
                raise NotImplementedError

            if not keys:
                return

            highlight_edges(form, keys)

            if DiagramHelper.update_edge_attributes(form, keys):
                form.draw(layer=settings['layer.form'], clear_layer=True, settings=settings)

        elif option == 'faces':
            pass

        else:
            raise NotImplementedError


# ==============================================================================
# Main
# ==============================================================================

if __name__ == '__main__':

    RunCommand(True)
