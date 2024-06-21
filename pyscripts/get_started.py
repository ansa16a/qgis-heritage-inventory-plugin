from PyQt5.QtWidgets import QMessageBox
from qgis.gui import QgsProjectionSelectionDialog
from qgis.core import QgsProject, QgsCoordinateReferenceSystem


def getStarted_step1(label, lineEdit_27, lineEdit_28):
    """
    Display a message box for Step 1 of 6 of the inventory process.
    Prompt the user to ensure the base map is present in the project.
    """

    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    btn_Ok = msg_box.button(QMessageBox.Ok)
    btn_Cancel = msg_box.button(QMessageBox.Cancel)
    if label.text().startswith('Ամսաթիվ'):
        msg_box.setWindowTitle('Քայլ 1 6-ից. Բազային քարտեզ')
        message = '<p align="justify">'\
                  'Նախքան գույքագրման գործընթացը սկսելը, խնդրում ենք համոզվել'\
                  ', որ հիմնական (բազային) քարտեզը առկա է նախագծում: Վերջինս '\
                  'անհրաժեշտ է ծրագրի տարրերը և քարտեզները միևնույն '\
                  'Կոորդինատների Տեղեկատվության Համակարգում (CRS) գրանցելու '\
                  'համար:</p>'\
                  '<ul><li>Եթե հիմնական քարտեզն ընտրված չէ, խնդրում ենք՝</li>'\
                  '<ol><li>փակել հավելվածը,</li>'\
                  '<li>ընտրել բազային քարտեզը, և</li>'\
                  '<li>վերագործարկել հավելվածը:</li></ol>'\
                  '<li>Եթե հիմնական քարտեզն ընտրված է, և ցանկանում եք անցնել '\
                  'հաջորդ քայլին, խնդրում ենք սեղմել '\
                  '<b><em>Քայլ 2</b></em> կոճակին։</li></ul>'
        btn_Ok.setText('Քայլ 2')
        btn_Cancel.setText('Փակել')
    elif label.text() == 'Date:':
        msg_box.setWindowTitle('Step 1 of 6: Base map')
        message = '<p align="justify">Before starting the inventory process, '\
                  'please ensure the base map is present in the project. '\
                  'This is needed in order for the project elements and the '\
                  'maps to be set in the same Coordinate Reference System '\
                  '(CRS).</p>'\
                  '<ul><li>If the base map is not selected, please:</li>'\
                  '<ol><li>Close the plugin,</li>'\
                  '<li>choose a base map, and </li>'\
                  '<li>restart the plugin.</li></ol>'\
                  '<li>If the base map is selected, and you want to proceed '\
                  'to the next step, please click <b><em>Step 2</b></em>.'\
                  '</li></ul>'
        btn_Ok.setText('Step 2')
        btn_Cancel.setText('Close')
    elif label.text() == 'Fecha:':
        msg_box.setWindowTitle('Paso 1 de 6: Mapa base')
        message = '<p align="justify">'\
                  'Antes de iniciar el proceso de inventario, asegúrese de '\
                  'que el mapa base está presente en el proyecto. Esto es '\
                  'necesario para que los elementos del proyecto y los mapas '\
                  'se establezcan en el mismo Sistema de Referencia de '\
                  'Coordenadas (SRC).</p>'\
                  '<ul><li>Si el mapa base no está seleccionado, por favor:'\
                  '</li><ol><li>Cierre el plugin,</li>'\
                  '<li>elija un mapa base, y </li>'\
                  '<li>reinicie el plugin.</li></ol>'\
                  '<li>Si el mapa base está seleccionado y desea continuar '\
                  'con el siguiente paso, haga clic en <b><em>Paso 2</b></em>.'\
                  '</li></ul>'
        btn_Ok.setText('Paso 2')
        btn_Cancel.setText('Cerrar')
    msg_box.setText(message)
    msg_box.setDefaultButton(btn_Ok)
    msg_box.exec_()
    if msg_box.clickedButton() == btn_Ok:
        getStarted_step2(label, lineEdit_27, lineEdit_28)


