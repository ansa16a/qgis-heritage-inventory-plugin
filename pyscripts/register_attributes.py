import os
from .utils import change_attribute_values
from qgis.core import QgsProject, QgsField
from qgis.PyQt.QtCore import QVariant
from .image_loader import ImageLoader_1
import shutil


def register_tabs(self, dir_doc, dir_img, fnameim_1, fnameim_2):
    """Register data from tabs to attribute tables"""

    global ID
    ID = ''

    reg_1_inspection_data(self)
    reg_2_identification_information(self)
    reg_3_visual_presentation(self, dir_img, fnameim_1, fnameim_2)
    reg_4_location_information(self)
    reg_5_monuments_and_protected_areas(self)
    reg_6_type_of_the_element_and_description_of_its_attributes(self)
    reg_7_descriptive_characteristic_reference(self)
    reg_8_physical_condition_and_conservation_details(self)
    reg_9_legal_information_and_management(self)
    reg_10_uses_accessibility_and_management(self)
    reg_11_intrinsic_and_tourism_values(self)
    reg_12_13_observations_bibliography(self)
    reg_14_graphical_documents(self, dir_doc, dir_img)


def reg_1_inspection_data(self):
    """Register data from tab '1': INSPECTION DATA."""

    global inda_wcode, inda_date, inda_pldaco, inda_fname, inda_email
    global inda_conum, inda_com

    inda_wcode, inda_date, inda_pldaco, inda_fname = '', '', '', ''
    inda_email, inda_conum, inda_com = '', '', ''

    # Worksheet code
    inda_wcode = (f'{self.lineEdit.text()}_{self.lineEdit_2.text()}_'
                  f'{self.lineEdit_30.text()}_{self.lineEdit_31.text()}')
    inda_date = self.dateEdit.date()  # Date
    inda_pldaco = self.lineEdit_3.text()  # Place of data collection
    inda_fname = (f'{self.lineEdit_4.text()} '
                  f'{self.lineEdit_5.text()}')  # Name Surname
    inda_email = self.lineEdit_6.text()  # E-mail
    inda_conum = (f'{self.lineEdit_7.text()}'  # Contact number
                  f'{self.lineEdit_12.text()}')
    inda_com = self.textEdit_32.toPlainText()  # Comments


def reg_2_identification_information(self):
    """Register data from tab '2': IDENTIFICATION INFORMATION."""

    global idin_hestat, idin_hecert, idin_heceid, idin_hilev, idin_sign
    global idin_name, idin_otname, idin_com

    idin_hestat, idin_hecert, idin_heceid, idin_hilev = '', '', '', ''
    idin_sign, idin_name, idin_otname, idin_com = '', '', '', ''

    # Heritage Status
    if self.radioButton_46.isChecked():
        idin_hestat = self.radioButton_46.text()  # Registered
    elif self.radioButton_45.isChecked():
        idin_hestat = self.radioButton_45.text()  # Inventoried
    elif self.radioButton_47.isChecked():
        idin_hestat = self.radioButton_47.text()  # None
    # Heritage Certificate
    if self.radioButton_3.isChecked():
        idin_hecert = self.radioButton_3.text()  # Yes
    elif self.radioButton_4.isChecked():
        idin_hecert = self.radioButton_4.text()  # No
    elif self.radioButton_5.isChecked():
        idin_hecert = self.lineEdit_8.text()  # Other
    idin_heceid = self.lineEdit_9.text()  # Heritage Certificate ID
    idin_hilev = self.lineEdit_19.text()  # Hierarchy level
    idin_sign = self.comboBox_5.currentText()  # Significance
    idin_name = self.lineEdit_10.text()  # Name
    idin_otname = self.lineEdit_11.text()  # Other Nmae
    idin_com = self.textEdit_15.toPlainText()  # Comments


def reg_3_visual_presentation(self, dir_img, fnameim_1, fnameim_2):
    """Register data from tab '3': VISUAL PRESENTATION."""

    global vipr_im_1, vipr_imcap1, vipr_credit1, vipr_datetkn1, vipr_pltkn1
    global vipr_source1, vipr_im_2, vipr_imcap2, vipr_credit2, vipr_datetkn2
    global vipr_pltkn2, vipr_source2, vipr_com

    vipr_im_1, vipr_imcap1, vipr_credit1, vipr_datetkn1 = '', '', '', ''
    vipr_pltkn1, vipr_source1, vipr_im_2, vipr_imcap2 = '', '', '', ''
    vipr_credit2, vipr_datetkn2, vipr_pltkn2, vipr_source2 = '', '', '', ''
    vipr_com = ''

    # Image 1 (current state)
    # img1 create a duplicate of the image in the new location and
    # store the image in the attribute table
    changeimagename1 = (f'{self.lineEdit.text()}_{self.lineEdit_2.text()}_'
                        f'{self.lineEdit_30.text()}_'
                        f'{self.lineEdit_31.text()}_'+'im_1')
    if self.label_130.isEnabled():
        if fnameim_1.endswith('PNG') or fnameim_1.endswith('png'):
            changeimagename1 = changeimagename1 + '.png'
        elif fnameim_1.endswith('JPG') or fnameim_1.endswith('jpg'):
            changeimagename1 = changeimagename1 + '.jpg'
        elif fnameim_1.endswith('JPEG') or fnameim_1.endswith('jpeg'):
            changeimagename1 = changeimagename1 + '.jpeg'
        elif fnameim_1.endswith('TIFF') or fnameim_1.endswith('tiff'):
            changeimagename1 = changeimagename1 + '.tiff'
        elif fnameim_1.endswith('RAW') or fnameim_1.endswith('raw'):
            changeimagename1 = changeimagename1 + '.raw'
        elif fnameim_1.endswith('JFIF') or fnameim_1.endswith('jfif'):
            changeimagename1 = changeimagename1 + '.jfif'
        dir_img1 = dir_img + '/' + changeimagename1
        original1 = r'{}'.format(fnameim_1)
        target1 = r'{}'.format(dir_img1)
        shutil.copyfile(original1, target1)
        vipr_im_1 = str(target1)
    else:
        if self.label.text().startswith('Ամսաթիվ'):
            vipr_im_1 = 'Տ․Բ․'
        elif self.label.text() == 'Date:':
            vipr_im_1 = 'N/A'
        elif self.label.text() == 'Fecha:':
            vipr_im_1 = 'N/D'
    vipr_imcap1 = self.lineEdit_13.text()  # Image caption
    vipr_credit1 = self.lineEdit_14.text()  # Credit
    vipr_datetkn1 = self.lineEdit_73.text()  # Date/Year taken
    vipr_pltkn1 = self.lineEdit_15.text()  # Place taken
    vipr_source1 = self.lineEdit_37.text()  # Source

    # Image 2 (initial state)
    # img2 create a duplicate of the image in the new location and
    # store the image in the attribute table
    changeimagename2 = (f'{self.lineEdit.text()}_{self.lineEdit_2.text()}_'
                        f'{self.lineEdit_30.text()}_'
                        f'{self.lineEdit_31.text()}_'+'im_2')
    if self.label_131.isEnabled():
        if fnameim_2.endswith('PNG') or fnameim_2.endswith('png'):
            changeimagename2 = changeimagename2 + '.png'
        elif fnameim_2.endswith('JPG') or fnameim_2.endswith('jpg'):
            changeimagename2 = changeimagename2 + '.jpg'
        elif fnameim_2.endswith('JPEG') or fnameim_2.endswith('jpeg'):
            changeimagename2 = changeimagename2 + '.jpeg'
        elif fnameim_2.endswith('TIFF') or fnameim_2.endswith('tiff'):
            changeimagename2 = changeimagename2 + '.tiff'
        elif fnameim_2.endswith('RAW') or fnameim_2.endswith('raw'):
            changeimagename2 = changeimagename2 + '.raw'
        elif fnameim_2.endswith('JFIF') or fnameim_2.endswith('jfif'):
            changeimagename2 = changeimagename2 + '.jfif'
        dir_img2 = dir_img + '/' + changeimagename2
        original2 = r'{}'.format(fnameim_2)
        target2 = r'{}'.format(dir_img2)
        shutil.copyfile(original2, target2)
        vipr_im_2 = str(target2)
    else:
        if self.label.text().startswith('Ամսաթիվ'):
            vipr_im_2 = 'Տ․Բ․'
        elif self.label.text() == 'Date:':
            vipr_im_2 = 'N/A'
        elif self.label.text() == 'Fecha:':
            vipr_im_2 = 'N/D'
    vipr_imcap2 = self.lineEdit_16.text()  # Image caption
    vipr_credit2 = self.lineEdit_17.text()  # Credit
    vipr_datetkn2 = self.lineEdit_79.text()  # Date/Year taken
    vipr_pltkn2 = self.lineEdit_18.text()  # Place the image was taken
    vipr_source2 = self.lineEdit_36.text()  # Source
    vipr_com = self.textEdit_16.toPlainText()  # Comments


