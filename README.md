# Heritage Inventory Plugin
The Heritage Inventory Plugin (HIP) is a digital inventory worksheet that helps to create a digital database of heritage elements through simple input of spatial and non-spatial data. It is available in English, Spanish and Armenian. The Plugin forms a part of a PhD thesis.

## User Interface Design
Main Window consists of a ***Title bar***, ***Menu bar***, ***Body***, or ***Work area*** (Figure 1). The window is resizable; horizontal and vertical scroll bars appear as required. The `Worksheet Code` information stays stationary. Within the GUI, there are 12 tabs, each collecting information thematically. Navigating through tabs can be done either by directly clicking on desired tab or by using the black circular buttons positioned at the bottom of the Work area (![Screenshot 2024-06-22 184719](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/62f3d79a-fda9-4be3-b78a-85e958302bcb)) or using shortcuts: ***Ctrl+Alt+Shift+Z*** for going `Back` to the previous tab and ***Ctrl+Alt+Shift+X*** for going to the `Next` tub.
||
|-|
|![Picture1](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/4965e9ea-ee56-40b1-bb00-e69bf43c197c)|
|**Figure 1**. GUI of the Main Window. Title bar (red); Menu bar (blue); Body or Work area (orange)|



### 1. Menu bar
The Menu bar has three options: `File`, `Language` and `Get Started` (Figure 2, 3, 4).
The `File` Menu bar offers the user the following options (Figure 2):
-	![f1](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/159d4640-6254-4f5e-be45-83b99cad3715)
***Create a New Worksheet*** - Refreshes the main window, provides with a Blank Worksheet for a new project.
- ![f2](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/4d531288-6654-41c8-b78f-59c8ead8152e) ***Create a New Project*** – First asks the user to specify the desired location for creating the project file.
  - First, creates two subfolders:
    - ***Heritage_Docs*** - stores all the documents attached to the plugin,
    - ***Heritage_Images*** - stores all the images imported into the plugin.
  - Next, three geopackages are generated in the folder and their corresponding three layers are created in QGIS:
    - Two polygon layers that come with pre-defined labels and styles:
      - ***Protected_Area*** - stores the polygon layer of the protected area,
      - ***Monument_Area*** - stores the area of the monument).
    - One point layer registering a single (representative) point of the heritage element (***Representative_Point***).
> [!IMPORTANT]
> To avoid possible errors, the full path to the folder where the project will be saved should not contain spaces. The spaces in the names should be replaced, for example, with an underscore (_).
- ![f3](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/4d81d545-96e4-483d-8a2c-fe8c2e284c00) ***Save the project*** – Asks the user to select the location to save the project and specify the file extension (either `*.qgs` or `*.qgz`).
- ![f4](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/51711c2a-1839-4254-ac0d-c4ebf9dc854a) ***Export to Excel*** – Exports all attribute les from the three layers into a single MS Excel `*.xlsx` file. The program creates three workbooks, each containing a single attribute table.
- ![f5](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/103d84e8-532b-4c16-a465-b8d8a67225a6) ***Open project*** – Askes to select an existing project.

The `Language` Menu bar includes Armenian (Eastern), English (British), and Spanish (Castilian) (Figure 3). After choosing the desired language, a confirmation message will appear, as switching the language may result in data loss.

The `Get Started` Menu bar offers a step-by-step introduction for first-time users to ensure a smooth experience (Figure 4):
  
  ||||
  |-|-|-|
  |![Picture16](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/562f6086-2e59-458c-aeaa-4ea159d6eb13)|![Picture17](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/b736914e-c945-48f4-8ad9-e2d2759cc537)|![Picture19](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/9927aac3-e285-491f-9972-eb0d27f28d8f)|
  |**Figure 2**. The contents of the HIP File Menu bar|**Figure 3**. The contents of the HIP Language Menu bar|**Figure 4**. The contents of the HIP Get Started Menu bar|
 
