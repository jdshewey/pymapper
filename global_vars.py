#-----------------------------------------------------------------------------
# Name:        global_vars.py
# Purpose:     Global variables for use in PyMapper
#
# Author:      Michael Seely, P.E.
#
# Created:     2009/06/13
# RCS-ID:      $Id: global_vars.py $
# Copyright:   (c) 2009 Michael Seely, P.E.
# Licence:     GNU Public License
#-----------------------------------------------------------------------------
import wx

#----------------------------------------

init = False #flag for final initialization

RoomList = []  #list of RoomInfo with descriptions, etc.

TrapList = []  #list of available traps
NPC_List = []   #list of the compiled (calculated) NPC's
MonsterList = [] #list of monsters
Spells5E = []    #list of Spells loaded from the 5E SRD data
Monsters5E = []  #list of monsters loaded from the 5E SRD data
NPC_5E = []      #list of NPC's generated for 5E

ClassData_5E = []  #5E class information

MapColumns = 0
PyMapperApp = None

PrintResolution = 50 #resolution for the printer bitmap
SavePrintResolution = False #should this value be saved to the .ini file?

RefreshTilePanel = False #allow redraw of the TilePanel
RefreshMapPanel = False  #allow redraw of the MapPanel
TileZoomFactor = 20  #This is the number of pixels per tile square
MapZoomFactor = 35 #This is the number of pixels per map square
MapZoomIncrement = 5 # This is the amount to zoom in per right click
TileZoomIncrement = 10 # This is the amount to zoom in per right click

tileborderwidth = 4 #The width of the selection border in the tile window

TilePanelVOffset = 0 #controls the vertical scrolling on the Tile Panel
TilePanelHOffset = 0 #controls the vertical scrolling on the Tile Panel

root_directory = None #place where the PyMapper was installed.  Tiles are a subfolder of this.
tiles_directory = None #location of the \tiles\ folder, ie, c:\pymapper\tiles\
backup_directory = None #location of the backup files, default to \backup\
maps_directory = None #location of the default maps folder
image_directory = None #location where the last image was exported to
srd_directory = None  #location of the d20 SRD information
artwork_directory = None #location of button images and resources
encounters_directory = None #location for xml files for traps, npc, etc.
geomorphs_directory = None #location for geomorph files, descriptions, preview bitmaps, etc.
tokens_directory = None    #location for custom images for npc/monsters
program_initialized = False

ScrollRate = 20 #map panel scrolling rate

TilePanelBackgroundColor = wx.Colour(64,128,128,255) #teal color
MapPanelBackgroundColor = wx.Colour(255,255,255,255) #white
SecondaryPanelBackgroundColor = wx.Colour(0,0,0,255) #black

AddTile = False #Are we adding a tile to the maplist from the TilePanel?
SelectedFromTilePanel = False

MapExtents = wx.Rect(0,0,0,0) #size of the overall map
WindowExtents = wx.Rect(0,0,800,600)

DisplayGrid = True
GridColor = wx.Colour(192,192,192,255)
GridPenWidth = 1
GridPenStyle = wx.SOLID
GridPen = None
ShowGridCoordinates = False
SnapToGrid = True

hovertime = 0            # used to determine if hovering over a tile
hovering = False         # are we sitting still over a tile?
StartPoint = None        # point to 
LastPoint = None         # where was the last point of the mouse, used for finding tiles
HoverPoint = None        # where will we place the hovering dialog?
hover_interval = 500     # how long to wait before hovering is confirmed?
hoverDlg = None          # this is the hovering window
hoverMonsterInfo = None  # if we hovered over a monster icon, this is the room.monster info
DisplayOnHover = False # are we using the hover option?  Default is the dual display.

rotation_increment = 90 #ie, 90 degrees.

TileDimFactor = 0.5 #how much to dim a tile when no more copies are left.
TileOpacity = 1.0

SelectionColor = wx.Colour(0, 0, 255, 255)
SelectionPenWidth = 2
SelectionPenStyle = wx.SOLID
SelectionPen = None #wx.Pen(SelectionColor, SelectionPenWidth, SelectionPenStyle)

ScrollIncrement = 1 #amount to change scrolling sensitivity
MapOffset = wx.Point(0,0) #this is the virtual origin.  It is changed as we pan around the screen
StartPan = wx.Point(0,0)
EndPan = wx.Point(0,0) #this is where we stopped panning the map