def reg_4_location_information(self):
    """Register data from tab '4': LOCATION INFORMATION."""

    global loin_geloin_country, loin_geloin_provstate, loin_geloin_city
    global loin_geloin_dist, loin_geloin_strname, loin_geloin_strnum
    global loin_geloin_postco, loin_geloin_otlocdet, loin_coorpore_crs
    global loin_coorpore_authid, loin_coorpore_full_utm, loin_coorpore_utm
    global loin_coorpore_hemi, loin_coorpore_lat_band, loin_coorpore_eax
    global loin_coorpore_noy, loin_coorpore_com

    loin_geloin_country, loin_geloin_provstate = '', ''
    loin_geloin_city, loin_geloin_dist, loin_geloin_strname = '', '', ''
    loin_geloin_strnum, loin_geloin_postco = '', ''
    loin_geloin_otlocdet, loin_coorpore_crs = '', ''
    loin_coorpore_authid, loin_coorpore_full_utm = '', ''
    loin_coorpore_utm, loin_coorpore_hemi = '', ''
    loin_coorpore_lat_band, loin_coorpore_eax = '', ''
    loin_coorpore_noy, loin_coorpore_com = '', ''

    loin_geloin_country = self.lineEdit_20.text()       # Country
    loin_geloin_provstate = self.lineEdit_22.text()     # Province/State
    loin_geloin_city = self.lineEdit_21.text()          # City
    loin_geloin_dist = self.lineEdit_23.text()          # District
    loin_geloin_strname = self.lineEdit_25.text()       # Street name
    loin_geloin_strnum = self.lineEdit_24.text()        # Street number
    loin_geloin_postco = self.lineEdit_47.text()        # Postal code
    loin_geloin_otlocdet = self.textEdit_19.toPlainText()  # Other details
    loin_coorpore_crs = self.lineEdit_27.text()         # CRS
    loin_coorpore_authid = self.lineEdit_28.text()      # Authority ID
    loin_coorpore_lat_band = self.comboBox.currentText()
    loin_coorpore_utm = self.lineEdit_29.text()         # UTM Zone
    # Hemisphere
    if self.radioButton_6.isChecked():  # North
        loin_coorpore_hemi = self.radioButton_6.text()
    elif self.radioButton_7.isChecked():    # South
        loin_coorpore_hemi = self.radioButton_7.text()
    loin_coorpore_eax = self.lineEdit_34.text()  # Easting (X)
    loin_coorpore_noy = self.lineEdit_35.text()  # Northing (Y)

    hem_text_n, hem_text_e = '', ''
    if self.label.text().startswith('Ամսաթիվ'):
        hem_text_n, hem_text_e = 'Հս', 'Հվ'
    else:
        hem_text_n, hem_text_e = 'N', 'S'

    if self.radioButton_6.isChecked():
        hemisphere = str(hem_text_n)
    else:
        hemisphere = str(hem_text_e)

    loin_coorpore_full_utm = (f'{hemisphere} {loin_coorpore_utm}'
                              f'{loin_coorpore_lat_band} {loin_coorpore_eax} '
                              f'{loin_coorpore_noy}')
    loin_coorpore_com = self.textEdit_17.toPlainText()  # Comments


def reg_5_monuments_and_protected_areas(self):
    """Register data from tab '5': MONUMENTS AND PROTECTED AREAS."""

    global mopra_mocota_por, mopra_mocota_monha, mopra_mocota_monsqm
    global mopra_prcota_prha, mopra_prcota_prsqm, mopra_prcota_com

    mopra_mocota_por, mopra_mocota_monha, mopra_mocota_monsqm = '', '', ''
    mopra_prcota_prha, mopra_prcota_prsqm, mopra_prcota_com = '', '', ''

    mopra_mocota_por = self.textEdit_21.toPlainText()  # Pivot edge text
    # Monument area:
    mopra_mocota_monha = self.lineEdit_45.text()  # ha
    mopra_mocota_monsqm = self.lineEdit_83.text()  # sqm
    # Protected area:
    mopra_prcota_prha = self.lineEdit_131.text()  # ha
    mopra_prcota_prsqm = self.lineEdit_132.text()  # sqm
    mopra_prcota_com = self.textEdit_42.toPlainText()  # Comments


def reg_6_type_of_the_element_and_description_of_its_attributes(self):
    """
    Register data from tab '6': TYPE OF THE ELEMENT AND DESCRIPTION OF ITS
    ATTRIBUTES.
    """

    global tyeldeat_ty_categ, tyeldeat_ty_elem, tyeldeat_ty_com
    global tyeldeat_code_constdate, tyeldeat_code_cent
    global tyeldeat_code_archsty, tyeldeat_code_author
    global tyeldeat_code_storeys, tyeldeat_code_material
    global tyeldeat_code_phydescsett, tyeldeat_code_com

    tyeldeat_ty_categ, tyeldeat_ty_elem, tyeldeat_ty_com = '', '', ''
    tyeldeat_code_constdate, tyeldeat_code_cent = '', ''
    tyeldeat_code_archsty, tyeldeat_code_author = '', ''
    tyeldeat_code_storeys, tyeldeat_code_material = '', ''
    tyeldeat_code_phydescsett, tyeldeat_code_com = '', ''

    # Category
    if self.radioButton_8.isChecked():
        tyeldeat_ty_categ = self.lineEdit_52.text()  # other category
    else:
        tyeldeat_ty_categ = self.comboBox_2.currentText()  # category
    # Element
    if self.radioButton_69.isChecked():
        tyeldeat_ty_elem = self.lineEdit_50.text()  # other element
    else:
        tyeldeat_ty_elem = self.comboBox_3.currentText()  # element
    tyeldeat_ty_com = self.textEdit_11.toPlainText()  # Comments
    # Construction date
    if self.radioButton_65.isChecked():
        tyeldeat_code_constdate = self.lineEdit_59.text()

    elif self.radioButton_67.isChecked():
        tyeldeat_code_constdate = self.radioButton_67.text()
    # Century
    if self.radioButton_66.isChecked():
        tyeldeat_code_cent = self.lineEdit_60.text()  # input data
    elif self.radioButton_72.isChecked():
        tyeldeat_code_cent = self.radioButton_72.text()  #
    # Architectural style: Registers data input by the user
    tyeldeat_code_archsty = self.lineEdit_61.text()

    if self.radioButton_73.isChecked():  # N/A
        tyeldeat_code_author = self.radioButton_73.text()
    elif self.radioButton_68.isChecked():  # Known
        # Author-role: position - full name
        p_n_1, p_n_2, p_n_3, p_n_4 = '', '', '', ''
        if self.checkBox_7.isChecked():  # 1
            p_n_1 = (f'{self.lineEdit_53.text()} - '
                     f'{self.lineEdit_54.text()}')
        if self.checkBox_10.isChecked():  # 2
            p_n_2 = (f'\n{self.lineEdit_55.text()} - '
                     f'{self.lineEdit_56.text()}')
        if self.checkBox_11.isChecked():  # 3
            p_n_3 = (f'\n{self.lineEdit_57.text()} - '
                     f'{self.lineEdit_58.text()}')
        if self.checkBox_24.isChecked():  # 4
            p_n_4 = (f'\n{self.lineEdit_85.text()} - '
                     f'{self.lineEdit_112.text()}')
        tyeldeat_code_author = (f'{p_n_1}{p_n_2}{p_n_3}{p_n_4}')

    # Stories
    if self.radioButton_9.isChecked():
        tyeldeat_code_storeys = self.radioButton_9.text()  # 1
    elif self.radioButton_10.isChecked():
        tyeldeat_code_storeys = self.radioButton_10.text()  # 2
    elif self.radioButton_12.isChecked():
        tyeldeat_code_storeys = self.radioButton_12.text()  # 3
    elif self.radioButton_11.isChecked():
        tyeldeat_code_storeys = self.radioButton_11.text()  # 4
    elif self.radioButton_13.isChecked():
        tyeldeat_code_storeys = self.radioButton_13.text()  # 5
    elif self.radioButton_14.isChecked():
        tyeldeat_code_storeys = self.lineEdit_32.text()  # Other

    # Material
    tyeldeat_code_material = self.lineEdit_33.text()
    # Description of the surrounding setting
    tyeldeat_code_phydescsett = self.textEdit_3.toPlainText()
    tyeldeat_code_com = self.textEdit_12.toPlainText()  # Comments


