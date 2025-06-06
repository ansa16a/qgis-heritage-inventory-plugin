from qgis.PyQt.QtWidgets import QMessageBox
from qgis.gui import QgsProjectionSelectionDialog
from qgis.core import QgsProject, QgsCoordinateReferenceSystem

STEP_KEYS = {
    1: ('step1_title', 'step1_message'),
    2: ('step2_title', 'step2_message'),
    3: ('step3_title', 'step3_message'),
    4: ('step4_title', 'step4_message'),
    5: ('step5_title', 'step5_message'),
    6: ('step6_title', 'step6_message')
}

MESSAGES = {
    'en': {
        'step1_title': "Step 1 of 6: Base map",
        'step1_message': """
            <p align='justify'>Before starting the inventory process,
            please ensure the base map is present in the project.
            This is needed in order for the project elements and the
            maps to be set in the same Coordinate Reference System (CRS).
            </p><ul>
                <li>If the base map is not selected, please:</li>
                <ol>
                    <li>Close the plugin,</li>
                    <li>choose a base map, and</li>
                    <li>restart the plugin.</li>
                </ol>
                <li>If the base map is selected, and you want to proceed
                to the next step, please click <b>Step 2</b>.</li>
            </ul>
        """,
        'step1_buttons': {'ok': 'Step 2', 'cancel': 'Close'},
        'step2_title': "Step 2 of 6: Select CRS",
        'step2_message': """
            <p align = "justify">Please select the CRS.</p>
            <p align = "justify">It is recommended to choose Web Marcator
            projection EPSG:3857.</p>
        """,
        'step2_buttons': {
            "ok": "Select CRS", "save": "Step 1", "open": "Step 3",
            "cancel": "Close"},
        'step3_title': "Step 3 of 6: Creating a New Project",
        'step3_message': """
            <p align = "justify">
            To create a new project, go to <b>File &gt; New Project</b> (or use
            Ctrl+Shift+N).</p>
            <p align = "justify">
            Choose a folder to store your project files. The program will
            create for you two folders and the following three geopackages:
            <ol>
                <li>A point layer for storing the points of reference.</li>
                <li>A polygon layer for recording monument areas.</li>
                <li>Another polygon layer for registering protected areas.</li>
            </ol> </p>
            <p align = "justify">
            Geopackages will store data input in the plugin. One of the folders
            will store the copies of all the images used in the project, while
            the other one will store all the additional attachments (if any).
            </p>
        """,
        'step3_buttons': {"ok": "Step 2", "open": "Step 4", "cancel": "Close"},
        'step4_title': "Step 4 of 6: New Worksheet",
        'step4_message': """
            <p align = "justify">
            To register a new heritage object go to <b>File &gt; New
            Worksheet</b> (or use Ctrl+N).</p>
            <p align = "justify">
            You will be prompted to select a folder where the project
            files will be created.</p>
        """,
        'step4_buttons': {"ok": "Step 3", "open": "Step 5", "cancel": "Close"},
        'step5_title': "Step 5 of 6: Fill out the worksheet",
        'step5_message': """
            <p align = "justify">
            The worksheet consists of a total of 14 sections.</p>
            <p align = "justify">
            Please note that most of the information in the worksheet is
            mandatory, and some sections may appear disabled. To enable
            these sections, ensure that you have completed all the required
            information.</p>
        """,
        'step5_buttons': {"ok": "Step 4", "open": "Step 6", "cancel": "Close"},
        'step6_title': "Step 6 of 6: Register and save",
        'step6_message': """
            <p align = "justify">
            By default, the <b>Register</b> button is disabled.</p>
            <p align = "justify">
            To enable it, make sure you have drawn at least the Point of
            Reference.</p>
            <p align = "justify">
            Once you complete the Step 5 and finish filling out the Worksheet,
            click the <b>Register</b> button and wait until the program
            registers all the data correctly.</p>
            <p align = "justify">
            After registration is complete, the program will prompt you to
            save the project as either a *.qgs or *.qgz file for future access,
            and will also export the coordinates of the Monument and Protected
            Area to a MS Excel file.</p>
            <p align = "justify">
            You can save the project by going to <b>File &gt; Save Project</b>
            (or use Ctrl+S).</p>
            <p align = "justify">
            Your project is now registered and saved for your convenience.</p>
        """,
        'step6_buttons': {"ok": "Step 5", "cancel": "Close"}
    },
    'hy': {
        'step1_title': "Քայլ 1 6-ից. Բազային քարտեզ",
        'step1_message': """
            <p align='justify'>
            Նախքան գույքագրման գործընթացը սկսելը, խնդրում ենք համոզվել, որ
            հիմնական (բազային) քարտեզը առկա է նախագծում: Վերջինս անհրաժեշտ է
            ծրագրի տարրերը և քարտեզները միևնույն Կոորդինատների Տեղեկատվության
            Համակարգում (CRS) գրանցելու համար:</p>
            <ul>
                <li>Եթե հիմնական քարտեզն ընտրված չէ, խնդրում ենք՝</li>
                <ol>
                    <li>փակել հավելվածը,</li>
                    <li>ընտրել բազային քարտեզը, և</li>
                    <li>վերագործարկել հավելվածը:</li>
                </ol>
                <li>Եթե հիմնական քարտեզն ընտրված է, և ցանկանում եք անցնել
                հաջորդ քայլին, խնդրում ենք սեղմել <b>Քայլ 2</b> կոճակին։</li>
            </ul>
        """,
        'step1_buttons': {'ok': 'Քայլ 2', 'cancel': 'Փակել'},
        'step2_title': "Քայլ 2 6-ից. Ընտրել CRS-ը",
        'step2_message': """
            <p align = "justify">Խնդրում ենք ընտրել CRS-ը:</p>
            <p align = "justify">Խորհուրդ է տրվում ընտրել Web Marcator
            պրոյեկցիան EPSG:3857:<p>
        """,
        'step2_buttons': {
            "ok": "Ընտրել CRS", "save": "Քայլ 1",
            "open": "Քայլ 2", "cancel": "Փակել"},
        'step3_title': "Քայլ 3 6-ից. Նոր նախագծի ստեղծում",
        'step3_message': """
            <p align = "justify">
            Նոր նախագիծ ստեղծելու համար անցեք <b>Գլխավոր -&gt; Նոր նախագիծ</b>
            (կամ օգտագործեք Ctrl+Shift+N):</p>
            <p align = "justify">
            Ընտրեք թղթապանակ՝ Ձեր նախագծի ֆայլերը պահելու համար: Ծրագիրը
            Ձեզ համար կստեղծի երկու թղթապանակ և հետևյալ երեք գեոփաթեթները.
            </p>
            <ol>
                <li>Կետային շերտ՝ հենակետի կոորդինատները պահելու համար:</li>
                <li>Բազմանկյուն շերտ՝ հուշարձանների տարածքը գրանցելու համար:</li>
                <li>Բազմանկյուն շերտ՝ պահպանական գոտու տարածքները գրանցելու
                համար:</li></ol>
            <p align = "justify">
            Գեոփաթեթներում կհավաքագրվեն մուտքագրված տվյալները: Թղթապանակներից
            մեկը կպահի նախագծում օգտագործված բոլոր պատկերների պատճենները, իսկ
            մյուսը կպահի բոլոր լրացուցիչ կցված նյութերը (եթե այդպիսիք լինեն):
            </p>
        """,
        'step3_buttons': {"ok": "Քայլ 2", "open": "Քայլ 4", "cancel": "Փակել"},
        'step4_title': "Քայլ 4 6-ից. Նոր աշխատաթերթ",
        'step4_message':  """
            <p align = "justify">
            Նոր ժառանգության օբյեկտ գրանցելու համար անցեք <b>Գլխավոր
            -&gt; Նոր աշխատաթերթ</b> (կամ օգտագործեք Ctrl+N):</p>
            <p align = "justify">
            Ընտրեք թղթապանակը, որտեղ կստեղծվեն նախագծի ֆայլերը:</p>
        """,
        'step4_buttons': {"ok": "Քայլ 3", "open": "Քայլ 5", "cancel": "Փակել"},
        'step5_title': "Քայլ 5 6-ից. Լրացնել աշխատաթերթը",
        'step5_message': """
            <p align = "justify">
            Աշխատաթերթն ընդհանուր առմամբ բաղկացած է 14 բաժիններից:</p>
            <p align = "justify">
            Խնդրում ենք նկատի ունենալ, որ աշխատանքային թերթի տեղեկատվության
            որոշ մասի լրացումը պարտադիր է, և որոշ բաժիններ կամ կոճակներ
            կարող են անջատված լինել: Դրանք միացնելու համար համոզվեք, որ
            լրացրել եք բոլոր անհրաժեշտ տեղեկությունները:</p>
        """,
        'step5_buttons': {"ok": "Քայլ 4", "open": "Քայլ 6", "cancel": "Փակել"},
        'step6_title': "Քայլ 6 6-ից. Գրանցել և պահպանել",
        'step6_message': """
            <p align = "justify">
            Նոր աշխատաթերթի լրացման սկզբում գրանցման կոճակն անջատված է:</p>
            <p align = "justify">
            Այն միացնելու համար համոզվեք, որ քարտեզի վրա առնվազն
            հենակետի կոորդինատները գրանցված են:</p>
            <p align = "justify">
            Երբ ավարտեք 5-րդ քայլը՝ աշխատաթերթի լրացումը, խնդրում ենք
            սեղմել <b>Գրանցել</b> կոճակը և սպասել, մինչև ծրագիրը
            գրանցի բոլոր տվյալները:</p>
            <p align = "justify">
            Գրանցման ավարտից հետո ծրագիրը կառաջարկի պահպանել նախագիծը որպես
            *.qgs կամ *.qgz ֆայլ՝ ապագայում այն որպես հիմնական ֆայլ
            օգտագործելու համար, ինչպես նաև կարտահանի Հուշարձանի տարածքի և
            Պահպանական գոտու կոորդինատները որպես MS Excel ֆայլ:</p>
            <p align = "justify">
            Դուք կարող եք պահպանել նախագիծը՝ անցնելով <b>Գլխավոր -&gt;
            Պահպանել նախագիծը</b> (կամ օգտագործել Ctrl+S):</p>
            <p align = "justify"> Ձեր նախագիծն այժմ գրանցված է։</p>
        """,
        'step6_buttons': {"ok": "Paso 4", "open": "Paso 6", "cancel": "Cerrar"}
    },
    'es': {
        'step1_title': "Paso 1 de 6: Mapa base",
        'step1_message': """
            <p align='justify'>
            Antes de iniciar el proceso de inventario, asegúrese de
            que el mapa base está presente en el proyecto. Esto es
            necesario para que los elementos del proyecto y los mapas
            se establezcan en el mismo Sistema de Referencia de Coordenadas
            (SRC).</p>
            <ul>
                <li>Si el mapa base no está seleccionado, por favor:</li>
                <ol>
                    <li>Cierre el plugin,</li>
                    <li>elija un mapa base, y</li>
                    <li>reinicie el plugin.</li>
                </ol>
                <li>Si el mapa base está seleccionado y desea continuar con
                el siguiente paso, haga clic en <b>Paso 2</b>.
                </li>
            </ul>
        """,
        'step1_buttons': {"ok": "Paso 2", "cancel": "Cerrar"},
        'step2_title': "Paso 2 de 6: Seleccionar SRC",
        'step2_message': """
            <p align = "justify">Por favor, seleccione el SRC.</p>
            <p align = "justify">Se recomienda elegir la proyección Web
            Marcator EPSG:3857.</p>
        """,
        'step2_buttons': {
            "ok": "Seleccionar SRC", "save": "Paso 1",
            "open": "Paso 3", "cancel": "Cerrar"},
        'step3_title': "Paso  de 6: Creación de un Nuevo Proyecto",
        'step3_message': """
            <p align = "justify">
            Para iniciar un nuevo proyecto, ve a <b>Archivo &gt; Nuevo
            Proyecto</b> (o utiliza Ctrl+Mayús+N).</p>
            <p align = "justify">
            Elija una carpeta para almacenar los archivos del proyecto. El
            programa creará dos carpetas y los tres siguientes geopaquetes:</p>
            <ol>
                <li>Una capa de puntos para almacenar los puntos de referencia.</li>
                <li>Una capa de polígonos para registrar las zonas monumentales.</li>
                <li>Otra capa de polígonos para registrar zonas protegidas.</li></ol>
            <p align = "justify">
            Los geopaquetes almacenarán los datos introducidos en el plugin.
            Una de las carpetas almacenará las copias de todas las imágenes
            utilizadas en el proyecto, mientras que la otra almacenará todos
            los archivos adjuntos adicionales (en su caso).</p>
        """,
        'step3_buttons': {"ok": "Paso 2", "open": "Paso 4", "cancel": "Cerrar"},
        'step4_title': "Paso 4 de 6: Nueva Ficha",
        'step4_message': """
            <p align = "justify">
            Para registrar un nuevo objeto patrimonial vaya a <b> Archivo &gt;
            Nueva Ficha </b>(o utilice Ctrl+N).</p>
            <p align = "justify">
            Se le pedirá que seleccione una carpeta donde se crearán los
            archivos del proyecto.</p>
        """,
        'step4_buttons': {"ok": "Paso 3", "open": "Paso 5", "cancel": "Cerrar"},
        'step5_title': "Paso 5 de 6: Rellenar la Ficha",
        'step5_message': """
            <p align = "justify">
            La ficha consta de un total de 14 secciones.</p>
            <p align = "justify">
            Tenga en cuenta que la mayor parte de la información de la ficha es
            obligatoria y que algunas secciones pueden aparecer deshabilitadas.
            Para habilitar estas secciones, asegúrese de haber completado toda
            la información requerida.</p>
        """,
        'step5_buttons': {"ok": "Paso 4", "open": "Paso 6", "cancel": "Cerrar"},
        'step6_title': "Paso 6 de 6: Registrar y guardar",
        'step6_message': """
            <p align = "justify">
            Por defecto, el botón <b>Registrar</b> está desactivado.</p>
            <p align = "justify">
            Para activarlo, asegúrese de haber elejido al menos el Punto de
            Referencia.</p>
            <p align = "justify">
            Una vez que complete el Paso 5 y termine de rellenar la Ficha, haga
            clic en el botón <b>Registrar</b> y espere hasta que el programa
            registra todos los datos correctamente.</p>
            <p align = "justify">
            Una vez completado el registro, el programa le pedirá que guarde el
            proyecto como archivo *.qgs o *.qgz para poder acceder a este en el
            futuro y también exportará las coordenadas del Monumento y de la
            Área Protegida a un archivo de MS Excel.</p>
            <p align = "justify">
            Para guardar el proyecto, vaya a <b>Archivo &gt; Guardar proyecto
            </b> (o utilice Ctrl+S).</p>
            <p align = "justify">
            Su proyecto ya está registrado y guardado para su comodidad.</p>
        """,
        'step6_buttons': {"ok": "Paso 5", "cancel": "Cerrar"}
    }
}