DisplayBackground = False
BackgroundOpacity = 1.0
ReadSRDFileData = False
Read5EditionFileData = False

AutoSave = False              #flag if backup copies should be made
AutoSaveInterval = 300.0      #default time for backup in seconds
SaveIniFile = True            #should we save the .ini file on close?
LimitTiles = True             #do we limit the number of tiles used to the number owned?
DualDisplayTileWindow = True  #Show both sides of the tile in the tile panel?
ShowTutorial = True           #flag used to read in the tutorial.map file during OnInit()
DrawGridOnTop = False         #draws line grid on top of tiles if True
ChangeDefaultFolder = True    #change the last opened folder to if True.  Otherwise keep /maps/ as default
ReverseMouseWheel = False     #change the mousewheel zoom to go the other direction if True
DrawHandles = True            #draw the handles on drawing items.

#-------------------------------------------------------------------------------
#add new variables below this line;  those above are included in .ini file as of v2.2

MapfileSpecificationVersion = 2.6
TilesetSpecificationVersion = 2.0

RightMousePoint = None #used to keep track of where the mouse was right-clicked

FontData = None #This will hold a wxFontData object, otherwise defaults are used.
TextForegroundColor = wx.Colour(0,0,0,255)
TextBackgroundColor = wx.Colour(255,255,255,255)
TextFont = None  #exFont object.  Set to system default font at frame init
OpaqueBackground = True 

SelectMode = 'tile' #Select mode is 'tile', 'icon', 'draw', 'fog'

FrameSize = None
SashPosition = None

HighlightColor = wx.Colour(255, 0, 0, 255)
HighlightPenWidth = 2
HighlightPenStyle = wx.SOLID
HighlightPen = None #wx.Pen(SelectionColor, SelectionPenWidth, SelectionPenStyle)

OutlineTiles = False  #if True, outline the tiles when printing
OutlineTilesColor = wx.Colour(255,0,0)  #default to red

RubberBandStart = None  # used to define the selection box
RubberBandEnd = None
RubberBandPrevious = None # end point of the previous box

ShowTips = True #Show user tips at startup?
LastTip = 0 #What was the last tip the user saw?

key_index = 0 #unique ID assigned to every tile loaded.

class LayerItem():
  """Display order of the layers is controlled by the position in the list"""
  def __init__(self, index=None, name=None):
    self.index = index         #unique index for the layer item
    self.name = name           #name of the layer
    self.display = True        #show on the map window?
    self.pages = []            #list of pages to display layer on
    self.opacity = 1.0         #0.0 = transparent; 1.0 = opaque
    self.activeLayer = False   #only one layer can be active at a time
    return
  def RenameLayer(self, newName):
    self.name = newName
    return
  def ChangeOpacity(self, newOpacity):
    self.opacity = newOpacity
    return

LayerList = [LayerItem(index=0, name='Base')]   # listing of the current layers.  Must always have at least one layer.
ActiveLayer = 0     #which layer is currently active
TilesetList = []
LayerDialog = None  #reference to the layers dialog

toolbar = None #reference to the toolbar on the main frame

tilesets = []  #list of loaded tilesets
tilesetMW_display = []  #list of selected tilesets displayed on the Map Window
tilesetTW_display = []  #list of selected tilesets displayed on the Tile Window
templist = [] #used for the dynamic right click menu for assigning layers.

TrapSaveType = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA','REF', 'FORT', 'WILL', 'None']
TrapTrigger = ['Location', 'Proximity', 'Sound', 'Visual', 'Touch', 'Timed', 'Spell']
TrapReset = ['No Reset', 'Repair', 'Manual', 'Automatic']
TrapBypass = ['Lock', 'Hidden Lock', 'Hidden Switch']
TrapAttackType = ['Ranged', 'Melee', 'n/a', 'Spell', 'Pit', 'Other']
TrapSaveAmount = ['Avoid Effect', 'Half Damage', 'No Save']
TrapDialogPosition = None

rtc_open = False  #Set to true if the rich text control is open, to prevent map window SetFocus()
rtc_icon = None   #set to the current icon being edited;  this is a RoomInfo class item.