def reg_7_descriptive_characteristic_reference(self):
    """Register data from tab '7': DESCRIPTIVE-CHARACTERISTIC REFERENCE."""

    global de_chre_reason, de_chre_histno, de_chre_descsh, de_chre_recogn
    global de_chre_com

    de_chre_reason, de_chre_histno, de_chre_descsh = '', '', ''
    de_chre_recogn, de_chre_com = '', ''

    cb_5, cb_6, cb_25, cb_26 = '', '', '', ''
    if self.checkBox_5.isChecked():
        cb_5 = (f'{self.checkBox_5.text()}\n')
    if self.checkBox_6.isChecked():
        cb_6 = (f'{self.checkBox_6.text()}\n')
    if self.checkBox_25.isChecked():
        cb_25 = (f'{self.checkBox_25.text()}\n')
    if self.checkBox_26.isChecked():
        cb_26 = (f'{self.lineEdit_38.text()}\n')
    # Reason for its designation:
    de_chre_reason = (f'{cb_5}{cb_6}{cb_25}{cb_26}')
    # Description of the element
    de_chre_histno = self.textEdit_41.toPlainText()
    # Brief description/historical summary (max 300 words):
    de_chre_descsh = self.textEdit_45.toPlainText()
    # Scientific recognition:
    de_chre_recogn = self.textEdit_43.toPlainText()
    de_chre_com = self.textEdit_44.toPlainText()  # Comments