def getStarted_step2(label, lineEdit_27, lineEdit_28):
    """
    Display a message box for Step 2 of 6 of the inventory process.
    Prompt the user to select the Coordinate Reference System for the project.
    """

    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setStandardButtons(
        QMessageBox.Ok | QMessageBox.Open | QMessageBox.Save | QMessageBox.Cancel)
    btn_Ok = msg_box.button(QMessageBox.Ok)
    btn_Open = msg_box.button(QMessageBox.Open)
    btn_Save = msg_box.button(QMessageBox.Save)
    btn_Cancel = msg_box.button(QMessageBox.Cancel)
    if label.text().startswith('Ամսաթիվ'):
        msg_box.setWindowTitle('Քայլ 2 6-ից. Ընտրել CRS-ը')
        message = ('Խնդրում ենք ընտրել CRS-ը:\nԽորհուրդ է տրվում ընտրել Web '
                   'Marcator պրոյեկցիան EPSG:3857:')
        btn_Ok.setText('Ընտրել CRS')
        btn_Save.setText('Քայլ 1')
        btn_Open.setText('Քայլ 3')
        btn_Cancel.setText('Փակել')
    elif label.text() == 'Date:':
        msg_box.setWindowTitle('Step 2 of 6: Select CRS')
        message = ('Please select the CRS.\nIt is recommended to choose Web '
                   'Marcator projection EPSG:3857.')
        btn_Ok.setText('Select CRS')
        btn_Save.setText('Step 1')
        btn_Open.setText('Step 3')
        btn_Cancel.setText('Close')
    elif label.text() == 'Fecha:':
        msg_box.setWindowTitle('Paso 2 de 6: Seleccionar SRC')
        message = ('Por favor, seleccione el SRC.\nSe recomienda elegir la '
                   'proyección Web Marcator EPSG:3857.')
        btn_Ok.setText('Seleccionar SRC')
        btn_Save.setText('Paso 1')
        btn_Open.setText('Paso 3')
        btn_Cancel.setText('Cerrar')
    msg_box.setText(message)
    msg_box.setDefaultButton(btn_Ok)
    msg_box.exec_()
    if msg_box.clickedButton() == btn_Ok:
        crs_selection(lineEdit_27, lineEdit_28)
    elif msg_box.clickedButton() == btn_Save:
        getStarted_step1(label, lineEdit_27, lineEdit_28)
    elif msg_box.clickedButton() == btn_Open:
        getStarted_step3(label, lineEdit_27, lineEdit_28)


def crs_selection(lineEdit_27, lineEdit_28):
    """
    Open the QgsProjectionSelectionDialog for selecting CRS/authority ID.
    Update the lineEdit_27 and lineEdit_28 widgets with the selected CRS
    description and authority ID respectively, and call change_crs function.
    """

    dialog = QgsProjectionSelectionDialog()
    dialog.exec_()
    target_crs = dialog.crs()
    lineEdit_27.setText(target_crs.description())
    lineEdit_28.setText(target_crs.authid())
    change_crs(target_crs)


def change_crs(target_crs):
    """
    Change the CRS for all layers in the current project to the specified
    target CRS.
    """

    # Get all layers
    layers = QgsProject.instance().mapLayers().values()
    # poly_layer1 = QgsProject.instance().mapLayersByName('Monument_Area')[0]
    # poly_layer2 = QgsProject.instance().mapLayersByName('Protected_Area')[0]
    # point_layer = QgsProject.instance().mapLayersByName('Representative_Point')[0]

    # Change CRS for each layer
    for layer in layers:
        change_layer_crs(layer, target_crs)
    # self.change_layer_crs(poly_layer1, target_crs)
    # self.change_layer_crs(poly_layer2, target_crs)
    # self.change_layer_crs(point_layer, target_crs)


def change_layer_crs(layer, target_crs):
    """Change the CRS for a specific layer to the specified target CRS."""

    if layer:
        layer.setCrs(QgsCoordinateReferenceSystem(target_crs))
        layer.triggerRepaint()  # Refresh the layer display
    QgsProject.instance().setCrs(QgsCoordinateReferenceSystem(target_crs))


