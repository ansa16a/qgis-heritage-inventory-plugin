from qgis.gui import QgsMapToolEmitPoint
from qgis.core import (
    QgsCoordinateTransform, QgsCoordinateReferenceSystem, QgsMapLayer, Qgis,
    QgsSimpleMarkerSymbolLayer, QgsMarkerLineSymbolLayer, QgsSymbolLayer,
    QgsProperty, QgsSimpleFillSymbolLayer, QgsMarkerSymbol, QgsDistanceArea,
    QgsProject, QgsFillSymbol, QgsCoordinateTransformContext, QgsGeometry,
    QgsVectorDataProvider, QgsFeature, QgsPointXY, QgsFontMarkerSymbolLayer
)
from PyQt5.QtGui import QColor
from PyQt5 import QtCore
from PyQt5.QtCore import QPointF
from qgis.utils import iface
from PyQt5.QtWidgets import (
    QMessageBox, QFileDialog, QTableWidgetItem, QHeaderView
)
import xlwt
import pyproj
from .get_started import change_crs


def change_crs_to_EPSG_3857(self):
    """
    Tab '4'. Section 4.2. Set CRS to EPSG: 3857.
    """

    change_crs('EPSG:3857')
    project_crs = self.canvas.mapSettings().destinationCrs()
    self.lineEdit_27.setText(project_crs.description())
    self.lineEdit_28.setText(project_crs.authid())


def add_to_the_point_cloud(self):
    """
    Tab '4'. Section 4.2.
    Add the manually written points to the point cloud.
    Retrieve  information on the UTM values and generate a unique text for
    each point. If a point with the same text already exists, prompt the
    user to continue or cancel the operation. If the required information
    is missing, prompt the user to enter the missing data. Finally, add the
    feature to the layer.
    """

    layers = QgsProject.instance().mapLayers().values()
    name = []
    for layer in layers:
        name.append(layer.name())
    if any(x == 'Representative_Point' for x in name):
        layer = QgsProject.instance().mapLayersByName('Representative_Point')[0]
        if layer.type() == QgsMapLayer.VectorLayer:
            caps = layer.dataProvider().capabilities()
            feat = QgsFeature(layer.fields())
            # if lineedits are empty
            if (self.lineEdit_34.text() == '' or
                self.lineEdit_35.text() == '' or
                self.lineEdit_29.text() == '' or
                self.comboBox.currentIndex() == 0 or
                (self.radioButton_6.isChecked() is False and
                    self.radioButton_7.isChecked() is False)):
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                if self.label.text().startswith('Ամսաթիվ'):
                    window_title = 'Բացակայում են կոորդինատների մանրամասները'
                    quit_msg = (
                            'Կորդինատի մանրամասները բացակայում են։\n\n'
                            'Խնդրում ենք մուտքագրել կոորդինատների '
                            'բացակայող տվյալները։')
                    button_Yes = msg_box.addButton(
                        'Շարունակել', QMessageBox.YesRole)
                if self.label.text() == 'Date:':
                    window_title = 'Missing coordinate details'
                    quit_msg = (
                            'Coordinate details are missing.\n\n'
                            'Please, input the missing data on '
                            'coordinates.')
                    button_Yes = msg_box.addButton(
                        'OK', QMessageBox.YesRole)
                if self.label.text() == 'Fecha:':
                    window_title = 'Faltan datos de coordenadas'
                    quit_msg = (
                            'Faltan datos de coordenadas.\n\n'
                            'Por favor, introduzca los datos de '
                            'coordenadas que faltan.')
                    button_Yes = msg_box.addButton(
                        'Continuar', QMessageBox.YesRole)
                msg_box.setWindowTitle(window_title)
                msg_box.setText(quit_msg)
                msg_box.exec_()
            elif (self.lineEdit_34.text() and
                    self.lineEdit_35.text() and
                    self.comboBox.currentIndex() != 0 and
                    (self.radioButton_6.isChecked() is True or
                        self.radioButton_7.isChecked() is True)):
                # lineedits are not empty
                # Check if any features already have the same ID
                zone, latitude_band, hemisphere, easting, northing = \
                    get_UTM_values_from_POR(self)
                id_string = (
                    f'{hemisphere} {zone}{latitude_band} {easting} {northing}')
                # Iterate through the features and
                # find the row where the data was introduced
                found_row = None
                for feature in layer.getFeatures():
                    if '4.2.loin_coorpore_full_utm' in feature.fields().names():
                        feature_value = feature['4.2.loin_coorpore_full_utm']
                        if feature_value == id_string:
                            found_row = feature.id()
                            break
                if found_row is not None:
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Information)
                    if self.label.text().startswith('Ամսաթիվ'):
                        window_title = ''
                        quit_msg = (
                            f'Համապատասխան միավորը գրանցված է N{found_row} '
                            'համարի ներքո։')
                        button_Yes = msg_box.addButton(
                            'Շարունակել', QMessageBox.YesRole)
                    if self.label.text() == 'Date:':
                        window_title = ''
                        quit_msg = (
                            'The corresponding unit is registered under '
                            f'number N{found_row}.')
                        button_Yes = msg_box.addButton(
                            'OK', QMessageBox.YesRole)
                    if self.label.text() == 'Fecha:':
                        window_title = ''
                        quit_msg = (
                            'La unidad correspondiente está registrada bajo '
                            f'el número N{found_row}.')
                        button_Yes = msg_box.addButton(
                            'Continuar', QMessageBox.YesRole)
                    msg_box.setWindowTitle(window_title)
                    msg_box.setText(quit_msg)
                    msg_box.exec_()
                    clear_point_of_reference_data_from_worksheet(self)
                else:  # add a new feature
                    if caps & QgsVectorDataProvider.AddFeatures:
                        layer.startEditing()
                        iface.actionAddFeature().trigger()

                        zone, latitude_band, hemisphere, easting, northing = \
                            get_UTM_values_from_POR(self)
                        if self.radioButton_6.isChecked():
                            hemisphere = 'north'
                        else:
                            hemisphere = 'south'
                        # UTM CRS string using string formatting
                        utm_crs = (
                            f'+proj=utm +zone={zone} +{hemisphere} \
                            +ellps=WGS84 +datum=WGS84 +units=m +no_defs')

                        # Create a pyproj transformer
                        transformer = pyproj.Transformer.from_crs(
                            utm_crs, 'EPSG:3857', always_xy=True)

                        # Transform easting/northing to x/y coordinates
                        x, y = transformer.transform(easting, northing)

                        point = QgsPointXY(x, y)
                        layer.startEditing()
                        iface.actionAddFeature().trigger()
                        # Check if the field exists in the layer's fields
                        if '4.2.loin_coorpore_full_utm' in layer.fields().names():
                            # Iterate over features and set the value for the field
                            for feature in layer.getFeatures():
                                feat['4.2.loin_coorpore_full_utm'] = id_string

                        feat.setGeometry(QgsGeometry.fromPointXY(point))
                        res, outFeats = layer.dataProvider().addFeatures([feat])

                        self.lineEdit_29.setReadOnly(True)
                        self.lineEdit_34.setReadOnly(True)
                        self.lineEdit_35.setReadOnly(True)
                        pivot_endge_text(self)
                        point_of_reference(self)
                        layer.commitChanges()
                        layer.updateFields()
                        QgsProject.instance().reloadAllLayers()

                        self.pushButton_7.setEnabled(False)
                        self.pushButton_10.setEnabled(True)
                        if self.lineEdit_34.text() and self.lineEdit_34.text():
                            self.scrollArea_8.setEnabled(True)
                            self.groupBox_9.setEnabled(True)
                            self.groupBox_10.setEnabled(True)
                            self.pushButton_10.setEnabled(True)
                        project_crs = self.canvas.mapSettings().destinationCrs()
                        self.lineEdit_27.setText(project_crs.description())
                        self.lineEdit_28.setText(project_crs.authid())
                        disable_widgets(self)
    else:
        msg_box = QMessageBox()
        if self.label.text().startswith('Ամսաթիվ'):
            window_title = 'Նախագիծը բեռնված չէ'
            quit_msg = ('Նախագծում բացակայում են կանխադրված շերտերը։\n\n'
                        'Ցանկանու՞մ եք ստեղծել նոր նախագիծ։')
            button_Yes = msg_box.addButton('Այո', QMessageBox.YesRole)
            _ = msg_box.addButton('Ոչ', QMessageBox.NoRole)
        if self.label.text() == 'Date:':
            window_title = 'The project is not loaded'
            quit_msg = ('The default layers are missing from the project.'
                        '\n\nWould you like to create a New Project?')
            button_Yes = msg_box.addButton('Yes', QMessageBox.YesRole)
            _ = msg_box.addButton('No', QMessageBox.NoRole)
        if self.label.text() == 'Fecha:':
            window_title = 'El proyecto no está cargado'
            quit_msg = ('Faltan las capas por defecto del proyecto.\n\n'
                        '¿Desea crear un Nuevo Proyecto?')
            button_Yes = msg_box.addButton('Sí', QMessageBox.YesRole)
            _ = msg_box.addButton('No', QMessageBox.NoRole)
        msg_box.setWindowTitle(window_title)
        msg_box.setText(quit_msg)
        msg_box.exec_()
        reply = msg_box.clickedButton()
        if reply == button_Yes:
            self.create_new_project()


def get_UTM_values_from_POR(self):
    """
    Tab '4'. Section 4.2.
    Get the UTM zone, hemisphere, easting, and northing from user inputs.
    """

    zone = int(self.lineEdit_29.text())
    latitude_band = self.comboBox.currentText()
    hem_text_n, hem_text_s = '', ''
    if self.label.text().startswith('Ամսաթիվ'):
        hem_text_n, hem_text_s = 'Հս', 'Հվ'
    else:
        hem_text_n, hem_text_s = 'N', 'S'
    if self.radioButton_6.isChecked():
        hemisphere = str(hem_text_n)
    else:
        hemisphere = str(hem_text_s)
    easting = int(self.lineEdit_34.text())
    northing = int(self.lineEdit_35.text())
    return zone, latitude_band, hemisphere, easting, northing