def reg_8_physical_condition_and_conservation_details(self):
    """
    Registers data from tab '8': PHYSICAL CONDITION AND CONSERVATION DETAILS.
    """

    global phcode_inhere_currcond, phcode_inhere_com
    global phcode_inrewoun_retaudate, phcode_inrewoun_cent
    global phcode_inrewoun_alterf, phcode_inrewoun_alterr
    global phcode_inrewoun_alterd, phcode_inrewoun_alterw
    global phcode_inrewoun_alterl, phcode_inrewoun_alterb
    global phcode_inrewoun_alterc, phcode_inrewoun_altero
    global phcode_inrewoun_desc, phcode_inrewoun_rest
    global phcode_inrewoun_consstand, phcode_inrewoun_com
    global phcode_rirewoun_risks, phcode_rirewoun_com

    phcode_inhere_currcond, phcode_inhere_com = '', ''
    phcode_inrewoun_retaudate, phcode_inrewoun_cent = '', ''
    phcode_inrewoun_alterf, phcode_inrewoun_alterr = '', ''
    phcode_inrewoun_alterd, phcode_inrewoun_alterw = '', ''
    phcode_inrewoun_alterl, phcode_inrewoun_alterb = '', ''
    phcode_inrewoun_alterc, phcode_inrewoun_altero = '', ''
    phcode_inrewoun_desc, phcode_inrewoun_rest = '', ''
    phcode_inrewoun_consstand, phcode_inrewoun_com = '', ''
    phcode_rirewoun_risks, phcode_rirewoun_com = '', ''

    # Current condition
    if self.radioButton_15.isChecked():
        phcode_inhere_currcond = (  # Demolished
            f'{self.radioButton_15.text()} - '
            f'{self.comboBox_4.currentText()}')
    elif self.radioButton_17.isChecked():  # Partially demolished
        phcode_inhere_currcond = self.radioButton_17.text()
    elif self.radioButton_16.isChecked():  # Façade only
        phcode_inhere_currcond = self.radioButton_16.text()
    elif self.radioButton_18.isChecked():  # Highly deteriorated
        phcode_inhere_currcond = self.radioButton_18.text()
    elif self.radioButton_19.isChecked():  # Partially maintained
        phcode_inhere_currcond = self.radioButton_19.text()
    elif self.radioButton_20.isChecked():  # Well maintained
        phcode_inhere_currcond = self.radioButton_20.text()
    elif self.radioButton_21.isChecked():  # Moved to a new location
        phcode_inhere_currcond = (
            f'{self.radioButton_21.text()} - '
            f'{self.textEdit_23.toPlainText()}')
    phcode_inhere_com = self.textEdit_22.toPlainText()  # Comments

    # Restauration date
    if self.radioButton_53.isChecked():  # Registers data input by the user
        phcode_inrewoun_retaudate = self.lineEdit_65.text()
    elif self.radioButton_54.isChecked():
        phcode_inrewoun_retaudate = self.radioButton_54.text()  # None
    elif self.radioButton_55.isChecked():
        phcode_inrewoun_retaudate = self.radioButton_55.text()  # n.d.

    # Century:
    if self.radioButton_56.isChecked():  # Registers data input by the user
        phcode_inrewoun_cent = self.lineEdit_66.text()
    elif self.radioButton_58.isChecked():
        phcode_inrewoun_cent = self.radioButton_58.text()  # None
    elif self.radioButton_57.isChecked():
        phcode_inrewoun_cent = self.radioButton_57.text()  # n.d.

    # Alterations: None, set text to None
    if self.radioButton_22.isChecked():
        phcode_inrewoun_alterf = self.radioButton_22.text()  # floor
        phcode_inrewoun_alterr = self.radioButton_22.text()  # room
        phcode_inrewoun_alterd = self.radioButton_22.text()  # door
        phcode_inrewoun_alterw = self.radioButton_22.text()  # window
        phcode_inrewoun_alterl = self.radioButton_22.text()  # lights
        phcode_inrewoun_alterb = self.radioButton_22.text()  # balcony
        phcode_inrewoun_alterc = self.radioButton_22.text()  # color
        phcode_inrewoun_altero = self.radioButton_22.text()  # other
    elif self.radioButton_23.isChecked():  # Alterations: Yes
        # Alterations: Floor
        if self.checkBox_13.isChecked():
            le_67, le_68, le_69 = '', '', ''
            if self.checkBox_21.isChecked():  # added
                le_67 = (f'{self.label_87.text()} - '
                         f'{self.lineEdit_67.text()}\n')
            if self.checkBox_22.isChecked():  # removed
                le_68 = (f'{self.label_88.text()} - '
                         f'{self.lineEdit_68.text()}\n')
            if self.checkBox_23.isChecked():  # reno/changed
                le_69 = (f'{self.label_89.text()} - '
                         f'{self.lineEdit_69.text()}')
            phcode_inrewoun_alterf = (  # added + removed + reno/changed
                f'{self.checkBox_13.text()}:\n{le_67}{le_68}{le_69}')
        else:  # None - not checked
            phcode_inrewoun_alterf = self.radioButton_22.text()
        # Alterations: Room
        if self.checkBox_14.isChecked():
            le_87, le_88, le_89 = '', '', ''
            if self.checkBox_41.isChecked():  # added
                le_87 = (f'{self.label_87.text()} - '
                         f'{self.lineEdit_87.text()}\n')
            if self.checkBox_42.isChecked():  # removed
                le_88 = (f'{self.label_88.text()} - '
                         f'{self.lineEdit_88.text()}\n')
            if self.checkBox_43.isChecked():  # reno/changed
                le_89 = (f'{self.label_89.text()} - '
                         f'{self.lineEdit_89.text()}')
            phcode_inrewoun_alterr = (  # added + removed + reno/changed
                f'{self.checkBox_14.text()}:\n{le_87}{le_88}{le_89}')
        else:  # None - not checked
            phcode_inrewoun_alterr = self.radioButton_22.text()
        # Alterations: Door
        if self.checkBox_16.isChecked():
            le_93, le_94, le_95 = '', '', ''
            if self.checkBox_47.isChecked():
                le_93 = (f'{self.label_87.text()} - '
                         f'{self.lineEdit_93.text()}\n')  # added
            if self.checkBox_48.isChecked():
                le_94 = (f'{self.label_88.text()} - '
                         f'{self.lineEdit_94.text()}\n')  # removed
            if self.checkBox_49.isChecked():
                le_95 = (f'{self.label_89.text()} - '
                         f'{self.lineEdit_95.text()}')  # reno/changed
            phcode_inrewoun_alterd = (  # added + removed + reno/changed
                f'{self.checkBox_16.text()}:\n{le_93}{le_94}{le_95}')
        else:  # None - not checked
            phcode_inrewoun_alterd = self.radioButton_22.text()
        # Alterations: Window
        if self.checkBox_15.isChecked():
            le_90, le_91, le_92 = '', '', ''
            if self.checkBox_44.isChecked():
                le_90 = (f'{self.label_87.text()} - '
                         f'{self.lineEdit_90.text()}\n')  # added
            if self.checkBox_45.isChecked():
                le_91 = (f'{self.label_88.text()} - '
                         f'{self.lineEdit_91.text()}\n')  # removed
            if self.checkBox_46.isChecked():
                le_92 = (f'{self.label_89.text()} - '
                         f'{self.lineEdit_92.text()}')  # reno/changed
            phcode_inrewoun_alterw = (  # added + removed + reno/changed
                f'{self.checkBox_15.text()}:\n{le_90}{le_91}{le_92}')
        else:  # None - not checked
            phcode_inrewoun_alterw = self.radioButton_22.text()
        # Alterations: Lights
        if self.checkBox_17.isChecked():
            le_96, le_97, le_98 = '', '', ''
            if self.checkBox_50.isChecked():
                le_96 = (f'{self.label_87.text()} - '
                         f'{self.lineEdit_96.text()}\n')  # added
            if self.checkBox_51.isChecked():
                le_97 = (f'{self.label_88.text()} - '
                         f'{self.lineEdit_97.text()}\n')  # removed
            if self.checkBox_52.isChecked():
                le_98 = (f'{self.label_89.text()} - '
                         f'{self.lineEdit_98.text()}')  # reno/changed
            phcode_inrewoun_alterl = (  # added + removed + reno/changed
                f'{self.checkBox_17.text()}:\n{le_96}{le_97}{le_98}')
        else:  # None - not checked
            phcode_inrewoun_alterl = self.radioButton_22.text()
        # Alterations: Balcony
        if self.checkBox_18.isChecked():
            le_99, le_100, le_101 = '', '', ''
            if self.checkBox_53.isChecked():
                le_99 = (f'{self.label_87.text()} - '
                         f'{self.lineEdit_99.text()}\n')  # added
            if self.checkBox_54.isChecked():
                le_100 = (f'{self.label_88.text()} - '
                          f'{self.lineEdit_100.text()}\n')  # removed
            if self.checkBox_55.isChecked():
                le_101 = (f'{self.label_89.text()} - '
                          f'{self.lineEdit_101.text()}')  # reno/changed
            phcode_inrewoun_alterb = (  # added + removed + reno/changed
                f'{self.checkBox_18.text()}:\n{le_99}{le_100}{le_101}')
        else:  # None - not checked
            phcode_inrewoun_alterb = self.radioButton_22.text()
        # Alterations: Colour
        if self.checkBox_19.isChecked():
            le_102, le_103, le_104 = '', '', ''
            if self.checkBox_56.isChecked():
                le_102 = (f'{self.label_87.text()} - '
                          f'{self.lineEdit_102.text()}\n')  # added
            if self.checkBox_57.isChecked():
                le_103 = (f'{self.label_88.text()} - '
                          f'{self.lineEdit_103.text()}\n')  # removed
            if self.checkBox_58.isChecked():
                le_104 = (f'{self.label_89.text()} - '
                          f'{self.lineEdit_104.text()}')  # reno/changed
            phcode_inrewoun_alterc = (  # added + removed + reno/changed
                f'{self.checkBox_19.text()}:\n{le_102}{le_103}{le_104}')
        else:  # None - not checked
            phcode_inrewoun_alterc = self.radioButton_22.text()
        # Alterations: Other
        if self.checkBox_20.isChecked():
            le_109, le_110, le_108 = '', '', ''
            if self.checkBox_63.isChecked():
                le_109 = (f'{self.label_87.text()} - '
                          f'{self.lineEdit_109.text()}\n')  # added
            if self.checkBox_64.isChecked():
                le_110 = (f'{self.label_88.text()} - '
                          f'{self.lineEdit_110.text()}\n')  # removed
            if self.checkBox_62.isChecked():
                le_108 = (f'{self.label_89.text()} - '
                          f'{self.lineEdit_108.text()}')  # changed
            phcode_inrewoun_altero = (  # added + removed + reno/changed
                f'{self.checkBox_20.text()}:\n{le_109}{le_110}{le_108}')
        else:  # None - not checked
            phcode_inrewoun_altero = self.radioButton_22.text()
    phcode_inrewoun_desc = self.textEdit_4.toPlainText()  # Description

    # Restaurateur - role
    if self.radioButton_52.isChecked():  # set text to n.d.
        phcode_inrewoun_rest = self.radioButton_52.text()
    elif self.radioButton_24.isChecked():  # set text to None
        phcode_inrewoun_rest = self.radioButton_24.text()
    elif self.radioButton_25.isChecked():  # Yes
        p_n_1, p_n_2, p_n_3, p_n_4 = '', '', '', ''
        if self.checkBox_74.isChecked():
            p_n_1 = (f'{self.lineEdit_124.text()} - '
                     f'{self.lineEdit_128.text()}')
        if self.checkBox_75.isChecked():
            p_n_2 = (f'\n{self.lineEdit_125.text()} - '
                     f'{self.lineEdit_129.text()}')
        if self.checkBox_76.isChecked():
            p_n_3 = (f'\n{self.lineEdit_126.text()} - '
                     f'{self.lineEdit_134.text()}')
        if self.checkBox_83.isChecked():
            p_n_4 = (f'\n{self.lineEdit_127.text()} - '
                     f'{self.lineEdit_135.text()}')
        phcode_inrewoun_rest = (f'{p_n_1}{p_n_2}{p_n_3}{p_n_4}')

    # Conservation standards (specify existent documents)
    if self.radioButton_30.isChecked():
        phcode_inrewoun_consstand = self.radioButton_30.text()  # None
    elif self.radioButton_31.isChecked():
        phcode_inrewoun_consstand = self.textEdit_13.toPlainText()  # Yes
    phcode_inrewoun_com = self.textEdit_24.toPlainText()  # Comments

    # Risks and threats
    if self.radioButton_59.isChecked():
        phcode_rirewoun_risks = self.radioButton_59.text()  # None
    elif self.radioButton_43.isChecked():  # Yes
        cb_39, cb_40, cb_59, cb_60, cb_61, cb_65 = '', '', '', '', '', ''
        cb_66, cb_67, cb_68, cb_69, cb_70, cb_71 = '', '', '', '', '', ''
        cb_72, cb_73, cb_77, cb_78, cb_79, cb_80 = '', '', '', '', '', ''
        cb_81, cb_82 = '', ''
        # Land-use changes (urban sprawl, etc.)
        if self.checkBox_39.isChecked():
            cb_39 = (f'{self.checkBox_39.text()}\n')
        # Alteration of the surrounding area
        if self.checkBox_40.isChecked():
            cb_40 = (f'{self.checkBox_40.text()}\n')
        # Traditional activities and customs no longer in use
        if self.checkBox_59.isChecked():
            cb_59 = (f'{self.checkBox_59.text()}\n')
        # Lack of heritage and territorial planning
        if self.checkBox_60.isChecked():
            cb_60 = (f'{self.checkBox_60.text()}\n')
        if self.checkBox_61.isChecked():  # Lack of maintenance
            cb_61 = (f'{self.checkBox_61.text()}\n')
        if self.checkBox_65.isChecked():  # Lack of legal protection
            cb_65 = (f'{self.checkBox_65.text()}\n')
        # Lack of physical barriers or protective elements
        if self.checkBox_66.isChecked():
            cb_66 = (f'{self.checkBox_66.text()}\n')
        # Lack of local communities’ appreciation
        if self.checkBox_67.isChecked():
            cb_67 = (f'{self.checkBox_67.text()}\n')
        # Lack of administrations awareness
        if self.checkBox_68.isChecked():
            cb_68 = (f'{self.checkBox_68.text()}\n')
        # Vulnerable construction techniques
        if self.checkBox_69.isChecked():
            cb_69 = (f'{self.checkBox_69.text()}\n')
        if self.checkBox_70.isChecked():  # Political conflicts and wars
            cb_70 = (f'{self.checkBox_70.text()}\n')
        if self.checkBox_71.isChecked():
            cb_71 = (f'{self.checkBox_71.text()}\n')  # Vandalism
        if self.checkBox_72.isChecked():
            cb_72 = (f'{self.checkBox_72.text()}\n')  # Abandonment
        if self.checkBox_73.isChecked():
            cb_73 = (f'{self.checkBox_73.text()}\n')  # Weathering
        if self.checkBox_77.isChecked():
            cb_77 = (f'{self.checkBox_77.text()}\n')  # Mass tourism
        if self.checkBox_78.isChecked():  # Inadequate interventions
            cb_78 = (f'{self.checkBox_78.text()}\n')
        if self.checkBox_79.isChecked():
            cb_79 = (f'{self.checkBox_79.text()}\n')  # Plundering
        if self.checkBox_80.isChecked():  # Unlawful appropriations
            cb_80 = (f'{self.checkBox_80.text()}\n')
        if self.checkBox_81.isChecked():
            cb_81 = (f'{self.checkBox_81.text()}\n')  # Humidity
        if self.checkBox_82.isChecked():
            cb_82 = (f'{self.textEdit_26.toPlainText()}')  # Others
        phcode_rirewoun_risks = (
            f'{cb_39}{cb_40}{cb_59}{cb_60}{cb_61}{cb_65}{cb_66}{cb_67}'
            f'{cb_68}{cb_69}{cb_70}{cb_71}{cb_72}{cb_73}{cb_77}{cb_78}'
            f'{cb_79}{cb_80}{cb_81}{cb_82}')
    phcode_rirewoun_com = self.textEdit_25.toPlainText()  # Comments