- ***Step 1***: Base Map (Figure 5) – to ensure the accurate projection of heritage elements in QGIS, the project's Coordinate Reference System (CRS) must match that of the chosen base map. Therefore, users should first select a base map (ideally the Open Street Maps) and then restart the plugin (and/or create a new project).
- ***Step 2***: Select CRS (Figure 6) – the CRS should be selected which can be done by clicking on the first button from the left called `Select CRS` (Figure 6).
  
  |||
  |-|-|
  |![S1](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/988cd0ec-eed8-4111-ab96-fab801ea94f8)|![S2](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/38a55723-114e-42a0-a589-c0ce74c7048c)|
  |**Figure 5**. Step 1: Select a base map|**Figure 6**. Step 2: Select the CRS|

- ***Step 3***: Create New Project (Figure 7) – Navigate to the `File` ► `New Project`.
- ***Step 4***: New Worksheet (Figure 8) – A New Worksheet should be created to register a new heritage element. If the previous steps were not completed or the program does not detect the specific geopackage layers, it will ask the user to create or open an existing project and then proceed to fill out a New Worksheet. If the previous steps are completed, the program will ask the user to specify the project folder’s location.
  
  |||
  |-|-|
  |![S3](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/05f65b4d-470c-4518-bca0-c505aa89cde7)|![S4](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/3ac3d473-08e4-4fc7-ab6b-c17d5543635e)|
  |**Figure 7**.Step 3: Create a New Project|**Figure 8**. Step 4: Open a New Worksheet|

- ***Step 5***: Fill out the Worksheet (Figure 9) – The user should go through each field, introducing the requested information or selecting the correct option from the provided choices. Some data fields have specific character requirements; for example, the field requesting the data compiler's contact number only permits numbers.
- ***Step 6***: Register and save (Figure 10) – A Blank Worksheet has several greyed areas that become enabled only when specific options are selected. To register the Worksheet, the minimum necessary information to be filled in is the registry of the coordinates of the Point of Reference. Once all the required fields are filled, the user can click the `Register` button to record all data from the Worksheet into the attribute tables of the three layers, except for the data in tables containing the coordinates of the monument and protected areas. Next, the program will ask the user to choose where to save the project, select the project's data type (`*.qgs or *.qgz`), and specify the location and name of the `*.xls` MS Excel file for storing the coordinates of the monument area and protected zone.
   
  |||
  |-|-| 
  |![S5](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/a39f3e53-8d69-4fe4-ada9-31276d2e485b)|![S6](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/8adbf088-a8e9-4528-965c-edc4a38dd328)|
  |**Figure 9**. Step 5: Fill out the Worksheet|**Figure 10**. Step 6: Register the heritage Element and save the project|

Many Worksheets can be filled out within the same project file depending on the number of heritage elements that should be registered. Therefore, steps 4 to 6 can be repeated as often as needed.



### 2. Work area
#### Worksheet code
||
|-|
|![Picture21](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/c3f7c032-6fb5-4d61-a2a5-5f621c0bf5b8)|
|**Figure 11**. Worksheet code|

The Worksheet Code serves as a unique identifier, ensuring easy reference to the Worksheet at a later stage. It is recommended to structure this identifier as follows: ***AAA_BBB_CCC_yyyymmdd***. The fields are organized in the following way (Figure 11):
  - **AAA** - shortened designations of a city - accepts symbols only, with no limit on the number of characters,
  - **BBB** - shortened designations of a district - accepts symbols only, with no limit on the number of characters,
  - **CCC** - variable Worksheet Number - accepts only numerals, with a maximum of three characters (000-999)
  - **yyyymmdd** - date (all four digits of the year when the Worksheet was completed, the month (01-12), and the day (01-31)) - accepts only numerals up to six characters

This format ensures that the old and the new worksheets, as well as their associated materials (documents and images) are organized in an orderly manner.
> [!NOTE]
> The final version of the worksheet code will serve as an identification number and will be part of the renamed versions of the documents and images copied to the ***Heritage_Docs*** and ***Heritage_Images*** folders.



#### Tab 1: Sections 1-3. Inspection data, Identification Information, Visual presentation
||
|-|
|![Picture22](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/89d51c3c-61f7-4dea-a9e1-449bf578c06d)|
|**Figure 12**. Inspection data; Identification Information|