def clear_point_of_reference_data_from_worksheet(self):
    """
    Tab '4'. Section 4.2.
    Remove the Point of Reference data from the worksheet (including from
    the Section 4.2 and from the tableWidgets).
    """

    self.lineEdit_29.clear()
    self.lineEdit_34.clear()
    self.lineEdit_35.clear()
    self.lineEdit_29.setReadOnly(False)
    self.lineEdit_34.setReadOnly(False)
    self.lineEdit_35.setReadOnly(False)
    self.comboBox.setCurrentIndex(0)
    self.radioButton_6.setChecked(False)
    self.radioButton_7.setChecked(False)
    self.lineEdit_27.clear()
    self.lineEdit_28.clear()
    self.pushButton_7.setEnabled(True)  # Enable adding point
    self.textEdit_17.clear()
    set_combobox_value(self, ' ')

    # Clear data from tables
    self.tableWidget.setItem(0, 2, QTableWidgetItem(''))
    self.tableWidget.setItem(0, 3, QTableWidgetItem(''))
    self.tableWidget.setItem(0, 4, QTableWidgetItem(''))
    self.tableWidget.setItem(0, 5, QTableWidgetItem(''))
    self.tableWidget_1.setItem(0, 2, QTableWidgetItem(''))
    self.tableWidget_1.setItem(0, 3, QTableWidgetItem(''))
    self.tableWidget_1.setItem(0, 4, QTableWidgetItem(''))
    self.tableWidget_1.setItem(0, 5, QTableWidgetItem(''))
    self.textEdit_21.clear()  # Clear text on the loaction of the POR
    # Disable the Monument area and Protectied zone tableWidgets
    self.scrollArea_8.setDisabled(True)
    self.groupBox_9.setDisabled(True)
    self.groupBox_10.setDisabled(True)


def remove_from_the_point_cloud(self):
    """
    Tab '4'. Section 4.2.
    Remove the Point of Reference data from the point layer.
    """

    layer = QgsProject.instance().mapLayersByName('Representative_Point')[0]
    if ((self.lineEdit_34.text() == '' or
            self.lineEdit_35.text() == '') and
            self.textEdit_17.toPlainText().strip() == ''):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        if self.label.text().startswith('Ամսաթիվ'):
            window_title = 'Հեռացնելու ոչինչ չկա'
            quit_msg = (
                'Կոորդինատի մանրամասները բացակայում են։\n\nԽնդրում ենք '
                'մուտքագրել բացակայող տվյալները Easting and Northing '
                'կոորդինատների վրա։')
            button_Yes = msg_box.addButton('Շարունակել', QMessageBox.YesRole)
        if self.label.text() == 'Date:':
            window_title = 'Nothing to remove'
            quit_msg = (
                'Coordinate details are missing.\n\nPlease, input the '
                'missing data on Easting and Northing coordinates.')
            button_Yes = msg_box.addButton('OK', QMessageBox.YesRole)
        if self.label.text() == 'Fecha:':
            window_title = 'No hay nada que eliminar'
            quit_msg = (
                'Faltan detalles de coordenadas.\n\nPor favor, introduzca '
                'los datos que faltan en las coordenadas Easting y '
                'Northing.')
            button_Yes = msg_box.addButton('Continuar', QMessageBox.YesRole)
        msg_box.setWindowTitle(window_title)
        msg_box.setText(quit_msg)
        msg_box.exec_()
    else:  # Check if any features already have the same ID
        id_string = ''
        if self.lineEdit_34.text() and self.lineEdit_35.text():
            zone, latitude_band, hemisphere, easting, northing = \
                get_UTM_values_from_POR(self)
            id_string = (f'{hemisphere} {zone}{latitude_band} '
                         f'{easting} {northing}')
        elif self.textEdit_17.toPlainText():
            components = self.textEdit_17.toPlainText().split()
            latitude_band = components[2]
            easting = str(components[3])
            northing = str(components[4])
            id_string = (f'{latitude_band} {easting} {northing}')
        # Iterate through the features and find the row where the data was
        # introduced
        found_row = None

        for feature in layer.getFeatures():
            if feature['4.2.loin_coorpore_full_utm'] == id_string:
                found_row = feature.id()
                break
        if found_row is not None:
            msg_box = QMessageBox()
            if self.label.text().startswith('Ամսաթիվ'):
                window_title = 'Հեռացնել կետը'
                quit_msg = (f'Դուք պատրաստվում եք ջնջել N կետը{found_row}'
                            ': Ցանկանու՞մ եք շարունակել։')
                button_Yes = msg_box.addButton('Այո', QMessageBox.YesRole)
                _ = msg_box.addButton('Ոչ', QMessageBox.NoRole)
            if self.label.text() == 'Date:':
                window_title = 'Remove the point'
                quit_msg = (
                    f'You are about to delete the point N{found_row}. Do '
                    'you wish to continue?')
                button_Yes = msg_box.addButton('Yes', QMessageBox.YesRole)
                _ = msg_box.addButton('No', QMessageBox.NoRole)
            if self.label.text() == 'Fecha:':
                window_title = 'Eliminar el punto'
                quit_msg = (
                    f'Está a punto de eliminar el punto N{found_row}. '
                    'Desea continuar?')
                button_Yes = msg_box.addButton('Sí', QMessageBox.YesRole)
                _ = msg_box.addButton('No', QMessageBox.NoRole)
            msg_box.setWindowTitle(window_title)
            msg_box.setText(quit_msg)
            msg_box.exec_()
            reply = msg_box.clickedButton()
            if reply == button_Yes:
                check_tableWidget_por(self)
                layer.startEditing()  # activate the 'Toggle Editing
                clear_point_of_reference_data_from_worksheet(self)
                enable_widgets(self)
                layer.deleteFeature(found_row)
                layer.commitChanges()  # Save changes and end edit mode
                layer.updateFields()
                QgsProject.instance().reloadAllLayers()
        else:
            clear_point_of_reference_data_from_worksheet(self)
            enable_widgets(self)


def disable_widgets(self):
    """
    Tab '4'. Section 4.2.
    Disable widgets that contain Point of Reference information.
    """

    self.pushButton_8.setEnabled(True)
    self.pushButton_30.setEnabled(True)
    self.lineEdit_29.setReadOnly(True)
    self.lineEdit_34.setReadOnly(True)
    self.lineEdit_35.setReadOnly(True)
    self.radioButton_6.setDisabled(True)
    self.radioButton_7.setDisabled(True)
    self.comboBox.setDisabled(True)


def enable_widgets(self):
    """
    Tab '4'. Section 4.2.
    Enable widgets that contain Point of Reference information.
    """

    self.pushButton_8.setDisabled(True)
    self.pushButton_30.setDisabled(True)
    self.lineEdit_29.setReadOnly(False)
    self.lineEdit_34.setReadOnly(False)
    self.lineEdit_35.setReadOnly(False)
    self.radioButton_6.setEnabled(True)
    self.radioButton_7.setEnabled(True)
    self.comboBox.setEnabled(True)


def register_point_on_map(self):
    """
    Tab '4'. Section 4.2.
    Register the Point of Reference on the map.
    """

    # Check if the layer exists
    layers = QgsProject.instance().mapLayers().values()
    name = []
    for layer in layers:
        name.append(layer.name())
    if any(x == 'Representative_Point' for x in name):
        # delete the last added which waswrongfully added
        delete_last_point(self, id)
        clear_point_of_reference_data_from_worksheet(self)
        # Store reference to the map canvas
        self.canvas = iface.mapCanvas()
        # Create the aps tool using the canvas reference
        self.point_tool = QgsMapToolEmitPoint(self.canvas)
        # connect signal that the canvas was clicked
        self.canvas.setMapTool(self.point_tool)
        self.point_tool.canvasClicked.connect(lambda: display_point_on_map(self))
        self.pushButton_7.setEnabled(False)
        self.pushButton_10.setEnabled(True)
        self.hide()
        project_crs = self.canvas.mapSettings().destinationCrs()
        self.lineEdit_27.setText(project_crs.description())
        self.lineEdit_28.setText(project_crs.authid())
        disable_widgets(self)
    else:
        msg_box = QMessageBox()
        if self.label.text().startswith('Ամսաթիվ'):
            window_title = 'Նախագիծը բեռնված չէ'
            quit_msg = ('Նախագծում բացակայում են կանխադրված շերտերը։\n\n'
                        'Ցանկանու՞մ եք ստեղծել նոր նախագիծ։')
            button_Yes = msg_box.addButton('Այո', QMessageBox.YesRole)
            _ = msg_box.addButton('Ոչ', QMessageBox.NoRole)
        if self.label.text() == 'Date:':
            window_title = 'The project is not loaded'
            quit_msg = ('The default layers are missing from the project.'
                        '\n\nWould you like to create a New Project?')
            button_Yes = msg_box.addButton('Yes', QMessageBox.YesRole)
            _ = msg_box.addButton('No', QMessageBox.NoRole)
        if self.label.text() == 'Fecha:':
            window_title = 'El proyecto no está cargado'
            quit_msg = ('Faltan las capas por defecto del proyecto\n\n'
                        '¿Desea crear un Nuevo Proyecto?')
            button_Yes = msg_box.addButton('Sí', QMessageBox.YesRole)
            _ = msg_box.addButton('No', QMessageBox.NoRole)
        msg_box.setWindowTitle(window_title)
        msg_box.setText(quit_msg)
        msg_box.exec_()
        reply = msg_box.clickedButton()
        if reply == button_Yes:
            self.create_new_project()


def check_tableWidget_por(self):
    """
    Delete the information on the Point of Reference from the tableWidgets.
    """

    layer_names = ['Monument_Area', 'Protected_Area']
    for layer_name in layer_names:
        point_value, polygon_value, last_point_feature, _, polygon_layer =\
            self.check_attribute_equality(layer_name)
        # Check if the attribute values are the same and
        # if the last_point_feature exists
        if (last_point_feature is not None and
            point_value is not None and
                polygon_value is not None):
            if point_value == polygon_value:
                if layer_name == 'Monument_Area':
                    clear_all_rows_and_remove_MA(self)
                else:
                    clear_all_rows_and_remove_PA(self)