def reg_9_legal_information_and_management(self):
    """Registers data from tab '9': LEGAL INFORMATION AND MANAGEMENT."""

    global leinma_ow_ownreg, leinma_ow_ownercontde, leinma_ow_com
    global leinma_lest_levprot, leinma_lest_lawprot, leinma_lest_com
    global leinma_ma_authinst, leinma_ma_authistrespman, leinma_ma_manmodel
    global leinma_ma_dissmat, leinma_ma_maintprog, leinma_ma_com

    leinma_ow_ownreg, leinma_ow_ownercontde, leinma_ow_com = '', '', ''
    leinma_lest_levprot, leinma_lest_lawprot, leinma_lest_com = '', '', ''
    leinma_ma_authinst, leinma_ma_authistrespman = '', ''
    leinma_ma_manmodel, leinma_ma_dissmat, leinma_ma_maintprog = '', '', ''
    leinma_ma_com = ''

    # Ownership regime (affiliation):
    if self.radioButton_32.isChecked():  # Private
        leinma_ow_ownreg = self.radioButton_32.text()
    elif self.radioButton_33.isChecked():  # Public
        leinma_ow_ownreg = self.radioButton_33.text()
    elif self.radioButton_34.isChecked():  # Mixed
        leinma_ow_ownreg = self.radioButton_34.text()

    # Level of protection:
    if self.radioButton_35.isChecked():
        leinma_lest_levprot = self.radioButton_35.text()  # Uncatalogued
    elif self.radioButton_36.isChecked():
        leinma_lest_levprot = self.radioButton_36.text()  # Catalogued
    elif self.radioButton_37.isChecked():
        leinma_lest_levprot = self.radioButton_37.text()  # Medium
    elif self.radioButton_38.isChecked():
        leinma_lest_levprot = self.radioButton_38.text()  # High
    elif self.radioButton_39.isChecked():
        leinma_lest_levprot = self.radioButton_39.text()  # Maximum

    # Management model
    if self.radioButton_40.isChecked():  # Direct
        leinma_ma_manmodel = self.radioButton_40.text()
    elif self.radioButton_41.isChecked():  # Indirect
        leinma_ma_manmodel = self.radioButton_41.text()
    elif self.radioButton_42.isChecked():  # Other
        leinma_ma_manmodel = self.textEdit_14.toPlainText()

    # Owner of the element and contact details
    leinma_ow_ownercontde = self.textEdit_28.toPlainText()
    leinma_ow_com = self.textEdit_29.toPlainText()  # Comments
    # Laws that protect the element
    leinma_lest_lawprot = self.textEdit_6.toPlainText()
    leinma_lest_com = self.textEdit_30.toPlainText()  # Comments
    # Authorities/Institutions with competences over the element
    leinma_ma_authinst = self.textEdit_7.toPlainText()
    # Authority/Institution responsible for the management of the element
    leinma_ma_authistrespman = self.textEdit_8.toPlainText()
    # Dissemination materials
    leinma_ma_dissmat = self.textEdit_27.toPlainText()
    # Maintenance programs and tasks
    leinma_ma_maintprog = self.textEdit_9.toPlainText()
    leinma_ma_com = self.textEdit_31.toPlainText()  # Comments


def reg_10_uses_accessibility_and_management(self):
    """Register data from tab '10': USES, ACCESSIBILITY AND MANAGEMENT."""

    global usacma_us_oguse, usacma_us_curruse, usacma_us_muluse, usacma_us_com
    global usacma_ac_openpubvis, usacma_ac_workhour, usacma_ac_breaks
    global usacma_ac_workdays, usacma_ac_vacholcloday, usacma_ac_typvis
    global usacma_ac_onsiteacc, usacma_ac_com, usacma_loac_pubtrans
    global usacma_loac_dist, usacma_loac_com

    usacma_us_oguse, usacma_us_curruse, usacma_us_muluse = '', '', ''
    usacma_us_com, usacma_ac_openpubvis, usacma_ac_workhour = '', '', ''
    usacma_ac_breaks, usacma_ac_workdays, usacma_ac_vacholcloday = '', '', ''
    usacma_ac_typvis, usacma_ac_onsiteacc, usacma_ac_com = '', '', ''
    usacma_loac_pubtrans, usacma_loac_dist, usacma_loac_com = '', '', ''

    usacma_us_oguse = self.textEdit_51.toPlainText()  # Original use

    cb_128, cb_126, cb_129, cb_127, cb_130 = '', '', '', '', ''
    if self.checkBox_128.isChecked():               # Current use:
        cb_128 = (f'{self.checkBox_128.text()}\n')  # Original use
    if self.checkBox_126.isChecked():
        cb_126 = (f'{self.checkBox_126.text()}\n')  # Residential
    if self.checkBox_129.isChecked():
        cb_129 = (f'{self.checkBox_129.text()}\n')  # Unused
    if self.checkBox_127.isChecked():
        cb_127 = (f'{self.checkBox_127.text()}\n')  # Commercial
    if self.checkBox_130.isChecked():  # Other use
        cb_130 = (f'{self.checkBox_130.text()}: '
                  f'{self.textEdit_53.toPlainText()}')
    # Original use + Residential + Unused + Commercial + Other
    usacma_us_curruse = (f'{cb_128}{cb_126}{cb_129}{cb_127}{cb_130}')
    # There is more than one use
    if self.radioButton_81.isChecked():
        usacma_us_muluse = self.radioButton_81.text()  # No
    elif self.radioButton_80.isChecked():
        usacma_us_muluse = self.textEdit_54.toPlainText()  # Yes
    usacma_us_com = self.textEdit_52.toPlainText()  # Comments
    # Open for public visits
    if self.radioButton_70.isChecked():
        usacma_ac_openpubvis = self.radioButton_70.text()  # Yes
    elif self.radioButton_71.isChecked():
        usacma_ac_openpubvis = self.radioButton_71.text()  # No

    # Working hours
    if self.radioButton_115.isChecked():
        usacma_ac_workhour = self.radioButton_115.text()  # None
    elif self.radioButton.isChecked():
        usacma_ac_workhour = self.radioButton.text()  # Unknown
    elif self.radioButton_116.isChecked():
        usacma_ac_workhour = (
            (self.timeEdit_11.time().toString()) + '-' +
            (self.timeEdit_12.time().toString()))  # From...to
    # Breaks
    if self.radioButton_117.isChecked():
        usacma_ac_breaks = self.radioButton_117.text()  # None
    elif self.radioButton_2.isChecked():
        usacma_ac_breaks = self.radioButton_2.text()  # Unknown
    elif self.radioButton_118.isChecked():
        usacma_ac_breaks = (
            (self.timeEdit_15.time().toString()) + '-' +
            (self.timeEdit_16.time().toString()))  # From...to

    # Opening days
    cb_115, cb_116, cb_117, cb_118, cb_119 = '', '', '', '', ''
    cb_120, cb_121 = '', ''
    if self.radioButton_28.isChecked():
        usacma_ac_workdays = self.radioButton_28.text()  # Unknown
    elif self.radioButton_29.isChecked():               # Known
        if self.checkBox_115.isChecked():
            cb_115 = (f'{self.checkBox_115.text()}\n')  # Mon
        if self.checkBox_116.isChecked():
            cb_116 = (f'{self.checkBox_116.text()}\n')  # Tue
        if self.checkBox_117.isChecked():
            cb_117 = (f'{self.checkBox_117.text()}\n')  # Wed
        if self.checkBox_118.isChecked():
            cb_118 = (f'{self.checkBox_118.text()}\n')  # Thu
        if self.checkBox_119.isChecked():
            cb_119 = (f'{self.checkBox_119.text()}\n')  # Fri
        if self.checkBox_120.isChecked():
            cb_120 = (f'{self.checkBox_120.text()}\n')  # Sat
        if self.checkBox_121.isChecked():
            cb_121 = (f'{self.checkBox_121.text()}\n')  # Sun
        # Mon + Tue + Wed + Thu + Fri + Sat + Sun
        usacma_ac_workdays = (
            f'{cb_115}{cb_116}{cb_117}{cb_118}{cb_119}{cb_120}{cb_121}')
    # Vacation/Holydays/closing days: Registers data input by the user
    usacma_ac_vacholcloday = self.textEdit_48.toPlainText()

    # Types of visits
    cb_122, cb_123, cb_124, cb_125 = '', '', '', ''
    if self.radioButton_76.isChecked():
        usacma_ac_typvis = self.radioButton_76.text()  # Not open for use
    elif self.radioButton_79.isChecked():  # Open for public use
        if self.checkBox_122.isChecked():
            cb_122 = (f'{self.checkBox_122.text()}\n')  # Guided/scheduled
        if self.checkBox_123.isChecked():
            cb_123 = (f'{self.checkBox_123.text()}\n')  # Self-guided
        if self.checkBox_124.isChecked():
            cb_124 = (f'{self.checkBox_124.text()}\n')  # Special events
        if self.checkBox_125.isChecked():
            cb_125 = (f'{self.checkBox_125.text()}\n')  # Non-existent
        # Guided/scheduled + Self-guided + Special events + Non-existent
        usacma_ac_typvis = (
            f'{self.radioButton_79.text()}:\n{cb_122}{cb_123}{cb_124}{cb_125}')

    cb_32, cb_, cb_2, cb_3, cb_4, cb_8, cb_9 = '', '', '', '', '', '', ''
    cb_12, cb_27, cb_28, cb_30, cb_29, cb_33 = '', '', '', '', '', ''
    cb_31 = ''
    if self.checkBox_32.isChecked():
        cb_32 = (f'{self.checkBox_32.text()}\n')
    if self.checkBox.isChecked():
        cb_ = (f'{self.checkBox.text()}\n')
    if self.checkBox_2.isChecked():
        cb_2 = (f'{self.checkBox_2.text()}\n')
    if self.checkBox_3.isChecked():
        cb_3 = (f'{self.checkBox_3.text()}\n')
    if self.checkBox_4.isChecked():
        cb_4 = (f'{self.checkBox_4.text()}\n')
    if self.checkBox_8.isChecked():
        cb_8 = (f'{self.checkBox_8.text()}\n')
    if self.checkBox_9.isChecked():
        cb_9 = (f'{self.checkBox_9.text()}\n')
    if self.checkBox_12.isChecked():
        cb_12 = (f'{self.checkBox_12.text()}\n')
    if self.checkBox_27.isChecked():
        cb_27 = (f'{self.checkBox_27.text()}\n')
    if self.checkBox_28.isChecked():
        cb_28 = (f'{self.checkBox_28.text()}\n')
    if self.checkBox_30.isChecked():
        cb_30 = (f'{self.checkBox_30.text()}\n')
    if self.checkBox_29.isChecked():
        cb_29 = (f'{self.checkBox_29.text()}\n')
    if self.checkBox_33.isChecked():
        cb_33 = (f'{self.checkBox_33.text()}\n')
    if self.checkBox_31.isChecked():
        cb_31 = (f'{self.textEdit_49.toPlainText()}')
    # On-site accessibility
    usacma_ac_onsiteacc = (f'{cb_32}{cb_}{cb_2}{cb_3}{cb_4}{cb_8}{cb_9}{cb_12}'
                           f'{cb_27}{cb_28}{cb_30}{cb_29}{cb_33}{cb_31}')
    usacma_ac_com = self.textEdit_50.toPlainText()  # Comments

    # Means of transportation
    cb_114, cb_108, cb_109, cb_111, cb_113, cb_110 = '', '', '', '', '', ''
    cb_112 = ''
    if self.checkBox_114.isChecked():               # bus
        cb_114 = (f'{self.checkBox_114.text()}: '
                  f'N{self.lineEdit_106.text()}\n')
    if self.checkBox_108.isChecked():               # metro
        cb_108 = (f'{self.checkBox_108.text()}: '
                  f'N{self.lineEdit_107.text()}\n')
    if self.checkBox_109.isChecked():               # tram
        cb_109 = (f'{self.checkBox_109.text()}: '
                  f'N{self.lineEdit_113.text()}\n')
    if self.checkBox_111.isChecked():               # car
        cb_111 = (f'{self.checkBox_111.text()}\n')
    if self.checkBox_113.isChecked():               # bicycle
        cb_113 = (f'{self.checkBox_113.text()}\n')
    if self.checkBox_110.isChecked():               # foot
        cb_110 = (f'{self.checkBox_110.text()}\n')
    if self.checkBox_112.isChecked():               # other
        cb_112 = (f'{self.checkBox_112.text()}: '
                  f'{self.textEdit_46.toPlainText()}')
    usacma_loac_pubtrans = (
        f'{cb_114}{cb_108}{cb_109}{cb_111}'  # bus + metro + tram + car
        f'{cb_113}{cb_110}{cb_112}')  # bicycle + foot + other

    # Distance (m): from the nearest ...
    le_86, le_105, le_111, le_133 = '', '', '', ''
    if self.label.text().startswith('Ամսաթիվ'):
        meters = 'մ'
    else:
        meters = 'm'
    if self.checkBox_114.isChecked():                   # stop
        le_86 = (f'{self.checkBox_114.text()} - '
                 f'{self.lineEdit_86.text()}{meters}\n')
    if self.checkBox_108.isChecked():                   # station
        le_105 = (f'{self.checkBox_108.text()} - '
                  f'{self.lineEdit_105.text()}{meters}\n')
    if self.checkBox_109.isChecked():                   # station
        le_111 = (f'{self.checkBox_109.text()} - '
                  f'{self.lineEdit_111.text()}{meters}\n')
    if self.checkBox_111.isChecked():                   # parking station
        le_133 = (f'{self.checkBox_111.text()} - '
                  f'{self.lineEdit_133.text()}{meters}')
    # stop + station + station + parking station
    usacma_loac_dist = (f'{le_86}{le_105}{le_111}{le_133}')
    usacma_loac_com = self.textEdit_47.toPlainText()  # Comments