1. ***Inspection data*** – comprises seven data fields designed to capture information regarding the inspection day, including details about when, where, and by whom the data was gathered.
  When specifying the contact number, it is essential to provide the phone number prefix separately from the main number. If the data compiler wishes to include multiple email addresses or contact numbers, such information can be accommodated in the comments section.
2. ***Identification information*** – encompasses a set of interconnected questions aimed at establishing the identity of the heritage element and connecting it to existing official documents. In cases where the element has no heritage status or a corresponding heritage certificate, it does not possess a previous identification. Recognising this, the program will automatically designate the `Does not have a certificate` option in the `Heritage Certificate` data field and set the `Heritage Certificate ID` to `None`.
3. ***Visual presentation*** – This section is intended to illustrate how the heritage element has evolved compared to its original state. It primarily consists of two components. On the left-hand side, users can select a recent image of the heritage element and provide associated data. The image chosen for the right-hand side should ideally depict the heritage element in its initial state. When clicking the `Browse` button, the program asks to choose the relevant image from computer. These selected images will be displayed within an empty container to the right of the `Browse` button. If an incorrect image was chosen, the `Clear` button will remove it.
Each file is expected to have a descriptive caption for easy identification. Furthermore, due recognition must be given to the authors of the images. The date and the specific location of document/file preparation are also obligatory details to be provided.

    ||
    |-|
    |![Picture23](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/f76a5b5e-3ba8-4297-baca-40917e1dcfc6)|
    |**Figure 13**. Visual presentation|



#### Tab 2: Section 4. Location information
||
|-|
|![Picture3](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/59398585-1ee5-4018-952c-3fa77fdd96ce)|
|**Figure 14**. Tab 2: Section 4. Location information of the heritage element. General location information (red); Coordinates of the point of reference (blue)|

- 4.1. ***General Location Information*** - general location information for the heritage element (Figure 14). Some data fields do not permit the input of numerical values.
- 4.2. ***Coordinates of the Point of Reference*** - recording a Point of Reference (POR) for the heritage element. It is suggested that the Coordinate Reference System (CRS) of all the layers and the project is set to Web Mercator projection, which can be accomplished by clicking the yellow button.

The POR can be registered in two ways: either directly on the map or by entering the coordinates. To register it directly on the map, users should click the `Register on map` button, which will temporarily hide the main window. Users should then perform a left click at the desired location on the map. The program will record the point on the map and in the attribute table and display the main window. The Standard UTM coordinates of the POR (Including the UTM Zone, latitude band, hemisphere, and easting and northing coordinates) will be recorded in their respective data fields. In the event that the user selects a point within the Y, Z, A or B zones (Figure 15), the Universal Polar Stereographic (UPS) coordinates of the point will be registered in the Comments section.

If the coordinates details of the POR are known, they can be input directly into the corresponding data fields and then the `Add` button should be pressed. The data needed includes specifying the `UTM Zone` (0-60), the `Latitude band` (C, D, E, F, G, H, J, K, L, M, N, P, Q, R, S, T, U, V, W or X), the `Hemisphere` (Northern or Southern), and the `Easting` and `Northing` coordinates. It should be noted that, given that no zones `32, 34, or 36` exist within the `X` latitude band, the plugin will either grey out the `X` option in the `Latitude band` combo box when the user inputs `32, 34, or 36` in the UTM zone, or will not permit the user to input these zones when the `X` option in the `Latitude band` is selected first.

||
|-|
|![Figures1](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/786019a1-a717-4641-8088-98e44a094240)|
|**Figure 15**. UTM Zones , Hemispheres (Western and Eastern), Latitude bands and Hemispheres (Northern and Southern) on the World Map with Web Mercator Projection (EPSG:3857). Source: own elaboration|.