def delete_last_point(self, id):
    """
    Tab '4'. Section 4.2.
    Delete the wrongfully added Point of Reference from the point layer.
    """

    layer = QgsProject.instance().mapLayersByName('Representative_Point')[0]
    if ((self.lineEdit_34.text() and self.lineEdit_35.text()) or
            self.textEdit_17.toPlainText().startswith('UPS')):
        layer.startEditing()
        # Get all features in the point layer
        point_features = [f for f in layer.getFeatures()]
        # Check if there are features in the point layer
        if not point_features:
            return
        # Get the last feature added to the point layer
        last_point_feature = point_features[-1]
        # Empty tablewidgets
        check_tableWidget_por(self)
        # Delete the last feature id from the layer
        layer.deleteFeature(last_point_feature[0])
        self.lineEdit_34.clear()
        self.lineEdit_35.clear()
        self.textEdit_17.clear()
        layer.commitChanges()  # Save changes and end edit mode
    layer.updateFields()
    QgsProject.instance().reloadAllLayers()


def display_point_on_map(self):
    """
    Display a point on the map and update the UI with the corresponding
    UTM values.
    """

    point = self.canvas.getCoordinateTransform().toMapCoordinates(
        self.canvas.mouseLastXY())
    layer = QgsProject.instance().mapLayersByName('Representative_Point')[0]
    if layer:
        layer.startEditing()
        feat = QgsFeature(layer.fields())

        zone, latitude_band, hemisphere, easting, northing = \
            get_utm_values(self, point)

        # Set values in the UI
        other_values = ['A', 'B', 'Y', 'Z']
        id_string = ''
        if latitude_band in other_values:
            easting, northing = ups_coords(self, latitude_band, point)
            id_string = (f'{latitude_band} {easting}mE {northing}mN')
        else:
            set_combobox_value(self, latitude_band)
            self.lineEdit_29.setText(str(zone))
            set_hemisphere_radio_button(self, hemisphere)
            self.lineEdit_34.setText(str(easting))
            self.lineEdit_35.setText(str(northing))
            zone, latitude_band, hemisphere, _, _ = \
                get_UTM_values_from_POR(self)
            id_string = (f'{hemisphere} {zone}{latitude_band} '
                         f'{easting} {northing}')
        # Iterate through the features and find the row where the data was
        # introduced
        found_row = None
        for feature in layer.getFeatures():
            if feature['4.2.loin_coorpore_full_utm'] == id_string:
                found_row = feature.id()
                break
        if found_row is not None:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            if self.label.text().startswith('Ամսաթիվ'):
                window_title = ''
                quit_msg = (
                    f'Համապատասխան միավորը գրանցված է N{found_row} համարի '
                    'ներքո։\n\nԵթե ցանկանում եք փոխել տվյալները, խնդրում '
                    'ենք հեռացնել տվյալնատները «Հեռացնել» կոճակի միջոցով '
                    'և մուտքագրել նոր տվյալներ:')
                _ = msg_box.addButton(
                    'Շարունակել', QMessageBox.YesRole)
            if self.label.text() == 'Date:':
                window_title = ''
                quit_msg = (
                    'The corresponding unit is registered under number '
                    f'N{found_row}.\n\nIf you want to change the data, '
                    'please remove the input information using the '
                    '"Remove" button and enter new data.')
                _ = msg_box.addButton('OK', QMessageBox.YesRole)
            if self.label.text() == 'Fecha:':
                window_title = ''
                quit_msg = (
                    'La unidad correspondiente está registrada bajo el '
                    f'número N{found_row}.\n\nSi desea cambiar los datos, '
                    'elimínelos con el botón "Eliminar" e introduzca '
                    'datos nuevos.')
                _ = msg_box.addButton('Continuar', QMessageBox.YesRole)
            msg_box.setWindowTitle(window_title)
            msg_box.setText(quit_msg)
            msg_box.exec_()
        else:
            # Set the value for the 'ID' field
            feat['4.2.loin_coorpore_full_utm'] = id_string
            feat.setGeometry(QgsGeometry.fromPointXY(
                QgsPointXY(point.x(), point.y())))
            # Add feature to the layer
            res, outFeats = layer.dataProvider().addFeatures([feat])
            pivot_endge_text(self)
            self.show()
            self.pantool()
            point_of_reference(self)
            layer.commitChanges()
            layer.updateFields()
            QgsProject.instance().reloadAllLayers()
            if self.lineEdit_34.text() and self.lineEdit_35.text():
                self.scrollArea_8.setEnabled(True)
                self.groupBox_9.setEnabled(True)
                self.groupBox_10.setEnabled(True)


def get_utm_values(self, point):
    """Retrieve UTM values for the given point."""

    project_crs = self.canvas.mapSettings().destinationCrs()
    transform_context = QgsCoordinateTransformContext()
    hem_text_n, hem_text_s = '', ''
    if self.label.text().startswith('Ամսաթիվ'):
        hem_text_n = 'Հս'
        hem_text_s = 'Հվ'
    else:
        hem_text_n = 'N'
        hem_text_s = 'S'
    if project_crs.authid() == 'EPSG:4326':
        project = (QgsCoordinateReferenceSystem('EPSG:3857'))
        target_crs = QgsCoordinateReferenceSystem('EPSG:4326')  # WGS 84
        transform = QgsCoordinateTransform(
            project, target_crs, transform_context)
        utm_point = transform.transform(point)
        # Calculate UTM zone based on the x-coordinate of the point
        if utm_point.x() < 180:
            zone = int(31 + (utm_point.x() / 6.0))
        else:
            zone = int((utm_point.x() / 6) - 29)

        if zone > 60:
            zone = 1
        # Handle UTM special cases
        if 56.0 <= utm_point.y() < 64.0 and 3.0 <= utm_point.x() < 12.0:
            zone = 32

        if 72.0 <= utm_point.y() < 84.0:
            if 0.0 <= utm_point.x() < 9.0:
                zone = 31
            elif 9.0 <= utm_point.x() < 21.0:
                zone = 33
            elif 21.0 <= utm_point.x() < 33.0:
                zone = 35
            elif 33.0 <= utm_point.x() < 42.0:
                zone = 37

        band_index = int((utm_point.y() + 80) / 8)
        if band_index < 0:
            band_index = 0
        elif band_index >= len('CDEFGHJKLMNPQRSTUVWX'):
            band_index = len('CDEFGHJKLMNPQRSTUVWX') - 1
        latitude_band = 'CDEFGHJKLMNPQRSTUVWX'[band_index]

        hemisphere = str(hem_text_n) if point.y() >= 0 else str(hem_text_s)
        utmcrs = QgsCoordinateReferenceSystem(
            utm_get_epsg(self, hemisphere, zone))
        utmtrans = QgsCoordinateTransform(
            project, utmcrs, transform_context)
        utm_point_new = utmtrans.transform(point)

        easting = f'{utm_point_new.x():.0f}'
        northing = f'{utm_point_new.y():.0f}'

        if utm_point.x() < -180 or utm_point.x() > 360:
            zone = ''
        if utm_point.y() > 84.5 or utm_point.y() < -80.5:
            zone = ''

        if hemisphere == hem_text_n:
            if 84.5 <= utm_point.y() < 90 and 0 <= utm_point.x() < 180:
                latitude_band = 'Z'
            elif 84.5 <= utm_point.y() < 90 and -180 <= utm_point.x() < 0:
                latitude_band = 'Y'
        elif hemisphere == hem_text_s:
            if -90 <= utm_point.y() < -80 and 0 <= utm_point.x() < 180:
                latitude_band = 'B'
            elif -90 <= utm_point.y() < -80 and -180 <= utm_point.x() < 0:
                latitude_band = 'A'

    else:
        project = (QgsCoordinateReferenceSystem('EPSG:3857'))
        target_crs = QgsCoordinateReferenceSystem('EPSG:4326')  # WGS 84
        transform = QgsCoordinateTransform(
            project_crs, target_crs, transform_context)
        utm_point = transform.transform(point)
        # Calculate UTM zone based on the x-coordinate of the point

        if utm_point.x() < 180:
            zone = int(31 + (utm_point.x() / 6.0))
        else:
            zone = int((utm_point.x() / 6) - 29)

        if zone > 60:
            zone = 1
        # Handle UTM special cases
        if 56.0 <= utm_point.y() < 64.0 and 3.0 <= utm_point.x() < 12.0:
            zone = 32

        if 72.0 <= utm_point.y() < 84.0:
            if 0.0 <= utm_point.x() < 9.0:
                zone = 31
            elif 9.0 <= utm_point.x() < 21.0:
                zone = 33
            elif 21.0 <= utm_point.x() < 33.0:
                zone = 35
            elif 33.0 <= utm_point.x() < 42.0:
                zone = 37

        band_index = int((utm_point.y() + 80) / 8)
        if band_index < 0:
            band_index = 0
        elif band_index >= len('CDEFGHJKLMNPQRSTUVWX'):
            band_index = len('CDEFGHJKLMNPQRSTUVWX') - 1
        latitude_band = 'CDEFGHJKLMNPQRSTUVWX'[band_index]

        hemisphere = str(hem_text_n) if point.y() >= 0 else str(hem_text_s)

        utmcrs = QgsCoordinateReferenceSystem(utm_get_epsg(self, hemisphere, zone))
        utmtrans = QgsCoordinateTransform(project_crs, utmcrs, transform_context)
        utm_point_new = utmtrans.transform(point)

        easting = f'{utm_point_new.x():.0f}'
        northing = f'{utm_point_new.y():.0f}'

        if utm_point.x() < -180 or utm_point.x() > 360:
            zone = ''
        if utm_point.y() > 84.5 or utm_point.y() < -80.5:
            zone = ''

        if hemisphere == hem_text_n:
            if 84.5 <= utm_point.y() < 90 and 0 <= utm_point.x() < 180:
                latitude_band = 'Z'
            elif 84.5 <= utm_point.y() < 90 and -180 <= utm_point.x() < 0:
                latitude_band = 'Y'
        elif hemisphere == hem_text_s:
            if -90 <= utm_point.y() < -80 and 0 <= utm_point.x() < 180:
                latitude_band = 'B'
            elif -90 <= utm_point.y() < -80 and -180 <= utm_point.x() < 0:
                latitude_band = 'A'

    return zone, latitude_band, hemisphere, easting, northing