def reg_11_intrinsic_and_tourism_values(self):
    """Register data from tab '11': INTRINSIC AND TOURISM VALUES."""

    global intova_inva_histsign, intova_inva_histsign_r
    global intova_inva_artsign, intova_inva_artsign_r
    global intova_inva_socspirsign,  intova_inva_socspirsign_r
    global intova_inva_repr, intova_inva_repr_r, intova_inva_singl
    global intova_inva_singl_r, intova_inva_integ, intova_inva_integ_r
    global intova_inva_authen, intova_inva_authen_r, intova_inva_contex
    global intova_inva_contex_r, intova_inva_com, intva_tova_attr
    global intva_tova_attr_r, intva_tova_avlb, intva_tova_avlb_r
    global intva_tova_onstacc, intva_tova_onstacc_r, intva_tova_edva
    global intva_tova_edva_r, intva_tova_func, intva_tova_func_r
    global intva_tova_com

    intova_inva_histsign, intova_inva_histsign_r = '', ''
    intova_inva_artsign, intova_inva_artsign_r = '', ''
    intova_inva_socspirsign, intova_inva_socspirsign_r = '', ''
    intova_inva_repr, intova_inva_repr_r, intova_inva_singl = '', '', ''
    intova_inva_singl_r, intova_inva_integ = '', ''
    intova_inva_integ_r, intova_inva_authen = '', ''
    intova_inva_authen_r, intova_inva_contex = '', ''
    intova_inva_contex_r, intova_inva_com, intva_tova_attr = '', '', ''
    intva_tova_attr_r, intva_tova_avlb, intva_tova_avlb_r = '', '', ''
    intva_tova_onstacc, intva_tova_onstacc_r, intva_tova_edva = '', '', ''
    intva_tova_edva_r, intva_tova_func, intva_tova_func_r = '', '', ''
    intva_tova_com = ''

    # Historical significance
    if self.radioButton_120.isChecked():
        intova_inva_histsign = self.radioButton_120.text()  # 1
    elif self.radioButton_145.isChecked():
        intova_inva_histsign = self.radioButton_145.text()  # 2
    elif self.radioButton_151.isChecked():
        intova_inva_histsign = self.radioButton_151.text()  # 3
    elif self.radioButton_152.isChecked():
        intova_inva_histsign = self.radioButton_152.text()  # 4
    elif self.radioButton_153.isChecked():
        intova_inva_histsign = self.radioButton_153.text()  # 5
    intova_inva_histsign_r = self.textEdit_66.toPlainText()  # Reason

    # Artistical significance
    if self.radioButton_154.isChecked():
        intova_inva_artsign = self.radioButton_154.text()  # 1
    elif self.radioButton_155.isChecked():
        intova_inva_artsign = self.radioButton_155.text()  # 2
    elif self.radioButton_204.isChecked():
        intova_inva_artsign = self.radioButton_204.text()  # 3
    elif self.radioButton_205.isChecked():
        intova_inva_artsign = self.radioButton_205.text()  # 4
    elif self.radioButton_206.isChecked():
        intova_inva_artsign = self.radioButton_206.text()  # 5
    intova_inva_artsign_r = self.textEdit_67.toPlainText()  # Reason

    # Social or spiritual significance
    if self.radioButton_207.isChecked():
        intova_inva_socspirsign = self.radioButton_207.text()  # 1
    elif self.radioButton_208.isChecked():
        intova_inva_socspirsign = self.radioButton_208.text()  # 2
    elif self.radioButton_209.isChecked():
        intova_inva_socspirsign = self.radioButton_209.text()  # 3
    elif self.radioButton_210.isChecked():
        intova_inva_socspirsign = self.radioButton_210.text()  # 4
    elif self.radioButton_211.isChecked():
        intova_inva_socspirsign = self.radioButton_211.text()  # 5
    intova_inva_socspirsign_r = self.textEdit_70.toPlainText()  # Reason

    # Representativeness
    if self.radioButton_212.isChecked():
        intova_inva_repr = self.radioButton_212.text()  # 1
    elif self.radioButton_213.isChecked():
        intova_inva_repr = self.radioButton_213.text()  # 2
    elif self.radioButton_214.isChecked():
        intova_inva_repr = self.radioButton_214.text()  # 3
    elif self.radioButton_215.isChecked():
        intova_inva_repr = self.radioButton_215.text()  # 4
    elif self.radioButton_216.isChecked():
        intova_inva_repr = self.radioButton_216.text()  # 5
    intova_inva_repr_r = self.textEdit_82.toPlainText()  # Reason

    # Singularity
    if self.radioButton_217.isChecked():
        intova_inva_singl = self.radioButton_217.text()  # 1
    elif self.radioButton_218.isChecked():
        intova_inva_singl = self.radioButton_218.text()  # 2
    elif self.radioButton_224.isChecked():
        intova_inva_singl = self.radioButton_224.text()  # 3
    elif self.radioButton_225.isChecked():
        intova_inva_singl = self.radioButton_225.text()  # 4
    elif self.radioButton_226.isChecked():
        intova_inva_singl = self.radioButton_226.text()  # 5
    intova_inva_singl_r = self.textEdit_83.toPlainText()  # Reason

    # Integrity
    if self.radioButton_227.isChecked():
        intova_inva_integ = self.radioButton_227.text()  # 1
    elif self.radioButton_228.isChecked():
        intova_inva_integ = self.radioButton_228.text()  # 2
    elif self.radioButton_229.isChecked():
        intova_inva_integ = self.radioButton_229.text()  # 3
    elif self.radioButton_230.isChecked():
        intova_inva_integ = self.radioButton_230.text()  # 4
    elif self.radioButton_231.isChecked():
        intova_inva_integ = self.radioButton_231.text()  # 5
    intova_inva_integ_r = self.textEdit_84.toPlainText()  # Reason

    # Authenticity
    if self.radioButton_232.isChecked():
        intova_inva_authen = self.radioButton_232.text()  # 1
    elif self.radioButton_233.isChecked():
        intova_inva_authen = self.radioButton_233.text()  # 2
    elif self.radioButton_234.isChecked():
        intova_inva_authen = self.radioButton_234.text()  # 3
    elif self.radioButton_235.isChecked():
        intova_inva_authen = self.radioButton_235.text()  # 4
    elif self.radioButton_236.isChecked():
        intova_inva_authen = self.radioButton_236.text()  # 5
    intova_inva_authen_r = self.textEdit_87.toPlainText()  # Reason

    # Contextualisation
    if self.radioButton_237.isChecked():
        intova_inva_contex = self.radioButton_237.text()  # 1
    elif self.radioButton_238.isChecked():
        intova_inva_contex = self.radioButton_238.text()  # 2
    elif self.radioButton_239.isChecked():
        intova_inva_contex = self.radioButton_239.text()  # 3
    elif self.radioButton_240.isChecked():
        intova_inva_contex = self.radioButton_240.text()  # 4
    elif self.radioButton_241.isChecked():
        intova_inva_contex = self.radioButton_241.text()  # 5
    intova_inva_contex_r = self.textEdit_88.toPlainText()  # Reason

    # Comments: Additional comments. Registers data input by the user
    intova_inva_com = self.textEdit_89.toPlainText()

    # Attractiveness
    if self.radioButton_126.isChecked():                # 1
        intva_tova_attr = self.radioButton_126.text()
    elif self.radioButton_257.isChecked():              # 2
        intva_tova_attr = self.radioButton_257.text()
    elif self.radioButton_258.isChecked():              # 3
        intva_tova_attr = self.radioButton_258.text()
    elif self.radioButton_259.isChecked():              # 4
        intva_tova_attr = self.radioButton_259.text()
    elif self.radioButton_260.isChecked():              # 5
        intva_tova_attr = self.radioButton_260.text()
    intva_tova_attr_r = self.textEdit_94.toPlainText()  # Reason

    # Availability
    if self.radioButton_247.isChecked():                # 1
        intva_tova_avlb = self.radioButton_247.text()
    elif self.radioButton_248.isChecked():              # 2
        intva_tova_avlb = self.radioButton_248.text()
    elif self.radioButton_249.isChecked():              # 3
        intva_tova_avlb = self.radioButton_249.text()
    elif self.radioButton_250.isChecked():              # 4
        intva_tova_avlb = self.radioButton_250.text()
    elif self.radioButton_251.isChecked():              # 5
        intva_tova_avlb = self.radioButton_251.text()
    intva_tova_avlb_r = self.textEdit_91.toPlainText()  # Reason

    # On-site Accessibility
    if self.radioButton_261.isChecked():                # 1
        intva_tova_onstacc = self.radioButton_261.text()
    elif self.radioButton_262.isChecked():              # 2
        intva_tova_onstacc = self.radioButton_262.text()
    elif self.radioButton_263.isChecked():              # 3
        intva_tova_onstacc = self.radioButton_263.text()
    elif self.radioButton_264.isChecked():              # 4
        intva_tova_onstacc = self.radioButton_264.text()
    elif self.radioButton_265.isChecked():              # 5
        intva_tova_onstacc = self.radioButton_265.text()
    intva_tova_onstacc_r = self.textEdit_95.toPlainText()  # Reason

    # Educational values
    if self.radioButton_252.isChecked():                # 1
        intva_tova_edva = self.radioButton_252.text()
    elif self.radioButton_253.isChecked():              # 2
        intva_tova_edva = self.radioButton_253.text()
    elif self.radioButton_254.isChecked():              # 3
        intva_tova_edva = self.radioButton_254.text()
    elif self.radioButton_255.isChecked():              # 4
        intva_tova_edva = self.radioButton_255.text()
    elif self.radioButton_256.isChecked():              # 5
        intva_tova_edva = self.radioButton_256.text()
    intva_tova_edva_r = self.textEdit_92.toPlainText()  # Reason

    # Functionality
    if self.radioButton_242.isChecked():                # 1
        intva_tova_func = self.radioButton_242.text()
    elif self.radioButton_243.isChecked():              # 2
        intva_tova_func = self.radioButton_243.text()
    elif self.radioButton_244.isChecked():              # 3
        intva_tova_func = self.radioButton_244.text()
    elif self.radioButton_245.isChecked():              # 4
        intva_tova_func = self.radioButton_245.text()
    elif self.radioButton_246.isChecked():              # 5
        intva_tova_func = self.radioButton_246.text()
    intva_tova_func_r = self.textEdit_90.toPlainText()  # Reason

    # Comments: Additional comments. Registers data input by the user
    intva_tova_com = self.textEdit_93.toPlainText()