def detect_language(label):
    """Detect language of the interface"""

    text = label.text()
    if text.startswith('Ամսաթիվ'):
        return 'hy'
    elif text == 'Date:':
        return 'en'
    elif text == 'Fecha:':
        return 'es'
    return 'en'


def show_message_box(label, step_num, buttons):
    """Message cration with dynamic button naming"""

    lang = detect_language(label)
    title_key, message_key = STEP_KEYS[step_num]
    msg_box = QMessageBox()
    msg_box.setStandardButtons(buttons)
    msg_box.setWindowTitle(MESSAGES[lang].get(title_key, ''))
    msg_box.setText(MESSAGES[lang].get(message_key, ''))

    button_labels = MESSAGES[lang].get(f'step{step_num}_buttons', {})
    role_map = {
       'ok': QMessageBox.Ok,
       'open': QMessageBox.Open,
       'save': QMessageBox.Save,
       'cancel': QMessageBox.Cancel
    }

    for key, role in role_map.items():
        button = msg_box.button(role)
        if button and key in button_labels:
            button.setText(button_labels[key])

    return msg_box


def getStarted_step1(label, lineEdit_27, lineEdit_28):
    """
    Display a message box for Step 1 of 6 of the inventory process.
    Prompt the user to ensure the base map is present in the project.
    """

    msg_box = show_message_box(
        label, 1, QMessageBox.Ok | QMessageBox.Cancel)
    msg_box.setDefaultButton(msg_box.button(QMessageBox.Ok))
    clicked = msg_box.exec_()
    if clicked == QMessageBox.Ok:
        getStarted_step2(label, lineEdit_27, lineEdit_28)


