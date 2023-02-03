# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb 26 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

tFileNew = 1000
tFileNewGeomorph = 1001
tFileOpen = 1002
tFileOpenGeomorph = 1003
tFileSave = 1004
tFileSaveAs = 1005
tPrintMap = 1006
tExportImage = 1007
tEditUndo = 1008
tImportTileset = 1009
tImportBackground = 1010
tTileQuantity = 1011
tSnapToGrid = 1012
tShowGrid = 1013
tShowBackground = 1014
tShowLayerFilter = 1015
tShowIcons = 1016
tShowLabels = 1017
tShowDrawingObjects = 1018
tShowDrawingHandles = 1019
tShowFogObjects = 1020
tZoomIn = 1021
tZoomOut = 1022
tHelp = 1023
mFileNew = 1024
mFileNewGeomorph = 1025
mFileOpen = 1026
mFileOpenGeomorph = 1027
mFileSave = 1028
mFileSaveAs = 1029
mFileImportFile = 1030
mFileImportBackground = 1031
mFileRecentFile1 = 1032
mFileRecentFile2 = 1033
mFileRecentFile3 = 1034
mFileRecentFile4 = 1035
mFileRecentFile5 = 1036
mFileExit = 1037
mEditUndo = 1038
mEditCut = 1039
mEditCopy = 1040
mEditPaste = 1041
mEditSelectAll = 1042
mEditMapSize = 1043
mTilesetCreateMaster = 1044
mTilesetCreateResolution = 1045
mTilesetEdit = 1046
mTilesetBrowser = 1047
mPrintMap = 1048
mPrintImage = 1049
mPrintChangeResolution = 1050
mViewGrid = 1051
mViewFilterTags = 1052
mViewBackground = 1053
mViewGridCoordinates = 1054
mViewHighlightIcons = 1055
mViewDualTileDisplay = 1056
mViewOutlineTiles = 1057
mShowIconNamesOnMap = 1058
mViewZoomIn = 1059
mViewZoomOut = 1060
mViewViewAll = 1061
mViewViewTilesetLayerFilter = 1062
mViewSecondaryScreen = 1063
mViewUpdateToFTP = 1064
mViewUpdateFog = 1065
mOptionsProgram = 1066
mOptionsTilesets = 1067
mOptionsSymbolsMarkers = 1068
mOptionsText = 1069
mOptionsSelectMode = 1070
mOptionsInifile = 1071
mOptionsFTP = 1072
mMapsRandomDungeon = 1073
mReportsManifest = 1074
mReportsTilesets = 1075
mDungeonLoadD20Files = 1076
mDungeonLoadDnD5Files = 1077
mDungeonNPCGenerator = 1078
mDungeonMonster = 1079
mDungeonMonster5E = 1080
mDungeonNPC_5E = 1081
mDungeonSpell_5E = 1082
mDungeonEncounters = 1083
mDungeonTraps = 1084
mDungeonTreasures = 1085
mDungeonCombatTracking = 1086
mDungeonDiceRoller = 1087
mDungeonShowIcons = 1088
mDungeonPathfinderMagicItems = 1089
mDungeonPathfinderMonsters = 1090
mDungeonD20Spells = 1091
mDungeonD20Feats = 1092
mDungeonAbout = 1093
mHelpContents = 1094
mHelpOpenTutorial = 1095
mHelpShowTips = 1096
mHelpKeyboardShortcuts = 1097
mHelpProgramFoundation = 1098
mHelpRegisterProgram = 1099
mHelpAbout = 1100
tCloseID = 1101
tOpenID = 1102
tSaveID = 1103
tUndoID = 1104
tRedoID = 1105
tCutID = 1106
tCopyID = 1107
tPasteID = 1108
tBoldID = 1109
tItalicID = 1110
tUnderlineID = 1111
tLeftJustifyID = 1112
tCenterJustifyID = 1113
tRightJustifyID = 1114
tChangeFontID = 1115
tChangeColorID = 1116
EditDescriptionID = 1117
NPC_menuID = 1118
Monster_menuID = 1119
NPC5E_menuID = 1120
Monster5E_menuID = 1121
Trap_menuID = 1122
Treasure_menuID = 1123
roomID = 1124
monsterID = 1125
trapID = 1126
npcID = 1127
treasureID = 1128
markerID = 1129
p1Dead = 1130
p1Action = 1131
p1HP = 1132
p1Name = 1133
p1Init = 1134
p1Order = 1135
p1Delay = 1136
p1Ready = 1137
p2Dead = 1138
p2Action = 1139
p2HP = 1140
p2Name = 1141
p2Init = 1142
p2Order = 1143
p2Delay = 1144
p2Ready = 1145
p3Dead = 1146
p3Action = 1147
p3HP = 1148
p3Name = 1149
p3Init = 1150
p3Order = 1151
p3Delay = 1152
p3Ready = 1153
p4Dead = 1154
p4Action = 1155
p4HP = 1156
p4Name = 1157
p4Init = 1158
p4Order = 1159
p4Delay = 1160
p4Ready = 1161
p5Dead = 1162
p5Action = 1163
p5HP = 1164
p5Name = 1165
p5Init = 1166
p5Order = 1167
p5Delay = 1168
p5Ready = 1169
p6Dead = 1170
p6Action = 1171
p6HP = 1172
p6Name = 1173
p6Init = 1174
p6Order = 1175
p6Delay = 1176
p6Ready = 1177
p7Dead = 1178
p7Action = 1179
p7HP = 1180
p7Name = 1181
p7Init = 1182
p7Order = 1183
p7Delay = 1184
p7Ready = 1185
p8Dead = 1186
p8Action = 1187
p8HP = 1188
p8Name = 1189
p8Init = 1190
p8Order = 1191
p8Delay = 1192
p8Ready = 1193
p9Dead = 1194
p9Action = 1195
p9HP = 1196
p9Name = 1197
p9Init = 1198
p9Order = 1199
p9Delay = 1200
p9Ready = 1201
p10Dead = 1202
p10Action = 1203
p10HP = 1204
p10Name = 1205
p10Init = 1206
p10Order = 1207
p10Delay = 1208
p10Ready = 1209
p11Dead = 1210
p11Action = 1211
p11HP = 1212
p11Name = 1213
p11Init = 1214
p11Order = 1215
p11Delay = 1216
p11Ready = 1217
p12Dead = 1218
p12Action = 1219
p12HP = 1220
p12Name = 1221
p12Init = 1222
p12Order = 1223
p12Delay = 1224
p12Ready = 1225
p13Dead = 1226
p13Action = 1227
p13HP = 1228
p13Name = 1229
p13Init = 1230
p13Order = 1231
p13Delay = 1232
p13Ready = 1233
p14Dead = 1234
p14Action = 1235
p14HP = 1236
p14Name = 1237
p14Init = 1238
p14Order = 1239
p14Delay = 1240
p14Ready = 1241
p15Dead = 1242
p15Action = 1243
p15HP = 1244
p15Name = 1245
p15Init = 1246
p15Order = 1247
p15Delay = 1248
p15Ready = 1249
skAcrobatics = 1250
skAnimalHandling = 1251
trCreatureSpellListID = 1252
trAllSpellListID = 1253
Setup_ImageListBox = 1254
Setup_ImageA = 1255
Setup_ZoomInA = 1256
Setup_ZoomOutA = 1257
Setup_ImageB = 1258
Setup_ZoomInB = 1259
Setup_ZoomOutB = 1260
Setup_TilesetBox = 1261
Setup_RemoveTile = 1262
Tileset_TilesetBox = 1263
Tileset_ZoomInA = 1264
Tileset_ZoomOutA = 1265
Tileset_SideAGridColor = 1266
Tileset_ZoomInB = 1267
Tileset_ZoomOutB = 1268
Tileset_SideBGridColor = 1269
ID_OK = 1270
ID_CANCEL = 1271
idxBlinded = 1272
idxCharmed = 1273
idxConcentrating = 1274
idxDeafened = 1275
idxFrightened = 1276
idxGrappled = 1277
idxIncapacitated = 1278
idxInvisible = 1279
idxParalyzed = 1280
idxPetrified = 1281
idxPoisoned = 1282
idxProne = 1283
idxRestrained = 1284
idxStunned = 1285
idxTurned = 1286
idxUnconscious = 1287

###########################################################################
## Class PyMapperFrameCore
###########################################################################

class PyMapperFrameCore ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PyMapper", pos = wx.DefaultPosition, size = wx.Size( 1023,441 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.Size( -1,-1 ), wx.DefaultSize )
		
		self.toolbar = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY )
		self.toolbar.SetToolBitmapSize( wx.Size( 20,20 ) )
		self.toolbar.SetToolSeparation( 2 )
		self.toolbar.AddSeparator()
		
		self.toolbar.AddTool( tFileNew, u"tool", wx.Bitmap( u"artwork/File_New.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Create New Map File", u"Create New Map File", None ) 
		
		self.toolbar.AddTool( tFileNewGeomorph, u"New Geomorph", wx.Bitmap( u"artwork/geomorph_button.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Select to create a new geomorph file", u"Select to create a new geomorph file", None ) 
		
		self.toolbar.AddSeparator()
		
		self.toolbar.AddTool( tFileOpen, u"Open Map File", wx.Bitmap( u"artwork/File_Open.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Open existing map file...", u"Open existing map file...", None ) 
		
		self.toolbar.AddTool( tFileOpenGeomorph, u"tool", wx.Bitmap( u"artwork/open_geomorph.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Open a pymapper geomorph file", u"Open a pymapper geomorph file", None ) 
		
		self.toolbar.AddSeparator()
		
		self.toolbar.AddTool( tFileSave, u"tool", wx.Bitmap( u"artwork/save.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Save current map file", u"Save current map file", None ) 
		
		self.toolbar.AddTool( tFileSaveAs, u"tool", wx.Bitmap( u"artwork/SaveAs.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Save current map file with a new name...", u"Save current map file with a new name...", None ) 
		
		self.toolbar.AddSeparator()
		
		self.toolbar.AddTool( tPrintMap, u"tool", wx.Bitmap( u"artwork/printer_small.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Print Map...", u"Print Map...", None ) 
		
		self.toolbar.AddTool( tExportImage, u"tool", wx.Bitmap( u"artwork/ExportImage.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Export the current map to a jpg or png image...", u"Export the current map to a jpg or png image...", None ) 
		
		self.toolbar.AddSeparator()
		
		self.toolbar.AddTool( tEditUndo, u"tool", wx.Bitmap( u"artwork/undo.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Undo the previous action", u"Undo the previous action", None ) 
		
		self.toolbar.AddSeparator()
		
		self.toolbar.AddTool( tImportTileset, u"tool", wx.Bitmap( u"artwork/import_tileset.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Import a tileset file...", u"Import a tileset file...", None ) 
		
		self.toolbar.AddTool( tImportBackground, u"tool", wx.Bitmap( u"artwork/ImportBackground.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Import Background...", u"Import Background...", None ) 
		
		self.toolbar.AddSeparator()
		
		self.toolbar.AddTool( tTileQuantity, u"tool", wx.Bitmap( u"artwork/TQ_single.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Switch between limited and unlimited tile usage", u"Switch between limited and unlimited tile usage", None ) 
		
		self.toolbar.AddTool( tSnapToGrid, u"tool", wx.Bitmap( u"artwork/snap_to_grid.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, u"Snap tiles to grid when active.  Free placement when toggled off.", u"Snap tiles to grid when active.  Free placement when toggled off.", None ) 
		
		self.toolbar.AddSeparator()
		
		self.toolbar.AddTool( tShowGrid, u"tool", wx.Bitmap( u"artwork/grid_on.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, u"Show or Hide the gridlines", u"Show or Hide the gridlines", None ) 
		
		self.toolbar.AddTool( tShowBackground, u"tool", wx.Bitmap( u"artwork/Background.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, u"Show/Hide Background", u"Show/Hide Background", None ) 
		
		self.toolbar.AddTool( tShowLayerFilter, u"tool", wx.Bitmap( u"artwork/Layers.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, u"Show layer and tileset filter", u"Show layer and tileset filter", None ) 
		
		self.toolbar.AddTool( tShowIcons, u"tool", wx.Bitmap( u"artwork/treasure_icon_small.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, u"Turn on/off display of room/trap/monster icons", u"Turn on/off display of room/trap/monster icons", None ) 
		
		self.toolbar.AddTool( tShowLabels, u"Show Labels", wx.Bitmap( u"artwork/icon_labels.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, u"Toggle to show icon labels", u"Toggle to show or hide labels on the icons", None ) 
		
		self.toolbar.AddSeparator()
		
		self.toolbar.AddTool( tShowDrawingObjects, u"tool", wx.Bitmap( u"artwork/draw_show_no_handles.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, u"Turn on/off display of drawing objects.", u"Turn on/off display of drawing objects.", None ) 
		
		self.toolbar.AddTool( tShowDrawingHandles, u"tool", wx.Bitmap( u"artwork/draw_show_handles.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, u"Turn on or off the handles on drawing objects", u"Turn on or off the handles on drawing objects", None ) 
		
		self.toolbar.AddTool( tShowFogObjects, u"tool", wx.Bitmap( u"artwork/add_fog.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, u"Toggle the display of fog of war objects", u"Toggle the display of fog of war objects", None ) 
		
		self.toolbar.AddSeparator()
		
		self.toolbar.AddTool( tZoomIn, u"tool", wx.Bitmap( u"artwork/ZoomIn.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Click to zoom in on the map", u"Click to zoom in on the map", None ) 
		
		self.toolbar.AddTool( tZoomOut, u"tool", wx.Bitmap( u"artwork/ZoomOut.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Click to zoom out on the map", u"Click to zoom out on the map", None ) 
		
		self.toolbar.AddSeparator()
		
		self.toolbar.AddTool( tHelp, u"tool", wx.Bitmap( u"artwork/help.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Open help file...", u"Open help file...", None ) 
		
		self.toolbar.Realize() 
		
		self.menubar = wx.MenuBar( 0 )
		self.Menu_File = wx.Menu()
		self.File_New = wx.MenuItem( self.Menu_File, mFileNew, u"New..."+ u"\t" + u"Ctrl+N", u"Create a new black map file", wx.ITEM_NORMAL )
		self.Menu_File.Append( self.File_New )
		
		self.File_New_Geomorph = wx.MenuItem( self.Menu_File, mFileNewGeomorph, u"New Geomorph...", wx.EmptyString, wx.ITEM_NORMAL )
		self.Menu_File.Append( self.File_New_Geomorph )
		
		self.Menu_File.AppendSeparator()
		
		self.File_Open = wx.MenuItem( self.Menu_File, mFileOpen, u"Open..."+ u"\t" + u"Ctrl+O", u"Open an existing map file", wx.ITEM_NORMAL )
		self.Menu_File.Append( self.File_Open )
		
		self.File_Open_Geomorph = wx.MenuItem( self.Menu_File, mFileOpenGeomorph, u"Open Geomorph...", wx.EmptyString, wx.ITEM_NORMAL )
		self.Menu_File.Append( self.File_Open_Geomorph )
		
		self.File_Save = wx.MenuItem( self.Menu_File, mFileSave, u"Save..."+ u"\t" + u"Ctrl+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.Menu_File.Append( self.File_Save )
		
		self.File_SaveAs = wx.MenuItem( self.Menu_File, mFileSaveAs, u"Save As...", wx.EmptyString, wx.ITEM_NORMAL )
		self.Menu_File.Append( self.File_SaveAs )
		
		self.Menu_File.AppendSeparator()
		
		self.File_ImportFile = wx.MenuItem( self.Menu_File, mFileImportFile, u"Import map file to a new page", u"Import existing map file to a new map page", wx.ITEM_NORMAL )
		self.Menu_File.Append( self.File_ImportFile )
		
		self.File_ImportBackground = wx.MenuItem( self.Menu_File, mFileImportBackground, u"Import Map Background...", u"Open an image to use as a map background", wx.ITEM_NORMAL )
		self.Menu_File.Append( self.File_ImportBackground )
		
		self.Menu_File.AppendSeparator()
		
		self.FileRecentFiles = wx.Menu()
		self.RecentFile1 = wx.MenuItem( self.FileRecentFiles, mFileRecentFile1, u"...", wx.EmptyString, wx.ITEM_NORMAL )
		self.FileRecentFiles.Append( self.RecentFile1 )
		
		self.RecentFile2 = wx.MenuItem( self.FileRecentFiles, mFileRecentFile2, u"...", wx.EmptyString, wx.ITEM_NORMAL )
		self.FileRecentFiles.Append( self.RecentFile2 )
		
		self.RecentFile3 = wx.MenuItem( self.FileRecentFiles, mFileRecentFile3, u"...", wx.EmptyString, wx.ITEM_NORMAL )
		self.FileRecentFiles.Append( self.RecentFile3 )
		
		self.RecentFile4 = wx.MenuItem( self.FileRecentFiles, mFileRecentFile4, u"...", wx.EmptyString, wx.ITEM_NORMAL )
		self.FileRecentFiles.Append( self.RecentFile4 )
		
		self.RecentFile5 = wx.MenuItem( self.FileRecentFiles, mFileRecentFile5, u"...", wx.EmptyString, wx.ITEM_NORMAL )
		self.FileRecentFiles.Append( self.RecentFile5 )
		
		self.Menu_File.AppendSubMenu( self.FileRecentFiles, u"Recent Files" )
		
		self.File_Exit = wx.MenuItem( self.Menu_File, mFileExit, u"Exit..."+ u"\t" + u"Ctrl+Q", u"Exit pymapper", wx.ITEM_NORMAL )
		self.Menu_File.Append( self.File_Exit )
		
		self.menubar.Append( self.Menu_File, u"File" ) 
		
		self.Menu_Edit = wx.Menu()
		self.Edit_Undo = wx.MenuItem( self.Menu_Edit, mEditUndo, u"Undo"+ u"\t" + u"Ctrl+Z", u"Undo the previous action", wx.ITEM_NORMAL )
		self.Edit_Undo.SetBitmap( wx.Bitmap( u"artwork/undo.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_Edit.Append( self.Edit_Undo )
		self.Edit_Undo.Enable( False )
		
		self.Edit_Cut = wx.MenuItem( self.Menu_Edit, mEditCut, u"Cut"+ u"\t" + u"Ctrl+X", u"Cut the tile out and place it in pymappers clipboard", wx.ITEM_NORMAL )
		self.Menu_Edit.Append( self.Edit_Cut )
		self.Edit_Cut.Enable( False )
		
		self.Edit_Copy = wx.MenuItem( self.Menu_Edit, mEditCopy, u"Copy"+ u"\t" + u"Ctrl+C", u"Copy the selected tile and place it in pymappers clipboard", wx.ITEM_NORMAL )
		self.Menu_Edit.Append( self.Edit_Copy )
		self.Edit_Copy.Enable( False )
		
		self.Edit_Paste = wx.MenuItem( self.Menu_Edit, mEditPaste, u"Paste"+ u"\t" + u"Ctrl+V", u"Paste the tile in pymappers clipboard to the map", wx.ITEM_NORMAL )
		self.Menu_Edit.Append( self.Edit_Paste )
		self.Edit_Paste.Enable( False )
		
		self.Edit_SelectAll = wx.MenuItem( self.Menu_Edit, mEditSelectAll, u"Select All Tiles", wx.EmptyString, wx.ITEM_NORMAL )
		self.Menu_Edit.Append( self.Edit_SelectAll )
		self.Edit_SelectAll.Enable( False )
		
		self.Edit_MapSize = wx.MenuItem( self.Menu_Edit, mEditMapSize, u"Change Map Size", u"Change the size of the map space", wx.ITEM_NORMAL )
		self.Edit_MapSize.SetBitmap( wx.Bitmap( u"artwork/changegridsize.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_Edit.Append( self.Edit_MapSize )
		
		self.menubar.Append( self.Menu_Edit, u"Edit" ) 
		
		self.Menu_Tilesets = wx.Menu()
		self.Tileset_CreateMaster = wx.MenuItem( self.Menu_Tilesets, mTilesetCreateMaster, u"Create from master image...", u"Create a new tileset from a single composite image", wx.ITEM_NORMAL )
		self.Menu_Tilesets.Append( self.Tileset_CreateMaster )
		self.Tileset_CreateMaster.Enable( False )
		
		self.Tileset_CreateResolution = wx.MenuItem( self.Menu_Tilesets, mTilesetCreateResolution, u"Create from image folder", u"Create new tileset from all images in a single folder", wx.ITEM_NORMAL )
		self.Menu_Tilesets.Append( self.Tileset_CreateResolution )
		self.Tileset_CreateResolution.Enable( False )
		
		self.Tileset_EditTileset = wx.MenuItem( self.Menu_Tilesets, mTilesetEdit, u"Edit Tileset..."+ u"\t" + u"Ctrl+I", u"Edit tileset", wx.ITEM_NORMAL )
		self.Menu_Tilesets.Append( self.Tileset_EditTileset )
		
		self.Tileset_TilesetBrowser = wx.MenuItem( self.Menu_Tilesets, mTilesetBrowser, u"Tileset Browser..."+ u"\t" + u"Ctrl+T", u"Open an existing tileset", wx.ITEM_NORMAL )
		self.Menu_Tilesets.Append( self.Tileset_TilesetBrowser )
		
		self.menubar.Append( self.Menu_Tilesets, u"Tilesets" ) 
		
		self.Menu_Print = wx.Menu()
		self.Print_Map = wx.MenuItem( self.Menu_Print, mPrintMap, u"Print Map..."+ u"\t" + u"Ctrl+P", u"Print the map", wx.ITEM_NORMAL )
		self.Print_Map.SetBitmap( wx.Bitmap( u"artwork/printer_small.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_Print.Append( self.Print_Map )
		
		self.Print_Image = wx.MenuItem( self.Menu_Print, mPrintImage, u"Export Image..."+ u"\t" + u"F2", u"Save the map as a jpg or png image", wx.ITEM_NORMAL )
		self.Print_Image.SetBitmap( wx.Bitmap( u"artwork/ExportImage.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_Print.Append( self.Print_Image )
		
		self.Print_ChangeResolution = wx.MenuItem( self.Menu_Print, mPrintChangeResolution, u"Change Print Resolution", u"Print Resolution affects the output quality of the print image", wx.ITEM_NORMAL )
		self.Print_ChangeResolution.SetBitmap( wx.Bitmap( u"artwork/PrintResolution.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_Print.Append( self.Print_ChangeResolution )
		
		self.menubar.Append( self.Menu_Print, u"Print" ) 
		
		self.Menu_View = wx.Menu()
		self.View_Grid = wx.MenuItem( self.Menu_View, mViewGrid, u"View Grid?"+ u"\t" + u"Ctrl + G", u"Turn the grid background on or off.", wx.ITEM_CHECK )
		self.View_Grid.SetBitmap( wx.NullBitmap )
		self.Menu_View.Append( self.View_Grid )
		self.View_Grid.Check( True )
		
		self.View_FilterTags = wx.MenuItem( self.Menu_View, mViewFilterTags, u"Change Filter Tags"+ u"\t" + u"Ctrl+F", wx.EmptyString, wx.ITEM_CHECK )
		self.View_FilterTags.SetBitmap( wx.NullBitmap )
		self.Menu_View.Append( self.View_FilterTags )
		self.View_FilterTags.Check( True )
		
		self.View_Background = wx.MenuItem( self.Menu_View, mViewBackground, u"View Background?"+ u"\t" + u"Ctrl+ B", wx.EmptyString, wx.ITEM_CHECK )
		self.View_Background.SetBitmap( wx.NullBitmap )
		self.Menu_View.Append( self.View_Background )
		
		self.View_GridCoordinates = wx.MenuItem( self.Menu_View, mViewGridCoordinates, u"Show Grid Coordinates?", u"Shows grid coordinates on the map.", wx.ITEM_CHECK )
		self.View_GridCoordinates.SetBitmap( wx.NullBitmap )
		self.Menu_View.Append( self.View_GridCoordinates )
		
		self.View_HighlightIcons = wx.MenuItem( self.Menu_View, mViewHighlightIcons, u"Highlight Map Icons?", u"Highlight the map icons on the map window?", wx.ITEM_CHECK )
		self.View_HighlightIcons.SetBitmap( wx.NullBitmap )
		self.Menu_View.Append( self.View_HighlightIcons )
		self.View_HighlightIcons.Check( True )
		
		self.View_DualTileDisplay = wx.MenuItem( self.Menu_View, mViewDualTileDisplay, u"Show both tile sides in Tile Window?", u"Show reverse side on tile window (on) or show on mouse hover (off)", wx.ITEM_CHECK )
		self.View_DualTileDisplay.SetBitmap( wx.NullBitmap )
		self.Menu_View.Append( self.View_DualTileDisplay )
		self.View_DualTileDisplay.Check( True )
		
		self.View_OutlineTiles = wx.MenuItem( self.Menu_View, mViewOutlineTiles, u"Outline Tiles?", wx.EmptyString, wx.ITEM_CHECK )
		self.Menu_View.Append( self.View_OutlineTiles )
		
		self.View_ShowIconNamesOnMap = wx.MenuItem( self.Menu_View, mShowIconNamesOnMap, u"Show Icon Names on Map?", wx.EmptyString, wx.ITEM_CHECK )
		self.Menu_View.Append( self.View_ShowIconNamesOnMap )
		self.View_ShowIconNamesOnMap.Check( True )
		
		self.View_ViewConditionColors = wx.MenuItem( self.Menu_View, wx.ID_ANY, u"View Monster Condition Colors", wx.EmptyString, wx.ITEM_NORMAL )
		self.View_ViewConditionColors.SetBitmap( wx.Bitmap( u"artwork/condition_colors.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_View.Append( self.View_ViewConditionColors )
		
		self.View_ZoomIn = wx.MenuItem( self.Menu_View, mViewZoomIn, u"Zoom In", wx.EmptyString, wx.ITEM_NORMAL )
		self.View_ZoomIn.SetBitmap( wx.Bitmap( u"artwork/ZoomIn.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_View.Append( self.View_ZoomIn )
		
		self.View_ZoomOut = wx.MenuItem( self.Menu_View, mViewZoomOut, u"Zoom Out", wx.EmptyString, wx.ITEM_NORMAL )
		self.View_ZoomOut.SetBitmap( wx.Bitmap( u"artwork/ZoomOut.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_View.Append( self.View_ZoomOut )
		
		self.View_ViewAll = wx.MenuItem( self.Menu_View, mViewViewAll, u"View All", wx.EmptyString, wx.ITEM_NORMAL )
		self.View_ViewAll.SetBitmap( wx.Bitmap( u"artwork/select_all.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_View.Append( self.View_ViewAll )
		
		self.View_TilesetLayerFilter = wx.MenuItem( self.Menu_View, mViewViewTilesetLayerFilter, u"Show Tileset/Layer Filter Dialog", u"Show a dialog to change display of layers and tilesets", wx.ITEM_NORMAL )
		self.View_TilesetLayerFilter.SetBitmap( wx.Bitmap( u"artwork/Layers.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_View.Append( self.View_TilesetLayerFilter )
		
		self.Menu_View.AppendSeparator()
		
		self.View_SecondaryScreen = wx.MenuItem( self.Menu_View, mViewSecondaryScreen, u"Secondary Map Viewport", u"Open a secondary map view for player displays", wx.ITEM_NORMAL )
		self.View_SecondaryScreen.SetBitmap( wx.Bitmap( u"artwork/screens.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_View.Append( self.View_SecondaryScreen )
		
		self.View_UpdateToFTP = wx.MenuItem( self.Menu_View, mViewUpdateToFTP, u"Update Map View to Remote Server"+ u"\t" + u"Ctrl+W", wx.EmptyString, wx.ITEM_NORMAL )
		self.View_UpdateToFTP.SetBitmap( wx.Bitmap( u"artwork/UpdateFTP.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_View.Append( self.View_UpdateToFTP )
		self.View_UpdateToFTP.Enable( False )
		
		self.View_UpdateFog = wx.MenuItem( self.Menu_View, mViewUpdateFog, u"Update Fog Display on Secondary"+ u"\t" + u"Ctrl+Y", wx.EmptyString, wx.ITEM_NORMAL )
		self.Menu_View.Append( self.View_UpdateFog )
		self.View_UpdateFog.Enable( False )
		
		self.menubar.Append( self.Menu_View, u"View" ) 
		
		self.Menu_Options = wx.Menu()
		self.Options_Program = wx.MenuItem( self.Menu_Options, mOptionsProgram, u"Program...", wx.EmptyString, wx.ITEM_NORMAL )
		self.Options_Program.SetBitmap( wx.Bitmap( u"artwork/gear.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_Options.Append( self.Options_Program )
		
		self.Options_Tilesets = wx.MenuItem( self.Menu_Options, mOptionsTilesets, u"Tilesets...", wx.EmptyString, wx.ITEM_NORMAL )
		self.Options_Tilesets.SetBitmap( wx.Bitmap( u"artwork/edit_tileset.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_Options.Append( self.Options_Tilesets )
		
		self.Options_SymbolsMarkers = wx.MenuItem( self.Menu_Options, mOptionsSymbolsMarkers, u"Symbols and Markers...", u"Add and Delete built-in symbols and markers", wx.ITEM_NORMAL )
		self.Options_SymbolsMarkers.SetBitmap( wx.Bitmap( u"artwork/SymbolMarker_icon.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_Options.Append( self.Options_SymbolsMarkers )
		
		self.Options_Text = wx.MenuItem( self.Menu_Options, mOptionsText, u"Text Annotations...", wx.EmptyString, wx.ITEM_NORMAL )
		self.Options_Text.SetBitmap( wx.Bitmap( u"artwork/rename_icon.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_Options.Append( self.Options_Text )
		
		self.Options_SelectMode = wx.MenuItem( self.Menu_Options, mOptionsSelectMode, u"Set Tile Select Mode?", wx.EmptyString, wx.ITEM_CHECK )
		self.Options_SelectMode.SetBitmap( wx.NullBitmap )
		self.Menu_Options.Append( self.Options_SelectMode )
		self.Options_SelectMode.Check( True )
		
		self.Options_inifile = wx.MenuItem( self.Menu_Options, mOptionsInifile, u"Save Settings File", wx.EmptyString, wx.ITEM_NORMAL )
		self.Menu_Options.Append( self.Options_inifile )
		
		self.Options_FTP = wx.MenuItem( self.Menu_Options, mOptionsFTP, u"FTP Settings...", wx.EmptyString, wx.ITEM_NORMAL )
		self.Options_FTP.SetBitmap( wx.Bitmap( u"artwork/ftp_settings.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_Options.Append( self.Options_FTP )
		
		self.menubar.Append( self.Menu_Options, u"Options" ) 
		
		self.Menu_Maps = wx.Menu()
		self.Maps_RandomDungeon = wx.MenuItem( self.Menu_Maps, mMapsRandomDungeon, u"Create Random Dungeon", u"Create random dungeon using geomorphs", wx.ITEM_NORMAL )
		self.Maps_RandomDungeon.SetBitmap( wx.Bitmap( u"artwork/random_dungeon.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_Maps.Append( self.Maps_RandomDungeon )
		
		self.Maps_Isometric = wx.MenuItem( self.Menu_Maps, wx.ID_ANY, u"Isometric View", wx.EmptyString, wx.ITEM_NORMAL )
		self.Maps_Isometric.SetBitmap( wx.Bitmap( u"artwork/isometric.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_Maps.Append( self.Maps_Isometric )
		
		self.menubar.Append( self.Menu_Maps, u"Maps" ) 
		
		self.Menu_Reports = wx.Menu()
		self.Reports_Manifests = wx.MenuItem( self.Menu_Reports, mReportsManifest, u"Tile Manifests...", u"Select to produce a list of tiles used in the map", wx.ITEM_NORMAL )
		self.Reports_Manifests.SetBitmap( wx.Bitmap( u"artwork/Reports.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_Reports.Append( self.Reports_Manifests )
		
		self.Reports_Tilesets = wx.MenuItem( self.Menu_Reports, mReportsTilesets, u"Tilesets Used...", u"Provide a list of tilesets used on the map", wx.ITEM_NORMAL )
		self.Reports_Tilesets.SetBitmap( wx.Bitmap( u"artwork/TileOptions.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_Reports.Append( self.Reports_Tilesets )
		
		self.menubar.Append( self.Menu_Reports, u"Reports" ) 
		
		self.Menu_Dungeon = wx.Menu()
		self.Dungeon_Load_d20_Files = wx.MenuItem( self.Menu_Dungeon, mDungeonLoadD20Files, u"Load Dungeon Resources", u"Load information related to monsters, traps, feats, etc.", wx.ITEM_NORMAL )
		self.Dungeon_Load_d20_Files.SetBitmap( wx.Bitmap( u"artwork/D20_logo_small.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_Dungeon.Append( self.Dungeon_Load_d20_Files )
		
		self.Dungeon_Load_DnD5_Files = wx.MenuItem( self.Menu_Dungeon, mDungeonLoadDnD5Files, u"Load 5E Resources", wx.EmptyString, wx.ITEM_NORMAL )
		self.Dungeon_Load_DnD5_Files.SetBitmap( wx.Bitmap( u"artwork/5E_monster.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_Dungeon.Append( self.Dungeon_Load_DnD5_Files )
		
		self.Menu_Dungeon.AppendSeparator()
		
		self.Dungeon_NPCgenerator = wx.MenuItem( self.Menu_Dungeon, mDungeonNPCGenerator, u"PF/3.5 NPC Generator", u"Generate Non Player Characters (NPC) for Pathfinder/3.5", wx.ITEM_NORMAL )
		self.Dungeon_NPCgenerator.SetBitmap( wx.Bitmap( u"artwork/npc_icon_small.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_Dungeon.Append( self.Dungeon_NPCgenerator )
		
		self.Dungeon_Monster = wx.MenuItem( self.Menu_Dungeon, mDungeonMonster, u"PF / 3.5 Monsters", u"View/Edit Monsters", wx.ITEM_NORMAL )
		self.Dungeon_Monster.SetBitmap( wx.Bitmap( u"artwork/pathfinder.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_Dungeon.Append( self.Dungeon_Monster )
		
		self.Menu_Dungeon.AppendSeparator()
		
		self.Dungeon_Monster5E = wx.MenuItem( self.Menu_Dungeon, mDungeonMonster5E, u"5E Monsters", u"View/Edit Monsters from the 5th Edition", wx.ITEM_NORMAL )
		self.Dungeon_Monster5E.SetBitmap( wx.Bitmap( u"artwork/5E_monster.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_Dungeon.Append( self.Dungeon_Monster5E )
		
		self.Dungeon_NPC_5E = wx.MenuItem( self.Menu_Dungeon, mDungeonNPC_5E, u"5E NPC", u"View/Edit NPC's from the 5th Edition", wx.ITEM_NORMAL )
		self.Dungeon_NPC_5E.SetBitmap( wx.Bitmap( u"artwork/npc_icon_small.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_Dungeon.Append( self.Dungeon_NPC_5E )
		
		self.Dungeon_Spell_5E = wx.MenuItem( self.Menu_Dungeon, mDungeonSpell_5E, u"5E Spells", wx.EmptyString, wx.ITEM_NORMAL )
		self.Dungeon_Spell_5E.SetBitmap( wx.Bitmap( u"artwork/Spell_5E_icon.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_Dungeon.Append( self.Dungeon_Spell_5E )
		
		self.Menu_Dungeon.AppendSeparator()
		
		self.Dungeon_Encounters = wx.MenuItem( self.Menu_Dungeon, mDungeonEncounters, u"Encounters", u"View/Edit Encounters", wx.ITEM_NORMAL )
		self.Dungeon_Encounters.SetBitmap( wx.Bitmap( u"artwork/torch_encounter.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_Dungeon.Append( self.Dungeon_Encounters )
		self.Dungeon_Encounters.Enable( False )
		
		self.Dungeon_Traps = wx.MenuItem( self.Menu_Dungeon, mDungeonTraps, u"Trap Designer", u"Create New Trap...", wx.ITEM_NORMAL )
		self.Dungeon_Traps.SetBitmap( wx.Bitmap( u"artwork/trap.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_Dungeon.Append( self.Dungeon_Traps )
		
		self.Dungeon_Treasures = wx.MenuItem( self.Menu_Dungeon, mDungeonTreasures, u"Treasure Calculator", u"Select to bring up the treasure calculator.", wx.ITEM_NORMAL )
		self.Dungeon_Treasures.SetBitmap( wx.Bitmap( u"artwork/treasure_icon_small.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_Dungeon.Append( self.Dungeon_Treasures )
		
		self.Dungeon_Combat_Tracking = wx.MenuItem( self.Menu_Dungeon, mDungeonCombatTracking, u"Combat Tracking", u"Start the combat tracking dialog", wx.ITEM_NORMAL )
		self.Dungeon_Combat_Tracking.SetBitmap( wx.Bitmap( u"artwork/npc.png", wx.BITMAP_TYPE_ANY ) )
		self.Menu_Dungeon.Append( self.Dungeon_Combat_Tracking )
		
		self.Dungeon_DiceRoller = wx.MenuItem( self.Menu_Dungeon, mDungeonDiceRoller, u"Dice Roller"+ u"\t" + u"Ctrl + D", u"Activate the dice roller dialog", wx.ITEM_NORMAL )
		self.Dungeon_DiceRoller.SetBitmap( wx.Bitmap( u"artwork/d20_dice.ico", wx.BITMAP_TYPE_ANY ) )
		self.Menu_Dungeon.Append( self.Dungeon_DiceRoller )
		
		self.Dungeon_ShowIcons = wx.MenuItem( self.Menu_Dungeon, mDungeonShowIcons, u"Show Dungeon Icons?", wx.EmptyString, wx.ITEM_CHECK )
		self.Dungeon_ShowIcons.SetBitmap( wx.NullBitmap )
		self.Menu_Dungeon.Append( self.Dungeon_ShowIcons )
		
		self.Resources = wx.Menu()
		self.Dungeon_Pathfinder_MagicItems = wx.MenuItem( self.Resources, mDungeonPathfinderMagicItems, u"Pathfinder Magic Items...", u"View magic items from the Pathfinder SRD", wx.ITEM_NORMAL )
		self.Resources.Append( self.Dungeon_Pathfinder_MagicItems )
		
		self.Dungeon_Pathfinder_Monsters = wx.MenuItem( self.Resources, mDungeonPathfinderMonsters, u"Pathfinder Monsters...", u"View monsters from the Pathfinder SRD", wx.ITEM_NORMAL )
		self.Resources.Append( self.Dungeon_Pathfinder_Monsters )
		
		self.Dungeon_d20Spells = wx.MenuItem( self.Resources, mDungeonD20Spells, u"d20 Spells...", u"View spells from the d20 SRD", wx.ITEM_NORMAL )
		self.Resources.Append( self.Dungeon_d20Spells )
		
		self.Dungeon_d20Feats = wx.MenuItem( self.Resources, mDungeonD20Feats, u"d20 Feats...", u"View feats from the d20 SRD", wx.ITEM_NORMAL )
		self.Resources.Append( self.Dungeon_d20Feats )
		
		self.Dungeon_About = wx.MenuItem( self.Resources, mDungeonAbout, u"License and Credits...", u"View licensing and credits for d20 and Pathfinder resources", wx.ITEM_NORMAL )
		self.Resources.Append( self.Dungeon_About )
		
		self.Menu_Dungeon.AppendSubMenu( self.Resources, u"Resources" )
		
		self.menubar.Append( self.Menu_Dungeon, u"Dungeon" ) 
		
		self.Menu_Help = wx.Menu()
		self.Help_Contents = wx.MenuItem( self.Menu_Help, mHelpContents, u"Contents..."+ u"\t" + u"F1", wx.EmptyString, wx.ITEM_NORMAL )
		self.Menu_Help.Append( self.Help_Contents )
		
		self.Help_OpenTutorial = wx.MenuItem( self.Menu_Help, mHelpOpenTutorial, u"Open Tutorial...", wx.EmptyString, wx.ITEM_NORMAL )
		self.Menu_Help.Append( self.Help_OpenTutorial )
		
		self.Help_ShowTips = wx.MenuItem( self.Menu_Help, mHelpShowTips, u"Show Tips...", wx.EmptyString, wx.ITEM_NORMAL )
		self.Menu_Help.Append( self.Help_ShowTips )
		
		self.Help_KeyboardShortcuts = wx.MenuItem( self.Menu_Help, mHelpKeyboardShortcuts, u"Keyboard Shortcuts...", u"Show a list of keyboard shortcuts", wx.ITEM_NORMAL )
		self.Menu_Help.Append( self.Help_KeyboardShortcuts )
		
		self.Help_ProgramFoundation = wx.MenuItem( self.Menu_Help, mHelpProgramFoundation, u"Development...", u"Show details about the software used to make PyMapper", wx.ITEM_NORMAL )
		self.Menu_Help.Append( self.Help_ProgramFoundation )
		
		self.Help_RegisterProgram = wx.MenuItem( self.Menu_Help, mHelpRegisterProgram, u"Register Program...", wx.EmptyString, wx.ITEM_NORMAL )
		self.Menu_Help.Append( self.Help_RegisterProgram )
		
		self.Help_About = wx.MenuItem( self.Menu_Help, mHelpAbout, u"About...", wx.EmptyString, wx.ITEM_NORMAL )
		self.Menu_Help.Append( self.Help_About )
		
		self.menubar.Append( self.Menu_Help, u"Help" ) 
		
		self.SetMenuBar( self.menubar )
		
		bSizer175 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer180 = wx.BoxSizer( wx.VERTICAL )
		
		self.SplitterSash = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.SplitterSash.Bind( wx.EVT_IDLE, self.SplitterSashOnIdle )
		self.SplitterSash.SetMinimumPaneSize( 100 )
		
		self.pnMapBasePanel = wx.Panel( self.SplitterSash, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer177 = wx.BoxSizer( wx.VERTICAL )
		
		self.nbMapNotebook = wx.Notebook( self.pnMapBasePanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.MapWindow = wx.ScrolledWindow( self.nbMapNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.MapWindow.SetScrollRate( 5, 5 )
		self.MapWindow.SetBackgroundColour( wx.Colour( 64, 128, 128 ) )
		
		self.nbMapNotebook.AddPage( self.MapWindow, u"map page", False )
		
		bSizer177.Add( self.nbMapNotebook, 1, wx.EXPAND, 5 )
		
		
		self.pnMapBasePanel.SetSizer( bSizer177 )
		self.pnMapBasePanel.Layout()
		bSizer177.Fit( self.pnMapBasePanel )
		self.pnTileBasePanel = wx.Panel( self.SplitterSash, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1781 = wx.BoxSizer( wx.VERTICAL )
		
		self.nbTileNotebook = wx.Notebook( self.pnTileBasePanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TileWindow = wx.ScrolledWindow( self.nbTileNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.TileWindow.SetScrollRate( 5, 5 )
		self.TileWindow.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )
		
		self.nbTileNotebook.AddPage( self.TileWindow, u"tile page", False )
		
		bSizer1781.Add( self.nbTileNotebook, 1, wx.EXPAND, 5 )
		
		
		self.pnTileBasePanel.SetSizer( bSizer1781 )
		self.pnTileBasePanel.Layout()
		bSizer1781.Fit( self.pnTileBasePanel )
		self.SplitterSash.SplitVertically( self.pnMapBasePanel, self.pnTileBasePanel, 501 )
		bSizer180.Add( self.SplitterSash, 1, wx.EXPAND, 5 )
		
		
		bSizer175.Add( bSizer180, 1, wx.EXPAND, 5 )
		
		bSizer179 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer182 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.MapWindowZoomSlider = wx.Slider( self, wx.ID_ANY, 25, 10, 75, wx.DefaultPosition, wx.DefaultSize, wx.SL_BOTH )
		self.MapWindowZoomSlider.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.MapWindowZoomSlider.SetBackgroundColour( wx.Colour( 64, 128, 128 ) )
		self.MapWindowZoomSlider.SetToolTip( u"Slide to change the zoom on the map window." )
		
		bSizer182.Add( self.MapWindowZoomSlider, 1, wx.EXPAND, 5 )
		
		
		bSizer179.Add( bSizer182, 1, wx.EXPAND, 5 )
		
		bSizer181 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.tgTileMode = wx.Button( self, wx.ID_ANY, u"Tile Mode", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.tgTileMode.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.tgTileMode.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.tgTileMode.SetBackgroundColour( wx.Colour( 0, 159, 0 ) )
		
		bSizer181.Add( self.tgTileMode, 0, 0, 5 )
		
		self.tgIconMode = wx.Button( self, wx.ID_ANY, u"Icon Mode", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.tgIconMode.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.tgIconMode.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.tgIconMode.SetBackgroundColour( wx.Colour( 215, 0, 0 ) )
		
		bSizer181.Add( self.tgIconMode, 0, 0, 5 )
		
		self.tgDrawMode = wx.Button( self, wx.ID_ANY, u"Draw Mode", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.tgDrawMode.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.tgDrawMode.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.tgDrawMode.SetBackgroundColour( wx.Colour( 215, 0, 0 ) )
		
		bSizer181.Add( self.tgDrawMode, 0, 0, 5 )
		
		self.tgFogMode = wx.Button( self, wx.ID_ANY, u"Fog Mode", wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER )
		self.tgFogMode.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.tgFogMode.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.tgFogMode.SetBackgroundColour( wx.Colour( 215, 0, 0 ) )
		
		bSizer181.Add( self.tgFogMode, 0, 0, 5 )
		
		cxLayerSelectorChoices = [ u"Base" ]
		self.cxLayerSelector = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cxLayerSelectorChoices, 0 )
		self.cxLayerSelector.SetSelection( 0 )
		self.cxLayerSelector.SetToolTip( u"Selects the active layer" )
		self.cxLayerSelector.SetMinSize( wx.Size( 125,-1 ) )
		
		bSizer181.Add( self.cxLayerSelector, 0, wx.EXPAND, 0 )
		
		
		bSizer179.Add( bSizer181, 1, wx.EXPAND, 5 )
		
		bSizer183 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.TileWindowZoomSlider = wx.Slider( self, wx.ID_ANY, 25, 10, 50, wx.DefaultPosition, wx.DefaultSize, wx.SL_BOTH )
		self.TileWindowZoomSlider.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )
		self.TileWindowZoomSlider.SetToolTip( u"Slide to change the zoom of the tile window." )
		
		bSizer183.Add( self.TileWindowZoomSlider, 1, wx.EXPAND, 5 )
		
		
		bSizer179.Add( bSizer183, 1, wx.EXPAND, 5 )
		
		
		bSizer175.Add( bSizer179, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer175 )
		self.Layout()
		self.sbStatusBar = self.CreateStatusBar( 3, wx.STB_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_TOOL, self.OnFileNew, id = tFileNew )
		self.Bind( wx.EVT_TOOL, self.OnFileNew, id = tFileNewGeomorph )
		self.Bind( wx.EVT_TOOL, self.OnFileOpen, id = tFileOpen )
		self.Bind( wx.EVT_TOOL, self.OnFileOpen, id = tFileOpenGeomorph )
		self.Bind( wx.EVT_TOOL, self.OnFileSave, id = tFileSave )
		self.Bind( wx.EVT_TOOL, self.OnFileSaveAs, id = tFileSaveAs )
		self.Bind( wx.EVT_TOOL, self.OnPrintMap, id = tPrintMap )
		self.Bind( wx.EVT_TOOL, self.OnPrintImage, id = tExportImage )
		self.Bind( wx.EVT_TOOL, self.OnUndoAction, id = tEditUndo )
		self.Bind( wx.EVT_TOOL, self.OnImportTileset, id = tImportTileset )
		self.Bind( wx.EVT_TOOL, self.OnImportBackground, id = tImportBackground )
		self.Bind( wx.EVT_TOOL, self.OnChangeTileQuantity, id = tTileQuantity )
		self.Bind( wx.EVT_TOOL, self.OnSnapToGrid, id = tSnapToGrid )
		self.Bind( wx.EVT_TOOL, self.OnViewGrid, id = tShowGrid )
		self.Bind( wx.EVT_TOOL, self.OnViewBackground, id = tShowBackground )
		self.Bind( wx.EVT_TOOL, self.OnViewTilesetLayerFilter, id = tShowLayerFilter )
		self.Bind( wx.EVT_TOOL, self.OnViewIcons, id = tShowIcons )
		self.Bind( wx.EVT_TOOL, self.OnViewShowIconNames, id = tShowLabels )
		self.Bind( wx.EVT_TOOL, self.OnViewDrawingObjects, id = tShowDrawingObjects )
		self.Bind( wx.EVT_TOOL, self.OnViewDrawingHandles, id = tShowDrawingHandles )
		self.Bind( wx.EVT_TOOL, self.OnViewFogObjects, id = tShowFogObjects )
		self.Bind( wx.EVT_TOOL, self.MapZoomIn, id = tZoomIn )
		self.Bind( wx.EVT_TOOL, self.RMapClickZoomOut, id = tZoomOut )
		self.Bind( wx.EVT_TOOL, self.OnHelp_Contents, id = tHelp )
		self.Bind( wx.EVT_MENU, self.OnFileNew, id = self.File_New.GetId() )
		self.Bind( wx.EVT_MENU, self.OnFileNew, id = self.File_New_Geomorph.GetId() )
		self.Bind( wx.EVT_MENU, self.OnFileOpen, id = self.File_Open.GetId() )
		self.Bind( wx.EVT_MENU, self.OnFileOpen, id = self.File_Open_Geomorph.GetId() )
		self.Bind( wx.EVT_MENU, self.OnFileSave, id = self.File_Save.GetId() )
		self.Bind( wx.EVT_MENU, self.OnFileSaveAs, id = self.File_SaveAs.GetId() )
		self.Bind( wx.EVT_MENU, self.OnImportFile, id = self.File_ImportFile.GetId() )
		self.Bind( wx.EVT_MENU, self.OnImportBackground, id = self.File_ImportBackground.GetId() )
		self.Bind( wx.EVT_MENU, self.OnRecentFile1, id = self.RecentFile1.GetId() )
		self.Bind( wx.EVT_MENU, self.OnRecentFile2, id = self.RecentFile2.GetId() )
		self.Bind( wx.EVT_MENU, self.OnRecentFile3, id = self.RecentFile3.GetId() )
		self.Bind( wx.EVT_MENU, self.OnRecentFile4, id = self.RecentFile4.GetId() )
		self.Bind( wx.EVT_MENU, self.OnRecentFile5, id = self.RecentFile5.GetId() )
		self.Bind( wx.EVT_MENU, self.OnExit, id = self.File_Exit.GetId() )
		self.Bind( wx.EVT_MENU, self.OnUndoAction, id = self.Edit_Undo.GetId() )
		self.Bind( wx.EVT_MENU, self.OnEditMapSize, id = self.Edit_MapSize.GetId() )
		self.Bind( wx.EVT_MENU, self.OnImportTiles, id = self.Tileset_EditTileset.GetId() )
		self.Bind( wx.EVT_MENU, self.OnImportTileset, id = self.Tileset_TilesetBrowser.GetId() )
		self.Bind( wx.EVT_MENU, self.OnPrintMap, id = self.Print_Map.GetId() )
		self.Bind( wx.EVT_MENU, self.OnPrintImage, id = self.Print_Image.GetId() )
		self.Bind( wx.EVT_MENU, self.OnChangeResolution, id = self.Print_ChangeResolution.GetId() )
		self.Bind( wx.EVT_MENU, self.OnViewGrid, id = self.View_Grid.GetId() )
		self.Bind( wx.EVT_MENU, self.OnViewFilterTags, id = self.View_FilterTags.GetId() )
		self.Bind( wx.EVT_MENU, self.OnViewBackground, id = self.View_Background.GetId() )
		self.Bind( wx.EVT_MENU, self.OnViewGridCoordinates, id = self.View_GridCoordinates.GetId() )
		self.Bind( wx.EVT_MENU, self.OnViewHighlightIcons, id = self.View_HighlightIcons.GetId() )
		self.Bind( wx.EVT_MENU, self.OnViewDualTileSides, id = self.View_DualTileDisplay.GetId() )
		self.Bind( wx.EVT_MENU, self.OnViewShowIconNames, id = self.View_ShowIconNamesOnMap.GetId() )
		self.Bind( wx.EVT_MENU, self.OnViewConditionColorsLegend, id = self.View_ViewConditionColors.GetId() )
		self.Bind( wx.EVT_MENU, self.OnViewViewAll, id = self.View_ViewAll.GetId() )
		self.Bind( wx.EVT_MENU, self.OnViewTilesetLayerFilter, id = self.View_TilesetLayerFilter.GetId() )
		self.Bind( wx.EVT_MENU, self.OnViewSecondaryScreen, id = self.View_SecondaryScreen.GetId() )
		self.Bind( wx.EVT_MENU, self.OnUpdateToFTP, id = self.View_UpdateToFTP.GetId() )
		self.Bind( wx.EVT_MENU, self.OnOptionsProgram, id = self.Options_Program.GetId() )
		self.Bind( wx.EVT_MENU, self.OnOptionsTilesets, id = self.Options_Tilesets.GetId() )
		self.Bind( wx.EVT_MENU, self.OnOptionsSymbolsMarkers, id = self.Options_SymbolsMarkers.GetId() )
		self.Bind( wx.EVT_MENU, self.OnOptionsText, id = self.Options_Text.GetId() )
		self.Bind( wx.EVT_MENU, self.OnOptionsIniFile, id = self.Options_inifile.GetId() )
		self.Bind( wx.EVT_MENU, self.OnOptionsFTP, id = self.Options_FTP.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMapsRandomDungeon, id = self.Maps_RandomDungeon.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMapsIsometric, id = self.Maps_Isometric.GetId() )
		self.Bind( wx.EVT_MENU, self.OnReportsManifest, id = self.Reports_Manifests.GetId() )
		self.Bind( wx.EVT_MENU, self.OnReportsTilesets, id = self.Reports_Tilesets.GetId() )
		self.Bind( wx.EVT_MENU, self.OnDungeon_Load_d20_Resources, id = self.Dungeon_Load_d20_Files.GetId() )
		self.Bind( wx.EVT_MENU, self.OnDungeon_Load_DnD5_Resources, id = self.Dungeon_Load_DnD5_Files.GetId() )
		self.Bind( wx.EVT_MENU, self.OnDungeon_NPCgenerator, id = self.Dungeon_NPCgenerator.GetId() )
		self.Bind( wx.EVT_MENU, self.OnDungeon_Monsters, id = self.Dungeon_Monster.GetId() )
		self.Bind( wx.EVT_MENU, self.OnDungeon_5EMonsters, id = self.Dungeon_Monster5E.GetId() )
		self.Bind( wx.EVT_MENU, self.OnDungeon_5E_NPC, id = self.Dungeon_NPC_5E.GetId() )
		self.Bind( wx.EVT_MENU, self.OnDungeon_5E_Spells, id = self.Dungeon_Spell_5E.GetId() )
		self.Bind( wx.EVT_MENU, self.OnDungeon_Encounters, id = self.Dungeon_Encounters.GetId() )
		self.Bind( wx.EVT_MENU, self.OnDungeon_Traps, id = self.Dungeon_Traps.GetId() )
		self.Bind( wx.EVT_MENU, self.OnDungeon_Treasures, id = self.Dungeon_Treasures.GetId() )
		self.Bind( wx.EVT_MENU, self.OnDungeon_CombatTracking, id = self.Dungeon_Combat_Tracking.GetId() )
		self.Bind( wx.EVT_MENU, self.OnDungeon_DiceRoller, id = self.Dungeon_DiceRoller.GetId() )
		self.Bind( wx.EVT_MENU, self.OnDungeon_ShowIcons, id = self.Dungeon_ShowIcons.GetId() )
		self.Bind( wx.EVT_MENU, self.OnHelp_Contents, id = self.Help_Contents.GetId() )
		self.Bind( wx.EVT_MENU, self.OnHelp_OpenTutorial, id = self.Help_OpenTutorial.GetId() )
		self.Bind( wx.EVT_MENU, self.OnHelp_ShowTips, id = self.Help_ShowTips.GetId() )
		self.Bind( wx.EVT_MENU, self.OnHelp_KeyboardShortcuts, id = self.Help_KeyboardShortcuts.GetId() )
		self.Bind( wx.EVT_MENU, self.OnHelp_ProgramFoundation, id = self.Help_ProgramFoundation.GetId() )
		self.Bind( wx.EVT_MENU, self.OnHelp_About, id = self.Help_About.GetId() )
		self.SplitterSash.Bind( wx.EVT_SPLITTER_SASH_POS_CHANGED, self.OnChangeSplitterSash )
		self.nbTileNotebook.Bind( wx.EVT_SIZE, self.OnResizeTilePanel )
		self.MapWindowZoomSlider.Bind( wx.EVT_SCROLL, self.MapWindowZoom )
		self.tgTileMode.Bind( wx.EVT_BUTTON, self.ChangeSelectionMode )
		self.tgIconMode.Bind( wx.EVT_BUTTON, self.ChangeSelectionMode )
		self.tgDrawMode.Bind( wx.EVT_BUTTON, self.ChangeSelectionMode )
		self.tgFogMode.Bind( wx.EVT_BUTTON, self.ChangeSelectionMode )
		self.cxLayerSelector.Bind( wx.EVT_CHOICE, self.ChangeActiveLayer )
		self.TileWindowZoomSlider.Bind( wx.EVT_COMMAND_SCROLL_THUMBRELEASE, self.TileWindowZoom )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnFileNew( self, event ):
		event.Skip()
	
	
	def OnFileOpen( self, event ):
		event.Skip()
	
	
	def OnFileSave( self, event ):
		event.Skip()
	
	def OnFileSaveAs( self, event ):
		event.Skip()
	
	def OnPrintMap( self, event ):
		event.Skip()
	
	def OnPrintImage( self, event ):
		event.Skip()
	
	def OnUndoAction( self, event ):
		event.Skip()
	
	def OnImportTileset( self, event ):
		event.Skip()
	
	def OnImportBackground( self, event ):
		event.Skip()
	
	def OnChangeTileQuantity( self, event ):
		event.Skip()
	
	def OnSnapToGrid( self, event ):
		event.Skip()
	
	def OnViewGrid( self, event ):
		event.Skip()
	
	def OnViewBackground( self, event ):
		event.Skip()
	
	def OnViewTilesetLayerFilter( self, event ):
		event.Skip()
	
	def OnViewIcons( self, event ):
		event.Skip()
	
	def OnViewShowIconNames( self, event ):
		event.Skip()
	
	def OnViewDrawingObjects( self, event ):
		event.Skip()
	
	def OnViewDrawingHandles( self, event ):
		event.Skip()
	
	def OnViewFogObjects( self, event ):
		event.Skip()
	
	def MapZoomIn( self, event ):
		event.Skip()
	
	def RMapClickZoomOut( self, event ):
		event.Skip()
	
	def OnHelp_Contents( self, event ):
		event.Skip()
	
	
	
	
	
	
	
	def OnImportFile( self, event ):
		event.Skip()
	
	
	def OnRecentFile1( self, event ):
		event.Skip()
	
	def OnRecentFile2( self, event ):
		event.Skip()
	
	def OnRecentFile3( self, event ):
		event.Skip()
	
	def OnRecentFile4( self, event ):
		event.Skip()
	
	def OnRecentFile5( self, event ):
		event.Skip()
	
	def OnExit( self, event ):
		event.Skip()
	
	
	def OnEditMapSize( self, event ):
		event.Skip()
	
	def OnImportTiles( self, event ):
		event.Skip()
	
	
	
	
	def OnChangeResolution( self, event ):
		event.Skip()
	
	
	def OnViewFilterTags( self, event ):
		event.Skip()
	
	
	def OnViewGridCoordinates( self, event ):
		event.Skip()
	
	def OnViewHighlightIcons( self, event ):
		event.Skip()
	
	def OnViewDualTileSides( self, event ):
		event.Skip()
	
	
	def OnViewConditionColorsLegend( self, event ):
		event.Skip()
	
	def OnViewViewAll( self, event ):
		event.Skip()
	
	
	def OnViewSecondaryScreen( self, event ):
		event.Skip()
	
	def OnUpdateToFTP( self, event ):
		event.Skip()
	
	def OnOptionsProgram( self, event ):
		event.Skip()
	
	def OnOptionsTilesets( self, event ):
		event.Skip()
	
	def OnOptionsSymbolsMarkers( self, event ):
		event.Skip()
	
	def OnOptionsText( self, event ):
		event.Skip()
	
	def OnOptionsIniFile( self, event ):
		event.Skip()
	
	def OnOptionsFTP( self, event ):
		event.Skip()
	
	def OnMapsRandomDungeon( self, event ):
		event.Skip()
	
	def OnMapsIsometric( self, event ):
		event.Skip()
	
	def OnReportsManifest( self, event ):
		event.Skip()
	
	def OnReportsTilesets( self, event ):
		event.Skip()
	
	def OnDungeon_Load_d20_Resources( self, event ):
		event.Skip()
	
	def OnDungeon_Load_DnD5_Resources( self, event ):
		event.Skip()
	
	def OnDungeon_NPCgenerator( self, event ):
		event.Skip()
	
	def OnDungeon_Monsters( self, event ):
		event.Skip()
	
	def OnDungeon_5EMonsters( self, event ):
		event.Skip()
	
	def OnDungeon_5E_NPC( self, event ):
		event.Skip()
	
	def OnDungeon_5E_Spells( self, event ):
		event.Skip()
	
	def OnDungeon_Encounters( self, event ):
		event.Skip()
	
	def OnDungeon_Traps( self, event ):
		event.Skip()
	
	def OnDungeon_Treasures( self, event ):
		event.Skip()
	
	def OnDungeon_CombatTracking( self, event ):
		event.Skip()
	
	def OnDungeon_DiceRoller( self, event ):
		event.Skip()
	
	def OnDungeon_ShowIcons( self, event ):
		event.Skip()
	
	
	def OnHelp_OpenTutorial( self, event ):
		event.Skip()
	
	def OnHelp_ShowTips( self, event ):
		event.Skip()
	
	def OnHelp_KeyboardShortcuts( self, event ):
		event.Skip()
	
	def OnHelp_ProgramFoundation( self, event ):
		event.Skip()
	
	def OnHelp_About( self, event ):
		event.Skip()
	
	def OnChangeSplitterSash( self, event ):
		event.Skip()
	
	def OnResizeTilePanel( self, event ):
		event.Skip()
	
	def MapWindowZoom( self, event ):
		event.Skip()
	
	def ChangeSelectionMode( self, event ):
		event.Skip()
	
	
	
	
	def ChangeActiveLayer( self, event ):
		event.Skip()
	
	def TileWindowZoom( self, event ):
		event.Skip()
	
	def SplitterSashOnIdle( self, event ):
		self.SplitterSash.SetSashPosition( 501 )
		self.SplitterSash.Unbind( wx.EVT_IDLE )
	

###########################################################################
## Class FTP_Options
###########################################################################

class FTP_Options ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Remote Server Details", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer626 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer627 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer634 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3301 = wx.StaticText( self, wx.ID_ANY, u"Remote image name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3301.Wrap( -1 )
		bSizer634.Add( self.m_staticText3301, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txFilename = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txFilename.SetToolTip( u"Images are saved in .png format" )
		
		bSizer634.Add( self.txFilename, 1, wx.ALL, 5 )
		
		
		bSizer627.Add( bSizer634, 1, wx.EXPAND, 5 )
		
		bSizer631 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText326 = wx.StaticText( self, wx.ID_ANY, u"Server Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText326.Wrap( -1 )
		bSizer631.Add( self.m_staticText326, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txServer = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer631.Add( self.txServer, 2, wx.ALL, 5 )
		
		
		bSizer627.Add( bSizer631, 1, wx.EXPAND, 5 )
		
		bSizer6311 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3261 = wx.StaticText( self, wx.ID_ANY, u"Username:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3261.Wrap( -1 )
		bSizer6311.Add( self.m_staticText3261, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txUsername = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6311.Add( self.txUsername, 2, wx.ALL, 5 )
		
		
		bSizer627.Add( bSizer6311, 1, wx.EXPAND, 5 )
		
		bSizer6312 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3262 = wx.StaticText( self, wx.ID_ANY, u"Password:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3262.Wrap( -1 )
		bSizer6312.Add( self.m_staticText3262, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txPassword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6312.Add( self.txPassword, 2, wx.ALL, 5 )
		
		
		bSizer627.Add( bSizer6312, 1, wx.EXPAND, 5 )
		
		bSizer637 = wx.BoxSizer( wx.VERTICAL )
		
		self.cbSaveUserInformation = wx.CheckBox( self, wx.ID_ANY, u"Remember Information (save to disk)?", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer637.Add( self.cbSaveUserInformation, 0, wx.ALL, 5 )
		
		self.m_staticText330 = wx.StaticText( self, wx.ID_ANY, u"Note:  Password information on disk is not encrypted", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText330.Wrap( -1 )
		bSizer637.Add( self.m_staticText330, 0, wx.ALL, 5 )
		
		
		bSizer627.Add( bSizer637, 0, wx.EXPAND, 5 )
		
		
		bSizer626.Add( bSizer627, 1, wx.EXPAND, 5 )
		
		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ID_OK = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_OK.SetDefault() 
		self.ID_OK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_OK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.ID_OK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer27.Add( self.ID_OK, 0, 0, 0 )
		
		self.ID_CANCEL = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_CANCEL.SetDefault() 
		self.ID_CANCEL.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_CANCEL.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ID_CANCEL.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		
		bSizer27.Add( self.ID_CANCEL, 0, wx.LEFT|wx.RIGHT, 3 )
		
		self.bHelp = wx.Button( self, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bHelp.SetDefault() 
		self.bHelp.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bHelp.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bHelp.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer27.Add( self.bHelp, 0, 0, 0 )
		
		
		bSizer626.Add( bSizer27, 0, wx.EXPAND|wx.ALL, 5 )
		
		
		self.SetSizer( bSizer626 )
		self.Layout()
		bSizer626.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.ID_OK.Bind( wx.EVT_BUTTON, self.OnOK )
		self.ID_CANCEL.Bind( wx.EVT_BUTTON, self.OnCancel )
		self.bHelp.Bind( wx.EVT_BUTTON, self.OnHelp )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnOK( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		event.Skip()
	
	def OnHelp( self, event ):
		event.Skip()
	

###########################################################################
## Class IconEditorBase
###########################################################################

class IconEditorBase ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Icon Editor", pos = wx.DefaultPosition, size = wx.Size( 650,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.FRAME_FLOAT_ON_PARENT|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.tbMainToolbar = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
		self.tbMainToolbar.AddTool( tCloseID, u"Close", wx.Bitmap( u"artwork/DeleteIcon.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.tbMainToolbar.AddTool( tOpenID, u"Open...", wx.Bitmap( u"artwork/File_Open.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.tbMainToolbar.AddTool( tSaveID, u"Save", wx.Bitmap( u"artwork/save.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.tbMainToolbar.AddSeparator()
		
		self.tbMainToolbar.AddTool( tUndoID, u"Undo", wx.Bitmap( u"artwork/undo.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.tbMainToolbar.AddTool( tRedoID, u"Redo", wx.Bitmap( u"artwork/redo.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.tbMainToolbar.AddSeparator()
		
		self.tbMainToolbar.AddTool( tCutID, u"Cut", wx.Bitmap( u"artwork/scissors.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.tbMainToolbar.AddTool( tCopyID, u"Copy", wx.Bitmap( u"artwork/clipboard copy.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.tbMainToolbar.AddTool( tPasteID, u"Paste", wx.Bitmap( u"artwork/clipboard-paste-document-text.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.tbMainToolbar.AddSeparator()
		
		self.tbMainToolbar.AddTool( tBoldID, u"Bold", wx.Bitmap( u"artwork/edit-bold.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.tbMainToolbar.AddTool( tItalicID, u"Italic", wx.Bitmap( u"artwork/edit-italic.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.tbMainToolbar.AddTool( tUnderlineID, u"Underline", wx.Bitmap( u"artwork/edit-underline.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.tbMainToolbar.AddSeparator()
		
		self.tbMainToolbar.AddTool( tLeftJustifyID, u"Left Justify", wx.Bitmap( u"artwork/justify_left.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.tbMainToolbar.AddTool( tCenterJustifyID, u"Center Justify", wx.Bitmap( u"artwork/justify_center.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.tbMainToolbar.AddTool( tRightJustifyID, u"Right Justify", wx.Bitmap( u"artwork/justify_right.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.tbMainToolbar.AddSeparator()
		
		self.tbMainToolbar.AddTool( tChangeFontID, u"Change Font", wx.Bitmap( u"artwork/font_small24.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Change Font", wx.EmptyString, None ) 
		
		self.tbMainToolbar.AddTool( tChangeColorID, u"Change Font Color", wx.Bitmap( u"artwork/font_color_small24.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Change Font Color", u"Change the font color", None ) 
		
		self.tbMainToolbar.Realize() 
		
		self.mMainMenu = wx.MenuBar( 0 )
		self.mFile = wx.Menu()
		self.mFileOpen = wx.MenuItem( self.mFile, wx.ID_ANY, u"Open..."+ u"\t" + u"CTRL+O", wx.EmptyString, wx.ITEM_NORMAL )
		self.mFile.Append( self.mFileOpen )
		
		self.mFileSave = wx.MenuItem( self.mFile, wx.ID_ANY, u"Save"+ u"\t" + u"CTRL+S", wx.EmptyString, wx.ITEM_NORMAL )
		self.mFile.Append( self.mFileSave )
		
		self.mFileSaveAs = wx.MenuItem( self.mFile, wx.ID_ANY, u"Save As..."+ u"\t" + u"F12", wx.EmptyString, wx.ITEM_NORMAL )
		self.mFile.Append( self.mFileSaveAs )
		
		self.mFile.AppendSeparator()
		
		self.mFileViewHTML = wx.MenuItem( self.mFile, wx.ID_ANY, u"View as HTML", wx.EmptyString, wx.ITEM_NORMAL )
		self.mFile.Append( self.mFileViewHTML )
		
		self.mFile.AppendSeparator()
		
		self.mFileExit = wx.MenuItem( self.mFile, wx.ID_ANY, u"Exit"+ u"\t" + u"CTRL+Q", wx.EmptyString, wx.ITEM_NORMAL )
		self.mFileExit.SetBitmap( wx.Bitmap( u"artwork/DeleteIcon.png", wx.BITMAP_TYPE_ANY ) )
		self.mFile.Append( self.mFileExit )
		
		self.mMainMenu.Append( self.mFile, u"File" ) 
		
		self.mEdit = wx.Menu()
		self.mEditUndo = wx.MenuItem( self.mEdit, wx.ID_UNDO, u"Undo"+ u"\t" + u"CTRL+Z", wx.EmptyString, wx.ITEM_NORMAL )
		self.mEdit.Append( self.mEditUndo )
		
		self.mEditRedo = wx.MenuItem( self.mEdit, wx.ID_REDO, u"Redo"+ u"\t" + u"CTRL+Y", wx.EmptyString, wx.ITEM_NORMAL )
		self.mEdit.Append( self.mEditRedo )
		
		self.mEdit.AppendSeparator()
		
		self.mEditCut = wx.MenuItem( self.mEdit, wx.ID_CUT, u"Cut"+ u"\t" + u"CTRL+X", wx.EmptyString, wx.ITEM_NORMAL )
		self.mEdit.Append( self.mEditCut )
		
		self.mEditCopy = wx.MenuItem( self.mEdit, wx.ID_COPY, u"Copy"+ u"\t" + u"CTRL+C", wx.EmptyString, wx.ITEM_NORMAL )
		self.mEdit.Append( self.mEditCopy )
		
		self.mEditPaste = wx.MenuItem( self.mEdit, wx.ID_PASTE, u"Paste"+ u"\t" + u"CTRL+V", wx.EmptyString, wx.ITEM_NORMAL )
		self.mEdit.Append( self.mEditPaste )
		
		self.mEdit.AppendSeparator()
		
		self.mEditSelectAll = wx.MenuItem( self.mEdit, wx.ID_SELECTALL, u"Select All"+ u"\t" + u"CTRL+A", wx.EmptyString, wx.ITEM_NORMAL )
		self.mEdit.Append( self.mEditSelectAll )
		
		self.mEdit.AppendSeparator()
		
		self.mEditEditDescription = wx.MenuItem( self.mEdit, EditDescriptionID, u"Edit Description", wx.EmptyString, wx.ITEM_NORMAL )
		self.mEdit.Append( self.mEditEditDescription )
		
		self.mMainMenu.Append( self.mEdit, u"Edit" ) 
		
		self.mFormat = wx.Menu()
		self.mFormatBold = wx.MenuItem( self.mFormat, wx.ID_ANY, u"Bold"+ u"\t" + u"CTRL+B", wx.EmptyString, wx.ITEM_CHECK )
		self.mFormat.Append( self.mFormatBold )
		
		self.mFormatItalic = wx.MenuItem( self.mFormat, wx.ID_ANY, u"Italic"+ u"\t" + u"CTRL+I", wx.EmptyString, wx.ITEM_CHECK )
		self.mFormat.Append( self.mFormatItalic )
		
		self.mFormatUnderline = wx.MenuItem( self.mFormat, wx.ID_ANY, u"Underline"+ u"\t" + u"CTRL+U", wx.EmptyString, wx.ITEM_CHECK )
		self.mFormat.Append( self.mFormatUnderline )
		
		self.mFormat.AppendSeparator()
		
		self.mFormatLeftAlign = wx.MenuItem( self.mFormat, wx.ID_ANY, u"Left Align", wx.EmptyString, wx.ITEM_RADIO )
		self.mFormat.Append( self.mFormatLeftAlign )
		
		self.mFormatCenterAlign = wx.MenuItem( self.mFormat, wx.ID_ANY, u"Center Align", wx.EmptyString, wx.ITEM_RADIO )
		self.mFormat.Append( self.mFormatCenterAlign )
		
		self.mFormatRightAlign = wx.MenuItem( self.mFormat, wx.ID_ANY, u"Right Align", wx.EmptyString, wx.ITEM_RADIO )
		self.mFormat.Append( self.mFormatRightAlign )
		
		self.mFormat.AppendSeparator()
		
		self.mFormatIndentMore = wx.MenuItem( self.mFormat, wx.ID_ANY, u"Indent More", wx.EmptyString, wx.ITEM_NORMAL )
		self.mFormat.Append( self.mFormatIndentMore )
		
		self.mFormatIndentLess = wx.MenuItem( self.mFormat, wx.ID_ANY, u"Indent Less", wx.EmptyString, wx.ITEM_NORMAL )
		self.mFormat.Append( self.mFormatIndentLess )
		
		self.mFormat.AppendSeparator()
		
		self.mFormatIncreaseParagraphSpacing = wx.MenuItem( self.mFormat, wx.ID_ANY, u"Increase Paragraph Spacing", wx.EmptyString, wx.ITEM_NORMAL )
		self.mFormat.Append( self.mFormatIncreaseParagraphSpacing )
		
		self.mFormatDecreaseParagraphSpacing = wx.MenuItem( self.mFormat, wx.ID_ANY, u"Decrease Paragraph Spacing", wx.EmptyString, wx.ITEM_NORMAL )
		self.mFormat.Append( self.mFormatDecreaseParagraphSpacing )
		
		self.mFormat.AppendSeparator()
		
		self.mFormatNormalLineSpacing = wx.MenuItem( self.mFormat, wx.ID_ANY, u"Normal Line Spacing", wx.EmptyString, wx.ITEM_NORMAL )
		self.mFormat.Append( self.mFormatNormalLineSpacing )
		
		self.mFormatHalfLineSpacing = wx.MenuItem( self.mFormat, wx.ID_ANY, u"1.5 Line Spacing", wx.EmptyString, wx.ITEM_NORMAL )
		self.mFormat.Append( self.mFormatHalfLineSpacing )
		
		self.mFormatDoubleLineSpacing = wx.MenuItem( self.mFormat, wx.ID_ANY, u"Double Line Spacing", wx.EmptyString, wx.ITEM_NORMAL )
		self.mFormat.Append( self.mFormatDoubleLineSpacing )
		
		self.mFormat.AppendSeparator()
		
		self.mFormatFont = wx.MenuItem( self.mFormat, wx.ID_ANY, u"Font...", wx.EmptyString, wx.ITEM_NORMAL )
		self.mFormat.Append( self.mFormatFont )
		
		self.mMainMenu.Append( self.mFormat, u"Format" ) 
		
		self.mPrint = wx.Menu()
		self.mPrintPrint = wx.MenuItem( self.mPrint, wx.ID_ANY, u"Print..."+ u"\t" + u"CTRL+P", wx.EmptyString, wx.ITEM_NORMAL )
		self.mPrint.Append( self.mPrintPrint )
		
		self.mMainMenu.Append( self.mPrint, u"Print" ) 
		
		self.mRpg = wx.Menu()
		self.mRpgAddNPC = wx.MenuItem( self.mRpg, NPC_menuID, u"Add NPC...", wx.EmptyString, wx.ITEM_NORMAL )
		self.mRpgAddNPC.SetBitmap( wx.Bitmap( u"artwork/npc_icon_small.png", wx.BITMAP_TYPE_ANY ) )
		self.mRpg.Append( self.mRpgAddNPC )
		
		self.mRpgAddMonster = wx.MenuItem( self.mRpg, Monster_menuID, u"Add Monster...", wx.EmptyString, wx.ITEM_NORMAL )
		self.mRpgAddMonster.SetBitmap( wx.Bitmap( u"artwork/monster_icon_small.png", wx.BITMAP_TYPE_ANY ) )
		self.mRpg.Append( self.mRpgAddMonster )
		
		self.mRpg.AppendSeparator()
		
		self.mRpgAdd5ENPC = wx.MenuItem( self.mRpg, NPC5E_menuID, u"Add 5E NPC...", wx.EmptyString, wx.ITEM_NORMAL )
		self.mRpgAdd5ENPC.SetBitmap( wx.Bitmap( u"artwork/npc.png", wx.BITMAP_TYPE_ANY ) )
		self.mRpg.Append( self.mRpgAdd5ENPC )
		
		self.mRpgAdd5EMonster = wx.MenuItem( self.mRpg, Monster5E_menuID, u"Add 5E Monster", wx.EmptyString, wx.ITEM_NORMAL )
		self.mRpgAdd5EMonster.SetBitmap( wx.Bitmap( u"artwork/5E_monster.png", wx.BITMAP_TYPE_ANY ) )
		self.mRpg.Append( self.mRpgAdd5EMonster )
		
		self.mRpg.AppendSeparator()
		
		self.mRpgAddTrap = wx.MenuItem( self.mRpg, Trap_menuID, u"Add Trap...", wx.EmptyString, wx.ITEM_NORMAL )
		self.mRpgAddTrap.SetBitmap( wx.Bitmap( u"artwork/trap.png", wx.BITMAP_TYPE_ANY ) )
		self.mRpg.Append( self.mRpgAddTrap )
		
		self.mRpgAddTreasure = wx.MenuItem( self.mRpg, Treasure_menuID, u"Add Treasure...", wx.EmptyString, wx.ITEM_NORMAL )
		self.mRpgAddTreasure.SetBitmap( wx.Bitmap( u"artwork/treasure_icon_small.png", wx.BITMAP_TYPE_ANY ) )
		self.mRpg.Append( self.mRpgAddTreasure )
		
		self.mMainMenu.Append( self.mRpg, u"RPG Items" ) 
		
		self.SetMenuBar( self.mMainMenu )
		
		bSizer532 = wx.BoxSizer( wx.VERTICAL )
		
		self.tbIconTools = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL ) 
		self.tbIconTools.AddTool( roomID, u"Information", wx.Bitmap( u"artwork/scroll_small24.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_RADIO, u"Room Information", wx.EmptyString, None ) 
		
		self.tbIconTools.AddTool( monsterID, u"Monster", wx.Bitmap( u"artwork/monster_icon_small24.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_RADIO, wx.EmptyString, wx.EmptyString, None ) 
		
		self.tbIconTools.AddTool( trapID, u"Trap", wx.Bitmap( u"artwork/trap_small24.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_RADIO, wx.EmptyString, wx.EmptyString, None ) 
		
		self.tbIconTools.AddTool( npcID, u"NPC", wx.Bitmap( u"artwork/npc_small24.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_RADIO, wx.EmptyString, wx.EmptyString, None ) 
		
		self.tbIconTools.AddTool( treasureID, u"Treasure", wx.Bitmap( u"artwork/treasure_small24.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_RADIO, wx.EmptyString, wx.EmptyString, None ) 
		
		self.tbIconTools.AddTool( markerID, u"Symbol", wx.Bitmap( u"artwork/marker_icon_small24.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_RADIO, wx.EmptyString, wx.EmptyString, None ) 
		
		self.tbIconTools.AddSeparator()
		
		cxIconSizeChoices = [ u"1 x 1", u"2 x 2", u"3 x 3", u"4 x 4", u"5 x 5" ]
		self.cxIconSize = wx.Choice( self.tbIconTools, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cxIconSizeChoices, 0 )
		self.cxIconSize.SetSelection( 0 )
		self.cxIconSize.SetToolTip( u"Icon Size in Map Window" )
		
		self.tbIconTools.AddControl( self.cxIconSize )
		self.tbIconTools.Realize() 
		
		bSizer532.Add( self.tbIconTools, 0, wx.EXPAND, 5 )
		
		self.pnMainpanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer534 = wx.BoxSizer( wx.VERTICAL )
		
		self.rtc = wx.richtext.RichTextCtrl( self.pnMainpanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.rtc.SetFont( wx.Font( 11, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer534.Add( self.rtc, 1, wx.EXPAND, 5 )
		
		
		self.pnMainpanel.SetSizer( bSizer534 )
		self.pnMainpanel.Layout()
		bSizer534.Fit( self.pnMainpanel )
		bSizer532.Add( self.pnMainpanel, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer532 )
		self.Layout()
		self.m_statusBar2 = self.CreateStatusBar( 2, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_TOOL, self.OnFileExit, id = tCloseID )
		self.Bind( wx.EVT_TOOL, self.OnFileOpen, id = tOpenID )
		self.Bind( wx.EVT_TOOL, self.OnFileSave, id = tSaveID )
		self.Bind( wx.EVT_TOOL, self.ForwardEvent, id = tUndoID )
		self.Bind( wx.EVT_TOOL, self.ForwardEvent, id = tRedoID )
		self.Bind( wx.EVT_TOOL, self.ForwardEvent, id = tCutID )
		self.Bind( wx.EVT_TOOL, self.ForwardEvent, id = tCopyID )
		self.Bind( wx.EVT_TOOL, self.ForwardEvent, id = tPasteID )
		self.Bind( wx.EVT_TOOL, self.OnBold, id = tBoldID )
		self.Bind( wx.EVT_TOOL, self.OnItalic, id = tItalicID )
		self.Bind( wx.EVT_TOOL, self.OnUnderline, id = tUnderlineID )
		self.Bind( wx.EVT_TOOL, self.OnAlignLeft, id = tLeftJustifyID )
		self.Bind( wx.EVT_TOOL, self.OnAlignCenter, id = tCenterJustifyID )
		self.Bind( wx.EVT_TOOL, self.OnAlignRight, id = tRightJustifyID )
		self.Bind( wx.EVT_TOOL, self.OnFont, id = tChangeFontID )
		self.Bind( wx.EVT_TOOL, self.OnColour, id = tChangeColorID )
		self.Bind( wx.EVT_MENU, self.OnFileOpen, id = self.mFileOpen.GetId() )
		self.Bind( wx.EVT_MENU, self.OnFileSave, id = self.mFileSave.GetId() )
		self.Bind( wx.EVT_MENU, self.OnFileSaveAs, id = self.mFileSaveAs.GetId() )
		self.Bind( wx.EVT_MENU, self.OnFileViewHTML, id = self.mFileViewHTML.GetId() )
		self.Bind( wx.EVT_MENU, self.OnFileExit, id = self.mFileExit.GetId() )
		self.Bind( wx.EVT_MENU, self.ForwardEvent, id = self.mEditUndo.GetId() )
		self.Bind( wx.EVT_MENU, self.ForwardEvent, id = self.mEditRedo.GetId() )
		self.Bind( wx.EVT_MENU, self.ForwardEvent, id = self.mEditCut.GetId() )
		self.Bind( wx.EVT_MENU, self.ForwardEvent, id = self.mEditCopy.GetId() )
		self.Bind( wx.EVT_MENU, self.ForwardEvent, id = self.mEditPaste.GetId() )
		self.Bind( wx.EVT_MENU, self.ForwardEvent, id = self.mEditSelectAll.GetId() )
		self.Bind( wx.EVT_MENU, self.EditDescription, id = self.mEditEditDescription.GetId() )
		self.Bind( wx.EVT_MENU, self.OnUpdateBold, id = self.mFormatBold.GetId() )
		self.Bind( wx.EVT_MENU, self.OnUpdateItalic, id = self.mFormatItalic.GetId() )
		self.Bind( wx.EVT_MENU, self.OnUpdateUnderline, id = self.mFormatUnderline.GetId() )
		self.Bind( wx.EVT_MENU, self.OnUpdateAlignLeft, id = self.mFormatLeftAlign.GetId() )
		self.Bind( wx.EVT_MENU, self.OnUpdateAlignCenter, id = self.mFormatCenterAlign.GetId() )
		self.Bind( wx.EVT_MENU, self.OnUpdateAlignRight, id = self.mFormatRightAlign.GetId() )
		self.Bind( wx.EVT_MENU, self.OnIndentMore, id = self.mFormatIndentMore.GetId() )
		self.Bind( wx.EVT_MENU, self.OnIndentLess, id = self.mFormatIndentLess.GetId() )
		self.Bind( wx.EVT_MENU, self.OnParagraphSpacingMore, id = self.mFormatIncreaseParagraphSpacing.GetId() )
		self.Bind( wx.EVT_MENU, self.OnParagraphSpacingLess, id = self.mFormatDecreaseParagraphSpacing.GetId() )
		self.Bind( wx.EVT_MENU, self.OnLineSpacingSingle, id = self.mFormatNormalLineSpacing.GetId() )
		self.Bind( wx.EVT_MENU, self.OnLineSpacingHalf, id = self.mFormatHalfLineSpacing.GetId() )
		self.Bind( wx.EVT_MENU, self.OnLineSpacingDouble, id = self.mFormatDoubleLineSpacing.GetId() )
		self.Bind( wx.EVT_MENU, self.OnFont, id = self.mFormatFont.GetId() )
		self.Bind( wx.EVT_MENU, self.OnFilePrint, id = self.mPrintPrint.GetId() )
		self.Bind( wx.EVT_MENU, self.AddNPC, id = self.mRpgAddNPC.GetId() )
		self.Bind( wx.EVT_MENU, self.AddMonster, id = self.mRpgAddMonster.GetId() )
		self.Bind( wx.EVT_MENU, self.Add5E_NPC, id = self.mRpgAdd5ENPC.GetId() )
		self.Bind( wx.EVT_MENU, self.Add5E_Monster, id = self.mRpgAdd5EMonster.GetId() )
		self.Bind( wx.EVT_MENU, self.AddTrap, id = self.mRpgAddTrap.GetId() )
		self.Bind( wx.EVT_MENU, self.AddTreasure, id = self.mRpgAddTreasure.GetId() )
		self.Bind( wx.EVT_TOOL, self.SetIcon, id = roomID )
		self.Bind( wx.EVT_TOOL, self.SetIcon, id = monsterID )
		self.Bind( wx.EVT_TOOL, self.SetIcon, id = trapID )
		self.Bind( wx.EVT_TOOL, self.SetIcon, id = npcID )
		self.Bind( wx.EVT_TOOL, self.SetIcon, id = treasureID )
		self.Bind( wx.EVT_TOOL, self.SetIcon, id = markerID )
		self.cxIconSize.Bind( wx.EVT_CHOICE, self.SetIconSize )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnFileExit( self, event ):
		event.Skip()
	
	def OnFileOpen( self, event ):
		event.Skip()
	
	def OnFileSave( self, event ):
		event.Skip()
	
	def ForwardEvent( self, event ):
		event.Skip()
	
	
	
	
	
	def OnBold( self, event ):
		event.Skip()
	
	def OnItalic( self, event ):
		event.Skip()
	
	def OnUnderline( self, event ):
		event.Skip()
	
	def OnAlignLeft( self, event ):
		event.Skip()
	
	def OnAlignCenter( self, event ):
		event.Skip()
	
	def OnAlignRight( self, event ):
		event.Skip()
	
	def OnFont( self, event ):
		event.Skip()
	
	def OnColour( self, event ):
		event.Skip()
	
	
	
	def OnFileSaveAs( self, event ):
		event.Skip()
	
	def OnFileViewHTML( self, event ):
		event.Skip()
	
	
	
	
	
	
	
	
	def EditDescription( self, event ):
		event.Skip()
	
	def OnUpdateBold( self, event ):
		event.Skip()
	
	def OnUpdateItalic( self, event ):
		event.Skip()
	
	def OnUpdateUnderline( self, event ):
		event.Skip()
	
	def OnUpdateAlignLeft( self, event ):
		event.Skip()
	
	def OnUpdateAlignCenter( self, event ):
		event.Skip()
	
	def OnUpdateAlignRight( self, event ):
		event.Skip()
	
	def OnIndentMore( self, event ):
		event.Skip()
	
	def OnIndentLess( self, event ):
		event.Skip()
	
	def OnParagraphSpacingMore( self, event ):
		event.Skip()
	
	def OnParagraphSpacingLess( self, event ):
		event.Skip()
	
	def OnLineSpacingSingle( self, event ):
		event.Skip()
	
	def OnLineSpacingHalf( self, event ):
		event.Skip()
	
	def OnLineSpacingDouble( self, event ):
		event.Skip()
	
	
	def OnFilePrint( self, event ):
		event.Skip()
	
	def AddNPC( self, event ):
		event.Skip()
	
	def AddMonster( self, event ):
		event.Skip()
	
	def Add5E_NPC( self, event ):
		event.Skip()
	
	def Add5E_Monster( self, event ):
		event.Skip()
	
	def AddTrap( self, event ):
		event.Skip()
	
	def AddTreasure( self, event ):
		event.Skip()
	
	def SetIcon( self, event ):
		event.Skip()
	
	
	
	
	
	
	def SetIconSize( self, event ):
		event.Skip()
	

###########################################################################
## Class TilesetManifestDialogBase
###########################################################################

class TilesetManifestDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tileset Manifest", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.txTextBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,250 ), wx.TE_MULTILINE )
		self.txTextBox.SetMaxLength( 0 ) 
		bSizer3.Add( self.txTextBox, 0, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bClose = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bClose.SetDefault() 
		self.bClose.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bClose.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.bClose.SetBackgroundColour( wx.Colour( 0, 64, 0 ) )
		
		bSizer2.Add( self.bClose, 0, wx.ALL, 5 )
		
		self.bCopyClipboard = wx.Button( self, wx.ID_ANY, u"Copy to clipboard", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bCopyClipboard.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bCopyClipboard.SetForegroundColour( wx.Colour( 255, 128, 0 ) )
		self.bCopyClipboard.SetBackgroundColour( wx.Colour( 0, 0, 160 ) )
		
		bSizer2.Add( self.bCopyClipboard, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 0, wx.ALIGN_BOTTOM|wx.SHAPED, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.bClose.Bind( wx.EVT_BUTTON, self.OnClose )
		self.bCopyClipboard.Bind( wx.EVT_BUTTON, self.OnCopyToClipboard )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()
	
	def OnCopyToClipboard( self, event ):
		event.Skip()
	

###########################################################################
## Class DrawingToolsDialogBase
###########################################################################

class DrawingToolsDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Drawing Tools", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.Size( -1,-1 ) )
		
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bSelectItem = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/draw_select.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bSelectItem.SetBitmapHover( wx.Bitmap( u"artwork/draw_select_selected.png", wx.BITMAP_TYPE_ANY ) )
		self.bSelectItem.SetToolTip( u"Select item by clicking on the handle boxes.  Modify by dragging them." )
		
		bSizer2.Add( self.bSelectItem, 1, wx.ALL, 0 )
		
		self.bDeleteItem = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/draw_DeleteIcon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bDeleteItem.SetBitmapHover( wx.Bitmap( u"artwork/draw_DeleteIcon_selected.png", wx.BITMAP_TYPE_ANY ) )
		self.bDeleteItem.SetToolTip( u"Delete selected item" )
		
		bSizer2.Add( self.bDeleteItem, 1, wx.ALL, 0 )
		
		self.bShowHandles = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/draw_show_handles.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bShowHandles.SetToolTip( u"Click to turn off handle display.  Activating the select tool will automatically turn this back on." )
		
		bSizer2.Add( self.bShowHandles, 1, wx.EXPAND, 0 )
		
		
		bSizer1.Add( bSizer2, 0, 0, 0 )
		
		bSizer467 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bChooseOutlineColor = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 67, 84, 233 ), wx.DefaultPosition, wx.Size( -1,-1 ), wx.CLRP_DEFAULT_STYLE )
		self.bChooseOutlineColor.SetToolTip( u"Change Outline Color" )
		
		bSizer467.Add( self.bChooseOutlineColor, 1, wx.EXPAND, 0 )
		
		self.bChooseFillColor = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 0, 128, 0 ), wx.DefaultPosition, wx.Size( -1,-1 ), wx.CLRP_DEFAULT_STYLE )
		self.bChooseFillColor.SetToolTip( u"Change Fill Color" )
		
		bSizer467.Add( self.bChooseFillColor, 1, wx.EXPAND, 0 )
		
		
		bSizer1.Add( bSizer467, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bDrawFilledCircle = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/draw_filled_circle.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bDrawFilledCircle.SetBitmapHover( wx.Bitmap( u"artwork/draw_filled_circle_selected.png", wx.BITMAP_TYPE_ANY ) )
		self.bDrawFilledCircle.SetToolTip( u"Draw filled circle; first click to set center, second click to set radius" )
		
		bSizer3.Add( self.bDrawFilledCircle, 0, wx.ALL, 0 )
		
		self.bDrawOutlinedCircle = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/draw_open_circle.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bDrawOutlinedCircle.SetBitmapHover( wx.Bitmap( u"artwork/draw_open_circle_selected.png", wx.BITMAP_TYPE_ANY ) )
		self.bDrawOutlinedCircle.SetToolTip( u"Draw outlined circle; first click to set center, second click to set radius" )
		
		bSizer3.Add( self.bDrawOutlinedCircle, 0, 0, 0 )
		
		self.bDrawFilledRectangle = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/draw_filled_rectangle.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bDrawFilledRectangle.SetBitmapHover( wx.Bitmap( u"artwork/draw_filled_rectangle_selected.png", wx.BITMAP_TYPE_ANY ) )
		self.bDrawFilledRectangle.SetToolTip( u"Draw filled rectangle; first click to set corner, second click to set other corner." )
		
		bSizer3.Add( self.bDrawFilledRectangle, 0, wx.ALL, 0 )
		
		self.bDrawOutlinedRectangle = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/draw_open_rectangle.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bDrawOutlinedRectangle.SetBitmapHover( wx.Bitmap( u"artwork/draw_open_rectangle_selected.png", wx.BITMAP_TYPE_ANY ) )
		self.bDrawOutlinedRectangle.SetToolTip( u"Draw outlined rectangle; first click to set corner, second click to set other corner." )
		
		bSizer3.Add( self.bDrawOutlinedRectangle, 0, wx.ALL, 0 )
		
		self.bChangeProperties = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/draw_change_properties.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bChangeProperties.SetBitmapHover( wx.Bitmap( u"artwork/draw_change_properties_selected.png", wx.BITMAP_TYPE_ANY ) )
		self.bChangeProperties.SetToolTip( u"Change the properties to the current color, fill, and linestyle." )
		
		bSizer3.Add( self.bChangeProperties, 0, 0, 5 )
		
		
		bSizer1.Add( bSizer3, 0, 0, 0 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bDrawLine = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/draw_line.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bDrawLine.SetBitmapHover( wx.Bitmap( u"artwork/draw_line_selected.png", wx.BITMAP_TYPE_ANY ) )
		self.bDrawLine.SetToolTip( u"Draw straight line" )
		
		bSizer4.Add( self.bDrawLine, 0, wx.ALL, 0 )
		
		self.bDrawMultiline = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/draw_line_segments.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bDrawMultiline.SetBitmapHover( wx.Bitmap( u"artwork/draw_line_segments_selected.png", wx.BITMAP_TYPE_ANY ) )
		self.bDrawMultiline.SetToolTip( u"Draw multiline.  Press spacebar to end the line." )
		
		bSizer4.Add( self.bDrawMultiline, 0, wx.ALL, 0 )
		
		self.bDrawFreehand = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/draw_freehand.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bDrawFreehand.SetBitmapHover( wx.Bitmap( u"artwork/draw_freehand_selected.png", wx.BITMAP_TYPE_ANY ) )
		self.bDrawFreehand.SetToolTip( u"Draw freehand line.  Click to start, click to end." )
		
		bSizer4.Add( self.bDrawFreehand, 0, wx.ALL, 0 )
		
		self.bImportCustomImage = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/draw_insert_custom.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bImportCustomImage.SetBitmapHover( wx.Bitmap( u"artwork/draw_insert_custom_selected.png", wx.BITMAP_TYPE_ANY ) )
		self.bImportCustomImage.SetToolTip( u"Import custom image. Click to select the top-left corner of the image." )
		
		bSizer4.Add( self.bImportCustomImage, 0, wx.ALL, 0 )
		
		self.bGetProperties = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/draw_get_properties.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bGetProperties.SetBitmapHover( wx.Bitmap( u"artwork/draw_get_properties_selected.png", wx.BITMAP_TYPE_ANY ) )
		self.bGetProperties.SetToolTip( u"Get the properties (color, fill, linestyle) from the selected item." )
		
		bSizer4.Add( self.bGetProperties, 0, 0, 5 )
		
		
		bSizer1.Add( bSizer4, 0, 0, 0 )
		
		bSizer370 = wx.BoxSizer( wx.VERTICAL )
		
		self.bDrawPoint = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/draw_point.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bDrawPoint.SetBitmapHover( wx.Bitmap( u"artwork/draw_point_selected.png", wx.BITMAP_TYPE_ANY ) )
		self.bDrawPoint.SetToolTip( u"Draw a single point.  The line width setting controls the radius of the point." )
		
		bSizer370.Add( self.bDrawPoint, 0, 0, 5 )
		
		
		bSizer1.Add( bSizer370, 1, wx.EXPAND, 5 )
		
		bSizer27 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stPanelDescription = wx.StaticText( self, wx.ID_ANY, u"Line Width:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stPanelDescription.Wrap( -1 )
		bSizer28.Add( self.stPanelDescription, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.spLineWidth = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 45,-1 ), wx.SP_ARROW_KEYS, 1, 20, 3 )
		self.spLineWidth.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.spLineWidth.SetToolTip( u"Adjusts the line width in pixels" )
		
		bSizer28.Add( self.spLineWidth, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		bSizer27.Add( bSizer28, 0, wx.EXPAND, 2 )
		
		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stLineStyle = wx.StaticText( self, wx.ID_ANY, u"Line Style: Solid", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stLineStyle.Wrap( -1 )
		bSizer31.Add( self.stLineStyle, 1, wx.ALL, 2 )
		
		self.bResetLineStyle = wx.Button( self, wx.ID_ANY, u"RESET", wx.DefaultPosition, wx.Size( 45,15 ), 0 )
		self.bResetLineStyle.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.bResetLineStyle.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bResetLineStyle.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		self.bResetLineStyle.SetToolTip( u"Reset to solid line style" )
		
		bSizer31.Add( self.bResetLineStyle, 0, wx.ALL, 2 )
		
		
		bSizer27.Add( bSizer31, 0, wx.EXPAND, 0 )
		
		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.spLineStyleSelector = wx.SpinButton( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_VERTICAL )
		self.spLineStyleSelector.SetToolTip( u"Click the buttons to change the line style" )
		
		bSizer30.Add( self.spLineStyleSelector, 0, wx.ALL|wx.EXPAND, 0 )
		
		self.pnLineStyleExample = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		self.pnLineStyleExample.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.pnLineStyleExample.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		self.pnLineStyleExample.SetToolTip( u"Sample Line and Fill.  Vertical black lines show when transparency is changed." )
		self.pnLineStyleExample.SetMinSize( wx.Size( -1,30 ) )
		
		bSizer30.Add( self.pnLineStyleExample, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		bSizer27.Add( bSizer30, 1, wx.EXPAND, 2 )
		
		bSizer29 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Fill Transparency", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer29.Add( self.m_staticText9, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 2 )
		
		self.slFillTransparency = wx.Slider( self, wx.ID_ANY, 255, 0, 255, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.slFillTransparency, 0, wx.EXPAND, 1 )
		
		bSizer301 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		bSizer301.Add( self.m_staticText10, 1, wx.ALIGN_LEFT, 0 )
		
		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"Opaque", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )
		bSizer301.Add( self.m_staticText101, 0, wx.ALIGN_RIGHT, 0 )
		
		
		bSizer29.Add( bSizer301, 0, wx.EXPAND, 0 )
		
		
		bSizer27.Add( bSizer29, 0, wx.EXPAND, 0 )
		
		
		bSizer1.Add( bSizer27, 0, wx.EXPAND, 0 )
		
		
		bSizer25.Add( bSizer1, 0, wx.EXPAND, 0 )
		
		
		self.SetSizer( bSizer25 )
		self.Layout()
		bSizer25.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.bSelectItem.Bind( wx.EVT_BUTTON, self.OnSelectItem )
		self.bDeleteItem.Bind( wx.EVT_BUTTON, self.OnDeleteItem )
		self.bShowHandles.Bind( wx.EVT_BUTTON, self.OnShowHandles )
		self.bChooseOutlineColor.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnChooseOutlineColor )
		self.bChooseFillColor.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnChooseFillColor )
		self.bDrawFilledCircle.Bind( wx.EVT_BUTTON, self.OnDrawFilledCircle )
		self.bDrawOutlinedCircle.Bind( wx.EVT_BUTTON, self.OnDrawOutlinedCircle )
		self.bDrawFilledRectangle.Bind( wx.EVT_BUTTON, self.OnDrawFilledRectangle )
		self.bDrawOutlinedRectangle.Bind( wx.EVT_BUTTON, self.OnDrawOutlinedRectangle )
		self.bChangeProperties.Bind( wx.EVT_BUTTON, self.OnChangeProperty )
		self.bDrawLine.Bind( wx.EVT_BUTTON, self.OnDrawLine )
		self.bDrawMultiline.Bind( wx.EVT_BUTTON, self.OnDrawMultiline )
		self.bDrawFreehand.Bind( wx.EVT_BUTTON, self.OnDrawFreehand )
		self.bImportCustomImage.Bind( wx.EVT_BUTTON, self.OnImportCustomImage )
		self.bGetProperties.Bind( wx.EVT_BUTTON, self.OnGetProperty )
		self.bDrawPoint.Bind( wx.EVT_BUTTON, self.OnDrawPoint )
		self.spLineWidth.Bind( wx.EVT_SPINCTRL, self.OnChangeLineWidth )
		self.bResetLineStyle.Bind( wx.EVT_BUTTON, self.OnResetLineStyle )
		self.spLineStyleSelector.Bind( wx.EVT_SPIN_DOWN, self.OnChangeLineStyleDown )
		self.spLineStyleSelector.Bind( wx.EVT_SPIN_UP, self.OnChangeLineStyleUp )
		self.pnLineStyleExample.Bind( wx.EVT_PAINT, self.OnPaint )
		self.slFillTransparency.Bind( wx.EVT_SCROLL, self.OnChangeTransparency )
		self.slFillTransparency.Bind( wx.EVT_SCROLL_CHANGED, self.OnChangeTransparency )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSelectItem( self, event ):
		event.Skip()
	
	def OnDeleteItem( self, event ):
		event.Skip()
	
	def OnShowHandles( self, event ):
		event.Skip()
	
	def OnChooseOutlineColor( self, event ):
		event.Skip()
	
	def OnChooseFillColor( self, event ):
		event.Skip()
	
	def OnDrawFilledCircle( self, event ):
		event.Skip()
	
	def OnDrawOutlinedCircle( self, event ):
		event.Skip()
	
	def OnDrawFilledRectangle( self, event ):
		event.Skip()
	
	def OnDrawOutlinedRectangle( self, event ):
		event.Skip()
	
	def OnChangeProperty( self, event ):
		event.Skip()
	
	def OnDrawLine( self, event ):
		event.Skip()
	
	def OnDrawMultiline( self, event ):
		event.Skip()
	
	def OnDrawFreehand( self, event ):
		event.Skip()
	
	def OnImportCustomImage( self, event ):
		event.Skip()
	
	def OnGetProperty( self, event ):
		event.Skip()
	
	def OnDrawPoint( self, event ):
		event.Skip()
	
	def OnChangeLineWidth( self, event ):
		event.Skip()
	
	def OnResetLineStyle( self, event ):
		event.Skip()
	
	def OnChangeLineStyleDown( self, event ):
		event.Skip()
	
	def OnChangeLineStyleUp( self, event ):
		event.Skip()
	
	def OnPaint( self, event ):
		event.Skip()
	
	def OnChangeTransparency( self, event ):
		event.Skip()
	
	

###########################################################################
## Class FogToolsDialogBase
###########################################################################

class FogToolsDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Fog of War Tools", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.Size( -1,-1 ) )
		
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bConcealAll = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/fog_conceal_all.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bConcealAll.SetBitmapHover( wx.Bitmap( u"artwork/fog_conceal_all_selected.png", wx.BITMAP_TYPE_ANY ) )
		self.bConcealAll.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.bConcealAll.SetToolTip( u"Cover the entire map with fog" )
		
		bSizer3.Add( self.bConcealAll, 0, 0, 5 )
		
		self.bDrawFilledCircle = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/fog_filled_circle.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bDrawFilledCircle.SetBitmapHover( wx.Bitmap( u"artwork/fog_filled_circle_selected.png", wx.BITMAP_TYPE_ANY ) )
		self.bDrawFilledCircle.SetToolTip( u"Add a fog circle" )
		
		bSizer3.Add( self.bDrawFilledCircle, 0, wx.ALL, 0 )
		
		self.bDrawFilledRectangle = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/fog_filled_rectangle.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bDrawFilledRectangle.SetBitmapHover( wx.Bitmap( u"artwork/fog_filled_rectangle_selected.png", wx.BITMAP_TYPE_ANY ) )
		self.bDrawFilledRectangle.SetToolTip( u"Add a fog rectangle" )
		
		bSizer3.Add( self.bDrawFilledRectangle, 0, wx.ALL, 0 )
		
		bSizer2811 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bAddFog = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/fog_brush.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bAddFog.SetBitmapHover( wx.Bitmap( u"artwork/fog_brush_selected.png", wx.BITMAP_TYPE_ANY ) )
		self.bAddFog.SetToolTip( u"Add fog to the display using the current brush radius" )
		
		bSizer2811.Add( self.bAddFog, 0, wx.ALL, 0 )
		
		self.stPanelDescription11 = wx.StaticText( self, wx.ID_ANY, u"Brush Radius:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stPanelDescription11.Wrap( 0 )
		bSizer2811.Add( self.stPanelDescription11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.spAddBrushRadius = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 45,-1 ), wx.SP_ARROW_KEYS, 1, 40, 5 )
		self.spAddBrushRadius.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.spAddBrushRadius.SetToolTip( u"Adjusts the brush radius in feet.  Change scale in Program Options" )
		
		bSizer2811.Add( self.spAddBrushRadius, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
		
		
		bSizer3.Add( bSizer2811, 0, wx.EXPAND, 5 )
		
		bSizer282 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bDrawLine = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/draw_line.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bDrawLine.SetBitmapHover( wx.Bitmap( u"artwork/draw_line_selected.png", wx.BITMAP_TYPE_ANY ) )
		self.bDrawLine.SetToolTip( u"Add fog line" )
		
		bSizer282.Add( self.bDrawLine, 0, wx.ALL, 0 )
		
		self.bDrawMultiline = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/draw_line_segments.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bDrawMultiline.SetBitmapHover( wx.Bitmap( u"artwork/draw_line_segments_selected.png", wx.BITMAP_TYPE_ANY ) )
		self.bDrawMultiline.SetToolTip( u"Add fog multiline" )
		
		bSizer282.Add( self.bDrawMultiline, 0, wx.ALL, 0 )
		
		self.stPanelDescription2 = wx.StaticText( self, wx.ID_ANY, u"Line Width:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stPanelDescription2.Wrap( 0 )
		bSizer282.Add( self.stPanelDescription2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.spAddLineWidth = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 45,-1 ), wx.SP_ARROW_KEYS, 1, 20, 5 )
		self.spAddLineWidth.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.spAddLineWidth.SetToolTip( u"Adjusts the line width in feet.  Change scale in Program Options" )
		
		bSizer282.Add( self.spAddLineWidth, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
		
		
		bSizer3.Add( bSizer282, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer3, 0, 0, 0 )
		
		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bRevealAll = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/fog_reveal_all.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bRevealAll.SetBitmapHover( wx.Bitmap( u"artwork/fog_reveal_all_selected.png", wx.BITMAP_TYPE_ANY ) )
		self.bRevealAll.SetToolTip( u"Remove all fog from the map" )
		
		bSizer31.Add( self.bRevealAll, 0, 0, 5 )
		
		self.bRemoveFilledCircle = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/fog_remove_filled_circle.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bRemoveFilledCircle.SetBitmapHover( wx.Bitmap( u"artwork/fog_remove_filled_circle_selected.png", wx.BITMAP_TYPE_ANY ) )
		self.bRemoveFilledCircle.SetToolTip( u"Remove circle fog" )
		
		bSizer31.Add( self.bRemoveFilledCircle, 0, wx.ALL, 0 )
		
		self.bRemoveFilledRectangle = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/fog_remove_filled_rectangle.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bRemoveFilledRectangle.SetBitmapHover( wx.Bitmap( u"artwork/fog_remove_filled_rectangle_selected.png", wx.BITMAP_TYPE_ANY ) )
		self.bRemoveFilledRectangle.SetToolTip( u"Remove fog rectangle" )
		
		bSizer31.Add( self.bRemoveFilledRectangle, 0, wx.ALL, 0 )
		
		bSizer2812 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bEraseFog = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/fog_eraser.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bEraseFog.SetBitmapHover( wx.Bitmap( u"artwork/fog_eraser_selected.png", wx.BITMAP_TYPE_ANY ) )
		self.bEraseFog.SetToolTip( u"Remove fog from the display using the current brush radius" )
		
		bSizer2812.Add( self.bEraseFog, 0, wx.ALL, 0 )
		
		self.stPanelDescription12 = wx.StaticText( self, wx.ID_ANY, u"Brush Radius:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stPanelDescription12.Wrap( 0 )
		bSizer2812.Add( self.stPanelDescription12, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.spRemoveBrushRadius = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 45,-1 ), wx.SP_ARROW_KEYS, 1, 40, 5 )
		self.spRemoveBrushRadius.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.spRemoveBrushRadius.SetToolTip( u"Adjusts the brush radius in feet.  Change scale in Program Options" )
		
		bSizer2812.Add( self.spRemoveBrushRadius, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer31.Add( bSizer2812, 0, wx.EXPAND|wx.RIGHT, 5 )
		
		bSizer2821 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bRemoveLine = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/fog_remove_line.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bRemoveLine.SetBitmapHover( wx.Bitmap( u"artwork/fog_remove_line_selected.png", wx.BITMAP_TYPE_ANY ) )
		self.bRemoveLine.SetToolTip( u"Remove fog in a straight line" )
		
		bSizer2821.Add( self.bRemoveLine, 0, wx.ALL, 0 )
		
		self.bRemoveMultiline = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/fog_remove_line_segments.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bRemoveMultiline.SetBitmapHover( wx.Bitmap( u"artwork/fog_remove_line_segments_selected.png", wx.BITMAP_TYPE_ANY ) )
		self.bRemoveMultiline.SetToolTip( u"Remove fog in a multiline." )
		
		bSizer2821.Add( self.bRemoveMultiline, 0, wx.ALL, 0 )
		
		self.stPanelDescription21 = wx.StaticText( self, wx.ID_ANY, u"Line Width:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stPanelDescription21.Wrap( 0 )
		bSizer2821.Add( self.stPanelDescription21, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.spRemoveLineWidth = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 45,-1 ), wx.SP_ARROW_KEYS, 1, 20, 5 )
		self.spRemoveLineWidth.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.spRemoveLineWidth.SetToolTip( u"Adjusts the line width in feet.  Change scale in Program Options" )
		
		bSizer2821.Add( self.spRemoveLineWidth, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
		
		
		bSizer31.Add( bSizer2821, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer31, 0, wx.EXPAND, 5 )
		
		bSizer160 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer371 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bAddLightSource = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/fog_generic_light.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bAddLightSource.SetBitmapHover( wx.Bitmap( u"artwork/fog_generic_light_selected.png", wx.BITMAP_TYPE_ANY ) )
		self.bAddLightSource.SetToolTip( u"Add a light source using the current options" )
		
		bSizer371.Add( self.bAddLightSource, 0, 0, 5 )
		
		bSizer370 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText164 = wx.StaticText( self, wx.ID_ANY, u"Light Radius:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText164.Wrap( 0 )
		bSizer370.Add( self.m_staticText164, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.spLightRadius = wx.SpinCtrl( self, wx.ID_ANY, u"20", wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 1, 1000, 20 )
		self.spLightRadius.SetToolTip( u"Radius in feet.  Change grid scale in Program Options" )
		
		bSizer370.Add( self.spLightRadius, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer371.Add( bSizer370, 0, wx.EXPAND, 5 )
		
		self.cpkLightSource = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 255, 255, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		self.cpkLightSource.SetToolTip( u"Light Source Color" )
		
		bSizer371.Add( self.cpkLightSource, 0, wx.ALIGN_CENTER_VERTICAL, 7 )
		
		
		bSizer160.Add( bSizer371, 1, wx.EXPAND, 5 )
		
		bSizer376 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText167 = wx.StaticText( self, wx.ID_ANY, u"Map Fog Density", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText167.Wrap( 60 )
		bSizer376.Add( self.m_staticText167, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.slMapFogDensity = wx.Slider( self, wx.ID_ANY, 128, 0, 255, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		self.slMapFogDensity.SetToolTip( u"Change density on map window" )
		
		bSizer376.Add( self.slMapFogDensity, 2, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer160.Add( bSizer376, 1, wx.ALIGN_RIGHT|wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer160, 1, wx.EXPAND, 5 )
		
		bSizer633 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bShowSecondary = wx.Button( self, wx.ID_ANY, u"Show Secondary Viewport", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer633.Add( self.bShowSecondary, 0, 0, 5 )
		
		self.bUpdateFog = wx.Button( self, wx.ID_ANY, u"Update Fog Image", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer633.Add( self.bUpdateFog, 0, 0, 5 )
		
		self.bUpdateFogOnline = wx.Button( self, wx.ID_ANY, u"Update Fog Online", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer633.Add( self.bUpdateFogOnline, 0, 0, 5 )
		
		
		bSizer1.Add( bSizer633, 0, wx.EXPAND, 5 )
		
		
		bSizer25.Add( bSizer1, 0, wx.EXPAND, 0 )
		
		
		self.SetSizer( bSizer25 )
		self.Layout()
		bSizer25.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.bConcealAll.Bind( wx.EVT_BUTTON, self.OnConcealAll )
		self.bDrawFilledCircle.Bind( wx.EVT_BUTTON, self.OnDrawFogCircle )
		self.bDrawFilledRectangle.Bind( wx.EVT_BUTTON, self.OnDrawFogRectangle )
		self.bAddFog.Bind( wx.EVT_BUTTON, self.OnDrawFog )
		self.bDrawLine.Bind( wx.EVT_BUTTON, self.OnDrawFogLine )
		self.bDrawMultiline.Bind( wx.EVT_BUTTON, self.OnDrawFogMultiline )
		self.bRevealAll.Bind( wx.EVT_BUTTON, self.OnRevealAll )
		self.bRemoveFilledCircle.Bind( wx.EVT_BUTTON, self.OnRemoveFogCircle )
		self.bRemoveFilledRectangle.Bind( wx.EVT_BUTTON, self.OnRemoveFogRectangle )
		self.bEraseFog.Bind( wx.EVT_BUTTON, self.OnEraseFog )
		self.bRemoveLine.Bind( wx.EVT_BUTTON, self.OnRemoveFogLine )
		self.bRemoveMultiline.Bind( wx.EVT_BUTTON, self.OnRemoveFogMultiline )
		self.bAddLightSource.Bind( wx.EVT_BUTTON, self.OnAddGenericLightSource )
		self.slMapFogDensity.Bind( wx.EVT_SCROLL_CHANGED, self.ChangeMapFogDensity )
		self.bShowSecondary.Bind( wx.EVT_BUTTON, self.OnShowSecondary )
		self.bUpdateFog.Bind( wx.EVT_BUTTON, self.OnUpdateFog )
		self.bUpdateFogOnline.Bind( wx.EVT_BUTTON, self.OnUpdateFogOnline )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()
	
	def OnConcealAll( self, event ):
		event.Skip()
	
	def OnDrawFogCircle( self, event ):
		event.Skip()
	
	def OnDrawFogRectangle( self, event ):
		event.Skip()
	
	def OnDrawFog( self, event ):
		event.Skip()
	
	def OnDrawFogLine( self, event ):
		event.Skip()
	
	def OnDrawFogMultiline( self, event ):
		event.Skip()
	
	def OnRevealAll( self, event ):
		event.Skip()
	
	def OnRemoveFogCircle( self, event ):
		event.Skip()
	
	def OnRemoveFogRectangle( self, event ):
		event.Skip()
	
	def OnEraseFog( self, event ):
		event.Skip()
	
	def OnRemoveFogLine( self, event ):
		event.Skip()
	
	def OnRemoveFogMultiline( self, event ):
		event.Skip()
	
	def OnAddGenericLightSource( self, event ):
		event.Skip()
	
	def ChangeMapFogDensity( self, event ):
		event.Skip()
	
	def OnShowSecondary( self, event ):
		event.Skip()
	
	def OnUpdateFog( self, event ):
		event.Skip()
	
	def OnUpdateFogOnline( self, event ):
		event.Skip()
	

###########################################################################
## Class ProgramFoundationDialogBase
###########################################################################

class ProgramFoundationDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Program Foundations", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"The following software programs and utiliies make PyMapper possible:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		self.m_staticText30.SetBackgroundColour( wx.Colour( 255, 255, 0 ) )
		
		bSizer8.Add( self.m_staticText30, 0, wx.ALL, 5 )
		
		bSizer91 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap21 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"artwork/python.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer91.Add( self.m_bitmap21, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Python is a remarkably powerful dynamic programming language \nthat is used in a wide variety of application domains. Python is often \ncompared to Tcl, Perl, Ruby, Scheme or Java. ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer91.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.m_hyperlink1 = wx.HyperlinkCtrl( self, wx.ID_ANY, u"Python website", u"http://www.python.org", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		self.m_hyperlink1.SetToolTip( u"www.python.org" )
		
		bSizer91.Add( self.m_hyperlink1, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer8.Add( bSizer91, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer911 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap211 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"artwork/wxpython.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer911.Add( self.m_bitmap211, 0, wx.ALL, 5 )
		
		self.m_staticText111 = wx.StaticText( self, wx.ID_ANY, u"wxPython is a GUI toolkit for the Python programming language. It allows \nPython programmers to create programs with a robust, highly functional \ngraphical user interface, simply and easily. ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )
		bSizer911.Add( self.m_staticText111, 0, wx.ALL, 5 )
		
		self.m_hyperlink2 = wx.HyperlinkCtrl( self, wx.ID_ANY, u"wxPython Website", u"http://www.wxpython.org", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		self.m_hyperlink2.SetToolTip( u"www.wxpython.org" )
		
		bSizer911.Add( self.m_hyperlink2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer8.Add( bSizer911, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap2 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"artwork/wingware.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_bitmap2, 0, wx.ALL, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Wingware's Python IDE is an Integrated Development Environment \ndesigned specifically for the Python programming language. Since 1999, \nWingware has focused on Python.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer9.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_hyperlink3 = wx.HyperlinkCtrl( self, wx.ID_ANY, u"Wingware Website", u"http://www.wingware.com", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		self.m_hyperlink3.SetToolTip( u"www.wingware.com" )
		
		bSizer9.Add( self.m_hyperlink3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer8.Add( bSizer9, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer9111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap2111 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"artwork/wxFormBuilder.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9111.Add( self.m_bitmap2111, 0, wx.ALL, 5 )
		
		self.m_staticText1111 = wx.StaticText( self, wx.ID_ANY, u"wxFormBuilder - a RAD tool for wxWidgets GUI design.  This is \nnow the primary tool being used for new dialogs and user interface elements.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1111.Wrap( -1 )
		bSizer9111.Add( self.m_staticText1111, 0, wx.ALL, 5 )
		
		self.m_hyperlink4 = wx.HyperlinkCtrl( self, wx.ID_ANY, u"wxFB Website", u"http://www.wxformbuilder.org", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		self.m_hyperlink4.SetToolTip( u"www.wxformbuilder.org" )
		
		bSizer9111.Add( self.m_hyperlink4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer8.Add( bSizer9111, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer91111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap21111 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"artwork/py2exe.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer91111.Add( self.m_bitmap21111, 0, wx.ALL, 5 )
		
		self.m_staticText11111 = wx.StaticText( self, wx.ID_ANY, u"py2exe is a Python Distutils extension which converts Python scripts \ninto executable Windows programs, able to run without requiring \na Python installation.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11111.Wrap( -1 )
		bSizer91111.Add( self.m_staticText11111, 0, wx.ALL, 5 )
		
		
		bSizer8.Add( bSizer91111, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer911111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_bitmap211111 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"artwork/gui2exe.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer911111.Add( self.m_bitmap211111, 0, wx.ALL, 5 )
		
		self.m_staticText111111 = wx.StaticText( self, wx.ID_ANY, u"GUI2Exe is a Graphical User Interface frontend to all the \"executable \nbuilders\" available for the Python programming language.  It is used to convert\nthe python scripts into a standalone windows executable.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111111.Wrap( -1 )
		bSizer911111.Add( self.m_staticText111111, 0, wx.ALL, 5 )
		
		
		bSizer8.Add( bSizer911111, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bClose = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bClose.SetDefault() 
		self.bClose.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bClose.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.bClose.SetBackgroundColour( wx.Colour( 0, 64, 0 ) )
		
		bSizer2.Add( self.bClose, 0, wx.ALL, 5 )
		
		
		bSizer8.Add( bSizer2, 0, wx.ALIGN_CENTER, 5 )
		
		
		self.SetSizer( bSizer8 )
		self.Layout()
		bSizer8.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.bClose.Bind( wx.EVT_BUTTON, self.OnClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()
	

###########################################################################
## Class GeomorphSettingsDialogBase
###########################################################################

class GeomorphSettingsDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Geomorph Alignment Settings", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer241 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer242 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer243 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap23 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 20,20 ), 0 )
		bSizer243.Add( self.m_bitmap23, 0, 0, 0 )
		
		self.tLeft1 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,30 ), 0 )
		self.tLeft1.SetValue( True ) 
		bSizer243.Add( self.tLeft1, 0, 0, 0 )
		
		self.tLeft2 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,30 ), 0 )
		self.tLeft2.SetValue( True ) 
		bSizer243.Add( self.tLeft2, 0, 0, 0 )
		
		self.tLeft4 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,30 ), 0 )
		self.tLeft4.SetValue( True ) 
		bSizer243.Add( self.tLeft4, 0, 0, 0 )
		
		self.tLeft8 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,30 ), 0 )
		self.tLeft8.SetValue( True ) 
		bSizer243.Add( self.tLeft8, 0, 0, 0 )
		
		self.tLeft16 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,30 ), 0 )
		self.tLeft16.SetValue( True ) 
		bSizer243.Add( self.tLeft16, 0, 0, 0 )
		
		self.tLeft32 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,30 ), 0 )
		self.tLeft32.SetValue( True ) 
		bSizer243.Add( self.tLeft32, 0, 0, 0 )
		
		self.tLeft64 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,30 ), 0 )
		bSizer243.Add( self.tLeft64, 0, 0, 0 )
		
		self.m_bitmap24 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 20,20 ), 0 )
		bSizer243.Add( self.m_bitmap24, 0, 0, 0 )
		
		
		bSizer242.Add( bSizer243, 9, 0, 0 )
		
		
		bSizer241.Add( bSizer242, 0, 0, 0 )
		
		bSizer244 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer245 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.tTop1 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,20 ), 0 )
		self.tTop1.SetValue( True ) 
		bSizer245.Add( self.tTop1, 0, 0, 0 )
		
		self.tTop2 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,20 ), 0 )
		self.tTop2.SetValue( True ) 
		bSizer245.Add( self.tTop2, 0, 0, 0 )
		
		self.tTop4 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,20 ), 0 )
		self.tTop4.SetValue( True ) 
		bSizer245.Add( self.tTop4, 0, 0, 0 )
		
		self.tTop8 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,20 ), 0 )
		self.tTop8.SetValue( True ) 
		bSizer245.Add( self.tTop8, 0, 0, 0 )
		
		self.tTop16 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,20 ), 0 )
		self.tTop16.SetValue( True ) 
		bSizer245.Add( self.tTop16, 0, 0, 0 )
		
		self.tTop32 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,20 ), 0 )
		self.tTop32.SetValue( True ) 
		bSizer245.Add( self.tTop32, 0, 0, 0 )
		
		
		bSizer244.Add( bSizer245, 0, 0, 0 )
		
		bSizer246 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.pnImagePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 180,210 ), wx.TAB_TRAVERSAL )
		self.pnImagePanel.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		
		bSizer246.Add( self.pnImagePanel, 0, 0, 0 )
		
		
		bSizer244.Add( bSizer246, 7, 0, 0 )
		
		bSizer247 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.tBottom1 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,20 ), 0 )
		self.tBottom1.SetValue( True ) 
		bSizer247.Add( self.tBottom1, 0, 0, 0 )
		
		self.tBottom2 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,20 ), 0 )
		self.tBottom2.SetValue( True ) 
		bSizer247.Add( self.tBottom2, 0, 0, 0 )
		
		self.tBottom4 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,20 ), 0 )
		self.tBottom4.SetValue( True ) 
		bSizer247.Add( self.tBottom4, 0, 0, 0 )
		
		self.tBottom8 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,20 ), 0 )
		self.tBottom8.SetValue( True ) 
		bSizer247.Add( self.tBottom8, 0, 0, 0 )
		
		self.tBottom16 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,20 ), 0 )
		self.tBottom16.SetValue( True ) 
		bSizer247.Add( self.tBottom16, 0, 0, 0 )
		
		self.tBottom32 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,20 ), 0 )
		self.tBottom32.SetValue( True ) 
		bSizer247.Add( self.tBottom32, 0, 0, 0 )
		
		
		bSizer244.Add( bSizer247, 0, 0, 0 )
		
		
		bSizer241.Add( bSizer244, 0, 0, 5 )
		
		bSizer248 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer249 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap25 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 20,20 ), 0 )
		bSizer249.Add( self.m_bitmap25, 0, 0, 0 )
		
		self.tRight1 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,30 ), 0 )
		self.tRight1.SetValue( True ) 
		bSizer249.Add( self.tRight1, 0, 0, 0 )
		
		self.tRight2 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,30 ), 0 )
		self.tRight2.SetValue( True ) 
		bSizer249.Add( self.tRight2, 0, 0, 0 )
		
		self.tRight4 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,30 ), 0 )
		self.tRight4.SetValue( True ) 
		bSizer249.Add( self.tRight4, 0, 0, 0 )
		
		self.tRight8 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,30 ), 0 )
		self.tRight8.SetValue( True ) 
		bSizer249.Add( self.tRight8, 0, 0, 0 )
		
		self.tRight16 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,30 ), 0 )
		self.tRight16.SetValue( True ) 
		bSizer249.Add( self.tRight16, 0, 0, 0 )
		
		self.tRight32 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,30 ), 0 )
		self.tRight32.SetValue( True ) 
		bSizer249.Add( self.tRight32, 0, 0, 0 )
		
		self.tRight64 = wx.ToggleButton( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,30 ), 0 )
		self.tRight64.SetValue( True ) 
		bSizer249.Add( self.tRight64, 0, 0, 0 )
		
		self.m_bitmap26 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 20,20 ), 0 )
		bSizer249.Add( self.m_bitmap26, 0, 0, 0 )
		
		
		bSizer248.Add( bSizer249, 0, 0, 0 )
		
		
		bSizer241.Add( bSizer248, 0, 0, 0 )
		
		bSizer250 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer45 = wx.BoxSizer( wx.VERTICAL )
		
		self.bSelectAll = wx.Button( self, wx.ID_ANY, u"Select All", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer45.Add( self.bSelectAll, 0, wx.ALIGN_TOP|wx.EXPAND, 0 )
		
		self.bSelectNone = wx.Button( self, wx.ID_ANY, u"Select None", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer45.Add( self.bSelectNone, 0, wx.ALL, 0 )
		
		
		bSizer250.Add( bSizer45, 1, wx.EXPAND|wx.TOP, 25 )
		
		bSizer251 = wx.BoxSizer( wx.VERTICAL )
		
		self.ID_OK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_OK.SetDefault() 
		self.ID_OK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_OK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.ID_OK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer251.Add( self.ID_OK, 0, wx.EXPAND, 0 )
		
		self.ID_CANCEL = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_CANCEL.SetDefault() 
		self.ID_CANCEL.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_CANCEL.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ID_CANCEL.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		
		bSizer251.Add( self.ID_CANCEL, 0, wx.EXPAND, 0 )
		
		self.bHelp = wx.Button( self, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bHelp.SetDefault() 
		self.bHelp.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bHelp.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bHelp.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer251.Add( self.bHelp, 0, wx.EXPAND, 0 )
		
		
		bSizer250.Add( bSizer251, 0, wx.EXPAND, 0 )
		
		
		bSizer241.Add( bSizer250, 0, wx.EXPAND|wx.LEFT, 5 )
		
		
		self.SetSizer( bSizer241 )
		self.Layout()
		bSizer241.Fit( self )
		
		# Connect Events
		self.bSelectAll.Bind( wx.EVT_BUTTON, self.OnSelectAllEdges )
		self.bSelectNone.Bind( wx.EVT_BUTTON, self.OnSelectNoEdges )
		self.ID_OK.Bind( wx.EVT_BUTTON, self.OnOK )
		self.ID_CANCEL.Bind( wx.EVT_BUTTON, self.OnCancel )
		self.bHelp.Bind( wx.EVT_BUTTON, self.OnHelp )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSelectAllEdges( self, event ):
		event.Skip()
	
	def OnSelectNoEdges( self, event ):
		event.Skip()
	
	def OnOK( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		event.Skip()
	
	def OnHelp( self, event ):
		event.Skip()
	

###########################################################################
## Class ProgramOptionsDialogBase
###########################################################################

class ProgramOptionsDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Program Options", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gSizer1 = wx.GridSizer( 2, 3, 2, 2 )
		
		szGridOptions = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Grid Options" ), wx.VERTICAL )
		
		GridColor_bitmap1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cbShowGrid = wx.CheckBox( self, wx.ID_ANY, u"Show Grid", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbShowGrid.SetValue(True) 
		self.cbShowGrid.SetToolTip( u"This option can be changed by pressing CTRL+G or on the toolbar." )
		
		GridColor_bitmap1.Add( self.cbShowGrid, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.TOP, 3 )
		
		self.m_staticline35 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		GridColor_bitmap1.Add( self.m_staticline35, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText162 = wx.StaticText( self, wx.ID_ANY, u"Grid Color:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText162.Wrap( -1 )
		GridColor_bitmap1.Add( self.m_staticText162, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.cpkGridColor = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 128, 128, 128 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		GridColor_bitmap1.Add( self.cpkGridColor, 0, 0, 5 )
		
		
		szGridOptions.Add( GridColor_bitmap1, 0, wx.ALL, 2 )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bChangeGridLinestyle = wx.Button( self, wx.ID_ANY, u"Change Grid Line Style", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bChangeGridLinestyle.SetDefault() 
		bSizer15.Add( self.bChangeGridLinestyle, 0, 0, 0 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Width", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( 0 )
		bSizer15.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 10 )
		
		self.spGridLineWidth = wx.SpinCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 43,-1 ), wx.SP_ARROW_KEYS, 1, 20, 1 )
		bSizer15.Add( self.spGridLineWidth, 0, wx.ALL, 0 )
		
		
		bSizer14.Add( bSizer15, 0, wx.EXPAND, 0 )
		
		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.GridLineStyleBitmap = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"artwork/draw_line_style.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 160, 30 ), 0 )
		bSizer16.Add( self.GridLineStyleBitmap, 0, 0, 0 )
		
		
		bSizer14.Add( bSizer16, 0, 0, 0 )
		
		
		szGridOptions.Add( bSizer14, 0, wx.ALL, 2 )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.ShowGridCoordinates = wx.CheckBox( self, wx.ID_ANY, u"Show Grid Coordinates on Map Window", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ShowGridCoordinates.SetValue(True) 
		bSizer17.Add( self.ShowGridCoordinates, 0, 0, 0 )
		
		self.cbDrawGridOnTop = wx.CheckBox( self, wx.ID_ANY, u"Draw grid on top of tiles.", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.cbDrawGridOnTop, 0, wx.TOP, 5 )
		
		self.cbSnapToGrid = wx.CheckBox( self, wx.ID_ANY, u"Snap tiles to grid", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbSnapToGrid.SetValue(True) 
		bSizer17.Add( self.cbSnapToGrid, 0, wx.TOP, 5 )
		
		bSizer127 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cbDrawIntermediateLines = wx.CheckBox( self, wx.ID_ANY, u"Draw Intermediate Guide Lines", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer127.Add( self.cbDrawIntermediateLines, 0, wx.TOP, 5 )
		
		self.cpkIntermediateGuideColor = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 255, 0, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		self.cpkIntermediateGuideColor.SetToolTip( u"Color for intermediate lines" )
		
		bSizer127.Add( self.cpkIntermediateGuideColor, 0, wx.BOTTOM|wx.LEFT, 5 )
		
		
		bSizer17.Add( bSizer127, 1, wx.EXPAND, 5 )
		
		bSizer128 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText50 = wx.StaticText( self, wx.ID_ANY, u"Interval between guides:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )
		bSizer128.Add( self.m_staticText50, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spGuideInterval = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 1, 999, 5 )
		self.spGuideInterval.SetToolTip( u"How many minor lines between guides?" )
		
		bSizer128.Add( self.spGuideInterval, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer17.Add( bSizer128, 1, wx.EXPAND|wx.LEFT, 20 )
		
		bSizer377 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText167 = wx.StaticText( self, wx.ID_ANY, u"Grid Scale (feet per square):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText167.Wrap( -1 )
		bSizer377.Add( self.m_staticText167, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.spGridScale = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 1, 1000, 10 )
		self.spGridScale.SetToolTip( u"Used by the fog-of-war and lightsources" )
		
		bSizer377.Add( self.spGridScale, 0, wx.ALL, 5 )
		
		
		bSizer17.Add( bSizer377, 1, wx.EXPAND, 5 )
		
		
		szGridOptions.Add( bSizer17, 0, wx.TOP, 5 )
		
		
		gSizer1.Add( szGridOptions, 0, wx.ALL|wx.EXPAND, 4 )
		
		szProgramOptions = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Program Options" ), wx.VERTICAL )
		
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cbAutoSave = wx.CheckBox( self, wx.ID_ANY, u"Use automatic backup?", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.cbAutoSave, 0, wx.ALL, 5 )
		
		
		szProgramOptions.Add( bSizer18, 0, wx.TOP|wx.BOTTOM, 3 )
		
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stAutoSave2 = wx.StaticText( self, wx.ID_ANY, u"Minutes between saves:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stAutoSave2.Wrap( -1 )
		bSizer19.Add( self.stAutoSave2, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.AutoSaveTimer = wx.SpinCtrl( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size( 50, -1 ), wx.SP_ARROW_KEYS, 1, 60, 5 )
		bSizer19.Add( self.AutoSaveTimer, 0, 0, 0 )
		
		
		szProgramOptions.Add( bSizer19, 0, wx.TOP|wx.BOTTOM, 3 )
		
		self.stAutoSaveText1 = wx.StaticText( self, wx.ID_ANY, u"Save path:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stAutoSaveText1.Wrap( -1 )
		szProgramOptions.Add( self.stAutoSaveText1, 0, 0, 0 )
		
		self.stAutoSavePath = wx.StaticText( self, wx.ID_ANY, u"pathfilename.bak", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stAutoSavePath.Wrap( 0 )
		szProgramOptions.Add( self.stAutoSavePath, 0, wx.TOP|wx.BOTTOM, 3 )
		
		self.bAutoSavePath = wx.Button( self, wx.ID_ANY, u"Change Path...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bAutoSavePath.SetDefault() 
		szProgramOptions.Add( self.bAutoSavePath, 0, 0, 0 )
		
		self.cbSaveIniFile = wx.CheckBox( self, wx.ID_ANY, u"Save .ini file on close?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbSaveIniFile.SetValue(True) 
		szProgramOptions.Add( self.cbSaveIniFile, 0, wx.TOP, 15 )
		
		self.cbOpenToLastFolder = wx.CheckBox( self, wx.ID_ANY, u"Remember last folder when opening files?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbOpenToLastFolder.SetValue(True) 
		self.cbOpenToLastFolder.SetToolTip( u"When checked, this option will remember the folder where you opened a file.  Otherwise, the maps folder is the default." )
		
		szProgramOptions.Add( self.cbOpenToLastFolder, 0, wx.BOTTOM|wx.TOP, 5 )
		
		
		gSizer1.Add( szProgramOptions, 0, wx.ALL|wx.EXPAND, 4 )
		
		szBackgroundOptions = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Background Options" ), wx.VERTICAL )
		
		stBackground11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cbShowBackground = wx.CheckBox( self, wx.ID_ANY, u"Display Background", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbShowBackground.SetValue(True) 
		stBackground11.Add( self.cbShowBackground, 0, wx.ALL, 5 )
		
		
		szBackgroundOptions.Add( stBackground11, 0, wx.TOP|wx.BOTTOM, 2 )
		
		GridColor_bitmap = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText163 = wx.StaticText( self, wx.ID_ANY, u"Background Color:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText163.Wrap( -1 )
		GridColor_bitmap.Add( self.m_staticText163, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
		
		self.cpkBackgroundColor = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 255, 255, 255 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		GridColor_bitmap.Add( self.cpkBackgroundColor, 0, 0, 5 )
		
		
		szBackgroundOptions.Add( GridColor_bitmap, 0, wx.TOP|wx.BOTTOM, 3 )
		
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.BackgroundOpacityValue = wx.Slider( self, wx.ID_ANY, 100, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_LABELS )
		bSizer22.Add( self.BackgroundOpacityValue, 0, wx.ALIGN_CENTRE_VERTICAL, 0 )
		
		self.BackgroundOpacitySpin = wx.SpinButton( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 25,25 ), wx.SP_ARROW_KEYS )
		bSizer22.Add( self.BackgroundOpacitySpin, 0, wx.ALIGN_BOTTOM, 0 )
		
		self.pnBackgroundOpacity = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 25,25 ), wx.TAB_TRAVERSAL )
		self.pnBackgroundOpacity.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.pnBackgroundOpacity.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer22.Add( self.pnBackgroundOpacity, 0, wx.ALIGN_BOTTOM|wx.ALL, 0 )
		
		self.stBackground3 = wx.StaticText( self, wx.ID_ANY, u"Background Opacity", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stBackground3.Wrap( 1 )
		bSizer22.Add( self.stBackground3, 0, wx.LEFT|wx.ALIGN_BOTTOM, 4 )
		
		
		szBackgroundOptions.Add( bSizer22, 0, wx.TOP, 10 )
		
		bSizer371 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer373 = wx.BoxSizer( wx.VERTICAL )
		
		self.stBackground2 = wx.StaticText( self, wx.ID_ANY, u"Current Background:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stBackground2.Wrap( -1 )
		bSizer373.Add( self.stBackground2, 0, wx.TOP, 5 )
		
		self.stBackgroundPath = wx.StaticText( self, wx.ID_ANY, u"     None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stBackgroundPath.Wrap( -1 )
		bSizer373.Add( self.stBackgroundPath, 0, wx.TOP, 3 )
		
		
		bSizer371.Add( bSizer373, 1, wx.EXPAND, 5 )
		
		
		szBackgroundOptions.Add( bSizer371, 0, wx.EXPAND, 5 )
		
		bSizer372 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText164 = wx.StaticText( self, wx.ID_ANY, u"Map Fog Color:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText164.Wrap( -1 )
		bSizer372.Add( self.m_staticText164, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.cpkMapFogColor = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 107, 107, 107 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		bSizer372.Add( self.cpkMapFogColor, 0, 0, 5 )
		
		
		szBackgroundOptions.Add( bSizer372, 0, wx.EXPAND|wx.TOP, 10 )
		
		bSizer375 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText168 = wx.StaticText( self, wx.ID_ANY, u"Outline tiles color:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText168.Wrap( -1 )
		bSizer375.Add( self.m_staticText168, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.cpkOutlineColor = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 255, 128, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		self.cpkOutlineColor.SetToolTip( u"When active, this color will outline tiles on the map window, and on printed maps." )
		
		bSizer375.Add( self.cpkOutlineColor, 0, wx.ALL, 5 )
		
		
		szBackgroundOptions.Add( bSizer375, 0, wx.TOP, 5 )
		
		
		gSizer1.Add( szBackgroundOptions, 0, wx.ALL|wx.EXPAND, 4 )
		
		szPanelDisplayOptions = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Map and Tile Panel Display Options" ), wx.VERTICAL )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.TileOpacityValue = wx.Slider( self, wx.ID_ANY, 100, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_LABELS )
		bSizer24.Add( self.TileOpacityValue, 0, wx.ALIGN_CENTRE_VERTICAL, 0 )
		
		self.TileOpacitySpin = wx.SpinButton( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 25,25 ), wx.SP_ARROW_KEYS )
		bSizer24.Add( self.TileOpacitySpin, 0, wx.ALIGN_BOTTOM, 0 )
		
		self.pnTileOpacity = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 25,25 ), wx.TAB_TRAVERSAL )
		self.pnTileOpacity.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.pnTileOpacity.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer24.Add( self.pnTileOpacity, 0, wx.ALIGN_BOTTOM|wx.ALL, 0 )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Tile Opacity", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( 1 )
		bSizer24.Add( self.m_staticText16, 0, wx.LEFT|wx.ALIGN_BOTTOM, 4 )
		
		
		sbSizer5.Add( bSizer24, 0, wx.TOP|wx.BOTTOM, 3 )
		
		bSizer25 = wx.BoxSizer( wx.VERTICAL )
		
		self.rbDualDisplayTileWindow = wx.RadioButton( self, wx.ID_ANY, u"Display both tile sides in tile window", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.rbDualDisplayTileWindow.SetValue( True ) 
		self.rbDualDisplayTileWindow.SetToolTip( u"Both sides of a tile are displayed in the tile window.  Either image can drag onto the map window." )
		
		bSizer25.Add( self.rbDualDisplayTileWindow, 0, wx.TOP|wx.BOTTOM, 4 )
		
		self.rbUseHoverOption = wx.RadioButton( self, wx.ID_ANY, u"Display reverse side on mouse hover", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rbUseHoverOption.SetValue( True ) 
		self.rbUseHoverOption.SetToolTip( u"Displays the reverse side of the tile when the mouse is held over for a short time." )
		
		bSizer25.Add( self.rbUseHoverOption, 0, wx.TOP|wx.BOTTOM, 2 )
		
		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stHoverText = wx.StaticText( self, wx.ID_ANY, u"Hover time interval (ms):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stHoverText.Wrap( -1 )
		bSizer26.Add( self.stHoverText, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.HoverTimeInterval = wx.SpinCtrl( self, wx.ID_ANY, u"500", wx.DefaultPosition, wx.Size( 65, -1 ), wx.SP_ARROW_KEYS, 0, 10000, 500 )
		self.HoverTimeInterval.SetToolTip( u"Changes the delay before the reverse side image is displayed.  (1000 ms = 1 second)" )
		
		bSizer26.Add( self.HoverTimeInterval, 0, 0, 0 )
		
		
		bSizer25.Add( bSizer26, 0, wx.LEFT, 20 )
		
		self.cbOutlineOnHover = wx.CheckBox( self, wx.ID_ANY, u"Outline Objects on Mouse Hover", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbOutlineOnHover.SetValue(True) 
		bSizer25.Add( self.cbOutlineOnHover, 0, wx.TOP, 5 )
		
		self.cbReverseMouseWheel = wx.CheckBox( self, wx.ID_ANY, u"Reverse mouse wheel for zoom.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbReverseMouseWheel.SetToolTip( u"Check to reverse the mouse wheel for zoom in and out." )
		
		bSizer25.Add( self.cbReverseMouseWheel, 0, wx.TOP, 5 )
		
		self.cbResetTileStats = wx.CheckBox( self, wx.ID_ANY, u"Reset tile statistics for each map page.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbResetTileStats.SetValue(True) 
		bSizer25.Add( self.cbResetTileStats, 0, wx.TOP, 5 )
		
		
		sbSizer5.Add( bSizer25, 0, wx.TOP|wx.BOTTOM, 5 )
		
		
		szPanelDisplayOptions.Add( sbSizer5, 0, wx.EXPAND, 0 )
		
		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ID_OK = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_OK.SetDefault() 
		self.ID_OK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_OK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.ID_OK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer27.Add( self.ID_OK, 0, 0, 0 )
		
		self.ID_CANCEL = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_CANCEL.SetDefault() 
		self.ID_CANCEL.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_CANCEL.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ID_CANCEL.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		
		bSizer27.Add( self.ID_CANCEL, 0, wx.LEFT|wx.RIGHT, 3 )
		
		self.bHelp = wx.Button( self, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bHelp.SetDefault() 
		self.bHelp.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bHelp.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bHelp.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer27.Add( self.bHelp, 0, 0, 0 )
		
		
		szPanelDisplayOptions.Add( bSizer27, 1, wx.ALIGN_CENTER_VERTICAL|wx.SHAPED, 5 )
		
		
		gSizer1.Add( szPanelDisplayOptions, 1, wx.EXPAND, 4 )
		
		sbSizer90 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Game System Resources" ), wx.VERTICAL )
		
		self.cbReadSRDFiles = wx.CheckBox( self, wx.ID_ANY, u"Read d20 SRD files on startup?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbReadSRDFiles.SetValue(True) 
		self.cbReadSRDFiles.SetToolTip( u"Read the d20 System Reference Document files when starting PyMapper?" )
		
		sbSizer90.Add( self.cbReadSRDFiles, 0, wx.TOP, 5 )
		
		self.cbRead5EditionFiles = wx.CheckBox( self, wx.ID_ANY, u"Read D&&D 5th Edition files on startup?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbRead5EditionFiles.SetValue(True) 
		sbSizer90.Add( self.cbRead5EditionFiles, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )
		
		
		gSizer1.Add( sbSizer90, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		sbSizer91 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Map Icons" ), wx.VERTICAL )
		
		self.cbHighlightIcons = wx.CheckBox( self, wx.ID_ANY, u"Highlight icons on map window?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbHighlightIcons.SetValue(True) 
		self.cbHighlightIcons.SetToolTip( u"Draws a yellow circle behind icons on the map window to improve visibility." )
		
		sbSizer91.Add( self.cbHighlightIcons, 0, wx.TOP, 10 )
		
		self.cbDisplayIconInformation = wx.CheckBox( self, wx.ID_ANY, u"Display Icon Information", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbDisplayIconInformation.SetValue(True) 
		sbSizer91.Add( self.cbDisplayIconInformation, 0, wx.TOP, 5 )
		
		self.cbSnapIconsToGrid = wx.CheckBox( self, wx.ID_ANY, u"Snap icons to grid?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbSnapIconsToGrid.SetValue(True) 
		sbSizer91.Add( self.cbSnapIconsToGrid, 0, wx.TOP, 5 )
		
		
		gSizer1.Add( sbSizer91, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer1 )
		self.Layout()
		gSizer1.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_PAINT, self.OnPaint )
		self.cbShowGrid.Bind( wx.EVT_CHECKBOX, self.ShowGridCheckbox )
		self.bChangeGridLinestyle.Bind( wx.EVT_BUTTON, self.ChangeGridLineStyle )
		self.spGridLineWidth.Bind( wx.EVT_SPINCTRL, self.ChangeGridLineWidth )
		self.cbAutoSave.Bind( wx.EVT_CHECKBOX, self.AutoSave )
		self.bAutoSavePath.Bind( wx.EVT_BUTTON, self.ChangeAutoSavePath )
		self.cbShowBackground.Bind( wx.EVT_CHECKBOX, self.ChangeBackgroundDisplay )
		self.BackgroundOpacityValue.Bind( wx.EVT_SCROLL, self.BackgroundOpacitySlider )
		self.BackgroundOpacityValue.Bind( wx.EVT_SCROLL_CHANGED, self.BackgroundOpacitySlider )
		self.BackgroundOpacitySpin.Bind( wx.EVT_SPIN, self.BackgroundOpacitySpinValue )
		self.TileOpacityValue.Bind( wx.EVT_SCROLL, self.TileOpacitySlider )
		self.TileOpacityValue.Bind( wx.EVT_SCROLL_CHANGED, self.TileOpacitySlider )
		self.TileOpacitySpin.Bind( wx.EVT_SPIN, self.TileOpacitySpinValue )
		self.rbUseHoverOption.Bind( wx.EVT_RADIOBUTTON, self.HoverOption )
		self.ID_OK.Bind( wx.EVT_BUTTON, self.OKButton )
		self.ID_CANCEL.Bind( wx.EVT_BUTTON, self.CancelButton )
		self.bHelp.Bind( wx.EVT_BUTTON, self.OnHelp )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnPaint( self, event ):
		event.Skip()
	
	def ShowGridCheckbox( self, event ):
		event.Skip()
	
	def ChangeGridLineStyle( self, event ):
		event.Skip()
	
	def ChangeGridLineWidth( self, event ):
		event.Skip()
	
	def AutoSave( self, event ):
		event.Skip()
	
	def ChangeAutoSavePath( self, event ):
		event.Skip()
	
	def ChangeBackgroundDisplay( self, event ):
		event.Skip()
	
	def BackgroundOpacitySlider( self, event ):
		event.Skip()
	
	
	def BackgroundOpacitySpinValue( self, event ):
		event.Skip()
	
	def TileOpacitySlider( self, event ):
		event.Skip()
	
	
	def TileOpacitySpinValue( self, event ):
		event.Skip()
	
	def HoverOption( self, event ):
		event.Skip()
	
	def OKButton( self, event ):
		event.Skip()
	
	def CancelButton( self, event ):
		event.Skip()
	
	def OnHelp( self, event ):
		event.Skip()
	

###########################################################################
## Class BackgroundRegistrationDialogBase
###########################################################################

class BackgroundRegistrationDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Background Images", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer220 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer221 = wx.BoxSizer( wx.VERTICAL )
		
		self.pnImageDisplay = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,300 ), wx.TAB_TRAVERSAL )
		self.pnImageDisplay.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer221.Add( self.pnImageDisplay, 0, wx.ALL|wx.ALIGN_CENTRE_VERTICAL|wx.ALIGN_CENTRE_HORIZONTAL, 3 )
		
		bSizer222 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bbZoomIn = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/ZoomIn.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bbZoomIn.SetDefault() 
		self.bbZoomIn.SetToolTip( u"Zoom In" )
		
		bSizer222.Add( self.bbZoomIn, 0, wx.RIGHT, 5 )
		
		self.bbZoomOut = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/ZoomOut.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bbZoomOut.SetDefault() 
		self.bbZoomOut.SetToolTip( u"Zoom Out" )
		
		bSizer222.Add( self.bbZoomOut, 0, wx.LEFT, 5 )
		
		
		bSizer221.Add( bSizer222, 0, wx.ALIGN_CENTER_HORIZONTAL, 0 )
		
		bSizer223 = wx.BoxSizer( wx.VERTICAL )
		
		self.rbTileBackground = wx.RadioButton( self, wx.ID_ANY, u"Tile Background", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.rbTileBackground.SetValue( True ) 
		bSizer223.Add( self.rbTileBackground, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 3 )
		
		self.rbCenterBackground = wx.RadioButton( self, wx.ID_ANY, u"Center Background", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rbCenterBackground.SetValue( True ) 
		bSizer223.Add( self.rbCenterBackground, 0, wx.LEFT, 3 )
		
		self.rbRegisterBackground = wx.RadioButton( self, wx.ID_ANY, u"Align to grid (register image)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rbRegisterBackground.SetValue( True ) 
		bSizer223.Add( self.rbRegisterBackground, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 3 )
		
		
		bSizer221.Add( bSizer223, 0, 0, 0 )
		
		bSizer224 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bImportImage = wx.Button( self, wx.ID_ANY, u"Import Image...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bImportImage.SetDefault() 
		bSizer224.Add( self.bImportImage, 0, wx.LEFT|wx.RIGHT, 5 )
		
		self.bDeleteImage = wx.Button( self, wx.ID_ANY, u"Delete Image", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bDeleteImage.SetDefault() 
		bSizer224.Add( self.bDeleteImage, 0, wx.LEFT|wx.RIGHT, 5 )
		
		
		bSizer221.Add( bSizer224, 0, wx.TOP|wx.BOTTOM, 5 )
		
		bSizer67 = wx.BoxSizer( wx.VERTICAL )
		
		self.rbShowOnCurrentPage = wx.RadioButton( self, wx.ID_ANY, u"Show on Current Page", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.rbShowOnCurrentPage.SetValue( True ) 
		bSizer67.Add( self.rbShowOnCurrentPage, 0, wx.ALL, 3 )
		
		self.rbShowOnAllPages = wx.RadioButton( self, wx.ID_ANY, u"Show On All Pages", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer67.Add( self.rbShowOnAllPages, 0, wx.ALL, 3 )
		
		
		bSizer221.Add( bSizer67, 1, wx.EXPAND, 5 )
		
		
		bSizer220.Add( bSizer221, 0, 0, 0 )
		
		bSizer225 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ID_OK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_OK.SetDefault() 
		self.ID_OK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_OK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.ID_OK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer225.Add( self.ID_OK, 0, wx.RIGHT, 2 )
		
		self.ID_CANCEL = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_CANCEL.SetDefault() 
		self.ID_CANCEL.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_CANCEL.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ID_CANCEL.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		
		bSizer225.Add( self.ID_CANCEL, 0, wx.LEFT|wx.RIGHT, 2 )
		
		self.bHelp = wx.Button( self, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bHelp.SetDefault() 
		self.bHelp.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bHelp.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bHelp.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer225.Add( self.bHelp, 0, wx.LEFT, 2 )
		
		
		bSizer220.Add( bSizer225, 0, wx.TOP, 5 )
		
		
		self.SetSizer( bSizer220 )
		self.Layout()
		bSizer220.Fit( self )
		
		# Connect Events
		self.pnImageDisplay.Bind( wx.EVT_LEFT_DOWN, self.RegisterGridMouseClick )
		self.pnImageDisplay.Bind( wx.EVT_PAINT, self.OnPaint )
		self.bbZoomIn.Bind( wx.EVT_BUTTON, self.ZoomIn )
		self.bbZoomOut.Bind( wx.EVT_BUTTON, self.ZoomOut )
		self.rbTileBackground.Bind( wx.EVT_RADIOBUTTON, self.TileBackground )
		self.rbCenterBackground.Bind( wx.EVT_RADIOBUTTON, self.CenterBackground )
		self.rbRegisterBackground.Bind( wx.EVT_RADIOBUTTON, self.RegisterBackground )
		self.bImportImage.Bind( wx.EVT_BUTTON, self.ImportImage )
		self.bDeleteImage.Bind( wx.EVT_BUTTON, self.DeleteImage )
		self.ID_OK.Bind( wx.EVT_BUTTON, self.OnOK )
		self.ID_CANCEL.Bind( wx.EVT_BUTTON, self.OnCANCEL )
		self.bHelp.Bind( wx.EVT_BUTTON, self.OnHelp )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def RegisterGridMouseClick( self, event ):
		event.Skip()
	
	def OnPaint( self, event ):
		event.Skip()
	
	def ZoomIn( self, event ):
		event.Skip()
	
	def ZoomOut( self, event ):
		event.Skip()
	
	def TileBackground( self, event ):
		event.Skip()
	
	def CenterBackground( self, event ):
		event.Skip()
	
	def RegisterBackground( self, event ):
		event.Skip()
	
	def ImportImage( self, event ):
		event.Skip()
	
	def DeleteImage( self, event ):
		event.Skip()
	
	def OnOK( self, event ):
		event.Skip()
	
	def OnCANCEL( self, event ):
		event.Skip()
	
	def OnHelp( self, event ):
		event.Skip()
	

###########################################################################
## Class PrintSetupDialogBase
###########################################################################

class PrintSetupDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Setup Map Printing", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer61 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer62 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer63 = wx.BoxSizer( wx.VERTICAL )
		
		self.pnPreviewPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 255,330 ), wx.SUNKEN_BORDER )
		self.pnPreviewPanel.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer63.Add( self.pnPreviewPanel, 0, 0, 0 )
		
		
		bSizer62.Add( bSizer63, 0, 0, 0 )
		
		bSizer64 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer65 = wx.BoxSizer( wx.VERTICAL )
		
		self.rbPrint1Scale = wx.RadioButton( self, wx.ID_ANY, u"Print in 1:1 scale", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.rbPrint1Scale.SetValue( True ) 
		bSizer65.Add( self.rbPrint1Scale, 0, wx.ALL, 3 )
		
		self.rbCustomScale = wx.RadioButton( self, wx.ID_ANY, u"Custom Scale", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer65.Add( self.rbCustomScale, 0, wx.ALL, 3 )
		
		bSizer66 = wx.BoxSizer( wx.VERTICAL )
		
		self.rbFit1Page = wx.RadioButton( self, wx.ID_ANY, u"Fit on 1 page", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.rbFit1Page.SetValue( True ) 
		bSizer66.Add( self.rbFit1Page, 0, wx.ALL, 5 )
		
		self.rbFitCustomPage = wx.RadioButton( self, wx.ID_ANY, u"Custom Size", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer66.Add( self.rbFitCustomPage, 0, wx.ALL, 5 )
		
		
		bSizer65.Add( bSizer66, 0, wx.LEFT, 15 )
		
		bSizer67 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer68 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.spPagesHigh = wx.SpinCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 1, 99, 1 )
		bSizer68.Add( self.spPagesHigh, 0, wx.ALIGN_CENTER_VERTICAL|wx.BOTTOM|wx.TOP, 5 )
		
		self.stPagesHigh = wx.StaticText( self, wx.ID_ANY, u"Pages High", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stPagesHigh.Wrap( 0 )
		bSizer68.Add( self.stPagesHigh, 0, wx.ALL|wx.ALIGN_CENTRE_VERTICAL, 3 )
		
		
		bSizer67.Add( bSizer68, 0, 0, 0 )
		
		bSizer69 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.spPagesWide = wx.SpinCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 1, 99, 1 )
		bSizer69.Add( self.spPagesWide, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.stPagesWide = wx.StaticText( self, wx.ID_ANY, u"Pages Wide", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stPagesWide.Wrap( 0 )
		bSizer69.Add( self.stPagesWide, 0, wx.ALL|wx.ALIGN_CENTRE_VERTICAL, 3 )
		
		
		bSizer67.Add( bSizer69, 0, 0, 0 )
		
		
		bSizer65.Add( bSizer67, 0, wx.LEFT, 30 )
		
		
		bSizer64.Add( bSizer65, 0, wx.ALL, 5 )
		
		bChangePrinter1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer78 = wx.BoxSizer( wx.VERTICAL )
		
		self.cbOutlineTiles = wx.CheckBox( self, wx.ID_ANY, u"Outline Tiles?", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer78.Add( self.cbOutlineTiles, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bChangePrinter1.Add( bSizer78, 0, wx.EXPAND, 5 )
		
		bSizer77 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Outline Color:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		bSizer77.Add( self.m_staticText24, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.cxOutlineColor = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		bSizer77.Add( self.cxOutlineColor, 0, wx.LEFT, 5 )
		
		
		bChangePrinter1.Add( bSizer77, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.bPageSetup = wx.Button( self, wx.ID_ANY, u"Page Setup...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bPageSetup.SetDefault() 
		self.bPageSetup.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bPageSetup.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bPageSetup.SetBackgroundColour( wx.Colour( 139, 1, 214 ) )
		self.bPageSetup.SetToolTip( u"Press to see the print job preview" )
		
		bChangePrinter1.Add( self.bPageSetup, 0, wx.TOP, 5 )
		
		self.bChangePrinter = wx.Button( self, wx.ID_ANY, u"Change Printer...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bChangePrinter.SetDefault() 
		self.bChangePrinter.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bChangePrinter.SetForegroundColour( wx.Colour( 255, 128, 0 ) )
		self.bChangePrinter.SetBackgroundColour( wx.Colour( 0, 0, 128 ) )
		
		bChangePrinter1.Add( self.bChangePrinter, 0, wx.TOP, 3 )
		
		self.ID_OK = wx.Button( self, wx.ID_ANY, u"Print Map", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_OK.SetDefault() 
		self.ID_OK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_OK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.ID_OK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bChangePrinter1.Add( self.ID_OK, 0, wx.TOP|wx.ALIGN_BOTTOM, 20 )
		
		self.ID_CANCEL = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_CANCEL.SetDefault() 
		self.ID_CANCEL.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_CANCEL.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ID_CANCEL.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		
		bChangePrinter1.Add( self.ID_CANCEL, 0, wx.TOP|wx.BOTTOM, 3 )
		
		
		bSizer64.Add( bChangePrinter1, 0, wx.TOP|wx.ALIGN_CENTRE|wx.ALIGN_CENTRE_VERTICAL, 35 )
		
		
		bSizer62.Add( bSizer64, 0, wx.EXPAND|wx.EXPAND, 0 )
		
		
		bSizer61.Add( bSizer62, 0, wx.EXPAND, 0 )
		
		
		self.SetSizer( bSizer61 )
		self.Layout()
		bSizer61.Fit( self )
		
		# Connect Events
		self.rbPrint1Scale.Bind( wx.EVT_RADIOBUTTON, self.OnPrint1Scale )
		self.rbCustomScale.Bind( wx.EVT_RADIOBUTTON, self.OnCustomScale )
		self.rbFit1Page.Bind( wx.EVT_RADIOBUTTON, self.OnFit1Page )
		self.rbFitCustomPage.Bind( wx.EVT_RADIOBUTTON, self.OnFitCustomPage )
		self.spPagesHigh.Bind( wx.EVT_SPINCTRL, self.spNumPagesHigh )
		self.spPagesWide.Bind( wx.EVT_SPINCTRL, self.spNumPagesWide )
		self.bPageSetup.Bind( wx.EVT_BUTTON, self.OnPageSetup )
		self.bChangePrinter.Bind( wx.EVT_BUTTON, self.OnChangePrinter )
		self.ID_OK.Bind( wx.EVT_BUTTON, self.OnOK )
		self.ID_CANCEL.Bind( wx.EVT_BUTTON, self.OnCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnPrint1Scale( self, event ):
		event.Skip()
	
	def OnCustomScale( self, event ):
		event.Skip()
	
	def OnFit1Page( self, event ):
		event.Skip()
	
	def OnFitCustomPage( self, event ):
		event.Skip()
	
	def spNumPagesHigh( self, event ):
		event.Skip()
	
	def spNumPagesWide( self, event ):
		event.Skip()
	
	def OnPageSetup( self, event ):
		event.Skip()
	
	def OnChangePrinter( self, event ):
		event.Skip()
	
	def OnOK( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class ImageTransformationBase
###########################################################################

class ImageTransformationBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Image Transformation", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer78 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer92 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.pnDisplayPanel = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,500 ), wx.HSCROLL|wx.SUNKEN_BORDER|wx.VSCROLL )
		self.pnDisplayPanel.SetScrollRate( 5, 5 )
		self.pnDisplayPanel.SetBackgroundColour( wx.Colour( 83, 83, 189 ) )
		
		bSizer92.Add( self.pnDisplayPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer78.Add( bSizer92, 1, wx.EXPAND, 5 )
		
		bSizer93 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer795 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText245 = wx.StaticText( self, wx.ID_ANY, u"x scale", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText245.Wrap( -1 )
		bSizer795.Add( self.m_staticText245, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.ValueA = wx.TextCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.ValueA.SetMaxLength( 0 ) 
		bSizer795.Add( self.ValueA, 0, wx.ALL, 5 )
		
		
		bSizer93.Add( bSizer795, 0, wx.EXPAND, 5 )
		
		bSizer794 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText244 = wx.StaticText( self, wx.ID_ANY, u"tangent of horiz skew", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText244.Wrap( -1 )
		bSizer794.Add( self.m_staticText244, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.ValueB = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.ValueB.SetMaxLength( 0 ) 
		bSizer794.Add( self.ValueB, 0, wx.ALL, 5 )
		
		
		bSizer93.Add( bSizer794, 0, wx.EXPAND, 5 )
		
		bSizer792 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText242 = wx.StaticText( self, wx.ID_ANY, u"x offset", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText242.Wrap( -1 )
		bSizer792.Add( self.m_staticText242, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.ValueC = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.ValueC.SetMaxLength( 0 ) 
		bSizer792.Add( self.ValueC, 0, wx.ALL, 5 )
		
		
		bSizer93.Add( bSizer792, 0, wx.EXPAND, 5 )
		
		bSizer793 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText243 = wx.StaticText( self, wx.ID_ANY, u"tangent of vertical skew", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText243.Wrap( -1 )
		bSizer793.Add( self.m_staticText243, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.ValueD = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.ValueD.SetMaxLength( 0 ) 
		bSizer793.Add( self.ValueD, 0, wx.ALL, 5 )
		
		
		bSizer93.Add( bSizer793, 0, wx.EXPAND, 5 )
		
		bSizer791 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText241 = wx.StaticText( self, wx.ID_ANY, u"width", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText241.Wrap( -1 )
		bSizer791.Add( self.m_staticText241, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.ValueE = wx.TextCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.ValueE.SetMaxLength( 0 ) 
		bSizer791.Add( self.ValueE, 0, wx.ALL, 5 )
		
		
		bSizer93.Add( bSizer791, 0, wx.EXPAND, 5 )
		
		bSizer79 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"y offset", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		bSizer79.Add( self.m_staticText24, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.ValueF = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.ValueF.SetMaxLength( 0 ) 
		bSizer79.Add( self.ValueF, 0, wx.ALL, 5 )
		
		
		bSizer93.Add( bSizer79, 0, wx.EXPAND, 5 )
		
		bSizer94 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button33 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer94.Add( self.m_button33, 0, wx.ALL, 5 )
		
		self.m_button34 = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer94.Add( self.m_button34, 0, wx.ALL, 5 )
		
		self.bTransformAffine = wx.Button( self, wx.ID_ANY, u"Transform Affine", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer94.Add( self.bTransformAffine, 0, wx.ALL, 5 )
		
		self.bTransformPerspective = wx.Button( self, wx.ID_ANY, u"Transform Perspective", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer94.Add( self.bTransformPerspective, 0, wx.ALL, 5 )
		
		bSizer121 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText46 = wx.StaticText( self, wx.ID_ANY, u"theta", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )
		bSizer121.Add( self.m_staticText46, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.txTheta = wx.TextCtrl( self, wx.ID_ANY, u"0.4", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.txTheta.SetMaxLength( 0 ) 
		bSizer121.Add( self.txTheta, 0, wx.ALL, 5 )
		
		
		bSizer94.Add( bSizer121, 1, wx.EXPAND, 5 )
		
		self.bTransformIsometric = wx.Button( self, wx.ID_ANY, u"Isometric Transform", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer94.Add( self.bTransformIsometric, 0, wx.ALL, 5 )
		
		
		bSizer93.Add( bSizer94, 0, wx.EXPAND, 5 )
		
		
		bSizer78.Add( bSizer93, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer78 )
		self.Layout()
		bSizer78.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.pnDisplayPanel.Bind( wx.EVT_PAINT, self.OnPaint )
		self.m_button33.Bind( wx.EVT_BUTTON, self.OnOK )
		self.m_button34.Bind( wx.EVT_BUTTON, self.OnCancel )
		self.bTransformAffine.Bind( wx.EVT_BUTTON, self.OnTransformAffine )
		self.bTransformPerspective.Bind( wx.EVT_BUTTON, self.OnTransformPerspective )
		self.bTransformIsometric.Bind( wx.EVT_BUTTON, self.OnTransformIsometric )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnPaint( self, event ):
		event.Skip()
	
	def OnOK( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		event.Skip()
	
	def OnTransformAffine( self, event ):
		event.Skip()
	
	def OnTransformPerspective( self, event ):
		event.Skip()
	
	def OnTransformIsometric( self, event ):
		event.Skip()
	

###########################################################################
## Class CharacterInfoBase
###########################################################################

class CharacterInfoBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"PC or NPC", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer88 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer97 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer891 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stArmorClass = wx.StaticText( self, wx.ID_ANY, u"AC", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stArmorClass.Wrap( -1 )
		bSizer891.Add( self.stArmorClass, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.stAC_text = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stAC_text.Wrap( -1 )
		bSizer891.Add( self.stAC_text, 0, wx.ALL, 5 )
		
		
		bSizer97.Add( bSizer891, 0, 0, 5 )
		
		bSizer89 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stHitPoints = wx.StaticText( self, wx.ID_ANY, u"Hit Points", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stHitPoints.Wrap( -1 )
		bSizer89.Add( self.stHitPoints, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.spHitPoints = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), wx.SP_ARROW_KEYS, -10, 9999, 6 )
		bSizer89.Add( self.spHitPoints, 0, wx.ALL, 5 )
		
		
		bSizer97.Add( bSizer89, 0, 0, 5 )
		
		
		bSizer88.Add( bSizer97, 0, wx.EXPAND|wx.SHAPED, 5 )
		
		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Attacks" ), wx.VERTICAL )
		
		bSizer122 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText47 = wx.StaticText( self, wx.ID_ANY, u"Melee:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )
		bSizer122.Add( self.m_staticText47, 0, wx.ALL, 5 )
		
		self.stMeleeAttack = wx.StaticText( self, wx.ID_ANY, u"Attacks", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stMeleeAttack.Wrap( -1 )
		bSizer122.Add( self.stMeleeAttack, 0, wx.ALL, 5 )
		
		
		sbSizer11.Add( bSizer122, 1, wx.EXPAND, 5 )
		
		
		bSizer88.Add( sbSizer11, 0, wx.EXPAND, 5 )
		
		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Saves" ), wx.HORIZONTAL )
		
		bSizer94 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText39 = wx.StaticText( self, wx.ID_ANY, u"REF:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )
		bSizer94.Add( self.m_staticText39, 0, wx.ALL, 5 )
		
		self.stReflexSave = wx.StaticText( self, wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stReflexSave.Wrap( -1 )
		bSizer94.Add( self.stReflexSave, 0, wx.ALL, 5 )
		
		
		sbSizer12.Add( bSizer94, 1, 0, 5 )
		
		bSizer95 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText36 = wx.StaticText( self, wx.ID_ANY, u"FORT:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		bSizer95.Add( self.m_staticText36, 0, wx.ALL, 5 )
		
		self.stFortitudeSave = wx.StaticText( self, wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stFortitudeSave.Wrap( -1 )
		bSizer95.Add( self.stFortitudeSave, 0, wx.ALL, 5 )
		
		
		sbSizer12.Add( bSizer95, 1, 0, 5 )
		
		bSizer96 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"WILL:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		bSizer96.Add( self.m_staticText34, 0, wx.ALL, 5 )
		
		self.stWillSave = wx.StaticText( self, wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stWillSave.Wrap( -1 )
		bSizer96.Add( self.stWillSave, 0, wx.ALL, 5 )
		
		
		sbSizer12.Add( bSizer96, 1, 0, 5 )
		
		
		bSizer88.Add( sbSizer12, 0, wx.EXPAND, 5 )
		
		sbSizer13 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Conditions" ), wx.VERTICAL )
		
		gSizer2 = wx.GridSizer( 2, 2, 0, 0 )
		
		cbCondition1Choices = []
		self.cbCondition1 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cbCondition1Choices, 0 )
		gSizer2.Add( self.cbCondition1, 1, wx.EXPAND, 5 )
		
		cbCondition2Choices = []
		self.cbCondition2 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cbCondition2Choices, 0 )
		gSizer2.Add( self.cbCondition2, 1, wx.EXPAND, 5 )
		
		cbCondition3Choices = []
		self.cbCondition3 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cbCondition3Choices, 0 )
		gSizer2.Add( self.cbCondition3, 0, wx.EXPAND, 5 )
		
		cbCondition4Choices = []
		self.cbCondition4 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cbCondition4Choices, 0 )
		gSizer2.Add( self.cbCondition4, 0, wx.EXPAND, 5 )
		
		
		sbSizer13.Add( gSizer2, 0, wx.EXPAND, 5 )
		
		
		bSizer88.Add( sbSizer13, 0, wx.ALL|wx.EXPAND, 0 )
		
		sbSizer14 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Spells" ), wx.VERTICAL )
		
		cbSpellListChoices = []
		self.cbSpellList = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cbSpellListChoices, 0 )
		sbSizer14.Add( self.cbSpellList, 0, wx.EXPAND, 5 )
		
		self.stSpellDescription = wx.StaticText( self, wx.ID_ANY, u"Spell Text", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stSpellDescription.Wrap( -1 )
		sbSizer14.Add( self.stSpellDescription, 0, wx.ALL, 3 )
		
		
		bSizer88.Add( sbSizer14, 0, wx.ALL|wx.EXPAND, 0 )
		
		
		self.SetSizer( bSizer88 )
		self.Layout()
		bSizer88.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class CombatTrackingBase
###########################################################################

class CombatTrackingBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Combat Tracking", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer95 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer97 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer101 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer412 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText66 = wx.StaticText( self, wx.ID_ANY, u"Round:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText66.Wrap( -1 )
		self.m_staticText66.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer412.Add( self.m_staticText66, 0, wx.ALL, 5 )
		
		self.stCurrentRound = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stCurrentRound.Wrap( -1 )
		self.stCurrentRound.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer412.Add( self.stCurrentRound, 0, wx.ALL, 5 )
		
		
		bSizer101.Add( bSizer412, 1, wx.EXPAND, 5 )
		
		bSizer468 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bNextRound = wx.Button( self, wx.ID_ANY, u"Next Round", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bNextRound.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )
		self.bNextRound.SetToolTip( u"Reset the actions, and advance the round counter" )
		
		bSizer468.Add( self.bNextRound, 0, 0, 2 )
		
		self.bResetRound = wx.Button( self, wx.ID_ANY, u"Reset Round", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bResetRound.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )
		self.bResetRound.SetToolTip( u"Reset the round counter to 1" )
		
		bSizer468.Add( self.bResetRound, 0, 0, 2 )
		
		
		bSizer101.Add( bSizer468, 1, wx.EXPAND, 5 )
		
		bSizer411 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, u"Player and NPC information:", wx.DefaultPosition, wx.Size( 175,-1 ), 0 )
		self.m_staticText42.Wrap( -1 )
		bSizer411.Add( self.m_staticText42, 0, wx.ALL, 5 )
		
		
		bSizer101.Add( bSizer411, 1, wx.EXPAND, 5 )
		
		
		bSizer97.Add( bSizer101, 1, wx.ALIGN_BOTTOM, 5 )
		
		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer97.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer403 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText222 = wx.StaticText( self, wx.ID_ANY, u"I n i t", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText222.Wrap( 1 )
		bSizer403.Add( self.m_staticText222, 0, wx.ALL, 5 )
		
		
		bSizer97.Add( bSizer403, 0, 0, 5 )
		
		self.m_staticline37 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer97.Add( self.m_staticline37, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer971 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText421 = wx.StaticText( self, wx.ID_ANY, u"O r d e r", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText421.Wrap( 5 )
		bSizer971.Add( self.m_staticText421, 0, wx.ALL, 5 )
		
		
		bSizer97.Add( bSizer971, 0, 0, 5 )
		
		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer97.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer9711 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText4211 = wx.StaticText( self, wx.ID_ANY, u"D e l a y", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4211.Wrap( 1 )
		bSizer9711.Add( self.m_staticText4211, 0, wx.ALL, 5 )
		
		
		bSizer97.Add( bSizer9711, 0, 0, 5 )
		
		self.m_staticline5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer97.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer9712 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText4212 = wx.StaticText( self, wx.ID_ANY, u"R e a d y", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4212.Wrap( 2 )
		bSizer9712.Add( self.m_staticText4212, 0, wx.ALL, 5 )
		
		
		bSizer97.Add( bSizer9712, 0, 0, 5 )
		
		
		bSizer95.Add( bSizer97, 0, wx.ALL|wx.EXPAND, 5 )
		
		szPlayer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cbPlayerDead1 = wx.CheckBox( self, p1Dead, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbPlayerDead1.SetToolTip( u"Dead?" )
		
		szPlayer1.Add( self.cbPlayerDead1, 0, wx.ALL, 5 )
		
		self.bActivateP1 = wx.Button( self, p1Action, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,20 ), wx.NO_BORDER )
		self.bActivateP1.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		self.bActivateP1.SetToolTip( u"Green=Ready\nRed=Acted\nBlack=Dead" )
		
		szPlayer1.Add( self.bActivateP1, 0, wx.BOTTOM|wx.TOP, 2 )
		
		self.spHitPointsP1 = wx.SpinCtrl( self, p1HP, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), wx.SP_ARROW_KEYS, -10, 9999, 100 )
		self.spHitPointsP1.SetToolTip( u"HP" )
		
		szPlayer1.Add( self.spHitPointsP1, 0, wx.ALL, 2 )
		
		cbPlayer1Choices = []
		self.cbPlayer1 = wx.ComboBox( self, p1Name, u"Combo!", wx.DefaultPosition, wx.Size( 125,-1 ), cbPlayer1Choices, 0 )
		self.cbPlayer1.SetToolTip( u"PC/NPC Name" )
		
		szPlayer1.Add( self.cbPlayer1, 0, wx.ALL, 2 )
		
		self.txInitiative1 = wx.TextCtrl( self, p1Init, u"0", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.txInitiative1.SetMaxLength( 0 ) 
		self.txInitiative1.SetToolTip( u"Initiative for this player" )
		
		szPlayer1.Add( self.txInitiative1, 0, wx.ALL, 2 )
		
		self.rbPlayer1 = wx.RadioButton( self, p1Order, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.RB_GROUP )
		self.rbPlayer1.SetValue( True ) 
		szPlayer1.Add( self.rbPlayer1, 0, wx.ALL, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer1d = wx.RadioButton( self, p1Delay, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer1.Add( self.rbPlayer1d, 0, wx.ALL, 5 )
		
		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer1.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer1r = wx.RadioButton( self, p1Ready, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer1.Add( self.rbPlayer1r, 0, wx.ALL, 5 )
		
		
		bSizer95.Add( szPlayer1, 0, wx.EXPAND, 5 )
		
		szPlayer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cbPlayerDead2 = wx.CheckBox( self, p2Dead, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbPlayerDead2.SetToolTip( u"Dead?" )
		
		szPlayer2.Add( self.cbPlayerDead2, 0, wx.ALL, 5 )
		
		self.bActivateP2 = wx.Button( self, p2Action, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,20 ), wx.NO_BORDER )
		self.bActivateP2.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		self.bActivateP2.SetToolTip( u"Green=Ready\nRed=Acted\nBlack=Dead" )
		
		szPlayer2.Add( self.bActivateP2, 0, wx.BOTTOM|wx.TOP, 2 )
		
		self.spHitPointsP2 = wx.SpinCtrl( self, p2HP, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), wx.SP_ARROW_KEYS, -10, 9999, 100 )
		self.spHitPointsP2.SetToolTip( u"HP" )
		
		szPlayer2.Add( self.spHitPointsP2, 0, wx.ALL, 2 )
		
		cbPlayer2Choices = []
		self.cbPlayer2 = wx.ComboBox( self, p2Name, u"Combo!", wx.DefaultPosition, wx.Size( 125,-1 ), cbPlayer2Choices, 0 )
		self.cbPlayer2.SetToolTip( u"PC/NPC Name" )
		
		szPlayer2.Add( self.cbPlayer2, 0, wx.ALL, 2 )
		
		self.txInitiative2 = wx.TextCtrl( self, p2Init, u"0", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.txInitiative2.SetMaxLength( 0 ) 
		szPlayer2.Add( self.txInitiative2, 0, wx.ALL, 2 )
		
		self.rbPlayer2 = wx.RadioButton( self, p2Order, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.rbPlayer2.SetValue( True ) 
		szPlayer2.Add( self.rbPlayer2, 0, wx.ALL, 5 )
		
		self.m_staticline11 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer2.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer2d = wx.RadioButton( self, p2Delay, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer2.Add( self.rbPlayer2d, 0, wx.ALL, 5 )
		
		self.m_staticline21 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer2.Add( self.m_staticline21, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer2r = wx.RadioButton( self, p2Ready, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer2.Add( self.rbPlayer2r, 0, wx.ALL, 5 )
		
		
		bSizer95.Add( szPlayer2, 0, wx.EXPAND, 5 )
		
		szPlayer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cbPlayerDead3 = wx.CheckBox( self, p3Dead, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbPlayerDead3.SetToolTip( u"Dead?" )
		
		szPlayer3.Add( self.cbPlayerDead3, 0, wx.ALL, 5 )
		
		self.bActivateP3 = wx.Button( self, p3Action, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,20 ), wx.NO_BORDER )
		self.bActivateP3.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		self.bActivateP3.SetToolTip( u"Green=Ready\nRed=Acted\nBlack=Dead" )
		
		szPlayer3.Add( self.bActivateP3, 0, wx.BOTTOM|wx.TOP, 2 )
		
		self.spHitPointsP3 = wx.SpinCtrl( self, p3HP, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), wx.SP_ARROW_KEYS, -10, 9999, 100 )
		self.spHitPointsP3.SetToolTip( u"HP" )
		
		szPlayer3.Add( self.spHitPointsP3, 0, wx.ALL, 2 )
		
		cbPlayer3Choices = []
		self.cbPlayer3 = wx.ComboBox( self, p3Name, u"Combo!", wx.DefaultPosition, wx.Size( 125,-1 ), cbPlayer3Choices, 0 )
		self.cbPlayer3.SetToolTip( u"PC/NPC Name" )
		
		szPlayer3.Add( self.cbPlayer3, 0, wx.ALL, 2 )
		
		self.txInitiative3 = wx.TextCtrl( self, p3Init, u"0", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.txInitiative3.SetMaxLength( 0 ) 
		szPlayer3.Add( self.txInitiative3, 0, wx.ALL, 2 )
		
		self.rbPlayer3 = wx.RadioButton( self, p3Order, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.rbPlayer3.SetValue( True ) 
		szPlayer3.Add( self.rbPlayer3, 0, wx.ALL, 5 )
		
		self.m_staticline12 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer3.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer3d = wx.RadioButton( self, p3Delay, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer3.Add( self.rbPlayer3d, 0, wx.ALL, 5 )
		
		self.m_staticline22 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer3.Add( self.m_staticline22, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer3r = wx.RadioButton( self, p3Ready, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer3.Add( self.rbPlayer3r, 0, wx.ALL, 5 )
		
		
		bSizer95.Add( szPlayer3, 0, wx.EXPAND, 5 )
		
		szPlayer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cbPlayerDead4 = wx.CheckBox( self, p4Dead, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbPlayerDead4.SetToolTip( u"Dead?" )
		
		szPlayer4.Add( self.cbPlayerDead4, 0, wx.ALL, 5 )
		
		self.bActivateP4 = wx.Button( self, p4Action, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,20 ), wx.NO_BORDER )
		self.bActivateP4.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		self.bActivateP4.SetToolTip( u"Green=Ready\nRed=Acted\nBlack=Dead" )
		
		szPlayer4.Add( self.bActivateP4, 0, wx.BOTTOM|wx.TOP, 2 )
		
		self.spHitPointsP4 = wx.SpinCtrl( self, p4HP, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), wx.SP_ARROW_KEYS, -10, 9999, 100 )
		self.spHitPointsP4.SetToolTip( u"HP" )
		
		szPlayer4.Add( self.spHitPointsP4, 0, wx.ALL, 2 )
		
		cbPlayer4Choices = []
		self.cbPlayer4 = wx.ComboBox( self, p4Name, u"Combo!", wx.DefaultPosition, wx.Size( 125,-1 ), cbPlayer4Choices, 0 )
		self.cbPlayer4.SetToolTip( u"PC/NPC Name" )
		
		szPlayer4.Add( self.cbPlayer4, 0, wx.ALL, 2 )
		
		self.txInitiative4 = wx.TextCtrl( self, p4Init, u"0", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.txInitiative4.SetMaxLength( 0 ) 
		szPlayer4.Add( self.txInitiative4, 0, wx.ALL, 2 )
		
		self.rbPlayer4 = wx.RadioButton( self, p4Order, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.rbPlayer4.SetValue( True ) 
		szPlayer4.Add( self.rbPlayer4, 0, wx.ALL, 5 )
		
		self.m_staticline13 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer4.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer4d = wx.RadioButton( self, p4Delay, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer4.Add( self.rbPlayer4d, 0, wx.ALL, 5 )
		
		self.m_staticline23 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer4.Add( self.m_staticline23, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer4r = wx.RadioButton( self, p4Ready, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer4.Add( self.rbPlayer4r, 0, wx.ALL, 5 )
		
		
		bSizer95.Add( szPlayer4, 0, wx.EXPAND, 5 )
		
		szPlayer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cbPlayerDead5 = wx.CheckBox( self, p5Dead, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbPlayerDead5.SetToolTip( u"Dead?" )
		
		szPlayer5.Add( self.cbPlayerDead5, 0, wx.ALL, 5 )
		
		self.bActivateP5 = wx.Button( self, p5Action, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,20 ), wx.NO_BORDER )
		self.bActivateP5.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		self.bActivateP5.SetToolTip( u"Green=Ready\nRed=Acted\nBlack=Dead" )
		
		szPlayer5.Add( self.bActivateP5, 0, wx.BOTTOM|wx.TOP, 2 )
		
		self.spHitPointsP5 = wx.SpinCtrl( self, p5HP, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), wx.SP_ARROW_KEYS, -10, 9999, 100 )
		self.spHitPointsP5.SetToolTip( u"HP" )
		
		szPlayer5.Add( self.spHitPointsP5, 0, wx.ALL, 2 )
		
		cbPlayer5Choices = []
		self.cbPlayer5 = wx.ComboBox( self, p5Name, u"Combo!", wx.DefaultPosition, wx.Size( 125,-1 ), cbPlayer5Choices, 0 )
		self.cbPlayer5.SetToolTip( u"PC/NPC Name" )
		
		szPlayer5.Add( self.cbPlayer5, 0, wx.ALL, 2 )
		
		self.txInitiative5 = wx.TextCtrl( self, p5Init, u"0", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.txInitiative5.SetMaxLength( 0 ) 
		szPlayer5.Add( self.txInitiative5, 0, wx.ALL, 2 )
		
		self.rbPlayer5 = wx.RadioButton( self, p5Order, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.rbPlayer5.SetValue( True ) 
		szPlayer5.Add( self.rbPlayer5, 0, wx.ALL, 5 )
		
		self.m_staticline14 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer5.Add( self.m_staticline14, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer5d = wx.RadioButton( self, p5Delay, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer5.Add( self.rbPlayer5d, 0, wx.ALL, 5 )
		
		self.m_staticline24 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer5.Add( self.m_staticline24, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer5r = wx.RadioButton( self, p5Ready, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer5.Add( self.rbPlayer5r, 0, wx.ALL, 5 )
		
		
		bSizer95.Add( szPlayer5, 0, wx.EXPAND, 5 )
		
		szPlayer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cbPlayerDead6 = wx.CheckBox( self, p6Dead, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbPlayerDead6.SetToolTip( u"Dead?" )
		
		szPlayer6.Add( self.cbPlayerDead6, 0, wx.ALL, 5 )
		
		self.bActivateP6 = wx.Button( self, p6Action, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,20 ), wx.NO_BORDER )
		self.bActivateP6.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		self.bActivateP6.SetToolTip( u"Green=Ready\nRed=Acted\nBlack=Dead" )
		
		szPlayer6.Add( self.bActivateP6, 0, wx.BOTTOM|wx.TOP, 2 )
		
		self.spHitPointsP6 = wx.SpinCtrl( self, p6HP, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), wx.SP_ARROW_KEYS, -10, 9999, 100 )
		self.spHitPointsP6.SetToolTip( u"HP" )
		
		szPlayer6.Add( self.spHitPointsP6, 0, wx.ALL, 2 )
		
		cbPlayer6Choices = []
		self.cbPlayer6 = wx.ComboBox( self, p6Name, u"Combo!", wx.DefaultPosition, wx.Size( 125,-1 ), cbPlayer6Choices, 0 )
		self.cbPlayer6.SetToolTip( u"PC/NPC Name" )
		
		szPlayer6.Add( self.cbPlayer6, 0, wx.ALL, 2 )
		
		self.txInitiative6 = wx.TextCtrl( self, p6Init, u"0", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.txInitiative6.SetMaxLength( 0 ) 
		szPlayer6.Add( self.txInitiative6, 0, wx.ALL, 2 )
		
		self.rbPlayer6 = wx.RadioButton( self, p6Order, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.rbPlayer6.SetValue( True ) 
		szPlayer6.Add( self.rbPlayer6, 0, wx.ALL, 5 )
		
		self.m_staticline141 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer6.Add( self.m_staticline141, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer6d = wx.RadioButton( self, p6Delay, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer6.Add( self.rbPlayer6d, 0, wx.ALL, 5 )
		
		self.m_staticline241 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer6.Add( self.m_staticline241, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer6r = wx.RadioButton( self, p6Ready, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer6.Add( self.rbPlayer6r, 0, wx.ALL, 5 )
		
		
		bSizer95.Add( szPlayer6, 0, wx.EXPAND, 5 )
		
		szPlayer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cbPlayerDead7 = wx.CheckBox( self, p7Dead, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbPlayerDead7.SetToolTip( u"Dead?" )
		
		szPlayer7.Add( self.cbPlayerDead7, 0, wx.ALL, 5 )
		
		self.bActivateP7 = wx.Button( self, p7Action, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,20 ), wx.NO_BORDER )
		self.bActivateP7.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		self.bActivateP7.SetToolTip( u"Green=Ready\nRed=Acted\nBlack=Dead" )
		
		szPlayer7.Add( self.bActivateP7, 0, wx.BOTTOM|wx.TOP, 2 )
		
		self.spHitPointsP7 = wx.SpinCtrl( self, p7HP, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), wx.SP_ARROW_KEYS, -10, 9999, 100 )
		self.spHitPointsP7.SetToolTip( u"HP" )
		
		szPlayer7.Add( self.spHitPointsP7, 0, wx.ALL, 2 )
		
		cbPlayer7Choices = []
		self.cbPlayer7 = wx.ComboBox( self, p7Name, u"Combo!", wx.DefaultPosition, wx.Size( 125,-1 ), cbPlayer7Choices, 0 )
		self.cbPlayer7.SetToolTip( u"PC/NPC Name" )
		
		szPlayer7.Add( self.cbPlayer7, 0, wx.ALL, 2 )
		
		self.txInitiative7 = wx.TextCtrl( self, p7Init, u"0", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.txInitiative7.SetMaxLength( 0 ) 
		szPlayer7.Add( self.txInitiative7, 0, wx.ALL, 2 )
		
		self.rbPlayer7 = wx.RadioButton( self, p7Order, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.rbPlayer7.SetValue( True ) 
		szPlayer7.Add( self.rbPlayer7, 0, wx.ALL, 5 )
		
		self.m_staticline142 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer7.Add( self.m_staticline142, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer7d = wx.RadioButton( self, p7Delay, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer7.Add( self.rbPlayer7d, 0, wx.ALL, 5 )
		
		self.m_staticline242 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer7.Add( self.m_staticline242, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer7r = wx.RadioButton( self, p7Ready, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer7.Add( self.rbPlayer7r, 0, wx.ALL, 5 )
		
		
		bSizer95.Add( szPlayer7, 0, wx.EXPAND, 5 )
		
		szPlayer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cbPlayerDead8 = wx.CheckBox( self, p8Dead, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbPlayerDead8.SetToolTip( u"Dead?" )
		
		szPlayer8.Add( self.cbPlayerDead8, 0, wx.ALL, 5 )
		
		self.bActivateP8 = wx.Button( self, p8Action, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,20 ), wx.NO_BORDER )
		self.bActivateP8.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		self.bActivateP8.SetToolTip( u"Green=Ready\nRed=Acted\nBlack=Dead" )
		
		szPlayer8.Add( self.bActivateP8, 0, wx.BOTTOM|wx.TOP, 2 )
		
		self.spHitPointsP8 = wx.SpinCtrl( self, p8HP, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), wx.SP_ARROW_KEYS, -10, 9999, 100 )
		self.spHitPointsP8.SetToolTip( u"HP" )
		
		szPlayer8.Add( self.spHitPointsP8, 0, wx.ALL, 2 )
		
		cbPlayer8Choices = []
		self.cbPlayer8 = wx.ComboBox( self, p8Name, u"Combo!", wx.DefaultPosition, wx.Size( 125,-1 ), cbPlayer8Choices, 0 )
		self.cbPlayer8.SetToolTip( u"PC/NPC Name" )
		
		szPlayer8.Add( self.cbPlayer8, 0, wx.ALL, 2 )
		
		self.txInitiative8 = wx.TextCtrl( self, p8Init, u"0", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.txInitiative8.SetMaxLength( 0 ) 
		szPlayer8.Add( self.txInitiative8, 0, wx.ALL, 2 )
		
		self.rbPlayer8 = wx.RadioButton( self, p8Order, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.rbPlayer8.SetValue( True ) 
		szPlayer8.Add( self.rbPlayer8, 0, wx.ALL, 5 )
		
		self.m_staticline143 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer8.Add( self.m_staticline143, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer8d = wx.RadioButton( self, p8Delay, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer8.Add( self.rbPlayer8d, 0, wx.ALL, 5 )
		
		self.m_staticline243 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer8.Add( self.m_staticline243, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer8r = wx.RadioButton( self, p8Ready, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer8.Add( self.rbPlayer8r, 0, wx.ALL, 5 )
		
		
		bSizer95.Add( szPlayer8, 0, wx.EXPAND, 5 )
		
		szPlayer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cbPlayerDead9 = wx.CheckBox( self, p9Dead, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbPlayerDead9.SetToolTip( u"Dead?" )
		
		szPlayer9.Add( self.cbPlayerDead9, 0, wx.ALL, 5 )
		
		self.bActivateP9 = wx.Button( self, p9Action, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,20 ), wx.NO_BORDER )
		self.bActivateP9.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		self.bActivateP9.SetToolTip( u"Green=Ready\nRed=Acted\nBlack=Dead" )
		
		szPlayer9.Add( self.bActivateP9, 0, wx.BOTTOM|wx.TOP, 2 )
		
		self.spHitPointsP9 = wx.SpinCtrl( self, p9HP, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), wx.SP_ARROW_KEYS, -10, 9999, 100 )
		self.spHitPointsP9.SetToolTip( u"HP" )
		
		szPlayer9.Add( self.spHitPointsP9, 0, wx.ALL, 2 )
		
		cbPlayer9Choices = []
		self.cbPlayer9 = wx.ComboBox( self, p9Name, u"Combo!", wx.DefaultPosition, wx.Size( 125,-1 ), cbPlayer9Choices, 0 )
		self.cbPlayer9.SetToolTip( u"PC/NPC Name" )
		
		szPlayer9.Add( self.cbPlayer9, 0, wx.ALL, 2 )
		
		self.txInitiative9 = wx.TextCtrl( self, p9Init, u"0", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.txInitiative9.SetMaxLength( 0 ) 
		szPlayer9.Add( self.txInitiative9, 0, wx.ALL, 2 )
		
		self.rbPlayer9 = wx.RadioButton( self, p9Order, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.rbPlayer9.SetValue( True ) 
		szPlayer9.Add( self.rbPlayer9, 0, wx.ALL, 5 )
		
		self.m_staticline144 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer9.Add( self.m_staticline144, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer9d = wx.RadioButton( self, p9Delay, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer9.Add( self.rbPlayer9d, 0, wx.ALL, 5 )
		
		self.m_staticline244 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer9.Add( self.m_staticline244, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer9r = wx.RadioButton( self, p9Ready, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer9.Add( self.rbPlayer9r, 0, wx.ALL, 5 )
		
		
		bSizer95.Add( szPlayer9, 0, wx.EXPAND, 5 )
		
		szPlayer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cbPlayerDead10 = wx.CheckBox( self, p10Dead, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbPlayerDead10.SetToolTip( u"Dead?" )
		
		szPlayer10.Add( self.cbPlayerDead10, 0, wx.ALL, 5 )
		
		self.bActivateP10 = wx.Button( self, p10Action, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,20 ), wx.NO_BORDER )
		self.bActivateP10.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		self.bActivateP10.SetToolTip( u"Green=Ready\nRed=Acted\nBlack=Dead" )
		
		szPlayer10.Add( self.bActivateP10, 0, wx.BOTTOM|wx.TOP, 2 )
		
		self.spHitPointsP10 = wx.SpinCtrl( self, p10HP, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), wx.SP_ARROW_KEYS, -10, 9999, 100 )
		self.spHitPointsP10.SetToolTip( u"HP" )
		
		szPlayer10.Add( self.spHitPointsP10, 0, wx.ALL, 2 )
		
		cbPlayer10Choices = []
		self.cbPlayer10 = wx.ComboBox( self, p10Name, u"Combo!", wx.DefaultPosition, wx.Size( 125,-1 ), cbPlayer10Choices, 0 )
		self.cbPlayer10.SetToolTip( u"PC/NPC Name" )
		
		szPlayer10.Add( self.cbPlayer10, 0, wx.ALL, 2 )
		
		self.txInitiative10 = wx.TextCtrl( self, p10Init, u"0", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.txInitiative10.SetMaxLength( 0 ) 
		szPlayer10.Add( self.txInitiative10, 0, wx.ALL, 2 )
		
		self.rbPlayer10 = wx.RadioButton( self, p10Order, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.rbPlayer10.SetValue( True ) 
		szPlayer10.Add( self.rbPlayer10, 0, wx.ALL, 5 )
		
		self.m_staticline145 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer10.Add( self.m_staticline145, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer10d = wx.RadioButton( self, p10Delay, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer10.Add( self.rbPlayer10d, 0, wx.ALL, 5 )
		
		self.m_staticline245 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer10.Add( self.m_staticline245, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer10r = wx.RadioButton( self, p10Ready, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer10.Add( self.rbPlayer10r, 0, wx.ALL, 5 )
		
		
		bSizer95.Add( szPlayer10, 0, wx.EXPAND, 5 )
		
		szPlayer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cbPlayerDead11 = wx.CheckBox( self, p11Dead, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbPlayerDead11.SetToolTip( u"Dead?" )
		
		szPlayer11.Add( self.cbPlayerDead11, 0, wx.ALL, 5 )
		
		self.bActivateP11 = wx.Button( self, p11Action, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,20 ), wx.NO_BORDER )
		self.bActivateP11.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		self.bActivateP11.SetToolTip( u"Green=Ready\nRed=Acted\nBlack=Dead" )
		
		szPlayer11.Add( self.bActivateP11, 0, wx.BOTTOM|wx.TOP, 2 )
		
		self.spHitPointsP11 = wx.SpinCtrl( self, p11HP, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), wx.SP_ARROW_KEYS, -10, 9999, 100 )
		self.spHitPointsP11.SetToolTip( u"HP" )
		
		szPlayer11.Add( self.spHitPointsP11, 0, wx.ALL, 2 )
		
		cbPlayer11Choices = []
		self.cbPlayer11 = wx.ComboBox( self, p11Name, u"Combo!", wx.DefaultPosition, wx.Size( 125,-1 ), cbPlayer11Choices, 0 )
		self.cbPlayer11.SetToolTip( u"PC/NPC Name" )
		
		szPlayer11.Add( self.cbPlayer11, 0, wx.ALL, 2 )
		
		self.txInitiative11 = wx.TextCtrl( self, p11Init, u"0", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.txInitiative11.SetMaxLength( 0 ) 
		szPlayer11.Add( self.txInitiative11, 0, wx.ALL, 2 )
		
		self.rbPlayer11 = wx.RadioButton( self, p11Order, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.rbPlayer11.SetValue( True ) 
		szPlayer11.Add( self.rbPlayer11, 0, wx.ALL, 5 )
		
		self.m_staticline146 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer11.Add( self.m_staticline146, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer11d = wx.RadioButton( self, p11Delay, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer11.Add( self.rbPlayer11d, 0, wx.ALL, 5 )
		
		self.m_staticline246 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer11.Add( self.m_staticline246, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer11r = wx.RadioButton( self, p11Ready, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer11.Add( self.rbPlayer11r, 0, wx.ALL, 5 )
		
		
		bSizer95.Add( szPlayer11, 0, wx.EXPAND, 5 )
		
		szPlayer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cbPlayerDead12 = wx.CheckBox( self, p12Dead, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbPlayerDead12.SetToolTip( u"Dead?" )
		
		szPlayer12.Add( self.cbPlayerDead12, 0, wx.ALL, 5 )
		
		self.bActivateP12 = wx.Button( self, p12Action, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,20 ), wx.NO_BORDER )
		self.bActivateP12.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		self.bActivateP12.SetToolTip( u"Green=Ready\nRed=Acted\nBlack=Dead" )
		
		szPlayer12.Add( self.bActivateP12, 0, wx.BOTTOM|wx.TOP, 2 )
		
		self.spHitPointsP12 = wx.SpinCtrl( self, p12HP, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), wx.SP_ARROW_KEYS, -10, 9999, 100 )
		self.spHitPointsP12.SetToolTip( u"HP" )
		
		szPlayer12.Add( self.spHitPointsP12, 0, wx.ALL, 2 )
		
		cbPlayer12Choices = []
		self.cbPlayer12 = wx.ComboBox( self, p12Name, u"Combo!", wx.DefaultPosition, wx.Size( 125,-1 ), cbPlayer12Choices, 0 )
		self.cbPlayer12.SetToolTip( u"PC/NPC Name" )
		
		szPlayer12.Add( self.cbPlayer12, 0, wx.ALL, 2 )
		
		self.txInitiative12 = wx.TextCtrl( self, p12Init, u"0", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.txInitiative12.SetMaxLength( 0 ) 
		szPlayer12.Add( self.txInitiative12, 0, wx.ALL, 2 )
		
		self.rbPlayer12 = wx.RadioButton( self, p12Order, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.rbPlayer12.SetValue( True ) 
		szPlayer12.Add( self.rbPlayer12, 0, wx.ALL, 5 )
		
		self.m_staticline147 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer12.Add( self.m_staticline147, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer12d = wx.RadioButton( self, p12Delay, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer12.Add( self.rbPlayer12d, 0, wx.ALL, 5 )
		
		self.m_staticline247 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer12.Add( self.m_staticline247, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer12r = wx.RadioButton( self, p12Ready, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer12.Add( self.rbPlayer12r, 0, wx.ALL, 5 )
		
		
		bSizer95.Add( szPlayer12, 0, wx.EXPAND, 5 )
		
		szPlayer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cbPlayerDead13 = wx.CheckBox( self, p13Dead, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbPlayerDead13.SetToolTip( u"Dead?" )
		
		szPlayer13.Add( self.cbPlayerDead13, 0, wx.ALL, 5 )
		
		self.bActivateP13 = wx.Button( self, p13Action, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,20 ), wx.NO_BORDER )
		self.bActivateP13.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		self.bActivateP13.SetToolTip( u"Green=Ready\nRed=Acted\nBlack=Dead" )
		
		szPlayer13.Add( self.bActivateP13, 0, wx.BOTTOM|wx.TOP, 2 )
		
		self.spHitPointsP13 = wx.SpinCtrl( self, p13HP, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), wx.SP_ARROW_KEYS, -10, 9999, 100 )
		self.spHitPointsP13.SetToolTip( u"HP" )
		
		szPlayer13.Add( self.spHitPointsP13, 0, wx.ALL, 2 )
		
		cbPlayer13Choices = []
		self.cbPlayer13 = wx.ComboBox( self, p13Name, u"Combo!", wx.DefaultPosition, wx.Size( 125,-1 ), cbPlayer13Choices, 0 )
		self.cbPlayer13.SetToolTip( u"PC/NPC Name" )
		
		szPlayer13.Add( self.cbPlayer13, 0, wx.ALL, 2 )
		
		self.txInitiative13 = wx.TextCtrl( self, p13Init, u"0", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.txInitiative13.SetMaxLength( 0 ) 
		szPlayer13.Add( self.txInitiative13, 0, wx.ALL, 2 )
		
		self.rbPlayer13 = wx.RadioButton( self, p13Order, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.rbPlayer13.SetValue( True ) 
		szPlayer13.Add( self.rbPlayer13, 0, wx.ALL, 5 )
		
		self.m_staticline148 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer13.Add( self.m_staticline148, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer13d = wx.RadioButton( self, p13Delay, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer13.Add( self.rbPlayer13d, 0, wx.ALL, 5 )
		
		self.m_staticline248 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer13.Add( self.m_staticline248, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer13r = wx.RadioButton( self, p13Ready, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer13.Add( self.rbPlayer13r, 0, wx.ALL, 5 )
		
		
		bSizer95.Add( szPlayer13, 0, wx.EXPAND, 5 )
		
		szPlayer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cbPlayerDead14 = wx.CheckBox( self, p14Dead, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbPlayerDead14.SetToolTip( u"Dead?" )
		
		szPlayer14.Add( self.cbPlayerDead14, 0, wx.ALL, 5 )
		
		self.bActivateP14 = wx.Button( self, p14Action, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,20 ), wx.NO_BORDER )
		self.bActivateP14.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		self.bActivateP14.SetToolTip( u"Green=Ready\nRed=Acted\nBlack=Dead" )
		
		szPlayer14.Add( self.bActivateP14, 0, wx.BOTTOM|wx.TOP, 2 )
		
		self.spHitPointsP14 = wx.SpinCtrl( self, p14HP, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), wx.SP_ARROW_KEYS, -10, 9999, 100 )
		self.spHitPointsP14.SetToolTip( u"HP" )
		
		szPlayer14.Add( self.spHitPointsP14, 0, wx.ALL, 2 )
		
		cbPlayer14Choices = []
		self.cbPlayer14 = wx.ComboBox( self, p14Name, u"Combo!", wx.DefaultPosition, wx.Size( 125,-1 ), cbPlayer14Choices, 0 )
		self.cbPlayer14.SetToolTip( u"PC/NPC Name" )
		
		szPlayer14.Add( self.cbPlayer14, 0, wx.ALL, 2 )
		
		self.txInitiative14 = wx.TextCtrl( self, p14Init, u"0", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.txInitiative14.SetMaxLength( 0 ) 
		szPlayer14.Add( self.txInitiative14, 0, wx.ALL, 2 )
		
		self.rbPlayer14 = wx.RadioButton( self, p14Order, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.rbPlayer14.SetValue( True ) 
		szPlayer14.Add( self.rbPlayer14, 0, wx.ALL, 5 )
		
		self.m_staticline149 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer14.Add( self.m_staticline149, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer14d = wx.RadioButton( self, p14Delay, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer14.Add( self.rbPlayer14d, 0, wx.ALL, 5 )
		
		self.m_staticline249 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer14.Add( self.m_staticline249, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer14r = wx.RadioButton( self, p14Ready, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer14.Add( self.rbPlayer14r, 0, wx.ALL, 5 )
		
		
		bSizer95.Add( szPlayer14, 0, wx.EXPAND, 5 )
		
		szPlayer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cbPlayerDead15 = wx.CheckBox( self, p15Dead, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbPlayerDead15.SetToolTip( u"Dead?" )
		
		szPlayer15.Add( self.cbPlayerDead15, 0, wx.ALL, 5 )
		
		self.bActivateP15 = wx.Button( self, p15Action, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,20 ), wx.NO_BORDER )
		self.bActivateP15.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		self.bActivateP15.SetToolTip( u"Green=Ready\nRed=Acted\nBlack=Dead" )
		
		szPlayer15.Add( self.bActivateP15, 0, wx.BOTTOM|wx.TOP, 2 )
		
		self.spHitPointsP15 = wx.SpinCtrl( self, p15HP, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), wx.SP_ARROW_KEYS, -10, 9999, 100 )
		self.spHitPointsP15.SetToolTip( u"HP" )
		
		szPlayer15.Add( self.spHitPointsP15, 0, wx.ALL, 2 )
		
		cbPlayer15Choices = []
		self.cbPlayer15 = wx.ComboBox( self, p15Name, u"Combo!", wx.DefaultPosition, wx.Size( 125,-1 ), cbPlayer15Choices, 0 )
		self.cbPlayer15.SetToolTip( u"PC/NPC Name" )
		
		szPlayer15.Add( self.cbPlayer15, 0, wx.ALL, 2 )
		
		self.txInitiative15 = wx.TextCtrl( self, p15Init, u"0", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.txInitiative15.SetMaxLength( 0 ) 
		szPlayer15.Add( self.txInitiative15, 0, wx.ALL, 2 )
		
		self.rbPlayer15 = wx.RadioButton( self, p15Order, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.rbPlayer15.SetValue( True ) 
		szPlayer15.Add( self.rbPlayer15, 0, wx.ALL, 5 )
		
		self.m_staticline1410 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer15.Add( self.m_staticline1410, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer15d = wx.RadioButton( self, p15Delay, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer15.Add( self.rbPlayer15d, 0, wx.ALL, 5 )
		
		self.m_staticline2410 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		szPlayer15.Add( self.m_staticline2410, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rbPlayer15r = wx.RadioButton( self, p15Ready, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		szPlayer15.Add( self.rbPlayer15r, 0, wx.ALL, 5 )
		
		
		bSizer95.Add( szPlayer15, 0, wx.EXPAND, 5 )
		
		bSizer108 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer133 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bAddNames = wx.Button( self, wx.ID_ANY, u"Add Names...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bAddNames.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )
		self.bAddNames.SetToolTip( u"Add names to the selection list" )
		
		bSizer133.Add( self.bAddNames, 0, 0, 2 )
		
		self.bSortInitiative = wx.Button( self, wx.ID_ANY, u"Sort Initiative", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bSortInitiative.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )
		self.bSortInitiative.SetToolTip( u"Sort the players by initiative ranking" )
		
		bSizer133.Add( self.bSortInitiative, 0, wx.ALL, 2 )
		
		self.bResetAll = wx.Button( self, wx.ID_ANY, u"Reset All", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bResetAll.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )
		self.bResetAll.SetToolTip( u"Reset the actions, HP, round counter, and status to default values " )
		
		bSizer133.Add( self.bResetAll, 0, wx.ALL, 2 )
		
		
		bSizer108.Add( bSizer133, 1, wx.EXPAND, 5 )
		
		bSizer118 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bClose = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bClose.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.bClose.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.bClose.SetBackgroundColour( wx.Colour( 0, 108, 54 ) )
		
		bSizer118.Add( self.bClose, 0, wx.ALIGN_LEFT|wx.ALL, 2 )
		
		self.bHelp = wx.Button( self, wx.ID_ANY, u"Help...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bHelp.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.bHelp.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bHelp.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer118.Add( self.bHelp, 0, wx.ALIGN_RIGHT|wx.ALL, 2 )
		
		self.cbSaveData = wx.CheckBox( self, wx.ID_ANY, u"Save data?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbSaveData.SetValue(True) 
		self.cbSaveData.SetToolTip( u"Save the state of all items if checked" )
		
		bSizer118.Add( self.cbSaveData, 0, wx.ALL, 5 )
		
		
		bSizer108.Add( bSizer118, 0, wx.EXPAND, 5 )
		
		
		bSizer95.Add( bSizer108, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer95 )
		self.Layout()
		bSizer95.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.bNextRound.Bind( wx.EVT_BUTTON, self.OnNextRound )
		self.bResetRound.Bind( wx.EVT_BUTTON, self.OnResetRound )
		self.cbPlayerDead1.Bind( wx.EVT_CHECKBOX, self.OnKillPlayer1 )
		self.bActivateP1.Bind( wx.EVT_BUTTON, self.OnActivatePlayer )
		self.cbPlayerDead2.Bind( wx.EVT_CHECKBOX, self.OnKillPlayer2 )
		self.bActivateP2.Bind( wx.EVT_BUTTON, self.OnActivatePlayer )
		self.cbPlayerDead3.Bind( wx.EVT_CHECKBOX, self.OnKillPlayer3 )
		self.bActivateP3.Bind( wx.EVT_BUTTON, self.OnActivatePlayer )
		self.cbPlayerDead4.Bind( wx.EVT_CHECKBOX, self.OnKillPlayer4 )
		self.bActivateP4.Bind( wx.EVT_BUTTON, self.OnActivatePlayer )
		self.cbPlayerDead5.Bind( wx.EVT_CHECKBOX, self.OnKillPlayer5 )
		self.bActivateP5.Bind( wx.EVT_BUTTON, self.OnActivatePlayer )
		self.cbPlayerDead6.Bind( wx.EVT_CHECKBOX, self.OnKillPlayer6 )
		self.bActivateP6.Bind( wx.EVT_BUTTON, self.OnActivatePlayer )
		self.cbPlayerDead7.Bind( wx.EVT_CHECKBOX, self.OnKillPlayer7 )
		self.bActivateP7.Bind( wx.EVT_BUTTON, self.OnActivatePlayer )
		self.cbPlayerDead8.Bind( wx.EVT_CHECKBOX, self.OnKillPlayer8 )
		self.bActivateP8.Bind( wx.EVT_BUTTON, self.OnActivatePlayer )
		self.cbPlayerDead9.Bind( wx.EVT_CHECKBOX, self.OnKillPlayer9 )
		self.bActivateP9.Bind( wx.EVT_BUTTON, self.OnActivatePlayer )
		self.cbPlayerDead10.Bind( wx.EVT_CHECKBOX, self.OnKillPlayer10 )
		self.bActivateP10.Bind( wx.EVT_BUTTON, self.OnActivatePlayer )
		self.cbPlayerDead11.Bind( wx.EVT_CHECKBOX, self.OnKillPlayer11 )
		self.bActivateP11.Bind( wx.EVT_BUTTON, self.OnActivatePlayer )
		self.cbPlayerDead12.Bind( wx.EVT_CHECKBOX, self.OnKillPlayer12 )
		self.bActivateP12.Bind( wx.EVT_BUTTON, self.OnActivatePlayer )
		self.cbPlayerDead13.Bind( wx.EVT_CHECKBOX, self.OnKillPlayer13 )
		self.bActivateP13.Bind( wx.EVT_BUTTON, self.OnActivatePlayer )
		self.cbPlayerDead14.Bind( wx.EVT_CHECKBOX, self.OnKillPlayer14 )
		self.bActivateP14.Bind( wx.EVT_BUTTON, self.OnActivatePlayer )
		self.cbPlayerDead15.Bind( wx.EVT_CHECKBOX, self.OnKillPlayer15 )
		self.bActivateP15.Bind( wx.EVT_BUTTON, self.OnActivatePlayer )
		self.bAddNames.Bind( wx.EVT_BUTTON, self.OnAddNames )
		self.bSortInitiative.Bind( wx.EVT_BUTTON, self.OnSortInitiative )
		self.bResetAll.Bind( wx.EVT_BUTTON, self.OnResetAllValues )
		self.bClose.Bind( wx.EVT_BUTTON, self.OnClose )
		self.bHelp.Bind( wx.EVT_BUTTON, self.OnHelp )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()
	
	def OnNextRound( self, event ):
		event.Skip()
	
	def OnResetRound( self, event ):
		event.Skip()
	
	def OnKillPlayer1( self, event ):
		event.Skip()
	
	def OnActivatePlayer( self, event ):
		event.Skip()
	
	def OnKillPlayer2( self, event ):
		event.Skip()
	
	
	def OnKillPlayer3( self, event ):
		event.Skip()
	
	
	def OnKillPlayer4( self, event ):
		event.Skip()
	
	
	def OnKillPlayer5( self, event ):
		event.Skip()
	
	
	def OnKillPlayer6( self, event ):
		event.Skip()
	
	
	def OnKillPlayer7( self, event ):
		event.Skip()
	
	
	def OnKillPlayer8( self, event ):
		event.Skip()
	
	
	def OnKillPlayer9( self, event ):
		event.Skip()
	
	
	def OnKillPlayer10( self, event ):
		event.Skip()
	
	
	def OnKillPlayer11( self, event ):
		event.Skip()
	
	
	def OnKillPlayer12( self, event ):
		event.Skip()
	
	
	def OnKillPlayer13( self, event ):
		event.Skip()
	
	
	def OnKillPlayer14( self, event ):
		event.Skip()
	
	
	def OnKillPlayer15( self, event ):
		event.Skip()
	
	
	def OnAddNames( self, event ):
		event.Skip()
	
	def OnSortInitiative( self, event ):
		event.Skip()
	
	def OnResetAllValues( self, event ):
		event.Skip()
	
	
	def OnHelp( self, event ):
		event.Skip()
	

###########################################################################
## Class TextEntryDialogBase
###########################################################################

class TextEntryDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add Names", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer119 = wx.BoxSizer( wx.VERTICAL )
		
		self.txNames = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,200 ), wx.TE_MULTILINE )
		self.txNames.SetMaxLength( 0 ) 
		bSizer119.Add( self.txNames, 0, wx.ALL|wx.EXPAND|wx.SHAPED, 5 )
		
		bSizer121 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bOkButton = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bOkButton.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.bOkButton.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.bOkButton.SetBackgroundColour( wx.Colour( 0, 64, 0 ) )
		
		bSizer121.Add( self.bOkButton, 0, wx.ALL, 2 )
		
		self.bCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bCancel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.bCancel.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bCancel.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		
		bSizer121.Add( self.bCancel, 0, wx.ALL, 2 )
		
		
		bSizer119.Add( bSizer121, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 0 )
		
		
		self.SetSizer( bSizer119 )
		self.Layout()
		bSizer119.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.bOkButton.Bind( wx.EVT_BUTTON, self.OnOK )
		self.bCancel.Bind( wx.EVT_BUTTON, self.OnCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnOK( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class TilesetBrowserBase
###########################################################################

class TilesetBrowserBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tileset Browser", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer124 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer138 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer125 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText49 = wx.StaticText( self, wx.ID_ANY, u"Tilesets found in the tiles folder:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )
		bSizer125.Add( self.m_staticText49, 0, wx.ALL, 5 )
		
		self.lsTilesetList = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 600,400 ), wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.LC_SORT_ASCENDING )
		self.lsTilesetList.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer125.Add( self.lsTilesetList, 0, wx.ALL, 5 )
		
		
		bSizer138.Add( bSizer125, 0, wx.EXPAND, 5 )
		
		sbSizer201 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"When importing new tilesets:" ), wx.VERTICAL )
		
		self.rbImportToCurrentPage = wx.RadioButton( self, wx.ID_ANY, u"Import to current page", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.rbImportToCurrentPage.SetValue( True ) 
		sbSizer201.Add( self.rbImportToCurrentPage, 0, wx.TOP|wx.BOTTOM, 3 )
		
		self.rbImportToNewPage = wx.RadioButton( self, wx.ID_ANY, u"Import to separate pages", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rbImportToNewPage.SetValue( True ) 
		sbSizer201.Add( self.rbImportToNewPage, 0, wx.TOP|wx.BOTTOM, 3 )
		
		self.bChangePageAssignments = wx.Button( self, wx.ID_ANY, u"Change Page Assignments...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bChangePageAssignments.SetToolTip( u"Select which pages tilesets appear on (for loaded tilesets only, not queued)" )
		
		sbSizer201.Add( self.bChangePageAssignments, 0, wx.ALL, 5 )
		
		
		bSizer138.Add( sbSizer201, 1, wx.EXPAND, 5 )
		
		
		bSizer124.Add( bSizer138, 1, wx.EXPAND, 5 )
		
		bSizer126 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer137 = wx.BoxSizer( wx.VERTICAL )
		
		self.bAddTileset = wx.Button( self, wx.ID_ANY, u"Add Quantity", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer137.Add( self.bAddTileset, 0, wx.BOTTOM, 2 )
		
		self.bSubtractTileset = wx.Button( self, wx.ID_ANY, u"Subtract Quantity", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer137.Add( self.bSubtractTileset, 0, wx.BOTTOM, 2 )
		
		self.bClearSelection = wx.Button( self, wx.ID_ANY, u"Clear Selection", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer137.Add( self.bClearSelection, 0, wx.BOTTOM, 20 )
		
		self.m_staticText53 = wx.StaticText( self, wx.ID_ANY, u"Tileset status is indicated by the background color:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( 115 )
		bSizer137.Add( self.m_staticText53, 0, wx.TOP, 20 )
		
		self.m_staticText54 = wx.StaticText( self, wx.ID_ANY, u" Tileset Loaded ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )
		self.m_staticText54.SetBackgroundColour( wx.Colour( 0, 174, 0 ) )
		
		bSizer137.Add( self.m_staticText54, 0, wx.ALL, 5 )
		
		self.m_staticText55 = wx.StaticText( self, wx.ID_ANY, u" Queued for loading ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )
		self.m_staticText55.SetBackgroundColour( wx.Colour( 255, 255, 0 ) )
		
		bSizer137.Add( self.m_staticText55, 0, wx.ALL, 5 )
		
		self.m_staticText531 = wx.StaticText( self, wx.ID_ANY, u" Queued to unload ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText531.Wrap( -1 )
		self.m_staticText531.SetBackgroundColour( wx.Colour( 255, 53, 53 ) )
		
		bSizer137.Add( self.m_staticText531, 0, wx.ALL, 5 )
		
		self.m_staticText5311 = wx.StaticText( self, wx.ID_ANY, u" Not loaded ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5311.Wrap( -1 )
		self.m_staticText5311.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer137.Add( self.m_staticText5311, 0, wx.ALL, 5 )
		
		self.m_staticText53111 = wx.StaticText( self, wx.ID_ANY, u"Double-click to change status.  Changing the quantity will change the text color.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53111.Wrap( 115 )
		bSizer137.Add( self.m_staticText53111, 0, wx.TOP, 10 )
		
		
		bSizer126.Add( bSizer137, 1, wx.EXPAND|wx.TOP, 25 )
		
		bSizer136 = wx.BoxSizer( wx.VERTICAL )
		
		self.bClose = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bClose.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.bClose.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.bClose.SetBackgroundColour( wx.Colour( 0, 94, 0 ) )
		
		bSizer136.Add( self.bClose, 0, wx.ALL, 2 )
		
		self.bCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bCancel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.bCancel.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bCancel.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		
		bSizer136.Add( self.bCancel, 0, wx.ALL, 2 )
		
		self.bHelp = wx.Button( self, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bHelp.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.bHelp.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bHelp.SetBackgroundColour( wx.Colour( 0, 0, 160 ) )
		
		bSizer136.Add( self.bHelp, 0, wx.ALL, 2 )
		
		
		bSizer126.Add( bSizer136, 0, wx.EXPAND, 5 )
		
		
		bSizer124.Add( bSizer126, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer124 )
		self.Layout()
		bSizer124.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.lsTilesetList.Bind( wx.EVT_LEFT_DCLICK, self.ChangeTilesetStatus )
		self.lsTilesetList.Bind( wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected )
		self.bChangePageAssignments.Bind( wx.EVT_BUTTON, self.OnChangePageAssignments )
		self.bAddTileset.Bind( wx.EVT_BUTTON, self.OnAddTileset )
		self.bSubtractTileset.Bind( wx.EVT_BUTTON, self.OnSubtractTileset )
		self.bClearSelection.Bind( wx.EVT_BUTTON, self.OnClearSelection )
		self.bClose.Bind( wx.EVT_BUTTON, self.OnClose )
		self.bCancel.Bind( wx.EVT_BUTTON, self.OnCancel )
		self.bHelp.Bind( wx.EVT_BUTTON, self.OnHelp )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def ChangeTilesetStatus( self, event ):
		event.Skip()
	
	def OnItemSelected( self, event ):
		event.Skip()
	
	def OnChangePageAssignments( self, event ):
		event.Skip()
	
	def OnAddTileset( self, event ):
		event.Skip()
	
	def OnSubtractTileset( self, event ):
		event.Skip()
	
	def OnClearSelection( self, event ):
		event.Skip()
	
	def OnClose( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		event.Skip()
	
	def OnHelp( self, event ):
		event.Skip()
	

###########################################################################
## Class TilesetPageManagerDialogBase_UX
###########################################################################

class TilesetPageManagerDialogBase_UX ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tileset Page Manager", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer96 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer297 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer70 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Loaded Tilesets" ), wx.VERTICAL )
		
		lbAvailableTilesetsChoices = []
		self.lbAvailableTilesets = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), lbAvailableTilesetsChoices, wx.LB_SINGLE )
		sbSizer70.Add( self.lbAvailableTilesets, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer297.Add( sbSizer70, 1, wx.EXPAND, 5 )
		
		bSizer304 = wx.BoxSizer( wx.VERTICAL )
		
		self.bAddAllTilesetsToPage = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/AddToPageAll.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bAddAllTilesetsToPage.SetToolTip( u"Click to add all tilesets to this page" )
		
		bSizer304.Add( self.bAddAllTilesetsToPage, 0, wx.BOTTOM, 0 )
		
		self.bAddTilesetToPage = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/AddToPage.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bAddTilesetToPage.SetToolTip( u"Click to add the selected tileset to this page" )
		
		bSizer304.Add( self.bAddTilesetToPage, 0, wx.BOTTOM, 5 )
		
		self.bRemoveTilesetFromPage = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/RemoveFromPage.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bRemoveTilesetFromPage.SetToolTip( u"Click to remove the selected tileset from this page" )
		
		bSizer304.Add( self.bRemoveTilesetFromPage, 0, wx.TOP, 5 )
		
		self.bRemoveAllTilesetsFromPage = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/RemoveFromPageAll.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bRemoveAllTilesetsFromPage.SetToolTip( u"Click to remove all tilesets from this page" )
		
		bSizer304.Add( self.bRemoveAllTilesetsFromPage, 0, wx.ALL, 0 )
		
		
		bSizer297.Add( bSizer304, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sbSizer69 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Available Pages" ), wx.VERTICAL )
		
		cbxPagesChoices = []
		self.cbxPages = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cbxPagesChoices, 0 )
		self.cbxPages.SetSelection( 0 )
		self.cbxPages.SetToolTip( u"Select the page to assign tilesets to." )
		
		sbSizer69.Add( self.cbxPages, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer302 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText280 = wx.StaticText( self, wx.ID_ANY, u"Assigned Tilesets:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText280.Wrap( -1 )
		bSizer302.Add( self.m_staticText280, 0, wx.TOP|wx.LEFT, 5 )
		
		lbTilesetPagesChoices = []
		self.lbTilesetPages = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,170 ), lbTilesetPagesChoices, wx.LB_SINGLE )
		bSizer302.Add( self.lbTilesetPages, 1, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		
		sbSizer69.Add( bSizer302, 1, wx.EXPAND, 5 )
		
		
		bSizer297.Add( sbSizer69, 1, wx.EXPAND, 5 )
		
		
		bSizer96.Add( bSizer297, 1, wx.EXPAND, 5 )
		
		bSizer457 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer101 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bAddTileset = wx.Button( self, wx.ID_ANY, u"Add Tileset Page", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bAddTileset.Enable( False )
		
		bSizer101.Add( self.bAddTileset, 0, wx.ALL, 2 )
		
		self.bRenamePage = wx.Button( self, wx.ID_ANY, u"Rename Page", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bRenamePage.Enable( False )
		
		bSizer101.Add( self.bRenamePage, 0, wx.ALL, 2 )
		
		self.bDeletePage = wx.Button( self, wx.ID_ANY, u"Delete Page", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bDeletePage.Enable( False )
		
		bSizer101.Add( self.bDeletePage, 0, wx.ALL, 2 )
		
		
		bSizer457.Add( bSizer101, 1, wx.ALIGN_LEFT|wx.EXPAND|wx.TOP, 3 )
		
		bSizer98 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ID_OK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_OK.SetDefault() 
		self.ID_OK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_OK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.ID_OK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer98.Add( self.ID_OK, 0, wx.RIGHT, 3 )
		
		self.ID_CANCEL = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_CANCEL.SetDefault() 
		self.ID_CANCEL.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_CANCEL.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ID_CANCEL.SetBackgroundColour( wx.Colour( 128, 0, 64 ) )
		
		bSizer98.Add( self.ID_CANCEL, 0, wx.LEFT|wx.RIGHT, 3 )
		
		self.bHelp = wx.Button( self, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bHelp.SetDefault() 
		self.bHelp.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bHelp.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bHelp.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer98.Add( self.bHelp, 0, wx.LEFT, 3 )
		
		
		bSizer457.Add( bSizer98, 1, wx.ALIGN_RIGHT|wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer96.Add( bSizer457, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer96 )
		self.Layout()
		bSizer96.Fit( self )
		
		# Connect Events
		self.lbAvailableTilesets.Bind( wx.EVT_LISTBOX_DCLICK, self.AddTilesetToPage )
		self.bAddAllTilesetsToPage.Bind( wx.EVT_BUTTON, self.AddAllTilesetsToPage )
		self.bAddTilesetToPage.Bind( wx.EVT_BUTTON, self.AddTilesetToPage )
		self.bRemoveTilesetFromPage.Bind( wx.EVT_BUTTON, self.RemoveTilesetFromPage )
		self.bRemoveAllTilesetsFromPage.Bind( wx.EVT_BUTTON, self.RemoveAllTilesetsFromPage )
		self.cbxPages.Bind( wx.EVT_CHOICE, self.ChangeTilepageUX )
		self.lbTilesetPages.Bind( wx.EVT_LISTBOX_DCLICK, self.RemoveTilesetFromPage )
		self.bAddTileset.Bind( wx.EVT_BUTTON, self.OnAddPage )
		self.bRenamePage.Bind( wx.EVT_BUTTON, self.OnRenamePage )
		self.bDeletePage.Bind( wx.EVT_BUTTON, self.OnDeletePage )
		self.ID_OK.Bind( wx.EVT_BUTTON, self.OnOK )
		self.ID_CANCEL.Bind( wx.EVT_BUTTON, self.OnCancel )
		self.bHelp.Bind( wx.EVT_BUTTON, self.OnHelp )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def AddTilesetToPage( self, event ):
		event.Skip()
	
	def AddAllTilesetsToPage( self, event ):
		event.Skip()
	
	
	def RemoveTilesetFromPage( self, event ):
		event.Skip()
	
	def RemoveAllTilesetsFromPage( self, event ):
		event.Skip()
	
	def ChangeTilepageUX( self, event ):
		event.Skip()
	
	
	def OnAddPage( self, event ):
		event.Skip()
	
	def OnRenamePage( self, event ):
		event.Skip()
	
	def OnDeletePage( self, event ):
		event.Skip()
	
	def OnOK( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		event.Skip()
	
	def OnHelp( self, event ):
		event.Skip()
	

###########################################################################
## Class IsometricMapBase
###########################################################################

class IsometricMapBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Isometric Mapping", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer78 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer92 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.pnDisplayPanel = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,500 ), wx.HSCROLL|wx.SUNKEN_BORDER|wx.VSCROLL )
		self.pnDisplayPanel.SetScrollRate( 5, 5 )
		self.pnDisplayPanel.SetBackgroundColour( wx.Colour( 83, 83, 189 ) )
		
		bSizer92.Add( self.pnDisplayPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer78.Add( bSizer92, 3, wx.EXPAND, 5 )
		
		bSizer93 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer94 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer121 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_listCtrl2 = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.LC_SINGLE_SEL )
		bSizer121.Add( self.m_listCtrl2, 0, wx.ALL, 5 )
		
		
		bSizer94.Add( bSizer121, 1, wx.EXPAND, 5 )
		
		bSizer152 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText65 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText65.Wrap( -1 )
		bSizer152.Add( self.m_staticText65, 0, wx.ALL, 5 )
		
		self.m_slider4 = wx.Slider( self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_VERTICAL )
		bSizer152.Add( self.m_slider4, 0, wx.ALL, 5 )
		
		self.m_staticText66 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText66.Wrap( -1 )
		bSizer152.Add( self.m_staticText66, 0, wx.ALL, 5 )
		
		
		bSizer94.Add( bSizer152, 1, wx.EXPAND, 5 )
		
		bSizer151 = wx.BoxSizer( wx.VERTICAL )
		
		self.bOK = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer151.Add( self.bOK, 0, wx.ALL, 5 )
		
		
		bSizer94.Add( bSizer151, 1, wx.EXPAND, 5 )
		
		
		bSizer93.Add( bSizer94, 0, wx.EXPAND, 5 )
		
		
		bSizer78.Add( bSizer93, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer78 )
		self.Layout()
		bSizer78.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.pnDisplayPanel.Bind( wx.EVT_PAINT, self.OnPaint )
		self.bOK.Bind( wx.EVT_BUTTON, self.OnOK )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnPaint( self, event ):
		event.Skip()
	
	def OnOK( self, event ):
		event.Skip()
	

###########################################################################
## Class SymbolManagerDialogCore
###########################################################################

class SymbolManagerDialogCore ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Symbol and Marker Manager", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer136 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Available Symbols" ), wx.HORIZONTAL )
		
		lbSymbolsChoices = []
		self.lbSymbols = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,150 ), lbSymbolsChoices, wx.LB_SINGLE )
		sbSizer12.Add( self.lbSymbols, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer137 = wx.BoxSizer( wx.VERTICAL )
		
		self.sbSymbolDisplay = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 100,100 ), wx.SUNKEN_BORDER )
		self.sbSymbolDisplay.SetBackgroundColour( wx.Colour( 79, 157, 157 ) )
		
		bSizer137.Add( self.sbSymbolDisplay, 0, wx.ALL|wx.FIXED_MINSIZE, 5 )
		
		self.bAddSymbol = wx.Button( self, wx.ID_ANY, u"Add Symbol...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer137.Add( self.bAddSymbol, 0, wx.ALL|wx.EXPAND, 3 )
		
		self.bDeleteSymbol = wx.Button( self, wx.ID_ANY, u"Delete Symbol", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer137.Add( self.bDeleteSymbol, 0, wx.ALL|wx.EXPAND, 3 )
		
		
		sbSizer12.Add( bSizer137, 0, wx.EXPAND, 5 )
		
		
		bSizer136.Add( sbSizer12, 0, wx.ALL, 5 )
		
		sbSizer121 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Monster and Creature Markers" ), wx.HORIZONTAL )
		
		bSizer143 = wx.BoxSizer( wx.VERTICAL )
		
		lbMarkersChoices = []
		self.lbMarkers = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), lbMarkersChoices, wx.LB_SINGLE )
		bSizer143.Add( self.lbMarkers, 2, wx.ALL|wx.EXPAND, 5 )
		
		rbMarkerShapeChoices = [ u"Circle", u"Square", u"Triangle", u"Diamond", u"InvTriangle", u"Hexagon" ]
		self.rbMarkerShape = wx.RadioBox( self, wx.ID_ANY, u"Marker Shape", wx.DefaultPosition, wx.DefaultSize, rbMarkerShapeChoices, 3, wx.RA_SPECIFY_COLS )
		self.rbMarkerShape.SetSelection( 4 )
		bSizer143.Add( self.rbMarkerShape, 1, wx.ALL, 5 )
		
		
		sbSizer121.Add( bSizer143, 1, wx.EXPAND, 5 )
		
		bSizer1371 = wx.BoxSizer( wx.VERTICAL )
		
		self.sbMarkerDisplay = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 100,100 ), wx.SUNKEN_BORDER )
		self.sbMarkerDisplay.SetBackgroundColour( wx.Colour( 79, 157, 157 ) )
		
		bSizer1371.Add( self.sbMarkerDisplay, 0, wx.ALL|wx.FIXED_MINSIZE, 5 )
		
		bSizer146 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText61 = wx.StaticText( self, wx.ID_ANY, u"Marker Size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )
		bSizer146.Add( self.m_staticText61, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
		
		self.spMarkerSize = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 45,-1 ), wx.SP_ARROW_KEYS, 1, 20, 1 )
		self.spMarkerSize.SetToolTip( u"Set the height and width of the marker" )
		
		bSizer146.Add( self.spMarkerSize, 0, wx.ALL, 5 )
		
		
		bSizer1371.Add( bSizer146, 0, 0, 5 )
		
		bSizer144 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cpOutlineColor = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		bSizer144.Add( self.cpOutlineColor, 0, wx.ALIGN_RIGHT, 5 )
		
		self.m_staticText59 = wx.StaticText( self, wx.ID_ANY, u"Outline Color", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText59.Wrap( -1 )
		bSizer144.Add( self.m_staticText59, 0, wx.ALL, 5 )
		
		
		bSizer1371.Add( bSizer144, 0, wx.ALL|wx.EXPAND, 3 )
		
		bSizer145 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cpFillColor = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 255, 255, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		bSizer145.Add( self.cpFillColor, 0, wx.ALIGN_RIGHT, 5 )
		
		self.m_staticText60 = wx.StaticText( self, wx.ID_ANY, u"Fill Color", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText60.Wrap( -1 )
		bSizer145.Add( self.m_staticText60, 0, wx.ALL, 5 )
		
		
		bSizer1371.Add( bSizer145, 0, wx.ALL|wx.EXPAND, 3 )
		
		bSizer1441 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cpTextColor = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 0, 0, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		bSizer1441.Add( self.cpTextColor, 0, wx.ALIGN_RIGHT, 5 )
		
		self.m_staticText591 = wx.StaticText( self, wx.ID_ANY, u"Text Color", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText591.Wrap( -1 )
		bSizer1441.Add( self.m_staticText591, 0, wx.ALL, 5 )
		
		
		bSizer1371.Add( bSizer1441, 0, wx.ALL|wx.EXPAND, 3 )
		
		self.bAddMarker = wx.Button( self, wx.ID_ANY, u"Add Marker...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1371.Add( self.bAddMarker, 0, wx.ALL, 3 )
		
		self.bDeleteMarker = wx.Button( self, wx.ID_ANY, u"Delete Marker", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1371.Add( self.bDeleteMarker, 0, wx.ALL, 3 )
		
		
		sbSizer121.Add( bSizer1371, 0, 0, 5 )
		
		
		bSizer136.Add( sbSizer121, 0, wx.ALL, 5 )
		
		bSizer98 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bOK = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bOK.SetDefault() 
		self.bOK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bOK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.bOK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer98.Add( self.bOK, 0, wx.RIGHT, 3 )
		
		self.bCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bCancel.SetDefault() 
		self.bCancel.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bCancel.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bCancel.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		self.bCancel.Hide()
		
		bSizer98.Add( self.bCancel, 0, wx.LEFT|wx.RIGHT, 5 )
		
		self.bHelp = wx.Button( self, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bHelp.SetDefault() 
		self.bHelp.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bHelp.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bHelp.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer98.Add( self.bHelp, 0, wx.LEFT, 3 )
		
		
		bSizer136.Add( bSizer98, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		self.SetSizer( bSizer136 )
		self.Layout()
		bSizer136.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.lbSymbols.Bind( wx.EVT_LISTBOX, self.OnSymbolListbox )
		self.bAddSymbol.Bind( wx.EVT_BUTTON, self.OnAddSymbol )
		self.bDeleteSymbol.Bind( wx.EVT_BUTTON, self.OnDeleteSymbol )
		self.lbMarkers.Bind( wx.EVT_LISTBOX, self.OnMarkerListbox )
		self.lbMarkers.Bind( wx.EVT_LISTBOX_DCLICK, self.OnOK )
		self.rbMarkerShape.Bind( wx.EVT_RADIOBOX, self.OnMarkerShape )
		self.spMarkerSize.Bind( wx.EVT_SPINCTRL, self.OnChangeMarkerSize )
		self.cpOutlineColor.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnChangeOutlineColor )
		self.cpFillColor.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnChangeFillColor )
		self.cpTextColor.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnChangeTextColor )
		self.bAddMarker.Bind( wx.EVT_BUTTON, self.OnAddMarker )
		self.bDeleteMarker.Bind( wx.EVT_BUTTON, self.OnDeleteMarker )
		self.bOK.Bind( wx.EVT_BUTTON, self.OnOK )
		self.bCancel.Bind( wx.EVT_BUTTON, self.OnCancel )
		self.bHelp.Bind( wx.EVT_BUTTON, self.OnHelp )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSymbolListbox( self, event ):
		event.Skip()
	
	def OnAddSymbol( self, event ):
		event.Skip()
	
	def OnDeleteSymbol( self, event ):
		event.Skip()
	
	def OnMarkerListbox( self, event ):
		event.Skip()
	
	def OnOK( self, event ):
		event.Skip()
	
	def OnMarkerShape( self, event ):
		event.Skip()
	
	def OnChangeMarkerSize( self, event ):
		event.Skip()
	
	def OnChangeOutlineColor( self, event ):
		event.Skip()
	
	def OnChangeFillColor( self, event ):
		event.Skip()
	
	def OnChangeTextColor( self, event ):
		event.Skip()
	
	def OnAddMarker( self, event ):
		event.Skip()
	
	def OnDeleteMarker( self, event ):
		event.Skip()
	
	
	def OnCancel( self, event ):
		event.Skip()
	
	def OnHelp( self, event ):
		event.Skip()
	

###########################################################################
## Class SecondaryMapDialogBase
###########################################################################

class SecondaryMapDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Player View", pos = wx.DefaultPosition, size = wx.Size( 632,500 ), style = wx.DEFAULT_DIALOG_STYLE|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.FULL_REPAINT_ON_RESIZE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer145 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer146 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bClose = wx.Button( self, wx.ID_ANY, u"Close Window", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bClose.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.bClose.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bClose.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		
		bSizer146.Add( self.bClose, 0, 0, 3 )
		
		self.bUpdateImage = wx.Button( self, wx.ID_ANY, u"Update Image", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bUpdateImage.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.bUpdateImage.SetForegroundColour( wx.Colour( 255, 168, 81 ) )
		self.bUpdateImage.SetBackgroundColour( wx.Colour( 0, 0, 128 ) )
		
		bSizer146.Add( self.bUpdateImage, 0, 0, 3 )
		
		self.bUpdateFTP = wx.Button( self, wx.ID_ANY, u"Update Image to ftp site", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bUpdateFTP.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.bUpdateFTP.SetForegroundColour( wx.Colour( 255, 168, 81 ) )
		self.bUpdateFTP.SetBackgroundColour( wx.Colour( 0, 0, 128 ) )
		
		bSizer146.Add( self.bUpdateFTP, 0, 0, 3 )
		
		self.bZoomIn = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/ZoomIn.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bZoomIn.SetToolTip( u"Zoom In" )
		
		bSizer146.Add( self.bZoomIn, 0, wx.LEFT, 5 )
		
		self.bZoomOut = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/ZoomOut.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bZoomOut.SetToolTip( u"Zoom Out" )
		
		bSizer146.Add( self.bZoomOut, 0, 0, 3 )
		
		self.bViewAll = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/select_all.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bViewAll.SetToolTip( u"Reset Zoom" )
		
		bSizer146.Add( self.bViewAll, 0, 0, 3 )
		
		self.bSaveImage = wx.Button( self, wx.ID_ANY, u"Save Current Image...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bSaveImage.SetToolTip( u"Save Current Image" )
		
		bSizer146.Add( self.bSaveImage, 0, wx.LEFT, 5 )
		
		
		bSizer145.Add( bSizer146, 0, wx.EXPAND, 5 )
		
		self.pnSecondaryMap = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.pnSecondaryMap.SetScrollRate( 5, 5 )
		self.pnSecondaryMap.SetForegroundColour( wx.Colour( 204, 230, 230 ) )
		self.pnSecondaryMap.SetBackgroundColour( wx.Colour( 148, 201, 201 ) )
		
		bSizer145.Add( self.pnSecondaryMap, 1, wx.ALL|wx.EXPAND, 2 )
		
		
		self.SetSizer( bSizer145 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.bClose.Bind( wx.EVT_BUTTON, self.OnClose )
		self.bUpdateImage.Bind( wx.EVT_BUTTON, self.UpdatePlayerView )
		self.bUpdateFTP.Bind( wx.EVT_BUTTON, self.UpdateFTP )
		self.bZoomIn.Bind( wx.EVT_BUTTON, self.OnZoomIn )
		self.bZoomIn.Bind( wx.EVT_UPDATE_UI, self.CheckZoomFactor )
		self.bZoomOut.Bind( wx.EVT_BUTTON, self.OnZoomOut )
		self.bZoomOut.Bind( wx.EVT_UPDATE_UI, self.CheckZoomFactor )
		self.bViewAll.Bind( wx.EVT_BUTTON, self.ResetZoom )
		self.bSaveImage.Bind( wx.EVT_BUTTON, self.OnSaveImage )
		self.pnSecondaryMap.Bind( wx.EVT_PAINT, self.OnPaint )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()
	
	
	def UpdatePlayerView( self, event ):
		event.Skip()
	
	def UpdateFTP( self, event ):
		event.Skip()
	
	def OnZoomIn( self, event ):
		event.Skip()
	
	def CheckZoomFactor( self, event ):
		event.Skip()
	
	def OnZoomOut( self, event ):
		event.Skip()
	
	
	def ResetZoom( self, event ):
		event.Skip()
	
	def OnSaveImage( self, event ):
		event.Skip()
	
	def OnPaint( self, event ):
		event.Skip()
	

###########################################################################
## Class IsometricMapDialogBase
###########################################################################

class IsometricMapDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Isometric Map View", pos = wx.DefaultPosition, size = wx.Size( 632,500 ), style = wx.DEFAULT_DIALOG_STYLE|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.FULL_REPAINT_ON_RESIZE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer145 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer146 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bClose = wx.Button( self, wx.ID_ANY, u"Close Window", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bClose.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.bClose.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bClose.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		
		bSizer146.Add( self.bClose, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 3 )
		
		self.bUpdateImage = wx.Button( self, wx.ID_ANY, u"Update Image", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bUpdateImage.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.bUpdateImage.SetForegroundColour( wx.Colour( 255, 168, 81 ) )
		self.bUpdateImage.SetBackgroundColour( wx.Colour( 0, 0, 128 ) )
		
		bSizer146.Add( self.bUpdateImage, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.bZoomIn = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/ZoomIn.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bZoomIn.SetToolTip( u"Zoom In" )
		
		bSizer146.Add( self.bZoomIn, 0, wx.ALL, 5 )
		
		self.bZoomOut = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/ZoomOut.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bZoomOut.SetToolTip( u"Zoom Out" )
		
		bSizer146.Add( self.bZoomOut, 0, wx.ALL, 5 )
		
		self.bViewAll = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/select_all.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bViewAll.SetToolTip( u"Reset Zoom" )
		
		bSizer146.Add( self.bViewAll, 0, wx.ALL, 5 )
		
		self.bSaveImage = wx.Button( self, wx.ID_ANY, u"Save Current Image...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bSaveImage.SetToolTip( u"Save Current Image" )
		
		bSizer146.Add( self.bSaveImage, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.bRegisterImage = wx.Button( self, wx.ID_ANY, u"Register Image", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer146.Add( self.bRegisterImage, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		
		bSizer145.Add( bSizer146, 0, wx.EXPAND, 5 )
		
		self.pnIsometricMap = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.pnIsometricMap.SetScrollRate( 5, 5 )
		self.pnIsometricMap.SetForegroundColour( wx.Colour( 204, 230, 230 ) )
		self.pnIsometricMap.SetBackgroundColour( wx.Colour( 148, 201, 201 ) )
		
		bSizer145.Add( self.pnIsometricMap, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer145 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.bClose.Bind( wx.EVT_BUTTON, self.OnClose )
		self.bUpdateImage.Bind( wx.EVT_BUTTON, self.UpdateIsometricView )
		self.bZoomIn.Bind( wx.EVT_BUTTON, self.OnZoomIn )
		self.bZoomIn.Bind( wx.EVT_UPDATE_UI, self.CheckZoomFactor )
		self.bZoomOut.Bind( wx.EVT_BUTTON, self.OnZoomOut )
		self.bZoomOut.Bind( wx.EVT_UPDATE_UI, self.CheckZoomFactor )
		self.bViewAll.Bind( wx.EVT_BUTTON, self.ResetZoom )
		self.bSaveImage.Bind( wx.EVT_BUTTON, self.OnSaveImage )
		self.bRegisterImage.Bind( wx.EVT_BUTTON, self.OnRegisterImage )
		self.pnIsometricMap.Bind( wx.EVT_PAINT, self.OnPaint )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()
	
	
	def UpdateIsometricView( self, event ):
		event.Skip()
	
	def OnZoomIn( self, event ):
		event.Skip()
	
	def CheckZoomFactor( self, event ):
		event.Skip()
	
	def OnZoomOut( self, event ):
		event.Skip()
	
	
	def ResetZoom( self, event ):
		event.Skip()
	
	def OnSaveImage( self, event ):
		event.Skip()
	
	def OnRegisterImage( self, event ):
		event.Skip()
	
	def OnPaint( self, event ):
		event.Skip()
	

###########################################################################
## Class NewMapDialogBase
###########################################################################

class NewMapDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Create New Map", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 74, 90, 90, False, "Tahoma" ) )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Number of Rows", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer9.Add( self.m_staticText3, 1, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
		
		self.RowSpinner = wx.SpinCtrl( self, wx.ID_ANY, u"20", wx.DefaultPosition, wx.Size( 70,-1 ), wx.SP_ARROW_KEYS, 1, 300, 20 )
		bSizer9.Add( self.RowSpinner, 0, wx.LEFT|wx.ALIGN_RIGHT, 23 )
		
		
		bSizer8.Add( bSizer9, 1, wx.ALL|wx.EXPAND, 2 )
		
		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Number of Columns", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer10.Add( self.m_staticText4, 1, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
		
		self.ColumnSpinner = wx.SpinCtrl( self, wx.ID_ANY, u"20", wx.DefaultPosition, wx.Size( 70,-1 ), wx.SP_ARROW_KEYS, 1, 300, 20 )
		bSizer10.Add( self.ColumnSpinner, 0, wx.LEFT, 5 )
		
		
		bSizer8.Add( bSizer10, 1, wx.ALL|wx.EXPAND, 2 )
		
		
		bSizer6.Add( bSizer8, 0, wx.EXPAND|wx.TOP, 3 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer6.Add( self.m_staticline1, 0, wx.BOTTOM|wx.EXPAND|wx.EXPAND, 4 )
		
		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer192 = wx.BoxSizer( wx.VERTICAL )
		
		self.UseGridOption = wx.CheckBox( self, wx.ID_ANY, u"Show Grid?", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.UseGridOption.SetValue(True) 
		bSizer192.Add( self.UseGridOption, 1, wx.SHAPED, 9 )
		
		
		bSizer11.Add( bSizer192, 1, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
		
		bSizer191 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText77 = wx.StaticText( self, wx.ID_ANY, u"Grid color:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText77.Wrap( -1 )
		bSizer191.Add( self.m_staticText77, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
		
		self.cpkGridColor = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 128, 128, 128 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		bSizer191.Add( self.cpkGridColor, 0, 0, 5 )
		
		
		bSizer11.Add( bSizer191, 0, wx.ALIGN_RIGHT|wx.SHAPED, 5 )
		
		
		bSizer6.Add( bSizer11, 0, wx.EXPAND, 0 )
		
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ID_OK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_OK.SetDefault() 
		self.ID_OK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_OK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.ID_OK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer12.Add( self.ID_OK, 0, 0, 0 )
		
		self.ID_CANCEL = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_CANCEL.SetDefault() 
		self.ID_CANCEL.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_CANCEL.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ID_CANCEL.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		
		bSizer12.Add( self.ID_CANCEL, 0, 0, 0 )
		
		
		bSizer6.Add( bSizer12, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM|wx.TOP, 5 )
		
		
		self.SetSizer( bSizer6 )
		self.Layout()
		bSizer6.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.CancelButton )
		self.ID_OK.Bind( wx.EVT_BUTTON, self.OKButton )
		self.ID_CANCEL.Bind( wx.EVT_BUTTON, self.CancelButton )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def CancelButton( self, event ):
		event.Skip()
	
	def OKButton( self, event ):
		event.Skip()
	
	

###########################################################################
## Class FilterTagsDialogBase
###########################################################################

class FilterTagsDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Filter Tags", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetToolTip( u"Select Filter Tags for Tiles" )
		
		bSizer38 = wx.BoxSizer( wx.VERTICAL )
		
		ID_OK1 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Dungeon" ), wx.VERTICAL )
		
		self.DGRuneTag = wx.CheckBox( self, wx.ID_ANY, u"Rune Tile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DGRuneTag.SetValue(True) 
		self.DGRuneTag.Enable( False )
		
		sbSizer11.Add( self.DGRuneTag, 0, wx.ALL, 3 )
		
		self.DGDoorTag = wx.CheckBox( self, wx.ID_ANY, u"Door", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DGDoorTag.SetValue(True) 
		self.DGDoorTag.Enable( False )
		
		sbSizer11.Add( self.DGDoorTag, 0, wx.ALL, 3 )
		
		self.DGLadderTag = wx.CheckBox( self, wx.ID_ANY, u"Ladder", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DGLadderTag.SetValue(True) 
		self.DGLadderTag.Enable( False )
		
		sbSizer11.Add( self.DGLadderTag, 0, wx.ALL, 3 )
		
		self.DGLargeRoomTag = wx.CheckBox( self, wx.ID_ANY, u"Large Room", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DGLargeRoomTag.SetValue(True) 
		self.DGLargeRoomTag.Enable( False )
		
		sbSizer11.Add( self.DGLargeRoomTag, 0, wx.ALL, 3 )
		
		self.DGSmallRoomTag = wx.CheckBox( self, wx.ID_ANY, u"Small Room", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DGSmallRoomTag.SetValue(True) 
		self.DGSmallRoomTag.Enable( False )
		
		sbSizer11.Add( self.DGSmallRoomTag, 0, wx.ALL, 3 )
		
		self.DGHallwayTag = wx.CheckBox( self, wx.ID_ANY, u"Hallway", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DGHallwayTag.SetValue(True) 
		self.DGHallwayTag.Enable( False )
		
		sbSizer11.Add( self.DGHallwayTag, 0, wx.ALL, 3 )
		
		self.DGTowerSectionTag = wx.CheckBox( self, wx.ID_ANY, u"Tower Section", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DGTowerSectionTag.SetValue(True) 
		self.DGTowerSectionTag.Enable( False )
		
		sbSizer11.Add( self.DGTowerSectionTag, 0, wx.ALL, 3 )
		
		self.DGParapetWallTag = wx.CheckBox( self, wx.ID_ANY, u"Parapet Wall", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DGParapetWallTag.SetValue(True) 
		self.DGParapetWallTag.Enable( False )
		
		sbSizer11.Add( self.DGParapetWallTag, 0, wx.ALL, 3 )
		
		self.DGTrapTag = wx.CheckBox( self, wx.ID_ANY, u"Trap", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DGTrapTag.SetValue(True) 
		self.DGTrapTag.Enable( False )
		
		sbSizer11.Add( self.DGTrapTag, 0, wx.ALL, 3 )
		
		self.DGStairsTag = wx.CheckBox( self, wx.ID_ANY, u"Stairs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DGStairsTag.SetValue(True) 
		self.DGStairsTag.Enable( False )
		
		sbSizer11.Add( self.DGStairsTag, 0, wx.ALL, 3 )
		
		self.DGDecorationTag = wx.CheckBox( self, wx.ID_ANY, u"Decoration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DGDecorationTag.SetValue(True) 
		self.DGDecorationTag.Enable( False )
		
		sbSizer11.Add( self.DGDecorationTag, 0, wx.ALL, 3 )
		
		self.DGTransitionTag = wx.CheckBox( self, wx.ID_ANY, u"Transition", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DGTransitionTag.SetValue(True) 
		self.DGTransitionTag.Enable( False )
		
		sbSizer11.Add( self.DGTransitionTag, 0, wx.ALL, 3 )
		
		
		ID_OK1.Add( sbSizer11, 0, wx.ALL, 3 )
		
		sbSizer12 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Cave" ), wx.VERTICAL )
		
		self.CVPassageTag = wx.CheckBox( self, wx.ID_ANY, u"Passage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CVPassageTag.SetValue(True) 
		self.CVPassageTag.Enable( False )
		
		sbSizer12.Add( self.CVPassageTag, 0, wx.ALL, 3 )
		
		self.CVEndTag = wx.CheckBox( self, wx.ID_ANY, u"Dead End", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CVEndTag.SetValue(True) 
		self.CVEndTag.Enable( False )
		
		sbSizer12.Add( self.CVEndTag, 0, wx.ALL, 3 )
		
		self.CVLargeCavernTag = wx.CheckBox( self, wx.ID_ANY, u"Large Cavern", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CVLargeCavernTag.SetValue(True) 
		self.CVLargeCavernTag.Enable( False )
		
		sbSizer12.Add( self.CVLargeCavernTag, 0, wx.ALL, 3 )
		
		self.CVPartialCavernTag = wx.CheckBox( self, wx.ID_ANY, u"Partial Cavern", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CVPartialCavernTag.SetValue(True) 
		self.CVPartialCavernTag.Enable( False )
		
		sbSizer12.Add( self.CVPartialCavernTag, 0, wx.ALL, 3 )
		
		self.CVDecorationTag = wx.CheckBox( self, wx.ID_ANY, u"Decoration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CVDecorationTag.SetValue(True) 
		self.CVDecorationTag.Enable( False )
		
		sbSizer12.Add( self.CVDecorationTag, 0, wx.ALL, 3 )
		
		self.CVTransitionTag = wx.CheckBox( self, wx.ID_ANY, u"Transition", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CVTransitionTag.SetValue(True) 
		self.CVTransitionTag.Enable( False )
		
		sbSizer12.Add( self.CVTransitionTag, 0, wx.ALL, 3 )
		
		
		ID_OK1.Add( sbSizer12, 0, wx.ALL, 3 )
		
		sbSizer13 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Wild" ), wx.VERTICAL )
		
		self.WLPondTag = wx.CheckBox( self, wx.ID_ANY, u"Pond", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WLPondTag.SetValue(True) 
		self.WLPondTag.Enable( False )
		
		sbSizer13.Add( self.WLPondTag, 0, wx.ALL, 3 )
		
		self.WLTreesTag = wx.CheckBox( self, wx.ID_ANY, u"Trees", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WLTreesTag.SetValue(True) 
		self.WLTreesTag.Enable( False )
		
		sbSizer13.Add( self.WLTreesTag, 0, wx.ALL, 3 )
		
		self.WLRoadTag = wx.CheckBox( self, wx.ID_ANY, u"Road", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WLRoadTag.SetValue(True) 
		self.WLRoadTag.Enable( False )
		
		sbSizer13.Add( self.WLRoadTag, 0, wx.ALL, 3 )
		
		self.WLStreamTag = wx.CheckBox( self, wx.ID_ANY, u"Stream", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WLStreamTag.SetValue(True) 
		self.WLStreamTag.Enable( False )
		
		sbSizer13.Add( self.WLStreamTag, 0, wx.ALL, 3 )
		
		self.WLPathTag = wx.CheckBox( self, wx.ID_ANY, u"Path", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WLPathTag.SetValue(True) 
		self.WLPathTag.Enable( False )
		
		sbSizer13.Add( self.WLPathTag, 0, wx.ALL, 3 )
		
		self.WLRuinsTag = wx.CheckBox( self, wx.ID_ANY, u"Ruins", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WLRuinsTag.SetValue(True) 
		self.WLRuinsTag.Enable( False )
		
		sbSizer13.Add( self.WLRuinsTag, 0, wx.ALL, 3 )
		
		self.WLDecorationTag = wx.CheckBox( self, wx.ID_ANY, u"Decoration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WLDecorationTag.SetValue(True) 
		self.WLDecorationTag.Enable( False )
		
		sbSizer13.Add( self.WLDecorationTag, 0, wx.ALL, 3 )
		
		self.WLTransitionTag = wx.CheckBox( self, wx.ID_ANY, u"Transition", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WLTransitionTag.SetValue(True) 
		self.WLTransitionTag.Enable( False )
		
		sbSizer13.Add( self.WLTransitionTag, 0, wx.ALL, 3 )
		
		
		ID_OK1.Add( sbSizer13, 0, wx.ALL, 3 )
		
		sbSizer14 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Town" ), wx.VERTICAL )
		
		self.TNTowerTag = wx.CheckBox( self, wx.ID_ANY, u"Tower", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TNTowerTag.SetValue(True) 
		self.TNTowerTag.Enable( False )
		
		sbSizer14.Add( self.TNTowerTag, 0, wx.ALL, 3 )
		
		self.TNTownTag = wx.CheckBox( self, wx.ID_ANY, u"Town", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TNTownTag.SetValue(True) 
		self.TNTownTag.Enable( False )
		
		sbSizer14.Add( self.TNTownTag, 0, wx.ALL, 3 )
		
		self.TNSmallBuildingTag = wx.CheckBox( self, wx.ID_ANY, u"Small Building", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TNSmallBuildingTag.SetValue(True) 
		self.TNSmallBuildingTag.Enable( False )
		
		sbSizer14.Add( self.TNSmallBuildingTag, 0, wx.ALL, 3 )
		
		self.TNLargeBuildingTag = wx.CheckBox( self, wx.ID_ANY, u"Large Building", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TNLargeBuildingTag.SetValue(True) 
		self.TNLargeBuildingTag.Enable( False )
		
		sbSizer14.Add( self.TNLargeBuildingTag, 0, wx.ALL, 3 )
		
		self.TNSewerTag = wx.CheckBox( self, wx.ID_ANY, u"Sewer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TNSewerTag.SetValue(True) 
		self.TNSewerTag.Enable( False )
		
		sbSizer14.Add( self.TNSewerTag, 0, wx.ALL, 3 )
		
		self.TNDecorationTag = wx.CheckBox( self, wx.ID_ANY, u"Decoration", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TNDecorationTag.SetValue(True) 
		self.TNDecorationTag.Enable( False )
		
		sbSizer14.Add( self.TNDecorationTag, 0, wx.ALL, 3 )
		
		self.TNLadderTag = wx.CheckBox( self, wx.ID_ANY, u"Ladder", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TNLadderTag.SetValue(True) 
		self.TNLadderTag.Enable( False )
		
		sbSizer14.Add( self.TNLadderTag, 0, wx.ALL, 3 )
		
		self.TNTransitionTag = wx.CheckBox( self, wx.ID_ANY, u"Transition", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TNTransitionTag.SetValue(True) 
		self.TNTransitionTag.Enable( False )
		
		sbSizer14.Add( self.TNTransitionTag, 0, wx.ALL, 3 )
		
		self.TNShipTag = wx.CheckBox( self, wx.ID_ANY, u"Ship", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TNShipTag.SetValue(True) 
		self.TNShipTag.Enable( False )
		
		sbSizer14.Add( self.TNShipTag, 0, wx.ALL, 3 )
		
		
		ID_OK1.Add( sbSizer14, 0, wx.ALL, 3 )
		
		
		bSizer38.Add( ID_OK1, 0, 0, 0 )
		
		ID_OK2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bOK.SetDefault() 
		self.bOK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bOK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.bOK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		ID_OK2.Add( self.bOK, 0, 0, 0 )
		
		self.bCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bCancel.SetDefault() 
		self.bCancel.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bCancel.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bCancel.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		
		ID_OK2.Add( self.bCancel, 0, 0, 0 )
		
		self.bSelectAllFilters = wx.Button( self, wx.ID_ANY, u"Select All Tags", wx.DefaultPosition, wx.DefaultSize, 0|wx.SUNKEN_BORDER )
		self.bSelectAllFilters.SetDefault() 
		self.bSelectAllFilters.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bSelectAllFilters.SetForegroundColour( wx.Colour( 0, 0, 128 ) )
		self.bSelectAllFilters.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		self.bSelectAllFilters.Enable( False )
		
		ID_OK2.Add( self.bSelectAllFilters, 0, wx.LEFT, 10 )
		
		self.bSelectNone = wx.Button( self, wx.ID_ANY, u"Select No Tags", wx.DefaultPosition, wx.DefaultSize, 0|wx.SUNKEN_BORDER )
		self.bSelectNone.SetDefault() 
		self.bSelectNone.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bSelectNone.SetForegroundColour( wx.Colour( 0, 0, 128 ) )
		self.bSelectNone.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		self.bSelectNone.Enable( False )
		
		ID_OK2.Add( self.bSelectNone, 0, 0, 0 )
		
		self.bInvertSelection = wx.Button( self, wx.ID_ANY, u"Invert Selection", wx.DefaultPosition, wx.DefaultSize, 0|wx.SUNKEN_BORDER )
		self.bInvertSelection.SetDefault() 
		self.bInvertSelection.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bInvertSelection.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bInvertSelection.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		self.bInvertSelection.Enable( False )
		
		ID_OK2.Add( self.bInvertSelection, 0, 0, 0 )
		
		
		bSizer38.Add( ID_OK2, 0, wx.ALL|wx.ALIGN_CENTRE, 3 )
		
		
		self.SetSizer( bSizer38 )
		self.Layout()
		bSizer38.Fit( self )
		
		# Connect Events
		self.bOK.Bind( wx.EVT_BUTTON, self.OnOK )
		self.bCancel.Bind( wx.EVT_BUTTON, self.OnCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnOK( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class TilePropertiesDialogBase
###########################################################################

class TilePropertiesDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tile Information", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		self.ImagePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 250,250 ), wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		self.ImagePanel.SetBackgroundColour( wx.Colour( 128, 128, 128 ) )
		
		bSizer41.Add( self.ImagePanel, 0, 0, 0 )
		
		ID_OK1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer43 = wx.BoxSizer( wx.VERTICAL )
		
		self.stTileName = wx.StaticText( self, wx.ID_ANY, u"Tile Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stTileName.Wrap( -1 )
		bSizer43.Add( self.stTileName, 0, wx.ALL, 2 )
		
		self.stSetID = wx.StaticText( self, wx.ID_ANY, u"Set ID:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stSetID.Wrap( -1 )
		bSizer43.Add( self.stSetID, 0, wx.ALL, 2 )
		
		self.stSetName = wx.StaticText( self, wx.ID_ANY, u"Set Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stSetName.Wrap( -1 )
		bSizer43.Add( self.stSetName, 0, wx.ALL, 2 )
		
		self.stGridSize = wx.StaticText( self, wx.ID_ANY, u"Grid Size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stGridSize.Wrap( -1 )
		bSizer43.Add( self.stGridSize, 0, wx.ALL, 2 )
		
		self.stFilenameA = wx.StaticText( self, wx.ID_ANY, u" FilenameA name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stFilenameA.Wrap( 1 )
		bSizer43.Add( self.stFilenameA, 0, wx.ALL, 2 )
		
		self.stFilenameB = wx.StaticText( self, wx.ID_ANY, u"FilenameB name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stFilenameB.Wrap( 1 )
		bSizer43.Add( self.stFilenameB, 0, wx.ALL, 2 )
		
		
		ID_OK1.Add( bSizer43, 0, wx.EXPAND|wx.LEFT|wx.TOP, 3 )
		
		ID_OK2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bShowFlipSide = wx.Button( self, wx.ID_ANY, u" Show Opposite Side ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bShowFlipSide.SetDefault() 
		self.bShowFlipSide.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bShowFlipSide.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bShowFlipSide.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		
		ID_OK2.Add( self.bShowFlipSide, 1, wx.SHAPED, 0 )
		
		self.ID_OK = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_OK.SetDefault() 
		self.ID_OK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_OK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.ID_OK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		self.ID_OK.SetToolTip( u"Click to dismiss info" )
		
		ID_OK2.Add( self.ID_OK, 0, wx.ALIGN_RIGHT, 0 )
		
		
		ID_OK1.Add( ID_OK2, 0, wx.ALL|wx.EXPAND, 3 )
		
		
		bSizer41.Add( ID_OK1, 0, wx.EXPAND|wx.EXPAND, 0 )
		
		
		self.SetSizer( bSizer41 )
		self.Layout()
		bSizer41.Fit( self )
		
		# Connect Events
		self.bShowFlipSide.Bind( wx.EVT_BUTTON, self.ShowFlipSide )
		self.ID_OK.Bind( wx.EVT_BUTTON, self.OnOK )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def ShowFlipSide( self, event ):
		event.Skip()
	
	def OnOK( self, event ):
		event.Skip()
	

###########################################################################
## Class HoverDialogBase
###########################################################################

class HoverDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"View Tile", pos = wx.DefaultPosition, size = wx.Size( 200,200 ), style = 0|wx.NO_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer45 = wx.BoxSizer( wx.VERTICAL )
		
		self.HoverPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER|wx.TAB_TRAVERSAL )
		bSizer45.Add( self.HoverPanel, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer45 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class ChangeMapSizeDialogBase
###########################################################################

class ChangeMapSizeDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Change Map Size", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer46 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer47 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer608 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText308 = wx.StaticText( self, wx.ID_ANY, u"Change Map Size to:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText308.Wrap( -1 )
		bSizer608.Add( self.m_staticText308, 0, wx.ALL, 5 )
		
		bSizer606 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Columns:", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText24.Wrap( -1 )
		bSizer606.Add( self.m_staticText24, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
		
		self.spColumns = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.SP_ARROW_KEYS, 1, 300, 1 )
		bSizer606.Add( self.spColumns, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		
		bSizer608.Add( bSizer606, 0, wx.ALIGN_RIGHT, 5 )
		
		bSizer607 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"Rows:  ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		bSizer607.Add( self.m_staticText25, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
		
		self.spRows = wx.SpinCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 70,-1 ), wx.SP_ARROW_KEYS, 1, 300, 1 )
		bSizer607.Add( self.spRows, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		
		bSizer608.Add( bSizer607, 0, wx.ALIGN_RIGHT, 5 )
		
		
		bSizer47.Add( bSizer608, 0, wx.EXPAND, 5 )
		
		self.m_staticText307 = wx.StaticText( self, wx.ID_ANY, u"Direction to add rows/columns:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText307.Wrap( -1 )
		bSizer47.Add( self.m_staticText307, 0, wx.ALL, 5 )
		
		fgSizer1 = wx.FlexGridSizer( 3, 3, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.bbTopLeft = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/arrow_up_left.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bbTopLeft.SetBitmapHover( wx.Bitmap( u"artwork/grid.png", wx.BITMAP_TYPE_ANY ) )
		fgSizer1.Add( self.bbTopLeft, 0, wx.ALL, 1 )
		
		self.bbTopCenter = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/arrow_up.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bbTopCenter.SetBitmapHover( wx.Bitmap( u"artwork/grid.png", wx.BITMAP_TYPE_ANY ) )
		fgSizer1.Add( self.bbTopCenter, 0, wx.ALL, 1 )
		
		self.bbTopRight = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/arrow_up_right.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bbTopRight.SetBitmapHover( wx.Bitmap( u"artwork/grid.png", wx.BITMAP_TYPE_ANY ) )
		fgSizer1.Add( self.bbTopRight, 0, wx.ALL, 1 )
		
		self.bbCenterLeft = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/arrow_left.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bbCenterLeft.SetBitmapHover( wx.Bitmap( u"artwork/grid.png", wx.BITMAP_TYPE_ANY ) )
		fgSizer1.Add( self.bbCenterLeft, 0, wx.ALL, 1 )
		
		self.bbCenter = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/grid.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bbCenter.SetBitmapHover( wx.Bitmap( u"artwork/grid.png", wx.BITMAP_TYPE_ANY ) )
		fgSizer1.Add( self.bbCenter, 0, wx.ALL, 1 )
		
		self.bbCenterRight = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/arrow_right.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bbCenterRight.SetBitmapHover( wx.Bitmap( u"artwork/grid.png", wx.BITMAP_TYPE_ANY ) )
		fgSizer1.Add( self.bbCenterRight, 0, wx.ALL, 1 )
		
		self.bbBottomLeft = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/arrow_down_left.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bbBottomLeft.SetBitmapHover( wx.Bitmap( u"artwork/grid.png", wx.BITMAP_TYPE_ANY ) )
		fgSizer1.Add( self.bbBottomLeft, 0, wx.ALL, 1 )
		
		self.bbBottomCenter = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/arrow_down.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bbBottomCenter.SetBitmapHover( wx.Bitmap( u"artwork/grid.png", wx.BITMAP_TYPE_ANY ) )
		fgSizer1.Add( self.bbBottomCenter, 0, wx.ALL, 1 )
		
		self.bbBottomRight = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/arrow_down_right.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		
		self.bbBottomRight.SetBitmapHover( wx.Bitmap( u"artwork/grid.png", wx.BITMAP_TYPE_ANY ) )
		fgSizer1.Add( self.bbBottomRight, 0, wx.ALL, 1 )
		
		
		bSizer47.Add( fgSizer1, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer46.Add( bSizer47, 0, wx.EXPAND, 10 )
		
		bSizer50 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ID_OK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_OK.SetDefault() 
		self.ID_OK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_OK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.ID_OK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer50.Add( self.ID_OK, 0, 0, 0 )
		
		self.ID_CANCEL = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_CANCEL.SetDefault() 
		self.ID_CANCEL.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_CANCEL.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ID_CANCEL.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		
		bSizer50.Add( self.ID_CANCEL, 0, 0, 0 )
		
		
		bSizer46.Add( bSizer50, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 4 )
		
		
		self.SetSizer( bSizer46 )
		self.Layout()
		bSizer46.Fit( self )
		
		# Connect Events
		self.bbTopLeft.Bind( wx.EVT_BUTTON, self.OnTopLeft )
		self.bbTopCenter.Bind( wx.EVT_BUTTON, self.OnTopCenter )
		self.bbTopRight.Bind( wx.EVT_BUTTON, self.OnTopRight )
		self.bbCenterLeft.Bind( wx.EVT_BUTTON, self.OnCenterLeft )
		self.bbCenter.Bind( wx.EVT_BUTTON, self.OnCenter )
		self.bbCenterRight.Bind( wx.EVT_BUTTON, self.OnCenterRight )
		self.bbBottomLeft.Bind( wx.EVT_BUTTON, self.OnBottomLeft )
		self.bbBottomCenter.Bind( wx.EVT_BUTTON, self.OnBottomCenter )
		self.bbBottomRight.Bind( wx.EVT_BUTTON, self.OnBottomRight )
		self.ID_OK.Bind( wx.EVT_BUTTON, self.OnOK )
		self.ID_CANCEL.Bind( wx.EVT_BUTTON, self.OnCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnTopLeft( self, event ):
		event.Skip()
	
	def OnTopCenter( self, event ):
		event.Skip()
	
	def OnTopRight( self, event ):
		event.Skip()
	
	def OnCenterLeft( self, event ):
		event.Skip()
	
	def OnCenter( self, event ):
		event.Skip()
	
	def OnCenterRight( self, event ):
		event.Skip()
	
	def OnBottomLeft( self, event ):
		event.Skip()
	
	def OnBottomCenter( self, event ):
		event.Skip()
	
	def OnBottomRight( self, event ):
		event.Skip()
	
	def OnOK( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class TextOptionsDialogBase
###########################################################################

class TextOptionsDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Text Options", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer51 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer52 = wx.BoxSizer( wx.VERTICAL )
		
		self.TextBoxBitmap = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 300,100 ), 0 )
		self.TextBoxBitmap.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer52.Add( self.TextBoxBitmap, 0, wx.ALIGN_CENTRE_HORIZONTAL, 0 )
		
		
		bSizer51.Add( bSizer52, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		bSizer53 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer54 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer15 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Text Background" ), wx.VERTICAL )
		
		self.rbTransparentBackground = wx.RadioButton( self, wx.ID_ANY, u"Transparent", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.rbTransparentBackground.SetValue( True ) 
		sbSizer15.Add( self.rbTransparentBackground, 0, wx.ALL, 4 )
		
		bSizer55 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.rbOpaque = wx.RadioButton( self, wx.ID_ANY, u"Opaque", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rbOpaque.SetValue( True ) 
		bSizer55.Add( self.rbOpaque, 0, wx.RIGHT|wx.ALIGN_CENTRE_VERTICAL, 4 )
		
		self.cpkBackgroundColor = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 0, 0, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		self.cpkBackgroundColor.SetToolTip( u"Click to change the background color" )
		
		bSizer55.Add( self.cpkBackgroundColor, 0, 0, 5 )
		
		
		sbSizer15.Add( bSizer55, 0, wx.ALL, 4 )
		
		
		bSizer54.Add( sbSizer15, 0, 0, 0 )
		
		bChangeFont1 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer364 = wx.BoxSizer( wx.VERTICAL )
		
		self.bChangeFont = wx.Button( self, wx.ID_ANY, u"Change Font...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bChangeFont.SetDefault() 
		self.bChangeFont.SetToolTip( u"Change font, size, and color of text" )
		
		bSizer364.Add( self.bChangeFont, 0, wx.ALL|wx.ALIGN_CENTRE_VERTICAL, 5 )
		
		bSizer365 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText163 = wx.StaticText( self, wx.ID_ANY, u"Text Color:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText163.Wrap( -1 )
		bSizer365.Add( self.m_staticText163, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.cpkTextColor = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		self.cpkTextColor.SetToolTip( u"Click to change the text color." )
		
		bSizer365.Add( self.cpkTextColor, 0, 0, 5 )
		
		
		bSizer364.Add( bSizer365, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bChangeFont1.Add( bSizer364, 1, wx.EXPAND, 5 )
		
		sbSizer16 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Outline Text" ), wx.VERTICAL )
		
		self.rbOutlineOn = wx.RadioButton( self, wx.ID_ANY, u"On", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.rbOutlineOn.SetValue( True ) 
		sbSizer16.Add( self.rbOutlineOn, 0, wx.RIGHT, 30 )
		
		self.rbOutlineOff = wx.RadioButton( self, wx.ID_ANY, u"Off", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rbOutlineOff.SetValue( True ) 
		sbSizer16.Add( self.rbOutlineOff, 0, wx.TOP|wx.BOTTOM, 4 )
		
		
		bChangeFont1.Add( sbSizer16, 0, wx.EXPAND|wx.EXPAND, 0 )
		
		
		bSizer54.Add( bChangeFont1, 0, wx.EXPAND|wx.EXPAND, 0 )
		
		
		bSizer53.Add( bSizer54, 0, wx.EXPAND, 0 )
		
		bApplyGlobal1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer244 = wx.BoxSizer( wx.VERTICAL )
		
		self.bApplyGlobal = wx.CheckBox( self, wx.ID_ANY, u"Apply changes to all annotations?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bApplyGlobal.SetValue(True) 
		bSizer244.Add( self.bApplyGlobal, 1, wx.TOP|wx.BOTTOM, 15 )
		
		
		bApplyGlobal1.Add( bSizer244, 0, wx.ALIGN_CENTER, 5 )
		
		bSizer243 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ID_OK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_OK.SetDefault() 
		self.ID_OK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_OK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.ID_OK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer243.Add( self.ID_OK, 0, wx.ALL|wx.ALIGN_CENTRE_HORIZONTAL, 2 )
		
		self.ID_CANCEL = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_CANCEL.SetDefault() 
		self.ID_CANCEL.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_CANCEL.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ID_CANCEL.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		
		bSizer243.Add( self.ID_CANCEL, 0, wx.ALL|wx.ALIGN_CENTRE_HORIZONTAL, 2 )
		
		
		bApplyGlobal1.Add( bSizer243, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer53.Add( bApplyGlobal1, 0, wx.EXPAND, 5 )
		
		
		bSizer51.Add( bSizer53, 1, 0, 0 )
		
		
		self.SetSizer( bSizer51 )
		self.Layout()
		bSizer51.Fit( self )
		
		# Connect Events
		self.rbTransparentBackground.Bind( wx.EVT_RADIOBUTTON, self.OnRB_TransparentBackground )
		self.rbOpaque.Bind( wx.EVT_RADIOBUTTON, self.OnRB_Opaque )
		self.cpkBackgroundColor.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnChangeBackgroundColor )
		self.bChangeFont.Bind( wx.EVT_BUTTON, self.OnChangeFont )
		self.cpkTextColor.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnChangeTextColor )
		self.rbOutlineOn.Bind( wx.EVT_RADIOBUTTON, self.OnRB_OutlineOn )
		self.rbOutlineOff.Bind( wx.EVT_RADIOBUTTON, self.OnRB_OutlineOff )
		self.ID_OK.Bind( wx.EVT_BUTTON, self.OnOK )
		self.ID_CANCEL.Bind( wx.EVT_BUTTON, self.OnCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnRB_TransparentBackground( self, event ):
		event.Skip()
	
	def OnRB_Opaque( self, event ):
		event.Skip()
	
	def OnChangeBackgroundColor( self, event ):
		event.Skip()
	
	def OnChangeFont( self, event ):
		event.Skip()
	
	def OnChangeTextColor( self, event ):
		event.Skip()
	
	def OnRB_OutlineOn( self, event ):
		event.Skip()
	
	def OnRB_OutlineOff( self, event ):
		event.Skip()
	
	def OnOK( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class PrintResolutionDialogBase
###########################################################################

class PrintResolutionDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Change Resolution", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer58 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer59 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Print Resolution", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		bSizer59.Add( self.m_staticText26, 1, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.spResolution = wx.SpinCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 1, 200, 1 )
		bSizer59.Add( self.spResolution, 0, wx.ALIGN_RIGHT, 0 )
		
		
		bSizer58.Add( bSizer59, 0, wx.ALL|wx.EXPAND, 3 )
		
		bSizer60 = wx.BoxSizer( wx.VERTICAL )
		
		self.cbSaveToINI = wx.CheckBox( self, wx.ID_ANY, u"Save setting to .ini file?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbSaveToINI.SetValue(True) 
		bSizer60.Add( self.cbSaveToINI, 0, 0, 0 )
		
		
		bSizer58.Add( bSizer60, 0, wx.ALL|wx.ALIGN_CENTRE_HORIZONTAL, 3 )
		
		bApplyGlobal = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ID_OK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_OK.SetDefault() 
		self.ID_OK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_OK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.ID_OK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bApplyGlobal.Add( self.ID_OK, 0, wx.ALL|wx.ALIGN_CENTRE_HORIZONTAL, 2 )
		
		self.ID_CANCEL = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_CANCEL.SetDefault() 
		self.ID_CANCEL.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_CANCEL.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ID_CANCEL.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		
		bApplyGlobal.Add( self.ID_CANCEL, 0, wx.ALL|wx.ALIGN_CENTRE_HORIZONTAL, 2 )
		
		
		bSizer58.Add( bApplyGlobal, 1, wx.ALIGN_BOTTOM|wx.ALL|wx.SHAPED, 3 )
		
		
		self.SetSizer( bSizer58 )
		self.Layout()
		bSizer58.Fit( self )
		
		# Connect Events
		self.ID_OK.Bind( wx.EVT_BUTTON, self.OnOK )
		self.ID_CANCEL.Bind( wx.EVT_BUTTON, self.OnCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnOK( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class LayerDisplayDialogBase
###########################################################################

class LayerDisplayDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Layers Display", pos = wx.DefaultPosition, size = wx.Size( 296,529 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		
		bSizer104 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer105 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer641 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText329 = wx.StaticText( self, wx.ID_ANY, u"Active Layer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText329.Wrap( -1 )
		bSizer641.Add( self.m_staticText329, 0, wx.ALL, 5 )
		
		self.lcActiveLayer = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		bSizer641.Add( self.lcActiveLayer, 1, wx.EXPAND|wx.BOTTOM, 5 )
		
		self.m_staticText330 = wx.StaticText( self, wx.ID_ANY, u"Layer Display", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText330.Wrap( -1 )
		bSizer641.Add( self.m_staticText330, 0, wx.ALL, 5 )
		
		self.lcLayerDisplay = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_REPORT )
		bSizer641.Add( self.lcLayerDisplay, 1, wx.EXPAND, 5 )
		
		
		bSizer105.Add( bSizer641, 1, wx.EXPAND, 5 )
		
		bSizer640 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer642 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText331 = wx.StaticText( self, wx.ID_ANY, u"Layer Opacity", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText331.Wrap( -1 )
		bSizer642.Add( self.m_staticText331, 0, wx.ALIGN_CENTER_HORIZONTAL, 2 )
		
		self.slOpacity = wx.Slider( self, wx.ID_ANY, 100, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS )
		self.slOpacity.SetBackgroundColour( wx.Colour( 192, 192, 192 ) )
		self.slOpacity.SetToolTip( u"Change layer opacity.  0=Transparent, 100=Opaque" )
		
		bSizer642.Add( self.slOpacity, 0, wx.EXPAND, 5 )
		
		
		bSizer640.Add( bSizer642, 0, wx.EXPAND|wx.TOP, 2 )
		
		bSizer643 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer644 = wx.BoxSizer( wx.VERTICAL )
		
		self.bAddLayer = wx.Button( self, wx.ID_ANY, u"Add Layer...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bAddLayer.SetDefault() 
		self.bAddLayer.SetToolTip( u"Click to add another layer to the map" )
		
		bSizer644.Add( self.bAddLayer, 0, wx.EXPAND, 0 )
		
		self.bRenameLayer = wx.Button( self, wx.ID_ANY, u"Rename Layer...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bRenameLayer.SetDefault() 
		self.bRenameLayer.SetToolTip( u"Click to rename active layer..." )
		
		bSizer644.Add( self.bRenameLayer, 0, wx.EXPAND, 0 )
		
		self.bDeleteLayer = wx.Button( self, wx.ID_ANY, u"Delete Layer...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bDeleteLayer.SetDefault() 
		self.bDeleteLayer.SetToolTip( u"Click to delete layer.  Base layer cannot be deleted." )
		
		bSizer644.Add( self.bDeleteLayer, 0, wx.BOTTOM|wx.EXPAND, 3 )
		
		
		bSizer643.Add( bSizer644, 1, wx.EXPAND, 5 )
		
		bSizer645 = wx.BoxSizer( wx.VERTICAL )
		
		self.bLayerUp = wx.Button( self, wx.ID_ANY, u"Move Layer Up", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer645.Add( self.bLayerUp, 0, wx.EXPAND, 5 )
		
		self.bLayerDown = wx.Button( self, wx.ID_ANY, u"Move Layer Down", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer645.Add( self.bLayerDown, 0, wx.EXPAND, 5 )
		
		
		bSizer643.Add( bSizer645, 1, wx.EXPAND, 5 )
		
		
		bSizer640.Add( bSizer643, 1, wx.EXPAND, 5 )
		
		
		bSizer105.Add( bSizer640, 0, wx.EXPAND, 5 )
		
		
		bSizer104.Add( bSizer105, 1, wx.ALL|wx.EXPAND, 2 )
		
		ID_OK1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ID_OK = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_OK.SetDefault() 
		self.ID_OK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_OK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.ID_OK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		ID_OK1.Add( self.ID_OK, 0, 0, 2 )
		
		self.bHelp = wx.Button( self, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bHelp.SetDefault() 
		self.bHelp.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.bHelp.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bHelp.SetBackgroundColour( wx.Colour( 0, 0, 160 ) )
		
		ID_OK1.Add( self.bHelp, 0, 0, 2 )
		
		
		bSizer104.Add( ID_OK1, 0, wx.ALIGN_CENTER_HORIZONTAL, 3 )
		
		
		self.SetSizer( bSizer104 )
		self.Layout()
		
		# Connect Events
		self.lcActiveLayer.Bind( wx.EVT_LIST_ITEM_SELECTED, self.SelectActiveLayer )
		self.lcLayerDisplay.Bind( wx.EVT_LIST_ITEM_DESELECTED, self.ChangeLayerDisplay )
		self.lcLayerDisplay.Bind( wx.EVT_LIST_ITEM_SELECTED, self.ChangeLayerDisplay )
		self.slOpacity.Bind( wx.EVT_SCROLL_CHANGED, self.ChangeLayerOpacity )
		self.bAddLayer.Bind( wx.EVT_BUTTON, self.AddLayer )
		self.bRenameLayer.Bind( wx.EVT_BUTTON, self.RenameLayer )
		self.bDeleteLayer.Bind( wx.EVT_BUTTON, self.DeleteLayer )
		self.bLayerUp.Bind( wx.EVT_BUTTON, self.OnLayerUp )
		self.bLayerDown.Bind( wx.EVT_BUTTON, self.OnLayerDown )
		self.ID_OK.Bind( wx.EVT_BUTTON, self.OnExit )
		self.bHelp.Bind( wx.EVT_BUTTON, self.OnHelpButton )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def SelectActiveLayer( self, event ):
		event.Skip()
	
	def ChangeLayerDisplay( self, event ):
		event.Skip()
	
	
	def ChangeLayerOpacity( self, event ):
		event.Skip()
	
	def AddLayer( self, event ):
		event.Skip()
	
	def RenameLayer( self, event ):
		event.Skip()
	
	def DeleteLayer( self, event ):
		event.Skip()
	
	def OnLayerUp( self, event ):
		event.Skip()
	
	def OnLayerDown( self, event ):
		event.Skip()
	
	def OnExit( self, event ):
		event.Skip()
	
	def OnHelpButton( self, event ):
		event.Skip()
	

###########################################################################
## Class HelpDialogBase
###########################################################################

class HelpDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Help", pos = wx.DefaultPosition, size = wx.Size( 451,251 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer107 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer108 = wx.BoxSizer( wx.VERTICAL )
		
		self.txTextArea = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,200 ), wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_LINEWRAP )
		self.txTextArea.SetMaxLength( 0 ) 
		bSizer108.Add( self.txTextArea, 1, wx.EXPAND, 0 )
		
		
		bSizer107.Add( bSizer108, 1, wx.EXPAND, 0 )
		
		bSizer109 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bClose = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bClose.SetDefault() 
		self.bClose.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bClose.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.bClose.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer109.Add( self.bClose, 0, wx.ALIGN_CENTRE_HORIZONTAL, 0 )
		
		
		bSizer107.Add( bSizer109, 0, wx.ALIGN_CENTER_HORIZONTAL, 0 )
		
		
		self.SetSizer( bSizer107 )
		self.Layout()
		
		# Connect Events
		self.bClose.Bind( wx.EVT_BUTTON, self.OnClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()
	

###########################################################################
## Class DungeonEncountersDialogBase
###########################################################################

class DungeonEncountersDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"5E Module and Adventure Designer", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer110 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer111 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer112 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText67 = wx.StaticText( self, wx.ID_ANY, u"Adventure Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText67.Wrap( 0 )
		bSizer112.Add( self.m_staticText67, 0, wx.RIGHT|wx.ALIGN_CENTRE_VERTICAL, 3 )
		
		self.txAdventureTitle = wx.TextCtrl( self, wx.ID_ANY, u"Enter the name or title of the module/adventure series here", wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		self.txAdventureTitle.SetMaxLength( 0 ) 
		bSizer112.Add( self.txAdventureTitle, 0, 0, 0 )
		
		
		bSizer111.Add( bSizer112, 5, 0, 0 )
		
		
		bSizer110.Add( bSizer111, 0, wx.ALL, 3 )
		
		tbDescriptionToggle = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Description icons currently placed on the map:" ), wx.VERTICAL )
		
		lbDescriptionsOnMapChoices = []
		self.lbDescriptionsOnMap = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,100 ), lbDescriptionsOnMapChoices, 0 )
		tbDescriptionToggle.Add( self.lbDescriptionsOnMap, 1, wx.EXPAND|wx.EXPAND, 0 )
		
		bSizer113 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bPrintMasterList = wx.Button( self, wx.ID_ANY, u"Print Master List...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bPrintMasterList.SetDefault() 
		self.bPrintMasterList.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bPrintMasterList.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bPrintMasterList.SetBackgroundColour( wx.Colour( 0, 0, 223 ) )
		
		bSizer113.Add( self.bPrintMasterList, 0, 0, 0 )
		
		self.bDeletePlacedDescription = wx.Button( self, wx.ID_ANY, u"Delete Description", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bDeletePlacedDescription.SetDefault() 
		self.bDeletePlacedDescription.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bDeletePlacedDescription.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bDeletePlacedDescription.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		
		bSizer113.Add( self.bDeletePlacedDescription, 0, wx.LEFT, 5 )
		
		
		tbDescriptionToggle.Add( bSizer113, 0, 0, 0 )
		
		
		bSizer110.Add( tbDescriptionToggle, 0, wx.ALL|wx.EXPAND|wx.EXPAND, 3 )
		
		bSizer114 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer34 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Add Monster" ), wx.HORIZONTAL )
		
		bSizer115 = wx.BoxSizer( wx.VERTICAL )
		
		self.bAddMonster = wx.Button( self, wx.ID_ANY, u"Monsters Dialog...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bAddMonster.SetDefault() 
		bSizer115.Add( self.bAddMonster, 0, wx.EXPAND, 0 )
		
		self.bMonsterFromFile = wx.Button( self, wx.ID_ANY, u"Add From File...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bMonsterFromFile.SetDefault() 
		bSizer115.Add( self.bMonsterFromFile, 0, wx.EXPAND|wx.EXPAND, 0 )
		
		
		sbSizer34.Add( bSizer115, 1, 0, 0 )
		
		
		bSizer114.Add( sbSizer34, 0, wx.RIGHT, 3 )
		
		sbSizer35 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Traps" ), wx.HORIZONTAL )
		
		bSizer116 = wx.BoxSizer( wx.VERTICAL )
		
		self.bAddTrap = wx.Button( self, wx.ID_ANY, u"Traps Dialog...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bAddTrap.SetDefault() 
		bSizer116.Add( self.bAddTrap, 0, wx.EXPAND, 0 )
		
		self.bTrapFromFile = wx.Button( self, wx.ID_ANY, u"Add From File...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bTrapFromFile.SetDefault() 
		bSizer116.Add( self.bTrapFromFile, 0, wx.EXPAND, 0 )
		
		
		sbSizer35.Add( bSizer116, 1, 0, 0 )
		
		
		bSizer114.Add( sbSizer35, 0, wx.LEFT|wx.RIGHT, 3 )
		
		sbSizer36 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Treasure" ), wx.HORIZONTAL )
		
		bSizer117 = wx.BoxSizer( wx.VERTICAL )
		
		self.bAddTreasure = wx.Button( self, wx.ID_ANY, u"Treasures Dialog...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bAddTreasure.SetDefault() 
		bSizer117.Add( self.bAddTreasure, 0, wx.EXPAND, 0 )
		
		self.bTreasureFromFile = wx.Button( self, wx.ID_ANY, u"Add From File...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bTreasureFromFile.SetDefault() 
		bSizer117.Add( self.bTreasureFromFile, 0, wx.EXPAND, 0 )
		
		
		sbSizer36.Add( bSizer117, 1, 0, 0 )
		
		
		bSizer114.Add( sbSizer36, 0, wx.LEFT|wx.RIGHT, 3 )
		
		sbSizer37 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"NPC" ), wx.HORIZONTAL )
		
		bSizer118 = wx.BoxSizer( wx.VERTICAL )
		
		self.bAddNPC = wx.Button( self, wx.ID_ANY, u"NPC Generator...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bAddNPC.SetDefault() 
		bSizer118.Add( self.bAddNPC, 0, wx.EXPAND, 0 )
		
		self.bNPCFromFile = wx.Button( self, wx.ID_ANY, u"Add From File...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bNPCFromFile.SetDefault() 
		bSizer118.Add( self.bNPCFromFile, 0, wx.EXPAND, 0 )
		
		
		sbSizer37.Add( bSizer118, 1, 0, 0 )
		
		
		bSizer114.Add( sbSizer37, 0, wx.LEFT, 3 )
		
		
		bSizer110.Add( bSizer114, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_CENTRE_HORIZONTAL, 5 )
		
		sbSizer38 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Descriptions not yet placed on the map:" ), wx.VERTICAL )
		
		lbUnplacedIconsChoices = []
		self.lbUnplacedIcons = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,100 ), lbUnplacedIconsChoices, 0 )
		sbSizer38.Add( self.lbUnplacedIcons, 1, wx.EXPAND|wx.EXPAND, 0 )
		
		bSizer119 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bPlaceDescription = wx.Button( self, wx.ID_ANY, u"Place description on map", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bPlaceDescription.SetDefault() 
		self.bPlaceDescription.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bPlaceDescription.SetForegroundColour( wx.Colour( 230, 232, 151 ) )
		self.bPlaceDescription.SetBackgroundColour( wx.Colour( 0, 128, 10 ) )
		
		bSizer119.Add( self.bPlaceDescription, 0, 0, 0 )
		
		self.bDeleteUnplacedDescription = wx.Button( self, wx.ID_ANY, u"Delete Description", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bDeleteUnplacedDescription.SetDefault() 
		self.bDeleteUnplacedDescription.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bDeleteUnplacedDescription.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bDeleteUnplacedDescription.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		
		bSizer119.Add( self.bDeleteUnplacedDescription, 0, wx.LEFT, 5 )
		
		
		sbSizer38.Add( bSizer119, 0, 0, 0 )
		
		
		bSizer110.Add( sbSizer38, -1, wx.ALL|wx.EXPAND|wx.EXPAND, 3 )
		
		bSizer120 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ID_OK = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_OK.SetDefault() 
		self.ID_OK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_OK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.ID_OK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer120.Add( self.ID_OK, 0, wx.RIGHT, 5 )
		
		self.bHelp = wx.Button( self, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bHelp.SetDefault() 
		self.bHelp.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bHelp.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bHelp.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer120.Add( self.bHelp, 0, wx.LEFT, 5 )
		
		
		bSizer110.Add( bSizer120, 0, wx.ALL|wx.ALIGN_CENTRE_HORIZONTAL, 3 )
		
		
		self.SetSizer( bSizer110 )
		self.Layout()
		bSizer110.Fit( self )
		
		# Connect Events
		self.lbDescriptionsOnMap.Bind( wx.EVT_LISTBOX_DCLICK, self.dclick_lbDescriptionsOnMap )
		self.bPrintMasterList.Bind( wx.EVT_BUTTON, self.OnPrintMasterList )
		self.bDeletePlacedDescription.Bind( wx.EVT_BUTTON, self.DeletePlacedDescription )
		self.bAddMonster.Bind( wx.EVT_BUTTON, self.AddMonster )
		self.bMonsterFromFile.Bind( wx.EVT_BUTTON, self.AddMonsterFromFile )
		self.bAddTrap.Bind( wx.EVT_BUTTON, self.AddTrap )
		self.bTrapFromFile.Bind( wx.EVT_BUTTON, self.AddTrapFromFile )
		self.bAddTreasure.Bind( wx.EVT_BUTTON, self.AddTreasure )
		self.bTreasureFromFile.Bind( wx.EVT_BUTTON, self.AddTreasureFromFile )
		self.bAddNPC.Bind( wx.EVT_BUTTON, self.AddNPC )
		self.bNPCFromFile.Bind( wx.EVT_BUTTON, self.AddNPCFromFile )
		self.lbUnplacedIcons.Bind( wx.EVT_LISTBOX_DCLICK, self.dclick_lbUnplacedIcons )
		self.bPlaceDescription.Bind( wx.EVT_BUTTON, self.PlaceDescription )
		self.bDeleteUnplacedDescription.Bind( wx.EVT_BUTTON, self.DeleteUnplacedDescription )
		self.ID_OK.Bind( wx.EVT_BUTTON, self.OnClose )
		self.bHelp.Bind( wx.EVT_BUTTON, self.OnHelp )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def dclick_lbDescriptionsOnMap( self, event ):
		event.Skip()
	
	def OnPrintMasterList( self, event ):
		event.Skip()
	
	def DeletePlacedDescription( self, event ):
		event.Skip()
	
	def AddMonster( self, event ):
		event.Skip()
	
	def AddMonsterFromFile( self, event ):
		event.Skip()
	
	def AddTrap( self, event ):
		event.Skip()
	
	def AddTrapFromFile( self, event ):
		event.Skip()
	
	def AddTreasure( self, event ):
		event.Skip()
	
	def AddTreasureFromFile( self, event ):
		event.Skip()
	
	def AddNPC( self, event ):
		event.Skip()
	
	def AddNPCFromFile( self, event ):
		event.Skip()
	
	def dclick_lbUnplacedIcons( self, event ):
		event.Skip()
	
	def PlaceDescription( self, event ):
		event.Skip()
	
	def DeleteUnplacedDescription( self, event ):
		event.Skip()
	
	def OnClose( self, event ):
		event.Skip()
	
	def OnHelp( self, event ):
		event.Skip()
	

###########################################################################
## Class ChooseEncounterDialogBase
###########################################################################

class ChooseEncounterDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Choose Encounter", pos = wx.DefaultPosition, size = wx.Size( 319,362 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer121 = wx.BoxSizer( wx.VERTICAL )
		
		lbEncountersChoices = []
		self.lbEncounters = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,300 ), lbEncountersChoices, 0 )
		bSizer121.Add( self.lbEncounters, 0, wx.ALL, 4 )
		
		bSizer122 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ID_OK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_OK.SetDefault() 
		self.ID_OK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_OK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.ID_OK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer122.Add( self.ID_OK, 0, wx.RIGHT, 2 )
		
		self.ID_CANCEL = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_CANCEL.SetDefault() 
		self.ID_CANCEL.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_CANCEL.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ID_CANCEL.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		
		bSizer122.Add( self.ID_CANCEL, 0, wx.LEFT|wx.RIGHT, 2 )
		
		self.bHelp = wx.Button( self, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bHelp.SetDefault() 
		self.bHelp.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bHelp.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bHelp.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer122.Add( self.bHelp, 0, wx.LEFT, 2 )
		
		
		bSizer121.Add( bSizer122, 0, wx.ALIGN_CENTRE, 0 )
		
		
		self.SetSizer( bSizer121 )
		self.Layout()
	
	def __del__( self ):
		pass
	

###########################################################################
## Class TrapsDialogBase
###########################################################################

class TrapsDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Traps", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer123 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer124 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer553 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer126 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer368 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer125 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer39 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Trap Type" ), wx.VERTICAL )
		
		self.rbMechanicalTrap = wx.RadioButton( self, wx.ID_ANY, u"Mechanical Trap", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		self.rbMechanicalTrap.SetValue( True ) 
		self.rbMechanicalTrap.SetToolTip( u"Trap is mechanical in nature." )
		
		sbSizer39.Add( self.rbMechanicalTrap, 0, 0, 0 )
		
		self.rbMagicTrap = wx.RadioButton( self, wx.ID_ANY, u"Magic Trap", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rbMagicTrap.SetValue( True ) 
		self.rbMagicTrap.SetToolTip( u"Trap is magical in nature." )
		
		sbSizer39.Add( self.rbMagicTrap, 0, 0, 0 )
		
		self.rbOtherTrap = wx.RadioButton( self, wx.ID_ANY, u"Other", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rbOtherTrap.SetValue( True ) 
		self.rbOtherTrap.SetToolTip( u"Other (used in filtering algorithm)" )
		
		sbSizer39.Add( self.rbOtherTrap, 0, 0, 0 )
		
		
		bSizer125.Add( sbSizer39, 0, wx.EXPAND, 0 )
		
		
		bSizer368.Add( bSizer125, 0, wx.TOP|wx.LEFT, 5 )
		
		bSizer369 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap20 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"artwork/trap_icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer369.Add( self.m_bitmap20, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer368.Add( bSizer369, 1, wx.EXPAND, 5 )
		
		
		bSizer126.Add( bSizer368, 0, wx.EXPAND, 5 )
		
		bSizer127 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText68 = wx.StaticText( self, wx.ID_ANY, u"Description:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText68.Wrap( 0 )
		bSizer127.Add( self.m_staticText68, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 3 )
		
		self.txDescription = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txDescription.SetMaxLength( 0 ) 
		self.txDescription.SetToolTip( u"Enter the description of the trap." )
		
		bSizer127.Add( self.txDescription, 2, wx.EXPAND|wx.EXPAND, 0 )
		
		
		bSizer126.Add( bSizer127, 0, wx.ALL|wx.EXPAND|wx.EXPAND, 3 )
		
		bSizer139 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText82 = wx.StaticText( self, wx.ID_ANY, u"Challenge Rating:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText82.Wrap( -1 )
		bSizer139.Add( self.m_staticText82, 1, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.spChallengeRating = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, -1, 99, 1 )
		self.spChallengeRating.SetToolTip( u"What is the challenge rating (CR) of this trap?" )
		
		bSizer139.Add( self.spChallengeRating, 0, 0, 0 )
		
		
		bSizer126.Add( bSizer139, 0, wx.ALL, 3 )
		
		bSizer128 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText69 = wx.StaticText( self, wx.ID_ANY, u"Trigger:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69.Wrap( 0 )
		bSizer128.Add( self.m_staticText69, 0, wx.ALIGN_CENTRE_VERTICAL|wx.ALIGN_CENTER_VERTICAL, 0 )
		
		cbxTriggerChoices = []
		self.cbxTrigger = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), cbxTriggerChoices, 0 )
		self.cbxTrigger.SetToolTip( u"How is this trap set off?" )
		
		bSizer128.Add( self.cbxTrigger, 1, wx.LEFT, 4 )
		
		
		bSizer126.Add( bSizer128, 0, wx.ALL, 3 )
		
		bSizer129 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText70 = wx.StaticText( self, wx.ID_ANY, u"Reset:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText70.Wrap( 0 )
		bSizer129.Add( self.m_staticText70, 0, wx.ALIGN_CENTRE_VERTICAL|wx.ALIGN_CENTER_VERTICAL, 0 )
		
		cbxResetChoices = []
		self.cbxReset = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cbxResetChoices, 0 )
		self.cbxReset.SetToolTip( u"How is this trap reset?" )
		
		bSizer129.Add( self.cbxReset, 0, wx.LEFT|wx.EXPAND|wx.EXPAND, 10 )
		
		
		bSizer126.Add( bSizer129, 0, wx.ALL|wx.EXPAND|wx.EXPAND, 3 )
		
		bSizer562 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText71 = wx.StaticText( self, wx.ID_ANY, u"Search DC:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		bSizer562.Add( self.m_staticText71, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.spSearchDC = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, -1, 99, 12 )
		self.spSearchDC.SetToolTip( u"What is the DC to find this trap?" )
		
		bSizer562.Add( self.spSearchDC, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 14 )
		
		
		bSizer126.Add( bSizer562, 0, wx.ALL|wx.EXPAND, 3 )
		
		bSizer131 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText72 = wx.StaticText( self, wx.ID_ANY, u"Disable DC:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText72.Wrap( -1 )
		bSizer131.Add( self.m_staticText72, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 0 )
		
		self.spDisableDC = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, -1, 99, 12 )
		self.spDisableDC.SetToolTip( u"What is the DC to disable this trap?" )
		
		bSizer131.Add( self.spDisableDC, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 14 )
		
		
		bSizer126.Add( bSizer131, 0, wx.ALL|wx.EXPAND, 3 )
		
		bSizer132 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText73 = wx.StaticText( self, wx.ID_ANY, u"Attack Bonus:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText73.Wrap( -1 )
		bSizer132.Add( self.m_staticText73, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.spAttackBonus = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, -1, 99,  )
		self.spAttackBonus.SetToolTip( u"If this trap simulates an attack, what is the bonus?" )
		
		bSizer132.Add( self.spAttackBonus, 0, wx.LEFT, 3 )
		
		cbxAttackTypeChoices = []
		self.cbxAttackType = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), cbxAttackTypeChoices, 0 )
		self.cbxAttackType.SetToolTip( u"What type of attack mode?" )
		
		bSizer132.Add( self.cbxAttackType, 0, wx.LEFT, 3 )
		
		
		bSizer126.Add( bSizer132, 0, wx.ALL, 3 )
		
		bSizer133 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer558 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText74 = wx.StaticText( self, wx.ID_ANY, u"Damage Effect:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText74.Wrap( -1 )
		bSizer558.Add( self.m_staticText74, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.txDamageEffect = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,60 ), wx.TE_MULTILINE )
		self.txDamageEffect.SetMaxLength( 0 ) 
		self.txDamageEffect.SetToolTip( u"If the trap is sprung, what happens?" )
		
		bSizer558.Add( self.txDamageEffect, 1, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 3 )
		
		
		bSizer133.Add( bSizer558, 0, wx.EXPAND, 5 )
		
		bSizer559 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText294 = wx.StaticText( self, wx.ID_ANY, u"Damage Dice:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText294.Wrap( -1 )
		bSizer559.Add( self.m_staticText294, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 15 )
		
		self.txDamageDice = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txDamageDice.SetToolTip( u"Enter the damage dice, ie, 2d10+3" )
		
		bSizer559.Add( self.txDamageDice, 0, wx.ALL, 5 )
		
		
		bSizer133.Add( bSizer559, 0, wx.EXPAND, 5 )
		
		
		bSizer126.Add( bSizer133, 0, wx.ALL|wx.EXPAND, 3 )
		
		bSizer134 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText75 = wx.StaticText( self, wx.ID_ANY, u"Save DC:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText75.Wrap( -1 )
		bSizer134.Add( self.m_staticText75, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.spSaveDC = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, -1, 99, 12 )
		self.spSaveDC.SetToolTip( u"What is the DC to save against this trap's effect?" )
		
		bSizer134.Add( self.spSaveDC, 0, wx.LEFT, 3 )
		
		cbxSaveTypeChoices = []
		self.cbxSaveType = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), cbxSaveTypeChoices, 0 )
		self.cbxSaveType.SetToolTip( u"Which save type to use?" )
		
		bSizer134.Add( self.cbxSaveType, 0, wx.LEFT, 2 )
		
		cbxSaveAmountChoices = []
		self.cbxSaveAmount = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120, -1 ), cbxSaveAmountChoices, 0 )
		self.cbxSaveAmount.SetToolTip( u"If the save is successful, save for half or avoid?" )
		
		bSizer134.Add( self.cbxSaveAmount, 0, 0, 0 )
		
		
		bSizer126.Add( bSizer134, 0, wx.ALL, 3 )
		
		bSizer135 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText76 = wx.StaticText( self, wx.ID_ANY, u"Optional:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText76.Wrap( 0 )
		bSizer135.Add( self.m_staticText76, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		cbxOptionalChoices = []
		self.cbxOptional = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), cbxOptionalChoices, 0 )
		self.cbxOptional.SetToolTip( u"Some traps have an optional feature." )
		
		bSizer135.Add( self.cbxOptional, 1, wx.LEFT, 4 )
		
		
		bSizer126.Add( bSizer135, 0, wx.ALL, 3 )
		
		bSizer137 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText78 = wx.StaticText( self, wx.ID_ANY, u"Bypass:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText78.Wrap( 0 )
		bSizer137.Add( self.m_staticText78, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		cbxBypassChoices = []
		self.cbxBypass = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), cbxBypassChoices, 0 )
		self.cbxBypass.SetToolTip( u"What kind of bypass is equipped with this trap?" )
		
		bSizer137.Add( self.cbxBypass, 0, wx.LEFT|wx.EXPAND|wx.EXPAND, 3 )
		
		
		bSizer126.Add( bSizer137, 0, wx.ALL, 3 )
		
		bSizer136 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText77 = wx.StaticText( self, wx.ID_ANY, u"Other Features:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText77.Wrap( -1 )
		bSizer136.Add( self.m_staticText77, 0, 0, 0 )
		
		self.txOtherFeature = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,40 ), wx.TE_MULTILINE )
		self.txOtherFeature.SetMaxLength( 0 ) 
		self.txOtherFeature.SetToolTip( u"Other notes or user-defined features of the trap." )
		
		bSizer136.Add( self.txOtherFeature, 2, wx.LEFT|wx.EXPAND|wx.EXPAND, 3 )
		
		
		bSizer126.Add( bSizer136, 0, wx.ALL|wx.EXPAND|wx.EXPAND, 3 )
		
		bSizer138 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText79 = wx.StaticText( self, wx.ID_ANY, u"Construction Cost:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText79.Wrap( -1 )
		bSizer138.Add( self.m_staticText79, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.m_staticText80 = wx.StaticText( self, wx.ID_ANY, u"GP:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText80.Wrap( 0 )
		bSizer138.Add( self.m_staticText80, 0, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 6 )
		
		self.txGPCost = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.SP_ARROW_KEYS, -1, 500000,  )
		self.txGPCost.SetToolTip( u"How much does this trap cost in gold?" )
		
		bSizer138.Add( self.txGPCost, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 3 )
		
		self.m_staticText81 = wx.StaticText( self, wx.ID_ANY, u"XP:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( 0 )
		bSizer138.Add( self.m_staticText81, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 20 )
		
		self.txXPCost = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), wx.SP_ARROW_KEYS, -1, 500000,  )
		self.txXPCost.SetToolTip( u"How much does this cost in XP?" )
		
		bSizer138.Add( self.txXPCost, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		
		bSizer126.Add( bSizer138, 0, wx.ALL|wx.EXPAND, 3 )
		
		
		bSizer553.Add( bSizer126, 0, wx.EXPAND|wx.EXPAND, 0 )
		
		sbSizer891 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Filters" ), wx.VERTICAL )
		
		bSizer518 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer525 = wx.BoxSizer( wx.VERTICAL )
		
		self.cbFilterByCR = wx.CheckBox( self, wx.ID_ANY, u"CR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbFilterByCR.SetToolTip( u"Check to filter by Challenge Rating" )
		
		bSizer525.Add( self.cbFilterByCR, 0, wx.ALL, 5 )
		
		lbCRFilterChoices = [ u"<1", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10", u"11", u"12", u"13", u"14", u"15", u"16", u"17", u"18", u"19", u"20+" ]
		self.lbCRFilter = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 50,-1 ), lbCRFilterChoices, wx.LB_MULTIPLE )
		self.lbCRFilter.Enable( False )
		self.lbCRFilter.SetToolTip( u"Select CR to filter" )
		
		bSizer525.Add( self.lbCRFilter, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer518.Add( bSizer525, 0, wx.EXPAND, 5 )
		
		bSizer561 = wx.BoxSizer( wx.VERTICAL )
		
		self.cbTypeFilter = wx.CheckBox( self, wx.ID_ANY, u"Type", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer561.Add( self.cbTypeFilter, 0, wx.ALL, 5 )
		
		lbFilterByTypeChoices = [ u"Mechanical", u"Magical", u"Other" ]
		self.lbFilterByType = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lbFilterByTypeChoices, wx.LB_MULTIPLE )
		self.lbFilterByType.Enable( False )
		
		bSizer561.Add( self.lbFilterByType, 0, wx.ALL, 5 )
		
		
		bSizer518.Add( bSizer561, 0, wx.EXPAND, 5 )
		
		bSizer563 = wx.BoxSizer( wx.VERTICAL )
		
		self.cbDangerFilter = wx.CheckBox( self, wx.ID_ANY, u"Danger Level", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer563.Add( self.cbDangerFilter, 0, wx.ALL, 5 )
		
		lbDangerFilterChoices = [ u"Annoyance", u"Setback", u"Dangerous", u"Deadly", u"Evil" ]
		self.lbDangerFilter = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lbDangerFilterChoices, wx.LB_MULTIPLE )
		self.lbDangerFilter.Enable( False )
		
		bSizer563.Add( self.lbDangerFilter, 0, wx.ALL, 5 )
		
		
		bSizer518.Add( bSizer563, 0, wx.EXPAND, 5 )
		
		bSizer564 = wx.BoxSizer( wx.VERTICAL )
		
		self.cbSourceFilter = wx.CheckBox( self, wx.ID_ANY, u"Source Definition", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer564.Add( self.cbSourceFilter, 0, wx.ALL, 5 )
		
		lbSourceFilterChoices = [ u"Original SRD", u"User Defined" ]
		self.lbSourceFilter = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lbSourceFilterChoices, wx.LB_MULTIPLE )
		self.lbSourceFilter.Enable( False )
		
		bSizer564.Add( self.lbSourceFilter, 0, wx.ALL, 5 )
		
		
		bSizer518.Add( bSizer564, 1, wx.EXPAND, 5 )
		
		
		sbSizer891.Add( bSizer518, 1, wx.EXPAND, 5 )
		
		
		bSizer553.Add( sbSizer891, 1, wx.EXPAND, 5 )
		
		
		bSizer124.Add( bSizer553, 0, wx.EXPAND, 5 )
		
		bApplyFilter1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bUpdateSelectedTrap = wx.Button( self, wx.ID_ANY, u"Update Selected Trap to Current Info", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bUpdateSelectedTrap.SetDefault() 
		self.bUpdateSelectedTrap.SetToolTip( u"Update the trap selected in the list to the values above." )
		
		bApplyFilter1.Add( self.bUpdateSelectedTrap, 0, wx.ALIGN_RIGHT, 5 )
		
		
		bSizer124.Add( bApplyFilter1, 0, wx.EXPAND, 0 )
		
		bSizer141 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ID_OK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_OK.SetDefault() 
		self.ID_OK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_OK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.ID_OK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer141.Add( self.ID_OK, 0, wx.RIGHT, 2 )
		
		self.ID_CANCEL = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_CANCEL.SetDefault() 
		self.ID_CANCEL.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_CANCEL.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ID_CANCEL.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		
		bSizer141.Add( self.ID_CANCEL, 0, wx.LEFT|wx.RIGHT, 2 )
		
		self.bHelp = wx.Button( self, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bHelp.SetDefault() 
		self.bHelp.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bHelp.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bHelp.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer141.Add( self.bHelp, 0, wx.LEFT, 2 )
		
		
		bSizer124.Add( bSizer141, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 10 )
		
		
		bSizer123.Add( bSizer124, 0, 0, 0 )
		
		bSizer142 = wx.BoxSizer( wx.VERTICAL )
		
		lbTrapListChoices = []
		self.lbTrapList = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 250,-1 ), lbTrapListChoices, wx.LB_SINGLE|wx.LB_SORT )
		bSizer142.Add( self.lbTrapList, 1, wx.ALL|wx.EXPAND|wx.EXPAND, 3 )
		
		bSizer143 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bAddTrap = wx.Button( self, wx.ID_ANY, u"Add New Trap", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bAddTrap.SetDefault() 
		self.bAddTrap.SetToolTip( u"Add a new trap based on the values to the left." )
		
		bSizer143.Add( self.bAddTrap, 0, wx.LEFT|wx.RIGHT, 3 )
		
		self.bDeleteTrap = wx.Button( self, wx.ID_ANY, u"Delete Trap", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bDeleteTrap.SetDefault() 
		self.bDeleteTrap.SetToolTip( u"Delete the currently selected trap." )
		
		bSizer143.Add( self.bDeleteTrap, 0, wx.LEFT|wx.RIGHT, 3 )
		
		self.bClearSelection = wx.Button( self, wx.ID_ANY, u"Clear Selection", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bClearSelection.SetDefault() 
		self.bClearSelection.SetToolTip( u"Clear all selections on the trap listing." )
		
		bSizer143.Add( self.bClearSelection, 0, wx.LEFT|wx.RIGHT, 3 )
		
		
		bSizer142.Add( bSizer143, 0, wx.ALIGN_CENTRE_HORIZONTAL, 0 )
		
		
		bSizer123.Add( bSizer142, 0, wx.LEFT|wx.EXPAND|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer123 )
		self.Layout()
		bSizer123.Fit( self )
		
		# Connect Events
		self.cbFilterByCR.Bind( wx.EVT_CHECKBOX, self.ApplyFilter )
		self.lbCRFilter.Bind( wx.EVT_LISTBOX, self.ApplyFilter )
		self.cbTypeFilter.Bind( wx.EVT_CHECKBOX, self.ApplyFilter )
		self.lbFilterByType.Bind( wx.EVT_LISTBOX, self.ApplyFilter )
		self.cbDangerFilter.Bind( wx.EVT_CHECKBOX, self.ApplyFilter )
		self.lbDangerFilter.Bind( wx.EVT_LISTBOX, self.ApplyFilter )
		self.cbSourceFilter.Bind( wx.EVT_CHECKBOX, self.ApplyFilter )
		self.lbSourceFilter.Bind( wx.EVT_LISTBOX, self.ApplyFilter )
		self.bUpdateSelectedTrap.Bind( wx.EVT_BUTTON, self.UpdateSelectedTrap )
		self.ID_OK.Bind( wx.EVT_BUTTON, self.OnOK )
		self.ID_CANCEL.Bind( wx.EVT_BUTTON, self.OnCancel )
		self.bHelp.Bind( wx.EVT_BUTTON, self.OnHelp )
		self.lbTrapList.Bind( wx.EVT_LISTBOX, self.OnListbox_lbTrapList )
		self.bAddTrap.Bind( wx.EVT_BUTTON, self.AddTrap )
		self.bDeleteTrap.Bind( wx.EVT_BUTTON, self.DeleteTrap )
		self.bClearSelection.Bind( wx.EVT_BUTTON, self.ClearSelection )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def ApplyFilter( self, event ):
		event.Skip()
	
	
	
	
	
	
	
	
	def UpdateSelectedTrap( self, event ):
		event.Skip()
	
	def OnOK( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		event.Skip()
	
	def OnHelp( self, event ):
		event.Skip()
	
	def OnListbox_lbTrapList( self, event ):
		event.Skip()
	
	def AddTrap( self, event ):
		event.Skip()
	
	def DeleteTrap( self, event ):
		event.Skip()
	
	def ClearSelection( self, event ):
		event.Skip()
	

###########################################################################
## Class TrapsHoverBase
###########################################################################

class TrapsHoverBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Traps", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer123 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer124 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer126 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer560 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bRollDamage = wx.Button( self, wx.ID_ANY, u"Roll Damage", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.bRollDamage.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.bRollDamage.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bRollDamage.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
		self.bRollDamage.SetToolTip( u"Roll dice to determine damage" )
		self.bRollDamage.SetHelpText( u"Click to roll the damage dice" )
		
		bSizer560.Add( self.bRollDamage, 0, 0, 5 )
		
		self.stDamageRoll = wx.StaticText( self, wx.ID_ANY, u"Damage: 0d0 HP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stDamageRoll.Wrap( -1 )
		bSizer560.Add( self.stDamageRoll, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		bSizer126.Add( bSizer560, 1, wx.EXPAND, 5 )
		
		bSizer127 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText68 = wx.StaticText( self, wx.ID_ANY, u"Description:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText68.Wrap( 0 )
		bSizer127.Add( self.m_staticText68, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.txDescription = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.txDescription.SetMaxLength( 0 ) 
		self.txDescription.SetToolTip( u"Enter the description of the trap." )
		
		bSizer127.Add( self.txDescription, 2, wx.EXPAND|wx.EXPAND, 0 )
		
		
		bSizer126.Add( bSizer127, 0, wx.ALL|wx.EXPAND|wx.EXPAND, 3 )
		
		bSizer368 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stTrapType = wx.StaticText( self, wx.ID_ANY, u"Mechanical/Magical/Other Trap", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stTrapType.Wrap( -1 )
		bSizer368.Add( self.stTrapType, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer126.Add( bSizer368, 1, wx.EXPAND, 3 )
		
		bSizer139 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText82 = wx.StaticText( self, wx.ID_ANY, u"Challenge Rating:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText82.Wrap( -1 )
		bSizer139.Add( self.m_staticText82, 1, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.spChallengeRating = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 0, 99, 1 )
		self.spChallengeRating.SetToolTip( u"What is the challenge rating (CR) of this trap?" )
		
		bSizer139.Add( self.spChallengeRating, 0, wx.LEFT, 10 )
		
		
		bSizer126.Add( bSizer139, 0, wx.ALL, 3 )
		
		bSizer555 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer130 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText71 = wx.StaticText( self, wx.ID_ANY, u"Search DC:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		bSizer130.Add( self.m_staticText71, 1, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.spSearchDC = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 0, 99, 12 )
		self.spSearchDC.SetToolTip( u"What is the DC to find this trap?" )
		
		bSizer130.Add( self.spSearchDC, 0, wx.LEFT, 5 )
		
		
		bSizer555.Add( bSizer130, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 3 )
		
		bSizer131 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText72 = wx.StaticText( self, wx.ID_ANY, u"Disable DC:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText72.Wrap( -1 )
		bSizer131.Add( self.m_staticText72, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.spDisableDC = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 0, 99, 12 )
		self.spDisableDC.SetToolTip( u"What is the DC to disable this trap?" )
		
		bSizer131.Add( self.spDisableDC, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.LEFT, 5 )
		
		
		bSizer555.Add( bSizer131, 1, wx.EXPAND|wx.LEFT, 25 )
		
		
		bSizer126.Add( bSizer555, 1, wx.EXPAND, 5 )
		
		bSizer128 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText69 = wx.StaticText( self, wx.ID_ANY, u"Trigger:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69.Wrap( 0 )
		bSizer128.Add( self.m_staticText69, 0, wx.ALIGN_CENTRE_VERTICAL|wx.ALIGN_CENTER_VERTICAL, 0 )
		
		cbxTriggerChoices = []
		self.cbxTrigger = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), cbxTriggerChoices, 0 )
		self.cbxTrigger.SetToolTip( u"How is this trap set off?" )
		
		bSizer128.Add( self.cbxTrigger, 1, wx.LEFT, 4 )
		
		
		bSizer126.Add( bSizer128, 0, wx.ALL|wx.EXPAND, 3 )
		
		bSizer129 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText70 = wx.StaticText( self, wx.ID_ANY, u"Reset:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText70.Wrap( 0 )
		bSizer129.Add( self.m_staticText70, 0, wx.ALIGN_CENTRE_VERTICAL, 0 )
		
		cbxResetChoices = []
		self.cbxReset = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cbxResetChoices, 0 )
		self.cbxReset.SetToolTip( u"How is this trap reset?" )
		
		bSizer129.Add( self.cbxReset, 1, wx.LEFT|wx.EXPAND|wx.EXPAND, 10 )
		
		
		bSizer126.Add( bSizer129, 0, wx.ALL|wx.EXPAND|wx.EXPAND, 3 )
		
		bSizer132 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText73 = wx.StaticText( self, wx.ID_ANY, u"Attack Bonus:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText73.Wrap( -1 )
		bSizer132.Add( self.m_staticText73, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.spAttackBonus = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, -1, 99,  )
		self.spAttackBonus.SetToolTip( u"If this trap simulates an attack, what is the bonus?" )
		
		bSizer132.Add( self.spAttackBonus, 0, wx.LEFT, 3 )
		
		cbxAttackTypeChoices = []
		self.cbxAttackType = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), cbxAttackTypeChoices, 0 )
		self.cbxAttackType.SetToolTip( u"What type of attack mode?" )
		
		bSizer132.Add( self.cbxAttackType, 1, wx.LEFT, 3 )
		
		
		bSizer126.Add( bSizer132, 0, wx.ALL|wx.EXPAND, 3 )
		
		bSizer133 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText74 = wx.StaticText( self, wx.ID_ANY, u"Damage:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText74.Wrap( 0 )
		bSizer133.Add( self.m_staticText74, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.txDamageEffect = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_MULTILINE )
		self.txDamageEffect.SetMaxLength( 0 ) 
		self.txDamageEffect.SetToolTip( u"If the trap is sprung, what happens?" )
		
		bSizer133.Add( self.txDamageEffect, 2, wx.EXPAND|wx.LEFT, 3 )
		
		
		bSizer126.Add( bSizer133, 0, wx.ALL|wx.EXPAND|wx.EXPAND, 3 )
		
		bSizer134 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText75 = wx.StaticText( self, wx.ID_ANY, u"Save DC:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText75.Wrap( -1 )
		bSizer134.Add( self.m_staticText75, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.spSaveDC = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, -1, 99, 12 )
		self.spSaveDC.SetToolTip( u"What is the DC to save against this trap's effect?" )
		
		bSizer134.Add( self.spSaveDC, 0, wx.LEFT, 3 )
		
		cbxSaveTypeChoices = []
		self.cbxSaveType = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), cbxSaveTypeChoices, 0 )
		self.cbxSaveType.SetToolTip( u"Which save type to use?" )
		
		bSizer134.Add( self.cbxSaveType, 0, wx.LEFT, 2 )
		
		cbxSaveAmountChoices = []
		self.cbxSaveAmount = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120, -1 ), cbxSaveAmountChoices, 0 )
		self.cbxSaveAmount.SetToolTip( u"If the save is successful, save for half or avoid?" )
		
		bSizer134.Add( self.cbxSaveAmount, 0, 0, 0 )
		
		
		bSizer126.Add( bSizer134, 0, wx.ALL, 3 )
		
		bSizer137 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText78 = wx.StaticText( self, wx.ID_ANY, u"Bypass:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText78.Wrap( 0 )
		bSizer137.Add( self.m_staticText78, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		cbxBypassChoices = []
		self.cbxBypass = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), cbxBypassChoices, 0 )
		self.cbxBypass.SetToolTip( u"What kind of bypass is equipped with this trap?" )
		
		bSizer137.Add( self.cbxBypass, 1, wx.LEFT|wx.EXPAND|wx.EXPAND, 3 )
		
		
		bSizer126.Add( bSizer137, 0, wx.ALL|wx.EXPAND, 3 )
		
		bSizer135 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText76 = wx.StaticText( self, wx.ID_ANY, u"Optional:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText76.Wrap( 0 )
		bSizer135.Add( self.m_staticText76, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		cbxOptionalChoices = []
		self.cbxOptional = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), cbxOptionalChoices, 0 )
		self.cbxOptional.SetToolTip( u"Some traps have an optional feature." )
		
		bSizer135.Add( self.cbxOptional, 1, wx.LEFT, 4 )
		
		
		bSizer126.Add( bSizer135, 0, wx.ALL|wx.EXPAND, 3 )
		
		bSizer136 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText77 = wx.StaticText( self, wx.ID_ANY, u"Other Features:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText77.Wrap( -1 )
		bSizer136.Add( self.m_staticText77, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.txOtherFeature = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_MULTILINE )
		self.txOtherFeature.SetMaxLength( 0 ) 
		self.txOtherFeature.SetToolTip( u"Other notes or user-defined features of the trap." )
		
		bSizer136.Add( self.txOtherFeature, 2, wx.LEFT|wx.EXPAND|wx.EXPAND, 3 )
		
		
		bSizer126.Add( bSizer136, 0, wx.ALL|wx.EXPAND|wx.EXPAND, 3 )
		
		
		bSizer124.Add( bSizer126, 0, wx.EXPAND|wx.EXPAND, 0 )
		
		
		bSizer123.Add( bSizer124, 0, 0, 0 )
		
		
		self.SetSizer( bSizer123 )
		self.Layout()
		bSizer123.Fit( self )
		
		# Connect Events
		self.bRollDamage.Bind( wx.EVT_BUTTON, self.OnRollDamage )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnRollDamage( self, event ):
		event.Skip()
	

###########################################################################
## Class DiceRollDialogBase
###########################################################################

class DiceRollDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Dice Roller", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bCloseDialog1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer638 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer636 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer145 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bRoll_d4 = wx.Button( self, wx.ID_ANY, u"1d4:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bRoll_d4.SetDefault() 
		self.bRoll_d4.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bRoll_d4.SetBackgroundColour( wx.Colour( 255, 255, 0 ) )
		
		bSizer145.Add( self.bRoll_d4, 0, 0, 0 )
		
		self.txResult_d4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.txResult_d4.SetMaxLength( 0 ) 
		bSizer145.Add( self.txResult_d4, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		
		bSizer636.Add( bSizer145, 0, 0, 0 )
		
		bSizer146 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bRoll_d6 = wx.Button( self, wx.ID_ANY, u"1d6:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bRoll_d6.SetDefault() 
		self.bRoll_d6.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bRoll_d6.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bRoll_d6.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer146.Add( self.bRoll_d6, 0, 0, 0 )
		
		self.txResult_d6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.txResult_d6.SetMaxLength( 0 ) 
		bSizer146.Add( self.txResult_d6, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		
		bSizer636.Add( bSizer146, 0, 0, 0 )
		
		bSizer147 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bRoll_d8 = wx.Button( self, wx.ID_ANY, u"1d8:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bRoll_d8.SetDefault() 
		self.bRoll_d8.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bRoll_d8.SetBackgroundColour( wx.Colour( 255, 88, 9 ) )
		
		bSizer147.Add( self.bRoll_d8, 0, 0, 0 )
		
		self.txResult_d8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.txResult_d8.SetMaxLength( 0 ) 
		bSizer147.Add( self.txResult_d8, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		
		bSizer636.Add( bSizer147, 0, 0, 0 )
		
		bSizer148 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bRoll_d10 = wx.Button( self, wx.ID_ANY, u"1d10:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bRoll_d10.SetDefault() 
		self.bRoll_d10.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bRoll_d10.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bRoll_d10.SetBackgroundColour( wx.Colour( 128, 64, 64 ) )
		
		bSizer148.Add( self.bRoll_d10, 0, 0, 0 )
		
		self.txResult_d10 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.txResult_d10.SetMaxLength( 0 ) 
		bSizer148.Add( self.txResult_d10, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		
		bSizer636.Add( bSizer148, 0, 0, 0 )
		
		bSizer149 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bRoll_d12 = wx.Button( self, wx.ID_ANY, u"1d12:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bRoll_d12.SetDefault() 
		self.bRoll_d12.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bRoll_d12.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.bRoll_d12.SetBackgroundColour( wx.Colour( 0, 64, 0 ) )
		
		bSizer149.Add( self.bRoll_d12, 0, 0, 0 )
		
		self.txResult_d12 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.txResult_d12.SetMaxLength( 0 ) 
		bSizer149.Add( self.txResult_d12, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		
		bSizer636.Add( bSizer149, 0, 0, 0 )
		
		bSizer150 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bRoll_d20 = wx.Button( self, wx.ID_ANY, u"1d20:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bRoll_d20.SetDefault() 
		self.bRoll_d20.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bRoll_d20.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bRoll_d20.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )
		
		bSizer150.Add( self.bRoll_d20, 0, 0, 0 )
		
		self.txResult_d20 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.txResult_d20.SetMaxLength( 0 ) 
		bSizer150.Add( self.txResult_d20, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		
		bSizer636.Add( bSizer150, 0, 0, 0 )
		
		bSizer151 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bRoll_d100 = wx.Button( self, wx.ID_ANY, u"1d100:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bRoll_d100.SetDefault() 
		self.bRoll_d100.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bRoll_d100.SetForegroundColour( wx.Colour( 192, 192, 192 ) )
		self.bRoll_d100.SetBackgroundColour( wx.Colour( 128, 0, 255 ) )
		
		bSizer151.Add( self.bRoll_d100, 0, 0, 0 )
		
		self.txResult_d100 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.txResult_d100.SetMaxLength( 0 ) 
		bSizer151.Add( self.txResult_d100, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		
		bSizer636.Add( bSizer151, 0, 0, 0 )
		
		
		bSizer638.Add( bSizer636, 0, wx.EXPAND, 5 )
		
		bSizer637 = wx.BoxSizer( wx.VERTICAL )
		
		self.txResults = wx.TextCtrl( self, wx.ID_ANY, u"1d100 = 100", wx.DefaultPosition, wx.Size( 80,-1 ), wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2 )
		bSizer637.Add( self.txResults, 1, wx.EXPAND|wx.LEFT, 5 )
		
		
		bSizer638.Add( bSizer637, 1, wx.EXPAND, 5 )
		
		
		bCloseDialog1.Add( bSizer638, 1, wx.EXPAND, 5 )
		
		self.m_staticText83 = wx.StaticText( self, wx.ID_ANY, u"Custom Dice (1d6, 3d4+2, etc.)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83.Wrap( -1 )
		bCloseDialog1.Add( self.m_staticText83, 0, wx.TOP|wx.BOTTOM|wx.LEFT, 2 )
		
		bSizer152 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txCustom1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.txCustom1.SetMaxLength( 0 ) 
		bSizer152.Add( self.txCustom1, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.bRoll_Custom1 = wx.Button( self, wx.ID_ANY, u"Roll:", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.bRoll_Custom1.SetDefault() 
		bSizer152.Add( self.bRoll_Custom1, 0, 0, 0 )
		
		self.txResult_Custom1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.txResult_Custom1.SetMaxLength( 0 ) 
		bSizer152.Add( self.txResult_Custom1, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		
		bCloseDialog1.Add( bSizer152, 0, 0, 0 )
		
		bSizer153 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txCustom2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.txCustom2.SetMaxLength( 0 ) 
		bSizer153.Add( self.txCustom2, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.bRoll_Custom2 = wx.Button( self, wx.ID_ANY, u"Roll:", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.bRoll_Custom2.SetDefault() 
		bSizer153.Add( self.bRoll_Custom2, 0, 0, 0 )
		
		self.txResult_Custom2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.txResult_Custom2.SetMaxLength( 0 ) 
		bSizer153.Add( self.txResult_Custom2, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		
		bCloseDialog1.Add( bSizer153, 0, 0, 0 )
		
		bCloseDialog2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bCloseDialog = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bCloseDialog.SetDefault() 
		self.bCloseDialog.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bCloseDialog.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.bCloseDialog.SetBackgroundColour( wx.Colour( 0, 64, 0 ) )
		
		bCloseDialog2.Add( self.bCloseDialog, 0, 0, 0 )
		
		self.bHelpButton = wx.Button( self, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bHelpButton.SetDefault() 
		self.bHelpButton.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bHelpButton.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bHelpButton.SetBackgroundColour( wx.Colour( 0, 0, 160 ) )
		
		bCloseDialog2.Add( self.bHelpButton, 0, 0, 0 )
		
		
		bCloseDialog1.Add( bCloseDialog2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP, 5 )
		
		
		self.SetSizer( bCloseDialog1 )
		self.Layout()
		bCloseDialog1.Fit( self )
		
		# Connect Events
		self.bRoll_d4.Bind( wx.EVT_BUTTON, self.OnRoll_d4 )
		self.bRoll_d6.Bind( wx.EVT_BUTTON, self.OnRoll_d6 )
		self.bRoll_d8.Bind( wx.EVT_BUTTON, self.OnRoll_d8 )
		self.bRoll_d10.Bind( wx.EVT_BUTTON, self.OnRoll_d10 )
		self.bRoll_d12.Bind( wx.EVT_BUTTON, self.OnRoll_d12 )
		self.bRoll_d20.Bind( wx.EVT_BUTTON, self.OnRoll_d20 )
		self.bRoll_d100.Bind( wx.EVT_BUTTON, self.OnRoll_d100 )
		self.bRoll_Custom1.Bind( wx.EVT_BUTTON, self.OnRoll_Custom1 )
		self.bRoll_Custom2.Bind( wx.EVT_BUTTON, self.OnRoll_Custom2 )
		self.bCloseDialog.Bind( wx.EVT_BUTTON, self.OnClose )
		self.bHelpButton.Bind( wx.EVT_BUTTON, self.OnHelp )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnRoll_d4( self, event ):
		event.Skip()
	
	def OnRoll_d6( self, event ):
		event.Skip()
	
	def OnRoll_d8( self, event ):
		event.Skip()
	
	def OnRoll_d10( self, event ):
		event.Skip()
	
	def OnRoll_d12( self, event ):
		event.Skip()
	
	def OnRoll_d20( self, event ):
		event.Skip()
	
	def OnRoll_d100( self, event ):
		event.Skip()
	
	def OnRoll_Custom1( self, event ):
		event.Skip()
	
	def OnRoll_Custom2( self, event ):
		event.Skip()
	
	def OnClose( self, event ):
		event.Skip()
	
	def OnHelp( self, event ):
		event.Skip()
	

###########################################################################
## Class NPC_GeneratorDialogBase
###########################################################################

class NPC_GeneratorDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"NPC Generator", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer155 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 3, 3, 5, 5 )
		
		sbSizer41 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Alignment" ), wx.VERTICAL )
		
		cbxAlignmentChoices = []
		self.cbxAlignment = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), cbxAlignmentChoices, 0 )
		sbSizer41.Add( self.cbxAlignment, 0, 0, 0 )
		
		
		gSizer1.Add( sbSizer41, 0, 0, 0 )
		
		sbSizer42 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Class" ), wx.VERTICAL )
		
		cbxClass1Choices = []
		self.cbxClass1 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cbxClass1Choices, wx.CB_READONLY )
		sbSizer42.Add( self.cbxClass1, 0, wx.EXPAND, 0 )
		
		cbxClass2Choices = []
		self.cbxClass2 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), cbxClass2Choices, wx.CB_READONLY )
		self.cbxClass2.Hide()
		
		sbSizer42.Add( self.cbxClass2, 0, wx.EXPAND, 0 )
		
		cbxClass3Choices = []
		self.cbxClass3 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), cbxClass3Choices, wx.CB_READONLY )
		self.cbxClass3.Hide()
		
		sbSizer42.Add( self.cbxClass3, 1, wx.EXPAND, 0 )
		
		
		gSizer1.Add( sbSizer42, 0, wx.EXPAND, 0 )
		
		sbSizer43 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Level" ), wx.VERTICAL )
		
		self.cbClass1Random = wx.CheckBox( self, wx.ID_ANY, u"Random?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbClass1Random.SetValue(True) 
		sbSizer43.Add( self.cbClass1Random, 0, wx.ALIGN_CENTRE_VERTICAL, 0 )
		
		self.spClass1Level = wx.SpinCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 55,-1 ), wx.SP_ARROW_KEYS, 1, 20, 1 )
		sbSizer43.Add( self.spClass1Level, 0, 0, 0 )
		
		self.cbClass3Random = wx.CheckBox( self, wx.ID_ANY, u"Random?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbClass3Random.SetValue(True) 
		self.cbClass3Random.Hide()
		
		sbSizer43.Add( self.cbClass3Random, 0, wx.ALIGN_CENTRE_VERTICAL, 0 )
		
		self.cbClass2Random = wx.CheckBox( self, wx.ID_ANY, u"Random?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbClass2Random.SetValue(True) 
		self.cbClass2Random.Hide()
		
		sbSizer43.Add( self.cbClass2Random, 0, wx.ALIGN_CENTRE_VERTICAL, 0 )
		
		self.spClass3Level = wx.SpinCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 55,-1 ), wx.SP_ARROW_KEYS, 0, 20, 0 )
		self.spClass3Level.Hide()
		
		sbSizer43.Add( self.spClass3Level, 0, 0, 0 )
		
		self.spClass2Level = wx.SpinCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 55,-1 ), wx.SP_ARROW_KEYS, 0, 20, 0 )
		self.spClass2Level.Hide()
		
		sbSizer43.Add( self.spClass2Level, 0, wx.ALIGN_CENTRE, 0 )
		
		
		gSizer1.Add( sbSizer43, 0, 0, 0 )
		
		sbSizer44 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Gender" ), wx.VERTICAL )
		
		cbxGenderChoices = []
		self.cbxGender = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 75,-1 ), cbxGenderChoices, wx.CB_READONLY )
		sbSizer44.Add( self.cbxGender, 0, wx.EXPAND, 0 )
		
		
		gSizer1.Add( sbSizer44, 0, wx.EXPAND, 0 )
		
		sbSizer47 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Race" ), wx.VERTICAL )
		
		cbxRaceChoices = []
		self.cbxRace = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, cbxRaceChoices, wx.CB_READONLY )
		sbSizer47.Add( self.cbxRace, 0, wx.EXPAND, 0 )
		
		
		gSizer1.Add( sbSizer47, 0, wx.EXPAND, 0 )
		
		sbSizer50 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Ability Score Generation" ), wx.VERTICAL )
		
		cbxAbilityScoreGenChoices = []
		self.cbxAbilityScoreGen = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), cbxAbilityScoreGenChoices, wx.CB_READONLY )
		sbSizer50.Add( self.cbxAbilityScoreGen, 0, 0, 0 )
		
		
		gSizer1.Add( sbSizer50, 0, wx.EXPAND, 0 )
		
		sbSizer51 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Number to Generate" ), wx.VERTICAL )
		
		self.spNumGenerate = wx.SpinCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 1, 10, 1 )
		sbSizer51.Add( self.spNumGenerate, 0, wx.ALIGN_CENTER, 0 )
		
		
		gSizer1.Add( sbSizer51, 0, 0, 0 )
		
		sbSizer52 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Other Options" ), wx.VERTICAL )
		
		self.m_checkBox45 = wx.CheckBox( self, wx.ID_ANY, u"Show NPC Motivation?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox45.SetValue(True) 
		sbSizer52.Add( self.m_checkBox45, 0, 0, 0 )
		
		
		gSizer1.Add( sbSizer52, 0, 0, 0 )
		
		bSizer635 = wx.BoxSizer( wx.VERTICAL )
		
		self.bGenerateNPC = wx.Button( self, wx.ID_ANY, u"Generate NPC", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bGenerateNPC.SetDefault() 
		self.bGenerateNPC.SetFont( wx.Font( 8, 74, 93, 92, False, "Tahoma" ) )
		self.bGenerateNPC.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bGenerateNPC.SetBackgroundColour( wx.Colour( 0, 0, 160 ) )
		
		bSizer635.Add( self.bGenerateNPC, 1, wx.SHAPED, 4 )
		
		
		gSizer1.Add( bSizer635, 1, wx.SHAPED, 5 )
		
		
		bSizer155.Add( gSizer1, 0, 0, 0 )
		
		bSizer156 = wx.BoxSizer( wx.VERTICAL )
		
		self.txStatBlock = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1, 150 ), wx.TE_MULTILINE|wx.TE_READONLY )
		self.txStatBlock.SetMaxLength( 0 ) 
		bSizer156.Add( self.txStatBlock, 0, wx.EXPAND|wx.EXPAND, 0 )
		
		
		bSizer155.Add( bSizer156, 0, wx.EXPAND|wx.EXPAND, 0 )
		
		bSizer157 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ID_OK = wx.Button( self, wx.ID_ANY, u"Add to Text", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_OK.SetDefault() 
		self.ID_OK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_OK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.ID_OK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer157.Add( self.ID_OK, 0, wx.RIGHT, 2 )
		
		self.ID_CANCEL = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_CANCEL.SetDefault() 
		self.ID_CANCEL.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_CANCEL.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ID_CANCEL.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		
		bSizer157.Add( self.ID_CANCEL, 0, wx.LEFT|wx.RIGHT, 2 )
		
		self.bHelp = wx.Button( self, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bHelp.SetDefault() 
		self.bHelp.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bHelp.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bHelp.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer157.Add( self.bHelp, 0, wx.LEFT, 2 )
		
		
		bSizer155.Add( bSizer157, 0, wx.ALIGN_CENTRE, 0 )
		
		
		self.SetSizer( bSizer155 )
		self.Layout()
		bSizer155.Fit( self )
		
		# Connect Events
		self.cbClass1Random.Bind( wx.EVT_CHECKBOX, self.OnCheckbox_cbClass1Random )
		self.cbClass3Random.Bind( wx.EVT_CHECKBOX, self.OnCheckbox_cbClass3Random )
		self.cbClass2Random.Bind( wx.EVT_CHECKBOX, self.OnCheckbox_cbClass2Random )
		self.bGenerateNPC.Bind( wx.EVT_BUTTON, self.GenerateNPC )
		self.ID_OK.Bind( wx.EVT_BUTTON, self.Add_NPC )
		self.ID_CANCEL.Bind( wx.EVT_BUTTON, self.OnCancel )
		self.bHelp.Bind( wx.EVT_BUTTON, self.OnHelp )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnCheckbox_cbClass1Random( self, event ):
		event.Skip()
	
	def OnCheckbox_cbClass3Random( self, event ):
		event.Skip()
	
	def OnCheckbox_cbClass2Random( self, event ):
		event.Skip()
	
	def GenerateNPC( self, event ):
		event.Skip()
	
	def Add_NPC( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		event.Skip()
	
	def OnHelp( self, event ):
		event.Skip()
	

###########################################################################
## Class SRD_Progress_DialogBase
###########################################################################

class SRD_Progress_DialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Loading Encounter Resource Files", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION|wx.SIMPLE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer188 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer328 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stTraps = wx.StaticText( self, wx.ID_ANY, u"Traps File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stTraps.Wrap( -1 )
		bSizer328.Add( self.stTraps, 1, 0, 0 )
		
		self.gTrapsGauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 200,15 ), wx.GA_HORIZONTAL|wx.GA_SMOOTH )
		self.gTrapsGauge.SetValue( 0 ) 
		self.gTrapsGauge.SetForegroundColour( wx.Colour( 0, 255, 0 ) )
		self.gTrapsGauge.SetBackgroundColour( wx.Colour( 202, 0, 0 ) )
		
		bSizer328.Add( self.gTrapsGauge, 0, wx.ALIGN_RIGHT, 0 )
		
		
		bSizer188.Add( bSizer328, 0, wx.ALL|wx.EXPAND, 2 )
		
		bSizer329 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stMonster = wx.StaticText( self, wx.ID_ANY, u"Monster File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stMonster.Wrap( -1 )
		bSizer329.Add( self.stMonster, 1, 0, 0 )
		
		self.gMonsterGauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 200,15 ), wx.GA_HORIZONTAL|wx.GA_SMOOTH )
		self.gMonsterGauge.SetValue( 0 ) 
		self.gMonsterGauge.SetForegroundColour( wx.Colour( 0, 255, 0 ) )
		self.gMonsterGauge.SetBackgroundColour( wx.Colour( 202, 0, 0 ) )
		
		bSizer329.Add( self.gMonsterGauge, 0, 0, 0 )
		
		
		bSizer188.Add( bSizer329, 0, wx.ALL|wx.EXPAND, 2 )
		
		bSizer330 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stSpells = wx.StaticText( self, wx.ID_ANY, u"Spells File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stSpells.Wrap( -1 )
		bSizer330.Add( self.stSpells, 1, 0, 0 )
		
		self.gSpellsGauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 200,15 ), wx.GA_HORIZONTAL|wx.GA_SMOOTH )
		self.gSpellsGauge.SetValue( 0 ) 
		self.gSpellsGauge.SetForegroundColour( wx.Colour( 0, 255, 0 ) )
		self.gSpellsGauge.SetBackgroundColour( wx.Colour( 202, 0, 0 ) )
		
		bSizer330.Add( self.gSpellsGauge, 0, 0, 0 )
		
		
		bSizer188.Add( bSizer330, 0, wx.ALL|wx.EXPAND, 2 )
		
		bSizer331 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stFeats = wx.StaticText( self, wx.ID_ANY, u"Feats File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stFeats.Wrap( -1 )
		bSizer331.Add( self.stFeats, 1, 0, 0 )
		
		self.gFeatsGauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 200,15 ), wx.GA_HORIZONTAL|wx.GA_SMOOTH )
		self.gFeatsGauge.SetValue( 0 ) 
		self.gFeatsGauge.SetForegroundColour( wx.Colour( 0, 255, 0 ) )
		self.gFeatsGauge.SetBackgroundColour( wx.Colour( 202, 0, 0 ) )
		
		bSizer331.Add( self.gFeatsGauge, 0, wx.ALIGN_RIGHT, 0 )
		
		
		bSizer188.Add( bSizer331, 0, wx.ALL|wx.EXPAND, 2 )
		
		bSizer332 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stClassSkills = wx.StaticText( self, wx.ID_ANY, u"Class Skills File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stClassSkills.Wrap( -1 )
		bSizer332.Add( self.stClassSkills, 1, 0, 0 )
		
		self.gClassSkillsGauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 200,15 ), wx.GA_HORIZONTAL|wx.GA_SMOOTH )
		self.gClassSkillsGauge.SetValue( 0 ) 
		self.gClassSkillsGauge.SetForegroundColour( wx.Colour( 0, 255, 0 ) )
		self.gClassSkillsGauge.SetBackgroundColour( wx.Colour( 202, 0, 0 ) )
		
		bSizer332.Add( self.gClassSkillsGauge, 0, 0, 0 )
		
		
		bSizer188.Add( bSizer332, 0, wx.ALL|wx.EXPAND, 2 )
		
		bSizer333 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stClassTable = wx.StaticText( self, wx.ID_ANY, u"Class Table File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stClassTable.Wrap( -1 )
		bSizer333.Add( self.stClassTable, 1, 0, 0 )
		
		self.gClassTableGauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 200,15 ), wx.GA_HORIZONTAL|wx.GA_SMOOTH )
		self.gClassTableGauge.SetValue( 0 ) 
		self.gClassTableGauge.SetForegroundColour( wx.Colour( 0, 255, 0 ) )
		self.gClassTableGauge.SetBackgroundColour( wx.Colour( 202, 0, 0 ) )
		
		bSizer333.Add( self.gClassTableGauge, 0, wx.ALIGN_RIGHT, 0 )
		
		
		bSizer188.Add( bSizer333, 0, wx.ALL|wx.EXPAND, 2 )
		
		bSizer334 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stNames = wx.StaticText( self, wx.ID_ANY, u"Names File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stNames.Wrap( -1 )
		bSizer334.Add( self.stNames, 1, 0, 0 )
		
		self.gNamesGauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 200,15 ), wx.GA_HORIZONTAL|wx.GA_SMOOTH )
		self.gNamesGauge.SetValue( 0 ) 
		self.gNamesGauge.SetForegroundColour( wx.Colour( 0, 255, 0 ) )
		self.gNamesGauge.SetBackgroundColour( wx.Colour( 202, 0, 0 ) )
		
		bSizer334.Add( self.gNamesGauge, 0, 0, 0 )
		
		
		bSizer188.Add( bSizer334, 0, wx.ALL|wx.EXPAND, 2 )
		
		bSizer335 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stRaces = wx.StaticText( self, wx.ID_ANY, u"Races File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stRaces.Wrap( -1 )
		bSizer335.Add( self.stRaces, 1, 0, 0 )
		
		self.gRacesGauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 200,15 ), wx.GA_HORIZONTAL|wx.GA_SMOOTH )
		self.gRacesGauge.SetValue( 0 ) 
		self.gRacesGauge.SetForegroundColour( wx.Colour( 0, 255, 0 ) )
		self.gRacesGauge.SetBackgroundColour( wx.Colour( 202, 0, 0 ) )
		
		bSizer335.Add( self.gRacesGauge, 0, 0, 0 )
		
		
		bSizer188.Add( bSizer335, 0, wx.ALL|wx.EXPAND, 2 )
		
		bSizer336 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stRacialBonuses = wx.StaticText( self, wx.ID_ANY, u"Racial Bonuses File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stRacialBonuses.Wrap( -1 )
		bSizer336.Add( self.stRacialBonuses, 1, 0, 0 )
		
		self.gRacialBonusesGauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 200,15 ), wx.GA_HORIZONTAL|wx.GA_SMOOTH )
		self.gRacialBonusesGauge.SetValue( 0 ) 
		self.gRacialBonusesGauge.SetForegroundColour( wx.Colour( 0, 255, 0 ) )
		self.gRacialBonusesGauge.SetBackgroundColour( wx.Colour( 202, 0, 0 ) )
		
		bSizer336.Add( self.gRacialBonusesGauge, 0, 0, 0 )
		
		
		bSizer188.Add( bSizer336, 0, wx.ALL|wx.EXPAND, 2 )
		
		
		self.SetSizer( bSizer188 )
		self.Layout()
		bSizer188.Fit( self )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class MonsterHoverBase
###########################################################################

class MonsterHoverBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Monster Information", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.Size( 630,-1 ), wx.DefaultSize )
		
		szMain = wx.BoxSizer( wx.VERTICAL )
		
		bSizer596 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer97 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer89 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bCalculateHP = wx.Button( self, wx.ID_ANY, u"HP:", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.bCalculateHP.SetBackgroundColour( wx.Colour( 151, 196, 179 ) )
		self.bCalculateHP.SetToolTip( u"Click to recalculate HP total based on hit dice" )
		
		bSizer89.Add( self.bCalculateHP, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spHitPoints = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), wx.SP_ARROW_KEYS, -10, 9999, 6 )
		self.spHitPoints.SetToolTip( u"Monster Hit Points" )
		
		bSizer89.Add( self.spHitPoints, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 3 )
		
		self.bSubtract1HP = wx.Button( self, wx.ID_ANY, u"-1", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.bSubtract1HP.SetBackgroundColour( wx.Colour( 255, 255, 191 ) )
		self.bSubtract1HP.SetToolTip( u"-1 HP" )
		
		bSizer89.Add( self.bSubtract1HP, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.bSubtract5HP = wx.Button( self, wx.ID_ANY, u"-5", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.bSubtract5HP.SetBackgroundColour( wx.Colour( 224, 172, 101 ) )
		self.bSubtract5HP.SetToolTip( u"-5 HP" )
		
		bSizer89.Add( self.bSubtract5HP, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.bSubtract10HP = wx.Button( self, wx.ID_ANY, u"-10", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.bSubtract10HP.SetBackgroundColour( wx.Colour( 224, 141, 120 ) )
		self.bSubtract10HP.SetToolTip( u"-10 HP" )
		
		bSizer89.Add( self.bSubtract10HP, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.bSubtract20HP = wx.Button( self, wx.ID_ANY, u"-20", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.bSubtract20HP.SetBackgroundColour( wx.Colour( 255, 100, 100 ) )
		self.bSubtract20HP.SetToolTip( u"-20 HP" )
		
		bSizer89.Add( self.bSubtract20HP, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.stStartHP = wx.StaticText( self, wx.ID_ANY, u"0 HP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stStartHP.Wrap( -1 )
		self.stStartHP.SetToolTip( u"Starting HP" )
		
		bSizer89.Add( self.stStartHP, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer97.Add( bSizer89, 0, 0, 5 )
		
		bSizer891 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer524 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stArmorClass = wx.StaticText( self, wx.ID_ANY, u"AC", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stArmorClass.Wrap( -1 )
		bSizer524.Add( self.stArmorClass, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		self.spArmorClass = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 1, 999, 10 )
		self.spArmorClass.SetToolTip( u"Monster Armor Class" )
		
		bSizer524.Add( self.spArmorClass, 0, wx.ALL, 3 )
		
		
		bSizer891.Add( bSizer524, 1, wx.EXPAND, 5 )
		
		bSizer525 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer520 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stXPvalue = wx.StaticText( self, wx.ID_ANY, u"0 XP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stXPvalue.Wrap( -1 )
		bSizer520.Add( self.stXPvalue, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer525.Add( bSizer520, 1, wx.ALIGN_CENTER, 5 )
		
		
		bSizer891.Add( bSizer525, 1, wx.EXPAND, 5 )
		
		bSizer526 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer523 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stPassivePerception = wx.StaticText( self, wx.ID_ANY, u"PP: 10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stPassivePerception.Wrap( -1 )
		self.stPassivePerception.SetToolTip( u"Passive Perception" )
		
		bSizer523.Add( self.stPassivePerception, 1, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer526.Add( bSizer523, 1, wx.ALIGN_CENTER, 5 )
		
		
		bSizer891.Add( bSizer526, 1, wx.EXPAND, 5 )
		
		
		bSizer97.Add( bSizer891, 0, 0, 5 )
		
		bSizer518 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stSpeed = wx.StaticText( self, wx.ID_ANY, u"Speed:  0'", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stSpeed.Wrap( -1 )
		bSizer518.Add( self.stSpeed, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer97.Add( bSizer518, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer660 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stDeathSaves = wx.StaticText( self, wx.ID_ANY, u"Death Saves:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stDeathSaves.Wrap( -1 )
		bSizer660.Add( self.stDeathSaves, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sbSizer84 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Pass" ), wx.HORIZONTAL )
		
		self.cbDeathSavePass1 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer84.Add( self.cbDeathSavePass1, 0, 0, 5 )
		
		self.cbDeathSavePass2 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer84.Add( self.cbDeathSavePass2, 0, 0, 5 )
		
		self.cbDeathSavePass3 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer84.Add( self.cbDeathSavePass3, 0, 0, 5 )
		
		
		bSizer660.Add( sbSizer84, 1, wx.EXPAND, 5 )
		
		sbSizer85 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Fail" ), wx.HORIZONTAL )
		
		self.cbDeathSaveFail1 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer85.Add( self.cbDeathSaveFail1, 0, 0, 5 )
		
		self.cbDeathSaveFail2 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer85.Add( self.cbDeathSaveFail2, 0, 0, 5 )
		
		self.cbDeathSaveFail3 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer85.Add( self.cbDeathSaveFail3, 0, 0, 5 )
		
		
		bSizer660.Add( sbSizer85, 1, wx.EXPAND, 5 )
		
		
		bSizer97.Add( bSizer660, 0, 0, 5 )
		
		
		bSizer596.Add( bSizer97, 0, wx.EXPAND, 5 )
		
		sbSizer13 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Conditions" ), wx.VERTICAL )
		
		gSizer2 = wx.GridSizer( 2, 2, 0, 0 )
		
		cxCondition1Choices = [ u"None", u"Blinded", u"Charmed", u"Concentrating", u"Deafened", u"Frightened", u"Grappled", u"Incapacitated", u"Invisible", u"Paralyzed", u"Petrified", u"Poisoned", u"Prone", u"Restrained", u"Stunned", u"Turned", u"Unconscious" ]
		self.cxCondition1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cxCondition1Choices, 0 )
		self.cxCondition1.SetSelection( 0 )
		gSizer2.Add( self.cxCondition1, 0, 0, 5 )
		
		cxCondition2Choices = [ u"None", u"Blinded", u"Charmed", u"Concentrating", u"Deafened", u"Frightened", u"Grappled", u"Incapacitated", u"Invisible", u"Paralyzed", u"Petrified", u"Poisoned", u"Prone", u"Restrained", u"Stunned", u"Turned", u"Unconscious" ]
		self.cxCondition2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cxCondition2Choices, 0 )
		self.cxCondition2.SetSelection( 0 )
		gSizer2.Add( self.cxCondition2, 0, 0, 5 )
		
		cxCondition3Choices = [ u"None", u"Blinded", u"Charmed", u"Concentrating", u"Deafened", u"Frightened", u"Grappled", u"Incapacitated", u"Invisible", u"Paralyzed", u"Petrified", u"Poisoned", u"Prone", u"Restrained", u"Stunned", u"Turned", u"Unconscious" ]
		self.cxCondition3 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cxCondition3Choices, 0 )
		self.cxCondition3.SetSelection( 0 )
		gSizer2.Add( self.cxCondition3, 0, 0, 5 )
		
		cxCondition4Choices = [ u"None", u"Blinded", u"Charmed", u"Concentrating", u"Deafened", u"Frightened", u"Grappled", u"Incapacitated", u"Invisible", u"Paralyzed", u"Petrified", u"Poisoned", u"Prone", u"Restrained", u"Stunned", u"Turned", u"Unconscious" ]
		self.cxCondition4 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cxCondition4Choices, 0 )
		self.cxCondition4.SetSelection( 0 )
		gSizer2.Add( self.cxCondition4, 0, 0, 5 )
		
		self.bRenameMonster = wx.Button( self, wx.ID_ANY, u"Rename...", wx.DefaultPosition, wx.Size( -1,-1 ), wx.BU_EXACTFIT )
		gSizer2.Add( self.bRenameMonster, 0, 0, 5 )
		
		
		sbSizer13.Add( gSizer2, 0, 0, 5 )
		
		
		bSizer596.Add( sbSizer13, 0, wx.ALL, 3 )
		
		sbSizer87 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Icon Image" ), wx.VERTICAL )
		
		self.bCustomImage = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/monster_icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 100,100 ), wx.BU_AUTODRAW )
		self.bCustomImage.SetToolTip( u"Click to change the monster image..." )
		
		sbSizer87.Add( self.bCustomImage, 0, 0, 0 )
		
		
		bSizer596.Add( sbSizer87, 0, 0, 0 )
		
		
		szMain.Add( bSizer596, 0, wx.EXPAND, 5 )
		
		bSizer94 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stAbilityScores1 = wx.StaticText( self, wx.ID_ANY, u"STR: 18(+4) DEX: 18(+4) INT: 18(+4)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stAbilityScores1.Wrap( -1 )
		bSizer94.Add( self.stAbilityScores1, 0, wx.ALL, 3 )
		
		self.stAbilityScores2 = wx.StaticText( self, wx.ID_ANY, u"CON: 18(+4)  WIS: 18(+4)  CHA: 18(+4)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stAbilityScores2.Wrap( -1 )
		bSizer94.Add( self.stAbilityScores2, 0, wx.ALL, 3 )
		
		
		szMain.Add( bSizer94, 0, wx.EXPAND, 5 )
		
		sbSizer89 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Actions (yellow) and Legendary Actions (red)" ), wx.VERTICAL )
		
		bSizer519 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txActions = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2|wx.TE_WORDWRAP )
		self.txActions.SetMinSize( wx.Size( -1,125 ) )
		
		bSizer519.Add( self.txActions, 1, wx.EXPAND, 5 )
		
		
		sbSizer89.Add( bSizer519, 0, wx.EXPAND, 5 )
		
		
		szMain.Add( sbSizer89, 0, wx.EXPAND, 5 )
		
		bSizer595 = wx.BoxSizer( wx.VERTICAL )
		
		self.nbInformationTabs = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_MULTILINE )
		self.nbInformationTabs.SetMinSize( wx.Size( -1,100 ) )
		
		self.pnTraits = wx.Panel( self.nbInformationTabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer519114 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txTraits = wx.TextCtrl( self.pnTraits, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2|wx.TE_WORDWRAP|wx.NO_BORDER )
		self.txTraits.SetMinSize( wx.Size( -1,125 ) )
		
		bSizer519114.Add( self.txTraits, 1, wx.ALL|wx.EXPAND, 2 )
		
		
		self.pnTraits.SetSizer( bSizer519114 )
		self.pnTraits.Layout()
		bSizer519114.Fit( self.pnTraits )
		self.nbInformationTabs.AddPage( self.pnTraits, u"Traits", True )
		self.pnSkills = wx.Panel( self.nbInformationTabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5191111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txSkills = wx.TextCtrl( self.pnSkills, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2|wx.TE_WORDWRAP|wx.NO_BORDER )
		bSizer5191111.Add( self.txSkills, 1, wx.ALL|wx.EXPAND, 2 )
		
		
		self.pnSkills.SetSizer( bSizer5191111 )
		self.pnSkills.Layout()
		bSizer5191111.Fit( self.pnSkills )
		self.nbInformationTabs.AddPage( self.pnSkills, u"Skills", False )
		self.pnIdeals = wx.Panel( self.nbInformationTabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer519111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txIdeals = wx.TextCtrl( self.pnIdeals, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2|wx.TE_WORDWRAP|wx.NO_BORDER )
		bSizer519111.Add( self.txIdeals, 1, wx.ALL|wx.EXPAND, 2 )
		
		
		self.pnIdeals.SetSizer( bSizer519111 )
		self.pnIdeals.Layout()
		bSizer519111.Fit( self.pnIdeals )
		self.nbInformationTabs.AddPage( self.pnIdeals, u"Ideals", False )
		self.pnBonds = wx.Panel( self.nbInformationTabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer519112 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txBonds = wx.TextCtrl( self.pnBonds, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2|wx.TE_WORDWRAP|wx.NO_BORDER )
		bSizer519112.Add( self.txBonds, 1, wx.ALL|wx.EXPAND, 2 )
		
		
		self.pnBonds.SetSizer( bSizer519112 )
		self.pnBonds.Layout()
		bSizer519112.Fit( self.pnBonds )
		self.nbInformationTabs.AddPage( self.pnBonds, u"Bonds", False )
		self.pnFlaws = wx.Panel( self.nbInformationTabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer519113 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txFlaws = wx.TextCtrl( self.pnFlaws, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2|wx.TE_WORDWRAP|wx.NO_BORDER )
		bSizer519113.Add( self.txFlaws, 1, wx.ALL|wx.EXPAND, 2 )
		
		
		self.pnFlaws.SetSizer( bSizer519113 )
		self.pnFlaws.Layout()
		bSizer519113.Fit( self.pnFlaws )
		self.nbInformationTabs.AddPage( self.pnFlaws, u"Flaws", False )
		self.pnOther = wx.Panel( self.nbInformationTabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer51911 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txOther = wx.TextCtrl( self.pnOther, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2|wx.TE_WORDWRAP|wx.NO_BORDER )
		bSizer51911.Add( self.txOther, 1, wx.ALL|wx.EXPAND, 2 )
		
		
		self.pnOther.SetSizer( bSizer51911 )
		self.pnOther.Layout()
		bSizer51911.Fit( self.pnOther )
		self.nbInformationTabs.AddPage( self.pnOther, u"Other", False )
		self.pnNotes = wx.Panel( self.nbInformationTabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer519115 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.txNotes = wx.TextCtrl( self.pnNotes, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_RICH2|wx.TE_WORDWRAP )
		bSizer519115.Add( self.txNotes, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.pnNotes.SetSizer( bSizer519115 )
		self.pnNotes.Layout()
		bSizer519115.Fit( self.pnNotes )
		self.nbInformationTabs.AddPage( self.pnNotes, u"Notes", False )
		
		bSizer595.Add( self.nbInformationTabs, 1, wx.EXPAND, 0 )
		
		
		szMain.Add( bSizer595, 1, wx.EXPAND, 5 )
		
		bSizer584 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer600 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stSpellLabel = wx.StaticText( self, wx.ID_ANY, u"Available Spells", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stSpellLabel.Wrap( -1 )
		bSizer600.Add( self.stSpellLabel, 2, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.stSpellDescription = wx.StaticText( self, wx.ID_ANY, u"Spell Description", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stSpellDescription.Wrap( -1 )
		bSizer600.Add( self.stSpellDescription, 3, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		bSizer584.Add( bSizer600, 0, wx.EXPAND, 5 )
		
		bSizer599 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.tcSpellTree = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,100 ), wx.TR_DEFAULT_STYLE )
		bSizer599.Add( self.tcSpellTree, 2, wx.EXPAND, 1 )
		
		self.txSpells = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,125 ), wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2|wx.TE_WORDWRAP )
		bSizer599.Add( self.txSpells, 3, wx.EXPAND, 5 )
		
		
		bSizer584.Add( bSizer599, 1, wx.EXPAND, 5 )
		
		
		szMain.Add( bSizer584, 1, wx.ALL|wx.EXPAND|wx.FIXED_MINSIZE, 5 )
		
		
		self.SetSizer( szMain )
		self.Layout()
		szMain.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.bCalculateHP.Bind( wx.EVT_BUTTON, self.CalculateHPTotal )
		self.bSubtract1HP.Bind( wx.EVT_BUTTON, self.OnSubtract1HP )
		self.bSubtract5HP.Bind( wx.EVT_BUTTON, self.OnSubtract5HP )
		self.bSubtract10HP.Bind( wx.EVT_BUTTON, self.OnSubtract10HP )
		self.bSubtract20HP.Bind( wx.EVT_BUTTON, self.OnSubtract20HP )
		self.bRenameMonster.Bind( wx.EVT_BUTTON, self.OnRenameMonster )
		self.bCustomImage.Bind( wx.EVT_BUTTON, self.OnSelectCustomImage )
		self.tcSpellTree.Bind( wx.EVT_TREE_SEL_CHANGED, self.SelectSpell )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def CalculateHPTotal( self, event ):
		event.Skip()
	
	def OnSubtract1HP( self, event ):
		event.Skip()
	
	def OnSubtract5HP( self, event ):
		event.Skip()
	
	def OnSubtract10HP( self, event ):
		event.Skip()
	
	def OnSubtract20HP( self, event ):
		event.Skip()
	
	def OnRenameMonster( self, event ):
		event.Skip()
	
	def OnSelectCustomImage( self, event ):
		event.Skip()
	
	def SelectSpell( self, event ):
		event.Skip()
	

###########################################################################
## Class MonstersDialogBase
###########################################################################

class MonstersDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pathfinder / d20 / 3.5 Edition Monsters", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer158 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer159 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer160 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer367 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer160.Add( bSizer367, 1, wx.EXPAND, 5 )
		
		
		bSizer159.Add( bSizer160, 1, wx.EXPAND|wx.LEFT|wx.TOP, 5 )
		
		bSizer161 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer165 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer166 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer162 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer163 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText84 = wx.StaticText( self, wx.ID_ANY, u"Monster Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText84.Wrap( -1 )
		bSizer163.Add( self.m_staticText84, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.txFamily = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.txFamily.SetMaxLength( 0 ) 
		bSizer163.Add( self.txFamily, 0, wx.LEFT, 3 )
		
		
		bSizer162.Add( bSizer163, 0, wx.BOTTOM, 5 )
		
		bSizer164 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText85 = wx.StaticText( self, wx.ID_ANY, u"Monster Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText85.Wrap( -1 )
		bSizer164.Add( self.m_staticText85, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 3 )
		
		self.txName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.txName.SetMaxLength( 0 ) 
		bSizer164.Add( self.txName, 0, 0, 0 )
		
		
		bSizer162.Add( bSizer164, 0, 0, 0 )
		
		
		bSizer166.Add( bSizer162, 0, wx.ALL, 5 )
		
		bSizer167 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText283 = wx.StaticText( self, wx.ID_ANY, u"Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText283.Wrap( -1 )
		bSizer167.Add( self.m_staticText283, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		cbxTypeChoices = []
		self.cbxType = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), cbxTypeChoices, 0 )
		bSizer167.Add( self.cbxType, 0, 0, 0 )
		
		
		bSizer166.Add( bSizer167, 0, wx.ALL, 2 )
		
		bSizer168 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText284 = wx.StaticText( self, wx.ID_ANY, u"Size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText284.Wrap( -1 )
		bSizer168.Add( self.m_staticText284, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		cbxSizeChoices = []
		self.cbxSize = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), cbxSizeChoices, 0 )
		bSizer168.Add( self.cbxSize, 0, wx.LEFT, 3 )
		
		
		bSizer166.Add( bSizer168, 0, wx.ALL, 2 )
		
		bSizer169 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText285 = wx.StaticText( self, wx.ID_ANY, u"Challenge Rating:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText285.Wrap( -1 )
		bSizer169.Add( self.m_staticText285, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txChallengeRating = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.txChallengeRating.SetMaxLength( 0 ) 
		bSizer169.Add( self.txChallengeRating, 0, wx.LEFT, 3 )
		
		
		bSizer166.Add( bSizer169, 0, wx.ALL, 2 )
		
		bSizer183 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText103 = wx.StaticText( self, wx.ID_ANY, u"Alignment:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText103.Wrap( -1 )
		bSizer183.Add( self.m_staticText103, 1, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
		
		self.txAlignment = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.txAlignment.SetMaxLength( 0 ) 
		bSizer183.Add( self.txAlignment, 0, 0, 0 )
		
		
		bSizer166.Add( bSizer183, 0, wx.LEFT, 3 )
		
		bSizer171 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer1711 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText891 = wx.StaticText( self, wx.ID_ANY, u"Hit Points:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText891.Wrap( -1 )
		bSizer1711.Add( self.m_staticText891, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.spHitPoints = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 55,-1 ), wx.SP_ARROW_KEYS, 0, 9999, 888 )
		bSizer1711.Add( self.spHitPoints, 0, wx.ALL, 5 )
		
		
		bSizer171.Add( bSizer1711, 0, wx.EXPAND, 5 )
		
		bSizer533 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText89 = wx.StaticText( self, wx.ID_ANY, u"HD:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText89.Wrap( -1 )
		bSizer533.Add( self.m_staticText89, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.txHitDice = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.txHitDice.SetMaxLength( 0 ) 
		self.txHitDice.SetToolTip( u"Monster Hit Dice, ie 7d8+10" )
		
		bSizer533.Add( self.txHitDice, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer171.Add( bSizer533, 1, wx.EXPAND, 5 )
		
		
		bSizer166.Add( bSizer171, 0, wx.ALL|wx.EXPAND|wx.EXPAND, 3 )
		
		bSizer172 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText90 = wx.StaticText( self, wx.ID_ANY, u"Initiative:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText90.Wrap( -1 )
		bSizer172.Add( self.m_staticText90, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.spInitiative = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, -1, 99,  )
		bSizer172.Add( self.spInitiative, 0, wx.LEFT, 14 )
		
		
		bSizer166.Add( bSizer172, 0, wx.ALL|wx.EXPAND|wx.EXPAND, 3 )
		
		bSizer173 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText91 = wx.StaticText( self, wx.ID_ANY, u"Speed:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )
		bSizer173.Add( self.m_staticText91, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.txSpeed = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.txSpeed.SetMaxLength( 0 ) 
		bSizer173.Add( self.txSpeed, 1, wx.EXPAND|wx.LEFT, 14 )
		
		
		bSizer166.Add( bSizer173, 0, wx.ALL|wx.EXPAND, 3 )
		
		bSizer174 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText92 = wx.StaticText( self, wx.ID_ANY, u"Armor Class:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText92.Wrap( -1 )
		bSizer174.Add( self.m_staticText92, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.txArmorClass = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.txArmorClass.SetMaxLength( 0 ) 
		bSizer174.Add( self.txArmorClass, 1, wx.EXPAND|wx.LEFT, 3 )
		
		
		bSizer166.Add( bSizer174, 0, wx.ALL|wx.EXPAND, 3 )
		
		
		bSizer165.Add( bSizer166, 0, 0, 0 )
		
		bSizer534 = wx.BoxSizer( wx.VERTICAL )
		
		self.pnFilterPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer89 = wx.StaticBoxSizer( wx.StaticBox( self.pnFilterPanel, wx.ID_ANY, u"Filters" ), wx.VERTICAL )
		
		bSizer518 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer525 = wx.BoxSizer( wx.VERTICAL )
		
		self.cbFilterByCR = wx.CheckBox( self.pnFilterPanel, wx.ID_ANY, u"CR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbFilterByCR.SetToolTip( u"Check to filter by Challenge Rating" )
		
		bSizer525.Add( self.cbFilterByCR, 0, wx.ALL, 5 )
		
		lbCRFilterChoices = [ u"<1", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10", u"11", u"12", u"13", u"14", u"15", u"16", u"17", u"18", u"19", u"20+" ]
		self.lbCRFilter = wx.ListBox( self.pnFilterPanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 50,-1 ), lbCRFilterChoices, wx.LB_MULTIPLE )
		self.lbCRFilter.Enable( False )
		self.lbCRFilter.SetToolTip( u"Select CR to filter" )
		
		bSizer525.Add( self.lbCRFilter, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer518.Add( bSizer525, 0, wx.EXPAND, 5 )
		
		bSizer526 = wx.BoxSizer( wx.VERTICAL )
		
		self.cbFilterByMonsterType = wx.CheckBox( self.pnFilterPanel, wx.ID_ANY, u"Monster Type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbFilterByMonsterType.SetToolTip( u"Check to filter by Monster Type" )
		
		bSizer526.Add( self.cbFilterByMonsterType, 0, wx.ALL, 5 )
		
		lbMonsterFilterChoices = [ u"Aberration", u"Beast", u"Celestial", u"Construct", u"Dragon", u"Elemental", u"Fey", u"Fiend", u"Giant", u"Humanoid", u"Monstrosity", u"Ooze", u"Plant", u"Undead" ]
		self.lbMonsterFilter = wx.ListBox( self.pnFilterPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lbMonsterFilterChoices, wx.LB_MULTIPLE )
		self.lbMonsterFilter.Enable( False )
		self.lbMonsterFilter.SetToolTip( u"Select monster to filter" )
		
		bSizer526.Add( self.lbMonsterFilter, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer518.Add( bSizer526, 0, wx.EXPAND, 5 )
		
		
		sbSizer89.Add( bSizer518, 1, wx.EXPAND, 5 )
		
		
		self.pnFilterPanel.SetSizer( sbSizer89 )
		self.pnFilterPanel.Layout()
		sbSizer89.Fit( self.pnFilterPanel )
		bSizer534.Add( self.pnFilterPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer165.Add( bSizer534, 1, wx.EXPAND, 5 )
		
		
		bSizer161.Add( bSizer165, 0, wx.ALL|wx.EXPAND, 3 )
		
		bSizer175 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText93 = wx.StaticText( self, wx.ID_ANY, u"Base Attack:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText93.Wrap( -1 )
		bSizer175.Add( self.m_staticText93, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.txBaseAttack = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.txBaseAttack.SetMaxLength( 0 ) 
		bSizer175.Add( self.txBaseAttack, 0, 0, 0 )
		
		self.m_staticText94 = wx.StaticText( self, wx.ID_ANY, u"Grapple:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText94.Wrap( 0 )
		bSizer175.Add( self.m_staticText94, 0, wx.LEFT|wx.ALIGN_CENTRE_VERTICAL, 15 )
		
		self.txGrapple = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.txGrapple.SetMaxLength( 0 ) 
		bSizer175.Add( self.txGrapple, 0, 0, 0 )
		
		
		bSizer161.Add( bSizer175, 0, wx.ALL|wx.EXPAND|wx.EXPAND, 3 )
		
		bSizer178 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText97 = wx.StaticText( self, wx.ID_ANY, u"Space:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText97.Wrap( -1 )
		bSizer178.Add( self.m_staticText97, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.txSpace = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.txSpace.SetMaxLength( 0 ) 
		bSizer178.Add( self.txSpace, 0, wx.LEFT|wx.EXPAND|wx.EXPAND, 3 )
		
		self.m_staticText98 = wx.StaticText( self, wx.ID_ANY, u"Reach:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText98.Wrap( 0 )
		bSizer178.Add( self.m_staticText98, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 15 )
		
		self.txReach = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.txReach.SetMaxLength( 0 ) 
		bSizer178.Add( self.txReach, 0, 0, 0 )
		
		
		bSizer161.Add( bSizer178, 0, wx.ALL|wx.EXPAND|wx.EXPAND, 3 )
		
		bSizer176 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText95 = wx.StaticText( self, wx.ID_ANY, u"Attack:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText95.Wrap( -1 )
		bSizer176.Add( self.m_staticText95, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.txAttack = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.txAttack.SetMaxLength( 0 ) 
		bSizer176.Add( self.txAttack, 1, wx.EXPAND|wx.LEFT, 5 )
		
		
		bSizer161.Add( bSizer176, 1, wx.ALL|wx.EXPAND, 3 )
		
		bSizer177 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText96 = wx.StaticText( self, wx.ID_ANY, u"Full Attack:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText96.Wrap( 0 )
		bSizer177.Add( self.m_staticText96, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.txFullAttack = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,50 ), wx.TE_MULTILINE )
		self.txFullAttack.SetMaxLength( 0 ) 
		bSizer177.Add( self.txFullAttack, 1, wx.EXPAND|wx.LEFT, 4 )
		
		
		bSizer161.Add( bSizer177, 1, wx.ALL|wx.EXPAND, 3 )
		
		bSizer179 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText99 = wx.StaticText( self, wx.ID_ANY, u"Special Attacks:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText99.Wrap( 0 )
		bSizer179.Add( self.m_staticText99, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.txSpecialAttacks = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,50 ), wx.TE_MULTILINE )
		self.txSpecialAttacks.SetMaxLength( 0 ) 
		bSizer179.Add( self.txSpecialAttacks, 1, wx.EXPAND|wx.LEFT, 3 )
		
		
		bSizer161.Add( bSizer179, 0, wx.ALL|wx.EXPAND, 3 )
		
		bSizer180 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText100 = wx.StaticText( self, wx.ID_ANY, u"Special Qualities:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText100.Wrap( 0 )
		bSizer180.Add( self.m_staticText100, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.txSpecialQualities = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,50 ), wx.TE_MULTILINE )
		self.txSpecialQualities.SetMaxLength( 0 ) 
		bSizer180.Add( self.txSpecialQualities, 1, wx.EXPAND|wx.LEFT, 3 )
		
		
		bSizer161.Add( bSizer180, 1, wx.ALL|wx.EXPAND, 3 )
		
		bSizer181 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"Special Abilities:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( 0 )
		bSizer181.Add( self.m_staticText101, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.txSpecialAbilities = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,50 ), wx.TE_MULTILINE )
		self.txSpecialAbilities.SetMaxLength( 0 ) 
		bSizer181.Add( self.txSpecialAbilities, 1, wx.EXPAND|wx.LEFT, 3 )
		
		
		bSizer161.Add( bSizer181, 0, wx.EXPAND|wx.LEFT, 3 )
		
		bSizer182 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText102 = wx.StaticText( self, wx.ID_ANY, u"Treasure:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText102.Wrap( -1 )
		bSizer182.Add( self.m_staticText102, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.txTreasure = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.txTreasure.SetMaxLength( 0 ) 
		bSizer182.Add( self.txTreasure, 1, wx.EXPAND|wx.RIGHT, 3 )
		
		
		bSizer161.Add( bSizer182, 0, wx.ALL|wx.EXPAND, 3 )
		
		
		bSizer159.Add( bSizer161, 0, wx.EXPAND|wx.EXPAND, 0 )
		
		bApplyFilter = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bAddMonster = wx.Button( self, wx.ID_ANY, u"Add New Monster", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bAddMonster.SetDefault() 
		self.bAddMonster.SetToolTip( u"Add a new monster based on the values to the left." )
		
		bApplyFilter.Add( self.bAddMonster, 0, 0, 0 )
		
		self.bUpdateMonster = wx.Button( self, wx.ID_ANY, u"Update User Defined Monster", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bUpdateMonster.SetDefault() 
		self.bUpdateMonster.Enable( False )
		self.bUpdateMonster.SetToolTip( u"Update the monster selected in the list to the values above." )
		
		bApplyFilter.Add( self.bUpdateMonster, 0, wx.LEFT|wx.ALIGN_CENTRE_HORIZONTAL, 5 )
		
		self.bDeleteMonster = wx.Button( self, wx.ID_ANY, u"Delete Monster", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bDeleteMonster.SetDefault() 
		self.bDeleteMonster.Enable( False )
		self.bDeleteMonster.SetToolTip( u"Delete the currently selected monster." )
		
		bApplyFilter.Add( self.bDeleteMonster, 0, 0, 0 )
		
		
		bSizer159.Add( bApplyFilter, 0, wx.TOP|wx.EXPAND, 5 )
		
		bSizer185 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ID_OK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_OK.SetDefault() 
		self.ID_OK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_OK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.ID_OK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer185.Add( self.ID_OK, 0, wx.RIGHT, 2 )
		
		self.ID_CANCEL = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_CANCEL.SetDefault() 
		self.ID_CANCEL.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_CANCEL.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ID_CANCEL.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		
		bSizer185.Add( self.ID_CANCEL, 0, wx.LEFT|wx.RIGHT, 2 )
		
		self.bHelp = wx.Button( self, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bHelp.SetDefault() 
		self.bHelp.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bHelp.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bHelp.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer185.Add( self.bHelp, 0, wx.LEFT, 2 )
		
		
		bSizer159.Add( bSizer185, 0, wx.TOP|wx.ALIGN_CENTRE_HORIZONTAL, 10 )
		
		
		bSizer158.Add( bSizer159, 0, 0, 0 )
		
		bSizer186 = wx.BoxSizer( wx.VERTICAL )
		
		lbMonsterListChoices = []
		self.lbMonsterList = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 225,-1 ), lbMonsterListChoices, wx.LB_SINGLE )
		self.lbMonsterList.SetToolTip( u"List of Monsters" )
		
		bSizer186.Add( self.lbMonsterList, 1, wx.ALL|wx.EXPAND|wx.EXPAND, 3 )
		
		
		bSizer158.Add( bSizer186, 0, wx.LEFT|wx.EXPAND|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer158 )
		self.Layout()
		bSizer158.Fit( self )
		
		# Connect Events
		self.cbFilterByCR.Bind( wx.EVT_CHECKBOX, self.EnableFilterCR )
		self.lbCRFilter.Bind( wx.EVT_LISTBOX, self.FilterMonsterList )
		self.cbFilterByMonsterType.Bind( wx.EVT_CHECKBOX, self.EnableFilterMonsterType )
		self.lbMonsterFilter.Bind( wx.EVT_LISTBOX, self.FilterMonsterList )
		self.bAddMonster.Bind( wx.EVT_BUTTON, self.OnAddMonster )
		self.bUpdateMonster.Bind( wx.EVT_BUTTON, self.OnUpdateMonster )
		self.bDeleteMonster.Bind( wx.EVT_BUTTON, self.OnDeleteMonster )
		self.ID_OK.Bind( wx.EVT_BUTTON, self.OnOK )
		self.ID_CANCEL.Bind( wx.EVT_BUTTON, self.OnCancel )
		self.bHelp.Bind( wx.EVT_BUTTON, self.OnHelp )
		self.lbMonsterList.Bind( wx.EVT_LISTBOX, self.OnListbox_lbMonsterList )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def EnableFilterCR( self, event ):
		event.Skip()
	
	def FilterMonsterList( self, event ):
		event.Skip()
	
	def EnableFilterMonsterType( self, event ):
		event.Skip()
	
	
	def OnAddMonster( self, event ):
		event.Skip()
	
	def OnUpdateMonster( self, event ):
		event.Skip()
	
	def OnDeleteMonster( self, event ):
		event.Skip()
	
	def OnOK( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		event.Skip()
	
	def OnHelp( self, event ):
		event.Skip()
	
	def OnListbox_lbMonsterList( self, event ):
		event.Skip()
	

###########################################################################
## Class Monsters5E_DialogBase
###########################################################################

class Monsters5E_DialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Fifth Edition Monsters", pos = wx.DefaultPosition, size = wx.Size( 900,1000 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetToolTip( u"Click to change image..." )
		
		bSizer158 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer159 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer161 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer165 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer166 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer367 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stRecordType = wx.StaticText( self, wx.ID_ANY, u"Monster Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stRecordType.Wrap( -1 )
		bSizer367.Add( self.stRecordType, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 3 )
		
		self.txName = wx.TextCtrl( self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.txName.SetMaxLength( 0 ) 
		bSizer367.Add( self.txName, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		
		bSizer166.Add( bSizer367, 0, wx.EXPAND|wx.LEFT, 3 )
		
		bSizer623 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer624 = wx.BoxSizer( wx.VERTICAL )
		
		self.bbSelectCustomImage = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/npc_icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 100,100 ), wx.BU_AUTODRAW )
		self.bbSelectCustomImage.Enable( False )
		
		bSizer624.Add( self.bbSelectCustomImage, 0, 0, 5 )
		
		
		bSizer623.Add( bSizer624, 0, wx.EXPAND, 5 )
		
		bSizer598 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer167 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stTypeOrRace = wx.StaticText( self, wx.ID_ANY, u"Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stTypeOrRace.Wrap( -1 )
		bSizer167.Add( self.stTypeOrRace, 0, wx.ALL, 3 )
		
		chTypeChoices = [ u"Aberration", u"Beast", u"Celestial", u"Construct", u"Dragon", u"Elemental", u"Fey", u"Fiend", u"Giant", u"Humanoid", u"Monstrosity", u"Ooze", u"Plant", u"Undead" ]
		self.chType = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chTypeChoices, 0 )
		self.chType.SetSelection( 9 )
		self.chType.Hide()
		
		bSizer167.Add( self.chType, 0, wx.ALL, 2 )
		
		chRaceChoices = [ u"Human", u"Halfling", u"Elf", u"Half-Orc", u"Half-Elf", u"Gnome", u"Dwarf", u"Dragonborn", u"Orc", u"Goblin", u"Other" ]
		self.chRace = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chRaceChoices, 0 )
		self.chRace.SetSelection( 0 )
		self.chRace.Hide()
		
		bSizer167.Add( self.chRace, 0, wx.ALL, 2 )
		
		
		bSizer598.Add( bSizer167, 0, wx.ALL, 3 )
		
		bSizer168 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stClass = wx.StaticText( self, wx.ID_ANY, u"Class", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stClass.Wrap( -1 )
		self.stClass.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.stClass.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer168.Add( self.stClass, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		chClassChoices = [ u"Barbarian (d12)", u"Bard (d8)", u"Cleric (d8)", u"Druid (d8)", u"Fighter (d10)", u"Monk (d8)", u"Paladin (d10)", u"Ranger (d10)", u"Rogue (d8)", u"Sorcerer (d6)", u"Warlock (d8)", u"Wizard (d6)" ]
		self.chClass = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chClassChoices, 0 )
		self.chClass.SetSelection( 0 )
		bSizer168.Add( self.chClass, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )
		
		
		bSizer598.Add( bSizer168, 0, wx.LEFT, 5 )
		
		bSizer648 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText331 = wx.StaticText( self, wx.ID_ANY, u"Sub-Class", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText331.Wrap( -1 )
		bSizer648.Add( self.m_staticText331, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		chSubClassChoices = []
		self.chSubClass = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chSubClassChoices, 0 )
		self.chSubClass.SetSelection( 0 )
		self.chSubClass.SetMinSize( wx.Size( 200,-1 ) )
		
		bSizer648.Add( self.chSubClass, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer598.Add( bSizer648, 0, wx.EXPAND, 5 )
		
		bSizer625 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stSize = wx.StaticText( self, wx.ID_ANY, u"Size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stSize.Wrap( -1 )
		bSizer625.Add( self.stSize, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
		
		chSizeChoices = [ u"Tiny", u"Small", u"Medium", u"Large", u"Huge", u"Gargantuan" ]
		self.chSize = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chSizeChoices, 0 )
		self.chSize.SetSelection( 2 )
		bSizer625.Add( self.chSize, 0, wx.ALL, 2 )
		
		
		bSizer598.Add( bSizer625, 0, wx.EXPAND|wx.LEFT, 5 )
		
		
		bSizer623.Add( bSizer598, 0, wx.EXPAND, 5 )
		
		
		bSizer166.Add( bSizer623, 1, wx.EXPAND, 5 )
		
		bSizer1691 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer169 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stCRorLevel = wx.StaticText( self, wx.ID_ANY, u" Challenge Rating:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stCRorLevel.Wrap( -1 )
		self.stCRorLevel.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.stCRorLevel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer169.Add( self.stCRorLevel, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.txChallengeRating = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 50,-1 ), wx.TE_PROCESS_ENTER )
		self.txChallengeRating.SetMaxLength( 0 ) 
		bSizer169.Add( self.txChallengeRating, 0, wx.LEFT, 3 )
		
		
		bSizer1691.Add( bSizer169, 0, wx.ALL, 2 )
		
		bSizer518 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText881 = wx.StaticText( self, wx.ID_ANY, u"XP:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText881.Wrap( -1 )
		self.m_staticText881.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText881.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer518.Add( self.m_staticText881, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.txXPValue = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.txXPValue.SetMaxLength( 0 ) 
		self.txXPValue.SetToolTip( u"Initial value based on CR, update this field to override" )
		
		bSizer518.Add( self.txXPValue, 0, wx.LEFT, 3 )
		
		
		bSizer1691.Add( bSizer518, 1, wx.LEFT, 3 )
		
		bSizer519 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText8811 = wx.StaticText( self, wx.ID_ANY, u"Alignment:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8811.Wrap( -1 )
		self.m_staticText8811.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_staticText8811.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer519.Add( self.m_staticText8811, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txAlignment = wx.TextCtrl( self, wx.ID_ANY, u"N", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.txAlignment.SetMaxLength( 0 ) 
		bSizer519.Add( self.txAlignment, 1, wx.EXPAND|wx.LEFT, 3 )
		
		
		bSizer1691.Add( bSizer519, 2, 0, 5 )
		
		
		bSizer166.Add( bSizer1691, 0, wx.EXPAND|wx.ALL, 3 )
		
		bSizer521 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer174 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText92 = wx.StaticText( self, wx.ID_ANY, u"Armor Class:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText92.Wrap( -1 )
		bSizer174.Add( self.m_staticText92, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 3 )
		
		self.spACValue = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 99, 10 )
		bSizer174.Add( self.spACValue, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer521.Add( bSizer174, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 3 )
		
		bSizer522 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText279 = wx.StaticText( self, wx.ID_ANY, u"Passive Perception:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText279.Wrap( -1 )
		bSizer522.Add( self.m_staticText279, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.BOTTOM|wx.LEFT, 5 )
		
		self.txPassivePerception = wx.TextCtrl( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		bSizer522.Add( self.txPassivePerception, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer521.Add( bSizer522, 0, wx.ALIGN_RIGHT|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 10 )
		
		
		bSizer166.Add( bSizer521, 0, wx.EXPAND, 3 )
		
		bSizer171 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText89 = wx.StaticText( self, wx.ID_ANY, u"HP:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText89.Wrap( -1 )
		bSizer171.Add( self.m_staticText89, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 3 )
		
		self.spHitPoints = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 9999, 10 )
		self.spHitPoints.SetMaxSize( wx.Size( 85,-1 ) )
		
		bSizer171.Add( self.spHitPoints, 0, 0, 5 )
		
		bSizer645 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button261 = wx.Button( self, wx.ID_ANY, u"Hit Dice:", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer645.Add( self.m_button261, 0, wx.SHAPED, 15 )
		
		self.txHitDice = wx.TextCtrl( self, wx.ID_ANY, u"1d10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txHitDice.SetMaxLength( 0 ) 
		self.txHitDice.SetToolTip( u"Enter dice format for calculating HP (ie, 4d8+3)" )
		
		bSizer645.Add( self.txHitDice, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer171.Add( bSizer645, 0, wx.LEFT, 15 )
		
		
		bSizer166.Add( bSizer171, 0, wx.ALL|wx.EXPAND|wx.EXPAND, 3 )
		
		bSizer173 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer653 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText91 = wx.StaticText( self, wx.ID_ANY, u"Speed:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )
		bSizer653.Add( self.m_staticText91, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 3 )
		
		self.txSpeed = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.txSpeed.SetMaxLength( 0 ) 
		self.txSpeed.SetToolTip( u"Enter base speed" )
		
		bSizer653.Add( self.txSpeed, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.LEFT, 14 )
		
		
		bSizer173.Add( bSizer653, 1, wx.EXPAND, 5 )
		
		bSizer654 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText330 = wx.StaticText( self, wx.ID_ANY, u"Proficiency Bonus", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText330.Wrap( -1 )
		bSizer654.Add( self.m_staticText330, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.LEFT, 5 )
		
		self.spProficiency = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 9, 2 )
		self.spProficiency.SetMinSize( wx.Size( 50,-1 ) )
		
		bSizer654.Add( self.spProficiency, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer173.Add( bSizer654, 1, wx.EXPAND|wx.LEFT, 5 )
		
		
		bSizer166.Add( bSizer173, 0, wx.ALL|wx.EXPAND, 3 )
		
		bSizer605 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bRandomizeStats = wx.Button( self, wx.ID_ANY, u"Randomize Stats", wx.DefaultPosition, wx.Size( -1,25 ), 0 )
		bSizer605.Add( self.bRandomizeStats, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		cxRandomizeSettingChoices = [ u"Straight 3d6", u"4d6, Drop Lowest", u"5d6, Drop Two Lowest" ]
		self.cxRandomizeSetting = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), cxRandomizeSettingChoices, 0 )
		self.cxRandomizeSetting.SetSelection( 0 )
		bSizer605.Add( self.cxRandomizeSetting, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer166.Add( bSizer605, 0, wx.EXPAND, 5 )
		
		
		bSizer165.Add( bSizer166, 0, 0, 0 )
		
		szApplyFilter = wx.BoxSizer( wx.VERTICAL )
		
		self.stUserMonster = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stUserMonster.Wrap( -1 )
		self.stUserMonster.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.stUserMonster.SetBackgroundColour( wx.Colour( 255, 255, 0 ) )
		
		szApplyFilter.Add( self.stUserMonster, 0, 0, 5 )
		
		bSizer560 = wx.BoxSizer( wx.VERTICAL )
		
		self.cbBasicMonster = wx.CheckBox( self, wx.ID_ANY, u"Basic Rules Monster?", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer560.Add( self.cbBasicMonster, 0, wx.ALL, 5 )
		
		
		szApplyFilter.Add( bSizer560, 0, wx.EXPAND, 3 )
		
		sbSizer89 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Filters" ), wx.VERTICAL )
		
		bSizer518 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer525 = wx.BoxSizer( wx.VERTICAL )
		
		self.cbFilterByCR = wx.CheckBox( self, wx.ID_ANY, u"CR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbFilterByCR.SetToolTip( u"Check to filter by Challenge Rating" )
		
		bSizer525.Add( self.cbFilterByCR, 0, wx.ALL, 5 )
		
		lbCRFilterChoices = [ u"<1", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10", u"11", u"12", u"13", u"14", u"15", u"16", u"17", u"18", u"19", u"20+" ]
		self.lbCRFilter = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 50,-1 ), lbCRFilterChoices, wx.LB_MULTIPLE )
		self.lbCRFilter.Enable( False )
		self.lbCRFilter.SetToolTip( u"Select CR to filter" )
		
		bSizer525.Add( self.lbCRFilter, 0, wx.ALL, 5 )
		
		
		bSizer518.Add( bSizer525, 0, wx.EXPAND, 5 )
		
		bSizer526 = wx.BoxSizer( wx.VERTICAL )
		
		self.cbFilterByMonsterType = wx.CheckBox( self, wx.ID_ANY, u"Monster Type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbFilterByMonsterType.SetToolTip( u"Check to filter by Monster Type" )
		
		bSizer526.Add( self.cbFilterByMonsterType, 0, wx.ALL, 5 )
		
		lbMonsterFilterChoices = [ u"Aberration", u"Beast", u"Celestial", u"Construct", u"Dragon", u"Elemental", u"Fey", u"Fiend", u"Giant", u"Humanoid", u"Monstrosity", u"Ooze", u"Plant", u"Undead" ]
		self.lbMonsterFilter = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lbMonsterFilterChoices, wx.LB_MULTIPLE )
		self.lbMonsterFilter.Enable( False )
		self.lbMonsterFilter.SetToolTip( u"Select monster to filter" )
		
		bSizer526.Add( self.lbMonsterFilter, 0, wx.ALL, 5 )
		
		
		bSizer518.Add( bSizer526, 0, wx.EXPAND, 5 )
		
		
		sbSizer89.Add( bSizer518, 1, wx.EXPAND, 5 )
		
		self.cbShowOnlyUserMonsters = wx.CheckBox( self, wx.ID_ANY, u"Show only custom monsters?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbShowOnlyUserMonsters.SetToolTip( u"Select to show only customized monsters." )
		
		sbSizer89.Add( self.cbShowOnlyUserMonsters, 0, 0, 1 )
		
		
		szApplyFilter.Add( sbSizer89, 0, wx.EXPAND, 5 )
		
		
		bSizer165.Add( szApplyFilter, 0, wx.LEFT, 20 )
		
		
		bSizer161.Add( bSizer165, 0, wx.ALL, 3 )
		
		bSizer175 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText93 = wx.StaticText( self, wx.ID_ANY, u"STR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText93.Wrap( -1 )
		bSizer175.Add( self.m_staticText93, 0, wx.ALIGN_CENTER_VERTICAL, 3 )
		
		self.txStr = wx.TextCtrl( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_PROCESS_ENTER )
		self.txStr.SetMaxLength( 0 ) 
		self.txStr.SetToolTip( u"Enter Ability Score" )
		
		bSizer175.Add( self.txStr, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticText931 = wx.StaticText( self, wx.ID_ANY, u"DEX", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText931.Wrap( -1 )
		bSizer175.Add( self.m_staticText931, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 3 )
		
		self.txDex = wx.TextCtrl( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_PROCESS_ENTER )
		self.txDex.SetMaxLength( 0 ) 
		self.txDex.SetToolTip( u"Enter Ability Score" )
		
		bSizer175.Add( self.txDex, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticText932 = wx.StaticText( self, wx.ID_ANY, u"CON", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText932.Wrap( -1 )
		bSizer175.Add( self.m_staticText932, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 3 )
		
		self.txCon = wx.TextCtrl( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_PROCESS_ENTER )
		self.txCon.SetMaxLength( 0 ) 
		self.txCon.SetToolTip( u"Enter Ability Score" )
		
		bSizer175.Add( self.txCon, 0, wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticText933 = wx.StaticText( self, wx.ID_ANY, u"INT", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText933.Wrap( -1 )
		bSizer175.Add( self.m_staticText933, 0, wx.ALIGN_CENTER_VERTICAL, 3 )
		
		self.txInt = wx.TextCtrl( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_PROCESS_ENTER )
		self.txInt.SetMaxLength( 0 ) 
		self.txInt.SetToolTip( u"Enter Ability Score" )
		
		bSizer175.Add( self.txInt, 0, wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticText934 = wx.StaticText( self, wx.ID_ANY, u"WIS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText934.Wrap( -1 )
		bSizer175.Add( self.m_staticText934, 0, wx.ALIGN_CENTER_VERTICAL, 3 )
		
		self.txWis = wx.TextCtrl( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_PROCESS_ENTER )
		self.txWis.SetMaxLength( 0 ) 
		self.txWis.SetToolTip( u"Enter Ability Score" )
		
		bSizer175.Add( self.txWis, 0, wx.RIGHT|wx.LEFT, 5 )
		
		self.m_staticText94 = wx.StaticText( self, wx.ID_ANY, u"CHA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText94.Wrap( 0 )
		bSizer175.Add( self.m_staticText94, 0, wx.LEFT|wx.ALIGN_CENTRE_VERTICAL|wx.ALIGN_CENTER_VERTICAL, 3 )
		
		self.txCha = wx.TextCtrl( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size( 40,-1 ), wx.TE_PROCESS_ENTER )
		self.txCha.SetMaxLength( 0 ) 
		self.txCha.SetToolTip( u"Enter Ability Score" )
		
		bSizer175.Add( self.txCha, 0, wx.RIGHT|wx.LEFT, 5 )
		
		
		bSizer161.Add( bSizer175, 0, wx.ALL|wx.EXPAND|wx.EXPAND, 3 )
		
		bSizer176 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_notebook9 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel48 = wx.Panel( self.m_notebook9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer667 = wx.BoxSizer( wx.VERTICAL )
		
		self.txActions = wx.TextCtrl( self.m_panel48, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,100 ), wx.TE_MULTILINE|wx.TE_RICH2|wx.TE_WORDWRAP )
		self.txActions.SetMaxLength( 0 ) 
		self.txActions.SetToolTip( u"Must add a ~ after the action name to define it" )
		
		bSizer667.Add( self.txActions, 0, wx.ALL|wx.EXPAND, 2 )
		
		
		self.m_panel48.SetSizer( bSizer667 )
		self.m_panel48.Layout()
		bSizer667.Fit( self.m_panel48 )
		self.m_notebook9.AddPage( self.m_panel48, u"Actions", True )
		self.m_panel49 = wx.Panel( self.m_notebook9, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer668 = wx.BoxSizer( wx.VERTICAL )
		
		self.txLegendaryActions = wx.TextCtrl( self.m_panel49, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,100 ), wx.TE_MULTILINE|wx.TE_RICH2|wx.TE_WORDWRAP )
		self.txLegendaryActions.SetMaxLength( 0 ) 
		self.txLegendaryActions.SetToolTip( u"Must add a ^ after the action name to define it." )
		
		bSizer668.Add( self.txLegendaryActions, 0, wx.ALL|wx.EXPAND, 2 )
		
		
		self.m_panel49.SetSizer( bSizer668 )
		self.m_panel49.Layout()
		bSizer668.Fit( self.m_panel49 )
		self.m_notebook9.AddPage( self.m_panel49, u"Legendary Actions", False )
		
		bSizer176.Add( self.m_notebook9, 1, wx.EXPAND, 5 )
		
		
		bSizer161.Add( bSizer176, 1, wx.ALL|wx.EXPAND, 3 )
		
		bSizer177 = wx.BoxSizer( wx.VERTICAL )
		
		self.nbNPC_Features = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_scrolledWindow10 = wx.ScrolledWindow( self.nbNPC_Features, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_scrolledWindow10.SetScrollRate( 5, 5 )
		self.m_scrolledWindow10.SetMaxSize( wx.Size( 1,75 ) )
		
		bSizer649 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer650 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stSaves = wx.StaticText( self.m_scrolledWindow10, wx.ID_ANY, u"Saves:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stSaves.Wrap( -1 )
		bSizer650.Add( self.stSaves, 1, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )
		
		self.txSaves = wx.TextCtrl( self.m_scrolledWindow10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RICH2 )
		bSizer650.Add( self.txSaves, 6, wx.EXPAND, 5 )
		
		
		bSizer649.Add( bSizer650, 0, wx.EXPAND, 5 )
		
		bSizer6501 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stResistances = wx.StaticText( self.m_scrolledWindow10, wx.ID_ANY, u"Resistances:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stResistances.Wrap( -1 )
		bSizer6501.Add( self.stResistances, 1, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )
		
		self.txResistances = wx.TextCtrl( self.m_scrolledWindow10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RICH2 )
		bSizer6501.Add( self.txResistances, 6, wx.EXPAND, 5 )
		
		
		bSizer649.Add( bSizer6501, 0, wx.EXPAND, 5 )
		
		bSizer65011 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stVulnerability = wx.StaticText( self.m_scrolledWindow10, wx.ID_ANY, u"Vulnerabilities:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stVulnerability.Wrap( -1 )
		bSizer65011.Add( self.stVulnerability, 1, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )
		
		self.txVulnerability = wx.TextCtrl( self.m_scrolledWindow10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RICH2 )
		bSizer65011.Add( self.txVulnerability, 6, wx.EXPAND, 5 )
		
		
		bSizer649.Add( bSizer65011, 0, wx.EXPAND, 5 )
		
		bSizer65012 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stImmunity = wx.StaticText( self.m_scrolledWindow10, wx.ID_ANY, u"Immunities:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stImmunity.Wrap( -1 )
		bSizer65012.Add( self.stImmunity, 1, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )
		
		self.txImmunity = wx.TextCtrl( self.m_scrolledWindow10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RICH2 )
		bSizer65012.Add( self.txImmunity, 6, wx.EXPAND, 5 )
		
		
		bSizer649.Add( bSizer65012, 0, wx.EXPAND, 5 )
		
		bSizer650123 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stConditionImmunity = wx.StaticText( self.m_scrolledWindow10, wx.ID_ANY, u"Condition Immunities:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stConditionImmunity.Wrap( -1 )
		bSizer650123.Add( self.stConditionImmunity, 1, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )
		
		self.txConditionImmunity = wx.TextCtrl( self.m_scrolledWindow10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RICH2 )
		bSizer650123.Add( self.txConditionImmunity, 6, wx.EXPAND, 5 )
		
		
		bSizer649.Add( bSizer650123, 0, wx.EXPAND, 5 )
		
		bSizer650121 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stSenses = wx.StaticText( self.m_scrolledWindow10, wx.ID_ANY, u"Senses:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stSenses.Wrap( -1 )
		bSizer650121.Add( self.stSenses, 1, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )
		
		self.txSenses = wx.TextCtrl( self.m_scrolledWindow10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RICH2 )
		bSizer650121.Add( self.txSenses, 6, wx.EXPAND, 5 )
		
		
		bSizer649.Add( bSizer650121, 0, wx.EXPAND, 5 )
		
		bSizer650122 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stLanguages = wx.StaticText( self.m_scrolledWindow10, wx.ID_ANY, u"Languages:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stLanguages.Wrap( -1 )
		bSizer650122.Add( self.stLanguages, 1, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )
		
		self.txLanguages = wx.TextCtrl( self.m_scrolledWindow10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_RICH2 )
		bSizer650122.Add( self.txLanguages, 6, wx.EXPAND, 5 )
		
		
		bSizer649.Add( bSizer650122, 0, wx.EXPAND, 5 )
		
		
		self.m_scrolledWindow10.SetSizer( bSizer649 )
		self.m_scrolledWindow10.Layout()
		bSizer649.Fit( self.m_scrolledWindow10 )
		self.nbNPC_Features.AddPage( self.m_scrolledWindow10, u"Attributes", False )
		self.m_panel351 = wx.Panel( self.nbNPC_Features, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer58611 = wx.BoxSizer( wx.VERTICAL )
		
		self.txTraits = wx.TextCtrl( self.m_panel351, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_RICH2|wx.TE_WORDWRAP )
		bSizer58611.Add( self.txTraits, 1, wx.ALL|wx.EXPAND, 2 )
		
		
		self.m_panel351.SetSizer( bSizer58611 )
		self.m_panel351.Layout()
		bSizer58611.Fit( self.m_panel351 )
		self.nbNPC_Features.AddPage( self.m_panel351, u"Traits", False )
		self.pnSkills = wx.Panel( self.nbNPC_Features, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.pnSkills.SetToolTip( u"Skill values based on current ability scores and proficiency bonus (if checked)" )
		
		gSizer51 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.cbSkill_Acrobatics = wx.CheckBox( self.pnSkills, skAcrobatics, u"Acrobatics", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbSkill_Acrobatics.SetToolTip( u"DEX" )
		
		gSizer51.Add( self.cbSkill_Acrobatics, 0, wx.EXPAND, 5 )
		
		self.cbSkill_History = wx.CheckBox( self.pnSkills, wx.ID_ANY, u"History", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbSkill_History.SetToolTip( u"INT" )
		
		gSizer51.Add( self.cbSkill_History, 0, wx.EXPAND, 5 )
		
		self.cbSkill_Nature = wx.CheckBox( self.pnSkills, wx.ID_ANY, u"Nature", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbSkill_Nature.SetToolTip( u"INT" )
		
		gSizer51.Add( self.cbSkill_Nature, 0, wx.EXPAND, 5 )
		
		self.cbSkill_Religion = wx.CheckBox( self.pnSkills, wx.ID_ANY, u"Religion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbSkill_Religion.SetToolTip( u"INT" )
		
		gSizer51.Add( self.cbSkill_Religion, 0, wx.EXPAND, 5 )
		
		self.cbSkill_AnimalHandling = wx.CheckBox( self.pnSkills, skAnimalHandling, u"Animal Handling", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbSkill_AnimalHandling.SetToolTip( u"WIS" )
		
		gSizer51.Add( self.cbSkill_AnimalHandling, 0, wx.EXPAND, 5 )
		
		self.cbSkill_Insight = wx.CheckBox( self.pnSkills, wx.ID_ANY, u"Insight", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbSkill_Insight.SetToolTip( u"WIS" )
		
		gSizer51.Add( self.cbSkill_Insight, 0, wx.EXPAND, 5 )
		
		self.cbSkill_Perception = wx.CheckBox( self.pnSkills, wx.ID_ANY, u"Perception", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbSkill_Perception.SetToolTip( u"WIS" )
		
		gSizer51.Add( self.cbSkill_Perception, 0, wx.EXPAND, 5 )
		
		self.cbSkill_SleightOfHand = wx.CheckBox( self.pnSkills, wx.ID_ANY, u"Sleight of Hand", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbSkill_SleightOfHand.SetToolTip( u"DEX" )
		
		gSizer51.Add( self.cbSkill_SleightOfHand, 0, wx.EXPAND, 5 )
		
		self.cbSkill_Arcana = wx.CheckBox( self.pnSkills, wx.ID_ANY, u"Arcana", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbSkill_Arcana.SetToolTip( u"INT" )
		
		gSizer51.Add( self.cbSkill_Arcana, 0, wx.EXPAND, 5 )
		
		self.cbSkill_Intimidation = wx.CheckBox( self.pnSkills, wx.ID_ANY, u"Intimidation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbSkill_Intimidation.SetToolTip( u"CHA" )
		
		gSizer51.Add( self.cbSkill_Intimidation, 0, wx.EXPAND, 5 )
		
		self.cbSkill_Performance = wx.CheckBox( self.pnSkills, wx.ID_ANY, u"Performance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbSkill_Performance.SetToolTip( u"CHA" )
		
		gSizer51.Add( self.cbSkill_Performance, 0, wx.EXPAND, 5 )
		
		self.cbSkill_Stealth = wx.CheckBox( self.pnSkills, wx.ID_ANY, u"Stealth", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbSkill_Stealth.SetToolTip( u"DEX" )
		
		gSizer51.Add( self.cbSkill_Stealth, 0, wx.EXPAND, 5 )
		
		self.cbSkill_Athletics = wx.CheckBox( self.pnSkills, wx.ID_ANY, u"Athletics", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbSkill_Athletics.SetToolTip( u"STR" )
		
		gSizer51.Add( self.cbSkill_Athletics, 0, wx.EXPAND, 5 )
		
		self.cbSkill_Investigation = wx.CheckBox( self.pnSkills, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbSkill_Investigation.SetToolTip( u"INT" )
		
		gSizer51.Add( self.cbSkill_Investigation, 0, wx.EXPAND, 5 )
		
		self.cbSkill_Persuasion = wx.CheckBox( self.pnSkills, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbSkill_Persuasion.SetToolTip( u"CHA" )
		
		gSizer51.Add( self.cbSkill_Persuasion, 0, wx.EXPAND, 5 )
		
		self.cbSkill_Survival = wx.CheckBox( self.pnSkills, wx.ID_ANY, u"Survival", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbSkill_Survival.SetToolTip( u"WIS" )
		
		gSizer51.Add( self.cbSkill_Survival, 0, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.cbSkill_Deception = wx.CheckBox( self.pnSkills, wx.ID_ANY, u"Deception", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbSkill_Deception.SetToolTip( u"CHA" )
		
		gSizer51.Add( self.cbSkill_Deception, 0, wx.EXPAND, 5 )
		
		self.cbSkill_Medicine = wx.CheckBox( self.pnSkills, wx.ID_ANY, u"Medicine", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbSkill_Medicine.SetToolTip( u"WIS" )
		
		gSizer51.Add( self.cbSkill_Medicine, 0, wx.EXPAND, 5 )
		
		
		self.pnSkills.SetSizer( gSizer51 )
		self.pnSkills.Layout()
		gSizer51.Fit( self.pnSkills )
		self.nbNPC_Features.AddPage( self.pnSkills, u"Skills", True )
		self.m_panel35 = wx.Panel( self.nbNPC_Features, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5861 = wx.BoxSizer( wx.VERTICAL )
		
		self.txIdeals = wx.TextCtrl( self.m_panel35, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_RICH2|wx.TE_WORDWRAP )
		bSizer5861.Add( self.txIdeals, 1, wx.ALL|wx.EXPAND, 2 )
		
		
		self.m_panel35.SetSizer( bSizer5861 )
		self.m_panel35.Layout()
		bSizer5861.Fit( self.m_panel35 )
		self.nbNPC_Features.AddPage( self.m_panel35, u"Ideals", False )
		self.m_panel34 = wx.Panel( self.nbNPC_Features, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer586 = wx.BoxSizer( wx.VERTICAL )
		
		self.txBonds = wx.TextCtrl( self.m_panel34, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_RICH2|wx.TE_WORDWRAP )
		bSizer586.Add( self.txBonds, 1, wx.ALL|wx.EXPAND, 2 )
		
		
		self.m_panel34.SetSizer( bSizer586 )
		self.m_panel34.Layout()
		bSizer586.Fit( self.m_panel34 )
		self.nbNPC_Features.AddPage( self.m_panel34, u"Bonds", False )
		self.m_panel36 = wx.Panel( self.nbNPC_Features, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5862 = wx.BoxSizer( wx.VERTICAL )
		
		self.txFlaws = wx.TextCtrl( self.m_panel36, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_RICH2|wx.TE_WORDWRAP )
		bSizer5862.Add( self.txFlaws, 1, wx.ALL|wx.EXPAND, 2 )
		
		
		self.m_panel36.SetSizer( bSizer5862 )
		self.m_panel36.Layout()
		bSizer5862.Fit( self.m_panel36 )
		self.nbNPC_Features.AddPage( self.m_panel36, u"Flaws", False )
		self.m_panel361 = wx.Panel( self.nbNPC_Features, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer58621 = wx.BoxSizer( wx.VERTICAL )
		
		self.txOtherFeatures = wx.TextCtrl( self.m_panel361, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,80 ), wx.TE_MULTILINE|wx.TE_RICH2|wx.TE_WORDWRAP )
		bSizer58621.Add( self.txOtherFeatures, 1, wx.ALL|wx.EXPAND, 2 )
		
		
		self.m_panel361.SetSizer( bSizer58621 )
		self.m_panel361.Layout()
		bSizer58621.Fit( self.m_panel361 )
		self.nbNPC_Features.AddPage( self.m_panel361, u"Other Features", False )
		self.m_panel46 = wx.Panel( self.nbNPC_Features, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer635 = wx.BoxSizer( wx.VERTICAL )
		
		self.txNotes = wx.TextCtrl( self.m_panel46, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_RICH2|wx.TE_WORDWRAP )
		bSizer635.Add( self.txNotes, 1, wx.ALL|wx.EXPAND, 2 )
		
		
		self.m_panel46.SetSizer( bSizer635 )
		self.m_panel46.Layout()
		bSizer635.Fit( self.m_panel46 )
		self.nbNPC_Features.AddPage( self.m_panel46, u"Notes", False )
		
		bSizer177.Add( self.nbNPC_Features, 1, wx.EXPAND, 2 )
		
		
		bSizer161.Add( bSizer177, 1, wx.ALL|wx.EXPAND, 3 )
		
		bSizer182 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer589 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cbSpellcaster = wx.CheckBox( self, wx.ID_ANY, u"Spellcaster?", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer589.Add( self.cbSpellcaster, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		self.stSpellFilterText = wx.StaticText( self, wx.ID_ANY, u"Filter spells by class:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stSpellFilterText.Wrap( -1 )
		bSizer589.Add( self.stSpellFilterText, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 20 )
		
		cbxSpellFilterChoices = [ u"All Classes", u"Bard", u"Cleric", u"Druid", u"Monk", u"Paladin", u"Ranger", u"Sorcerer", u"Warlock", u"Wizard" ]
		self.cbxSpellFilter = wx.ComboBox( self, wx.ID_ANY, u"All", wx.DefaultPosition, wx.DefaultSize, cbxSpellFilterChoices, wx.CB_READONLY )
		self.cbxSpellFilter.SetSelection( 0 )
		bSizer589.Add( self.cbxSpellFilter, 0, wx.ALL, 2 )
		
		bSizer658 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stSpellAttack = wx.StaticText( self, wx.ID_ANY, u"Spell Attack:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stSpellAttack.Wrap( -1 )
		bSizer658.Add( self.stSpellAttack, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spSpellAttack = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, -10, 20, 1 )
		self.spSpellAttack.SetToolTip( u"Attack = Proficiency + Spellcasting Ability Modifier" )
		
		bSizer658.Add( self.spSpellAttack, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer589.Add( bSizer658, 1, wx.EXPAND, 5 )
		
		bSizer6581 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stSpellDC = wx.StaticText( self, wx.ID_ANY, u"Save DC:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stSpellDC.Wrap( -1 )
		bSizer6581.Add( self.stSpellDC, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spSpellDC = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, -10, 20, 8 )
		self.spSpellDC.SetToolTip( u"Save = 8 + Proficiency + Spellcasting Ability Modifier" )
		
		bSizer6581.Add( self.spSpellDC, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer589.Add( bSizer6581, 1, wx.EXPAND, 5 )
		
		
		bSizer182.Add( bSizer589, 0, wx.EXPAND, 5 )
		
		bSizer588 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.trCreatureSpellList = wx.TreeCtrl( self, trCreatureSpellListID, wx.DefaultPosition, wx.Size( -1,100 ), wx.TR_DEFAULT_STYLE )
		self.trCreatureSpellList.SetBackgroundColour( wx.Colour( 201, 241, 184 ) )
		self.trCreatureSpellList.SetToolTip( u"Spells for this NPC/Monster" )
		
		bSizer588.Add( self.trCreatureSpellList, 1, wx.ALL|wx.EXPAND|wx.FIXED_MINSIZE, 2 )
		
		self.trAllSpellList = wx.TreeCtrl( self, trAllSpellListID, wx.DefaultPosition, wx.Size( -1,100 ), wx.TR_DEFAULT_STYLE )
		self.trAllSpellList.SetBackgroundColour( wx.Colour( 196, 196, 255 ) )
		self.trAllSpellList.SetToolTip( u"Available Spells" )
		
		bSizer588.Add( self.trAllSpellList, 1, wx.ALL|wx.EXPAND|wx.FIXED_MINSIZE, 2 )
		
		
		bSizer182.Add( bSizer588, 1, wx.EXPAND, 5 )
		
		self.txSpellDescription = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP )
		bSizer182.Add( self.txSpellDescription, 1, wx.ALL|wx.EXPAND, 2 )
		
		
		bSizer161.Add( bSizer182, 0, wx.ALL|wx.EXPAND, 3 )
		
		
		bSizer159.Add( bSizer161, 0, wx.EXPAND|wx.EXPAND, 0 )
		
		szUpdateButtons = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bNewMonster = wx.Button( self, wx.ID_ANY, u"New Monster", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bNewMonster.SetToolTip( u"Clear selection and all fields" )
		
		szUpdateButtons.Add( self.bNewMonster, 0, 0, 5 )
		
		self.bAddMonster = wx.Button( self, wx.ID_ANY, u"Add to Master List", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bAddMonster.SetDefault() 
		self.bAddMonster.SetToolTip( u"Add a new monster based on the values to the left." )
		
		szUpdateButtons.Add( self.bAddMonster, 0, 0, 0 )
		
		self.bCopyMonster = wx.Button( self, wx.ID_ANY, u"Copy Monster", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bCopyMonster.SetDefault() 
		self.bCopyMonster.Enable( False )
		self.bCopyMonster.SetToolTip( u"Copy selected monster stats to a new monster" )
		
		szUpdateButtons.Add( self.bCopyMonster, 0, wx.LEFT, 0 )
		
		bSizer601 = wx.BoxSizer( wx.VERTICAL )
		
		self.bUpdateMonster = wx.Button( self, wx.ID_ANY, u"Update Monster", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bUpdateMonster.SetDefault() 
		self.bUpdateMonster.Enable( False )
		self.bUpdateMonster.SetToolTip( u"Update the monster selected in the list to the values above." )
		
		bSizer601.Add( self.bUpdateMonster, 0, wx.LEFT|wx.ALIGN_CENTRE_HORIZONTAL, 0 )
		
		self.gxUpdateGauge = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 100,10 ), wx.GA_HORIZONTAL )
		self.gxUpdateGauge.SetValue( 0 ) 
		self.gxUpdateGauge.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.gxUpdateGauge.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer601.Add( self.gxUpdateGauge, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.LEFT, 0 )
		
		
		szUpdateButtons.Add( bSizer601, 0, 0, 5 )
		
		self.bDeleteMonster = wx.Button( self, wx.ID_ANY, u"Delete Monster", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bDeleteMonster.SetDefault() 
		self.bDeleteMonster.Enable( False )
		self.bDeleteMonster.SetToolTip( u"Delete the currently selected monster." )
		
		szUpdateButtons.Add( self.bDeleteMonster, 0, 0, 0 )
		
		
		bSizer159.Add( szUpdateButtons, 0, wx.TOP|wx.EXPAND, 5 )
		
		bSizer185 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ID_OK = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_OK.SetDefault() 
		self.ID_OK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_OK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.ID_OK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		self.ID_OK.SetToolTip( u"Add to description text if open" )
		
		bSizer185.Add( self.ID_OK, 0, wx.RIGHT, 2 )
		
		self.ID_CANCEL = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_CANCEL.SetDefault() 
		self.ID_CANCEL.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_CANCEL.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ID_CANCEL.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		
		bSizer185.Add( self.ID_CANCEL, 0, wx.LEFT|wx.RIGHT, 2 )
		
		self.bHelp = wx.Button( self, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bHelp.SetDefault() 
		self.bHelp.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bHelp.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bHelp.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer185.Add( self.bHelp, 0, wx.LEFT, 2 )
		
		
		bSizer159.Add( bSizer185, 0, wx.TOP|wx.ALIGN_CENTRE_HORIZONTAL|wx.EXPAND, 10 )
		
		
		bSizer158.Add( bSizer159, 2, wx.EXPAND, 0 )
		
		bSizer186 = wx.BoxSizer( wx.VERTICAL )
		
		lbMonsterListChoices = []
		self.lbMonsterList = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 225,-1 ), lbMonsterListChoices, wx.LB_SINGLE|wx.LB_SORT )
		self.lbMonsterList.SetToolTip( u"List of Monsters" )
		
		bSizer186.Add( self.lbMonsterList, 1, wx.ALL|wx.EXPAND|wx.EXPAND, 2 )
		
		self.bClearSelection = wx.Button( self, wx.ID_ANY, u"Clear Selection", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bClearSelection.SetBackgroundColour( wx.Colour( 219, 162, 177 ) )
		
		bSizer186.Add( self.bClearSelection, 0, wx.EXPAND, 0 )
		
		
		bSizer158.Add( bSizer186, 1, wx.LEFT|wx.EXPAND|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer158 )
		self.Layout()
		
		# Connect Events
		self.txName.Bind( wx.EVT_TEXT, self.OnMonsterNamed )
		self.bbSelectCustomImage.Bind( wx.EVT_BUTTON, self.OnSelectCustomImage )
		self.txChallengeRating.Bind( wx.EVT_TEXT, self.UpdateXPfromCR )
		self.m_button261.Bind( wx.EVT_BUTTON, self.OnCalculateHP )
		self.spProficiency.Bind( wx.EVT_SPINCTRL, self.UpdateSkills )
		self.bRandomizeStats.Bind( wx.EVT_BUTTON, self.OnRandomizeStats )
		self.cbFilterByCR.Bind( wx.EVT_CHECKBOX, self.EnableFilterCR )
		self.lbCRFilter.Bind( wx.EVT_LISTBOX, self.FilterMonsterList )
		self.cbFilterByMonsterType.Bind( wx.EVT_CHECKBOX, self.EnableFilterMonsterType )
		self.lbMonsterFilter.Bind( wx.EVT_LISTBOX, self.FilterMonsterList )
		self.cbShowOnlyUserMonsters.Bind( wx.EVT_CHECKBOX, self.FilterMonsterList )
		self.txStr.Bind( wx.EVT_TEXT_ENTER, self.UpdateSkills )
		self.txDex.Bind( wx.EVT_TEXT_ENTER, self.UpdateSkills )
		self.txCon.Bind( wx.EVT_TEXT_ENTER, self.UpdateSkills )
		self.txInt.Bind( wx.EVT_TEXT_ENTER, self.UpdateSkills )
		self.txWis.Bind( wx.EVT_TEXT_ENTER, self.UpdateSkills )
		self.txCha.Bind( wx.EVT_TEXT_ENTER, self.UpdateSkills )
		self.cbSkill_Acrobatics.Bind( wx.EVT_CHECKBOX, self.UpdateSkills )
		self.cbSkill_History.Bind( wx.EVT_CHECKBOX, self.UpdateSkills )
		self.cbSkill_Nature.Bind( wx.EVT_CHECKBOX, self.UpdateSkills )
		self.cbSkill_Religion.Bind( wx.EVT_CHECKBOX, self.UpdateSkills )
		self.cbSkill_AnimalHandling.Bind( wx.EVT_CHECKBOX, self.UpdateSkills )
		self.cbSkill_Insight.Bind( wx.EVT_CHECKBOX, self.UpdateSkills )
		self.cbSkill_Perception.Bind( wx.EVT_CHECKBOX, self.UpdateSkills )
		self.cbSkill_SleightOfHand.Bind( wx.EVT_CHECKBOX, self.UpdateSkills )
		self.cbSkill_Arcana.Bind( wx.EVT_CHECKBOX, self.UpdateSkills )
		self.cbSkill_Intimidation.Bind( wx.EVT_CHECKBOX, self.UpdateSkills )
		self.cbSkill_Performance.Bind( wx.EVT_CHECKBOX, self.UpdateSkills )
		self.cbSkill_Stealth.Bind( wx.EVT_CHECKBOX, self.UpdateSkills )
		self.cbSkill_Athletics.Bind( wx.EVT_CHECKBOX, self.UpdateSkills )
		self.cbSkill_Investigation.Bind( wx.EVT_CHECKBOX, self.UpdateSkills )
		self.cbSkill_Persuasion.Bind( wx.EVT_CHECKBOX, self.UpdateSkills )
		self.cbSkill_Survival.Bind( wx.EVT_CHECKBOX, self.UpdateSkills )
		self.cbSkill_Deception.Bind( wx.EVT_CHECKBOX, self.UpdateSkills )
		self.cbSkill_Medicine.Bind( wx.EVT_CHECKBOX, self.UpdateSkills )
		self.cbSpellcaster.Bind( wx.EVT_CHECKBOX, self.OnSpellcasterCheckbox )
		self.cbxSpellFilter.Bind( wx.EVT_COMBOBOX, self.ChangeSpellListFilter )
		self.trCreatureSpellList.Bind( wx.EVT_TREE_ITEM_ACTIVATED, self.OnSelectSpellItemMonster )
		self.trCreatureSpellList.Bind( wx.EVT_TREE_SEL_CHANGED, self.OnDisplaySpell )
		self.trAllSpellList.Bind( wx.EVT_TREE_ITEM_ACTIVATED, self.OnSelectSpellItemMain )
		self.trAllSpellList.Bind( wx.EVT_TREE_SEL_CHANGED, self.OnDisplaySpell )
		self.bNewMonster.Bind( wx.EVT_BUTTON, self.OnNewMonster )
		self.bAddMonster.Bind( wx.EVT_BUTTON, self.OnAddMonster )
		self.bCopyMonster.Bind( wx.EVT_BUTTON, self.OnCopyMonster )
		self.bUpdateMonster.Bind( wx.EVT_BUTTON, self.OnUpdateMonster )
		self.bDeleteMonster.Bind( wx.EVT_BUTTON, self.OnDeleteMonster )
		self.ID_OK.Bind( wx.EVT_BUTTON, self.OnOK )
		self.ID_CANCEL.Bind( wx.EVT_BUTTON, self.OnCancel )
		self.bHelp.Bind( wx.EVT_BUTTON, self.OnHelp )
		self.lbMonsterList.Bind( wx.EVT_LISTBOX, self.OnListbox_lbMonsterList )
		self.bClearSelection.Bind( wx.EVT_BUTTON, self.ClearSelection )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnMonsterNamed( self, event ):
		event.Skip()
	
	def OnSelectCustomImage( self, event ):
		event.Skip()
	
	def UpdateXPfromCR( self, event ):
		event.Skip()
	
	def OnCalculateHP( self, event ):
		event.Skip()
	
	def UpdateSkills( self, event ):
		event.Skip()
	
	def OnRandomizeStats( self, event ):
		event.Skip()
	
	def EnableFilterCR( self, event ):
		event.Skip()
	
	def FilterMonsterList( self, event ):
		event.Skip()
	
	def EnableFilterMonsterType( self, event ):
		event.Skip()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	def OnSpellcasterCheckbox( self, event ):
		event.Skip()
	
	def ChangeSpellListFilter( self, event ):
		event.Skip()
	
	def OnSelectSpellItemMonster( self, event ):
		event.Skip()
	
	def OnDisplaySpell( self, event ):
		event.Skip()
	
	def OnSelectSpellItemMain( self, event ):
		event.Skip()
	
	
	def OnNewMonster( self, event ):
		event.Skip()
	
	def OnAddMonster( self, event ):
		event.Skip()
	
	def OnCopyMonster( self, event ):
		event.Skip()
	
	def OnUpdateMonster( self, event ):
		event.Skip()
	
	def OnDeleteMonster( self, event ):
		event.Skip()
	
	def OnOK( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		event.Skip()
	
	def OnHelp( self, event ):
		event.Skip()
	
	def OnListbox_lbMonsterList( self, event ):
		event.Skip()
	
	def ClearSelection( self, event ):
		event.Skip()
	

###########################################################################
## Class TreasureDialogBase
###########################################################################

class TreasureDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Treasure", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer189 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer190 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText113 = wx.StaticText( self, wx.ID_ANY, u"Treasure Description:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText113.Wrap( -1 )
		bSizer190.Add( self.m_staticText113, 0, wx.ALL, 3 )
		
		self.txDescription = wx.TextCtrl( self, wx.ID_ANY, u"Describe treasure owner, location, etc.", wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.txDescription.SetMaxLength( 0 ) 
		self.txDescription.SetForegroundColour( wx.Colour( 0, 0, 160 ) )
		
		bSizer190.Add( self.txDescription, 0, wx.LEFT, 6 )
		
		bSizer191 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText114 = wx.StaticText( self, wx.ID_ANY, u"Encounter Level:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText114.Wrap( -1 )
		bSizer191.Add( self.m_staticText114, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.spEncounterLevel = wx.SpinCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 1, 20, 1 )
		bSizer191.Add( self.spEncounterLevel, 0, 0, 0 )
		
		
		bSizer190.Add( bSizer191, 0, wx.ALL, 5 )
		
		self.bGenerateStandardTreasure = wx.Button( self, wx.ID_ANY, u"Generate Standard Treasure", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bGenerateStandardTreasure.SetDefault() 
		self.bGenerateStandardTreasure.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bGenerateStandardTreasure.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bGenerateStandardTreasure.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer190.Add( self.bGenerateStandardTreasure, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 3 )
		
		bSizer192 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer193 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer194 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap17 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"artwork/treasure_icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 100,100 ), 0 )
		bSizer194.Add( self.m_bitmap17, 0, 0, 0 )
		
		
		bSizer193.Add( bSizer194, 0, wx.LEFT|wx.RIGHT, 20 )
		
		bSizer195 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer196 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText115 = wx.StaticText( self, wx.ID_ANY, u"Copper (CP):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText115.Wrap( -1 )
		bSizer196.Add( self.m_staticText115, 0, wx.ALIGN_CENTRE_VERTICAL, 0 )
		
		self.txCP = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.txCP.SetMaxLength( 0 ) 
		bSizer196.Add( self.txCP, 0, 0, 0 )
		
		
		bSizer195.Add( bSizer196, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_RIGHT, 2 )
		
		bSizer197 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText116 = wx.StaticText( self, wx.ID_ANY, u"Silver (SP):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText116.Wrap( -1 )
		bSizer197.Add( self.m_staticText116, 0, wx.ALIGN_CENTRE_VERTICAL, 0 )
		
		self.txSP = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.txSP.SetMaxLength( 0 ) 
		bSizer197.Add( self.txSP, 0, 0, 0 )
		
		
		bSizer195.Add( bSizer197, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_RIGHT, 2 )
		
		bSizer198 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText117 = wx.StaticText( self, wx.ID_ANY, u"Gold (GP):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText117.Wrap( -1 )
		bSizer198.Add( self.m_staticText117, 0, wx.ALIGN_CENTRE_VERTICAL, 0 )
		
		self.txGP = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.txGP.SetMaxLength( 0 ) 
		bSizer198.Add( self.txGP, 0, 0, 0 )
		
		
		bSizer195.Add( bSizer198, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_RIGHT, 2 )
		
		bSizer199 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText118 = wx.StaticText( self, wx.ID_ANY, u"Platinum (PP):", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText118.Wrap( -1 )
		bSizer199.Add( self.m_staticText118, 0, wx.ALIGN_CENTRE_VERTICAL, 0 )
		
		self.txPP = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.txPP.SetMaxLength( 0 ) 
		bSizer199.Add( self.txPP, 0, 0, 0 )
		
		
		bSizer195.Add( bSizer199, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_RIGHT, 2 )
		
		
		bSizer193.Add( bSizer195, 0, wx.ALIGN_RIGHT, 0 )
		
		
		bSizer192.Add( bSizer193, 0, wx.EXPAND|wx.EXPAND, 0 )
		
		bSizer200 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText119 = wx.StaticText( self, wx.ID_ANY, u"Magic Items:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText119.Wrap( 0 )
		bSizer200.Add( self.m_staticText119, 0, wx.ALIGN_CENTRE_VERTICAL, 0 )
		
		lbMagicItemsChoices = []
		self.lbMagicItems = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), lbMagicItemsChoices, 0 )
		bSizer200.Add( self.lbMagicItems, 0, 0, 0 )
		
		
		bSizer192.Add( bSizer200, 0, wx.ALL|wx.ALIGN_RIGHT, 3 )
		
		bSizer201 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText120 = wx.StaticText( self, wx.ID_ANY, u"Mundane Items:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText120.Wrap( 0 )
		bSizer201.Add( self.m_staticText120, 0, wx.ALIGN_CENTRE_VERTICAL, 0 )
		
		lbMundaneItemsChoices = []
		self.lbMundaneItems = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), lbMundaneItemsChoices, 0 )
		bSizer201.Add( self.lbMundaneItems, 0, 0, 0 )
		
		
		bSizer192.Add( bSizer201, 0, wx.ALL, 3 )
		
		bSizer202 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText121 = wx.StaticText( self, wx.ID_ANY, u"Goods:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( 0 )
		bSizer202.Add( self.m_staticText121, 0, wx.ALIGN_CENTRE_VERTICAL, 0 )
		
		lbGoodsChoices = []
		self.lbGoods = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), lbGoodsChoices, 0 )
		bSizer202.Add( self.lbGoods, 0, 0, 0 )
		
		
		bSizer192.Add( bSizer202, 0, wx.ALL|wx.ALIGN_RIGHT, 3 )
		
		
		bSizer190.Add( bSizer192, 0, wx.ALL, 5 )
		
		
		bSizer189.Add( bSizer190, 0, 0, 0 )
		
		bSizer203 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ID_OK = wx.Button( self, wx.ID_ANY, u"Add as Icon ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_OK.SetDefault() 
		self.ID_OK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_OK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.ID_OK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer203.Add( self.ID_OK, 0, wx.RIGHT, 2 )
		
		self.ID_CANCEL = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_CANCEL.SetDefault() 
		self.ID_CANCEL.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_CANCEL.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ID_CANCEL.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		
		bSizer203.Add( self.ID_CANCEL, 0, wx.LEFT|wx.RIGHT, 2 )
		
		self.bHelp = wx.Button( self, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bHelp.SetDefault() 
		self.bHelp.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bHelp.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bHelp.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer203.Add( self.bHelp, 0, wx.LEFT, 2 )
		
		
		bSizer189.Add( bSizer203, 0, wx.ALL|wx.ALIGN_CENTRE, 3 )
		
		
		self.SetSizer( bSizer189 )
		self.Layout()
		bSizer189.Fit( self )
		
		# Connect Events
		self.bGenerateStandardTreasure.Bind( wx.EVT_BUTTON, self.GenerateStandardTreasure )
		self.ID_OK.Bind( wx.EVT_BUTTON, self.OnOK )
		self.ID_CANCEL.Bind( wx.EVT_BUTTON, self.OnCancel )
		self.bHelp.Bind( wx.EVT_BUTTON, self.OnHelp )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def GenerateStandardTreasure( self, event ):
		event.Skip()
	
	def OnOK( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		event.Skip()
	
	def OnHelp( self, event ):
		event.Skip()
	

###########################################################################
## Class RandomGeomorphDungeonDialogBase
###########################################################################

class RandomGeomorphDungeonDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Create Random Geomorph Dungeon", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer204 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer54 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Size of dungeon (number of geomorphs)" ), wx.HORIZONTAL )
		
		bSizer205 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText122 = wx.StaticText( self, wx.ID_ANY, u"Horizontal Size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText122.Wrap( -1 )
		bSizer205.Add( self.m_staticText122, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.spHorizontalSize = wx.SpinCtrl( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size( 40,-1 ), wx.SP_ARROW_KEYS, 1, 30, 4 )
		bSizer205.Add( self.spHorizontalSize, 0, 0, 0 )
		
		
		sbSizer54.Add( bSizer205, 0, wx.LEFT, 30 )
		
		bSizer206 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText123 = wx.StaticText( self, wx.ID_ANY, u"Vertical Size", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText123.Wrap( -1 )
		bSizer206.Add( self.m_staticText123, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.spVerticalSize = wx.SpinCtrl( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size( 40,-1 ), wx.SP_ARROW_KEYS, 1, 30, 4 )
		bSizer206.Add( self.spVerticalSize, 0, 0, 0 )
		
		
		sbSizer54.Add( bSizer206, 0, wx.LEFT, 20 )
		
		self.bGenerateDungeon = wx.Button( self, wx.ID_ANY, u"Generate Dungeon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bGenerateDungeon.SetDefault() 
		self.bGenerateDungeon.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bGenerateDungeon.SetBackgroundColour( wx.Colour( 64, 0, 128 ) )
		self.bGenerateDungeon.Enable( False )
		
		sbSizer54.Add( self.bGenerateDungeon, 0, wx.LEFT, 10 )
		
		
		bSizer204.Add( sbSizer54, 0, wx.EXPAND, 0 )
		
		sbSizer55 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Available Geomorphs" ), wx.HORIZONTAL )
		
		bSizer207 = wx.BoxSizer( wx.VERTICAL )
		
		lbGeomorphListChoices = []
		self.lbGeomorphList = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 230,180 ), lbGeomorphListChoices, 0 )
		bSizer207.Add( self.lbGeomorphList, 0, 0, 0 )
		
		bSizer208 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bLoadGeomorphs = wx.Button( self, wx.ID_ANY, u"Load Geomorphs...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bLoadGeomorphs.SetDefault() 
		bSizer208.Add( self.bLoadGeomorphs, 0, 0, 0 )
		
		self.bUnloadGeomorphs = wx.Button( self, wx.ID_ANY, u"Unload Geomorphs...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bUnloadGeomorphs.SetDefault() 
		bSizer208.Add( self.bUnloadGeomorphs, 0, 0, 0 )
		
		
		bSizer207.Add( bSizer208, 0, 0, 0 )
		
		self.cbLimitGeomorphUsage = wx.CheckBox( self, wx.ID_ANY, u"Limit number of geomorphs selected?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbLimitGeomorphUsage.SetValue(True) 
		bSizer207.Add( self.cbLimitGeomorphUsage, 0, wx.BOTTOM|wx.TOP, 5 )
		
		bSizer209 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stLimitText1 = wx.StaticText( self, wx.ID_ANY, u"Use no more than ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stLimitText1.Wrap( -1 )
		bSizer209.Add( self.stLimitText1, 0, wx.RIGHT|wx.ALIGN_CENTRE, 2 )
		
		self.spGeomorphUseLimit = wx.SpinCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 40,-1 ), wx.SP_ARROW_KEYS, 1, 99, 1 )
		bSizer209.Add( self.spGeomorphUseLimit, 0, 0, 0 )
		
		self.stLimitText2 = wx.StaticText( self, wx.ID_ANY, u"geomorphs per map.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stLimitText2.Wrap( -1 )
		bSizer209.Add( self.stLimitText2, 0, wx.LEFT|wx.ALIGN_CENTRE, 2 )
		
		
		bSizer207.Add( bSizer209, 0, wx.TOP|wx.ALIGN_RIGHT, 3 )
		
		
		sbSizer55.Add( bSizer207, 0, wx.ALL, 3 )
		
		bSizer210 = wx.BoxSizer( wx.VERTICAL )
		
		self.pnImagePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 180,210 ), wx.TAB_TRAVERSAL )
		self.pnImagePanel.SetBackgroundColour( wx.Colour( 64, 128, 128 ) )
		
		bSizer210.Add( self.pnImagePanel, 0, 0, 0 )
		
		
		sbSizer55.Add( bSizer210, 0, wx.ALL, 3 )
		
		
		bSizer204.Add( sbSizer55, 0, 0, 0 )
		
		bSizer211 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ID_OK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_OK.SetDefault() 
		self.ID_OK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_OK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.ID_OK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer211.Add( self.ID_OK, 0, 0, 0 )
		
		self.ID_CANCEL = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_CANCEL.SetDefault() 
		self.ID_CANCEL.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_CANCEL.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ID_CANCEL.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		
		bSizer211.Add( self.ID_CANCEL, 0, 0, 0 )
		
		self.bHelp = wx.Button( self, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bHelp.SetDefault() 
		self.bHelp.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bHelp.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bHelp.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer211.Add( self.bHelp, 0, 0, 0 )
		
		
		bSizer204.Add( bSizer211, 0, wx.ALL|wx.ALIGN_CENTRE_HORIZONTAL, 3 )
		
		
		self.SetSizer( bSizer204 )
		self.Layout()
		bSizer204.Fit( self )
		
		# Connect Events
		self.bGenerateDungeon.Bind( wx.EVT_BUTTON, self.GenerateDungeon )
		self.lbGeomorphList.Bind( wx.EVT_LISTBOX, self.OnGeomorphList )
		self.bLoadGeomorphs.Bind( wx.EVT_BUTTON, self.LoadGeomorphs )
		self.bUnloadGeomorphs.Bind( wx.EVT_BUTTON, self.UnloadGeomorphs )
		self.cbLimitGeomorphUsage.Bind( wx.EVT_CHECKBOX, self.LimitGeomorphUsage )
		self.ID_OK.Bind( wx.EVT_BUTTON, self.OnOK )
		self.ID_CANCEL.Bind( wx.EVT_BUTTON, self.OnCancel )
		self.bHelp.Bind( wx.EVT_BUTTON, self.OnHelp )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def GenerateDungeon( self, event ):
		event.Skip()
	
	def OnGeomorphList( self, event ):
		event.Skip()
	
	def LoadGeomorphs( self, event ):
		event.Skip()
	
	def UnloadGeomorphs( self, event ):
		event.Skip()
	
	def LimitGeomorphUsage( self, event ):
		event.Skip()
	
	def OnOK( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		event.Skip()
	
	def OnHelp( self, event ):
		event.Skip()
	

###########################################################################
## Class PC_GeneratorBase
###########################################################################

class PC_GeneratorBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Player Character Generator", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer376 = wx.BoxSizer( wx.VERTICAL )
		
		self.nbMainNotebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pnASF = wx.Panel( self.nbMainNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer378 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer385 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer381 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText169 = wx.StaticText( self.pnASF, wx.ID_ANY, u"Character Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText169.Wrap( -1 )
		bSizer381.Add( self.m_staticText169, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.txCharacterName = wx.TextCtrl( self.pnASF, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 175,-1 ), 0 )
		self.txCharacterName.SetMaxLength( 0 ) 
		bSizer381.Add( self.txCharacterName, 0, wx.ALL, 5 )
		
		self.bRandomName = wx.Button( self.pnASF, wx.ID_ANY, u"Random", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer381.Add( self.bRandomName, 0, wx.ALL, 5 )
		
		
		bSizer385.Add( bSizer381, 0, 0, 5 )
		
		bSizer3811 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1691 = wx.StaticText( self.pnASF, wx.ID_ANY, u"Player Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1691.Wrap( -1 )
		bSizer3811.Add( self.m_staticText1691, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.txPlayerName = wx.TextCtrl( self.pnASF, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 175,-1 ), 0 )
		self.txPlayerName.SetMaxLength( 0 ) 
		bSizer3811.Add( self.txPlayerName, 0, wx.ALL, 5 )
		
		
		bSizer385.Add( bSizer3811, 0, wx.SHAPED, 5 )
		
		
		bSizer378.Add( bSizer385, 0, wx.EXPAND, 5 )
		
		bSizer386 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer57 = wx.StaticBoxSizer( wx.StaticBox( self.pnASF, wx.ID_ANY, u"Class" ), wx.VERTICAL )
		
		cxClassChoices = [ u"Barbarian", u"Bard", u"Cleric", u"Druid", u"Fighter", u"Monk", u"Paladin", u"Ranger", u"Rogue", u"Sorcerer", u"Wizard" ]
		self.cxClass = wx.Choice( self.pnASF, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cxClassChoices, 0 )
		self.cxClass.SetSelection( 0 )
		sbSizer57.Add( self.cxClass, 0, wx.ALL, 5 )
		
		
		bSizer386.Add( sbSizer57, 1, wx.EXPAND, 5 )
		
		sbSizer60 = wx.StaticBoxSizer( wx.StaticBox( self.pnASF, wx.ID_ANY, u"Race" ), wx.VERTICAL )
		
		cxRaceChoices = [ u"Human", u"Dwarf", u"Elf", u"Half-Elf", u"Half-Orc", u"Gnome", u"Halfling" ]
		self.cxRace = wx.Choice( self.pnASF, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cxRaceChoices, 0 )
		self.cxRace.SetSelection( 0 )
		sbSizer60.Add( self.cxRace, 0, wx.ALL, 5 )
		
		
		bSizer386.Add( sbSizer60, 1, wx.EXPAND, 5 )
		
		sbSizer61 = wx.StaticBoxSizer( wx.StaticBox( self.pnASF, wx.ID_ANY, u"Gender" ), wx.VERTICAL )
		
		cxGenderChoices = [ u"Male", u"Female" ]
		self.cxGender = wx.Choice( self.pnASF, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cxGenderChoices, 0 )
		self.cxGender.SetSelection( 0 )
		sbSizer61.Add( self.cxGender, 0, wx.ALL, 5 )
		
		
		bSizer386.Add( sbSizer61, 1, wx.EXPAND, 5 )
		
		sbSizer58 = wx.StaticBoxSizer( wx.StaticBox( self.pnASF, wx.ID_ANY, u"Level" ), wx.VERTICAL )
		
		self.spLevel = wx.SpinCtrl( self.pnASF, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 1, 20, 1 )
		sbSizer58.Add( self.spLevel, 0, wx.ALL, 5 )
		
		
		bSizer386.Add( sbSizer58, 1, wx.EXPAND, 5 )
		
		sbSizer59 = wx.StaticBoxSizer( wx.StaticBox( self.pnASF, wx.ID_ANY, u"Alignment" ), wx.VERTICAL )
		
		cxAlignmentChoices = [ u"Lawful Good", u"Lawful Neutral", u"Lawful Evil", u"Neutral Good", u"Neutral", u"Neutral Evil", u"Chaotic Good", u"Chaotic Neutral", u"Chaotic Evil" ]
		self.cxAlignment = wx.Choice( self.pnASF, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cxAlignmentChoices, 0 )
		self.cxAlignment.SetSelection( 0 )
		sbSizer59.Add( self.cxAlignment, 0, wx.ALL, 5 )
		
		
		bSizer386.Add( sbSizer59, 1, wx.EXPAND, 5 )
		
		
		bSizer378.Add( bSizer386, 0, wx.SHAPED, 5 )
		
		bSizer406 = wx.BoxSizer( wx.HORIZONTAL )
		
		szAbilityScores = wx.StaticBoxSizer( wx.StaticBox( self.pnASF, wx.ID_ANY, u"Ability Scores" ), wx.VERTICAL )
		
		bSizer394 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText178 = wx.StaticText( self.pnASF, wx.ID_ANY, u"Strength (STR)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText178.Wrap( -1 )
		bSizer394.Add( self.m_staticText178, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_spinCtrl60 = wx.SpinCtrl( self.pnASF, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 3, 30, 12 )
		bSizer394.Add( self.m_spinCtrl60, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		szAbilityScores.Add( bSizer394, 0, wx.EXPAND, 5 )
		
		bSizer3941 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1781 = wx.StaticText( self.pnASF, wx.ID_ANY, u"Dexterity (DEX)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1781.Wrap( -1 )
		bSizer3941.Add( self.m_staticText1781, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_spinCtrl601 = wx.SpinCtrl( self.pnASF, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 3, 30, 12 )
		bSizer3941.Add( self.m_spinCtrl601, 0, wx.ALL, 5 )
		
		
		szAbilityScores.Add( bSizer3941, 0, wx.EXPAND, 5 )
		
		bSizer3942 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1782 = wx.StaticText( self.pnASF, wx.ID_ANY, u"Constitution (CON)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1782.Wrap( -1 )
		bSizer3942.Add( self.m_staticText1782, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_spinCtrl602 = wx.SpinCtrl( self.pnASF, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 3, 30, 12 )
		bSizer3942.Add( self.m_spinCtrl602, 0, wx.ALL, 5 )
		
		
		szAbilityScores.Add( bSizer3942, 0, wx.EXPAND, 5 )
		
		bSizer3943 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1783 = wx.StaticText( self.pnASF, wx.ID_ANY, u"Intelligence (INT)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1783.Wrap( -1 )
		bSizer3943.Add( self.m_staticText1783, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_spinCtrl603 = wx.SpinCtrl( self.pnASF, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 3, 30, 12 )
		bSizer3943.Add( self.m_spinCtrl603, 0, wx.ALL, 5 )
		
		
		szAbilityScores.Add( bSizer3943, 0, wx.EXPAND, 5 )
		
		bSizer3944 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1784 = wx.StaticText( self.pnASF, wx.ID_ANY, u"Wisdom (WIS)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1784.Wrap( -1 )
		bSizer3944.Add( self.m_staticText1784, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_spinCtrl604 = wx.SpinCtrl( self.pnASF, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 3, 30, 12 )
		bSizer3944.Add( self.m_spinCtrl604, 0, wx.ALL, 5 )
		
		
		szAbilityScores.Add( bSizer3944, 0, wx.EXPAND, 5 )
		
		bSizer3945 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1785 = wx.StaticText( self.pnASF, wx.ID_ANY, u"Charisma (CHA)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1785.Wrap( -1 )
		bSizer3945.Add( self.m_staticText1785, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_spinCtrl605 = wx.SpinCtrl( self.pnASF, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 3, 30, 12 )
		bSizer3945.Add( self.m_spinCtrl605, 0, wx.ALL, 5 )
		
		
		szAbilityScores.Add( bSizer3945, 0, wx.EXPAND, 5 )
		
		
		bSizer406.Add( szAbilityScores, 0, 0, 5 )
		
		bSizer440 = wx.BoxSizer( wx.VERTICAL )
		
		szSavingThrows = wx.StaticBoxSizer( wx.StaticBox( self.pnASF, wx.ID_ANY, u"Saving Throws" ), wx.VERTICAL )
		
		bSizer407 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer415 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText185 = wx.StaticText( self.pnASF, wx.ID_ANY, u"Saving Throw:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText185.Wrap( -1 )
		bSizer415.Add( self.m_staticText185, 0, wx.ALL, 5 )
		
		
		bSizer407.Add( bSizer415, 0, wx.EXPAND, 5 )
		
		bSizer416 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stTotal = wx.StaticText( self.pnASF, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stTotal.Wrap( -1 )
		bSizer416.Add( self.stTotal, 0, wx.ALL, 5 )
		
		self.m_staticText187 = wx.StaticText( self.pnASF, wx.ID_ANY, u"=", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText187.Wrap( -1 )
		bSizer416.Add( self.m_staticText187, 0, wx.ALL, 5 )
		
		self.stAbilityMod = wx.StaticText( self.pnASF, wx.ID_ANY, u"Base Save", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.stAbilityMod.Wrap( 20 )
		bSizer416.Add( self.stAbilityMod, 3, wx.ALL, 5 )
		
		self.m_staticText195 = wx.StaticText( self.pnASF, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText195.Wrap( -1 )
		bSizer416.Add( self.m_staticText195, 1, wx.ALL, 5 )
		
		self.m_staticText190 = wx.StaticText( self.pnASF, wx.ID_ANY, u"Ability Modifier", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText190.Wrap( 16 )
		bSizer416.Add( self.m_staticText190, 3, wx.ALL, 5 )
		
		self.m_staticText191 = wx.StaticText( self.pnASF, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText191.Wrap( -1 )
		bSizer416.Add( self.m_staticText191, 1, wx.ALL, 5 )
		
		self.m_staticText194 = wx.StaticText( self.pnASF, wx.ID_ANY, u"Modifier", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText194.Wrap( 20 )
		bSizer416.Add( self.m_staticText194, 3, wx.ALL, 5 )
		
		self.m_staticText193 = wx.StaticText( self.pnASF, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText193.Wrap( -1 )
		bSizer416.Add( self.m_staticText193, 1, wx.ALL, 5 )
		
		self.m_staticText192 = wx.StaticText( self.pnASF, wx.ID_ANY, u"Magic Modifier", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText192.Wrap( 20 )
		bSizer416.Add( self.m_staticText192, 3, wx.ALL, 5 )
		
		self.m_staticText189 = wx.StaticText( self.pnASF, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText189.Wrap( -1 )
		bSizer416.Add( self.m_staticText189, 1, wx.ALL, 5 )
		
		self.m_staticText196 = wx.StaticText( self.pnASF, wx.ID_ANY, u"Other Modifier", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText196.Wrap( 20 )
		bSizer416.Add( self.m_staticText196, 3, wx.ALL, 5 )
		
		
		bSizer407.Add( bSizer416, 0, wx.EXPAND, 5 )
		
		
		szSavingThrows.Add( bSizer407, 1, wx.EXPAND, 5 )
		
		bSizer4071 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer4151 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1851 = wx.StaticText( self.pnASF, wx.ID_ANY, u"Fortitude:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1851.Wrap( -1 )
		bSizer4151.Add( self.m_staticText1851, 1, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		bSizer4071.Add( bSizer4151, 1, 0, 5 )
		
		bSizer4161 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stTotalFORT = wx.StaticText( self.pnASF, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stTotalFORT.Wrap( -1 )
		bSizer4161.Add( self.stTotalFORT, 0, wx.ALL, 5 )
		
		self.m_staticText1871 = wx.StaticText( self.pnASF, wx.ID_ANY, u"=", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1871.Wrap( -1 )
		bSizer4161.Add( self.m_staticText1871, 0, wx.ALL, 5 )
		
		self.stBaseFORT = wx.StaticText( self.pnASF, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.stBaseFORT.Wrap( 20 )
		bSizer4161.Add( self.stBaseFORT, 3, wx.ALL, 5 )
		
		self.m_staticText1951 = wx.StaticText( self.pnASF, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1951.Wrap( -1 )
		bSizer4161.Add( self.m_staticText1951, 1, wx.ALL, 5 )
		
		self.stAbilityFORT = wx.StaticText( self.pnASF, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.stAbilityFORT.Wrap( 16 )
		bSizer4161.Add( self.stAbilityFORT, 3, wx.ALL, 5 )
		
		self.m_staticText1911 = wx.StaticText( self.pnASF, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1911.Wrap( -1 )
		bSizer4161.Add( self.m_staticText1911, 1, wx.ALL, 5 )
		
		self.stModFORT = wx.StaticText( self.pnASF, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.stModFORT.Wrap( 20 )
		bSizer4161.Add( self.stModFORT, 3, wx.ALL, 5 )
		
		self.m_staticText1931 = wx.StaticText( self.pnASF, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1931.Wrap( -1 )
		bSizer4161.Add( self.m_staticText1931, 1, wx.ALL, 5 )
		
		self.stMagicFORT = wx.StaticText( self.pnASF, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.stMagicFORT.Wrap( 20 )
		bSizer4161.Add( self.stMagicFORT, 3, wx.ALL, 5 )
		
		self.m_staticText1891 = wx.StaticText( self.pnASF, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1891.Wrap( -1 )
		bSizer4161.Add( self.m_staticText1891, 1, wx.ALL, 5 )
		
		self.spOtherFORT = wx.SpinCtrl( self.pnASF, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer4161.Add( self.spOtherFORT, 0, wx.ALL, 5 )
		
		
		bSizer4071.Add( bSizer4161, 6, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		szSavingThrows.Add( bSizer4071, 1, wx.EXPAND, 5 )
		
		bSizer40711 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer41511 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText18511 = wx.StaticText( self.pnASF, wx.ID_ANY, u"Reflex:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18511.Wrap( -1 )
		bSizer41511.Add( self.m_staticText18511, 1, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		bSizer40711.Add( bSizer41511, 1, 0, 5 )
		
		bSizer41611 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stTotalREF = wx.StaticText( self.pnASF, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stTotalREF.Wrap( -1 )
		bSizer41611.Add( self.stTotalREF, 0, wx.ALL, 5 )
		
		self.m_staticText18711 = wx.StaticText( self.pnASF, wx.ID_ANY, u"=", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18711.Wrap( -1 )
		bSizer41611.Add( self.m_staticText18711, 0, wx.ALL, 5 )
		
		self.stBaseREF = wx.StaticText( self.pnASF, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.stBaseREF.Wrap( 20 )
		bSizer41611.Add( self.stBaseREF, 3, wx.ALL, 5 )
		
		self.m_staticText19511 = wx.StaticText( self.pnASF, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19511.Wrap( -1 )
		bSizer41611.Add( self.m_staticText19511, 1, wx.ALL, 5 )
		
		self.stAbilityREF = wx.StaticText( self.pnASF, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.stAbilityREF.Wrap( 16 )
		bSizer41611.Add( self.stAbilityREF, 3, wx.ALL, 5 )
		
		self.m_staticText19111 = wx.StaticText( self.pnASF, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19111.Wrap( -1 )
		bSizer41611.Add( self.m_staticText19111, 1, wx.ALL, 5 )
		
		self.stModREF = wx.StaticText( self.pnASF, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.stModREF.Wrap( 20 )
		bSizer41611.Add( self.stModREF, 3, wx.ALL, 5 )
		
		self.m_staticText19311 = wx.StaticText( self.pnASF, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19311.Wrap( -1 )
		bSizer41611.Add( self.m_staticText19311, 1, wx.ALL, 5 )
		
		self.stMagicREF = wx.StaticText( self.pnASF, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.stMagicREF.Wrap( 20 )
		bSizer41611.Add( self.stMagicREF, 3, wx.ALL, 5 )
		
		self.m_staticText18911 = wx.StaticText( self.pnASF, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18911.Wrap( -1 )
		bSizer41611.Add( self.m_staticText18911, 1, wx.ALL, 5 )
		
		self.spOtherREF = wx.SpinCtrl( self.pnASF, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer41611.Add( self.spOtherREF, 0, wx.ALL, 5 )
		
		
		bSizer40711.Add( bSizer41611, 6, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		szSavingThrows.Add( bSizer40711, 1, wx.EXPAND, 5 )
		
		bSizer407111 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer415111 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText185111 = wx.StaticText( self.pnASF, wx.ID_ANY, u"Will:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText185111.Wrap( -1 )
		bSizer415111.Add( self.m_staticText185111, 1, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		bSizer407111.Add( bSizer415111, 1, 0, 5 )
		
		bSizer416111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stTotalWILL = wx.StaticText( self.pnASF, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stTotalWILL.Wrap( -1 )
		bSizer416111.Add( self.stTotalWILL, 0, wx.ALL, 5 )
		
		self.m_staticText187111 = wx.StaticText( self.pnASF, wx.ID_ANY, u"=", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText187111.Wrap( -1 )
		bSizer416111.Add( self.m_staticText187111, 0, wx.ALL, 5 )
		
		self.stBaseWILL = wx.StaticText( self.pnASF, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.stBaseWILL.Wrap( 20 )
		bSizer416111.Add( self.stBaseWILL, 3, wx.ALL, 5 )
		
		self.m_staticText195111 = wx.StaticText( self.pnASF, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText195111.Wrap( -1 )
		bSizer416111.Add( self.m_staticText195111, 1, wx.ALL, 5 )
		
		self.stAbilityWILL = wx.StaticText( self.pnASF, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.stAbilityWILL.Wrap( 16 )
		bSizer416111.Add( self.stAbilityWILL, 3, wx.ALL, 5 )
		
		self.m_staticText191111 = wx.StaticText( self.pnASF, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText191111.Wrap( -1 )
		bSizer416111.Add( self.m_staticText191111, 1, wx.ALL, 5 )
		
		self.stModWILL = wx.StaticText( self.pnASF, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.stModWILL.Wrap( 20 )
		bSizer416111.Add( self.stModWILL, 3, wx.ALL, 5 )
		
		self.m_staticText193111 = wx.StaticText( self.pnASF, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText193111.Wrap( -1 )
		bSizer416111.Add( self.m_staticText193111, 1, wx.ALL, 5 )
		
		self.stMagicWILL = wx.StaticText( self.pnASF, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.stMagicWILL.Wrap( 20 )
		bSizer416111.Add( self.stMagicWILL, 3, wx.ALL, 5 )
		
		self.m_staticText189111 = wx.StaticText( self.pnASF, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText189111.Wrap( -1 )
		bSizer416111.Add( self.m_staticText189111, 1, wx.ALL, 5 )
		
		self.spOtherWILL = wx.SpinCtrl( self.pnASF, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer416111.Add( self.spOtherWILL, 0, wx.ALL, 5 )
		
		
		bSizer407111.Add( bSizer416111, 6, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		szSavingThrows.Add( bSizer407111, 1, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		
		bSizer440.Add( szSavingThrows, 1, wx.EXPAND, 5 )
		
		bSizer441 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer440.Add( bSizer441, 1, wx.EXPAND, 5 )
		
		
		bSizer406.Add( bSizer440, 1, wx.EXPAND, 5 )
		
		
		bSizer378.Add( bSizer406, 0, wx.EXPAND, 5 )
		
		
		self.pnASF.SetSizer( bSizer378 )
		self.pnASF.Layout()
		bSizer378.Fit( self.pnASF )
		self.nbMainNotebook.AddPage( self.pnASF, u"Abilities, Skills, and Feats", True )
		self.pnSheet = wx.Panel( self.nbMainNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.nbMainNotebook.AddPage( self.pnSheet, u"Character Sheet", False )
		
		bSizer376.Add( self.nbMainNotebook, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer376 )
		self.Layout()
		bSizer376.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class PC_5_GeneratorBase
###########################################################################

class PC_5_GeneratorBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Fifth Edition PC/NPC Generator", pos = wx.DefaultPosition, size = wx.Size( 720,415 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer376 = wx.BoxSizer( wx.VERTICAL )
		
		self.nbMainNotebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pnASF = wx.Panel( self.nbMainNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer378 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer385 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer381 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText169 = wx.StaticText( self.pnASF, wx.ID_ANY, u"Character Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText169.Wrap( -1 )
		bSizer381.Add( self.m_staticText169, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.txCharacterName = wx.TextCtrl( self.pnASF, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 175,-1 ), 0 )
		self.txCharacterName.SetMaxLength( 0 ) 
		bSizer381.Add( self.txCharacterName, 0, wx.ALL, 5 )
		
		self.bRandomName = wx.Button( self.pnASF, wx.ID_ANY, u"Random", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer381.Add( self.bRandomName, 0, wx.ALL, 5 )
		
		
		bSizer385.Add( bSizer381, 0, 0, 5 )
		
		bSizer3811 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1691 = wx.StaticText( self.pnASF, wx.ID_ANY, u"Player Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1691.Wrap( -1 )
		bSizer3811.Add( self.m_staticText1691, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.txPlayerName = wx.TextCtrl( self.pnASF, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 175,-1 ), 0 )
		self.txPlayerName.SetMaxLength( 0 ) 
		bSizer3811.Add( self.txPlayerName, 0, wx.ALL, 5 )
		
		
		bSizer385.Add( bSizer3811, 0, wx.SHAPED, 5 )
		
		
		bSizer378.Add( bSizer385, 0, wx.EXPAND, 5 )
		
		bSizer386 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer57 = wx.StaticBoxSizer( wx.StaticBox( self.pnASF, wx.ID_ANY, u"Class" ), wx.VERTICAL )
		
		cxClassChoices = [ u"Barbarian", u"Bard", u"Cleric", u"Druid", u"Fighter", u"Monk", u"Paladin", u"Ranger", u"Rogue", u"Sorcerer", u"Wizard" ]
		self.cxClass = wx.Choice( self.pnASF, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cxClassChoices, 0 )
		self.cxClass.SetSelection( 0 )
		sbSizer57.Add( self.cxClass, 0, wx.ALL, 5 )
		
		
		bSizer386.Add( sbSizer57, 1, wx.EXPAND, 5 )
		
		sbSizer60 = wx.StaticBoxSizer( wx.StaticBox( self.pnASF, wx.ID_ANY, u"Race" ), wx.VERTICAL )
		
		cxRaceChoices = [ u"Human", u"Dwarf", u"Elf", u"Half-Elf", u"Half-Orc", u"Gnome", u"Halfling" ]
		self.cxRace = wx.Choice( self.pnASF, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cxRaceChoices, 0 )
		self.cxRace.SetSelection( 0 )
		sbSizer60.Add( self.cxRace, 0, wx.ALL, 5 )
		
		
		bSizer386.Add( sbSizer60, 1, wx.EXPAND, 5 )
		
		sbSizer61 = wx.StaticBoxSizer( wx.StaticBox( self.pnASF, wx.ID_ANY, u"Gender" ), wx.VERTICAL )
		
		cxGenderChoices = [ u"Male", u"Female" ]
		self.cxGender = wx.Choice( self.pnASF, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cxGenderChoices, 0 )
		self.cxGender.SetSelection( 0 )
		sbSizer61.Add( self.cxGender, 0, wx.ALL, 5 )
		
		
		bSizer386.Add( sbSizer61, 1, wx.EXPAND, 5 )
		
		sbSizer58 = wx.StaticBoxSizer( wx.StaticBox( self.pnASF, wx.ID_ANY, u"Level" ), wx.VERTICAL )
		
		self.spLevel = wx.SpinCtrl( self.pnASF, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 1, 20, 1 )
		sbSizer58.Add( self.spLevel, 0, wx.ALL, 5 )
		
		
		bSizer386.Add( sbSizer58, 1, wx.EXPAND, 5 )
		
		sbSizer59 = wx.StaticBoxSizer( wx.StaticBox( self.pnASF, wx.ID_ANY, u"Alignment" ), wx.VERTICAL )
		
		cxAlignmentChoices = [ u"Lawful Good", u"Lawful Neutral", u"Lawful Evil", u"Neutral Good", u"Neutral", u"Neutral Evil", u"Chaotic Good", u"Chaotic Neutral", u"Chaotic Evil" ]
		self.cxAlignment = wx.Choice( self.pnASF, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cxAlignmentChoices, 0 )
		self.cxAlignment.SetSelection( 0 )
		sbSizer59.Add( self.cxAlignment, 0, wx.ALL, 5 )
		
		
		bSizer386.Add( sbSizer59, 1, wx.EXPAND, 5 )
		
		
		bSizer378.Add( bSizer386, 0, wx.SHAPED, 5 )
		
		bSizer406 = wx.BoxSizer( wx.HORIZONTAL )
		
		szAbilityScores = wx.StaticBoxSizer( wx.StaticBox( self.pnASF, wx.ID_ANY, u"Ability Scores" ), wx.VERTICAL )
		
		bSizer394 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText178 = wx.StaticText( self.pnASF, wx.ID_ANY, u"Strength (STR)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText178.Wrap( -1 )
		bSizer394.Add( self.m_staticText178, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_spinCtrl60 = wx.SpinCtrl( self.pnASF, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 3, 20, 12 )
		bSizer394.Add( self.m_spinCtrl60, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		szAbilityScores.Add( bSizer394, 0, wx.EXPAND, 5 )
		
		bSizer3941 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1781 = wx.StaticText( self.pnASF, wx.ID_ANY, u"Dexterity (DEX)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1781.Wrap( -1 )
		bSizer3941.Add( self.m_staticText1781, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_spinCtrl601 = wx.SpinCtrl( self.pnASF, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 3, 20, 12 )
		bSizer3941.Add( self.m_spinCtrl601, 0, wx.ALL, 5 )
		
		
		szAbilityScores.Add( bSizer3941, 0, wx.EXPAND, 5 )
		
		bSizer3942 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1782 = wx.StaticText( self.pnASF, wx.ID_ANY, u"Constitution (CON)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1782.Wrap( -1 )
		bSizer3942.Add( self.m_staticText1782, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_spinCtrl602 = wx.SpinCtrl( self.pnASF, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 3, 20, 12 )
		bSizer3942.Add( self.m_spinCtrl602, 0, wx.ALL, 5 )
		
		
		szAbilityScores.Add( bSizer3942, 0, wx.EXPAND, 5 )
		
		bSizer3943 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1783 = wx.StaticText( self.pnASF, wx.ID_ANY, u"Intelligence (INT)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1783.Wrap( -1 )
		bSizer3943.Add( self.m_staticText1783, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_spinCtrl603 = wx.SpinCtrl( self.pnASF, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 3, 20, 12 )
		bSizer3943.Add( self.m_spinCtrl603, 0, wx.ALL, 5 )
		
		
		szAbilityScores.Add( bSizer3943, 0, wx.EXPAND, 5 )
		
		bSizer3944 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1784 = wx.StaticText( self.pnASF, wx.ID_ANY, u"Wisdom (WIS)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1784.Wrap( -1 )
		bSizer3944.Add( self.m_staticText1784, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_spinCtrl604 = wx.SpinCtrl( self.pnASF, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 3, 20, 12 )
		bSizer3944.Add( self.m_spinCtrl604, 0, wx.ALL, 5 )
		
		
		szAbilityScores.Add( bSizer3944, 0, wx.EXPAND, 5 )
		
		bSizer3945 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1785 = wx.StaticText( self.pnASF, wx.ID_ANY, u"Charisma (CHA)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1785.Wrap( -1 )
		bSizer3945.Add( self.m_staticText1785, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_spinCtrl605 = wx.SpinCtrl( self.pnASF, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 3, 20, 12 )
		bSizer3945.Add( self.m_spinCtrl605, 0, wx.ALL, 5 )
		
		
		szAbilityScores.Add( bSizer3945, 0, wx.EXPAND, 5 )
		
		
		bSizer406.Add( szAbilityScores, 0, 0, 5 )
		
		bSizer440 = wx.BoxSizer( wx.VERTICAL )
		
		szSavingThrows = wx.StaticBoxSizer( wx.StaticBox( self.pnASF, wx.ID_ANY, u"Saving Throws and Skills" ), wx.VERTICAL )
		
		bSizer441 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText452 = wx.StaticText( self.pnASF, wx.ID_ANY, u"Proficiency bonus:  +2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText452.Wrap( -1 )
		bSizer441.Add( self.m_staticText452, 0, wx.ALL, 5 )
		
		self.cb_SaveSTR = wx.CheckBox( self.pnASF, wx.ID_ANY, u"STR: +0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer441.Add( self.cb_SaveSTR, 0, wx.ALL, 5 )
		
		self.cb_SaveDEX = wx.CheckBox( self.pnASF, wx.ID_ANY, u"DEX: +0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer441.Add( self.cb_SaveDEX, 0, wx.ALL, 5 )
		
		self.cb_SaveCON = wx.CheckBox( self.pnASF, wx.ID_ANY, u"CON: +0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer441.Add( self.cb_SaveCON, 0, wx.ALL, 5 )
		
		self.cb_SaveINT = wx.CheckBox( self.pnASF, wx.ID_ANY, u"INT: +0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer441.Add( self.cb_SaveINT, 0, wx.ALL, 5 )
		
		self.cb_SaveWIS = wx.CheckBox( self.pnASF, wx.ID_ANY, u"WIS: +0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer441.Add( self.cb_SaveWIS, 0, wx.ALL, 5 )
		
		self.cb_SaveCHA = wx.CheckBox( self.pnASF, wx.ID_ANY, u"CHA: +0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer441.Add( self.cb_SaveCHA, 0, wx.ALL, 5 )
		
		
		szSavingThrows.Add( bSizer441, 1, wx.EXPAND, 5 )
		
		
		bSizer440.Add( szSavingThrows, 1, wx.EXPAND, 5 )
		
		
		bSizer406.Add( bSizer440, 1, wx.EXPAND, 5 )
		
		szAbilities = wx.StaticBoxSizer( wx.StaticBox( self.pnASF, wx.ID_ANY, u"Abilities" ), wx.HORIZONTAL )
		
		bSizer579 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_checkBox86 = wx.CheckBox( self.pnASF, wx.ID_ANY, u"Acrobatics", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox86.SetToolTip( u"DEX" )
		
		bSizer579.Add( self.m_checkBox86, 0, wx.ALL, 5 )
		
		self.m_checkBox88 = wx.CheckBox( self.pnASF, wx.ID_ANY, u"Animal Handling", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox88.SetToolTip( u"WIS" )
		
		bSizer579.Add( self.m_checkBox88, 0, wx.ALL, 5 )
		
		self.m_checkBox89 = wx.CheckBox( self.pnASF, wx.ID_ANY, u"Arcana", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox89.SetToolTip( u"INT" )
		
		bSizer579.Add( self.m_checkBox89, 0, wx.ALL, 5 )
		
		self.m_checkBox90 = wx.CheckBox( self.pnASF, wx.ID_ANY, u"Athletics", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox90.SetToolTip( u"STR" )
		
		bSizer579.Add( self.m_checkBox90, 0, wx.ALL, 5 )
		
		self.m_checkBox91 = wx.CheckBox( self.pnASF, wx.ID_ANY, u"Deception", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox91.SetToolTip( u"CHA" )
		
		bSizer579.Add( self.m_checkBox91, 0, wx.ALL, 5 )
		
		self.m_checkBox92 = wx.CheckBox( self.pnASF, wx.ID_ANY, u"History", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox92.SetToolTip( u"INT" )
		
		bSizer579.Add( self.m_checkBox92, 0, wx.ALL, 5 )
		
		self.m_checkBox93 = wx.CheckBox( self.pnASF, wx.ID_ANY, u"Insight", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox93.SetToolTip( u"WIS" )
		
		bSizer579.Add( self.m_checkBox93, 0, wx.ALL, 5 )
		
		self.m_checkBox94 = wx.CheckBox( self.pnASF, wx.ID_ANY, u"Intimidation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox94.SetToolTip( u"CHA" )
		
		bSizer579.Add( self.m_checkBox94, 0, wx.ALL, 5 )
		
		self.m_checkBox95 = wx.CheckBox( self.pnASF, wx.ID_ANY, u"Investigation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox95.SetToolTip( u"INT" )
		
		bSizer579.Add( self.m_checkBox95, 0, wx.ALL, 5 )
		
		
		szAbilities.Add( bSizer579, 1, wx.EXPAND, 5 )
		
		bSizer580 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_checkBox87 = wx.CheckBox( self.pnASF, wx.ID_ANY, u"Medicine", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox87.SetToolTip( u"WIS" )
		
		bSizer580.Add( self.m_checkBox87, 0, wx.ALL, 5 )
		
		self.m_checkBox96 = wx.CheckBox( self.pnASF, wx.ID_ANY, u"Nature", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox96.SetToolTip( u"INT" )
		
		bSizer580.Add( self.m_checkBox96, 0, wx.ALL, 5 )
		
		self.m_checkBox97 = wx.CheckBox( self.pnASF, wx.ID_ANY, u"Perception", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox97.SetToolTip( u"WIS" )
		
		bSizer580.Add( self.m_checkBox97, 0, wx.ALL, 5 )
		
		self.m_checkBox98 = wx.CheckBox( self.pnASF, wx.ID_ANY, u"Performance", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox98.SetToolTip( u"CHA" )
		
		bSizer580.Add( self.m_checkBox98, 0, wx.ALL, 5 )
		
		self.m_checkBox99 = wx.CheckBox( self.pnASF, wx.ID_ANY, u"Persuasion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox99.SetToolTip( u"CHA" )
		
		bSizer580.Add( self.m_checkBox99, 0, wx.ALL, 5 )
		
		self.m_checkBox100 = wx.CheckBox( self.pnASF, wx.ID_ANY, u"Religion", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox100.SetToolTip( u"INT" )
		
		bSizer580.Add( self.m_checkBox100, 0, wx.ALL, 5 )
		
		self.m_checkBox101 = wx.CheckBox( self.pnASF, wx.ID_ANY, u"Sleight of Hand", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox101.SetToolTip( u"DEX" )
		
		bSizer580.Add( self.m_checkBox101, 0, wx.ALL, 5 )
		
		self.m_checkBox102 = wx.CheckBox( self.pnASF, wx.ID_ANY, u"Stealth", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox102.SetToolTip( u"DEX" )
		
		bSizer580.Add( self.m_checkBox102, 0, wx.ALL, 5 )
		
		self.m_checkBox103 = wx.CheckBox( self.pnASF, wx.ID_ANY, u"Survival", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox103.SetToolTip( u"WIS" )
		
		bSizer580.Add( self.m_checkBox103, 0, wx.ALL, 5 )
		
		
		szAbilities.Add( bSizer580, 1, wx.EXPAND, 5 )
		
		
		bSizer406.Add( szAbilities, 1, wx.EXPAND, 5 )
		
		
		bSizer378.Add( bSizer406, 0, wx.EXPAND, 5 )
		
		
		self.pnASF.SetSizer( bSizer378 )
		self.pnASF.Layout()
		bSizer378.Fit( self.pnASF )
		self.nbMainNotebook.AddPage( self.pnASF, u"Abilities, Skills, and Feats", True )
		self.pnSheet = wx.Panel( self.nbMainNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.nbMainNotebook.AddPage( self.pnSheet, u"Character Sheet", False )
		
		bSizer376.Add( self.nbMainNotebook, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer376 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class ManifestPreviewDialogBase
###########################################################################

class ManifestPreviewDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tileset Manifest Preview", pos = wx.DefaultPosition, size = wx.Size( 425,624 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer406 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer407 = wx.BoxSizer( wx.VERTICAL )
		
		self.pnPagePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 425,550 ), wx.TAB_TRAVERSAL )
		self.pnPagePanel.SetBackgroundColour( wx.Colour( 128, 128, 128 ) )
		
		bSizer407.Add( self.pnPagePanel, 1, wx.ALL|wx.EXPAND|wx.FIXED_MINSIZE, 10 )
		
		
		bSizer406.Add( bSizer407, 0, wx.EXPAND|wx.FIXED_MINSIZE, 5 )
		
		bSizer408 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer410 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stNumPages = wx.StaticText( self, wx.ID_ANY, u"0 Pages", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stNumPages.Wrap( -1 )
		bSizer410.Add( self.stNumPages, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT|wx.SHAPED, 10 )
		
		self.bFirstPage = wx.Button( self, wx.ID_ANY, u"<<", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.bFirstPage.Enable( False )
		self.bFirstPage.SetToolTip( u"Go to first page" )
		
		bSizer410.Add( self.bFirstPage, 0, 0, 5 )
		
		self.bPreviousPage = wx.Button( self, wx.ID_ANY, u"<", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.bPreviousPage.Enable( False )
		self.bPreviousPage.SetToolTip( u"Go to previous page" )
		
		bSizer410.Add( self.bPreviousPage, 0, 0, 5 )
		
		self.bNextPage = wx.Button( self, wx.ID_ANY, u">", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.bNextPage.Enable( False )
		self.bNextPage.SetToolTip( u"Go to next page" )
		
		bSizer410.Add( self.bNextPage, 0, 0, 5 )
		
		self.bLastPage = wx.Button( self, wx.ID_ANY, u">>", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.bLastPage.Enable( False )
		self.bLastPage.SetToolTip( u"Go to last page" )
		
		bSizer410.Add( self.bLastPage, 0, 0, 5 )
		
		
		bSizer408.Add( bSizer410, 2, wx.EXPAND, 5 )
		
		bSizer409 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bPrint = wx.Button( self, wx.ID_ANY, u"Print", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bPrint.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.bPrint.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.bPrint.SetBackgroundColour( wx.Colour( 0, 64, 0 ) )
		self.bPrint.SetToolTip( u"Print the document" )
		
		bSizer409.Add( self.bPrint, 1, wx.ALIGN_RIGHT, 5 )
		
		self.bCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bCancel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.bCancel.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bCancel.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		self.bCancel.SetToolTip( u"Cancel printing" )
		
		bSizer409.Add( self.bCancel, 1, wx.ALIGN_RIGHT, 5 )
		
		
		bSizer408.Add( bSizer409, 1, 0, 5 )
		
		
		bSizer406.Add( bSizer408, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer406 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_PAINT, self.OnPaint )
		self.bFirstPage.Bind( wx.EVT_BUTTON, self.GoToFirstPage )
		self.bPreviousPage.Bind( wx.EVT_BUTTON, self.GoToPreviousPage )
		self.bNextPage.Bind( wx.EVT_BUTTON, self.GoToNextPage )
		self.bLastPage.Bind( wx.EVT_BUTTON, self.GoToLastPage )
		self.bPrint.Bind( wx.EVT_BUTTON, self.OnPrint )
		self.bCancel.Bind( wx.EVT_BUTTON, self.OnCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnPaint( self, event ):
		event.Skip()
	
	def GoToFirstPage( self, event ):
		event.Skip()
	
	def GoToPreviousPage( self, event ):
		event.Skip()
	
	def GoToNextPage( self, event ):
		event.Skip()
	
	def GoToLastPage( self, event ):
		event.Skip()
	
	def OnPrint( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class ImportTilesDialogBase
###########################################################################

class ImportTilesDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Create and Edit Tileset", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )
		
		szrTilesets = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer10 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		bClearSelection1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer219 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bLoadTileset = wx.Button( self, wx.ID_ANY, u"Load Tileset...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bLoadTileset.SetDefault() 
		bSizer219.Add( self.bLoadTileset, 1, wx.ALL, 0 )
		
		self.bSaveTileset = wx.Button( self, wx.ID_ANY, u"Save Tileset", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bSaveTileset.SetDefault() 
		self.bSaveTileset.Enable( False )
		
		bSizer219.Add( self.bSaveTileset, 1, 0, 0 )
		
		
		bClearSelection1.Add( bSizer219, 0, wx.EXPAND, 5 )
		
		bSizer33 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Tileset Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		bSizer33.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.txTilesetName = wx.TextCtrl( self, wx.ID_ANY, u"Tileset Name", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.txTilesetName.SetMaxLength( 0 ) 
		bSizer33.Add( self.txTilesetName, 0, 0, 0 )
		
		
		bClearSelection1.Add( bSizer33, 0, wx.ALL, 4 )
		
		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Tileset ID:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		bSizer34.Add( self.m_staticText14, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.txTilesetID = wx.TextCtrl( self, wx.ID_ANY, u"SetID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txTilesetID.SetMaxLength( 0 ) 
		self.txTilesetID.SetToolTip( u"Enter the Set ID here.  This is also the folder name where the tiles are stored." )
		
		bSizer34.Add( self.txTilesetID, 0, 0, 0 )
		
		
		bClearSelection1.Add( bSizer34, 0, wx.ALL, 4 )
		
		bSizer35 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Number of Sets Owned:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		bSizer35.Add( self.m_staticText15, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.spNumSets = wx.SpinCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 1, 0, 0 )
		bSizer35.Add( self.spNumSets, 0, 0, 0 )
		
		
		bClearSelection1.Add( bSizer35, 0, wx.ALL, 4 )
		
		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"Current Tileset:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		bClearSelection1.Add( self.m_staticText16, 0, wx.ALL, 3 )
		
		self.stCurrentTilesetName = wx.StaticText( self, wx.ID_ANY, u"No tileset selected", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stCurrentTilesetName.Wrap( -1 )
		bClearSelection1.Add( self.stCurrentTilesetName, 0, wx.LEFT, 10 )
		
		lbTilesetBoxChoices = []
		self.lbTilesetBox = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 225, 200 ), lbTilesetBoxChoices, wx.LB_SINGLE )
		self.lbTilesetBox.SetToolTip( u"Lists all tiles currently part of the active tileset" )
		
		bClearSelection1.Add( self.lbTilesetBox, 6, wx.TOP, 5 )
		
		bSizer36 = wx.BoxSizer( wx.VERTICAL )
		
		self.bClearTileSelection = wx.Button( self, wx.ID_ANY, u"Clear Tile Selection", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bClearTileSelection.SetDefault() 
		self.bClearTileSelection.Enable( False )
		
		bSizer36.Add( self.bClearTileSelection, 0, wx.EXPAND, 10 )
		
		self.bUpdateTile = wx.Button( self, wx.ID_ANY, u"Update Selected Tile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bUpdateTile.SetDefault() 
		self.bUpdateTile.Enable( False )
		self.bUpdateTile.SetToolTip( u"Update the above selected tile with values at right" )
		
		bSizer36.Add( self.bUpdateTile, 0, wx.EXPAND, 1 )
		
		self.bRemoveTile = wx.Button( self, wx.ID_ANY, u"Remove Selected Tile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bRemoveTile.SetDefault() 
		self.bRemoveTile.Enable( False )
		
		bSizer36.Add( self.bRemoveTile, 0, 0, 10 )
		
		
		bClearSelection1.Add( bSizer36, 0, wx.ALIGN_CENTRE_HORIZONTAL, 0 )
		
		
		sbSizer10.Add( bClearSelection1, 0, 0, 0 )
		
		
		szrTilesets.Add( sbSizer10, 0, 0, 0 )
		
		bSizer98 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ID_OK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_OK.SetDefault() 
		self.ID_OK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_OK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.ID_OK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer98.Add( self.ID_OK, 0, wx.RIGHT, 2 )
		
		self.ID_CANCEL = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_CANCEL.SetDefault() 
		self.ID_CANCEL.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_CANCEL.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ID_CANCEL.SetBackgroundColour( wx.Colour( 128, 0, 64 ) )
		
		bSizer98.Add( self.ID_CANCEL, 0, wx.LEFT|wx.RIGHT, 2 )
		
		self.bHelp = wx.Button( self, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bHelp.SetDefault() 
		self.bHelp.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bHelp.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bHelp.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer98.Add( self.bHelp, 0, wx.LEFT, 2 )
		
		
		szrTilesets.Add( bSizer98, 1, wx.EXPAND|wx.TOP, 5 )
		
		
		bSizer13.Add( szrTilesets, 0, wx.EXPAND, 5 )
		
		szrTiles = wx.BoxSizer( wx.VERTICAL )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer218 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bAddImages = wx.Button( self, wx.ID_ANY, u"Add Images...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bAddImages.SetDefault() 
		bSizer218.Add( self.bAddImages, 0, wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.bRemoveImage = wx.Button( self, wx.ID_ANY, u"Remove Image", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bRemoveImage.SetDefault() 
		self.bRemoveImage.Enable( False )
		
		bSizer218.Add( self.bRemoveImage, 0, wx.ALL, 2 )
		
		self.bClearImageSelection = wx.Button( self, wx.ID_ANY, u"Clear Selection", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer218.Add( self.bClearImageSelection, 0, wx.ALL, 2 )
		
		
		bSizer14.Add( bSizer218, 0, wx.EXPAND, 5 )
		
		bSizer365 = wx.BoxSizer( wx.VERTICAL )
		
		ImageListBoxChoices = []
		self.ImageListBox = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), ImageListBoxChoices, wx.LB_NEEDED_SB|wx.LB_SINGLE )
		self.ImageListBox.SetToolTip( u"List of available images to include in the tileset" )
		
		bSizer365.Add( self.ImageListBox, 1, wx.EXPAND, 0 )
		
		
		bSizer14.Add( bSizer365, 1, wx.EXPAND, 5 )
		
		
		szrTiles.Add( bSizer14, 1, wx.EXPAND, 0 )
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Tile Images" ), wx.VERTICAL )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Number of duplicate tiles in this set:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer24.Add( self.m_staticText8, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 3 )
		
		self.spTileCount = wx.SpinCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 1, 99, 1 )
		bSizer24.Add( self.spTileCount, 0, 0, 0 )
		
		
		sbSizer4.Add( bSizer24, 0, wx.ALL, 3 )
		
		bSizer367 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stXSize = wx.StaticText( self, wx.ID_ANY, u"X Size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stXSize.Wrap( -1 )
		bSizer26.Add( self.stXSize, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.spXSize = wx.SpinCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 1, 99, 1 )
		bSizer26.Add( self.spXSize, 0, 0, 0 )
		
		self.stSquaresXText = wx.StaticText( self, wx.ID_ANY, u"squares", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stSquaresXText.Wrap( 0 )
		bSizer26.Add( self.stSquaresXText, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 4 )
		
		
		bSizer367.Add( bSizer26, 1, wx.ALL, 4 )
		
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stYSize = wx.StaticText( self, wx.ID_ANY, u"Y Size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stYSize.Wrap( -1 )
		bSizer25.Add( self.stYSize, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.spYSize = wx.SpinCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 1, 99, 1 )
		bSizer25.Add( self.spYSize, 0, 0, 0 )
		
		self.stSquaresYText = wx.StaticText( self, wx.ID_ANY, u"squares", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stSquaresYText.Wrap( 0 )
		bSizer25.Add( self.stSquaresYText, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 4 )
		
		
		bSizer367.Add( bSizer25, 1, wx.ALL, 4 )
		
		
		sbSizer4.Add( bSizer367, 0, wx.EXPAND, 5 )
		
		bSizer373 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer60 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Image Preview" ), wx.VERTICAL )
		
		self.pnImagePreview = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		self.pnImagePreview.SetBackgroundColour( wx.Colour( 58, 118, 118 ) )
		
		sbSizer60.Add( self.pnImagePreview, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.stImageSize = wx.StaticText( self, wx.ID_ANY, u"Image Size", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stImageSize.Wrap( -1 )
		sbSizer60.Add( self.stImageSize, 0, wx.ALL, 2 )
		
		
		bSizer373.Add( sbSizer60, 1, wx.EXPAND, 5 )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.bSetImageSideA = wx.Button( self, wx.ID_ANY, u"Set Image Side A", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bSetImageSideA.SetDefault() 
		self.bSetImageSideA.SetBackgroundColour( wx.Colour( 255, 255, 202 ) )
		self.bSetImageSideA.SetToolTip( u"Assign the currently selected image to side A" )
		
		bSizer17.Add( self.bSetImageSideA, 0, wx.EXPAND|wx.TOP, 3 )
		
		self.bRemoveImageSideA = wx.Button( self, wx.ID_ANY, u"Clear Side A", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bRemoveImageSideA.SetDefault() 
		self.bRemoveImageSideA.SetBackgroundColour( wx.Colour( 255, 255, 202 ) )
		
		bSizer17.Add( self.bRemoveImageSideA, 0, wx.EXPAND, 3 )
		
		
		bSizer16.Add( bSizer17, 1, wx.ALL|wx.EXPAND, 4 )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.bSetImageSideB = wx.Button( self, wx.ID_ANY, u"Set Image Side B", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bSetImageSideB.SetDefault() 
		self.bSetImageSideB.SetBackgroundColour( wx.Colour( 202, 202, 255 ) )
		self.bSetImageSideB.SetToolTip( u"Assign the currently selected image to side B" )
		
		bSizer18.Add( self.bSetImageSideB, 0, wx.EXPAND|wx.TOP, 3 )
		
		self.bRemoveImageSideB = wx.Button( self, wx.ID_ANY, u"Clear Side B", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bRemoveImageSideB.SetDefault() 
		self.bRemoveImageSideB.SetBackgroundColour( wx.Colour( 202, 202, 255 ) )
		
		bSizer18.Add( self.bRemoveImageSideB, 0, wx.EXPAND, 3 )
		
		
		bSizer16.Add( bSizer18, 1, wx.ALL|wx.EXPAND, 4 )
		
		bSizer19 = wx.BoxSizer( wx.VERTICAL )
		
		self.bSwapImageSides = wx.Button( self, wx.ID_ANY, u"Swap A && B Images", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bSwapImageSides.SetDefault() 
		bSizer19.Add( self.bSwapImageSides, 0, wx.EXPAND, 0 )
		
		self.bRefreshTilePanels = wx.Button( self, wx.ID_ANY, u"Refresh Images", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bRefreshTilePanels.SetDefault() 
		self.bRefreshTilePanels.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bRefreshTilePanels.SetBackgroundColour( wx.Colour( 0, 0, 160 ) )
		
		bSizer19.Add( self.bRefreshTilePanels, 0, wx.EXPAND, 0 )
		
		
		bSizer16.Add( bSizer19, 1, wx.ALL|wx.EXPAND, 4 )
		
		
		sbSizer5.Add( bSizer16, 1, wx.EXPAND, 0 )
		
		self.bAddCurrentToTileset = wx.Button( self, wx.ID_ANY, u"Add New Tile to Set", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bAddCurrentToTileset.SetDefault() 
		self.bAddCurrentToTileset.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.bAddCurrentToTileset.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.bAddCurrentToTileset.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		self.bAddCurrentToTileset.SetToolTip( u"Add the tile to the tileset with the given attributes" )
		
		sbSizer5.Add( self.bAddCurrentToTileset, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 4 )
		
		
		bSizer373.Add( sbSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL, 0 )
		
		
		sbSizer4.Add( bSizer373, 1, wx.EXPAND, 5 )
		
		
		bSizer15.Add( sbSizer4, 0, wx.EXPAND, 0 )
		
		bSizer366 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer368 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer59 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Optional Names" ), wx.VERTICAL )
		
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		self.stTileNameA = wx.StaticText( self, wx.ID_ANY, u"Tile Name Side A:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stTileNameA.Wrap( -1 )
		bSizer21.Add( self.stTileNameA, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.TileNameA = wx.TextCtrl( self, wx.ID_ANY, u"SideA Tile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TileNameA.SetMaxLength( 0 ) 
		bSizer21.Add( self.TileNameA, 1, wx.EXPAND|wx.EXPAND, 0 )
		
		
		sbSizer59.Add( bSizer21, 0, wx.ALL|wx.EXPAND, 2 )
		
		bSizer22 = wx.BoxSizer( wx.VERTICAL )
		
		self.stTileNameB = wx.StaticText( self, wx.ID_ANY, u"Tile Name Side B:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stTileNameB.Wrap( -1 )
		bSizer22.Add( self.stTileNameB, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.TileNameB = wx.TextCtrl( self, wx.ID_ANY, u"SideB Tile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TileNameB.SetMaxLength( 0 ) 
		bSizer22.Add( self.TileNameB, 1, wx.EXPAND|wx.EXPAND, 0 )
		
		
		sbSizer59.Add( bSizer22, 0, wx.ALL|wx.EXPAND, 2 )
		
		
		bSizer368.Add( sbSizer59, 1, wx.EXPAND, 5 )
		
		
		bSizer366.Add( bSizer368, 1, wx.EXPAND, 5 )
		
		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Optional tile attributes" ), wx.VERTICAL )
		
		self.bSetWallsSideA = wx.ToggleButton( self, wx.ID_ANY, u"Set tags for Side A", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer7.Add( self.bSetWallsSideA, 0, 0, 0 )
		
		self.bSetWallsSideB = wx.ToggleButton( self, wx.ID_ANY, u"Set tags for Side B", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bSetWallsSideB.SetValue( True ) 
		sbSizer7.Add( self.bSetWallsSideB, 0, wx.TOP, 5 )
		
		self.bmpLineTypes = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"artwork/LineDefinitions.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 140,100 ), 0 )
		sbSizer7.Add( self.bmpLineTypes, 0, wx.TOP, 5 )
		
		self.bAddFilterTags = wx.Button( self, wx.ID_ANY, u"Add Tile Filter Tags...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bAddFilterTags.SetDefault() 
		self.bAddFilterTags.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bAddFilterTags.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		sbSizer7.Add( self.bAddFilterTags, 0, wx.TOP, 5 )
		
		
		bSizer366.Add( sbSizer7, 0, 0, 0 )
		
		
		bSizer15.Add( bSizer366, 1, wx.EXPAND, 5 )
		
		
		szrTiles.Add( bSizer15, 0, 0, 0 )
		
		
		bSizer13.Add( szrTiles, 0, wx.EXPAND, 5 )
		
		szrImages = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Side A Image:" ), wx.VERTICAL )
		
		self.SideAImagePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,300 ), wx.DOUBLE_BORDER )
		self.SideAImagePanel.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.SideAImagePanel.SetBackgroundColour( wx.Colour( 255, 255, 202 ) )
		
		sbSizer8.Add( self.SideAImagePanel, 0, 0, 0 )
		
		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bZoomInSideA = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/ZoomIn.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bZoomInSideA.SetDefault() 
		self.bZoomInSideA.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bZoomInSideA.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer29.Add( self.bZoomInSideA, 0, wx.ALIGN_CENTER_HORIZONTAL, 0 )
		
		self.bZoomOutSideA = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/ZoomOut.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bZoomOutSideA.SetDefault() 
		bSizer29.Add( self.bZoomOutSideA, 0, 0, 0 )
		
		self.cpkSideAGridColor = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 255, 0, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		self.cpkSideAGridColor.SetToolTip( u"Grid color for Side A.  Click to change." )
		
		bSizer29.Add( self.cpkSideAGridColor, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
		
		
		sbSizer8.Add( bSizer29, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 3 )
		
		
		szrImages.Add( sbSizer8, 0, 0, 0 )
		
		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Side B Image:" ), wx.VERTICAL )
		
		self.SideBImagePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,300 ), wx.DOUBLE_BORDER )
		self.SideBImagePanel.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.SideBImagePanel.SetBackgroundColour( wx.Colour( 202, 202, 255 ) )
		
		sbSizer9.Add( self.SideBImagePanel, 0, 0, 0 )
		
		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bZoomInSideB = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/ZoomIn.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bZoomInSideB.SetDefault() 
		self.bZoomInSideB.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bZoomInSideB.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer30.Add( self.bZoomInSideB, 0, 0, 0 )
		
		self.bZoomOutSideB = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/ZoomOut.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bZoomOutSideB.SetDefault() 
		bSizer30.Add( self.bZoomOutSideB, 0, wx.ALIGN_CENTRE, 0 )
		
		self.cpkSideBGridColor = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 255, 0, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		self.cpkSideBGridColor.SetToolTip( u"Grid Color for Side B.  Click to change." )
		
		bSizer30.Add( self.cpkSideBGridColor, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
		
		
		sbSizer9.Add( bSizer30, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 3 )
		
		
		szrImages.Add( sbSizer9, 0, 0, 0 )
		
		
		bSizer13.Add( szrImages, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer13 )
		self.Layout()
		bSizer13.Fit( self )
		
		# Connect Events
		self.bLoadTileset.Bind( wx.EVT_BUTTON, self.LoadTileset )
		self.bSaveTileset.Bind( wx.EVT_BUTTON, self.SaveTileset )
		self.lbTilesetBox.Bind( wx.EVT_LISTBOX, self.OnTilesetBox )
		self.bClearTileSelection.Bind( wx.EVT_BUTTON, self.OnClearTileSelection )
		self.bUpdateTile.Bind( wx.EVT_BUTTON, self.OnUpdateTile )
		self.bRemoveTile.Bind( wx.EVT_BUTTON, self.OnRemoveTile )
		self.ID_OK.Bind( wx.EVT_BUTTON, self.OnOK )
		self.ID_CANCEL.Bind( wx.EVT_BUTTON, self.OnCancel )
		self.bHelp.Bind( wx.EVT_BUTTON, self.OnHelp )
		self.bAddImages.Bind( wx.EVT_BUTTON, self.AddImages )
		self.bRemoveImage.Bind( wx.EVT_BUTTON, self.RemoveImage )
		self.bClearImageSelection.Bind( wx.EVT_BUTTON, self.OnClearImageSelection )
		self.ImageListBox.Bind( wx.EVT_LISTBOX, self.OnImageListBox )
		self.spXSize.Bind( wx.EVT_SPINCTRL, self.SetXSize )
		self.spYSize.Bind( wx.EVT_SPINCTRL, self.SetYSize )
		self.bSetImageSideA.Bind( wx.EVT_BUTTON, self.SetImageSideA )
		self.bRemoveImageSideA.Bind( wx.EVT_BUTTON, self.RemoveImageSideA )
		self.bSetImageSideB.Bind( wx.EVT_BUTTON, self.SetImageSideB )
		self.bRemoveImageSideB.Bind( wx.EVT_BUTTON, self.RemoveImageSideB )
		self.bSwapImageSides.Bind( wx.EVT_BUTTON, self.SwapImageSides )
		self.bRefreshTilePanels.Bind( wx.EVT_BUTTON, self.RefreshImages )
		self.bAddCurrentToTileset.Bind( wx.EVT_BUTTON, self.AddCurrentTile )
		self.bSetWallsSideA.Bind( wx.EVT_TOGGLEBUTTON, self.DrawImagePanels )
		self.bSetWallsSideB.Bind( wx.EVT_TOGGLEBUTTON, self.DrawImagePanels )
		self.bAddFilterTags.Bind( wx.EVT_BUTTON, self.AddFilterTags )
		self.SideAImagePanel.Bind( wx.EVT_LEFT_UP, self.OnPanelAClick )
		self.bZoomInSideA.Bind( wx.EVT_BUTTON, self.ZoomInPanelSideA )
		self.bZoomOutSideA.Bind( wx.EVT_BUTTON, self.ZoomOutPanelSideA )
		self.cpkSideAGridColor.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnChangeGridColor )
		self.SideBImagePanel.Bind( wx.EVT_LEFT_UP, self.OnPanelBClick )
		self.bZoomInSideB.Bind( wx.EVT_BUTTON, self.ZoomInPanelSideB )
		self.bZoomOutSideB.Bind( wx.EVT_BUTTON, self.ZoomOutPanelSideB )
		self.cpkSideBGridColor.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnChangeGridColor )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def LoadTileset( self, event ):
		event.Skip()
	
	def SaveTileset( self, event ):
		event.Skip()
	
	def OnTilesetBox( self, event ):
		event.Skip()
	
	def OnClearTileSelection( self, event ):
		event.Skip()
	
	def OnUpdateTile( self, event ):
		event.Skip()
	
	def OnRemoveTile( self, event ):
		event.Skip()
	
	def OnOK( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		event.Skip()
	
	def OnHelp( self, event ):
		event.Skip()
	
	def AddImages( self, event ):
		event.Skip()
	
	def RemoveImage( self, event ):
		event.Skip()
	
	def OnClearImageSelection( self, event ):
		event.Skip()
	
	def OnImageListBox( self, event ):
		event.Skip()
	
	def SetXSize( self, event ):
		event.Skip()
	
	def SetYSize( self, event ):
		event.Skip()
	
	def SetImageSideA( self, event ):
		event.Skip()
	
	def RemoveImageSideA( self, event ):
		event.Skip()
	
	def SetImageSideB( self, event ):
		event.Skip()
	
	def RemoveImageSideB( self, event ):
		event.Skip()
	
	def SwapImageSides( self, event ):
		event.Skip()
	
	def RefreshImages( self, event ):
		event.Skip()
	
	def AddCurrentTile( self, event ):
		event.Skip()
	
	def DrawImagePanels( self, event ):
		event.Skip()
	
	
	def AddFilterTags( self, event ):
		event.Skip()
	
	def OnPanelAClick( self, event ):
		event.Skip()
	
	def ZoomInPanelSideA( self, event ):
		event.Skip()
	
	def ZoomOutPanelSideA( self, event ):
		event.Skip()
	
	def OnChangeGridColor( self, event ):
		event.Skip()
	
	def OnPanelBClick( self, event ):
		event.Skip()
	
	def ZoomInPanelSideB( self, event ):
		event.Skip()
	
	def ZoomOutPanelSideB( self, event ):
		event.Skip()
	
	

###########################################################################
## Class TilesetBuilderDialogCore
###########################################################################

class TilesetBuilderDialogCore ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tileset Builder Image Extractor", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetToolTip( u"Browse in the tiles folder" )
		
		bSizer160 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer173 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer172 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText72 = wx.StaticText( self, wx.ID_ANY, u"Tileset Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText72.Wrap( -1 )
		bSizer172.Add( self.m_staticText72, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.txTilesetName = wx.TextCtrl( self, wx.ID_ANY, u"Tileset Name", wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		self.txTilesetName.SetMaxLength( 0 ) 
		self.txTilesetName.SetToolTip( u"This is the name of the tileset." )
		
		bSizer172.Add( self.txTilesetName, 0, wx.ALL, 5 )
		
		
		bSizer173.Add( bSizer172, 0, wx.EXPAND, 5 )
		
		bSizer174 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText73 = wx.StaticText( self, wx.ID_ANY, u"Tileset ID:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText73.Wrap( -1 )
		bSizer174.Add( self.m_staticText73, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.txFolderID = wx.TextCtrl( self, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txFolderID.SetMaxLength( 0 ) 
		self.txFolderID.SetToolTip( u"This is the folder name where images are stored in the tiles folder" )
		
		bSizer174.Add( self.txFolderID, 0, wx.ALL, 5 )
		
		
		bSizer173.Add( bSizer174, 0, wx.EXPAND, 5 )
		
		
		bSizer160.Add( bSizer173, 0, 0, 5 )
		
		bSizer161 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSideASizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Side A" ), wx.VERTICAL )
		
		bSizer165 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer405 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2231 = wx.StaticText( self, wx.ID_ANY, u"Choose Image File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2231.Wrap( -1 )
		bSizer405.Add( self.m_staticText2231, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.fpkLoadSideA = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select Image for Front Side", u"Image Files (*.jpg, *.png)|*.jpg; *.png", wx.DefaultPosition, wx.DefaultSize, wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN )
		self.fpkLoadSideA.SetToolTip( u"Select for front side image" )
		
		bSizer405.Add( self.fpkLoadSideA, 0, wx.ALL, 5 )
		
		self.bDefineTileA = wx.Button( self, wx.ID_ANY, u"Define tile", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer405.Add( self.bDefineTileA, 0, wx.ALL, 5 )
		
		
		bSizer165.Add( bSizer405, 1, wx.EXPAND, 5 )
		
		bSizer404 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText223 = wx.StaticText( self, wx.ID_ANY, u"Image resolution 100 pixels per square", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText223.Wrap( -1 )
		bSizer404.Add( self.m_staticText223, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.bChangeResolutionA = wx.Button( self, wx.ID_ANY, u"Change...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer404.Add( self.bChangeResolutionA, 0, wx.ALL, 5 )
		
		
		bSizer165.Add( bSizer404, 1, wx.EXPAND, 5 )
		
		
		sbSideASizer.Add( bSizer165, 0, wx.EXPAND, 5 )
		
		self.scrImageA = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,300 ), wx.ALWAYS_SHOW_SB|wx.HSCROLL|wx.SUNKEN_BORDER|wx.VSCROLL )
		self.scrImageA.SetScrollRate( 5, 5 )
		self.scrImageA.SetBackgroundColour( wx.Colour( 64, 128, 128 ) )
		
		sbSideASizer.Add( self.scrImageA, 0, wx.ALL, 5 )
		
		bSizer181 = wx.BoxSizer( wx.VERTICAL )
		
		
		sbSideASizer.Add( bSizer181, 1, wx.EXPAND, 5 )
		
		bSizer222 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bZoomInA = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/ZoomIn.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bZoomInA.SetDefault() 
		self.bZoomInA.SetToolTip( u"Zoom In" )
		
		bSizer222.Add( self.bZoomInA, 0, wx.RIGHT, 5 )
		
		self.bZoomOutA = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/ZoomOut.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bZoomOutA.SetDefault() 
		self.bZoomOutA.SetToolTip( u"Zoom Out" )
		
		bSizer222.Add( self.bZoomOutA, 0, wx.LEFT, 5 )
		
		
		sbSideASizer.Add( bSizer222, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer161.Add( sbSideASizer, 0, wx.ALL, 5 )
		
		sbSideBSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Side B" ), wx.VERTICAL )
		
		bSizer1651 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer406 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2241 = wx.StaticText( self, wx.ID_ANY, u"Choose Image File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2241.Wrap( 55 )
		bSizer406.Add( self.m_staticText2241, 0, wx.ALL, 5 )
		
		self.fpkLoadSideB = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"Image Files (*.jpg, *.png)|*.jpg; *.png", wx.DefaultPosition, wx.DefaultSize, wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN )
		bSizer406.Add( self.fpkLoadSideB, 0, wx.ALIGN_BOTTOM|wx.ALL, 2 )
		
		self.bDefineTileB = wx.Button( self, wx.ID_ANY, u"Define tile", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer406.Add( self.bDefineTileB, 0, wx.ALIGN_BOTTOM|wx.ALL, 2 )
		
		self.tgSideB = wx.ToggleButton( self, wx.ID_ANY, u"Turn off side B", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tgSideB.SetToolTip( u"Toggle this button on if there is no side B image." )
		
		bSizer406.Add( self.tgSideB, 0, wx.ALIGN_BOTTOM|wx.ALL, 2 )
		
		
		bSizer1651.Add( bSizer406, 1, wx.EXPAND, 5 )
		
		bSizer407 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText224 = wx.StaticText( self, wx.ID_ANY, u"Image resolution 100 pixels per square", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText224.Wrap( -1 )
		bSizer407.Add( self.m_staticText224, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.bChangeResolutionB = wx.Button( self, wx.ID_ANY, u"Change...", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer407.Add( self.bChangeResolutionB, 0, wx.ALL, 5 )
		
		
		bSizer1651.Add( bSizer407, 1, wx.EXPAND, 5 )
		
		
		sbSideBSizer.Add( bSizer1651, 0, wx.EXPAND, 5 )
		
		self.scrImageB = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,300 ), wx.ALWAYS_SHOW_SB|wx.HSCROLL|wx.SUNKEN_BORDER|wx.VSCROLL )
		self.scrImageB.SetScrollRate( 5, 5 )
		self.scrImageB.SetBackgroundColour( wx.Colour( 64, 128, 128 ) )
		
		sbSideBSizer.Add( self.scrImageB, 0, wx.ALL, 5 )
		
		bSizer2221 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bZoomInB = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/ZoomIn.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bZoomInB.SetDefault() 
		self.bZoomInB.SetToolTip( u"Zoom In" )
		
		bSizer2221.Add( self.bZoomInB, 0, wx.RIGHT, 5 )
		
		self.bZoomOutB = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/ZoomOut.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bZoomOutB.SetDefault() 
		self.bZoomOutB.SetToolTip( u"Zoom Out" )
		
		bSizer2221.Add( self.bZoomOutB, 0, wx.LEFT, 5 )
		
		
		sbSideBSizer.Add( bSizer2221, 0, wx.ALIGN_CENTER, 5 )
		
		
		bSizer161.Add( sbSideBSizer, 0, wx.ALL, 5 )
		
		sbTilesetSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Tileset" ), wx.VERTICAL )
		
		self.bAddTile = wx.Button( self, wx.ID_ANY, u"Add current selection to tileset", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbTilesetSizer.Add( self.bAddTile, 0, wx.ALL, 5 )
		
		lbTilesetBoxChoices = []
		self.lbTilesetBox = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,100 ), lbTilesetBoxChoices, wx.LB_SINGLE )
		self.lbTilesetBox.SetToolTip( u"List of tiles in tileset.  Select to see the tile below." )
		
		sbTilesetSizer.Add( self.lbTilesetBox, 0, wx.ALL, 5 )
		
		self.bDeleteSelection = wx.Button( self, wx.ID_ANY, u"Delete Selection", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bDeleteSelection.Enable( False )
		
		sbTilesetSizer.Add( self.bDeleteSelection, 0, wx.LEFT, 5 )
		
		self.pnSelectedTile = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,200 ), wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		self.pnSelectedTile.SetBackgroundColour( wx.Colour( 64, 128, 128 ) )
		self.pnSelectedTile.SetToolTip( u"Display selected tile from the tileset" )
		
		sbTilesetSizer.Add( self.pnSelectedTile, 0, wx.ALL, 5 )
		
		self.bSaveTileset = wx.Button( self, wx.ID_ANY, u"Save Tileset File...", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbTilesetSizer.Add( self.bSaveTileset, 0, wx.LEFT, 5 )
		
		
		bSizer161.Add( sbTilesetSizer, 0, wx.ALL, 5 )
		
		
		bSizer160.Add( bSizer161, 1, wx.EXPAND, 5 )
		
		bSizer178 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer160.Add( bSizer178, 0, wx.EXPAND, 5 )
		
		bSizer179 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText71 = wx.StaticText( self, wx.ID_ANY, u"Step 1: Enter a tileset name and ID for the group of tiles.  Images will be copied into the tiles folder, with the ID being the subfolder.  The ID will also be the base filename for the new images.\nStep 1:  Load images for side A and side B.\nStep 2:  Press 'Define Tile' to define the border for each side of the tile.\nStep 3:  Change the height and width of the tile as necessary.\nStep 4:  Press 'Add Tile' to add the tile to the master list.\n", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		bSizer179.Add( self.m_staticText71, 0, wx.ALL, 5 )
		
		
		bSizer160.Add( bSizer179, 0, wx.EXPAND, 5 )
		
		bSizer98 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bOK.SetDefault() 
		self.bOK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bOK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.bOK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer98.Add( self.bOK, 0, wx.RIGHT, 3 )
		
		self.bCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bCancel.SetDefault() 
		self.bCancel.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bCancel.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bCancel.SetBackgroundColour( wx.Colour( 128, 0, 64 ) )
		
		bSizer98.Add( self.bCancel, 0, wx.LEFT|wx.RIGHT, 3 )
		
		self.bHelp = wx.Button( self, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bHelp.SetDefault() 
		self.bHelp.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bHelp.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bHelp.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer98.Add( self.bHelp, 0, wx.LEFT, 3 )
		
		
		bSizer160.Add( bSizer98, 0, wx.ALIGN_CENTER, 5 )
		
		
		self.SetSizer( bSizer160 )
		self.Layout()
		bSizer160.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.fpkLoadSideA.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnLoadSideA )
		self.bDefineTileA.Bind( wx.EVT_BUTTON, self.OnDefineTileA )
		self.bChangeResolutionA.Bind( wx.EVT_BUTTON, self.OnChangeResolutionA )
		self.bZoomInA.Bind( wx.EVT_BUTTON, self.OnZoomInA )
		self.bZoomOutA.Bind( wx.EVT_BUTTON, self.OnZoomOutA )
		self.bDefineTileB.Bind( wx.EVT_BUTTON, self.OnDefineTileB )
		self.tgSideB.Bind( wx.EVT_TOGGLEBUTTON, self.OnDeactivateSideB )
		self.bChangeResolutionB.Bind( wx.EVT_BUTTON, self.OnChangeResolutionB )
		self.bZoomInB.Bind( wx.EVT_BUTTON, self.OnZoomInB )
		self.bZoomOutB.Bind( wx.EVT_BUTTON, self.OnZoomOutB )
		self.bAddTile.Bind( wx.EVT_BUTTON, self.OnAddTile )
		self.lbTilesetBox.Bind( wx.EVT_LISTBOX, self.OnTilesetListbox )
		self.bDeleteSelection.Bind( wx.EVT_BUTTON, self.OnDeleteSelection )
		self.bSaveTileset.Bind( wx.EVT_BUTTON, self.OnSaveTileset )
		self.bOK.Bind( wx.EVT_BUTTON, self.OnOK )
		self.bCancel.Bind( wx.EVT_BUTTON, self.OnCancel )
		self.bHelp.Bind( wx.EVT_BUTTON, self.OnHelp )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnLoadSideA( self, event ):
		event.Skip()
	
	def OnDefineTileA( self, event ):
		event.Skip()
	
	def OnChangeResolutionA( self, event ):
		event.Skip()
	
	def OnZoomInA( self, event ):
		event.Skip()
	
	def OnZoomOutA( self, event ):
		event.Skip()
	
	def OnDefineTileB( self, event ):
		event.Skip()
	
	def OnDeactivateSideB( self, event ):
		event.Skip()
	
	def OnChangeResolutionB( self, event ):
		event.Skip()
	
	def OnZoomInB( self, event ):
		event.Skip()
	
	def OnZoomOutB( self, event ):
		event.Skip()
	
	def OnAddTile( self, event ):
		event.Skip()
	
	def OnTilesetListbox( self, event ):
		event.Skip()
	
	def OnDeleteSelection( self, event ):
		event.Skip()
	
	def OnSaveTileset( self, event ):
		event.Skip()
	
	def OnOK( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		event.Skip()
	
	def OnHelp( self, event ):
		event.Skip()
	

###########################################################################
## Class TilesetEditor2Base
###########################################################################

class TilesetEditor2Base ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tileset Editor", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer415 = wx.BoxSizer( wx.VERTICAL )
		
		self.nbTilesetEditor = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pnSetupTile = wx.Panel( self.nbTilesetEditor, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.pnSetupTile.SetBackgroundColour( wx.Colour( 224, 224, 224 ) )
		
		bSizer544 = wx.BoxSizer( wx.HORIZONTAL )
		
		szrTiles1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer141 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer218 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bAddImages = wx.Button( self.pnSetupTile, wx.ID_ANY, u"Add Images...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bAddImages.SetDefault() 
		bSizer218.Add( self.bAddImages, 0, wx.LEFT|wx.RIGHT|wx.TOP, 2 )
		
		self.bRemoveImage = wx.Button( self.pnSetupTile, wx.ID_ANY, u"Remove Image", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bRemoveImage.SetDefault() 
		self.bRemoveImage.Enable( False )
		
		bSizer218.Add( self.bRemoveImage, 0, wx.ALL, 2 )
		
		self.bClearImageSelection = wx.Button( self.pnSetupTile, wx.ID_ANY, u"Clear Selection", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer218.Add( self.bClearImageSelection, 0, wx.ALL, 2 )
		
		
		bSizer141.Add( bSizer218, 0, wx.EXPAND, 5 )
		
		bSizer3651 = wx.BoxSizer( wx.VERTICAL )
		
		ImageListBox_SetupChoices = []
		self.ImageListBox_Setup = wx.ListBox( self.pnSetupTile, Setup_ImageListBox, wx.DefaultPosition, wx.Size( -1,150 ), ImageListBox_SetupChoices, wx.LB_NEEDED_SB|wx.LB_SINGLE )
		self.ImageListBox_Setup.SetToolTip( u"List of available images to include in the tileset" )
		
		bSizer3651.Add( self.ImageListBox_Setup, 1, wx.EXPAND, 0 )
		
		
		bSizer141.Add( bSizer3651, 1, wx.EXPAND, 5 )
		
		
		szrTiles1.Add( bSizer141, 0, wx.EXPAND, 0 )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.pnSetupTile, wx.ID_ANY, u"Tile Images" ), wx.VERTICAL )
		
		bSizer373 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer601 = wx.StaticBoxSizer( wx.StaticBox( self.pnSetupTile, wx.ID_ANY, u"Image Preview" ), wx.VERTICAL )
		
		self.pnImagePreview_Setup = wx.Panel( self.pnSetupTile, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,200 ), wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		self.pnImagePreview_Setup.SetBackgroundColour( wx.Colour( 58, 118, 118 ) )
		self.pnImagePreview_Setup.SetToolTip( u"Image preview of selected tile" )
		
		sbSizer601.Add( self.pnImagePreview_Setup, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.stImageSize_Setup = wx.StaticText( self.pnSetupTile, wx.ID_ANY, u"Image Size: 0 x 0 pixels", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stImageSize_Setup.Wrap( -1 )
		sbSizer601.Add( self.stImageSize_Setup, 0, wx.ALL, 2 )
		
		
		bSizer373.Add( sbSizer601, 1, wx.EXPAND, 5 )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.pnSetupTile, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.bSetImageSideA = wx.Button( self.pnSetupTile, wx.ID_ANY, u"Set Image for Side A", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bSetImageSideA.SetDefault() 
		self.bSetImageSideA.SetBackgroundColour( wx.Colour( 255, 255, 202 ) )
		self.bSetImageSideA.Enable( False )
		self.bSetImageSideA.SetToolTip( u"Assign the currently selected image to side A" )
		
		bSizer17.Add( self.bSetImageSideA, 0, wx.EXPAND|wx.TOP, 3 )
		
		self.bRemoveImageSideA = wx.Button( self.pnSetupTile, wx.ID_ANY, u"Clear Side A", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bRemoveImageSideA.SetDefault() 
		self.bRemoveImageSideA.SetBackgroundColour( wx.Colour( 255, 255, 202 ) )
		
		bSizer17.Add( self.bRemoveImageSideA, 0, wx.EXPAND, 3 )
		
		
		bSizer16.Add( bSizer17, 1, wx.ALL|wx.EXPAND, 4 )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		self.bSetImageSideB = wx.Button( self.pnSetupTile, wx.ID_ANY, u"Set Image for Side B", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bSetImageSideB.SetDefault() 
		self.bSetImageSideB.SetBackgroundColour( wx.Colour( 202, 202, 255 ) )
		self.bSetImageSideB.Enable( False )
		self.bSetImageSideB.SetToolTip( u"Assign the currently selected image to side B" )
		
		bSizer18.Add( self.bSetImageSideB, 0, wx.EXPAND|wx.TOP, 3 )
		
		self.bRemoveImageSideB = wx.Button( self.pnSetupTile, wx.ID_ANY, u"Clear Side B", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bRemoveImageSideB.SetDefault() 
		self.bRemoveImageSideB.SetBackgroundColour( wx.Colour( 202, 202, 255 ) )
		
		bSizer18.Add( self.bRemoveImageSideB, 0, wx.EXPAND, 3 )
		
		
		bSizer16.Add( bSizer18, 1, wx.ALL|wx.EXPAND, 4 )
		
		bSizer19 = wx.BoxSizer( wx.VERTICAL )
		
		self.bSwapImageSides = wx.Button( self.pnSetupTile, wx.ID_ANY, u"Swap A && B Images", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bSwapImageSides.SetDefault() 
		bSizer19.Add( self.bSwapImageSides, 0, wx.EXPAND, 0 )
		
		self.bRefreshTilePanels = wx.Button( self.pnSetupTile, wx.ID_ANY, u"Refresh Images", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bRefreshTilePanels.SetDefault() 
		self.bRefreshTilePanels.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bRefreshTilePanels.SetBackgroundColour( wx.Colour( 0, 0, 160 ) )
		
		bSizer19.Add( self.bRefreshTilePanels, 0, wx.EXPAND, 0 )
		
		
		bSizer16.Add( bSizer19, 1, wx.ALL|wx.EXPAND, 4 )
		
		
		sbSizer5.Add( bSizer16, 1, wx.EXPAND, 0 )
		
		self.bAddCurrentToTileset = wx.Button( self.pnSetupTile, wx.ID_ANY, u"Add New Tile to Set", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bAddCurrentToTileset.SetDefault() 
		self.bAddCurrentToTileset.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.bAddCurrentToTileset.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.bAddCurrentToTileset.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		self.bAddCurrentToTileset.SetToolTip( u"Add the tile to the tileset with the given attributes" )
		
		sbSizer5.Add( self.bAddCurrentToTileset, 0, wx.ALIGN_CENTER_HORIZONTAL, 4 )
		
		self.bUpdateTile = wx.Button( self.pnSetupTile, wx.ID_ANY, u"Update Tile to Set", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bUpdateTile.SetDefault() 
		self.bUpdateTile.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.bUpdateTile.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.bUpdateTile.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		self.bUpdateTile.Enable( False )
		self.bUpdateTile.SetToolTip( u"Update the selected tile with the given attributes" )
		
		sbSizer5.Add( self.bUpdateTile, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer373.Add( sbSizer5, 0, wx.ALIGN_CENTER_HORIZONTAL, 0 )
		
		
		sbSizer4.Add( bSizer373, 0, wx.EXPAND, 5 )
		
		self.nbOptionalNames = wx.Notebook( self.pnSetupTile, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.pnTileProperties = wx.Panel( self.nbOptionalNames, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer456 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer367 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stXSize = wx.StaticText( self.pnTileProperties, wx.ID_ANY, u"Width:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stXSize.Wrap( -1 )
		bSizer26.Add( self.stXSize, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
		
		self.spXSize = wx.SpinCtrl( self.pnTileProperties, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 1, 99, 1 )
		bSizer26.Add( self.spXSize, 0, 0, 0 )
		
		self.stSquaresXText = wx.StaticText( self.pnTileProperties, wx.ID_ANY, u"squares", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stSquaresXText.Wrap( 0 )
		bSizer26.Add( self.stSquaresXText, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 4 )
		
		
		bSizer367.Add( bSizer26, 1, wx.ALL, 4 )
		
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stYSize = wx.StaticText( self.pnTileProperties, wx.ID_ANY, u"Height:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stYSize.Wrap( -1 )
		bSizer25.Add( self.stYSize, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
		
		self.spYSize = wx.SpinCtrl( self.pnTileProperties, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 1, 99, 1 )
		bSizer25.Add( self.spYSize, 0, 0, 0 )
		
		self.stSquaresYText = wx.StaticText( self.pnTileProperties, wx.ID_ANY, u"squares", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stSquaresYText.Wrap( 0 )
		bSizer25.Add( self.stSquaresYText, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 4 )
		
		
		bSizer367.Add( bSizer25, 1, wx.ALL, 4 )
		
		
		bSizer456.Add( bSizer367, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText8 = wx.StaticText( self.pnTileProperties, wx.ID_ANY, u"Number of duplicate tiles in this set:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer24.Add( self.m_staticText8, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 3 )
		
		self.spTileCount = wx.SpinCtrl( self.pnTileProperties, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 1, 99, 1 )
		bSizer24.Add( self.spTileCount, 0, 0, 0 )
		
		
		bSizer456.Add( bSizer24, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.pnTileProperties.SetSizer( bSizer456 )
		self.pnTileProperties.Layout()
		bSizer456.Fit( self.pnTileProperties )
		self.nbOptionalNames.AddPage( self.pnTileProperties, u"Properties", True )
		self.pnTileNames = wx.Panel( self.nbOptionalNames, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer59 = wx.StaticBoxSizer( wx.StaticBox( self.pnTileNames, wx.ID_ANY, u"Optional Names" ), wx.VERTICAL )
		
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		self.stTileNameA = wx.StaticText( self.pnTileNames, wx.ID_ANY, u"Tile Name Side A:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stTileNameA.Wrap( -1 )
		bSizer21.Add( self.stTileNameA, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.TileNameA = wx.TextCtrl( self.pnTileNames, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TileNameA.SetMaxLength( 0 ) 
		bSizer21.Add( self.TileNameA, 1, wx.EXPAND|wx.EXPAND, 0 )
		
		
		sbSizer59.Add( bSizer21, 0, wx.ALL|wx.EXPAND, 2 )
		
		bSizer22 = wx.BoxSizer( wx.VERTICAL )
		
		self.stTileNameB = wx.StaticText( self.pnTileNames, wx.ID_ANY, u"Tile Name Side B:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stTileNameB.Wrap( -1 )
		bSizer22.Add( self.stTileNameB, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.TileNameB = wx.TextCtrl( self.pnTileNames, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TileNameB.SetMaxLength( 0 ) 
		bSizer22.Add( self.TileNameB, 1, wx.EXPAND|wx.EXPAND, 0 )
		
		
		sbSizer59.Add( bSizer22, 0, wx.ALL|wx.EXPAND, 2 )
		
		
		self.pnTileNames.SetSizer( sbSizer59 )
		self.pnTileNames.Layout()
		sbSizer59.Fit( self.pnTileNames )
		self.nbOptionalNames.AddPage( self.pnTileNames, u"Optional Names", False )
		self.pnTileAttributes = wx.Panel( self.nbOptionalNames, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self.pnTileAttributes, wx.ID_ANY, u"Optional tile attributes" ), wx.HORIZONTAL )
		
		bSizer466 = wx.BoxSizer( wx.VERTICAL )
		
		self.bSetWallsSideA = wx.ToggleButton( self.pnTileAttributes, wx.ID_ANY, u"Set edge types on Side A", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bSetWallsSideA.SetToolTip( u"Click toggle to set edge types " )
		
		bSizer466.Add( self.bSetWallsSideA, 0, 0, 0 )
		
		self.bSetWallsSideB = wx.ToggleButton( self.pnTileAttributes, wx.ID_ANY, u"Set edge types on Side B", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bSetWallsSideB.SetToolTip( u"Click toggle to set edge types " )
		
		bSizer466.Add( self.bSetWallsSideB, 0, wx.TOP, 5 )
		
		self.bAddFilterTags = wx.Button( self.pnTileAttributes, wx.ID_ANY, u"Add Tile Filter Tags...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bAddFilterTags.SetDefault() 
		self.bAddFilterTags.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bAddFilterTags.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		self.bAddFilterTags.SetToolTip( u"Add tags for filtering tiles" )
		
		bSizer466.Add( self.bAddFilterTags, 0, wx.TOP, 5 )
		
		
		sbSizer7.Add( bSizer466, 1, wx.TOP, 5 )
		
		sbSizer811 = wx.StaticBoxSizer( wx.StaticBox( self.pnTileAttributes, wx.ID_ANY, u"Edge Types" ), wx.VERTICAL )
		
		self.bmpLineTypes = wx.StaticBitmap( self.pnTileAttributes, wx.ID_ANY, wx.Bitmap( u"artwork/LineDefinitions.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 112,80 ), 0 )
		sbSizer811.Add( self.bmpLineTypes, 0, 0, 5 )
		
		
		sbSizer7.Add( sbSizer811, 0, 0, 5 )
		
		
		self.pnTileAttributes.SetSizer( sbSizer7 )
		self.pnTileAttributes.Layout()
		sbSizer7.Fit( self.pnTileAttributes )
		self.nbOptionalNames.AddPage( self.pnTileAttributes, u"Optional Attributes", False )
		
		sbSizer4.Add( self.nbOptionalNames, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		szrTiles1.Add( sbSizer4, 1, wx.EXPAND, 0 )
		
		
		bSizer544.Add( szrTiles1, 0, 0, 5 )
		
		szrImages1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer455 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer81 = wx.StaticBoxSizer( wx.StaticBox( self.pnSetupTile, wx.ID_ANY, u"Side A Image:" ), wx.VERTICAL )
		
		self.Setup_SideAImagePanel = wx.Panel( self.pnSetupTile, Setup_ImageA, wx.DefaultPosition, wx.Size( 200,200 ), wx.DOUBLE_BORDER )
		self.Setup_SideAImagePanel.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Setup_SideAImagePanel.SetBackgroundColour( wx.Colour( 255, 255, 202 ) )
		self.Setup_SideAImagePanel.SetToolTip( u"Image for side A" )
		
		sbSizer81.Add( self.Setup_SideAImagePanel, 0, 0, 0 )
		
		bSizer291 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bZoomInSideA1 = wx.BitmapButton( self.pnSetupTile, Setup_ZoomInA, wx.Bitmap( u"artwork/ZoomIn.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bZoomInSideA1.SetDefault() 
		self.bZoomInSideA1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bZoomInSideA1.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer291.Add( self.bZoomInSideA1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0 )
		
		self.bZoomOutSideA1 = wx.BitmapButton( self.pnSetupTile, Setup_ZoomOutA, wx.Bitmap( u"artwork/ZoomOut.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bZoomOutSideA1.SetDefault() 
		bSizer291.Add( self.bZoomOutSideA1, 0, 0, 0 )
		
		self.cpkSideAGridColor_Setup = wx.ColourPickerCtrl( self.pnSetupTile, wx.ID_ANY, wx.Colour( 255, 0, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		self.cpkSideAGridColor_Setup.SetToolTip( u"Grid color for Side A.  Click to change." )
		
		bSizer291.Add( self.cpkSideAGridColor_Setup, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
		
		
		sbSizer81.Add( bSizer291, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 3 )
		
		
		bSizer455.Add( sbSizer81, 0, 0, 0 )
		
		sbSizer91 = wx.StaticBoxSizer( wx.StaticBox( self.pnSetupTile, wx.ID_ANY, u"Side B Image:" ), wx.VERTICAL )
		
		self.Setup_SideBImagePanel = wx.Panel( self.pnSetupTile, Setup_ImageB, wx.DefaultPosition, wx.Size( 200,200 ), wx.DOUBLE_BORDER )
		self.Setup_SideBImagePanel.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Setup_SideBImagePanel.SetBackgroundColour( wx.Colour( 202, 202, 255 ) )
		self.Setup_SideBImagePanel.SetToolTip( u"Image for side B" )
		
		sbSizer91.Add( self.Setup_SideBImagePanel, 0, 0, 0 )
		
		bSizer301 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bZoomInSideB1 = wx.BitmapButton( self.pnSetupTile, Setup_ZoomInB, wx.Bitmap( u"artwork/ZoomIn.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bZoomInSideB1.SetDefault() 
		self.bZoomInSideB1.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bZoomInSideB1.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer301.Add( self.bZoomInSideB1, 0, 0, 0 )
		
		self.bZoomOutSideB1 = wx.BitmapButton( self.pnSetupTile, Setup_ZoomOutB, wx.Bitmap( u"artwork/ZoomOut.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bZoomOutSideB1.SetDefault() 
		bSizer301.Add( self.bZoomOutSideB1, 0, wx.ALIGN_CENTRE, 0 )
		
		self.cpkSideBGridColor_Setup = wx.ColourPickerCtrl( self.pnSetupTile, wx.ID_ANY, wx.Colour( 255, 0, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		self.cpkSideBGridColor_Setup.SetToolTip( u"Grid Color for Side B.  Click to change." )
		
		bSizer301.Add( self.cpkSideBGridColor_Setup, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
		
		
		sbSizer91.Add( bSizer301, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 3 )
		
		
		bSizer455.Add( sbSizer91, 0, 0, 0 )
		
		
		szrImages1.Add( bSizer455, 0, 0, 5 )
		
		sbSizer76 = wx.StaticBoxSizer( wx.StaticBox( self.pnSetupTile, wx.ID_ANY, u"Tiles in the current tileset" ), wx.VERTICAL )
		
		lbSetup_TilesetBoxChoices = []
		self.lbSetup_TilesetBox = wx.ListBox( self.pnSetupTile, Setup_TilesetBox, wx.DefaultPosition, wx.Size( 225, 200 ), lbSetup_TilesetBoxChoices, wx.LB_SINGLE )
		self.lbSetup_TilesetBox.SetToolTip( u"Lists all tiles currently part of the active tileset" )
		
		sbSizer76.Add( self.lbSetup_TilesetBox, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer456 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bSetup_RemoveTile = wx.Button( self.pnSetupTile, Setup_RemoveTile, u"Remove Selected Tile", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bSetup_RemoveTile.SetDefault() 
		self.bSetup_RemoveTile.Enable( False )
		
		bSizer456.Add( self.bSetup_RemoveTile, 0, wx.ALL, 5 )
		
		
		sbSizer76.Add( bSizer456, 1, wx.EXPAND, 5 )
		
		
		szrImages1.Add( sbSizer76, 0, wx.TOP, 5 )
		
		bSizer457 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ID_OK2 = wx.Button( self.pnSetupTile, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_OK2.SetDefault() 
		self.ID_OK2.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_OK2.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.ID_OK2.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer457.Add( self.ID_OK2, 0, wx.ALL, 5 )
		
		self.ID_CANCEL2 = wx.Button( self.pnSetupTile, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_CANCEL2.SetDefault() 
		self.ID_CANCEL2.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_CANCEL2.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ID_CANCEL2.SetBackgroundColour( wx.Colour( 128, 0, 64 ) )
		
		bSizer457.Add( self.ID_CANCEL2, 0, wx.ALL, 5 )
		
		self.bHelpTiles = wx.Button( self.pnSetupTile, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bHelpTiles.SetDefault() 
		self.bHelpTiles.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bHelpTiles.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bHelpTiles.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer457.Add( self.bHelpTiles, 0, wx.ALL, 5 )
		
		
		szrImages1.Add( bSizer457, 0, 0, 5 )
		
		
		bSizer544.Add( szrImages1, 0, 0, 5 )
		
		
		self.pnSetupTile.SetSizer( bSizer544 )
		self.pnSetupTile.Layout()
		bSizer544.Fit( self.pnSetupTile )
		self.nbTilesetEditor.AddPage( self.pnSetupTile, u"Setup Tiles", True )
		self.pnTilesetProperties = wx.Panel( self.nbTilesetEditor, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		szrTilesets = wx.BoxSizer( wx.VERTICAL )
		
		bSizer533 = wx.BoxSizer( wx.HORIZONTAL )
		
		szrTilesetDetails = wx.BoxSizer( wx.VERTICAL )
		
		bSizer465 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText16 = wx.StaticText( self.pnTilesetProperties, wx.ID_ANY, u"Current Tileset:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		bSizer465.Add( self.m_staticText16, 0, wx.ALL, 3 )
		
		self.stCurrentTilesetName = wx.StaticText( self.pnTilesetProperties, wx.ID_ANY, u"No tileset loaded", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stCurrentTilesetName.Wrap( 250 )
		bSizer465.Add( self.stCurrentTilesetName, 0, wx.LEFT, 10 )
		
		
		szrTilesetDetails.Add( bSizer465, 0, wx.BOTTOM|wx.SHAPED, 5 )
		
		bSizer219 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bNewTileset = wx.Button( self.pnTilesetProperties, wx.ID_ANY, u"New Tileset", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer219.Add( self.bNewTileset, 0, wx.ALL, 2 )
		
		self.bLoadTileset = wx.Button( self.pnTilesetProperties, wx.ID_ANY, u"Load Tileset...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bLoadTileset.SetDefault() 
		bSizer219.Add( self.bLoadTileset, 1, wx.ALL, 2 )
		
		self.bSaveTileset = wx.Button( self.pnTilesetProperties, wx.ID_ANY, u"Save Tileset", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bSaveTileset.SetDefault() 
		bSizer219.Add( self.bSaveTileset, 1, wx.ALL, 2 )
		
		
		szrTilesetDetails.Add( bSizer219, 0, wx.EXPAND, 5 )
		
		bSizer33 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText13 = wx.StaticText( self.pnTilesetProperties, wx.ID_ANY, u"Tileset Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		bSizer33.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.txTilesetName = wx.TextCtrl( self.pnTilesetProperties, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.txTilesetName.SetMaxLength( 0 ) 
		self.txTilesetName.SetToolTip( u"Enter a name for the tileset filename" )
		
		bSizer33.Add( self.txTilesetName, 0, wx.LEFT, 5 )
		
		
		szrTilesetDetails.Add( bSizer33, 0, wx.ALL, 4 )
		
		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText14 = wx.StaticText( self.pnTilesetProperties, wx.ID_ANY, u"Tileset ID:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		bSizer34.Add( self.m_staticText14, 0, wx.ALIGN_CENTER_VERTICAL, 0 )
		
		self.txTilesetID = wx.TextCtrl( self.pnTilesetProperties, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txTilesetID.SetMaxLength( 0 ) 
		self.txTilesetID.SetToolTip( u"Enter the Set ID here.  This is also the folder name where the tiles are stored." )
		
		bSizer34.Add( self.txTilesetID, 0, wx.LEFT, 3 )
		
		
		szrTilesetDetails.Add( bSizer34, 0, wx.ALL, 4 )
		
		bSizer35 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText15 = wx.StaticText( self.pnTilesetProperties, wx.ID_ANY, u"Number of Sets Owned:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		bSizer35.Add( self.m_staticText15, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 3 )
		
		self.spNumSets = wx.SpinCtrl( self.pnTilesetProperties, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 1, 99, 1 )
		bSizer35.Add( self.spNumSets, 0, 0, 0 )
		
		
		szrTilesetDetails.Add( bSizer35, 0, wx.ALL, 4 )
		
		sbSizer80 = wx.StaticBoxSizer( wx.StaticBox( self.pnTilesetProperties, wx.ID_ANY, u"Tiles in the current tileset:" ), wx.VERTICAL )
		
		lbTileset_TilesetBoxChoices = []
		self.lbTileset_TilesetBox = wx.ListBox( self.pnTilesetProperties, Tileset_TilesetBox, wx.DefaultPosition, wx.Size( 225, 200 ), lbTileset_TilesetBoxChoices, wx.LB_SINGLE )
		self.lbTileset_TilesetBox.SetToolTip( u"Lists all tiles currently part of the active tileset" )
		
		sbSizer80.Add( self.lbTileset_TilesetBox, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		szrTilesetDetails.Add( sbSizer80, 1, wx.EXPAND|wx.TOP, 10 )
		
		
		bSizer533.Add( szrTilesetDetails, 0, wx.EXPAND, 0 )
		
		szrImagePanels = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( self.pnTilesetProperties, wx.ID_ANY, u"Side A Image:" ), wx.HORIZONTAL )
		
		self.Tileset_SideAImagePanel = wx.Panel( self.pnTilesetProperties, wx.ID_ANY, wx.DefaultPosition, wx.Size( 250,250 ), wx.DOUBLE_BORDER )
		self.Tileset_SideAImagePanel.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Tileset_SideAImagePanel.SetBackgroundColour( wx.Colour( 255, 255, 202 ) )
		
		sbSizer8.Add( self.Tileset_SideAImagePanel, 0, 0, 0 )
		
		bSizer29 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer537 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bZoomInSideA = wx.BitmapButton( self.pnTilesetProperties, Tileset_ZoomInA, wx.Bitmap( u"artwork/ZoomIn.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bZoomInSideA.SetDefault() 
		self.bZoomInSideA.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bZoomInSideA.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer537.Add( self.bZoomInSideA, 0, wx.ALIGN_CENTER_HORIZONTAL, 0 )
		
		self.bZoomOutSideA = wx.BitmapButton( self.pnTilesetProperties, Tileset_ZoomOutA, wx.Bitmap( u"artwork/ZoomOut.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bZoomOutSideA.SetDefault() 
		bSizer537.Add( self.bZoomOutSideA, 0, 0, 0 )
		
		
		bSizer29.Add( bSizer537, 1, wx.EXPAND, 5 )
		
		self.cpkSideAGridColor_Tileset = wx.ColourPickerCtrl( self.pnTilesetProperties, Tileset_SideAGridColor, wx.Colour( 255, 0, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		self.cpkSideAGridColor_Tileset.SetToolTip( u"Grid color for Side A.  Click to change." )
		
		bSizer29.Add( self.cpkSideAGridColor_Tileset, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		sbSizer8.Add( bSizer29, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 3 )
		
		
		szrImagePanels.Add( sbSizer8, 0, 0, 0 )
		
		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self.pnTilesetProperties, wx.ID_ANY, u"Side B Image:" ), wx.HORIZONTAL )
		
		self.Tileset_SideBImagePanel = wx.Panel( self.pnTilesetProperties, wx.ID_ANY, wx.DefaultPosition, wx.Size( 250,250 ), wx.DOUBLE_BORDER )
		self.Tileset_SideBImagePanel.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.Tileset_SideBImagePanel.SetBackgroundColour( wx.Colour( 202, 202, 255 ) )
		
		sbSizer9.Add( self.Tileset_SideBImagePanel, 0, 0, 0 )
		
		bSizer30 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer536 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bZoomInSideB = wx.BitmapButton( self.pnTilesetProperties, Tileset_ZoomInB, wx.Bitmap( u"artwork/ZoomIn.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bZoomInSideB.SetDefault() 
		self.bZoomInSideB.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bZoomInSideB.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		bSizer536.Add( self.bZoomInSideB, 0, 0, 0 )
		
		self.bZoomOutSideB = wx.BitmapButton( self.pnTilesetProperties, Tileset_ZoomOutB, wx.Bitmap( u"artwork/ZoomOut.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bZoomOutSideB.SetDefault() 
		bSizer536.Add( self.bZoomOutSideB, 0, wx.ALIGN_CENTRE, 0 )
		
		
		bSizer30.Add( bSizer536, 1, wx.EXPAND, 5 )
		
		bSizer532 = wx.BoxSizer( wx.VERTICAL )
		
		self.cpkSideBGridColor_Tileset = wx.ColourPickerCtrl( self.pnTilesetProperties, Tileset_SideBGridColor, wx.Colour( 255, 0, 0 ), wx.DefaultPosition, wx.Size( -1,-1 ), wx.CLRP_DEFAULT_STYLE )
		self.cpkSideBGridColor_Tileset.SetToolTip( u"Grid Color for Side B.  Click to change." )
		
		bSizer532.Add( self.cpkSideBGridColor_Tileset, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer30.Add( bSizer532, 1, 0, 5 )
		
		
		sbSizer9.Add( bSizer30, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 3 )
		
		
		szrImagePanels.Add( sbSizer9, 0, 0, 0 )
		
		
		bSizer533.Add( szrImagePanels, 1, wx.EXPAND, 5 )
		
		
		szrTilesets.Add( bSizer533, 1, wx.EXPAND, 5 )
		
		bSizer98 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ID_OK = wx.Button( self.pnTilesetProperties, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_OK.SetDefault() 
		self.ID_OK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_OK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.ID_OK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer98.Add( self.ID_OK, 0, wx.RIGHT, 2 )
		
		self.ID_CANCEL = wx.Button( self.pnTilesetProperties, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_CANCEL.SetDefault() 
		self.ID_CANCEL.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_CANCEL.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ID_CANCEL.SetBackgroundColour( wx.Colour( 128, 0, 64 ) )
		
		bSizer98.Add( self.ID_CANCEL, 0, wx.LEFT|wx.RIGHT, 2 )
		
		self.bHelpTileset = wx.Button( self.pnTilesetProperties, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bHelpTileset.SetDefault() 
		self.bHelpTileset.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bHelpTileset.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bHelpTileset.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer98.Add( self.bHelpTileset, 0, wx.LEFT, 2 )
		
		
		szrTilesets.Add( bSizer98, 0, wx.EXPAND|wx.TOP, 5 )
		
		
		self.pnTilesetProperties.SetSizer( szrTilesets )
		self.pnTilesetProperties.Layout()
		szrTilesets.Fit( self.pnTilesetProperties )
		self.nbTilesetEditor.AddPage( self.pnTilesetProperties, u"Tileset Properties", False )
		
		bSizer415.Add( self.nbTilesetEditor, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer415 )
		self.Layout()
		bSizer415.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.nbTilesetEditor.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnChangeNotebookPage )
		self.bAddImages.Bind( wx.EVT_BUTTON, self.AddImages )
		self.bRemoveImage.Bind( wx.EVT_BUTTON, self.RemoveImage )
		self.bClearImageSelection.Bind( wx.EVT_BUTTON, self.OnClearImageSelection )
		self.ImageListBox_Setup.Bind( wx.EVT_LISTBOX, self.OnImageListBox )
		self.bSetImageSideA.Bind( wx.EVT_BUTTON, self.SetImageSideA )
		self.bRemoveImageSideA.Bind( wx.EVT_BUTTON, self.RemoveImageSideA )
		self.bSetImageSideB.Bind( wx.EVT_BUTTON, self.SetImageSideB )
		self.bRemoveImageSideB.Bind( wx.EVT_BUTTON, self.RemoveImageSideB )
		self.bSwapImageSides.Bind( wx.EVT_BUTTON, self.SwapImageSides )
		self.bRefreshTilePanels.Bind( wx.EVT_BUTTON, self.RefreshImages )
		self.bAddCurrentToTileset.Bind( wx.EVT_BUTTON, self.AddCurrentTile )
		self.bUpdateTile.Bind( wx.EVT_BUTTON, self.OnUpdateTile )
		self.spXSize.Bind( wx.EVT_SPINCTRL, self.SetXSize )
		self.spXSize.Bind( wx.EVT_TEXT, self.SetXSize )
		self.spYSize.Bind( wx.EVT_SPINCTRL, self.SetYSize )
		self.spYSize.Bind( wx.EVT_TEXT, self.SetYSize )
		self.spTileCount.Bind( wx.EVT_SPINCTRL, self.SetTileQuantity )
		self.spTileCount.Bind( wx.EVT_TEXT, self.SetTileQuantity )
		self.TileNameA.Bind( wx.EVT_TEXT, self.SetTilenameA )
		self.TileNameA.Bind( wx.EVT_TEXT_ENTER, self.SetTilenameA )
		self.TileNameB.Bind( wx.EVT_TEXT, self.SetTilenameB )
		self.TileNameB.Bind( wx.EVT_TEXT_ENTER, self.SetTilenameB )
		self.bSetWallsSideA.Bind( wx.EVT_TOGGLEBUTTON, self.DrawImagePanels )
		self.bSetWallsSideB.Bind( wx.EVT_TOGGLEBUTTON, self.DrawImagePanels )
		self.bAddFilterTags.Bind( wx.EVT_BUTTON, self.AddFilterTags )
		self.Setup_SideAImagePanel.Bind( wx.EVT_LEFT_UP, self.OnPanelAClick )
		self.bZoomInSideA1.Bind( wx.EVT_BUTTON, self.ZoomInPanelSideA )
		self.bZoomOutSideA1.Bind( wx.EVT_BUTTON, self.ZoomOutPanelSideA )
		self.cpkSideAGridColor_Setup.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnChangeGridColorA_setup )
		self.Setup_SideBImagePanel.Bind( wx.EVT_LEFT_UP, self.OnPanelBClick )
		self.bZoomInSideB1.Bind( wx.EVT_BUTTON, self.ZoomInPanelSideB )
		self.bZoomOutSideB1.Bind( wx.EVT_BUTTON, self.ZoomOutPanelSideB )
		self.cpkSideBGridColor_Setup.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnChangeGridColorB_setup )
		self.lbSetup_TilesetBox.Bind( wx.EVT_LISTBOX, self.OnTilesetBox )
		self.bSetup_RemoveTile.Bind( wx.EVT_BUTTON, self.OnRemoveTile )
		self.ID_OK2.Bind( wx.EVT_BUTTON, self.OnOK )
		self.ID_CANCEL2.Bind( wx.EVT_BUTTON, self.OnCancel )
		self.bHelpTiles.Bind( wx.EVT_BUTTON, self.OnHelpSetup )
		self.bNewTileset.Bind( wx.EVT_BUTTON, self.OnNewTileset )
		self.bLoadTileset.Bind( wx.EVT_BUTTON, self.LoadTileset )
		self.bSaveTileset.Bind( wx.EVT_BUTTON, self.SaveTileset )
		self.txTilesetName.Bind( wx.EVT_TEXT, self.TilesetNameChanged )
		self.txTilesetID.Bind( wx.EVT_TEXT, self.TilesetIDChanged )
		self.lbTileset_TilesetBox.Bind( wx.EVT_LISTBOX, self.OnTilesetBox )
		self.Tileset_SideAImagePanel.Bind( wx.EVT_LEFT_UP, self.OnPanelAClick )
		self.bZoomInSideA.Bind( wx.EVT_BUTTON, self.ZoomInPanelSideA )
		self.bZoomOutSideA.Bind( wx.EVT_BUTTON, self.ZoomOutPanelSideA )
		self.cpkSideAGridColor_Tileset.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnChangeGridColorA_tileset )
		self.Tileset_SideBImagePanel.Bind( wx.EVT_LEFT_UP, self.OnPanelBClick )
		self.bZoomInSideB.Bind( wx.EVT_BUTTON, self.ZoomInPanelSideB )
		self.bZoomOutSideB.Bind( wx.EVT_BUTTON, self.ZoomOutPanelSideB )
		self.cpkSideBGridColor_Tileset.Bind( wx.EVT_COLOURPICKER_CHANGED, self.OnChangeGridColorB_tileset )
		self.ID_OK.Bind( wx.EVT_BUTTON, self.OnOK )
		self.ID_CANCEL.Bind( wx.EVT_BUTTON, self.OnCancel )
		self.bHelpTileset.Bind( wx.EVT_BUTTON, self.OnHelp )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnChangeNotebookPage( self, event ):
		event.Skip()
	
	def AddImages( self, event ):
		event.Skip()
	
	def RemoveImage( self, event ):
		event.Skip()
	
	def OnClearImageSelection( self, event ):
		event.Skip()
	
	def OnImageListBox( self, event ):
		event.Skip()
	
	def SetImageSideA( self, event ):
		event.Skip()
	
	def RemoveImageSideA( self, event ):
		event.Skip()
	
	def SetImageSideB( self, event ):
		event.Skip()
	
	def RemoveImageSideB( self, event ):
		event.Skip()
	
	def SwapImageSides( self, event ):
		event.Skip()
	
	def RefreshImages( self, event ):
		event.Skip()
	
	def AddCurrentTile( self, event ):
		event.Skip()
	
	def OnUpdateTile( self, event ):
		event.Skip()
	
	def SetXSize( self, event ):
		event.Skip()
	
	
	def SetYSize( self, event ):
		event.Skip()
	
	
	def SetTileQuantity( self, event ):
		event.Skip()
	
	
	def SetTilenameA( self, event ):
		event.Skip()
	
	
	def SetTilenameB( self, event ):
		event.Skip()
	
	
	def DrawImagePanels( self, event ):
		event.Skip()
	
	
	def AddFilterTags( self, event ):
		event.Skip()
	
	def OnPanelAClick( self, event ):
		event.Skip()
	
	def ZoomInPanelSideA( self, event ):
		event.Skip()
	
	def ZoomOutPanelSideA( self, event ):
		event.Skip()
	
	def OnChangeGridColorA_setup( self, event ):
		event.Skip()
	
	def OnPanelBClick( self, event ):
		event.Skip()
	
	def ZoomInPanelSideB( self, event ):
		event.Skip()
	
	def ZoomOutPanelSideB( self, event ):
		event.Skip()
	
	def OnChangeGridColorB_setup( self, event ):
		event.Skip()
	
	def OnTilesetBox( self, event ):
		event.Skip()
	
	def OnRemoveTile( self, event ):
		event.Skip()
	
	def OnOK( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		event.Skip()
	
	def OnHelpSetup( self, event ):
		event.Skip()
	
	def OnNewTileset( self, event ):
		event.Skip()
	
	def LoadTileset( self, event ):
		event.Skip()
	
	def SaveTileset( self, event ):
		event.Skip()
	
	def TilesetNameChanged( self, event ):
		event.Skip()
	
	def TilesetIDChanged( self, event ):
		event.Skip()
	
	
	
	
	
	def OnChangeGridColorA_tileset( self, event ):
		event.Skip()
	
	
	
	
	def OnChangeGridColorB_tileset( self, event ):
		event.Skip()
	
	
	
	def OnHelp( self, event ):
		event.Skip()
	

###########################################################################
## Class ReorderPagesBase
###########################################################################

class ReorderPagesBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Reorder Pages", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer526 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer528 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer531 = wx.BoxSizer( wx.VERTICAL )
		
		lbPageNamesChoices = []
		self.lbPageNames = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lbPageNamesChoices, wx.LB_NEEDED_SB )
		self.lbPageNames.SetMinSize( wx.Size( 250,300 ) )
		
		bSizer531.Add( self.lbPageNames, 0, wx.ALL, 5 )
		
		
		bSizer528.Add( bSizer531, 1, wx.EXPAND, 5 )
		
		bSizer530 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer529 = wx.BoxSizer( wx.VERTICAL )
		
		self.bMoveToTop = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/UpAll.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bMoveToTop.Enable( False )
		self.bMoveToTop.SetToolTip( u"Move selected page to first position" )
		
		bSizer529.Add( self.bMoveToTop, 0, wx.ALL, 5 )
		
		self.bMoveUp = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/Up.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bMoveUp.Enable( False )
		self.bMoveUp.SetToolTip( u"Move selected page up one position" )
		
		bSizer529.Add( self.bMoveUp, 0, wx.ALL, 5 )
		
		self.bMoveDown = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/Down.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bMoveDown.Enable( False )
		self.bMoveDown.SetToolTip( u"Move selected page down one position" )
		
		bSizer529.Add( self.bMoveDown, 0, wx.ALL, 5 )
		
		self.bMoveToBottom = wx.BitmapButton( self, wx.ID_ANY, wx.Bitmap( u"artwork/DownAll.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
		self.bMoveToBottom.Enable( False )
		self.bMoveToBottom.SetToolTip( u"Move selected page to bottom position" )
		
		bSizer529.Add( self.bMoveToBottom, 0, wx.ALL, 5 )
		
		
		bSizer530.Add( bSizer529, 1, 0, 5 )
		
		
		bSizer528.Add( bSizer530, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer526.Add( bSizer528, 1, wx.EXPAND, 5 )
		
		bSizer98 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ID_OK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_OK.SetDefault() 
		self.ID_OK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_OK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.ID_OK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer98.Add( self.ID_OK, 0, wx.RIGHT, 2 )
		
		self.ID_CANCEL = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_CANCEL.SetDefault() 
		self.ID_CANCEL.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_CANCEL.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ID_CANCEL.SetBackgroundColour( wx.Colour( 128, 0, 64 ) )
		
		bSizer98.Add( self.ID_CANCEL, 0, wx.LEFT|wx.RIGHT, 2 )
		
		self.bHelp = wx.Button( self, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bHelp.SetDefault() 
		self.bHelp.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bHelp.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bHelp.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer98.Add( self.bHelp, 0, wx.LEFT, 2 )
		
		
		bSizer526.Add( bSizer98, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer526 )
		self.Layout()
		bSizer526.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.lbPageNames.Bind( wx.EVT_LISTBOX, self.SelectPage )
		self.bMoveToTop.Bind( wx.EVT_BUTTON, self.OnMoveToTop )
		self.bMoveUp.Bind( wx.EVT_BUTTON, self.OnMoveUp )
		self.bMoveDown.Bind( wx.EVT_BUTTON, self.OnMoveDown )
		self.bMoveToBottom.Bind( wx.EVT_BUTTON, self.OnMoveToBottom )
		self.ID_OK.Bind( wx.EVT_BUTTON, self.OnOK )
		self.ID_CANCEL.Bind( wx.EVT_BUTTON, self.OnCancel )
		self.bHelp.Bind( wx.EVT_BUTTON, self.OnHelp )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def SelectPage( self, event ):
		event.Skip()
	
	def OnMoveToTop( self, event ):
		event.Skip()
	
	def OnMoveUp( self, event ):
		event.Skip()
	
	def OnMoveDown( self, event ):
		event.Skip()
	
	def OnMoveToBottom( self, event ):
		event.Skip()
	
	def OnOK( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		event.Skip()
	
	def OnHelp( self, event ):
		event.Skip()
	

###########################################################################
## Class UserDetailsDialogBase
###########################################################################

class UserDetailsDialogBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Register Program", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer526 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer528 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer529 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText280 = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText280.Wrap( -1 )
		bSizer529.Add( self.m_staticText280, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txUserName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer529.Add( self.txUserName, 1, wx.ALL, 5 )
		
		
		bSizer528.Add( bSizer529, 0, wx.EXPAND, 5 )
		
		bSizer5291 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2801 = wx.StaticText( self, wx.ID_ANY, u"Email:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2801.Wrap( -1 )
		bSizer5291.Add( self.m_staticText2801, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txUserEmail = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5291.Add( self.txUserEmail, 1, wx.ALL, 5 )
		
		
		bSizer528.Add( bSizer5291, 0, wx.EXPAND, 5 )
		
		bSizer5292 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2802 = wx.StaticText( self, wx.ID_ANY, u"Comments:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2802.Wrap( -1 )
		bSizer5292.Add( self.m_staticText2802, 0, wx.ALL, 5 )
		
		self.txUserComments = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,55 ), wx.TE_MULTILINE )
		bSizer5292.Add( self.txUserComments, 1, wx.ALL, 5 )
		
		
		bSizer528.Add( bSizer5292, 0, wx.EXPAND, 5 )
		
		bSizer535 = wx.BoxSizer( wx.VERTICAL )
		
		self.cbReceiveUpdates = wx.CheckBox( self, wx.ID_ANY, u"Receive updates about pymapper via email?", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer535.Add( self.cbReceiveUpdates, 0, wx.ALL, 5 )
		
		self.cbSendCrashReports = wx.CheckBox( self, wx.ID_ANY, u"Allow pymapper to send crash reports back to developer?", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer535.Add( self.cbSendCrashReports, 0, wx.ALL, 5 )
		
		
		bSizer528.Add( bSizer535, 0, wx.EXPAND, 5 )
		
		
		bSizer526.Add( bSizer528, 1, wx.EXPAND, 5 )
		
		bSizer527 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bRegister = wx.Button( self, ID_OK, u"Register", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bRegister.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.bRegister.SetForegroundColour( wx.Colour( 232, 232, 0 ) )
		self.bRegister.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer527.Add( self.bRegister, 0, wx.TOP, 5 )
		
		self.bCancel = wx.Button( self, ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bCancel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.bCancel.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bCancel.SetBackgroundColour( wx.Colour( 128, 0, 0 ) )
		
		bSizer527.Add( self.bCancel, 0, wx.TOP, 5 )
		
		self.bPrivacyInfo = wx.Button( self, wx.ID_ANY, u"Privacy Information", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bPrivacyInfo.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.bPrivacyInfo.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bPrivacyInfo.SetBackgroundColour( wx.Colour( 0, 94, 187 ) )
		
		bSizer527.Add( self.bPrivacyInfo, 0, wx.TOP, 5 )
		
		
		bSizer526.Add( bSizer527, 0, wx.EXPAND, 0 )
		
		
		self.SetSizer( bSizer526 )
		self.Layout()
		bSizer526.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.bRegister.Bind( wx.EVT_BUTTON, self.OnRegisterProgram )
		self.bCancel.Bind( wx.EVT_BUTTON, self.OnCancel )
		self.bPrivacyInfo.Bind( wx.EVT_BUTTON, self.OnPrivacyInformation )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnRegisterProgram( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		event.Skip()
	
	def OnPrivacyInformation( self, event ):
		event.Skip()
	

###########################################################################
## Class Spellbook5EBase
###########################################################################

class Spellbook5EBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Fifth Edition Spellbook", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer561 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer562 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer564 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText297 = wx.StaticText( self, wx.ID_ANY, u"Spell Name :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText297.Wrap( -1 )
		bSizer564.Add( self.m_staticText297, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txSpellName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer564.Add( self.txSpellName, 1, wx.ALL, 5 )
		
		
		bSizer562.Add( bSizer564, 0, wx.EXPAND, 5 )
		
		bSizer565 = wx.BoxSizer( wx.VERTICAL )
		
		self.stSpellDescriptor = wx.StaticText( self, wx.ID_ANY, u"Spell/Cantrip Level and School", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stSpellDescriptor.Wrap( -1 )
		self.stSpellDescriptor.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 93, 90, False, wx.EmptyString ) )
		
		bSizer565.Add( self.stSpellDescriptor, 0, wx.ALL, 3 )
		
		bSizer583 = wx.BoxSizer( wx.HORIZONTAL )
		
		cxSpellLevelChoices = [ u"Cantrip", u"1st Level", u"2nd Level", u"3rd Level", u"4th Level", u"5th Level", u"6th Level", u"7th Level", u"8th Level", u"9th Level" ]
		self.cxSpellLevel = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cxSpellLevelChoices, 0 )
		self.cxSpellLevel.SetSelection( 0 )
		bSizer583.Add( self.cxSpellLevel, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		lbClassType1Choices = [ u"Bard", u"Cleric", u"Druid", u"Paladin" ]
		self.lbClassType1 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lbClassType1Choices, wx.LB_MULTIPLE )
		bSizer583.Add( self.lbClassType1, 0, 0, 5 )
		
		lbClassType2Choices = [ u"Ranger", u"Sorcerer", u"Warlock", u"Wizard" ]
		self.lbClassType2 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lbClassType2Choices, wx.LB_MULTIPLE )
		bSizer583.Add( self.lbClassType2, 0, 0, 5 )
		
		cxMagicSchoolChoices = [ u"Abjuration", u"Conjuration", u"Divination", u"Enchantment", u"Evocation", u"Illusion", u"Necromancy", u"Transmutation" ]
		self.cxMagicSchool = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cxMagicSchoolChoices, 0 )
		self.cxMagicSchool.SetSelection( 0 )
		bSizer583.Add( self.cxMagicSchool, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer565.Add( bSizer583, 0, wx.EXPAND, 5 )
		
		self.cbBasicSpell = wx.CheckBox( self, wx.ID_ANY, u"Basic Rules Spell?", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer565.Add( self.cbBasicSpell, 0, wx.ALL, 3 )
		
		self.cbRitualSpell = wx.CheckBox( self, wx.ID_ANY, u"Ritual Spell?", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer565.Add( self.cbRitualSpell, 0, wx.ALL, 3 )
		
		self.cbConcentrationSpell = wx.CheckBox( self, wx.ID_ANY, u"Concentration spell?", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer565.Add( self.cbConcentrationSpell, 0, wx.ALL, 3 )
		
		
		bSizer562.Add( bSizer565, 0, wx.EXPAND, 5 )
		
		bSizer566 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText300 = wx.StaticText( self, wx.ID_ANY, u"Casting Time :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText300.Wrap( -1 )
		bSizer566.Add( self.m_staticText300, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 3 )
		
		self.txCastingTime = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer566.Add( self.txCastingTime, 1, wx.ALL|wx.EXPAND, 3 )
		
		
		bSizer562.Add( bSizer566, 0, wx.EXPAND, 5 )
		
		bSizer5661 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3001 = wx.StaticText( self, wx.ID_ANY, u"Range :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3001.Wrap( -1 )
		bSizer5661.Add( self.m_staticText3001, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 3 )
		
		self.txSpellRange = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5661.Add( self.txSpellRange, 1, wx.ALL|wx.EXPAND, 3 )
		
		
		bSizer562.Add( bSizer5661, 0, wx.EXPAND, 5 )
		
		bSizer5662 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3002 = wx.StaticText( self, wx.ID_ANY, u"Components :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3002.Wrap( -1 )
		bSizer5662.Add( self.m_staticText3002, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3 )
		
		bSizer585 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.cbVerbal = wx.CheckBox( self, wx.ID_ANY, u"V", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbVerbal.SetToolTip( u"Verbal Component?" )
		
		bSizer585.Add( self.cbVerbal, 0, wx.ALL, 5 )
		
		self.cbSomatic = wx.CheckBox( self, wx.ID_ANY, u"S", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbSomatic.SetToolTip( u"Somatic Component?" )
		
		bSizer585.Add( self.cbSomatic, 0, wx.ALL, 5 )
		
		self.cbMaterial = wx.CheckBox( self, wx.ID_ANY, u"M", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbMaterial.SetToolTip( u"Material Component?" )
		
		bSizer585.Add( self.cbMaterial, 0, wx.ALL, 5 )
		
		self.cbFocus = wx.CheckBox( self, wx.ID_ANY, u"F", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cbFocus.SetToolTip( u"Focus Component?" )
		
		bSizer585.Add( self.cbFocus, 0, wx.ALL, 5 )
		
		
		bSizer5662.Add( bSizer585, 1, wx.EXPAND, 5 )
		
		
		bSizer562.Add( bSizer5662, 0, wx.EXPAND, 5 )
		
		bSizer5663 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3003 = wx.StaticText( self, wx.ID_ANY, u"Duration :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3003.Wrap( -1 )
		bSizer5663.Add( self.m_staticText3003, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 3 )
		
		self.txSpellDuration = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5663.Add( self.txSpellDuration, 1, wx.ALL|wx.EXPAND, 3 )
		
		
		bSizer562.Add( bSizer5663, 0, wx.EXPAND, 2 )
		
		bSizer5665 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer578 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3005 = wx.StaticText( self, wx.ID_ANY, u"Base Damage :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3005.Wrap( -1 )
		bSizer578.Add( self.m_staticText3005, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2 )
		
		self.txDamage = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer578.Add( self.txDamage, 0, wx.ALL, 3 )
		
		cxDamageTypeChoices = [ u"Acid", u"Bludgeoning", u"Cold", u"Fire", u"Force", u"Lightning", u"Necrotic", u"Piercing", u"Poison", u"Psychic", u"Radiant", u"Slashing", u"Thunder" ]
		self.cxDamageType = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, cxDamageTypeChoices, 0 )
		self.cxDamageType.SetSelection( 0 )
		bSizer578.Add( self.cxDamageType, 0, wx.ALL, 3 )
		
		
		bSizer5665.Add( bSizer578, 0, wx.EXPAND, 5 )
		
		bSizer579 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bRollDamage = wx.Button( self, wx.ID_ANY, u"Roll Damage", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer579.Add( self.bRollDamage, 0, wx.ALL, 5 )
		
		self.stDamage = wx.StaticText( self, wx.ID_ANY, u"0 HP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stDamage.Wrap( -1 )
		bSizer579.Add( self.stDamage, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer5665.Add( bSizer579, 0, wx.EXPAND, 5 )
		
		
		bSizer562.Add( bSizer5665, 0, wx.EXPAND, 2 )
		
		bSizer5664 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3004 = wx.StaticText( self, wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3004.Wrap( -1 )
		bSizer5664.Add( self.m_staticText3004, 0, wx.ALL, 3 )
		
		self.txDescription = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,150 ), wx.TE_MULTILINE )
		bSizer5664.Add( self.txDescription, 1, wx.ALL|wx.EXPAND, 3 )
		
		bSizer581 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.stSource = wx.StaticText( self, wx.ID_ANY, u"Source : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stSource.Wrap( -1 )
		bSizer581.Add( self.stSource, 0, wx.ALL, 5 )
		
		self.stSourceText = wx.StaticText( self, wx.ID_ANY, u"None", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.stSourceText.Wrap( -1 )
		bSizer581.Add( self.stSourceText, 0, wx.ALL, 5 )
		
		
		bSizer5664.Add( bSizer581, 0, wx.EXPAND, 5 )
		
		
		bSizer562.Add( bSizer5664, 0, wx.EXPAND, 5 )
		
		sbSizer88 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Filters" ), wx.HORIZONTAL )
		
		bSizer580 = wx.BoxSizer( wx.VERTICAL )
		
		self.cbLevelFilter = wx.CheckBox( self, wx.ID_ANY, u"Spell Level", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer580.Add( self.cbLevelFilter, 0, wx.ALL, 5 )
		
		lbLevelFilterChoices = [ u"Cantrip", u"1st Level", u"2nd Level", u"3rd Level", u"4th Level", u"5th Level", u"6th Level", u"7th Level", u"8th Level", u"9th Level" ]
		self.lbLevelFilter = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lbLevelFilterChoices, wx.LB_MULTIPLE )
		self.lbLevelFilter.Enable( False )
		
		bSizer580.Add( self.lbLevelFilter, 0, wx.ALL, 5 )
		
		
		sbSizer88.Add( bSizer580, 1, wx.EXPAND, 5 )
		
		bSizer5801 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer582 = wx.BoxSizer( wx.VERTICAL )
		
		self.cbClassFilter = wx.CheckBox( self, wx.ID_ANY, u"Class Availability", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer582.Add( self.cbClassFilter, 0, wx.ALL, 5 )
		
		lbClassFilterChoices = [ u"Bard", u"Cleric", u"Druid", u"Paladin", u"Ranger", u"Sorcerer", u"Warlock", u"Wizard" ]
		self.lbClassFilter = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lbClassFilterChoices, wx.LB_MULTIPLE )
		self.lbClassFilter.Enable( False )
		
		bSizer582.Add( self.lbClassFilter, 0, wx.ALL, 5 )
		
		
		bSizer5801.Add( bSizer582, 1, wx.EXPAND, 5 )
		
		bSizer5831 = wx.BoxSizer( wx.VERTICAL )
		
		self.cbBasicRules = wx.CheckBox( self, wx.ID_ANY, u"Basic Spells only?", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5831.Add( self.cbBasicRules, 0, wx.ALL, 5 )
		
		
		bSizer5801.Add( bSizer5831, 0, wx.EXPAND, 5 )
		
		
		sbSizer88.Add( bSizer5801, 1, wx.EXPAND, 5 )
		
		bSizer5802 = wx.BoxSizer( wx.VERTICAL )
		
		self.cbSchoolFilter = wx.CheckBox( self, wx.ID_ANY, u"Magic School", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5802.Add( self.cbSchoolFilter, 0, wx.ALL, 5 )
		
		lbSchoolFilterChoices = [ u"Abjuration", u"Conjuration", u"Divination", u"Enchantment", u"Evocation", u"Illusion", u"Necromancy", u"Transmutation" ]
		self.lbSchoolFilter = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lbSchoolFilterChoices, wx.LB_MULTIPLE )
		self.lbSchoolFilter.Enable( False )
		
		bSizer5802.Add( self.lbSchoolFilter, 0, wx.ALL, 5 )
		
		
		sbSizer88.Add( bSizer5802, 1, wx.EXPAND, 5 )
		
		
		bSizer562.Add( sbSizer88, 0, wx.EXPAND, 5 )
		
		bSizer98 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ID_OK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_OK.SetDefault() 
		self.ID_OK.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_OK.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.ID_OK.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer98.Add( self.ID_OK, 0, wx.RIGHT, 2 )
		
		self.ID_CANCEL = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ID_CANCEL.SetDefault() 
		self.ID_CANCEL.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.ID_CANCEL.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.ID_CANCEL.SetBackgroundColour( wx.Colour( 128, 0, 64 ) )
		
		bSizer98.Add( self.ID_CANCEL, 0, wx.LEFT|wx.RIGHT, 2 )
		
		self.bHelp = wx.Button( self, wx.ID_ANY, u"Help", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bHelp.SetDefault() 
		self.bHelp.SetFont( wx.Font( 8, 74, 90, 92, False, "Tahoma" ) )
		self.bHelp.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bHelp.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer98.Add( self.bHelp, 0, wx.LEFT, 2 )
		
		
		bSizer562.Add( bSizer98, 1, wx.EXPAND, 5 )
		
		
		bSizer561.Add( bSizer562, 1, wx.EXPAND, 5 )
		
		bSizer563 = wx.BoxSizer( wx.VERTICAL )
		
		lbSpellListChoices = []
		self.lbSpellList = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lbSpellListChoices, wx.LB_SORT )
		bSizer563.Add( self.lbSpellList, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer578 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.bAddSpell = wx.Button( self, wx.ID_ANY, u"Add New Spell", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer578.Add( self.bAddSpell, 0, wx.ALL, 2 )
		
		self.bUpdateSpell = wx.Button( self, wx.ID_ANY, u"Update Spell Info", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer578.Add( self.bUpdateSpell, 0, wx.ALL, 2 )
		
		self.bDeleteSpell = wx.Button( self, wx.ID_ANY, u"Delete Spell", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bDeleteSpell.Enable( False )
		self.bDeleteSpell.SetToolTip( u"Deletes a user-defined spell" )
		
		bSizer578.Add( self.bDeleteSpell, 0, wx.ALL, 2 )
		
		
		bSizer563.Add( bSizer578, 0, wx.EXPAND|wx.LEFT, 5 )
		
		
		bSizer561.Add( bSizer563, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer561 )
		self.Layout()
		bSizer561.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.cbLevelFilter.Bind( wx.EVT_CHECKBOX, self.FilterByLevel )
		self.lbLevelFilter.Bind( wx.EVT_LISTBOX, self.RefreshSpellList )
		self.cbClassFilter.Bind( wx.EVT_CHECKBOX, self.FilterByClass )
		self.lbClassFilter.Bind( wx.EVT_LISTBOX, self.RefreshSpellList )
		self.cbBasicRules.Bind( wx.EVT_CHECKBOX, self.FilterBasicSpells )
		self.cbSchoolFilter.Bind( wx.EVT_CHECKBOX, self.FilterBySchool )
		self.lbSchoolFilter.Bind( wx.EVT_LISTBOX, self.RefreshSpellList )
		self.ID_OK.Bind( wx.EVT_BUTTON, self.OnOK )
		self.ID_CANCEL.Bind( wx.EVT_BUTTON, self.OnCancel )
		self.bHelp.Bind( wx.EVT_BUTTON, self.OnHelp )
		self.lbSpellList.Bind( wx.EVT_LISTBOX, self.OnListBoxSelect )
		self.bAddSpell.Bind( wx.EVT_BUTTON, self.AddNewSpell )
		self.bUpdateSpell.Bind( wx.EVT_BUTTON, self.UpdateCurrentSpell )
		self.bDeleteSpell.Bind( wx.EVT_BUTTON, self.DeleteUserSpell )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def FilterByLevel( self, event ):
		event.Skip()
	
	def RefreshSpellList( self, event ):
		event.Skip()
	
	def FilterByClass( self, event ):
		event.Skip()
	
	
	def FilterBasicSpells( self, event ):
		event.Skip()
	
	def FilterBySchool( self, event ):
		event.Skip()
	
	
	def OnOK( self, event ):
		event.Skip()
	
	def OnCancel( self, event ):
		event.Skip()
	
	def OnHelp( self, event ):
		event.Skip()
	
	def OnListBoxSelect( self, event ):
		event.Skip()
	
	def AddNewSpell( self, event ):
		event.Skip()
	
	def UpdateCurrentSpell( self, event ):
		event.Skip()
	
	def DeleteUserSpell( self, event ):
		event.Skip()
	

###########################################################################
## Class ConditionsLegendBase
###########################################################################

class ConditionsLegendBase ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Conditions", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer606 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer607 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText309 = wx.StaticText( self, wx.ID_ANY, u"Blinded", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText309.Wrap( -1 )
		bSizer607.Add( self.m_staticText309, 1, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.cpkBlinded = wx.ColourPickerCtrl( self, idxBlinded, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		bSizer607.Add( self.cpkBlinded, 0, 0, 5 )
		
		
		bSizer606.Add( bSizer607, 1, wx.EXPAND, 5 )
		
		bSizer6071 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3091 = wx.StaticText( self, wx.ID_ANY, u"Charmed", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3091.Wrap( -1 )
		bSizer6071.Add( self.m_staticText3091, 1, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.cpkCharmed = wx.ColourPickerCtrl( self, idxCharmed, wx.Colour( 255, 0, 128 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		bSizer6071.Add( self.cpkCharmed, 0, 0, 5 )
		
		
		bSizer606.Add( bSizer6071, 1, wx.EXPAND, 5 )
		
		bSizer6072 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3092 = wx.StaticText( self, wx.ID_ANY, u"Concentrating", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3092.Wrap( -1 )
		bSizer6072.Add( self.m_staticText3092, 1, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.cpkConcentrating = wx.ColourPickerCtrl( self, idxConcentrating, wx.Colour( 0, 0, 255 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		bSizer6072.Add( self.cpkConcentrating, 0, 0, 5 )
		
		
		bSizer606.Add( bSizer6072, 1, wx.EXPAND, 5 )
		
		bSizer6074 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3094 = wx.StaticText( self, wx.ID_ANY, u"Deafened", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3094.Wrap( -1 )
		bSizer6074.Add( self.m_staticText3094, 1, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.cpkDeafened = wx.ColourPickerCtrl( self, idxDeafened, wx.Colour( 128, 0, 255 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		bSizer6074.Add( self.cpkDeafened, 0, 0, 5 )
		
		
		bSizer606.Add( bSizer6074, 1, wx.EXPAND, 5 )
		
		bSizer6075 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3095 = wx.StaticText( self, wx.ID_ANY, u"Frightened", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3095.Wrap( -1 )
		bSizer6075.Add( self.m_staticText3095, 1, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.cpkFrightened = wx.ColourPickerCtrl( self, idxFrightened, wx.Colour( 255, 0, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		bSizer6075.Add( self.cpkFrightened, 0, 0, 5 )
		
		
		bSizer606.Add( bSizer6075, 1, wx.EXPAND, 5 )
		
		bSizer6076 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3096 = wx.StaticText( self, wx.ID_ANY, u"Grappled", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3096.Wrap( -1 )
		bSizer6076.Add( self.m_staticText3096, 1, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.cpkGrappled = wx.ColourPickerCtrl( self, idxGrappled, wx.Colour( 128, 128, 128 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		bSizer6076.Add( self.cpkGrappled, 0, 0, 5 )
		
		
		bSizer606.Add( bSizer6076, 1, wx.EXPAND, 5 )
		
		bSizer6073 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3093 = wx.StaticText( self, wx.ID_ANY, u"Incapacitated", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3093.Wrap( -1 )
		bSizer6073.Add( self.m_staticText3093, 1, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.cpkIncapacitated = wx.ColourPickerCtrl( self, idxIncapacitated, wx.Colour( 255, 128, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		bSizer6073.Add( self.cpkIncapacitated, 0, 0, 5 )
		
		
		bSizer606.Add( bSizer6073, 1, wx.EXPAND, 5 )
		
		bSizer6077 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3097 = wx.StaticText( self, wx.ID_ANY, u"Invisible", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3097.Wrap( -1 )
		bSizer6077.Add( self.m_staticText3097, 1, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.cpkInvisible = wx.ColourPickerCtrl( self, idxInvisible, wx.Colour( 225, 175, 119 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		bSizer6077.Add( self.cpkInvisible, 0, 0, 5 )
		
		
		bSizer606.Add( bSizer6077, 1, wx.EXPAND, 5 )
		
		bSizer6078 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3098 = wx.StaticText( self, wx.ID_ANY, u"Paralyzed", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3098.Wrap( -1 )
		bSizer6078.Add( self.m_staticText3098, 1, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.cpkParalyzed = wx.ColourPickerCtrl( self, idxParalyzed, wx.Colour( 120, 237, 182 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		bSizer6078.Add( self.cpkParalyzed, 0, 0, 5 )
		
		
		bSizer606.Add( bSizer6078, 1, wx.EXPAND, 5 )
		
		bSizer6079 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3099 = wx.StaticText( self, wx.ID_ANY, u"Petrified", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3099.Wrap( -1 )
		bSizer6079.Add( self.m_staticText3099, 1, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.cpkPetrified = wx.ColourPickerCtrl( self, idxPetrified, wx.Colour( 64, 128, 128 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		bSizer6079.Add( self.cpkPetrified, 0, 0, 5 )
		
		
		bSizer606.Add( bSizer6079, 1, wx.EXPAND, 5 )
		
		bSizer60710 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText30910 = wx.StaticText( self, wx.ID_ANY, u"Poisoned", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30910.Wrap( -1 )
		bSizer60710.Add( self.m_staticText30910, 1, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.cpkPoisoned = wx.ColourPickerCtrl( self, idxPoisoned, wx.Colour( 0, 255, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		bSizer60710.Add( self.cpkPoisoned, 0, 0, 5 )
		
		
		bSizer606.Add( bSizer60710, 1, wx.EXPAND, 5 )
		
		bSizer60711 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText30911 = wx.StaticText( self, wx.ID_ANY, u"Prone", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30911.Wrap( -1 )
		bSizer60711.Add( self.m_staticText30911, 1, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.cpkProne = wx.ColourPickerCtrl( self, idxProne, wx.Colour( 128, 128, 255 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		bSizer60711.Add( self.cpkProne, 0, 0, 5 )
		
		
		bSizer606.Add( bSizer60711, 1, wx.EXPAND, 5 )
		
		bSizer60712 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText30912 = wx.StaticText( self, wx.ID_ANY, u"Restrained", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30912.Wrap( -1 )
		bSizer60712.Add( self.m_staticText30912, 1, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.cpkRestrained = wx.ColourPickerCtrl( self, idxRestrained, wx.Colour( 255, 255, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		bSizer60712.Add( self.cpkRestrained, 0, 0, 5 )
		
		
		bSizer606.Add( bSizer60712, 1, wx.EXPAND, 5 )
		
		bSizer60713 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText30913 = wx.StaticText( self, wx.ID_ANY, u"Stunned", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30913.Wrap( -1 )
		bSizer60713.Add( self.m_staticText30913, 1, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.cpkStunned = wx.ColourPickerCtrl( self, idxStunned, wx.Colour( 128, 64, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		bSizer60713.Add( self.cpkStunned, 0, 0, 5 )
		
		
		bSizer606.Add( bSizer60713, 1, wx.EXPAND, 5 )
		
		bSizer60714 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText30914 = wx.StaticText( self, wx.ID_ANY, u"Turned", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30914.Wrap( -1 )
		bSizer60714.Add( self.m_staticText30914, 1, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.cpkTurned = wx.ColourPickerCtrl( self, idxTurned, wx.Colour( 128, 128, 64 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		bSizer60714.Add( self.cpkTurned, 0, 0, 5 )
		
		
		bSizer606.Add( bSizer60714, 1, wx.EXPAND, 5 )
		
		bSizer60715 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText30915 = wx.StaticText( self, wx.ID_ANY, u"Unconscious", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30915.Wrap( -1 )
		bSizer60715.Add( self.m_staticText30915, 1, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.cpkUnconscious = wx.ColourPickerCtrl( self, idxUnconscious, wx.Colour( 128, 255, 255 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		bSizer60715.Add( self.cpkUnconscious, 0, 0, 5 )
		
		
		bSizer606.Add( bSizer60715, 1, wx.EXPAND, 5 )
		
		self.bCloseDialog = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.bCloseDialog.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.bCloseDialog.SetForegroundColour( wx.Colour( 255, 255, 255 ) )
		self.bCloseDialog.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
		
		bSizer606.Add( self.bCloseDialog, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer606 )
		self.Layout()
		bSizer606.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.cpkBlinded.Bind( wx.EVT_COLOURPICKER_CHANGED, self.ChangeConditionColor )
		self.cpkCharmed.Bind( wx.EVT_COLOURPICKER_CHANGED, self.ChangeConditionColor )
		self.cpkConcentrating.Bind( wx.EVT_COLOURPICKER_CHANGED, self.ChangeConditionColor )
		self.cpkDeafened.Bind( wx.EVT_COLOURPICKER_CHANGED, self.ChangeConditionColor )
		self.cpkFrightened.Bind( wx.EVT_COLOURPICKER_CHANGED, self.ChangeConditionColor )
		self.cpkGrappled.Bind( wx.EVT_COLOURPICKER_CHANGED, self.ChangeConditionColor )
		self.cpkIncapacitated.Bind( wx.EVT_COLOURPICKER_CHANGED, self.ChangeConditionColor )
		self.cpkInvisible.Bind( wx.EVT_COLOURPICKER_CHANGED, self.ChangeConditionColor )
		self.cpkParalyzed.Bind( wx.EVT_COLOURPICKER_CHANGED, self.ChangeConditionColor )
		self.cpkPetrified.Bind( wx.EVT_COLOURPICKER_CHANGED, self.ChangeConditionColor )
		self.cpkPoisoned.Bind( wx.EVT_COLOURPICKER_CHANGED, self.ChangeConditionColor )
		self.cpkProne.Bind( wx.EVT_COLOURPICKER_CHANGED, self.ChangeConditionColor )
		self.cpkRestrained.Bind( wx.EVT_COLOURPICKER_CHANGED, self.ChangeConditionColor )
		self.cpkStunned.Bind( wx.EVT_COLOURPICKER_CHANGED, self.ChangeConditionColor )
		self.cpkTurned.Bind( wx.EVT_COLOURPICKER_CHANGED, self.ChangeConditionColor )
		self.cpkUnconscious.Bind( wx.EVT_COLOURPICKER_CHANGED, self.ChangeConditionColor )
		self.bCloseDialog.Bind( wx.EVT_BUTTON, self.OnCloseDialog )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def ChangeConditionColor( self, event ):
		event.Skip()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	def OnCloseDialog( self, event ):
		event.Skip()
	