CurrentRoom = None  #created when the RTC window is opened.
IconScaleFactor = 0.85   #scales the room icons to this fraction of a 1x1 tile
ShowIcons = True  #set to T/F to show the room, treasure, monseter, etc. icons

SRD_RacesList = []
NPC_Classes = ["None","Any","Adept","Aristocrat",'Barbarian',"Bard",
               "Cleric","Commoner","Druid","Expert","Fighter","Monk",
               "Paladin","Ranger","Rogue","Sorcerer","Warrior","Wizard"]
NPC_Races = ["Any","Dwarf","Elf","Gnome","HalfElf", "Halfling","HalfOrc","Human"]
NPC_Sex = ['Any', 'Male', 'Female']
NPC_Alignments = [ "Any", "Chaotic Evil", "Chaotic Good", "Any Chaotic", "Chaotic Neutral",
                    "Lawful Good", "Lawful Neutral", "Lawful Evil", "Any Lawful",
                    "Neutral Good", "Neutral Evil", "True Neutral", "Any Neutral"]
NPC_AbilityGeneration = ['Straight 3d6', 'Best of 4d6', 'Modified 4d6', 'Straight 18s']
NPC_Languages = ['Common',    'Elven',    'Dwarven', 'Gnome',  'Halfling',
                 'Orc',       'Sylvan',   'Ignan',   'Goblin', 'Undercommon',
                 'Terran',    'Draconic', 'Giant',   'Gnoll',  'Abyssal',
                 'Celestial', 'Infernal', 'Auran']
NPC_Size = ['Any','Fine', 'Diminutive', 'Tiny', 'Small', 'Medium', 'Large', 'Huge', 'Gargantuan', 'Colossal']

NPC_Class_Info = []  #info about spell numbers, special abilitites, saves
NPC_Skill_Info = []  #info about class skills and points per level
NPC_Feat_Info = []   #list of feats
d20_Spell_List = []  #list of spells

MonsterTypes = ['Any','Aberration','Animal','Construct','Dragon','Elemental',
                'Fey','Giant','Magical Beast','Monstrous Humanoid','Ooze',
                'Outsider','Plant','Undead','Vermin']

NPC_Names = None

PromptSave = False              #prompt for saving the existing file?
d20_SRD_data_available = False  #set to True if PF/d20 data files are loaded
DnD_5E_data_available = False   #set to True if 5th Edition data is loaded

StartupOffset = None  #used to offset the import tile progress dialog.

HighlightIcons = True
HighlightIconColor = wx.Colour(255,255,0)
ShowIconNamesOnMap = True

HexGridMode = False  #False for grid, or 'A' or 'B'
DrawHexCenterDot = True
HexCenterPoints = []

MapPageList = []            #data for changing notebook pages
MapPanelPosition = wx.Point(0,0)
MapPanelList = []           #list of wxScrolledWindows for the pages
ResetTileStatistics = True  #Reset the tile usage for each new map page

TilePageList = []           #Page_Record data for changing notebook pages
TilePanelList = []          #list of wxScrolledWindows for the pages

TileImportLocation = 'CurrentPage'  #when importing tilesets,  it goes to 'NewPage' or to 'CurrentPage'

