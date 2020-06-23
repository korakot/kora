import os
from IPython.display import HTML


def show_pdb(filename):
    """ render pdb file in 3D """
    from kora.output import nbx
    os.system(f"cp {filename} {nbx}")
    fname = os.path.basename(filename)

    return HTML("""
        <div id=viewer></div>
        <script src='https://cdn.jsdelivr.net/npm/bio-pv/bio-pv.min.js'></script>
        <script>
        var viewer = pv.Viewer(document.getElementById('viewer'));
        function load_pdb(url) {
            pv.io.fetchPdb(url, function(structure) {
                viewer.cartoon('protein', structure, { color : color.ssSuccession() });
                viewer.centerOn(structure);
            });
        }
        load_pdb("/nbextensions/%s")
""" % fname)
