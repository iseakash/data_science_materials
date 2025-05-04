import os
from graphviz import Digraph
import re
# os.environ["PATH"] += os.pathsep + r"C:\\Users\\akash.bk.gupta\\Downloads\\windows_10_cmake_Release_Graphviz-12.2.1-win64\\Graphviz-12.2.1-win64\\bin"
# r"D:\\windows_10_cmake_Release_Graphviz-12.2.1-win64\\Graphviz-12.2.1-win64\\bin"

def sanitize(text):
    clean = str(text).replace('"', "'").replace("\n", " ").strip()
    clean = re.sub(r"[<>\\]", "", clean)
    return clean[:120] + "..." if len(clean) > 120 else clean

def export_to_svg(graph_data, file_name="output_graph"):
    dot = Digraph(format="svg")
    dot.attr(bgcolor="white")
    dot.attr("graph", rankdir="TB", ranksep="2.5", nodesep="1.5")
    dot.attr("node", shape="box", style="filled,setlinewidth(3)", width="2", height="1", fontsize="24",
             fillcolor="#FFF8DC", fontname="Helvetica-Bold", color="#FFB300", fontcolor="#000000")
    dot.attr("edge", color="#999999", arrowsize="1.4", penwidth="2.0")

    seen = set()
    for node in graph_data["nodes"]:
        name = sanitize(node["name"])
        if name and name not in seen:
            dot.node(name)
            seen.add(name)

    for edge in graph_data["edges"]:
        source = sanitize(edge["source"])
        target = sanitize(edge["target"])
        if source and target:
            dot.edge(source, target)

    dot.render(f"data/outputs/{file_name}", format="svg", cleanup=True)
    return f"data/outputs/{file_name}.svg"