class DrawingObject_Record():
  """tool may be Freehand, Line, Multiline, OutlineRect, Point,
  FilledRect, OutlineCircle, FillCircle, Image, GetProperty, ChangeProperty"""
  def __init__(self, startpoint=None, tool_type=None, init_brush=None,
               init_pen=None, init_page_name=None):
    self.selected = False            #has this item been selected?
    self.line = []                   # [wxPoint(start), wxPoint(end)] OR [wxPoint(start), wxPoint(end), ...]
    self.circle = []                 # [wxPoint(center), int(radius)]
    self.rect = wx.Rect2D(0,0,0,0)   #wxRect()
    self.image = None                #wxImage for custom bitmaps
    self.image_filename = None       #source filename for the image
    self.image_path = None           #folder path
    self.handles = []                #list of wxRect 
    self.handle_index = None
    self.layer = 0                   #index of the layer to display on, not the position in the gv.LayerList list
    self.page_name = None            #this is the name of the page to display on.
    self.object_type = SelectMode    #set to either 'draw' or 'fog' depending on the item.
    self.fog_density = None          #player view density from 0-1
    
    if (init_page_name):
      self.page_name = init_page_name
 
    if (init_brush):
      self.brush = init_brush
    else:
      self.brush = wx.BLACK_BRUSH  #wxBrush
    if (init_pen):
      self.pen = init_pen
    else:
      self.pen = wx.BLACK_PEN  #wxPen
    self.tool = tool_type  #Freehand, Line, Multiline, OutlineRect, FilledRect, OutlineCircle, FillCircle, Image
    if (tool_type == 'Line'):
      self.line.append(startpoint)
    elif (tool_type == 'Point'):  #point is a line with length zero
      self.circle.append(startpoint)
    elif (tool_type == 'Multiline'):
      self.line.append(startpoint)
    elif (tool_type == 'Freehand'):
      self.line.append(startpoint)
    elif (tool_type == 'OutlineRect') or (tool_type == 'FilledRect'):
      self.rect = wx.Rect(startpoint.x, startpoint.y, 0,0)
    elif (tool_type == 'OutlineCircle') or (tool_type == 'FillCircle'):
      self.circle.append(startpoint)
    return
  
#end DrawingObject_Record class
DrawingSelectPen = None            #setup during the read_ini_file
DrawingObject = None               #DrawingObject_Record
DrawingToolBrush = wx.BLACK_BRUSH  #wx.Brush
DrawingToolPen = wx.BLACK_PEN      #wx.Pen
DrawingToolStartPoint = None       #wx.Point
DrawingToolPrevious = None         #wx.Point
DrawingTool = None  #Line, Multiline, OutlineRect, FillRect, OutlineCircle, FillCircle, Image, Select, Delete
DrawFillColor = wx.Colour(0,255,0,255)
DrawOutlineColor = wx.Colour(0,0,255,255)
ShowDrawingObjects = True  #global filter to turn display off for all draw objects
ShowFogObjects = True      #global filter to turn display off for all fog objects
MainFogDensity = 0.3       #density for main map window; 0 is fully transparent, 1 is fully opaque
MapFogColor = wx.Colour(107,107,107,255)
DrawingNextStep = 'start'  #depending on the tool, this is the next action to take.  Allows for the MouseUp to sync with the right operation
DrawIntermediate = False   #draw the segments on a multiline

ShowIntermediateGridLines = False               #Show intermediate lines?
IntermediateGridColor = wx.Colour(0,255,0,255)  #Secondary grid line color
IntermediateGridLinesInterval = 3               #how many secondary lines at a time

PlayerList = []   #list of player_data items used by the Combat Tracker dialog

DisplayIconInformation = True #this flag will pop up the user information when hovering over an icon.
TempPageIndex = 0

IRC_Message_Queue = []           #set the following flags to False when a message is taken off

IRC_GameTableCheckQueue = False  #set to True when the GameTable should check the message queue
IRC_PyMapperCheckQueue = False   #set to True when pymapper should check the message queue

IRC_RunServer = True
IRCserver = None
IRCchannel = None
IRCname = None
IRCpassword = None

IRCParticipants = []  #list of players in the game
GameTableDisplayFog = True   #DM can switch on and off;  always on for PC's
GameTableTool = None
GameTableLightRadius = 20  #radius for bright illumination in feet.  Set from GameTools dialog
GameTableFogDensity = 1.0  #grid cell density is set between 0.0 (transparent) and 1.0 (opaque)
GameTableMask = []

SecondaryScreen = None   #points to a reference of the secondary map screen
GridScale = 5            #scale for use in light sources and fog.  Feet per square.
FogAddBrushRadius = 5
FogRemoveBrushRadius = 5

DrawMapDiagonals = False  #Draw map diagonals for an isometric map
IsometricViewer = False   #otherwise, a reference to the IsometricMapDialog

SaveSRD_Traps = False
SaveSRD_Monsters = False
SaveSRD_Spells = False
SaveSRD_Feats = False
SaveSRD_ClassSkills = False
SaveSRD_ClassTable = False
SaveSRD_Names = False
SaveSRD_Races = False

UserName = None
UserEmail = None
UserReceiveUpdates = False
UserSendCrashInfo = False
UserComments = None

PymapperUser = False

