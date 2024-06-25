import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QFrame, QGridLayout, QCheckBox, QFileDialog
from qgis.core import QgsField, QgsEditorWidgetSetup
from PyQt5.QtCore import QVariant, QCoreApplication
from PyQt5.QtGui import QPixmap
import re


class Ui_Form(object):
    """A class for setting up the user interface."""

    image_count = 1  # Initialize counter for image labels
    new_frames = []  # Store references to newly created frames
    checkbox_widgets_ = []  # Store references to checkbox widgets

    def setupUi(self, Form):
        """Set up the user interface."""

        Form.setObjectName("Form")

        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setKerning(True)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 5, 1, 1, 3)

        self.pushButton_1 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setKerning(True)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")

        self.gridLayout.addWidget(self.pushButton_1, 2, 0, 1, 1)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setKerning(True)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 6, 1, 2, 1)

        self.checkBox = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")

        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(False)
        font.setKerning(True)
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight |
            QtCore.Qt.AlignmentFlag.AlignTrailing |
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")

        self.gridLayout.addWidget(self.label_2, 10, 0, 2, 1)

        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(True)
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight |
            QtCore.Qt.AlignmentFlag.AlignTrailing |
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")

        self.gridLayout.addWidget(self.label_7, 9, 0, 1, 1)

        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(True)
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight |
            QtCore.Qt.AlignmentFlag.AlignTrailing |
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.lineEdit_1 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_1.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setKerning(True)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setObjectName("lineEdit_1")

        self.gridLayout.addWidget(self.lineEdit_1, 4, 1, 1, 3)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setKerning(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 3, 0, 1, 1)

        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(True)
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight |
            QtCore.Qt.AlignmentFlag.AlignTrailing |
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")

        self.gridLayout.addWidget(self.label_5, 6, 0, 2, 1)

        self.textEdit_1 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_1.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setKerning(True)
        self.textEdit_1.setFont(font)
        self.textEdit_1.setObjectName("textEdit_1")

        self.gridLayout.addWidget(self.textEdit_1, 9, 1, 1, 3)

        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(True)
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight |
            QtCore.Qt.AlignmentFlag.AlignTrailing |
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.label_6 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setKerning(True)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(True)
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight |
            QtCore.Qt.AlignmentFlag.AlignTrailing |
            QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")

        self.gridLayout.addWidget(self.label_6, 6, 2, 2, 1)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setKerning(True)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 6, 3, 2, 1)

        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_5, 10, 1, 2, 3)

        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 8, 1, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.label_1 = QtWidgets.QLabel(self.frame)
        self.label_1.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")

        self.gridLayout.addWidget(self.label_1, 0, 1, 4, 3)

        self.label_8 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setAlignment(
            QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")

        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.checkBox, self.pushButton_1)
        Form.setTabOrder(self.pushButton_1, self.pushButton_2)
        Form.setTabOrder(self.pushButton_2, self.lineEdit_1)
        Form.setTabOrder(self.lineEdit_1, self.lineEdit_2)
        Form.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        Form.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        Form.setTabOrder(self.lineEdit_4, self.textEdit_1)

        self.pushButton_1.clicked.connect(
            lambda: ImageLoader_1.browseImage(self, self.label_1))
        self.pushButton_2.clicked.connect(
            lambda: ImageLoader_1.clearImage(self.label_1, self.lineEdit_5))

    def create_vl_17(self):
        """Create a vertical layout."""

        self.frame_4 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_4.setFrameStyle(QFrame.StyledPanel | QFrame.Raised)
        self.frame_4.setObjectName("frame_4")

        self.gridLayout_25 = QGridLayout(self.frame_4)
        self.gridLayout_25.setObjectName("gridLayout_25")

        self.gridLayout_40 = QGridLayout()
        self.gridLayout_40.setObjectName("gridLayout_40")

        self.gridLayout_25.addLayout(self.gridLayout_40, 0, 0, 1, 1)
        return self.frame_4

    def retranslateUi(self, Form):
        """Translate the user interface."""

        Form.setWindowTitle(self.translate("Form", "Form"))
        self.pushButton_1.setText(self.translate("Form", "Browse"))
        self.pushButton_2.setText(self.translate("Form", "Clear"))
        self.checkBox.setText(self.translate("Form", "Image_1"))
        self.label_3.setText(self.translate("Form", "Image caption:"))
        self.label_4.setText(self.translate("Form", "Credit:"))
        self.label_5.setText(self.translate("Form", "Date/Year taken:"))
        self.label_6.setText(self.translate("Form", "Place taken:"))
        self.label_8.setText(self.translate("Form", "Source:"))
        self.label_7.setText(self.translate("Form", "Comments:"))
        self.label_2.setAccessibleDescription(self.translate("Form", "0"))
        self.label_2.setText(self.translate("Form", "Image path:"))

    def translate(self, context, text):
        """Translate text."""

        return QCoreApplication.translate(context, text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


class ImageLoader_1(QWidget, Ui_Form):
    """A class for loading and managing images."""

    def __init__(self):
        """Initialize the ImageLoader_1 instance."""

        super().__init__()
        self.ui = Ui_Form()  # Instantiate Ui_Form
        self.ui.setupUi(self)  # Call setupUi on the instance

    def browseImage(self, label):
        """Browse for an image file and display it on the provided label."""

        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        global fnameim_

        ext = '(*.jpg *.jpeg *.png *.jfif *.tiff *.raw *.bmp)'

        fnameim_, _ = file_dialog.getOpenFileName(None, '', '.', ext)
        if fnameim_:
            label.setPixmap(QPixmap(fnameim_))
            label.setToolTip(fnameim_)
            # Find the layout of the frame containing the label
            frame_layout = label.parent().layout()
            if frame_layout:
                # Traverse through all child widgets of the frame and its descendants
                line_edit_5 = ImageLoader_1.find_lineEdit_5(frame_layout)
                if line_edit_5:
                    line_edit_5.setText(fnameim_)

    def clearImage(label, line_edit_5):
        """
        Clear the image displayed on the label and clear the associated line
        edit.
        """

        # Check if label is a QLabel object
        if isinstance(label, QtWidgets.QLabel):
            # Clear the pixmap of the label
            label.clear()

        # Check if lineEdit_5 is found
        if isinstance(line_edit_5, QtWidgets.QLineEdit):
            line_edit_5.clear()

    def remove_checked_layouts(self, label, verticalLayout):
        """Remove layouts containing checked checkboxes."""

        # Get the list of checkbox widgets before the loop
        checkbox_widgets = ImageLoader_1.get_checkbox_widget_list(verticalLayout)

        for i in reversed(range(verticalLayout.count())):
            frame = verticalLayout.itemAt(i).widget()
            if isinstance(frame, QFrame):
                checkbox = frame.findChild(QtWidgets.QCheckBox, 'checkBox')
                if checkbox:
                    if checkbox.isChecked():
                        match = re.search(r'\d+', checkbox.text())
                        if match:
                            checkbox_index = int(match.group())
                            if checkbox_index == 1:
                                ImageLoader_1.rem_lay(
                                    frame, checkbox, checkbox_widgets,
                                    verticalLayout, label, 1)
                                self.layout_duplicated = True
                            else:
                                ImageLoader_1.rem_lay(
                                    frame, checkbox, checkbox_widgets,
                                    verticalLayout, label, 1)
                                self.layout_duplicated = False

    def rem_lay(
            frame, checkbox, checkbox_widgets, verticalLayout, label, start):
        """Remove a layout along with its associated widgets."""

        # Remove the layout containing the checkbox
        layout = frame.layout()
        if layout:
            for j in reversed(range(layout.count())):
                item = layout.itemAt(j)
                if item and item.widget():
                    item.widget().deleteLater()
            layout.deleteLater()
        # Remove the checkbox widget from the list
        if checkbox in checkbox_widgets:
            checkbox_widgets.remove(checkbox)
        # Remove the frame
        frame.deleteLater()
        ImageLoader_1.update_checkbox_labels(
            label, verticalLayout, checkbox_widgets, start)

    def update_checkbox_labels(label, verticalLayout, checkbox_widgets, start):
        """Update the numbering of the labels of checkbox widgets."""

        # Iterate over checkbox widgets and update their labels
        for i, checkbox in enumerate(checkbox_widgets, start):
            if label.text().startswith('Ամսաթիվ'):
                checkbox.setText(f'Պատկեր_{i}')
            if label.text() == 'Date:':
                checkbox.setText(f'Image_{i}')
            if label.text() == 'Fecha:':
                checkbox.setText(f'Imagen_{i}')

    def create_widget_copy(self, original_widget, verticalLayout):
        """Create a copy of a widget."""

        if original_widget is None:
            return None

        if isinstance(original_widget, ImageLoader_1):
            # Create a new instance of ImageLoader_1
            new_widget = ImageLoader_1()
            return new_widget

        if new_widget:
            new_widget.setFont(original_widget.font())  # Copy font
            # Set object name to preserve it for finding later
            new_widget.setObjectName(original_widget.objectName())

        return new_widget

    def duplicate_layout(self, gridLayout, verticalLayout, label):
        """Duplicate a layout."""

        if gridLayout is None:
            return

        Ui_Form.image_count += 1

        new_frame_4 = QFrame()
        new_frame_4.setFrameStyle(QFrame.StyledPanel | QFrame.Raised)

        new_grid_layout_25 = QGridLayout(new_frame_4)
        new_grid_layout_40 = QGridLayout()

        # Iterate over the widgets in the original layout and create copies
        for i in range(gridLayout.count()):
            item = gridLayout.itemAt(i)
            widget = item.widget()
            if widget:
                new_widget = ImageLoader_1.create_widget_copy(
                    self, widget, verticalLayout)
                if new_widget:
                    row, column, rowspan, colspan = gridLayout.getItemPosition(i)
                    new_grid_layout_40.addWidget(
                        new_widget, row, column, rowspan, colspan)

        # Add the duplicated layout to the new frame
        new_grid_layout_25.addLayout(
            new_grid_layout_40, gridLayout.rowCount(), 0, 1, 1)

        # Disconnect the signal-slot connection for the browse button in the original layout
        browse_button = new_frame_4.findChild(
            QtWidgets.QPushButton, 'pushButton_1')
        if browse_button:
            browse_button.clicked.disconnect()  # Disconnect the old connection

        # Connect the browse button in the new layout to the browseImage method
        new_label = new_frame_4.findChild(QtWidgets.QLabel, 'label_1')
        if browse_button and new_label:
            browse_button.clicked.connect(
                lambda checked, label=new_label: ImageLoader_1.browseImage(
                    self, label))

        # Add the new frame to the main layout
        verticalLayout.addWidget(new_frame_4)
        # Get the list of checkbox widgets before the loop
        checkbox_widgets = ImageLoader_1.get_checkbox_widget_list(verticalLayout)
        # Update checkbox labels
        ImageLoader_1.update_checkbox_labels(
            label, verticalLayout, checkbox_widgets, 1)

    def create_fields(
            self, layer, checkbox_index, image_path, caption, credit,
            date_taken, place_taken, source, comments):
        """Create attribute fields and set attribute values."""

        # Construct attribute names based on the checkbox index
        attribute_names = [
            f'14.grdo_im_{checkbox_index}',
            f'14.grdo_cap_{checkbox_index}',
            f'14.grdo_credit_{checkbox_index}',
            f'14.grdo_datetkn_{checkbox_index}',
            f'14.grdo_pltkn_{checkbox_index}',
            f'14.grdo_source_{checkbox_index}',
            f'14.grdo_com_{checkbox_index}'
        ]
        # Check if attribute fields exist, if not, create them
        for attribute_name in attribute_names:
            if layer.fields().indexFromName(attribute_name) == -1:
                if attribute_name == f'14.grdo_im_{checkbox_index}':
                    layer.addAttribute(QgsField(
                        attribute_name, QVariant.String))
                    editor_widget_setup = QgsEditorWidgetSetup(
                        'ExternalResource',
                        {'FileWidget': True,
                         'DocumentViewer': 1,
                         'RelativeStorage': 0,
                         'StorageMode': 0,
                         'DocumentViewerHeight': 0,
                         'FileWidgetButton': True,
                         'DocumentViewerWidth': 800})
                    index = layer.fields().indexFromName(
                        f'14.grdo_im_{checkbox_index}')

                    layer.setEditorWidgetSetup(index, editor_widget_setup)
                else:
                    # Attribute field doesn't exist, create it
                    layer.addAttribute(
                        QgsField(attribute_name, QVariant.String))

        # Get the last feature in the attribute table
        last_feature = None
        for feature in layer.getFeatures():
            last_feature = feature

        # Set attribute values for the last feature
        for attribute_name in attribute_names:
            attribute_value = None
            if attribute_name.endswith(f'_im_{checkbox_index}'):
                attribute_value = image_path
            elif attribute_name.endswith(f'_cap_{checkbox_index}'):
                attribute_value = caption
            elif attribute_name.endswith(f'_credit_{checkbox_index}'):
                attribute_value = credit
            elif attribute_name.endswith(f'_datetkn_{checkbox_index}'):
                attribute_value = date_taken
            elif attribute_name.endswith(f'_pltkn_{checkbox_index}'):
                attribute_value = place_taken
            elif attribute_name.endswith(f'_source_{checkbox_index}'):
                attribute_value = source
            elif attribute_name.endswith(f'_com_{checkbox_index}'):
                attribute_value = comments

            last_feature.setAttribute(attribute_name, attribute_value)

        # Update the last feature in the attribute table
        layer.updateFeature(last_feature)

    def get_checkbox_widget_list(verticalLayout):
        """Get a list of checkbox widgets in a from all the layouts."""

        checkbox_widgets_ = []
        for i in range(verticalLayout.count()):
            frame = verticalLayout.itemAt(i).widget()
            if isinstance(frame, QFrame):
                checkbox = frame.findChild(QtWidgets.QCheckBox, 'checkBox')
                if isinstance(checkbox, QCheckBox):
                    checkbox_widgets_.append(checkbox)
        return checkbox_widgets_

    def find_lineEdit_1(layout):
        """Find a QLineEdit widget with object name 'lineEdit_1'."""

        line_edit_1 = layout.findChild(QtWidgets.QLineEdit, 'lineEdit_1')
        if line_edit_1:
            return line_edit_1

        # If lineEdit_1 is not found in the current layout, recursively search
        # in its child layouts
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if isinstance(item, QtWidgets.QWidgetItem):
                widget = item.widget()
                if (widget and
                        isinstance(widget, QtWidgets.QLineEdit) and
                        widget.objectName() == 'lineEdit_1'):
                    return widget
            elif isinstance(item, QtWidgets.QLayout):
                line_edit_1 = ImageLoader_1.find_lineEdit_1(item)
                if line_edit_1:
                    return line_edit_1

        return None

    def find_lineEdit_2(layout):
        """Find a QLineEdit widget with object name 'lineEdit_2'."""

        line_edit_2 = layout.findChild(QtWidgets.QLineEdit, 'lineEdit_2')
        if line_edit_2:
            return line_edit_2

        # If lineEdit_2 is not found in the current layout, recursively search
        # in its child layouts
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if isinstance(item, QtWidgets.QWidgetItem):
                widget = item.widget()
                if (widget and
                        isinstance(widget, QtWidgets.QLineEdit) and
                        widget.objectName() == 'lineEdit_2'):
                    return widget
            elif isinstance(item, QtWidgets.QLayout):
                line_edit_2 = ImageLoader_1.find_lineEdit_2(item)
                if line_edit_2:
                    return line_edit_2
        return None

    def find_lineEdit_3(layout):
        """Find a QLineEdit widget with object name 'lineEdit_3'."""

        line_edit_3 = layout.findChild(QtWidgets.QLineEdit, 'lineEdit_3')
        if line_edit_3:
            return line_edit_3

        # If lineEdit_3 is not found in the current layout, recursively search
        # in its child layouts
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if isinstance(item, QtWidgets.QWidgetItem):
                widget = item.widget()
                if (widget and
                        isinstance(widget, QtWidgets.QLineEdit) and
                        widget.objectName() == 'lineEdit_3'):
                    return widget
            elif isinstance(item, QtWidgets.QLayout):
                line_edit_3 = ImageLoader_1.find_lineEdit_3(item)
                if line_edit_3:
                    return line_edit_3
        return None

    def find_lineEdit_4(layout):
        """Find a QLineEdit widget with object name 'lineEdit_4'."""

        line_edit_4 = layout.findChild(QtWidgets.QLineEdit, 'lineEdit_4')
        if line_edit_4:
            return line_edit_4

        # If lineEdit_4 is not found in the current layout, recursively search
        # in its child layouts
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if isinstance(item, QtWidgets.QWidgetItem):
                widget = item.widget()
                if (widget and
                        isinstance(widget, QtWidgets.QLineEdit) and
                        widget.objectName() == 'lineEdit_4'):
                    return widget
            elif isinstance(item, QtWidgets.QLayout):
                line_edit_4 = ImageLoader_1.find_lineEdit_4(item)
                if line_edit_4:
                    return line_edit_4

        return None

    def find_lineEdit_5(layout):
        """Find a QLineEdit widget with object name 'lineEdit_5'."""

        line_edit_5 = layout.findChild(QtWidgets.QLineEdit, 'lineEdit_5')
        if line_edit_5:
            return line_edit_5
        # If lineEdit_5 is not found in the current layout, recursively search
        # in its child layouts
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if isinstance(item, QtWidgets.QLayoutItem):
                widget = item.widget()
                if widget:
                    if (isinstance(widget, QtWidgets.QLineEdit) and
                            widget.objectName() == 'lineEdit_5'):
                        return widget
                else:
                    sub_layout = item.layout()
                    if sub_layout:
                        line_edit_5 = ImageLoader_1.find_lineEdit_5(sub_layout)
                        if line_edit_5:
                            return line_edit_5
        return None

    def find_lineEdit_6(layout):
        """Find a QLineEdit widget with object name 'lineEdit_6'."""

        line_edit_6 = layout.findChild(QtWidgets.QLineEdit, 'lineEdit_6')
        if line_edit_6:
            return line_edit_6
        # If lineEdit_5 is not found in the current layout, recursively search
        # in its child layouts
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if isinstance(item, QtWidgets.QLayoutItem):
                widget = item.widget()
                if widget:
                    if (isinstance(widget, QtWidgets.QLineEdit) and
                            widget.objectName() == 'lineEdit_6'):
                        return widget
                else:
                    sub_layout = item.layout()
                    if sub_layout:
                        line_edit_6 = ImageLoader_1.find_lineEdit_6(sub_layout)
                        if line_edit_6:
                            return line_edit_6
        return None

    def find_textEdit_1(layout):
        """Find a QTextEdit widget with object name 'textEdit_1'."""

        text_edit_1 = layout.findChild(QtWidgets.QTextEdit, 'textEdit_1')
        if text_edit_1:
            return text_edit_1

        # If textEdit_1 is not found in the current layout, search in its child layouts
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if isinstance(item, QtWidgets.QWidgetItem):
                widget = item.widget()
                if (widget and
                        isinstance(widget, QtWidgets.QTextEdit) and
                        widget.objectName() == 'textEdit_1'):
                    return widget
            elif isinstance(item, QtWidgets.QLayout):
                text_edit_1 = ImageLoader_1.find_textEdit_1(item)
                if text_edit_1:
                    return text_edit_1
        return None