def getStarted_step2(label, lineEdit_27, lineEdit_28):
    """
    Display a message box for Step 2 of 6 of the inventory process.
    Prompt the user to select the Coordinate Reference System for the project.
    """

    msg_box = show_message_box(
        label, 2,
        QMessageBox.Ok | QMessageBox.Save | QMessageBox.Open | QMessageBox.Cancel)
    msg_box.setDefaultButton(msg_box.button(QMessageBox.Ok))
    clicked = msg_box.exec_()
    if clicked == QMessageBox.Ok:
        crs_selection(lineEdit_27, lineEdit_28)
    elif clicked == QMessageBox.Save:
        getStarted_step1(label, lineEdit_27, lineEdit_28)
    elif clicked == QMessageBox.Open:
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

    msg_box = show_message_box(
        label, 3, QMessageBox.Ok | QMessageBox.Open | QMessageBox.Cancel)
    msg_box.setDefaultButton(msg_box.button(QMessageBox.Open))
    clicked = msg_box.exec_()
    if clicked == QMessageBox.Ok:
        getStarted_step2(label, lineEdit_27, lineEdit_28)
    elif clicked == QMessageBox.Open:
        getStarted_step4(label, lineEdit_27, lineEdit_28)


def getStarted_step4(label, lineEdit_27, lineEdit_28):
    """
    Display a message box for Step 4 of 6 of the the inventory process, which
    involves creating a new worksheet.
    """

    msg_box = show_message_box(
        label, 4, QMessageBox.Ok | QMessageBox.Open | QMessageBox.Cancel)
    msg_box.setDefaultButton(msg_box.button(QMessageBox.Open))
    clicked = msg_box.exec_()
    if clicked == QMessageBox.Ok:
        getStarted_step3(label, lineEdit_27, lineEdit_28)
    elif clicked == QMessageBox.Open:
        getStarted_step5(label, lineEdit_27, lineEdit_28)


def getStarted_step5(label, lineEdit_27, lineEdit_28):
    """
    Display a message box for Step 5 of 6 of the inventory process, which
    involves filling out the worksheet.
    """

    msg_box = show_message_box(
        label, 5, QMessageBox.Ok | QMessageBox.Open | QMessageBox.Cancel)
    msg_box.setDefaultButton(msg_box.button(QMessageBox.Open))
    clicked = msg_box.exec_()
    if clicked == QMessageBox.Ok:
        getStarted_step4(label, lineEdit_27, lineEdit_28)
    elif clicked == QMessageBox.Open:
        getStarted_step6(label, lineEdit_27, lineEdit_28)


def getStarted_step6(label, lineEdit_27, lineEdit_28):
    """
    Display a message box for the final Step of the inventory process, which
    involves registering and saving the project.
    """

    msg_box = show_message_box(
        label, 6, QMessageBox.Ok | QMessageBox.Cancel)
    msg_box.setDefaultButton(msg_box.button(QMessageBox.Cancel))
    if msg_box.exec_() == QMessageBox.Ok:
        getStarted_step5(label, lineEdit_27, lineEdit_28)