UserMonster5E_NextIndex = 100000
UserSpell5E_NextIndex = 100000

########################################################################
class ConditionColorsBase:
  """These are the highlight colors used in the labels for monsters"""

  #----------------------------------------------------------------------
  def __init__(self):
    """Constructor default colors"""
    self.BlindedColor = wx.Colour(0,0,0,255)
    self.CharmedColor = wx.Colour(255,0,128,255)
    self.ConcentratingColor = wx.Colour(0,0,255)
    self.DeafenedColor = wx.Colour(128,0,255,255)
    self.FrightenedColor = wx.Colour(255,0,0,255)
    self.GrappledColor = wx.Colour(128,128,128,255)
    self.IncapacitatedColor = wx.Colour(255,128,0,255)
    self.InvisibleColor = wx.Colour(225,175,119,255)
    self.ParalyzedColor = wx.Colour(120,237,182,255)
    self.PetrifiedColor = wx.Colour(64,128,128,255)
    self.PoisonedColor = wx.Colour(0,255,0,255)
    self.ProneColor = wx.Colour(128,128,255,255)
    self.RestrainedColor = wx.Colour(255,255,0,255)
    self.StunnedColor = wx.Colour(128,64,0,255)
    self.TurnedColor = wx.Colour(128,128,64,255)
    self.UnconsciousColor = wx.Colour(128,255,255,255)
    return
  
  def GetConditionColor(self, condition):
    """returns the selected condition color"""
    if (condition == 'Blinded'):
      return self.BlindedColor
    elif (condition == 'Charmed'):
      return self.CharmedColor
    elif (condition == 'Concentrating'):
      return self.ConcentratingColor
    elif (condition == 'Deafened'):
      return self.DeafenedColor
    elif (condition == 'Frightened'):
      return self.FrightenedColor
    elif (condition == 'Grappled'):
      return self.GrappledColor
    elif (condition == 'Incapacitated'):
      return self.IncapacitatedColor
    elif (condition == 'Invisible'):
      return self.InvisibleColor
    elif (condition == 'Paralyzed'):
      return self.ParalyzedColor
    elif (condition == 'Petrified'):
      return self.PetrifiedColor
    elif (condition == 'Poisoned'):
      return self.PoisonedColor
    elif (condition == 'Prone'):
      return self.ProneColor
    elif (condition == 'Restrained'):
      return self.RestrainedColor
    elif (condition == 'Stunned'):
      return self.StunnedColor
    elif (condition == 'Turned'):
      return self.TurnedColor
    elif (condition == 'Unconscious'):
      return self.UnconsciousColor
    else:  #return white
      return wx.Colour(255,255,255,255)

  def ChangeColor(self, condition, color):
    """condition is the text name of the condition to change
       color is a valid wx.Colour()
    """
    if (condition == 'Blinded'):
      self.BlindedColor = color
    elif (condition == 'Charmed'):
      self.CharmedColor = color
    elif (condition == 'Concentrating'):
      self.ConcentratingColor = color
    elif (condition == 'Deafened'):
      self.DeafenedColor = color
    elif (condition == 'Frightened'):
      self.FrightenedColor = color
    elif (condition == 'Grappled'):
      self.GrappledColor = color
    elif (condition == 'Incapacitated'):
      self.IncapacitatedColor = color
    elif (condition == 'Invisible'):
      self.InvisibleColor = color
    elif (condition == 'Paralyzed'):
      self.ParalyzedColor = color
    elif (condition == 'Petrified'):
      self.PetrifiedColor = color
    elif (condition == 'Poisoned'):
      self.PoisonedColor = color
    elif (condition == 'Prone'):
      self.ProneColor = color
    elif (condition == 'Restrained'):
      self.RestrainedColor = color
    elif (condition == 'Stunned'):
      self.StunnedColor = color
    elif (condition == 'Turned'):
      self.TurnedColor = color
    elif (condition == 'Unconscious'):
      self.UnconsciousColor = color

    return
  
ConditionColors = ConditionColorsBase()
ConditionBarThickness = 15

FTP_Filename = None
FTP_Server = None
FTP_Username = None
FTP_Password = None
FTP_SaveUserInfo = False

OutlineOnHover = False  #should we outline objects under the mouse?
SnapIconToGrid = True  #snap icon placement to grid?