def getStarted_step3(label, lineEdit_27, lineEdit_28):
    """
    Display a message box for Step 3 of 6 of the inventory process, which
    involves creating a new project.
    """

    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setStandardButtons(
        QMessageBox.Ok | QMessageBox.Open | QMessageBox.Cancel)
    btn_Ok = msg_box.button(QMessageBox.Ok)
    btn_Open = msg_box.button(QMessageBox.Open)
    btn_Cancel = msg_box.button(QMessageBox.Cancel)
    if label.text().startswith('Ամսաթիվ'):
        msg_box.setWindowTitle('Քայլ 3 6-ից. Նոր նախագծի ստեղծում')
        message = '<p align = "justify">'\
                  'Նոր նախագիծ ստեղծելու համար անցեք <b><em>Գլխավոր &gt; Նոր '\
                  'նախագիծ</em></b> (կամ օգտագործեք Ctrl+Shift+N):</p>'\
                  '<p align = "justify">'\
                  'Ընտրեք թղթապանակ՝ ձեր նախագծի ֆայլերը պահելու համար: '\
                  'Ծրագիրը ձեզ համար կստեղծի երկու թղթապանակ և հետևյալ երեք '\
                  'գեոփաթեթները.'\
                  '<ol><li> Կետային շերտ՝ հենակետի '\
                  'կոորդինատները պահելու համար:</li>'\
                  '<li>Բազմանկյուն շերտ՝ '\
                  'հուշարձանների տարածքը գրանցելու համար:</li>'\
                  '<li>Բազմանկյուն շերտ՝ պահպանական գոտու տարածքները '\
                  'գրանցելու համար:</li></ol>'\
                  '<p align = "justify">'\
                  'Գոեփաթեթներում կհավաքագրվեն մուտքագրված տվյալները: '\
                  'Թղթապանակներից մեկը կպահի նախագծում օգտագործված բոլոր '\
                  'պատկերների պատճենները, իսկ մյուսը կպահի բոլոր լրացուցիչ '\
                  'կցված նյութերը (եթե այդպիսիք լինեն):</p>'
        btn_Ok.setText('Քայլ 2')
        btn_Open.setText('Քայլ 4')
        btn_Cancel.setText('Փակել')
    elif label.text() == 'Date:':
        msg_box.setWindowTitle('Step 3 of 6: Creating a New Project')
        message = '<p align = "justify">'\
                  'To create a new project, go to <b><em>File &gt; New '\
                  'Project</em></b> (or use Ctrl+Shift+N).</p>'\
                  '<p align = "justify">'\
                  'Choose a folder to store your project files. The program '\
                  'will create for you two folders and the following three '\
                  'geopackages:'\
                  '<ol><li>A point layer for storing the points of reference.</li>'\
                  '<li>A polygon layer for recording monument areas.</li>'\
                  '<li>Another polygon layer for registering protected areas.</li></ol>'\
                  '<p align = "justify">'\
                  'Geopackages will store data input in the plugin. One of '\
                  'the folders will store the copies of all the images used '\
                  'in the project, while the other one will store all the '\
                  'additional attachments (if any).</p>'
        btn_Ok.setText('Step 2')
        btn_Open.setText('Step 4')
        btn_Cancel.setText('Close')
    elif label.text() == 'Fecha:':
        msg_box.setWindowTitle('Paso 3 de 6: Creación de un Nuevo Proyecto')
        message = '<p align = "justify">'\
                  'Para iniciar un nuevo proyecto, ve a <b><em>Archivo &gt; '\
                  'Nuevo Proyecto</em></b> (o utiliza Ctrl+Mayús+N).</p>'\
                  '<p align = "justify">'\
                  'Elija una carpeta para almacenar los archivos del proyecto'\
                  '. El programa creará dos carpetas y los tres siguientes '\
                  'geopaquetes:'\
                  '<ol><li>Una capa de puntos para almacenar los '\
                  'puntos de referencia.</li>'\
                  '<li>Una capa de polígonos para registrar las zonas '\
                  'monumentales.</li>'\
                  '<li>Otra capa de polígonos para registrar zonas protegidas.</li></ol>'\
                  '<p align = "justify">'\
                  'Los geopaquetes almacenarán los datosintroducidos en el '\
                  'plugin. Una de las carpetas almacenará las copias de '\
                  'todas las imágenes utilizadas en el proyecto, mientras '\
                  'que la otra almacenará todos los archivos adjuntos '\
                  'adicionales (en su caso).</p>'
        btn_Ok.setText('Paso 2')
        btn_Open.setText('Paso 4')
        btn_Cancel.setText('Cerrar')
    msg_box.setText(message)
    msg_box.setDefaultButton(btn_Open)
    msg_box.exec_()
    if msg_box.clickedButton() == btn_Ok:
        getStarted_step2(label, lineEdit_27, lineEdit_28)
    elif msg_box.clickedButton() == btn_Open:
        getStarted_step4(label, lineEdit_27, lineEdit_28)