def set_combobox_value(self, value):
    """Tab '5'. Add a row. Pop up window. Set the value of a combobox."""

    self.comboBox.clear()
    combo_box_values = [
        ' ', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
        'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X']
    self.comboBox.addItems(combo_box_values)
    if value in combo_box_values:
        index = combo_box_values.index(value)
        self.comboBox.setCurrentIndex(index)


def ups_coords(self, latitude_band, point):
    """
    Convert geographical coordinates to the Universal Polar Stereographic (UPS)
    system if the point clicked on the map is in the polar regions,
    specifically areas above 84°N and below 80°S.
    """

    # epsg4326 = QgsCoordinateReferenceSystem('EPSG:4326')
    epsg32661 = QgsCoordinateReferenceSystem('EPSG:32661')
    epsg32761 = QgsCoordinateReferenceSystem('EPSG:32761')
    epsg3857 = (QgsCoordinateReferenceSystem('EPSG:3857'))

    project_crs = self.canvas.mapSettings().destinationCrs()
    if latitude_band == 'Y' or latitude_band == 'Z':
        target_epsg = epsg32661
    elif latitude_band == 'A' or latitude_band == 'B':
        target_epsg = epsg32761
    if project_crs.authid() == 'EPSG:4326':
        transform_ups = QgsCoordinateTransform(
            epsg3857, target_epsg, QgsCoordinateTransformContext())
    else:
        transform_ups = QgsCoordinateTransform(
            project_crs, target_epsg, QgsCoordinateTransformContext())
    ups_point = transform_ups.transform(point)
    ups_easting = f'{ups_point.x():.0f}'
    ups_northing = f'{ups_point.y():.0f}'
    id_string = f'{latitude_band} {ups_easting}mE {ups_northing}mN'
    self.textEdit_17.setText('UPS - '+id_string)

    return ups_easting, ups_northing


def set_hemisphere_radio_button(self, hemisphere):
    """Set the radioButton for the specified hemisphere."""

    if hemisphere == 'Հս' or hemisphere == 'N':
        self.radioButton_6.setChecked(True)
    else:
        self.radioButton_7.setChecked(True)


def utm_get_epsg(self, hemisphere, zone):
    """Retrieve the EPSG code for the given UTM zone and hemisphere."""

    if hemisphere == 'Հս' or hemisphere == 'N':
        code = 32600 + zone
    elif hemisphere == 'Հվ' or hemisphere == 'S':
        code = 32700 + zone
    return code


def point_of_reference(self):
    """
    Tab '5'. TableWgidgets.
    Place the Point of Reference coodinate data in the tableWidgets.
    """

    hem_text_n, hem_text_s = '', ''
    if self.label.text().startswith('Ամսաթիվ'):
        hem_text_n = 'Հս'
        hem_text_s = 'Հվ'
    else:
        hem_text_n = self.radioButton_6.text()[0]
        hem_text_s = self.radioButton_7.text()[0]
    if self.radioButton_6.isChecked():
        hemisphere = str(hem_text_n)
    else:
        hemisphere = str(hem_text_s)

    if (self.lineEdit_34.text() and
            self.lineEdit_35.text() and
            self.comboBox.currentIndex() != 0 and
            (self.radioButton_6.isChecked() is True or
                self.radioButton_7.isChecked() is True)):
        # lineedits are not empty
        # Check if any features already have the same ID
        _, latitude_band, _, easting, northing = \
            get_UTM_values_from_POR(self)
        zone = (f'{hemisphere} {self.lineEdit_29.text()}{latitude_band}')
        easting, northing = self.lineEdit_34.text(), self.lineEdit_35.text()
    elif self.textEdit_17.toPlainText().startswith('UPS'):
        components = self.textEdit_17.toPlainText().split()
        latitude_band = components[2]
        easting = (components[3][:-2])
        northing = (components[4][:-2])
        zone = f'{latitude_band}'
        self.scrollArea_8.setEnabled(True)
        self.groupBox_9.setEnabled(True)
        self.groupBox_10.setEnabled(True)

    def update_table_widget(table_widget, suffix=''):
        if table_widget.rowCount() != 1:
            numRows = table_widget.rowCount()
            table_widget.insertRow(numRows)
        if self.label.text().startswith('Ամսաթիվ'):
            item0 = QTableWidgetItem('Ա')
        else:
            item0 = QTableWidgetItem('A')
        table_widget.setItem(0, 0, item0)
        table_widget.setItem(0, 3, QTableWidgetItem(zone))
        table_widget.setItem(0, 4, QTableWidgetItem(easting))
        table_widget.setItem(0, 5, QTableWidgetItem(northing))

    update_table_widget(self.tableWidget)
    update_table_widget(self.tableWidget_1, '1')


def clear_style_MA(self):
    """
    Tab '5'. Section 5.1. Numbering.
    Clear the edge numbering style from the map.
    """

    lyr1 = QgsProject.instance().mapLayersByName('Monument_Area')[0]
    lyr1.renderer().symbol().deleteSymbolLayer(1)
    lyr1.renderer().symbol().deleteSymbolLayer(1)
    lyr1.triggerRepaint()


def clear_style_PA(self):
    """
    Tab '5'. Section 5.2. Numbering.
    Clear the edge numbering style from the map.
    """

    lyr1 = QgsProject.instance().mapLayersByName('Protected_Area')[0]
    lyr1.renderer().symbol().deleteSymbolLayer(1)
    lyr1.renderer().symbol().deleteSymbolLayer(1)
    lyr1.triggerRepaint()


def hide_numbering_from_map_MA(self):
    """
    Tab '5'. Section 5.1. Numbering.
    Hide edge numbering from the map.
    """

    clear_style_MA(self)
    self.radioButton_61.setDisabled(True)
    self.radioButton_62.setDisabled(True)


def hide_numbering_from_map_PA(self):
    """
    Tab '5'. Section 5.2. Numbering.
    Hide edge numbering from the map.
    """

    clear_style_PA(self)
    self.radioButton_63.setDisabled(True)
    self.radioButton_64.setDisabled(True)


def show_numbering_on_map_MA(self):
    """
    Tab '5'. Section 5.1. Numbering.
    Show edge numbering on the map.
    """

    clear_style_MA(self)
    self.radioButton_61.setChecked(True)
    self.radioButton_61.setEnabled(True)
    self.radioButton_62.setEnabled(True)
    numbering_style_white_MA(self)


def show_numbering_on_map_PA(self):
    """
    Tab '5'. Section 5.1. Numbering.
    Show edge numbering on the map.
    """

    clear_style_PA(self)
    self.radioButton_63.setChecked(True)
    self.radioButton_63.setEnabled(True)
    self.radioButton_64.setEnabled(True)
    numbering_style_white_PA(self)


def numbering_style_white_MA(self):
    """
    Tab '5'. Section 5.1. Numbering. Light
    Show 'Light' numbering of the edges on the map.
    """

    clear_style_MA(self)
    lyr1 = QgsProject.instance().mapLayersByName('Monument_Area')[0]
    color_base = QColor(218, 218, 218, 89)
    black = QColor(0, 0, 0, 255)
    white = QColor(255, 255, 255, 255)
    color_num = black
    color_base_mark = white
    if self.radioButton_61.isChecked():
        color_num = black
        color_base_mark = white
    elif self.radioButton_62.isChecked():
        color_num = white
        color_base_mark = black

    # base symbol
    base_symbol = QgsSimpleFillSymbolLayer(
        color=color_base,
        strokeColor=black,
        strokeWidth=0.5)
    lyr1.renderer().symbol().changeSymbolLayer(0, base_symbol)
    lyr1.triggerRepaint()

    # markerline white circle
    markerLine2 = QgsMarkerLineSymbolLayer.create()
    markerLine2.setPlacement(Qgis.MarkerLinePlacement.Vertex)
    lyr1.renderer().symbol().appendSymbolLayer(markerLine2)
    base_color = QgsSimpleMarkerSymbolLayer(
        shape=QgsSimpleMarkerSymbolLayer.Circle,
        size=4.5,
        color=color_base_mark,
        strokeColor=black)
    marker_symbol1 = QgsMarkerSymbol()
    marker_symbol1.changeSymbolLayer(0, base_color)
    markerLine2.setSubSymbol(marker_symbol1)
    lyr1.renderer().symbol().appendSymbolLayer(base_color)
    lyr1.triggerRepaint()

    # markerLine numbers
    markerLine = QgsMarkerLineSymbolLayer.create()
    markerLine.setPlacement(Qgis.MarkerLinePlacement.Vertex)
    markerLine.setRotateMarker(False)
    lyr1.renderer().symbol().appendSymbolLayer(markerLine)
    symb_numbering = QgsFontMarkerSymbolLayer(
        fontFamily='Arial',
        chr='',
        pointSize=3.5,
        color=color_num)

    symb_numbering.setDataDefinedProperty(
        QgsSymbolLayer.PropertyCharacter,
        QgsProperty.fromExpression('@geometry_point_num'))
    symb_numbering.setOffset(QPointF(0, -0.4))
    marker_symbol = QgsMarkerSymbol()
    marker_symbol.changeSymbolLayer(0, symb_numbering)
    markerLine.setSubSymbol(marker_symbol)
    lyr1.renderer().symbol().appendSymbolLayer(symb_numbering)
    lyr1.triggerRepaint()


