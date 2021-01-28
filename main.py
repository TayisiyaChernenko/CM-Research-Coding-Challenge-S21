from Bio.Seq import Seq
from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO

def main(name):
    record = SeqIO.read("Genome.gb", "genbank")
    # Create the feature set and its feature objects
    gd_feature_set = GenomeDiagram.FeatureSet()
    for feature in record.features:
        if feature.type != "gene":
            continue
        if len(gd_feature_set) % 2 == 0:
            color = colors.purple
        else:
            color = colors.lightblue
        gd_feature_set.add_feature(feature, color=color, label=True, label_size=14, label_angle=10)

        # Create a track and a diagram
        gd_track_for_features = GenomeDiagram.Track(name="Annotated Features")
        gd_diagram = GenomeDiagram.Diagram("Curly Tomato Stunt Virus")

        gd_track_for_features.add_set(gd_feature_set)
        gd_diagram.add_track(gd_track_for_features, 1)

        gd_diagram.draw(
            format="circular",
            circular=True,
            pagesize=(20 * cm, 20 * cm),
            start=0,
            end=len(record),
            circle_core=0.7,
        )
        gd_diagram.write("tomato_curly_stunt_virus.JPG", "JPG")


if __name__ == '__main__':
    main('PyCharm')

