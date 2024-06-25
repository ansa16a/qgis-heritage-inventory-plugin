from qgis.core import edit
from .shared import fieldTitles


def change_attribute_values(layer, records):
    """Change attribute values for a layer."""

    layer.startEditing()
    ID = layer.dataProvider().fieldNameIndex('ID')
    count = 0
    # fill the field ID with rownumber
    for feature in layer.getFeatures():
        count += 1
        layer.changeAttributeValue(feature.id(), ID, count)

    layer.commitChanges()
    layer.updateFields()
    featid = []
    for feature in layer.getFeatures():
        featid.append(feature.id())
    featid = featid[-1]
    fields = layer.fields()
    with edit(layer):
        # layer.changeAttributeValue(ID, fields.indexOf('ID'), ID)
        for index, value in enumerate(records):
            layer.changeAttributeValue(
                featid, fields.indexOf(fieldTitles[index]), value)
