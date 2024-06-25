from qgis.PyQt import uic
import os
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp
from .point_and_polygons import (
    distance_calc, add_point_2_tableMA, add_point_2_tablePA, numbering)

# Load the .ui file
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), '..', 'UI', 'AddPointPoly.ui'))


class AddPointPoly(QDialog, FORM_CLASS):
    def __init__(self, table_widget, layer_name, main_instance):
        """Initialise the AddPointPoly dialog."""

        super().__init__()

        self.setupUi(self)  # Set up the user interface from Designer
        self.setModal(True)  # Make the dialog modal

        # Store
        self.table_widget = table_widget
        self.layer_name = layer_name
        self.main_instance = main_instance

        # Connect the accepted and rejected signals of the button box to slots
        # Only allows inputing numbers and '.' characters
        self.lineEdit.setValidator(
            QRegExpValidator(QRegExp('([1-9]|[1-5][0-9]|60)')))
        # Only allows inputing numbers and . characters
        self.lineEdit_2.setValidator(
            QRegExpValidator(QRegExp('[0-9]+\\.?[0-9]*')))
        # Only allows inputing numbers and . characters
        self.lineEdit_3.setValidator(
            QRegExpValidator(QRegExp('[0-9]+\\.?[0-9]*')))

        self.pushButton.clicked.connect(self.AddRow)
        self.pushButton_2.clicked.connect(self.clearAndFocus)
        self.pushButton_3.clicked.connect(self.finish_adding_points)
        self.pushButton_4.clicked.connect(self.close)

    def AddRow(self):
        """Add a row to the tableWidget based on the layer name."""

        if self.layer_name == 'Monument_Area':
            self.main_instance.addrowMA()
        elif self.layer_name == 'Protected_Area':
            self.main_instance.addrowPA()

    def clearAndFocus(self):
        """
        Clear all data in the dialog and set focus to the first input field.
        """

        # Clear all data in the dialog
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.comboBox.setCurrentIndex(0)
        # Set focus to the first input field
        self.lineEdit.setFocus()

    def finish_adding_points(self):
        """
        Add a final row to the tableWidget based on the layer name, call the
        appropriate method to finish adding points and then set the map tool.
        """

        main = self.main_instance
        if not (self.lineEdit.text() and
                self.comboBox.currentIndex() != 0 and
                self.lineEdit_2.text() and
                self.lineEdit_3.text() and
                (self.radioButton.isChecked() or
                self.radioButton_2.isChecked())):
            if self.layer_name == 'Monument_Area':
                add_row_result = main.add_row(
                    main.tableWidget, None)
                if add_row_result is True:
                    main.finish_adding_pointsMA()
            elif self.layer_name == 'Protected_Area':
                add_row_result = main.add_row(
                    main.tableWidget_1, None)
                if add_row_result is True:
                    main.finish_adding_pointsPA()
        else:
            if self.layer_name == 'Monument_Area':
                num_rows = main.tableWidget.rowCount()
                main.tableWidget.insertRow(num_rows)
                add_point_2_tableMA(main)
                numbering(main, main.tableWidget)
                distance_calc(main, main.tableWidget)
                main.finish_adding_pointsMA()
            elif self.layer_name == 'Protected_Area':
                num_rows = main.tableWidget_1.rowCount()
                main.tableWidget_1.insertRow(num_rows)
                add_point_2_tablePA(main)
                numbering(main, main.tableWidget_1)
                distance_calc(main, main.tableWidget_1)
                main.finish_adding_pointsPA()
        main.pantool()

    def notext(self):
        """
        Display an information message box indicating missing coordinate
        details.
        """

        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        if self.label.text().startswith('UTM գոտի'):
            msg_box.information(
                self,
                'Բացակայում են կոորդինատների մանրամասները',
                ('Կորդինատի մանրամասները բացակայում են։\n\nԽնդրում ենք '
                 'մուտքագրել կոորդինատների բացակայող տվյալները։'))
        elif self.label.text() == 'UTM Zone:':
            msg_box.information(
                self,
                'Missing coordinate details',
                ('Coordinate details are missing.\n\nPlease, input the '
                 'missing data on coordinates.'))
        elif self.label.text() == 'Zona UTM:':
            msg_box.information(
                self,
                'Faltan datos de coordenadas',
                ('Faltan datos de coordenadas.\n\nPor favor, introduzca los '
                 'datos de coordenadas que faltan.'))

    def closeEvent(self, event):
        """Accept the close event for the dialog."""

        event.accept()