As soon as the point is registered (either by the mouse click or by the data input) the `Add` button will be automatically disabled to prevent the same point from being registered twice. In the event that incorrect coordinates have been entered, the point can be replaced by a new one by `Registering on the map` option. The incorrect coordinates could also be removed by clicking on the `Remove` button. This will result in data fields being cleared and the point being removed from the map and attribute table. By default, the `Remove` button is disabled to prevent the erroneous deletion of any previously registered POR. However, as soon as a new POR is registered (either by the mouse click or by the data input), the button becomes enabled to help rectify any mistakes.
> [!IMPORTANT]
> The POR will also be recorded as the initial entry in both tables within `Tab 3: Section 5`, identified as ***point A***. Consequently, the removal of the POR will result in the elimination of all data within these tables.This will imply the deletion of any polygons registered in the current worksheet.
> 
> If the POR is invisible after changing the CRS, following the initial step outlined in the `Get Started` Menu Bar is recommended.



#### Tab 3: Section 5. Monument area and Protected zone
||
|-|
|![Picture4](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/f1e635db-6c78-454d-b523-e1f606824ca6)|
|**Figure 16**. Tab 3: Section 5. Monument area and Protected zone. Spatial data of the Monument area (red); Spatial data of the Protected zone (blue); additional section (orange)|

The tab is initially disabled and becomes active only after the POR has been selected in the previous tab.

The sections can be activated by clicking the checkboxes.

In this tab, the first two sections serve similar purposes, with the first one used for registering the area of the monument and the second for registering the protected zone (Figure 16). Both sections offer three methods for registration: drawing the area on the map, providing the coordinates of the edges, importing coordinates with MS Excel file. The buttons and functionalities are identical in both subsections for both registration methods.
-	The user can select the `Draw on the map` option to draw the area on the map. This action temporarily hides the main window, allowing the user to outline the polygon's edges by left-clicking on the map. After all edges are registered, the mouse should be moved away from the polygon; a right-click on the map will reveal the polygon and the main window. The coordinates are recorded in the order in which they were clicked on the map, and the edges are numbered while the segments are specified. The program calculates the distances between segments in meters. The `Zone` column registers the Hemisphere (N for Northern, S for Southern), the UTM zone and the latitude band. The last two data entries in the table are the Easting and Northing coordinates. The program also calculates the monument area in hectares and square meters.
-	The coordinates can also be added one by one by clicking the `Add a row` button. A dialog box will pop up (Figure 17) asking users to enter the coordinate details in the same way as in `Tab 2 Section 4.2`. If additional points need to be incorporated, this process can be repeated as many times as required. All the newly added points will appear at the bottom of the list. The last point should be added by selecting the `Add and Finish` button. The program will auto-populate the empty fields within the `Edge`, `Segment`, `Distance`, `Zone`, `Easting` and `Northing` columns. Then, a polygon will be constructed on the map, simultaneously creating an item in the attribute table.

    ||
    |-|
    |![Picture24](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/7aaa4db8-89cf-4ec4-b962-1bc0e11b5b2a)|
    |**Figure 17**. Dialog box that records data entered by the user and then stores it in the table|

    In the case where a user mistakenly selects or enters a point, it can be deleted by selecting the desired row and clicking `Delete a row` button. This action prompts the program to delete the previously created polygon and generate a new one with the updated coordinate list. Similar steps apply if the user wants to change the order of a point by moving a row up via `Move up` button or down via `Move down` button. The user can click the `Clear all rows` button to clear all data from the table and delete the polygon.
-	If the list of the coordinates is available in the Excel sheet, the list can be imported to the table using the `Import data from MS Excel file` button. The program provides specific steps to follow for a smooth and error-free import (Figure 18).

    ||
    |-|
    |![Picture25](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/a2557e3a-b689-438a-bd98-3544bf619303)|
    |**Figure 18**. Instructions specifying the correct way of importing coordinates into a table from an Excel file|

> [!IMPORTANT]
> The first row in both tables is reserved for the POR, labelled as `A`. This row cannot be altered, edited, or deleted. To change the Point of Reference, the user should follow the instructions in Tab 2. Any change in the POR will result in erasure of data in the tables.

The `Numbering` data label in both tables facilitates the visualisation of the polygon edges' numbering on the map. The numbering is hidden by default. However, clicking the `Show` button allows users to switch between `Light` and `Dark` modes for visualizing the edges.