def reg_12_13_observations_bibliography(self):
    """Register data from tabs '12', and '13'."""

    global obadco, biotli
    obadco, biotli = '', ''

    # 12. OBSERVATIONS AND ADDITIONAL COMMENTS
    obadco = self.textEdit_5.toPlainText()
    # 13. BIBLIOGRAPHY AND OTHER LINKS
    biotli = self.textEdit_10.toPlainText()


def reg_14_graphical_documents(self, dir_doc, dir_img):
    """Register data from tab '14': GRAPHICAL DOCUMENTS."""

    fields = [
        inda_wcode, inda_date, inda_pldaco, inda_fname, inda_email,
        inda_conum, inda_com, idin_hestat, idin_hecert, idin_heceid,
        idin_hilev, idin_sign, idin_name, idin_otname, idin_com, vipr_im_1,
        vipr_imcap1, vipr_credit1, vipr_datetkn1, vipr_pltkn1, vipr_source1,
        vipr_im_2, vipr_imcap2, vipr_credit2, vipr_datetkn2, vipr_pltkn2,
        vipr_source2, vipr_com, loin_geloin_country, loin_geloin_provstate,
        loin_geloin_city, loin_geloin_dist, loin_geloin_strname,
        loin_geloin_strnum, loin_geloin_postco, loin_geloin_otlocdet,
        loin_coorpore_crs, loin_coorpore_authid, loin_coorpore_full_utm,
        loin_coorpore_utm, loin_coorpore_hemi, loin_coorpore_lat_band,
        loin_coorpore_eax, loin_coorpore_noy, loin_coorpore_com,
        mopra_mocota_por, mopra_mocota_monha, mopra_mocota_monsqm,
        mopra_prcota_prha, mopra_prcota_prsqm, mopra_prcota_com,
        tyeldeat_ty_categ, tyeldeat_ty_elem, tyeldeat_ty_com,
        tyeldeat_code_constdate, tyeldeat_code_cent, tyeldeat_code_archsty,
        tyeldeat_code_author, tyeldeat_code_storeys, tyeldeat_code_material,
        tyeldeat_code_phydescsett, tyeldeat_code_com, de_chre_reason,
        de_chre_histno, de_chre_descsh, de_chre_recogn, de_chre_com,
        phcode_inhere_currcond, phcode_inhere_com,
        phcode_inrewoun_retaudate, phcode_inrewoun_cent,
        phcode_inrewoun_alterf, phcode_inrewoun_alterr,
        phcode_inrewoun_alterd, phcode_inrewoun_alterw,
        phcode_inrewoun_alterl, phcode_inrewoun_alterb,
        phcode_inrewoun_alterc, phcode_inrewoun_altero,
        phcode_inrewoun_desc, phcode_inrewoun_rest,
        phcode_inrewoun_consstand, phcode_inrewoun_com,
        phcode_rirewoun_risks, phcode_rirewoun_com, leinma_ow_ownreg,
        leinma_ow_ownercontde, leinma_ow_com, leinma_lest_levprot,
        leinma_lest_lawprot, leinma_lest_com, leinma_ma_authinst,
        leinma_ma_authistrespman, leinma_ma_manmodel, leinma_ma_dissmat,
        leinma_ma_maintprog, leinma_ma_com, usacma_us_oguse,
        usacma_us_curruse, usacma_us_muluse, usacma_us_com,
        usacma_ac_openpubvis, usacma_ac_workhour, usacma_ac_breaks,
        usacma_ac_workdays, usacma_ac_vacholcloday, usacma_ac_typvis,
        usacma_ac_onsiteacc, usacma_ac_com, usacma_loac_pubtrans,
        usacma_loac_dist, usacma_loac_com, intova_inva_histsign,
        intova_inva_histsign_r, intova_inva_artsign, intova_inva_artsign_r,
        intova_inva_socspirsign, intova_inva_socspirsign_r,
        intova_inva_repr, intova_inva_repr_r, intova_inva_singl,
        intova_inva_singl_r, intova_inva_integ, intova_inva_integ_r,
        intova_inva_authen, intova_inva_authen_r, intova_inva_contex,
        intova_inva_contex_r, intova_inva_com, intva_tova_attr,
        intva_tova_attr_r, intva_tova_avlb, intva_tova_avlb_r,
        intva_tova_onstacc, intva_tova_onstacc_r, intva_tova_edva,
        intva_tova_edva_r, intva_tova_func, intva_tova_func_r,
        intva_tova_com, obadco, biotli
    ]
    self.iface.actionAddFeature().trigger()
    change_attribute_values(
        QgsProject.instance().mapLayersByName('Representative_Point')[0],
        fields)
    register_docs_attribute_table(self, 'Representative_Point', dir_doc)
    register_images_attribute_table(self, 'Representative_Point', dir_img)
    fill_blank_cells(self, 'Representative_Point')

    layer_names = ['Monument_Area', 'Protected_Area']
    for layer_name in layer_names:
        point_value, polygon_value, last_point_feature, _, polygon_layer =\
            self.check_attribute_equality(layer_name)
        # Check if the attribute values are the same
        # and if the last_point_feature exists
        if (last_point_feature is not None and
            point_value is not None and
                polygon_value is not None):
            if point_value == polygon_value:
                self.iface.actionAddFeature().trigger()
                change_attribute_values(polygon_layer, fields)
                register_docs_attribute_table(self, layer_name, dir_doc)
                register_images_attribute_table(self, layer_name, dir_img)
                fill_blank_cells(self, layer_name)
    QgsProject.instance().reloadAllLayers()
    self.iface.actionPan().trigger()