def getStarted_step4(label, lineEdit_27, lineEdit_28):
    """
    Display a message box for Step 4 of 6 of the the inventory process, which
    involves creating a new worksheet.
    """

    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setStandardButtons(
        QMessageBox.Ok | QMessageBox.Open | QMessageBox.Cancel)
    btn_Ok = msg_box.button(QMessageBox.Ok)
    btn_Open = msg_box.button(QMessageBox.Open)
    btn_Cancel = msg_box.button(QMessageBox.Cancel)
    if label.text().startswith('Ամսաթիվ'):
        msg_box.setWindowTitle('Քայլ 4 6-ից. Նոր աշխատաթերթ')
        message = '<p align = "justify">'\
                  'Նոր ժառանգության օբյեկտ գրանցելու համար անցեք <b><em>'\
                  'Գլխավոր &gt; Նոր աշխատաթերթ</em> </b>(կամ օգտագործեք '\
                  'Ctrl+N):</p>'\
                  '<p align = "justify">'\
                  'Ընտրեք թղթապանակը, որտեղ կստեղծվեն նախագծի ֆայլերը:</p>'
        btn_Ok.setText('Քայլ 3')
        btn_Open.setText('Քայլ 5')
        btn_Cancel.setText('Փակել')
    elif label.text() == 'Date:':
        msg_box.setWindowTitle('Step 4 of 6: New Worksheet')
        message = '<p align = "justify">'\
                  'To register a new heritage object go to <b><em>File &gt; '\
                  'New Worksheet</em> </b>(or use Ctrl+N).</p>'\
                  '<p align = "justify">'\
                  'You will be prompted to select a folder where the project '\
                  'files will be created.</p>'
        btn_Ok.setText('Step 3')
        btn_Open.setText('Step 5')
        btn_Cancel.setText('Close')
    elif label.text() == 'Fecha:':
        msg_box.setWindowTitle('Paso 4 de 6: Nueva Ficha')
        message = '<p align = "justify">'\
                  'Para registrar un nuevo objeto patrimonial vaya a <b><em>'\
                  'Archivo &gt; Nueva Ficha</em> </b>(o utilice Ctrl+N).</p>'\
                  '<p align = "justify">'\
                  'Se le pedirá que seleccione una carpeta donde se crearán '\
                  'los archivos del proyecto.</p>'
        btn_Ok.setText('Paso 3')
        btn_Open.setText('Paso 5')
        btn_Cancel.setText('Cerrar')
    msg_box.setText(message)
    msg_box.setDefaultButton(btn_Open)
    msg_box.exec_()
    if msg_box.clickedButton() == btn_Ok:
        getStarted_step3(label, lineEdit_27, lineEdit_28)
    elif msg_box.clickedButton() == btn_Open:
        getStarted_step5(label, lineEdit_27, lineEdit_28)