Once both subsections are completed, the tables can be exported as `*.xls` files by clicking the `Export Tables to MS Excel` button.

After selecting the POR, a default text is generated in the `Point of Reference` data field. Here, additional information should be provided and any other pertinent details.



#### Tab 4: Section 6. Type of the element and description of its attributes
||
|-|
|![Picture6](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/a622525c-be1f-4715-ae56-d93524b45995)|
|**Figure 19**. Tab 3: Section 6. Type of the element and description of its attributes. Typology of the element (red); Construction details (blue)|

-	6.1. ***Typology*** - The user is presented with a drop-down list from which the appropriate Category and Element typology can be selected to classify the heritage element (Figure 19). In the event that the desired options are not available in the lists, additional entries can be input into the respective `Other` fields. Whenever the user selects the `Other` option, the items previously chosen from the main category and element drop-down list are cleared. Conversely, selecting an item from the category drop-down list deselects the `Other` option.
-	6.2. ***Construction Details*** - Some data fields are disabled by default and could be activated by selecting the corresponding options. For instance, if the architect of the heritage building is identified, the `Known` option should be selected, which will enable additional data fields in the `Author-position` section. In the event that the heritage building comprises more than five storeys, the user can specify the exact number after clicking the `more` button to enable the relevant data field.



#### Tab 5: Section 7. Justification for Protection
||
|-|
|![Picture7](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/3ce19ca2-9334-43d0-9eeb-e20d9fc6209e)|
|**Figure 20**. Tab 4: Section 7. Justification for protection |

Given the diverse possible reasons for designation (Figure 20), users have the flexibility to select multiple answers, as well as the option to add their own. The remaining data fields require textual information. If any bibliographical sources were referenced, they should be accurately credited in Tab 13.



#### Tab 6: Section 8. Physical condition and Conservation details
||
|-|
|![Picture8](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/7b44c496-754a-4d04-925a-8e90b4959db0)|
|**Figure 21**. Tab 6: Section 8. Physical condition and conservation details. Integrity of the heritage element (red); Interventions and restoration work undertaken (blue); Risks and threats (orange)|

A significant portion of the data fields in this tab are initially disabled and require affirmative selections by the user to enable them (Figure 21). For example, in Section 8.2, if the user wishes to specify that two floors have been added, and that three windows have been removed, the corresponding checkboxes should be marked and additional data should be entered (e.g., the number of windows, on which floor, etc.). It is imperative to ensure that the corresponding checkboxes are duly selected so that the entered information can be accurately registered in the attribute table.



#### Tab 7: Section 9. Legal information and Management
||
|-|
|![Picture9](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/ed8a988f-4cdb-4775-ac58-44cccb053d1a)|
|**Figure 22**. Tab 7: Section 9. Legal Information and Management. Ownership of the element (red); Legal status (blue); Management (orange)|

The structure of the questions and options in this tab is direct, requiring selection from provided options or input descriptive text (Figure 22). In the `Dissemination materials` data field, users are expected to describe the materials, and if visual materials are included, they should be attached in the last tab (Section 14).



#### Tab 8: Section 10. Uses and accessibility
||
|-|
|![Picture10](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/1baa12ec-8a8f-4d39-961c-7aeb9282560f)|
|**Figure 23**. Tab 8. Section 10. Uses and accessibility. Uses of the element (red); Accessibility (blue); Local Accessibility (orange)|

First, the uses of the element should be specified (Figure 23). Should the current use of the heritage element not be represented within the list of choices for current uses provided in the Worksheet, the appropriate action will be to select the `other uses` option, which will enable the space where the current use can be specified.
Subsequently, the user is required to complete the section regarding the accessibility of the element. Only information that is available or known should be included. If any specific information is unknown, the `N/A` option must be chosen to indicate the absence of data.



#### Tab 9: Section 11. Intrinsic and Tourism values
||
|-|
|![Picture11](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/79cfeebb-a04d-4266-96ea-1db7cce332c5)|
|**Figure 24**. Tab 9: Section 11. Intrinsic and tourism values. Intrinsic value (red); Tourism value (blue)|