def numbering_style_white_PA(self):
    """
    Tab '5'. Section 5.2. Numbering. Light
    Show 'Light' numbering of the edges on the map.
    """

    layer = QgsProject.instance().mapLayersByName('Protected_Area')[0]

    color_base = QColor(218, 218, 218, 89)
    black = QColor(0, 0, 0, 255)
    white = QColor(255, 255, 255, 255)
    color_num = black
    color_base_mark = white
    if self.radioButton_63.isChecked():
        color_num = black
        color_base_mark = white
    elif self.radioButton_64.isChecked():
        color_num = white
        color_base_mark = black

    # base symbol
    myRenderer = layer.renderer()
    mySymbol1 = QgsFillSymbol.createSimple(
        {'color': color_base, 'color_border': black,
         'width_border': '0.5', 'outline_style': 'dot'})
    myRenderer.setSymbol(mySymbol1)
    layer.triggerRepaint()

    # markerline white circle
    markerLine2 = QgsMarkerLineSymbolLayer.create()
    markerLine2.setPlacement(Qgis.MarkerLinePlacement.Vertex)
    layer.renderer().symbol().appendSymbolLayer(markerLine2)
    base_color = QgsSimpleMarkerSymbolLayer(
        shape=QgsSimpleMarkerSymbolLayer.Circle,
        size=4.5,
        color=color_base_mark,
        strokeColor=black)
    marker_symbol1 = QgsMarkerSymbol()
    marker_symbol1.changeSymbolLayer(0, base_color)
    markerLine2.setSubSymbol(marker_symbol1)
    layer.renderer().symbol().appendSymbolLayer(base_color)
    layer.triggerRepaint()

    # markerLine numbers
    markerLine = QgsMarkerLineSymbolLayer.create()
    markerLine.setPlacement(Qgis.MarkerLinePlacement.Vertex)
    markerLine.setRotateMarker(False)
    layer.renderer().symbol().appendSymbolLayer(markerLine)
    symb_numbering = QgsFontMarkerSymbolLayer(
        fontFamily='Arial',
        chr='',
        pointSize=3.5,
        color=color_num)

    symb_numbering.setDataDefinedProperty(
        QgsSymbolLayer.PropertyCharacter,
        QgsProperty.fromExpression('@geometry_point_num'))
    symb_numbering.setOffset(QPointF(0, -0.4))
    marker_symbol = QgsMarkerSymbol()
    marker_symbol.changeSymbolLayer(0, symb_numbering)
    markerLine.setSubSymbol(marker_symbol)
    layer.renderer().symbol().appendSymbolLayer(symb_numbering)
    layer.triggerRepaint()


def numbering_style_black_MA(self):
    """
    Tab '5'. Section 5.1. Numbering. Dark.
    Show 'Dark' numbering of the edges on the map.
    """

    clear_style_MA(self)
    numbering_style_white_MA(self)


def numbering_style_black_PA(self):
    """
    Tab '5'. Section 5.2. Numbering. Dark.
    Show 'Dark' numbering of the edges on the map.
    """

    clear_style_PA(self)
    numbering_style_white_PA(self)


def add_point_to_table(self, table_widget):
    """
    Add UTM values to the specified tableWidget.
    Rretrieve the UTM values from the dialog and insert them into the table
    as new rows.
    """

    numRows = table_widget.rowCount()
    utm_values = get_poly_utm_values(self)
    if utm_values is not None:
        dlg_zone, dlg_easting, dlg_northing = utm_values
        table_widget.setItem(numRows-1, 3, QTableWidgetItem(dlg_zone))
        table_widget.setItem(numRows-1, 4, QTableWidgetItem(dlg_easting))
        table_widget.setItem(numRows-1, 5, QTableWidgetItem(dlg_northing))


def add_point_2_tableMA(self):
    """Add UTM values to the Monument Area tableWidget."""

    add_point_to_table(self, self.tableWidget)


def add_point_2_tablePA(self):
    """Add UTM values to the Protected Area tableWidget."""

    add_point_to_table(self, self.tableWidget_1)


def get_poly_utm_values(self):
    """
    Get UTM values from the pop-up dialog and validate them. If the
    required information is missing, display an information dialog
    prompting the user to fill in the missing information.
    """

    if (self.AddPointPoly.lineEdit.text() and
            self.AddPointPoly.comboBox.currentIndex() != 0 and
            self.AddPointPoly.lineEdit_2.text() and
            self.AddPointPoly.lineEdit_3.text() and
            (self.AddPointPoly.radioButton.isChecked() is True or
                self.AddPointPoly.radioButton_2.isChecked() is True)):
        dlg_utm = self.AddPointPoly.lineEdit.text()
        dlg_lat_band = self.AddPointPoly.comboBox.currentText()
        dlg_hemisphere = self.AddPointPoly.radioButton.text()[0] if self.AddPointPoly.radioButton.isChecked() else self.AddPointPoly.radioButton_2.text()[0]
        dlg_zone = str(f'{dlg_hemisphere} {dlg_utm}{dlg_lat_band}')
        dlg_easting = self.AddPointPoly.lineEdit_2.text()
        dlg_northing = self.AddPointPoly.lineEdit_3.text()
        return (dlg_zone, dlg_easting, dlg_northing)
    else:
        msg_box = QMessageBox()
        if self.AddPointPoly.label.text().startswith('UTM գոտի'):
            msg_box.information(
                self,
                'Տվյալները բացակայում են',
                'Խնդրում ենք լրացնել բաց թողնված տեղեկատվությունը և նորից'
                'փորձել:')
        elif self.AddPointPoly.label.text() == 'UTM Zone:':
            msg_box.information(
                self,
                'Missing data',
                'Please fill in the missing information and try again.')
        elif self.AddPointPoly.label.text() == 'Zona UTM:':
            msg_box.information(
                self,
                'Faltan datos',
                'Rellene los datos que faltan e inténtelo de nuevo.')


def is_polygon_already_added(self, layer_name, new_polygon):
    """
    Check if a polygon with the same geometry as 'new_polygon' is already
    present in the specified layer.
    """

    # Get the layer containing the polygons
    layer = QgsProject.instance().mapLayersByName(layer_name)[0]
    # Iterate through the features in the layer
    for feature in layer.getFeatures():
        # Compare feature geometry with the geometry of the new polygon
        if feature.geometry().equals(new_polygon):
            # Return True and the feature ID if a match is found
            return True, feature.id()
    return False, None  # Return False if no match is found


def area_calc(self, layer_name, lineEdit_ha, lineEdit_sqm, lineEdit_ha_2):
    """
    Calculate the area of polygons in the specified layer and update the
    provided lineEdit widgets with the calculated values.
    """

    layer = QgsProject.instance().mapLayersByName(layer_name)[0]
    d = QgsDistanceArea()
    crs = QgsProject.instance().crs()
    d.setEllipsoid('{}'.format(crs))
    feat = layer.getFeatures()
    for f in feat:
        geom = f.geometry()
        sq_m = d.measureArea(geom)
        ha = sq_m / 10000
        lineEdit_ha.setText('{:.2f}'.format(ha))
        lineEdit_sqm.setText('{:.2f}'.format(sq_m))


def numbering(self, table_widget):
    """
    Assign sequential numbering to rows in the specified tableWidget and
    update the table accordingly.
    """

    numRows = table_widget.rowCount()
    for row in range(1, numRows):
        table_widget.setItem(row, 0, QTableWidgetItem('{}'.format(row)))
        easting = table_widget.item(row - 1, 0).text()
        northing = table_widget.item(row, 0).text()
        table_widget.setItem(
            row - 1, 1, QTableWidgetItem(f'{easting}-{northing}'))
        table_widget.setItem(
            row, 1, QTableWidgetItem(f'{northing}-1'))


def clear_all_rows(
        self, table_widget, line_edit_1, line_edit_2, line_edit_ha_2,
        push_button_1, push_button_2, push_button_3, push_button_4):
    """
    Clear all rows in a specified tableWidget and reset the provided
    lineEdit and pushButton widgets.
    """

    num_rows = table_widget.rowCount()
    for _ in range(1, num_rows):
        table_widget.removeRow(1)
    line_edit_1.clear()
    line_edit_2.clear()
    table_widget.setItem(0, 1, QTableWidgetItem(''))
    table_widget.setItem(0, 2, QTableWidgetItem(''))
    push_button_1.setDisabled(True)
    push_button_2.setDisabled(True)
    push_button_3.setDisabled(True)
    push_button_4.setDisabled(True)


def delete_polygon(self, layer_name):
    """Delete the last added polygon from the specified layer."""

    layer = QgsProject.instance().mapLayersByName(layer_name)[0]
    caps = layer.dataProvider().capabilities()
    if caps & QgsVectorDataProvider.DeleteFeatures:
        layer.startEditing()
        layer.startEditing()
        # Get all features in the point layer
        point_features = [f for f in layer.getFeatures()]
        # Check if there are features in the point layer
        if not point_features:
            return
        # Get the last feature added to the point layer
        last_point_feature = point_features[-1]
        # Delete the last feature id from the layer
        layer.deleteFeature(last_point_feature[0])
        layer.triggerRepaint()
        layer.commitChanges()
        layer.updateExtents()
    QgsProject.instance().reloadAllLayers()


def clear_all_rows_and_remove_polygon(
        self, table_widget, line_edit1, line_edit2, push_button1,
        push_button2, push_button3, push_button4):
    """
    Clear all rows in the specified tableWidget, remove the last added
    polygon from the corresponding layer, and reset associated widgets.
    """

    if table_widget.rowCount() != 1:
        if table_widget == self.tableWidget_1:
            layer_name = 'Protected_Area'
        else:
            layer_name = 'Monument_Area'
        delete_polygon(self, layer_name)
        clear_all_rows(
            self, table_widget, line_edit1, line_edit2, '', push_button1,
            push_button2, push_button3, push_button4)
    else:
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        if self.label.text().startswith('Ամսաթիվ'):
            msg_box.information(
                self, '',
                'Չկա ջնջման ենթակա տարր:\n\nԽնդրում ենք ստեղծել '
                'բազմանկյուն:')
        elif self.label.text() == 'Date:':
            msg_box.information(
                self, '',
                'There is no element to be cleared.\n\nPlease, create a '
                'polygon.')
        elif self.label.text() == 'Fecha:':
            msg_box.information(
                self, '',
                'No hay ningún elemento que limpiar.\n\nPor favor, crea '
                'un polígono.')


def clear_all_rows_and_remove_MA(self):
    """
    Clear all rows and remove the last added polygon from the Monument Area
    layer.
    """

    clear_all_rows_and_remove_polygon(
        self, self.tableWidget, self.lineEdit_45, self.lineEdit_83,
        self.pushButton_11, self.pushButton_12, self.pushButton_14,
        self.pushButton_13)