def register_images_attribute_table(self, layer_name, dir_img):
    """Register image information input in the added layouts."""

    layer = QgsProject.instance().mapLayersByName(layer_name)[0]
    layer.startEditing()
    # Initialize checkbox_index
    checkbox_index = None
    # Iterate over checkbox widgets and collect information
    checkbox_widgets_ = ImageLoader_1.get_checkbox_widget_list(
        self.verticalLayout_17)
    # If checkbox_widgets_ is empty
    if not checkbox_widgets_:
        pass
    else:
        for checkbox in checkbox_widgets_:
            # Extract the index from the checkbox name
            checkbox_index = int(checkbox.text().split('_')[1])
            # Find the corresponding QLineEdit and QTextEdit widgets
            layout = checkbox.parent().layout()
            # for the current layer
            line_edit_1 = ImageLoader_1.find_lineEdit_1(layout)
            line_edit_2 = ImageLoader_1.find_lineEdit_2(layout)
            line_edit_3 = ImageLoader_1.find_lineEdit_3(layout)
            line_edit_4 = ImageLoader_1.find_lineEdit_4(layout)
            line_edit_5 = ImageLoader_1.find_lineEdit_5(layout)
            line_edit_6 = ImageLoader_1.find_lineEdit_6(layout)
            text_edit_1 = ImageLoader_1.find_textEdit_1(layout)

            # Extract values from the widgets
            caption = line_edit_1.text()
            credit = line_edit_2.text()
            date_taken = line_edit_3.text()
            place_taken = line_edit_4.text()
            source = line_edit_6.text()
            image_path = line_edit_5.text()
            comments = text_edit_1.toPlainText()

            # img1 create a duplicate of the image in the new location and
            # store the image in the attribute table
            changeimagename_ = self.lineEdit.text() + '_' +\
                self.lineEdit_2.text() + '_' +\
                self.lineEdit_30.text() + '_' +\
                self.lineEdit_31.text() + '_oim_' + str(checkbox_index)
            if image_path:
                # Determine the file extension and rename accordingly
                img = 'png', 'jpg', 'jpeg', 'tiff', 'raw', 'jfif'
                if image_path.lower().endswith(img):
                    file_extension = (
                        '.' + image_path.split('.')[-1].lower())
                    changeimagename_ += file_extension
                dir_img_ = os.path.join(dir_img, changeimagename_)
                shutil.copyfile(image_path, dir_img_)
                vipr_im_ = dir_img_
            else:
                # Image N: Registers the image selected by the user
                if self.label.text().startswith('Ամսաթիվ'):
                    vipr_im_ = 'Տ․Բ․'
                elif self.label.text() == 'Date:':
                    vipr_im_ = 'N/A'
                elif self.label.text() == 'Fecha:':
                    vipr_im_ = 'N/D'
            ImageLoader_1.create_fields(
                self, layer, checkbox_index, vipr_im_, caption, credit,
                date_taken, place_taken, source, comments)
        layer.commitChanges()
        layer.updateFields()


def register_docs_attribute_table(self, layer_name, dir_doc):
    """Rename and create copies of documents attached to the project folder."""

    layer = QgsProject.instance().mapLayersByName(layer_name)[0]
    layer.startEditing()
    # Iterate over the items in the QTreeWidget
    docs = []
    for row in range(self.treeWidget.topLevelItemCount()):
        item = self.treeWidget.topLevelItem(row)
        # Get the item text in the 1st 4th and 5th columns
        if item is not None:
            name = item.text(0)  # Index of the 1st column
            note = item.text(3)  # Index of the 4th column
            path = item.text(4)  # Index of the 5th column
            changedocname_ = self.lineEdit.text() + '_' + \
                self.lineEdit_2.text() + '_' + \
                self.lineEdit_30.text() + '_' + \
                self.lineEdit_31.text() + '_-_' + str(name)
            source_path = path
            target_path = os.path.join(dir_doc, changedocname_)
            shutil.copyfile(source_path, target_path)
            if note != '':
                doc = str(f'{changedocname_} - {note}')
            else:
                doc = str(name)
            docs.append(doc)
    # Update fields with the retrieved values for each layer
    create_fields_docs(self, layer, docs)
    layer.commitChanges()
    layer.updateFields()


def create_fields_docs(self, layer, docs):
    """
    Add a column in the attribute table to store information about attached
    documents.
    """

    attribute_name = '14.grdo_docs'
    if layer.fields().indexFromName(attribute_name) == -1:
        # Attribute field doesn't exist, create it
        layer.addAttribute(QgsField(attribute_name, QVariant.String))
    # Get the last feature in the attribute table
    last_feature = None
    for feature in layer.getFeatures():
        last_feature = feature
    if last_feature:
        # Format the list items with new lines between them
        docs_text = '\n'.join(docs)
        # Update the attribute value of the last feature
        layer.changeAttributeValue(
            last_feature.id(),
            layer.fields().indexFromName(attribute_name),
            docs_text)


def fill_blank_cells(self, layer_name):
    "Set 'Null' or empty cells in the attribute table to 'N/A'."

    if self.label.text().startswith('Ամսաթիվ'):
        set_data = 'Տ․Բ․'
    elif self.label.text() == 'Date:':
        set_data = 'N/A'
    elif self.label.text() == 'Fecha:':
        set_data = 'N/D'
    # Get the layer
    layer = QgsProject.instance().mapLayersByName(layer_name)[0]
    # Start editing the layer
    layer.startEditing()
    # Get all features in the layer
    features = layer.getFeatures()
    for feature in features:
        # Iterate over each field
        for field in layer.fields():
            # Get the index of the field
            field_index = layer.fields().indexFromName(field.name())
            # Get the value of the field for the feature
            value = feature[field.name()]
            # Check if the value is blank or NULL
            if str(value).strip() == '' or str(value) == 'NULL':
                # Update the value to the specified value
                layer.changeAttributeValue(
                    feature.id(), field_index, set_data)
    layer.commitChanges()  # Commit changes to the layer