The present section comprises two subsections (Figure 24), where the user is asked to evaluate the intrinsic and tourism values of the heritage element using an ascending scale from 1 to 5. The explanations of the criteria are provided for reference. In addition to assigning a rating, the user is required to specify the reason for the chosen rating; when the assigned rating deviates from 5, it is necessary to specify the particular rationale behind the rating.



#### Tab 10: Section 12. Observations and Additional comments
||
|-|
|![Picture12](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/caec24f3-1706-4123-8e67-7bc92efd2b8f)|
|**Figure 25**. Tab.10: Section 12. Observations and additional comments|

This section (Figure 25) is designated for including any observations, remarks, or comments that have not been accommodated elsewhere in the Worksheet.



#### Tab 11: Section 13. Bibliography and Other links
||
|-|
|![Picture13](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/b58f96cf-0c8c-484f-be52-0d2e671f549b)|
|**Figure 26**. Tab 11. Section 13. Bibliography and other links|

This section (Figure 26) serves as a repository for all bibliographic references cited in the Worksheet, as well as any associated bibliography or hyperlinks. The bibliography should be enumerated systematically and referenced appropriately both throughout the worksheet and in the current section.



#### Tab 12: Section 14. Graphical documents (photographs, maps, leaflets, etc.)
||
|-|
|![Picture14](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/7be7a4eb-5d36-41fa-9613-11824fad8583)|
|**Figure 27**. Tab 12: Section 14. Graphical documents (photographs, maps, leaflets, etc.). Documents (red); Images (blue)|

In the final tab (Section 14) two subsections are dedicated to the inclusion of graphic documents and visual material, as shown in Figure 27.
-	14.1. ***Documents*** - Any file can be attached by clicking the `Add Items` button. If a file is added by mistake, it can be removed by ticking the checkboxes to select the file to be removed and clicking the `Remove Item` button. The plugin automatically records the name, type, size and path of each uploaded file. The only editable column is the `Notes` column, where users are encouraged to provide additional remarks or comments about the content of each document or its relevance to the cultural heritage resource.
-	14.2. ***Images*** - To upload additional images to the plugin, the `Add Container` button should be clicked. This action adds a container, shown in Figure 28, with an interface identical to that described in Section 3. To remove a container, users should tick the checkboxes of the appropriate container (located in the top left corner) and click the `Remove Container` button.
The documents and images uploaded to the plugin are renamed based on the Worksheet Code and the corresponding item/container number. To illustrate, if the user uploads three documents and five images, the following process will occur: the documents and images are copied to designated folders, ***Heritage_Docs*** and ***Heritage_Images***, respectively. If the Worksheet Code is ***a_b_c_d***, the third document will be renamed ***a_b_c_d_-_original_name***, and the fifth image will be renamed ***a_b_c_d_im_5***. The image extension will remain unchanged.
> [!NOTE]
> If no supplementary visual materials are attached, no containers should be added.

||
|-|
|![Picture15](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/973ef463-93e6-4403-8d12-a409b6104230)|
|**Figure 28**. The interface of the containers for registering additional images|



#### Register button
![Picture20](https://github.com/ansa16a/qgis-heritage-inventory-plugin/assets/163760360/136e0b47-24d0-4f50-88b8-6f84bb0c09c4) The button is disabled by default. Once a Point of Reference has been added to the map, the button will become enabled.

When the button is pressed, the user is asked to specify the location where project will be saved and register the data from all data fields to the corresponding fields in the attribute table. The coordinates of the monument and protected area are exported to Excel format, and users will be asked to provide a name for the file. All uploaded documents and images will be renamed and stored in the corresponding folder.
> [!NOTE]
> The attribute table does not, by default, include columns for documents or images. The program dynamically creates a column for documents and adds columns for images based on the number of container added to the plugin. Upon adding a single container, the program will create as many columns as are necessary to register the user-provided information.
> 
> Any missing required data will be substituted with ***N/A*** in the attribute table by the plugin.