def clear_all_rows_and_remove_PA(self):
    """
    Clear all rows and remove the last added polygon from the Polygon Area
    layer.
    """
    clear_all_rows_and_remove_polygon(
        self, self.tableWidget_1, self.lineEdit_131, self.lineEdit_132,
        self.pushButton_18, self.pushButton_19, self.pushButton_21,
        self.pushButton_20)


def create_geometry_poly(self, layer_name, table_widget):
    """
    Create a polygon geometry based on the points stored in the
    tableWidget. Check if the polygon is already added to the layer and add
    it if otherwise.
    """

    layer = QgsProject.instance().mapLayersByName(layer_name)[0]
    caps = layer.dataProvider().capabilities()
    if caps & QgsVectorDataProvider.AddFeatures:
        provider = layer.dataProvider()
        feature = QgsFeature()
        numRows = table_widget.rowCount()
        coords = []
        for row in range(1, numRows):
            x = float(QTableWidgetItem(table_widget.item(row, 1)).text())
            y = float(QTableWidgetItem(table_widget.item(row, 2)).text())
            tup = (x, y)
            coords.append(tup)
        coords = coords[:-1]  # delete the last (Right Click) point
        table_widget.removeRow(numRows - 1)
        new_polygon = QgsGeometry.fromPolygonXY(
            [[QgsPointXY(pair[0], pair[1]) for pair in coords]])
        # Check if the polygon is already added
        is_added, fid = is_polygon_already_added(
            self, layer_name, new_polygon)
        if is_added:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            if self.label.text().startswith('Ամսաթիվ'):
                msg_box.information(
                    self, '',
                    f'Համապատասխան միավորը գրանցված է N{fid} համարի ներքո։'
                    '\n\nԵթե ցանկանում եք փոխել տվյալները, խնդրում ենք '
                    'հեռացնել տվյալնատները «Հեռացնել» կոճակի միջոցով և '
                    'մուտքագրել նոր տվյալներ:')
            elif self.label.text() == 'Date:':
                msg_box.information(
                    self, '',
                    'The corresponding unit is registered under number '
                    f'N{fid}.\n\nIf you want to change the data, please '
                    'remove the input information using the "Remove" '
                    'button and enter new data.')
            elif self.label.text() == 'Fecha:':
                msg_box.information(
                    self, '',
                    'La unidad correspondiente está registrada bajo el '
                    f'número N{fid}.\n\nSi desea cambiar los datos, '
                    'elimínelos con el botón "Eliminar" e introduzca '
                    'datos nuevos.')
        else:
            feature.setGeometry(new_polygon)
            provider.addFeatures([feature])
            layer.updateExtents()
            QgsProject.instance().reloadAllLayers()


def distance_calc(self, table_widget):
    """
    Calculate distances between points stored in a tableWidget and update
    the table with the calculated distances.
    """

    numRows = table_widget.rowCount()
    for row in range(1, numRows):
        # create origin lat-lon
        easting_o = float(QTableWidgetItem(
            table_widget.item(row - 1, 4)).text())
        northing_o = float(QTableWidgetItem(
            table_widget.item(row - 1, 5)).text())
        # create destination easting-northing
        easting_d = float(QTableWidgetItem(
            table_widget.item(row, 4)).text())
        northing_d = float(QTableWidgetItem(
            table_widget.item(row, 5)).text())
        # create pointA easting-northing
        easting_A = float(QTableWidgetItem(
            table_widget.item(0, 4)).text())
        northing_A = float(QTableWidgetItem(
            table_widget.item(0, 5)).text())
        # create point1 easting-northing
        easting1 = float(QTableWidgetItem(
            table_widget.item(1, 4)).text())
        northing1 = float(QTableWidgetItem(
            table_widget.item(1, 5)).text())
        origin = QgsPointXY(easting_o, northing_o)
        destination = QgsPointXY(easting_d, northing_d)
        point1 = QgsPointXY(easting1, northing1)
        pointA = QgsPointXY(easting_A, northing_A)
        # Create a measure object
        distance = QgsDistanceArea()
        m = distance.measureLine(origin, destination)
        # distance from the point1
        m1 = distance.measureLine(destination, point1)
        # distance from the pointA to 1
        mA_1 = distance.measureLine(pointA, point1)
        # distances between two points, precision of 2 decimal points
        table_widget.setItem(
            row - 1, 2, QTableWidgetItem(
                '{}'.format(str('{:.2f}'.format(m)))))
        table_widget.setItem(
            row, 2, QTableWidgetItem(
                '{}'.format(str('{:.2f}'.format(m1)))))
        table_widget.setItem(
            0, 2, QTableWidgetItem(
                '{}'.format(str('{:.2f}'.format(mA_1)))))


def rightclick(
        self, layer_name, table_widget, line_edit_1, line_edit_2,
        push_button_1, push_button_2, push_button_3, push_button_4):
    """
    Clear the tableWidget, delete the last added polygon from the layer,
    and update the layer with new data.
    """

    # Get the number of rows in the tableWidget
    numRows = table_widget.rowCount()
    if numRows < 3:  # Check if the number of rows is less than 2
        push_button_2.setDisabled(True)
        push_button_3.setDisabled(True)
    if numRows < 5:  # Check if the number of rows is less than 4
        # Display a message box indicating that minimum 3 points are needed
        msg_box = QMessageBox()
        if self.label.text().startswith('Ամսաթիվ'):
            msg_box.information(
                self, 'Ուշադրություն',
                'Գրանցման համար անհրաժեշտ է առնվազն 3 կետ։')
        elif self.label.text() == 'Date:':
            msg_box.information(
                self, 'Warning',
                'A minimum of 3 points is required to be registered.')
        elif self.label.text() == 'Fecha:':
            msg_box.information(
                self, 'Atención',
                'Se requiere un mínimo de 3 puntos para ser registrado.')
        # Clear all rows except the first one
        clear_all_rows(
            self, table_widget, line_edit_1, line_edit_2, '', push_button_1,
            push_button_2, push_button_3, push_button_4)
    else:
        create_geometry_poly(self, layer_name, table_widget)
        distance_calc(self, table_widget)
        numbering(self, table_widget)
        layer = QgsProject.instance().mapLayersByName(layer_name)[0]
        area_calc(self, layer_name, line_edit_1, line_edit_2, line_edit_1)
        push_button_1.setEnabled(True)
        push_button_2.setEnabled(True)
        push_button_3.setEnabled(True)
        push_button_4.setEnabled(True)
        layer.commitChanges()
        layer.updateFields()
        QgsProject.instance().reloadAllLayers()
        update_polygon_layer(self, layer_name)
    self.show()
    self.pantool()


def rightclickMA(self):
    """
    When right-clicking to draw a polygon for the Monument Area layer.
    """

    rightclick(
        self, 'Monument_Area', self.tableWidget, self.lineEdit_45,
        self.lineEdit_83, self.pushButton_11, self.pushButton_12,
        self.pushButton_14, self.pushButton_13)


def rightclickPA(self):
    """
    When right-clicking to draw a polygon for the Protected Area layer.
    """

    rightclick(
        self, 'Protected_Area', self.tableWidget_1, self.lineEdit_131,
        self.lineEdit_132, self.pushButton_18, self.pushButton_19,
        self.pushButton_21, self.pushButton_20)


def update_polygon_layer(self, layer_name):
    """
    Update the attribute value of the polygon layer with the UTM
    coordinates of the last added point.
    """

    # Get the point and polygon layers
    point_layer = QgsProject.instance().mapLayersByName(
        'Representative_Point')[0]
    polygon_layer = QgsProject.instance().mapLayersByName(layer_name)[0]
    # Get all features in the point layer
    point_features = [f for f in point_layer.getFeatures()]
    # Check if there are features in the point layer
    if not point_features:
        return
    # Get the last feature added to the point layer
    last_point_feature = point_features[-1]
    # Get all features in the polygon layer
    polygon_features = [f for f in polygon_layer.getFeatures()]
    # Check if there are features in the polygon layer
    if not polygon_features:
        return
    # Get the last feature added to the polygon layer
    last_polygon_feature = polygon_features[-1]
    # Get the field index of the field to be updated
    field_index = polygon_layer.fields().indexFromName(
        '4.2.loin_coorpore_full_utm')
    # Start editing the polygon layer
    polygon_layer.startEditing()
    # Update the attribute value in the polygon layer
    polygon_layer.changeAttributeValue(
        last_polygon_feature.id(), field_index,
        last_point_feature['4.2.loin_coorpore_full_utm'])
    polygon_layer.commitChanges()  # Commit changes to the polygon layer


def store_values_in_table(
        self, point, event, table_widget, rightclick_method):
    """
    Store UTM coordinates of a clicked point in the tableWidget and
    trigger the right-click action when done constructing the polygon.
    """

    numRows = table_widget.rowCount()
    table_widget.insertRow(numRows)
    zone, latitude_band, hemisphere, easting, northing = \
        get_utm_values(self, point)

    x = f'{(point.x()):.0f}'
    y = f'{(point.y()):.0f}'
    table_widget.setItem(numRows, 1, QTableWidgetItem(str(x)))
    table_widget.setItem(numRows, 2, QTableWidgetItem(str(y)))

    other_values = ['A', 'B', 'Y', 'Z']
    if latitude_band in other_values:
        z_text = f'{latitude_band}'
        table_widget.setItem(numRows, 3, QTableWidgetItem(z_text))
        ups_easting, ups_northing = ups_coords(self, latitude_band, point)
        table_widget.setItem(numRows, 4, QTableWidgetItem(ups_easting))
        table_widget.setItem(numRows, 5, QTableWidgetItem(ups_northing))
    else:
        z_text = f'{hemisphere} {zone}{latitude_band}'
        table_widget.setItem(numRows, 3, QTableWidgetItem(z_text))
        table_widget.setItem(numRows, 4, QTableWidgetItem(easting))
        table_widget.setItem(numRows, 5, QTableWidgetItem(northing))

    if event == QtCore.Qt.RightButton:
        rightclick_method()
        iface.actionPan().trigger()