def getStarted_step5(label, lineEdit_27, lineEdit_28):
    """
    Display a message box for Step 5 of 6 of the inventory process, which
    involves filling out the worksheet.
    """

    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setStandardButtons(
        QMessageBox.Ok | QMessageBox.Open | QMessageBox.Cancel)
    btn_Ok = msg_box.button(QMessageBox.Ok)
    btn_Open = msg_box.button(QMessageBox.Open)
    btn_Cancel = msg_box.button(QMessageBox.Cancel)
    if label.text().startswith('Ամսաթիվ'):
        msg_box.setWindowTitle('Քայլ 5 6-ից. Լրացնել աշխատաթերթը')
        message = '<p align = "justify">'\
                  'Աշխատաթերթն ընդհանուր առմամբ բաղկացած է 14 բաժիններից:</p>'\
                  '<p align = "justify">'\
                  'Խնդրում ենք նկատի ունենալ, որ աշխատանքային թերթի '\
                  'տեղեկատվության որոշ մասի լրացումը պարտադիր է, և որոշ '\
                  'բաժիններ կամ կոճակներ կարող են անջատված լինել: Դրանք '\
                  'միացնելու համար համոզվեք, որ լրացրել եք բոլոր անհրաժեշտ '\
                  'տեղեկությունները:</p>'
        btn_Ok.setText('Քայլ 4')
        btn_Open.setText('Քայլ 6')
        btn_Cancel.setText('Փակել')
    elif label.text() == 'Date:':
        msg_box.setWindowTitle('Step 5 of 6: Fill out the worksheet')
        message = '<p align = "justify">'\
                  'The worksheet consists of a total of 14 sections.</p>'\
                  '<p align = "justify">'\
                  'Please note that most of the information in the worksheet '\
                  'is mandatory, and some sections may appear disabled. To '\
                  'enable these sections, ensure that you have completed all '\
                  'the required information.</p>'
        btn_Ok.setText('Step 4')
        btn_Open.setText('Step 6')
        btn_Cancel.setText('Close')
    elif label.text() == 'Fecha:':
        msg_box.setWindowTitle('Paso 5 de 6: Rellenar la Ficha')
        message = '<p align = "justify">'\
                  'La hoja de trabajo consta de un total de 14 secciones.</p>'\
                  '<p align = "justify">'\
                  'Tenga en cuenta que la mayor parte de la información de '\
                  'la ficha es obligatoria y que algunas secciones pueden '\
                  'aparecer deshabilitadas. Para habilitar estas secciones, '\
                  'asegúrese de haber completado toda la información '\
                  'requerida.</p>'
        btn_Ok.setText('Paso 4')
        btn_Open.setText('Paso 6')
        btn_Cancel.setText('Cerrar')
    msg_box.setText(message)
    msg_box.setDefaultButton(btn_Open)
    msg_box.exec_()
    if msg_box.clickedButton() == btn_Ok:
        getStarted_step4(label, lineEdit_27, lineEdit_28)
    elif msg_box.clickedButton() == btn_Open:
        getStarted_step6(label, lineEdit_27, lineEdit_28)