def store_values_in_table_MA(self, point, event):
    """
    Store UTM coordinates of a clicked point in the Monument Area
    tableWidget and trigger the rightclickMA when done constructing the
    polygon.
    """

    store_values_in_table(
        self, point, event, self.tableWidget, lambda: rightclickMA(self))


def store_values_in_table_PA(self, point, event):
    """
    Store UTM coordinates of a clicked point in the Protected Area
    tableWidget and trigger the rightclickPA when done constructing the
    polygon.
    """

    store_values_in_table(
        self, point, event, self.tableWidget_1, lambda: rightclickPA(self))


def draw_area_on_map(
        self, table_widget, layer_name, line_edit_1, line_edit_2,
        store_values_in_table):
    """
    Prepare the canvas to draw polygons by connecting it to a map tool and
    set up event handlers for storing UTM values in the tableWidget.
    """

    # Get the number of rows in the tableWidget
    numRows = table_widget.rowCount()
    # empty the Table Widget
    if table_widget.rowCount() != 1:
        for row in range(1, numRows):
            table_widget.removeRow(1)
        delete_polygon(self, layer_name)
        line_edit_1.clear()
        line_edit_2.clear()
        table_widget.setItem(0, 1, QTableWidgetItem(''))
        table_widget.setItem(0, 2, QTableWidgetItem(''))

    self.hide()
    self.iface = iface
    # Store reference to the map canvas
    self.canvas = self.iface.mapCanvas()
    # Create the aps tool using the canvas reference
    self.polygon_tool = QgsMapToolEmitPoint(self.canvas)
    # connect signal that the canvas was clicked
    self.canvas.setMapTool(self.polygon_tool)
    self.polygon_tool.canvasClicked.connect(store_values_in_table)


def draw_area_on_map_MA(self):
    """Prepare the canvas to draw polygons for the Monument Area layer."""

    draw_area_on_map(
        self, self.tableWidget, 'Monument_Area', self.lineEdit_45,
        self.lineEdit_83,
        lambda point, event: store_values_in_table_MA(self, point, event))


def draw_area_on_map_PA(self):
    """Prepare the canvas to draw polygons for the Protected Area layer."""

    draw_area_on_map(
        self, self.tableWidget_1, 'Protected_Area', self.lineEdit_131,
        self.lineEdit_132,
        lambda point, event: store_values_in_table_PA(self, point, event))


def create_polygon(
        self, layer_name, table_widget, line_edit_ha, line_edit_sqm,
        line_edit_ha_2, push_button_1, push_button_2, push_button_3,
        push_button_4):
    """
    Create polygons for the polygon layers, using the UTM coordinates
    stored in the respective tableWidgets.
    """

    layer = QgsProject.instance().mapLayersByName(layer_name)[0]
    provider = layer.dataProvider()
    feature = QgsFeature()
    numRows = table_widget.rowCount()
    coords = []
    for row in range(1, numRows):
        hemisphere_zone_latband = table_widget.item(row, 3).text()
        hem = hemisphere_zone_latband[:2]
        hemisphere = 'north' if (hem == 'N ' or hem == 'Հս') else 'south'
        zone = int(hemisphere_zone_latband[-3:-1])
        easting = float(table_widget.item(row, 4).text())
        northing = float(table_widget.item(row, 5).text())
        utm_crs = (f'+proj=utm +zone={zone} +{hemisphere} +ellps=WGS84 '
                   '+datum=WGS84 +units=m +no_defs')
        transformer = pyproj.Transformer.from_crs(
            utm_crs, 'EPSG:3857', always_xy=True)
        x, y = transformer.transform(easting, northing)
        point = QgsPointXY(x, y)
        coords.append(point)
    polygon_geom = [coords]
    new_polygon = QgsGeometry.fromPolygonXY(polygon_geom)
    is_added, fid = is_polygon_already_added(self, layer_name, new_polygon)
    if is_added:
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        if self.label.text().startswith('Ամսաթիվ'):
            msg = (f'Համապատասխան միավորը գրանցված է N{fid} համարի ներքո։'
                   '\n\nԽնդրում ենք մուտքագրել նոր տվյալներ:')
        elif self.label.text() == 'Date:':
            msg = ('The corresponding unit is registered under number '
                   f'N{fid}.\n\nPlease enter new data.')
        elif self.label.text() == 'Fecha:':
            msg = ('La unidad correspondiente está registrada bajo el '
                   f'número N{fid}.\n\nPor favor introduzca datos nuevos.')
        msg_box.information(self, '', msg)
        clear_all_rows(
            self, table_widget, line_edit_ha, line_edit_sqm, '',
            push_button_1, push_button_2, push_button_3, push_button_4)
    else:
        feature.setGeometry(new_polygon)
        provider.addFeatures([feature])
        area_calc(
            self, layer_name, line_edit_ha, line_edit_sqm, line_edit_ha_2)
        layer.updateExtents()
        QgsProject.instance().reloadAllLayers()
        layer.startEditing()
        iface.actionAddFeature().trigger()
        layer.commitChanges()
        layer.updateFields()
        update_polygon_layer(self, layer_name)


def create_polygonMA(self):
    """
    Create polygons for the Monument Area, using the UTM coordinates stored
    in the tableWidget.
    """

    create_polygon(
        self, 'Monument_Area', self.tableWidget, self.lineEdit_45,
        self.lineEdit_83, self.lineEdit_131, self.pushButton_11,
        self.pushButton_12, self.pushButton_14, self.pushButton_13)


def create_polygonPA(self):
    """
    Create polygons for the Protected Area, using the UTM coordinates
    stored in the tableWidget.
    """

    create_polygon(
        self, 'Protected_Area', self.tableWidget_1, self.lineEdit_131,
        self.lineEdit_132, self.lineEdit_45, self.pushButton_18,
        self.pushButton_19, self.pushButton_21, self.pushButton_20)