def getStarted_step6(label, lineEdit_27, lineEdit_28):
    """
    Display a message box for the final Step of the inventory process, which
    involves registering and saving the project.
    """
    # Step 6 of 6: Register and save
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    btn_Ok = msg_box.button(QMessageBox.Ok)
    btn_Cancel = msg_box.button(QMessageBox.Cancel)
    if label.text().startswith('Ամսաթիվ'):
        msg_box.setWindowTitle('Քայլ 6 6-ից. Գրանցել և պահպանել')
        message = '<p align = "justify">'\
                  'Նոր աշխատաթերթի լրացման սկզբում '\
                  'գրանցման կոճակն անջատված է:</p>'\
                  '<p align = "justify">'\
                  'Այն միացնելու համար համոզվեք, որ քարտեզի վրա գրանցել եք '\
                  'առնվազն հղման կետը:</p>'\
                  '<p align = "justify">'\
                  'Երբ ավարտեք 5-րդ քայլը՝ աշխատաթերթի լրացումը, խնդրում ենք '\
                  'սեղմել <b>''<em>Գրանցել</em></b> կոճակը և սպասել, մինչև '\
                  'ծրագիրը գրանցի բոլոր տվյալները:</p>'\
                  '<p align = "justify">'\
                  'Գրանցման ավարտից հետո ծրագիրը կառաջարկի պահպանել նախագիծը '\
                  'որպես *.qgs կամ *.qgz ֆայլ ապագայում այն որպես հիմնական '\
                  'ֆայլ օգտագործելու համար, ինչպես նաև կարտահանի Հուշարձանի '\
                  'տարածքի և Պահպանական գոտու կոորդինատները որպես *.xls MS '\
                  'Excel ֆայլ:</p>'\
                  '<p align = "justify">'\
                  'Դուք կարող եք պահպանել նախագիծը՝ անցնելով <b><em>'\
                  'Գլխավոր&gt; Պահպանել նախագիծը</em> </b>(կամ օգտագործել '\
                  'Ctrl+S):</p>'\
                  '<p align = "justify">'\
                  'Ձեր նախագիծն այժմ գրանցված է։</p>'
        btn_Ok.setText('Քայլ 5')
        btn_Cancel.setText('Փակել')
    elif label.text() == 'Date:':
        msg_box.setWindowTitle('Step 6 of 6: Register and save')
        message = '<p align = "justify">'\
                  'By default, the <b><em>Register</em></b> button is '\
                  'disabled.</p>'\
                  '<p align = "justify">'\
                  'To enable it, make sure you have drawn at least the Point '\
                  'of Reference.</p>'\
                  '<p align = "justify">'\
                  'Once you complete the Step 5 and finish filling out the '\
                  'Worksheet, click the <b><em>Register</em> </b> button and '\
                  'wait until the program registers all the data correctly.'\
                  '</p><p align = "justify">'\
                  'After registration is complete, the program will prompt '\
                  'you to save the project as either a *.qgs or *.qgz file '\
                  'for future access, and will also export the coordinates '\
                  'of the Monument and Protected Area to an *.xls MS Excel '\
                  'file.</p>'\
                  '<p align = "justify">'\
                  'You can save the project by going to <b><em>File &gt; '\
                  'Save Project</em> </b>(or use Ctrl+S). </p>'\
                  '<p align = "justify">'\
                  'Your project is now registered and saved for your '\
                  'convenience.</p>'
        btn_Ok.setText('Step 5')
        btn_Cancel.setText('Close')
    elif label.text() == 'Fecha:':
        msg_box.setWindowTitle('Paso 6 de 6: Registrar y guardar')
        message = '<p align = "justify">'\
                  'Por defecto, el botón <b><em>Registrar</em></b> está '\
                  'desactivado.</p>'\
                  '<p align = "justify">'\
                  'Para activarlo, asegúrese de haber elejido al menos el '\
                  'Punto de Referencia.</p>'\
                  '<p align = "justify">'\
                  'Una vez que complete el Paso 5 y termine de rellenar la '\
                  'Ficha, haga clic en el botón <b><em>Registrar</em></b> y '\
                  'espere hasta que el programa registra todos los datos '\
                  'correctamente.</p>'\
                  '<p align = "justify">'\
                  'Una vez completado el registro, el programa le pedirá que '\
                  'guarde el proyecto como archivo *.qgs o *.qgz para poder '\
                  'acceder a él en el futuroy también exportará las '\
                  'coordenadas del Monumento y de la Área Protegida a un '\
                  'archivo *.xls de MS Excel.</p>'\
                  '<p align = "justify">'\
                  'Para guardar el proyecto, vaya a <b><em>Archivo &gt; '\
                  'Guardar proyecto </em> </b>(o utilice Ctrl+S).</p>'\
                  '<p align = "justify">'\
                  'Su proyecto ya está registrado y guardado para su '\
                  'comodidad.</p>'
        btn_Ok.setText('Paso 5')
        btn_Cancel.setText('Cerrar')
    msg_box.setText(message)
    msg_box.setDefaultButton(btn_Cancel)
    msg_box.exec_()
    if msg_box.clickedButton() == btn_Ok:
        getStarted_step5(label, lineEdit_27, lineEdit_28)
    elif msg_box.clickedButton() == btn_Cancel:
        pass