def remove_selected_rows(
        self, table_widget, layer_name, button_1, button_2):
    """Remove selected row(s) from the tableWidget."""

    selected_rows = table_widget.selectionModel().selectedRows()
    if not selected_rows:
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        if self.label.text().startswith('Ամսաթիվ'):
            msg_box.information(
                self, 'Տեղեկություն',
                'Խնդրում ենք ընտրել ջնջվելիք մեկ կամ մի քանի տողերը:',
                QMessageBox.Yes | QMessageBox.No)
        elif self.label.text() == 'Date:':
            msg_box.information(
                self, 'Information',
                'Please select one or multiple rows to delete.',
                QMessageBox.Yes | QMessageBox.No)
        elif self.label.text() == 'Fecha:':
            msg_box.information(
                self, 'Información',
                'Seleccione una o varias filas para eliminar.',
                QMessageBox.Yes | QMessageBox.No)
    else:
        if self.label.text().startswith('Ամսաթիվ'):
            title = 'Հաստատում'
            msg = 'Վստա՞հ եք, որ ցանկանում եք ջնջել ընտրված տող(ները):'
        elif self.label.text() == 'Date:':
            title = 'Confirmation'
            msg = ('Are you sure that you want to delete the selected '
                   'row(s)?')
        elif self.label.text() == 'Fecha:':
            title = 'Confirmación'
            msg = ('¿Está seguro(a) de que desea eliminar la(s) fila(s) '
                   'seleccionada(s)?')
        buttonReply = QMessageBox.question(
            self, title, msg, QMessageBox.Yes | QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            row_indices = sorted(
                [row_index.row() for row_index in selected_rows], reverse=True
                )
            numRows = table_widget.rowCount()
            if row_indices[-1] == 0:
                msg_box = QMessageBox()
                msg_box.setIcon(QMessageBox.Information)
                if self.label.text().startswith('Ամսաթիվ'):
                    msg = ('Հենակետը հնարավոր չէ հեռացնել:\n\nԽնդրում ենք '
                           'ընտրել մեկ այլ տող:')
                elif self.label.text() == 'Date:':
                    msg = ('The point of reference cannot be removed.'
                           '\n\nPlease, select another row.')
                elif self.label.text() == 'Fecha:':
                    msg = ('No se puede eliminar el punto de referencia.'
                           '\n\nPor favor, seleccione otra fila.')
                msg_box.information(self, '', msg)
            else:
                # Calculate the number of rows left after removing the selected ones
                remaining_rows = numRows - len(row_indices)

                if remaining_rows >= 4:
                    # Remove the selected rows
                    for row in row_indices:
                        table_widget.removeRow(row)
                    delete_polygon(self, layer_name)
                    numbering(self, table_widget)
                    distance_calc(self, table_widget)
                    if layer_name == 'Monument_Area':
                        create_polygonMA(self)
                        area_calc(
                            self, layer_name, self.lineEdit_45,
                            self.lineEdit_83, self.lineEdit_131)
                    else:
                        create_polygonPA(self)
                        area_calc(
                            self, layer_name, self.lineEdit_131,
                            self.lineEdit_132, self.lineEdit_45)
                else:
                    # Display a message indicating that at least four rows should remain
                    msg_box = QMessageBox()
                    if self.label.text().startswith('Ամսաթիվ'):
                        msg_box.information(
                            self, 'Ուշադրություն',
                            'Գրանցման համար անհրաժեշտ է, որ աղյուսակը '
                            'պարունակի առնվազն 4 տող։')
                    elif self.label.text() == 'Date:':
                        msg_box.information(
                            self, 'Warning',
                            'The table must contain at least 4 rows for the '
                            'registration process to be successful.')
                    elif self.label.text() == 'Fecha:':
                        msg_box.information(
                            self, 'Atención',
                            'La tabla debe contener al menos 4 filas para que '
                            'el proceso de registro se realice correctamente.')
            # Enable or disable buttons based on the number of rows
            if numRows > 3:
                button_1.setEnabled(True)
                button_2.setEnabled(True)
            else:
                button_1.setDisabled(True)
                button_2.setDisabled(True)


def remove_selected_rows_MA(self):
    """Remove selected row(s) from the Monument Area tableWidget."""

    remove_selected_rows(
        self, self.tableWidget, 'Monument_Area', self.pushButton_14,
        self.pushButton_12)


def remove_selected_rows_PA(self):
    """Remove selected row(s) from the Protected Area tableWidget."""

    remove_selected_rows(
        self, self.tableWidget_1, 'Protected_Area', self.pushButton_21,
        self.pushButton_19)


def move_row_down(self, table_widget, layer_name):
    """Move the selected row down in the tableWidget."""

    row = table_widget.currentRow()
    column = table_widget.currentColumn()
    if row == 0:
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        if self.label.text().startswith('Ամսաթիվ'):
            msg_box.information(
                self, '', ('Հենակետը չի կարող տեղափոխվել:\n\nԽնդրում ենք '
                           'ընտրել մեկ այլ տող:'))
        elif self.label.text() == 'Date:':
            msg_box.information(
                self, '', ('The point of reference cannot be moved.\n\n'
                           'Please, select another row.'))
        elif self.label.text() == 'Fecha:':
            msg_box.information(
                self, '', ('El punto de referencia no se puede mover.\n\n'
                           'Por favor, seleccione otra fila.'))
    elif row < table_widget.rowCount() - 1:
        table_widget.insertRow(row + 2)
        for i in range(table_widget.columnCount()):
            table_widget.setItem(row + 2, i, table_widget.takeItem(row, i))
            table_widget.setCurrentCell(row + 2, column)
        table_widget.removeRow(row)
        delete_polygon(self, layer_name)
        numbering(self, table_widget)
        distance_calc(self, table_widget)
        if layer_name == 'Monument_Area':
            create_polygonMA(self)
        else:
            create_polygonPA(self)


def move_row_down_MA(self):
    """Move the selected row down in the Monument Area tableWidget."""

    move_row_down(self, self.tableWidget, 'Monument_Area')


def move_row_down_PA(self):
    """Move the selected row down in the Protected Area tableWidget."""

    move_row_down(self, self.tableWidget_1, 'Protected_Area')


def move_row_up(self, table_widget, layer_name):
    """Move the selected row up in the tableWidget."""

    row = table_widget.currentRow()
    column = table_widget.currentColumn()
    if row == 0 or row == 1:
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        if self.label.text().startswith('Ամսաթիվ'):
            msg_box.information(
                self, '', ('Հենակետը չի կարող տեղափոխվել:\n\nԽնդրում ենք '
                           'ընտրել մեկ այլ տող:'))
        elif self.label.text() == 'Date:':
            msg_box.information(
                self, '', ('The point of reference cannot be moved.\n\n'
                           'Please, select another row.'))
        elif self.label.text() == 'Fecha:':
            msg_box.information(
                self, '', ('El punto de referencia no se puede mover.\n\n'
                           'Por favor, seleccione otra fila.'))
    else:
        table_widget.insertRow(row - 1)
        for i in range(table_widget.columnCount()):
            table_widget.setItem(
                row - 1, i, table_widget.takeItem(row + 1, i))
            table_widget.setCurrentCell(row - 1, column)
        table_widget.removeRow(row + 1)
        delete_polygon(self, layer_name)
        numbering(self, table_widget)
        distance_calc(self, table_widget)
        if layer_name == 'Monument_Area':
            create_polygonMA(self)
        else:
            create_polygonPA(self)


def move_row_up_MA(self):
    """Move the selected row up in the Monument Area table."""

    move_row_up(self, self.tableWidget, 'Monument_Area')


def move_row_up_PA(self):
    """Move the selected row up in the Protected Area table."""

    move_row_up(self, self.tableWidget_1, 'Protected_Area')


def input_polygon_coords(self, add_point_func, finish_adding_points_func):
    """Prompt for coordinate input and handle finishing point addition."""

    add_point_func()
    msg_box = QMessageBox()
    if self.AddPointPoly.label.text().startswith('UTM գոտի'):
        title = 'Կետն ավելացված է։'
        text = 'Կցանկանայի՞ք ավելացնել ևս մեկ կետ:'
    elif self.AddPointPoly.label.text() == 'UTM Zone:':
        title = 'The point has been added.'
        text = 'Would you like to add another point?'
    elif self.AddPointPoly.label.text() == 'Zona UTM:':
        title = 'Se ha añadido el punto.'
        text = '¿Quiere añadir otro punto?'
    buttonReply = msg_box.question(self, title, text)
    if buttonReply == QMessageBox.Yes:
        self.AddPointPoly.clearAndFocus()
    elif buttonReply == QMessageBox.No:
        finish_adding_points_func()


def input_polygon_coordsMA(self):
    """
    Tab '5'. Section 5.1. Add a row.
    Handle coordinate input for the Monument Area table.
    """

    input_polygon_coords(
        self, lambda: add_point_2_tableMA(self), self.finish_adding_pointsMA)


def input_polygon_coordsPA(self):
    """
    Tab '5'. Section 5.2. Add a row.
    Handle coordinate input for the Protected Area table.
    """

    input_polygon_coords(
        self, lambda: add_point_2_tablePA(self), self.finish_adding_pointsPA)


def remove_tw_cont_and_last_value(self, layer_name):
    """
    Remove the contentes of the tableWidgets and the last added values of
    the layers.
    """

    point_value, polygon_value, last_point_feature, _, polygon_layer = \
        self.check_attribute_equality(layer_name)
    # Check if the attribute values are the same and
    # if the last_point_feature exists
    if (last_point_feature is not None and
            point_value is not None and
            polygon_value is not None):
        if point_value == polygon_value:
            delete_polygon(self, layer_name)


def resize_tablewidget_to_contents(self, table_widget):
    """Resize the columns of the tableWidget to fit the contents."""
    header = table_widget.horizontalHeader()
    for i in range(header.count()):
        header.setSectionResizeMode(i, QHeaderView.ResizeToContents)


def init_resize_tablewidgets_to_contents(self):
    """Initialize resizing tableWidgets to contents."""
    resize_tablewidget_to_contents(self, self.tableWidget)
    resize_tablewidget_to_contents(self, self.tableWidget_1)


def export_tablewidgets_2_excel(self):
    """
    Tab '5'.
    Export the data from tableWidgets to MS Excel.
    """

    filename, _ = QFileDialog.getSaveFileName(
        self, 'Save File', '', 'Excel (*.xls)')
    if filename:
        wbk = xlwt.Workbook()
        # workbook 1
        sheet1 = wbk.add_sheet('Monument area', cell_overwrite_ok=True)
        style = xlwt.XFStyle()
        font = xlwt.Font()
        font.bold = True
        style.font = font
        model1 = self.tableWidget.model()
        for c in range(model1.columnCount()):
            text = model1.headerData(c, QtCore.Qt.Horizontal)
            sheet1.write(0, c+1, text, style=style)
        for r in range(model1.rowCount()):
            text = model1.headerData(r, QtCore.Qt.Vertical)
            sheet1.write(r+1, 0, text, style=style)
        for c in range(model1.columnCount()):
            for r in range(model1.rowCount()):
                text = model1.data(model1.index(r, c))
                sheet1.write(r+1, c+1, text)
        # workbook 2
        sheet2 = wbk.add_sheet('Protected area', cell_overwrite_ok=True)
        model2 = self.tableWidget_1.model()
        for c in range(model2.columnCount()):
            text = model2.headerData(c, QtCore.Qt.Horizontal)
            sheet2.write(0, c+1, text, style=style)
        for r in range(model2.rowCount()):
            text = model2.headerData(r, QtCore.Qt.Vertical)
            sheet2.write(r+1, 0, text, style=style)
        for c in range(model2.columnCount()):
            for r in range(model2.rowCount()):
                text = model2.data(model2.index(r, c))
                sheet2.write(r+1, c+1, text)
        wbk.save(filename)
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        if self.label.text().startswith('Ամսաթիվ'):
            msg_box.information(
                self, '', 'Excel ֆայլը հաջողությամբ ստեղծվեց:')
        elif self.label.text() == 'Date:':
            msg_box.information(
                self, '', 'The Excel file was created successfully.')
        elif self.label.text() == 'Fecha:':
            msg_box.information(
                self, '', 'El archivo Excel se ha creado correctamente.')


def pivot_endge_text(self):
    """
    Tab '5'. Pivot edge (point of reference).
    Populate the textEdit with information on the Point of Reference.
    """

    point = self.canvas.getCoordinateTransform().toMapCoordinates(
        self.canvas.mouseLastXY())
    other_values = ['A', 'B', 'Y', 'Z']
    # when registering on the map with mouseclick
    if self.lineEdit_34.text() == '' or self.lineEdit_35.text() == '':
        zone, latitude_band, hemisphere, easting, northing = \
            get_utm_values(self, point)

        if (hemisphere == 'Հս' or hemisphere == 'N'):
            hem = self.radioButton_6.text()
        elif (hemisphere == 'Հվ' or hemisphere == 'S'):
            hem = self.radioButton_7.text()

        if latitude_band in other_values:
            easting, northing = ups_coords(self, latitude_band, point)
    # when registering manually
    else:
        zone = self.lineEdit_29.text()
        latitude_band = self.comboBox.currentText()
        if self.radioButton_6.isChecked() is True:
            hem = self.radioButton_6.text()
        elif self.radioButton_7.isChecked() is True:
            hem = self.radioButton_7.text()
        easting = self.lineEdit_34.text()
        northing = self.lineEdit_35.text()

    if self.label.text().startswith('Ամսաթիվ'):
        self.textEdit_21.setText(
            f'Որպես հենակետ ընտրվել է Ա կետը՝ {zone}{latitude_band} '
            f'{easting} {northing} ({hem} կիսագնդում): Այն գտնվում է...')
    elif self.label.text() == 'Date:':
        self.textEdit_21.setText(
            f'The point A with the coordinates {zone}{latitude_band} '
            f'{easting} {northing} ({hem} hemisphere), was chosen as a '
            'point of reference. It is located...')
    elif self.label.text() == 'Fecha:':
        self.textEdit_21.setText(
            f'Se ha elegido como punto de referencia el punto A con las '
            f'coordenadas {zone}{latitude_band} {easting} {northing} '
            f'(hemisferio {hem}). Está situado...')
