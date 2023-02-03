#!/usr/bin/python
#-----------------------------------------------------------------------------
# Name:        pymapper.py
# Purpose:     Dungeon Tiles PyMapper
#
# Author:      Michael Seely, P.E.
#
# Created:     2009/06/14
# RCS-ID:      $Id: PyMapper.py $
# Copyright:   (c) 2009-2015 Michael S Seely, P.E.
# Licence:     Gnu General Public License v3
#-----------------------------------------------------------------------------

#/////////////////////////////////////////////////////////////////////////////
#Subversion Revision History
#5.04:  Removed support for the gv.cbLayerSelect control in the toolbar
#       due to crashing on Ubuntu 10.x
#5.3:   Beginning of hexagon map implementation.  Abandonded development 12/24/10
#7.2    Removed image transformation routines.  No user feedback on desirability of 
#       the feature, and caused issues for MacOS and Linux installations due to the lack of a PIL module for these platforms
#       This feature remains in 7.1 and 7.0 versions.
#8.0....Conversion to using wxFormBuilder for all dialog creation;  xrc is no longer used by pymapper
#8.0.6..Map fog working
#8.0.10  Removed self.LoadMarkerFiles() from program execution to test on kubuntu linux
#8.3.2  self.LoadSymbolFiles and self.LoadMarkerFiles automatically add tile pages on win32 only
#8.6    hex map removed from code.  12/5/14
#9.0    Support for 5E D&D monsters, improved handling of icons.  Email Registration.
#9.1    Fixed email registration, removed many references to sys.platform status using os.path.join instead.

from __future__ import division   #this makes 5/10 = 0.5, not 0
                                  # 5//10 = 0
#standard python modules
import wx     #Using a version higher than 2.8.12 will result in breaks in RichTextCtrl
import wx.adv
import os
import shutil #high level file operations
import time
import math
import operator
import copy
import sys
import string    #constants for validators
import logging   #record error messages in pymapper_errors.log in the program startup directory.
import glob      #pathname pattern expansion
import platform  #detection of mac/win/linux architecture
import random    #random number generator
import pickle    #routine for saving data files; new for v8.5
import smtplib   #simple email client for registration info;  new in v9.0
import subprocess  #opening help file exe
import ftplib      #updating of map images to a remote server. new in v9.4
from email.mime.text import MIMEText
#import profile

#extra wxpython modules
import wx.richtext as rt

#pymapper developed modules
import srd as srd      #functions for reading xml files 
import global_vars as gv
import PyMapperDialogs
import fog as fog             #fog of war 
import treasure as ts  #information for d20 treasure items
import gsl             #information for 4th Edition D&D license stuff

#import RichTextControl_Images  #removed in v9.4

#unused modules.  May include in future versions
#import Image, ImageDraw  #Python Imaging Library  (PIL)
#import imaging           #image conversion routines for PIL

menu_titles = [ "Zoom In", "Zoom Out", "Show All", "Other" ]
temp_page_index = 0
SINE_45 = 0.707106   #sine(45 degrees)
COSINE_45 = 0.707106

SPLASH = False

menu_title_by_id = {}
for title in menu_titles:
  menu_title_by_id[ wx.Window.NewControlId() ] = title

RoomIcon = None
TrapIcon = None
MonsterIcon = None 
ImageNotFound = None

VERSION = '9.7'

files_wildcard = "Map file (*.map)|*.map|Geomorph file (*.pgf)|*.pgf"
map_wildcard = "Map file (*.map)|*.map"
geomorph_wildcard = "Geomorph file (*.pgf)|*.pgf"
xml_wildcard = "Room Description file (*.xml)|*.xml"
tilesets_wildcard = "Tileset file (*.set)|*.set"
images_wildcard = "Image Files (*.jpg; *.png; *.gif) | *.jpg; *.png; *.gif"
export_wildcard = "JPEG Image (*.jpg) | *.jpg|" "PNG Image (*.png) | *.png"

class TilesetBrowserDialog(PyMapperDialogs.TilesetBrowserBase):
  def __init__(self, parent):
    olddir = os.getcwd()
    os.chdir(gv.root_directory)  #this is necessary so that bitmap paths are read by the dialog code correctly
    
    PyMapperDialogs.TilesetBrowserBase.__init__(self, parent)
    os.chdir(olddir)
    self.bAddTileset.Enable(False)
    self.bSubtractTileset.Enable(False)
    self.lsTilesetList.InsertColumn(0,"Tileset Name")
    self.lsTilesetList.InsertColumn(1,"Set ID")
    self.lsTilesetList.InsertColumn(2,"Num. Sets")
    self.lsTilesetList.InsertColumn(3,"Loaded?")
    self.lsTilesetList.InsertColumn(4,"Path + Filename")

    self.selected_layer = None  #this will be a wxListItem when an object is selected.
    self.LoadedColor = wx.Colour(0,174,0)
    self.LoadedColorText = wx.Colour(255,255,0)  #color for text when qty changed.

    self.LoadQueueColor = wx.Colour(255,255,0)
    self.LoadQueueColorText = wx.Colour(128,0,0)

    self.UnloadQueueColor = wx.Colour(255,53,53)
    self.UnloadQueueColorText = wx.Colour(255,255,255)

    self.NormalColor = wx.Colour(255,255,255)
    self.NormalColorText = wx.Colour(0,0,255)

    tileset = TileSet()
    index = 0

    #copy the tilesets list
    self.tilesets = copy.deepcopy(gv.tilesets)
    self.tilesets.reverse()
    for tileset in self.tilesets:
      listitem = wx.ListItem()
      listitem.SetText(tileset.Name)
      index = self.lsTilesetList.InsertItem(listitem)
      listitem.SetId(index)

      self.lsTilesetList.SetStringItem(index, 1, tileset.SetID)
      self.lsTilesetList.SetStringItem(index, 2, str(tileset.copies))
      self.lsTilesetList.SetStringItem(index, 3, str(tileset.loaded))
      self.lsTilesetList.SetStringItem(index, 4, tileset.filename)
      if (tileset.loaded):
        listitem.SetBackgroundColour(self.LoadedColor)
      self.lsTilesetList.SetItem(listitem)

    self.lsTilesetList.SetColumnWidth(0,wx.LIST_AUTOSIZE)
    self.lsTilesetList.SetColumnWidth(4,wx.LIST_AUTOSIZE)

    return

  def OnClose(self, event):
    self.EndModal(True)
    return

  def OnHelp(self, event):
    text = "The tileset browser displays a list of all available tilesets located in the tilesets folder where pymapper is installed.\n\n"
    text += "Individual tilesets will be highlighted based on their status.  Green indicaates that a tileset has been loaded.  To load a new tileset, doubleclick the entry, and it will change to yellow.  Doubleclick a loaded tileset to unload it;  the name will change to a red highlight.\n\n"
    text += "Then importing tilesets, pymapper will import them to the currently selected page on main window, or you can have pymapper create new tilepages to imoport to.  If you select the 'Import to separate pages' option, you will be prompted to provide a page name for the tilesets as they are loaded.\n\n"
    text += "If you wish to change the page assignments where tilesets appear, click on the 'Change Page Assignments' button in the lower left."
    dlg = HelpDialog(self, text)
    dlg.ShowModal()
    dlg.Destroy()
    return

  def OnCancel(self, event):
    self.EndModal(False)
    return

  def OnChangePageAssignments(self, event):
    """Brings up the tileset library manager dialog."""
    app.OnOptionsTilesets()
    return

  def OnAddTileset(self, event):
    #add a copy to the available tilesets
    self.tilesets[self.selected_layer].copies += 1
    self.bSubtractTileset.Enable(True)
    self.lsTilesetList.SetStringItem(self.selected_layer, 2, str(self.tilesets[self.selected_layer].copies))
    if (self.lsTilesetList.GetItemBackgroundColour(self.selected_layer) == self.LoadedColor):
      self.lsTilesetList.SetItemTextColour(self.selected_layer, self.LoadedColorText)
    elif (self.lsTilesetList.GetItemBackgroundColour(self.selected_layer) == self.LoadQueueColor):
      self.lsTilesetList.SetItemTextColour(self.selected_layer, self.LoadQueueColorText)
    elif (self.lsTilesetList.GetItemBackgroundColour(self.selected_layer) == self.UnloadQueueColor):
      self.lsTilesetList.SetItemTextColour(self.selected_layer, self.UnloadQueueColorText)
    else:
      self.lsTilesetList.SetItemTextColour(self.selected_layer, self.NormalColorText)
    self.lsTilesetList.SetItemState(self.selected_layer, (not wx.LIST_STATE_SELECTED), wx.LIST_STATE_SELECTED)
    return

  def OnSubtractTileset(self, event):
    self.tilesets[self.selected_layer].copies -= 1
    if (self.tilesets[self.selected_layer].copies <= 0):
      self.tilesets[self.selected_layer].copies = 0
      self.bSubtractTileset.Enable(False)
    self.lsTilesetList.SetStringItem(self.selected_layer, 2, str(self.tilesets[self.selected_layer].copies))
    if (self.lsTilesetList.GetItemBackgroundColour(self.selected_layer) == self.LoadedColor):
      self.lsTilesetList.SetItemTextColour(self.selected_layer, self.LoadedColorText)
    elif (self.lsTilesetList.GetItemBackgroundColour(self.selected_layer) == self.LoadQueueColor):
      self.lsTilesetList.SetItemTextColour(self.selected_layer, self.LoadQueueColorText)
    elif (self.lsTilesetList.GetItemBackgroundColour(self.selected_layer) == self.UnloadQueueColor):
      self.lsTilesetList.SetItemTextColour(self.selected_layer, self.UnloadQueueColorText)
    else:
      self.lsTilesetList.SetItemTextColour(self.selected_layer, self.NormalColorText)
    self.lsTilesetList.SetItemState(self.selected_layer, (not wx.LIST_STATE_SELECTED), wx.LIST_STATE_SELECTED)
    return

  def OnClearSelection(self, event):
    self.lsTilesetList.SetItemState(self.selected_layer, (not wx.LIST_STATE_SELECTED), wx.LIST_STATE_SELECTED)
    self.bAddTileset.Enable(False)
    self.bSubtractTileset.Enable(False)
    return


  def ChangeTilesetStatus(self, event):
    BKcolor = self.lsTilesetList.GetItemBackgroundColour(self.selected_layer)
    if (BKcolor == self.LoadedColor):  #if loaded, unload
      self.lsTilesetList.SetItemBackgroundColour(self.selected_layer, self.UnloadQueueColor)
    elif (BKcolor == self.LoadQueueColor): #if queued for loading, cancel it (do not load)
      self.lsTilesetList.SetItemBackgroundColour(self.selected_layer, self.NormalColor)
    elif (BKcolor == self.UnloadQueueColor): #if changed to unload, cancel (leave as loaded)
      self.lsTilesetList.SetItemBackgroundColour(self.selected_layer, self.LoadedColor)
    else: #load tileset
      self.lsTilesetList.SetItemBackgroundColour(self.selected_layer, self.LoadQueueColor)

    self.lsTilesetList.SetItemState(self.selected_layer, (not wx.LIST_STATE_SELECTED), wx.LIST_STATE_SELECTED)
    return

  def OnItemSelected(self, event):
    self.selected_layer = event.GetIndex()
    if (self.tilesets[self.selected_layer].copies >= 0):
      self.bSubtractTileset.Enable(True)
    self.bAddTileset.Enable(True)
    return

class  MonsterHoverDialog(PyMapperDialogs.MonsterHoverBase):
  """  This dialog hovers over the monster icon
       room is from the RoomInfo record
       room.monster must be a valid Monster_Record() or Monster5E_Record()
       window_position is the wxPoint to place the window
  """
  def __init__(self, parent, room, window_position):
    self.HPChanged = False
    currentDir = os.getcwd()
    os.chdir(gv.root_directory)
    PyMapperDialogs.MonsterHoverBase.__init__(self, parent)
    os.chdir(currentDir)
    self.room = room  #keep a reference to the room so that the size of the dialog can be saved
    
    #data structure for Monster_Record() and Monster5E_Record() are different
    #this affects how the fields are filled out
    
    if (isinstance(room.monster, srd.Monster5E_Record)):
      self.Monster5E = True
      if (room.monster.deathSaveFail > 0):
        self.cbDeathSaveFail1.SetValue(True)
        if (room.monster.deathSaveFail == 2):
          self.cbDeathSaveFail2.SetValue(True)
        if (room.monster.deathSaveFail == 3):
          self.cbDeathSaveFail2.SetValue(True)
          self.cbDeathSaveFail3.SetValue(True)
      if (room.monster.deathSavePass > 0):
        self.cbDeathSavePass1.SetValue(True)
        if (room.monster.deathSavePass == 2):
          self.cbDeathSavePass2.SetValue(True)
        if (room.monster.deathSaveFail == 3):
          self.cbDeathSavePass2.SetValue(True)
          self.cbDeathSavePass3.SetValue(True)
        
      if (room.monster.image):
        #set the image for the monster on the selector button
        xsize = room.monster.image.GetWidth()
        if (xsize != 100): #resize the image
          image = room.monster.image.Scale(100, 100)
        else:
          image = room.monster.image
        bmp = wx.BitmapFromImage(image)
        self.bCustomImage.SetBitmapLabel(bmp)

    else:
      self.Monster5E = False
      self.bRenameMonster.Show(False)
      self.cbDeathSaveFail1.Hide()
      self.cbDeathSaveFail2.Hide()
      self.cbDeathSaveFail3.Hide()
      self.cbDeathSavePass1.Hide()
      self.cbDeathSavePass2.Hide()
      self.cbDeathSavePass3.Hide()
      self.stDeathSaves.Hide()
      
    
    if (self.Monster5E) and (room.monster.customName):
      self.SetLabel(room.monster.customName + " ("+room.monster.TypeInfo()+")")
    elif (room.monster.name):
      self.SetLabel(room.monster.name + " ("+room.monster.TypeInfo()+")")
    else:
      self.SetLabel("Unnamed")
      
    if (self.Monster5E) and (room.monster.HD != None):
      self.bCalculateHP.SetToolTipString("Click to recalculate HP using HD: %s" % room.monster.HD)
    self.spArmorClass.SetValue(room.monster.AC)
    self.spHitPoints.SetValue(room.monster.HP)
    self.HitDice = room.monster.HD
    self.StartHP = room.monster.startHP
    self.stStartHP.SetLabel("Full HP:"+str(room.monster.startHP))
    self.stXPvalue.SetLabel("XP: "+room.monster.XP + "   CR:" +room.monster.CR)
    
    if (self.Monster5E):
      self.stPassivePerception.SetLabel("PP: "+room.monster.passive_perception)
    else:
      self.stPassivePerception.Show(False)

    if (gv.Spells5E != []) and (self.Monster5E):
      if (room.monster.spells == []):
        self.tcSpellTree.Hide()
        self.txSpells.Hide()
        self.stSpellLabel.Hide()
        self.stSpellDescription.Hide()
      else: #set up the spell tree by unpacking the spell data
        self.SpellRoot = self.tcSpellTree.AddRoot("Spells")
        for spellLevel in room.monster.spells:
          child = self.tcSpellTree.AppendItem(self.SpellRoot, spellLevel)
          if (spellLevel == 'Level0'):
            self.tcSpellTree.SetItemText(child, "Cantrips")
          elif (spellLevel == 'Level1'):
            self.tcSpellTree.SetItemText(child, ("Level 1: " + room.monster.spellSlots['Slot1'] + " slots"))
          elif (spellLevel == 'Level2'):
            self.tcSpellTree.SetItemText(child, ("Level 2: " + room.monster.spellSlots['Slot2'] + " slots"))
          elif (spellLevel == 'Level3'):
            self.tcSpellTree.SetItemText(child, ("Level 3: " + room.monster.spellSlots['Slot3'] + " slots"))
          elif (spellLevel == 'Level4'):
            self.tcSpellTree.SetItemText(child, ("Level 4: " + room.monster.spellSlots['Slot4'] + " slots"))
          elif (spellLevel == 'Level5'):
            self.tcSpellTree.SetItemText(child, ("Level 5: " + room.monster.spellSlots['Slot5'] + " slots"))
          elif (spellLevel == 'Level6'):
            self.tcSpellTree.SetItemText(child, ("Level 6: " + room.monster.spellSlots['Slot6'] + " slots"))
          elif (spellLevel == 'Level7'):
            self.tcSpellTree.SetItemText(child, ("Level 7: " + room.monster.spellSlots['Slot7'] + " slots"))
          elif (spellLevel == 'Level8'):
            self.tcSpellTree.SetItemText(child, ("Level 8: " + room.monster.spellSlots['Slot8'] + " slots"))
          elif (spellLevel == 'Level9'):
            self.tcSpellTree.SetItemText(child, ("Level 9: " + room.monster.spellSlots['Slot9'] + " slots"))
          for spell in room.monster.spells[spellLevel]:
            self.tcSpellTree.AppendItem(child, spell)
        self.tcSpellTree.ExpandAllChildren(self.SpellRoot)

    if (self.Monster5E):
      actionText = room.monster.actions + "\n" + room.monster.legendaryAction
    else:
      actionText = "Attack: " + room.monster.attack + "\nFull Attack: " + room.monster.full_attack
      
    self.txActions.SetValue(actionText)
    self.ApplyRichTextFormatting(self.txActions)
    
    text = ''
    if (room.monster.saves != ''):
      text += (room.monster.saves + '\n')
    if (self.Monster5E) and (room.monster.resistances != ''):
      text += ('Damage Resistances:~ ' + room.monster.resistances + '\n')
    if (self.Monster5E) and (room.monster.vulnerable != ''):
      text += ('Vulnerable:~ ' + room.monster.vulnerable + '\n')
    if (self.Monster5E) and (room.monster.immunities != ''):
      text += ('Immunity:~ ' + room.monster.immunities + '\n')
    if (self.Monster5E) and (room.monster.conditionImmune != ''):
      text += ('Condition Immunity:~ ' + room.monster.conditionImmune + '\n')
    if (self.Monster5E) and (room.monster.senses != ''):
      text += ('Senses:~ ' + room.monster.senses + '\n')
    if (self.Monster5E) and (room.monster.languages != ''):
      text += ('Languages:~ ' + room.monster.languages + '\n')
    if (room.monster.skills != ''):
      text += ('Skills:~ ' + room.monster.skills + '\n')
    if (room.monster.CR != ''):
      text += ('Challenge Rating:~ ' + room.monster.CR + '\n')
    if (not self.Monster5E):
      text += ('Feats:~ ' + room.monster.feats + '\n')
    
    self.txSkills.SetValue(text)
    self.ApplyRichTextFormatting(self.txSkills)
  
    text = ''
    if (self.Monster5E) and (room.monster.trait != ''):
      text += (room.monster.trait + '\n')
    if (room.monster.abilities != ''):
      text += (room.monster.abilities + '\n')
    self.txTraits.SetValue(text)
    self.ApplyRichTextFormatting(self.txTraits)
  
    text = ''
    if (room.monster.treasure != ''):
      text += ('Treasure:~ ' + room.monster.treasure + '\n')
    if (room.monster.other_text != ''):
      text += (room.monster.other_text + '\n')
    self.txOther.SetValue(text)
    self.ApplyRichTextFormatting(self.txOther)

    if (self.Monster5E) and (room.monster.userNotes != ''):
      self.txNotes.SetValue(room.monster.userNotes)
      
    if (self.Monster5E) and (room.monster.bonds != ''):
      self.txBonds.SetValue(room.monster.bonds)
      self.ApplyRichTextFormatting(self.txBonds)
      
    if (self.Monster5E) and (room.monster.flaws != ''):
      self.txFlaws.SetValue(room.monster.flaws)
      self.ApplyRichTextFormatting(self.txFlaws)
      
    if (self.Monster5E) and (room.monster.ideals != ''):
      self.txIdeals.SetValue(room.monster.ideals)
      self.ApplyRichTextFormatting(self.txIdeals)
      
    #Set speed of monster
    text = "Speed: "+room.monster.speed + "' "
    self.stSpeed.SetLabel(text)
    
    text = ''
    if (room.monster.STR):
      text += "STR:"+room.monster.STR
      text = self.AddModifierToScoreText(text, int(room.monster.STR))
    else:
      text += "STR:xx   "
      
    if (room.monster.DEX):
      text += "DEX:"+room.monster.DEX
      text = self.AddModifierToScoreText(text, int(room.monster.DEX))
    else:
      text += "DEX:xx   "
      
    if (room.monster.INT):
      text += "INT:"+room.monster.INT
      text = self.AddModifierToScoreText(text, int(room.monster.INT))
    else:
      text += "INT:xx   "
      
    self.stAbilityScores1.SetLabel(text)
    text = ''
      
    if (room.monster.CON):
      text += "CON:"+room.monster.CON
      text = self.AddModifierToScoreText(text, int(room.monster.CON))
    else:
      text += "CON:xx   "
      
    if (room.monster.WIS):
      text += "WIS:"+room.monster.WIS
      text = self.AddModifierToScoreText(text, int(room.monster.WIS))
    else:
      text += "WIS:xx   "
      
    if (room.monster.CHA):
      text += "CHA:"+room.monster.CHA
      text = self.AddModifierToScoreText(text, int(room.monster.CHA))
    else:
      text += "CHA:xx   "
    self.stAbilityScores2.SetLabel(text)
    
    if (self.Monster5E):
      self.cxCondition1.SetStringSelection(room.monster.con1)
      self.cxCondition2.SetStringSelection(room.monster.con2)
      self.cxCondition3.SetStringSelection(room.monster.con3)
      self.cxCondition4.SetStringSelection(room.monster.con4)

    #delete notebook pages with no info
    if (self.txOther.GetValue() == ''):
      self.nbInformationTabs.DeletePage(5)
    if (self.txFlaws.GetValue() == ''):
      self.nbInformationTabs.DeletePage(4)
    if (self.txBonds.GetValue() == ''):
      self.nbInformationTabs.DeletePage(3)
    if (self.txIdeals.GetValue() == ''):
      self.nbInformationTabs.DeletePage(2)
    if (self.txSkills.GetValue() == ''):
      self.nbInformationTabs.DeletePage(1)
    if (self.txTraits.GetValue() == ''):
      self.nbInformationTabs.DeletePage(0)
    

    if (room.windowSize): #if the window size was previously changed, set to old value
      self.SetSize(room.windowSize)
    else:
      self.Fit()
    position = window_position
    position.x -= 30
    position.y -= 30
    self.Move(position)
    return
  
  def OnSelectCustomImage(self, event):
    """Selects a custom image for display on the map window"""
    dlg = wx.FileDialog(self, message="Choose monster image", defaultDir=gv.tokens_directory,
                        defaultFile="", wildcard=images_wildcard, style=wx.OPEN)
    if (dlg.ShowModal()==wx.ID_OK):
      filename = dlg.GetPath()
      dlg.Destroy()
      #store as wxImage for display
      image = wx.Image(filename, wx.BITMAP_TYPE_ANY)
      if (not image.IsOk()):
        wx.MessageBox("Could not open image")
        return
      self.room.monster.image = image
      self.room.monster.filepath = filename
      #set the image for the monster on the selector button
      xsize = self.room.monster.image.GetWidth()
      if (xsize != 100): #resize the image
        image = self.room.monster.image.Scale(100, 100)
      bmp = wx.BitmapFromImage(image)
      self.bCustomImage.SetBitmapLabel(bmp)
    return
  #----------------------------------------------------------------------
  def ApplyRichTextFormatting(self, item):
    """Scans the wxTextCtrl fields and places highlighting text formatting on entries before the ~: characters"""
    """item must be a wxTextCtrl"""
    if (type(item) != wx.TextCtrl):
      return
    
    text = item.GetValue()
    
    startPosition = 0
    highlightText = False
    item.SetInsertionPoint(0)
    
    for index,char in enumerate(text):
      if (char == '~'):  #highlight from previous start to current index
        item.SetStyle(startPosition, index, wx.TextAttr("BLACK", "YELLOW"))
        startPosition = index+1
      elif (char == '^'):  #highlight legendary actions 
        item.SetStyle(startPosition, index, wx.TextAttr("WHITE", "RED"))
        startPosition = index+1
      elif (char == '\n'):  #reset the startPosition to highlight on the next line
        startPosition = index+1
    return

  
  #----------------------------------------------------------------------
  def AddModifierToScoreText(self, textstring, score):
    """Add the proper modifier to the text based on the ability score
    score must be an integer
    """
    if (not self.Monster5E):  #these bonuses only apply to 5E ruleset
      return textstring
    
    if (score <= 1):
      textstring += "(-5)  "
    elif (score <= 3):
      textstring += "(-4)  "
    elif (score <= 5):
      textstring += "(-3)  "
    elif (score <= 7):
      textstring += "(-2)  "
    elif (score <= 9):
      textstring += "(-1)  "
    elif (score <= 11):
      textstring += "(+0)  "
    elif (score <= 13):
      textstring += "(+1)  "
    elif (score <= 15):
      textstring += "(+2)  "
    elif (score <= 17):
      textstring += "(+3)  "
    elif (score <= 19):
      textstring += "(+4)  "
    elif (score <= 21):
      textstring += "(+5)  "
    elif (score <= 23):
      textstring += "(+6)  "
    elif (score <= 25):
      textstring += "(+7)  "
    elif (score <= 27):
      textstring += "(+8)  "
    elif (score <= 29):
      textstring += "(+9)  "
    elif (score <= 30):
      textstring += "(+10)  "
    
    return textstring
  
  #---------------------------------------------------
  def CalculateHPTotal(self, event):
    """Calculate new HP total based on HD for the monster"""
    #check if there is valid HD info
    self.StartHP = app.RollDice(self.HitDice)
    self.spHitPoints.SetValue(self.StartHP)
    self.stStartHP.SetLabel("Full HP:"+str(self.StartHP))
    return

  def OnRenameMonster(self, event):
    if (self.room.monster.customName):
      name = self.room.monster.customName
    elif (self.room.monster.name):
      name = self.room.monster.name
    else:
      name = 'Unnamed'
    dlg = wx.TextEntryDialog(self, "Please enter the name for this icon", "Rename", name)
    dlg.ShowModal()
    self.room.monster.customName = dlg.GetValue()
    dlg.Destroy()
    return
  
  #----------------------------------------------------------------------
  def OnSubtract20HP(self, event):
    """Subtract 20 HP from the monster"""
    self.subtractHP(20)
    return
  
  def OnSubtract10HP(self, event):
    """Subtract 10 HP from the monster"""
    self.subtractHP(10)
    return
  
  def OnSubtract5HP(self, event):
    """Subtract 5 HP from the monster"""
    self.subtractHP(5)
    return
  
  def OnSubtract1HP(self, event):
    """Subtract 1 HP from the monster"""
    self.subtractHP(1)
    return

  def subtractHP(self, damage):
    """HP is not reduced below 0"""
    self.HPChanged = True
    currentHP = self.spHitPoints.GetValue()
    value = max(0,(currentHP-damage))
    self.spHitPoints.SetValue(value)
    return
  
  def SelectSpell(self, event):
    item = srd.Spell5E_Record()
    spell = self.tcSpellTree.GetItemText(event.GetItem())
    self.txSpells.Clear()
    for item in gv.Spells5E:
      if (item.Name == spell):
        if (item.Ritual):
          ritualText = " (or Ritual)"
        else:
          ritualText = ""
        text = "Casting Time: " + item.CastTime + ritualText + "\n"
        text += "Range: "+item.SpellRange + "\n"
        text += "Duration: " + item.Duration + "\n"
        text += item.Description +"\n"
        text += "Source: " + item.SourceMaterial
        self.txSpells.SetValue(text)
        break
    return
  #----------------------------------------------------------------------


class CharacterInfoDialog(PyMapperDialogs.CharacterInfoBase):
  def __init__(self, parent, room, window_position):
    """room is a RoomInfo class item.  The IconType must be 'NPC'"""
    #room = RoomInfo()
    
    PyMapperDialogs.CharacterInfoBase.__init__(self, parent)

    if (not room.monster):
      return
    if (room.monster.name):
      self.SetName(room.monster.name)
    else:
      self.SetName("Unnamed Character")
    self.stAC_text.SetLabel(room.monster.AC)
    self.spHitPoints.SetValue(room.monster.HP)
    if (room.monster.attack):
      self.stMeleeAttack.SetLabel(room.monster.attack)
    else:
      self.stMeleeAttack.SetLabel("No melee attacks")
    if (room.monster.REF != None):
      self.stReflexSave.SetLabel(str(room.monster.REF))
    else:
      self.stReflexSave.SetLabel("Undefined")
    if (room.monster.WILL != None):
      self.stWillSave.SetLabel(str(room.monster.WILL))
    else:
      self.stWillSave.SetLabel("Undefined")
    if (room.monster.FORT != None):
      self.stFortitudeSave.SetLabel(str(room.monster.FORT))
    else:
      self.stFortitudeSave.SetLabel("Undefined")
      
    position = window_position
    position.x -= 30
    position.y -= 30
    self.Move(position)
    return

  def OnExit(self, event):
    event.Skip()
    return

class TextEntryDialog(PyMapperDialogs.TextEntryDialogBase):
  def __init__(self, parent, textlist):
    olddir = os.getcwd()
    os.chdir(gv.root_directory)  #this is necessary so that bitmap paths are read by the dialog code correctly
    
    PyMapperDialogs.TextEntryDialogBase.__init__(self, parent)
    os.chdir(olddir)
    for item in textlist:
      self.txNames.AppendText(item)
      self.txNames.AppendText('\n')
    return

  def OnOK(self, event):
    self.EndModal(True)
    return

  def OnCancel(self, event):
    self.EndModal(False)
    return

class PlayerCombatTrackingInfo():
  def __init__(self):
    self.index = 1      #Player number
    self.dead = False   #True if dead, False if alive
    self.status = "Ready"  #Could be dead, ready, or acted
    self.HP = 0
    self.name = "None"   #Name of the PC, NPC, or monster
    self.planned_action = None  #Could be 'delay' or 'ready' or None.  If none, PC/NPC will act in order of initiative 
    self.names_list = []  #list of all names entered in the text box.
    self.init = 99        #default initiative for the player
    return

class PyMapperFrame(PyMapperDialogs.PyMapperFrameCore):
  def __init__(self, parent=None):
    self.ConditionColorsDialog = None
    PyMapperDialogs.PyMapperFrameCore.__init__(self, parent)
    return
  
  def OnChangeSplitterSash(self, event):
    gv.SashPosition = self.SplitterSash.GetSashPosition()
    return
  
  def UpdateLayerSelector(self):
    for layer in gv.LayerList:
      self.cxLayerSelector.Append(layer.name)
    return
  
  def ChangeActiveLayer(self, event):
    gv.ActiveLayer = self.cxLayerSelector.GetSelection()
    if (gv.LayerDialog):
      gv.LayerDialog.UpdateLists()
    return
  
  def OnResizeTilePanel(self, event):
    if (gv.PyMapperApp):
      app.DrawTileWindow(True)
    event.Skip()
    return
  
  def ChangeSelectionMode(self,event):
    app.ChangeSelectionMode(event)
    return

  def OnFileNew( self, event ):
    app.OnFileNew(event)
    return

  def OnFileOpen( self, event ):
    app.OnFileOpen(event)
    return

  def OnFileSave( self, event ):
    app.OnFileSave(event)
    return

  def OnFileSaveAs( self, event ):
    app.OnFileSaveAs(event)
    return

  def OnTilesetBrowser( self, event ):
    app.OnTilesetBrowser(event)
    return

  def OnImportBackground( self, event ):
    app.OnImportBackground(event)
    return

  def OnUndoAction( self, event ):
    app.OnUndoAction(event)
    return

  def OnPrintMap( self, event ):
    app.OnPrintMap(event)
    return

  def OnPrintImage( self, event ):
    app.OnPrintImage(event)
    return

  def OnChangeTileQuantity(self, event):
    app.OnChangeTileQuantity(event)
    return
  
  def OnViewGrid( self, event ):
    app.OnViewGrid(event)
    return
  
  def OnViewIcons(self, event):
    app.OnViewIcons(event)
    return
  
  def OnSnapToGrid(self, event):
    app.OnSnapToGrid(event)
    return

  def OnViewBackground( self, event ):
    app.OnViewBackground(event)
    return

  def OnViewTilesetLayerFilter( self, event ):
    app.OnViewTilesetLayerFilter(event)
    return
  
  def OnViewConditionColorsLegend(self, event):
    if (self.ConditionColorsDialog):
      self.ConditionColorsDialog.Raise()
    else:
      self.ConditionColorsDialog = ConditionColorsDialog(self)
      self.ConditionColorsDialog.Show(True)
    return
  
  def OnViewFogTools(self, event):
    app.OnViewFogTools(event)
    return

  def OnDungeon_ShowIcons( self, event ):
    app.OnViewIcons(event)
    return
  
  def OnViewDrawingObjects( self, event ):
    app.OnViewDrawingObjects(event)
    return
  
  def OnViewFogObjects(self, event):
    app.OnViewFogObjects(event)
    return
  
  def OnViewShowIconNames(self, event):
    app.OnViewShowIconNames(event)
    return
  
  def OnViewDrawingHandles( self, event ):
    app.OnViewDrawingHandles(event)
    return
    
  def OnHelp_Contents( self, event ):
    app.OnHelp_Contents(event)
    return
  
  def OnHelp_OpenTutorial(self, event):
    app.OnHelp_OpenTutorial(event)
    return  

  def MapZoomIn( self, event ):
    app.RMapClickZoomIn(event)
    return
  
  def MapZoomOut( self, event ):
    app.RMapClickZoomOut(event)
    return
  
  def OnMapsIsometric (self, event):
    app.OnMapsIsometric(event)
    return

class CombatInitiativeValidator(wx.PyValidator):
  def __init__(self):
    wx.PyValidator.__init__(self)
    self.Bind(wx.EVT_CHAR, self.OnChar)
    self.Bind(wx.EVT_KILL_FOCUS, self.CheckField)
    return
  
  def Clone(self):
    return CombatInitiativeValidator()
  
  def Validate(self, win):
    """Validate the contents of a control"""
    widget = self.GetWindow()
    value = widget.GetValue()
    if (value[0] == '-'):
      value = value.strip('-')
    for x in value:
      if (x not in string.digits):
        return False
    return True
  
  def CheckField(self, event):
    """Check to make sure that the negative sign is not in the wrong space"""
    widget = self.GetWindow()
    value = widget.GetValue()
    
    if ('-' in value) and (value[0] != '-'):
      #negative in the wrong position
      widget.SetBackgroundColour("pink")
      widget.SetFocus()
      widget.Refresh()
      return False
    else:
      widget.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
      widget.Refresh()
      return True
      
  def OnChar(self, event):
    key = event.GetKeyCode()
    if key < wx.WXK_SPACE or key == wx.WXK_DELETE or key > 255:
      event.Skip()
      return
    if (chr(key) in string.digits) or (key == 45):
      event.Skip()
      return

    # Returning without calling even.Skip eats the event before it
    # gets to the text control
    return
  
  def TransferToWindow(self):
    """ We simply return True, as we don't do any data transfer."""
    return True # Prevent wxDialog from complaining.

  def TransferFromWindow(self):
    """ We simply return True, as we don't do any data transfer."""
    return True # Prevent wxDialog from complaining.
  
#---------------End of CombatInitiativeValidator----------------------


class CombatTrackingDialog(PyMapperDialogs.CombatTrackingBase):
  def __init__(self, parent):
    logging.debug("INIT CombatTrackingDialog")
    validator = CombatInitiativeValidator()
    self.names_list = []
    self.current_round = 1
    olddir = os.getcwd()
    os.chdir(gv.root_directory)  #this is necessary so that bitmap paths are read by the dialog code correctly    
    PyMapperDialogs.CombatTrackingBase.__init__(self, parent)
    os.chdir(olddir)
    if (gv.PlayerList != []):
      #Saved player data from older box
      self.LoadSavedData()
      
    startID = PyMapperDialogs.p1Init
    endID = PyMapperDialogs.p15Init+1
    for item in range(startID, endID, 8):
      validator = CombatInitiativeValidator()
      widget = self.FindWindowById(item)
      widget.SetValidator(validator)

    self.SetComboBoxNames(self.names_list)
    self.SetPosition(gv.HoverPoint)
    self.stCurrentRound.SetLabel(str(self.current_round))
    self.InitiativeList = []
    logging.debug("End INIT")
    return

  def OnSortInitiative(self, event):
    """Sort the player information based on initiative ranking"""
    self.SavePlayerData()  #collect the information
    gv.PlayerList.sort(key=lambda x: int(x.init), reverse=True)
    count = 1
    for item in gv.PlayerList:
      item.index = count
      count += 1
    self.LoadSavedData()
    return
    
  def SavePlayerData(self):
    gv.PlayerList = []
    for index in range(1,16):
      item = PlayerCombatTrackingInfo()
      item.index = index
      item.names_list = copy.copy(self.names_list)
      gv.PlayerList.append(item)
    for item in gv.PlayerList:
      if (item.index == 1):
        item.init = self.txInitiative1.GetValue()
        item.dead = self.cbPlayerDead1.IsChecked()
        color = self.bActivateP1.GetBackgroundColour()
        if (color == wx.Colour(0,128,0)):
          item.status = "Ready"
        elif (color == wx.Colour(255,0,0)):
          item.status = "Acted"
        item.HP = int(self.spHitPointsP1.GetValue())
        item.name = str(self.cbPlayer1.GetValue())
        if (self.rbPlayer1d.GetValue() == True):
          item.planned_action = 'delay'
        elif (self.rbPlayer1r.GetValue() == True):
          item.planned_action = 'ready'
        else:
          item.planned_action == None
      elif (item.index == 2):
        item.init = self.txInitiative2.GetValue()
        item.dead = self.cbPlayerDead2.IsChecked()
        color = self.bActivateP2.GetBackgroundColour()
        if (color == wx.Colour(0,128,0)):
          item.status = "Ready"
        elif (color == wx.Colour(255,0,0)):
          item.status = "Acted"
        item.HP = int(self.spHitPointsP2.GetValue())
        item.name = str(self.cbPlayer2.GetValue())
        if (self.rbPlayer2d.GetValue() == True):
          item.planned_action = 'delay'
        elif (self.rbPlayer2r.GetValue() == True):
          item.planned_action = 'ready'
        else:
          item.planned_action == None
      elif (item.index == 3):
        item.init = self.txInitiative3.GetValue()
        item.dead = self.cbPlayerDead3.IsChecked()
        color = self.bActivateP3.GetBackgroundColour()
        if (color == wx.Colour(0,128,0)):
          item.status = "Ready"
        elif (color == wx.Colour(255,0,0)):
          item.status = "Acted"
        item.HP = int(self.spHitPointsP3.GetValue())
        item.name = str(self.cbPlayer3.GetValue())
        if (self.rbPlayer3d.GetValue() == True):
          item.planned_action = 'delay'
        elif (self.rbPlayer3r.GetValue() == True):
          item.planned_action = 'ready'
        else:
          item.planned_action == None
      elif (item.index == 4):
        item.init = self.txInitiative4.GetValue()
        item.dead = self.cbPlayerDead4.IsChecked()
        color = self.bActivateP4.GetBackgroundColour()
        if (color == wx.Colour(0,128,0)):
          item.status = "Ready"
        elif (color == wx.Colour(255,0,0)):
          item.status = "Acted"
        item.HP = int(self.spHitPointsP4.GetValue())
        item.name = str(self.cbPlayer4.GetValue())
        if (self.rbPlayer4d.GetValue() == True):
          item.planned_action = 'delay'
        elif (self.rbPlayer4r.GetValue() == True):
          item.planned_action = 'ready'
        else:
          item.planned_action == None
      elif (item.index == 5):
        item.init = self.txInitiative5.GetValue()
        item.dead = self.cbPlayerDead5.IsChecked()
        color = self.bActivateP5.GetBackgroundColour()
        if (color == wx.Colour(0,128,0)):
          item.status = "Ready"
        elif (color == wx.Colour(255,0,0)):
          item.status = "Acted"
        item.HP = int(self.spHitPointsP5.GetValue())
        item.name = str(self.cbPlayer5.GetValue())
        if (self.rbPlayer5d.GetValue() == True):
          item.planned_action = 'delay'
        elif (self.rbPlayer5r.GetValue() == True):
          item.planned_action = 'ready'
        else:
          item.planned_action == None
      elif (item.index == 6):
        item.init = self.txInitiative6.GetValue()
        item.dead = self.cbPlayerDead6.IsChecked()
        color = self.bActivateP6.GetBackgroundColour()
        if (color == wx.Colour(0,128,0)):
          item.status = "Ready"
        elif (color == wx.Colour(255,0,0)):
          item.status = "Acted"
        item.HP = int(self.spHitPointsP6.GetValue())
        item.name = str(self.cbPlayer6.GetValue())
        if (self.rbPlayer6d.GetValue() == True):
          item.planned_action = 'delay'
        elif (self.rbPlayer6r.GetValue() == True):
          item.planned_action = 'ready'
        else:
          item.planned_action == None
      elif (item.index == 7):
        item.init = self.txInitiative7.GetValue()
        item.dead = self.cbPlayerDead7.IsChecked()
        color = self.bActivateP7.GetBackgroundColour()
        if (color == wx.Colour(0,128,0)):
          item.status = "Ready"
        elif (color == wx.Colour(255,0,0)):
          item.status = "Acted"
        item.HP = int(self.spHitPointsP7.GetValue())
        item.name = str(self.cbPlayer7.GetValue())
        if (self.rbPlayer7d.GetValue() == True):
          item.planned_action = 'delay'
        elif (self.rbPlayer7r.GetValue() == True):
          item.planned_action = 'ready'
        else:
          item.planned_action == None
      elif (item.index == 8):
        item.init = self.txInitiative8.GetValue()
        item.dead = self.cbPlayerDead8.IsChecked()
        color = self.bActivateP8.GetBackgroundColour()
        if (color == wx.Colour(0,128,0)):
          item.status = "Ready"
        elif (color == wx.Colour(255,0,0)):
          item.status = "Acted"
        item.HP = int(self.spHitPointsP8.GetValue())
        item.name = str(self.cbPlayer8.GetValue())
        if (self.rbPlayer8d.GetValue() == True):
          item.planned_action = 'delay'
        elif (self.rbPlayer8r.GetValue() == True):
          item.planned_action = 'ready'
        else:
          item.planned_action == None
      elif (item.index == 9):
        item.init = self.txInitiative9.GetValue()
        item.dead = self.cbPlayerDead9.IsChecked()
        color = self.bActivateP9.GetBackgroundColour()
        if (color == wx.Colour(0,128,0)):
          item.status = "Ready"
        elif (color == wx.Colour(255,0,0)):
          item.status = "Acted"
        item.HP = int(self.spHitPointsP9.GetValue())
        item.name = str(self.cbPlayer9.GetValue())
        if (self.rbPlayer9d.GetValue() == True):
          item.planned_action = 'delay'
        elif (self.rbPlayer9r.GetValue() == True):
          item.planned_action = 'ready'
        else:
          item.planned_action == None
      elif (item.index == 10):
        item.init = self.txInitiative10.GetValue()
        item.dead = self.cbPlayerDead10.IsChecked()
        color = self.bActivateP10.GetBackgroundColour()
        if (color == wx.Colour(0,128,0)):
          item.status = "Ready"
        elif (color == wx.Colour(255,0,0)):
          item.status = "Acted"
        item.HP = int(self.spHitPointsP10.GetValue())
        item.name = str(self.cbPlayer10.GetValue())
        if (self.rbPlayer10d.GetValue() == True):
          item.planned_action = 'delay'
        elif (self.rbPlayer10r.GetValue() == True):
          item.planned_action = 'ready'
        else:
          item.planned_action == None
      elif (item.index == 11):
        item.init = self.txInitiative11.GetValue()
        item.dead = self.cbPlayerDead11.IsChecked()
        color = self.bActivateP11.GetBackgroundColour()
        if (color == wx.Colour(0,128,0)):
          item.status = "Ready"
        elif (color == wx.Colour(255,0,0)):
          item.status = "Acted"
        item.HP = int(self.spHitPointsP11.GetValue())
        item.name = str(self.cbPlayer11.GetValue())
        if (self.rbPlayer11d.GetValue() == True):
          item.planned_action = 'delay'
        elif (self.rbPlayer11r.GetValue() == True):
          item.planned_action = 'ready'
        else:
          item.planned_action == None
      elif (item.index == 12):
        item.init = self.txInitiative12.GetValue()
        item.dead = self.cbPlayerDead12.IsChecked()
        color = self.bActivateP12.GetBackgroundColour()
        if (color == wx.Colour(0,128,0)):
          item.status = "Ready"
        elif (color == wx.Colour(255,0,0)):
          item.status = "Acted"
        item.HP = int(self.spHitPointsP12.GetValue())
        item.name = str(self.cbPlayer12.GetValue())
        if (self.rbPlayer12d.GetValue() == True):
          item.planned_action = 'delay'
        elif (self.rbPlayer12r.GetValue() == True):
          item.planned_action = 'ready'
        else:
          item.planned_action == None
      elif (item.index == 13):
        item.init = self.txInitiative13.GetValue()
        item.dead = self.cbPlayerDead13.IsChecked()
        color = self.bActivateP13.GetBackgroundColour()
        if (color == wx.Colour(0,128,0)):
          item.status = "Ready"
        elif (color == wx.Colour(255,0,0)):
          item.status = "Acted"
        item.HP = int(self.spHitPointsP13.GetValue())
        item.name = str(self.cbPlayer13.GetValue())
        if (self.rbPlayer13d.GetValue() == True):
          item.planned_action = 'delay'
        elif (self.rbPlayer13r.GetValue() == True):
          item.planned_action = 'ready'
        else:
          item.planned_action == None
      elif (item.index == 14):
        item.init = self.txInitiative14.GetValue()
        item.dead = self.cbPlayerDead14.IsChecked()
        color = self.bActivateP14.GetBackgroundColour()
        if (color == wx.Colour(0,128,0)):
          item.status = "Ready"
        elif (color == wx.Colour(255,0,0)):
          item.status = "Acted"
        item.HP = int(self.spHitPointsP14.GetValue())
        item.name = str(self.cbPlayer14.GetValue())
        if (self.rbPlayer14d.GetValue() == True):
          item.planned_action = 'delay'
        elif (self.rbPlayer14r.GetValue() == True):
          item.planned_action = 'ready'
        else:
          item.planned_action == None
      elif (item.index == 15):
        item.init = self.txInitiative15.GetValue()
        item.dead = self.cbPlayerDead15.IsChecked()
        color = self.bActivateP15.GetBackgroundColour()
        if (color == wx.Colour(0,128,0)):
          item.status = "Ready"
        elif (color == wx.Colour(255,0,0)):
          item.status = "Acted"
        item.HP = int(self.spHitPointsP15.GetValue())
        item.name = str(self.cbPlayer15.GetValue())
        if (self.rbPlayer15d.GetValue() == True):
          item.planned_action = 'delay'
        elif (self.rbPlayer15r.GetValue() == True):
          item.planned_action = 'ready'
        else:
          item.planned_action == None
    return

  def LoadSavedData(self):
    item = PlayerCombatTrackingInfo()
    self.names_list = copy.copy(gv.PlayerList[0].names_list)
    for item in gv.PlayerList:
      if (item.name != ''):
        if not(item.name in self.names_list):
          self.names_list.append(item.name)
      if (item.index == 1):
        self.txInitiative1.SetValue(item.init)
        self.cbPlayerDead1.SetValue(item.dead)
        if (item.status == "Ready"):
          self.bActivateP1.SetBackgroundColour(wx.Colour(0,128,0))
        elif (item.status == "Acted"):
          self.bActivateP1.SetBackgroundColour(wx.Colour(255,0,0))
        self.spHitPointsP1.SetValue(item.HP)
        self.cbPlayer1.SetValue(item.name)
        if (item.dead):
          self.OnKillPlayer1()
        if (item.planned_action == 'delay'):
          self.rbPlayer1d.SetValue(True)
        elif (item.planned_action == 'ready'):
          self.rbPlayer1r.SetValue(True)
        else:
          self.rbPlayer1.SetValue(True)
      elif (item.index == 2):
        self.txInitiative2.SetValue(item.init)
        self.cbPlayerDead2.SetValue(item.dead)
        if (item.status == "Ready"):
          self.bActivateP2.SetBackgroundColour(wx.Colour(0,128,0))
        elif (item.status == "Acted"):
          self.bActivateP2.SetBackgroundColour(wx.Colour(255,0,0))
        self.spHitPointsP2.SetValue(item.HP)
        self.cbPlayer2.SetValue(item.name)
        if (item.dead):
          self.OnKillPlayer2()
        if (item.planned_action == 'delay'):
          self.rbPlayer2d.SetValue(True)
        elif (item.planned_action == 'ready'):
          self.rbPlayer2r.SetValue(True)
        else:
          self.rbPlayer2.SetValue(True)   
      elif (item.index == 3):
        self.txInitiative3.SetValue(item.init)
        self.cbPlayerDead3.SetValue(item.dead)
        if (item.status == "Ready"):
          self.bActivateP3.SetBackgroundColour(wx.Colour(0,128,0))
        elif (item.status == "Acted"):
          self.bActivateP3.SetBackgroundColour(wx.Colour(255,0,0))
        self.spHitPointsP3.SetValue(item.HP)
        self.cbPlayer3.SetValue(item.name)
        if (item.dead):
          self.OnKillPlayer3()
        if (item.planned_action == 'delay'):
          self.rbPlayer3d.SetValue(True)
        elif (item.planned_action == 'ready'):
          self.rbPlayer3r.SetValue(True)
        else:
          self.rbPlayer3.SetValue(True)   
      elif (item.index == 4):
        self.txInitiative4.SetValue(item.init)
        self.cbPlayerDead4.SetValue(item.dead)
        if (item.status == "Ready"):
          self.bActivateP4.SetBackgroundColour(wx.Colour(0,128,0))
        elif (item.status == "Acted"):
          self.bActivateP4.SetBackgroundColour(wx.Colour(255,0,0))
        self.spHitPointsP4.SetValue(item.HP)
        self.cbPlayer4.SetValue(item.name)
        if (item.dead):
          self.OnKillPlayer4()
        if (item.planned_action == 'delay'):
          self.rbPlayer4d.SetValue(True)
        elif (item.planned_action == 'ready'):
          self.rbPlayer4r.SetValue(True)
        else:
          self.rbPlayer4.SetValue(True)   
      elif (item.index == 5):
        self.txInitiative5.SetValue(item.init)
        self.cbPlayerDead5.SetValue(item.dead)
        if (item.status == "Ready"):
          self.bActivateP5.SetBackgroundColour(wx.Colour(0,128,0))
        elif (item.status == "Acted"):
          self.bActivateP5.SetBackgroundColour(wx.Colour(255,0,0))
        self.spHitPointsP5.SetValue(item.HP)
        self.cbPlayer5.SetValue(item.name)
        if (item.dead):
          self.OnKillPlayer5()
        if (item.planned_action == 'delay'):
          self.rbPlayer5d.SetValue(True)
        elif (item.planned_action == 'ready'):
          self.rbPlayer5r.SetValue(True)
        else:
          self.rbPlayer5.SetValue(True)   
      elif (item.index == 6):
        self.txInitiative6.SetValue(item.init)
        self.cbPlayerDead6.SetValue(item.dead)
        if (item.status == "Ready"):
          self.bActivateP6.SetBackgroundColour(wx.Colour(0,128,0))
        elif (item.status == "Acted"):
          self.bActivateP6.SetBackgroundColour(wx.Colour(255,0,0))
        self.spHitPointsP6.SetValue(item.HP)
        self.cbPlayer6.SetValue(item.name)
        if (item.dead):
          self.OnKillPlayer6()
        if (item.planned_action == 'delay'):
          self.rbPlayer6d.SetValue(True)
        elif (item.planned_action == 'ready'):
          self.rbPlayer6r.SetValue(True)
        else:
          self.rbPlayer6.SetValue(True)   
      elif (item.index == 7):
        self.txInitiative7.SetValue(item.init)
        self.cbPlayerDead7.SetValue(item.dead)
        if (item.status == "Ready"):
          self.bActivateP7.SetBackgroundColour(wx.Colour(0,128,0))
        elif (item.status == "Acted"):
          self.bActivateP7.SetBackgroundColour(wx.Colour(255,0,0))
        self.spHitPointsP7.SetValue(item.HP)
        self.cbPlayer7.SetValue(item.name)
        if (item.dead):
          self.OnKillPlayer7()
        if (item.planned_action == 'delay'):
          self.rbPlayer7d.SetValue(True)
        elif (item.planned_action == 'ready'):
          self.rbPlayer7r.SetValue(True)
        else:
          self.rbPlayer7.SetValue(True)   
      elif (item.index == 8):
        self.txInitiative8.SetValue(item.init)
        self.cbPlayerDead8.SetValue(item.dead)
        if (item.status == "Ready"):
          self.bActivateP8.SetBackgroundColour(wx.Colour(0,128,0))
        elif (item.status == "Acted"):
          self.bActivateP8.SetBackgroundColour(wx.Colour(255,0,0))
        self.spHitPointsP8.SetValue(item.HP)
        self.cbPlayer8.SetValue(item.name)
        if (item.dead):
          self.OnKillPlayer8()
        if (item.planned_action == 'delay'):
          self.rbPlayer8d.SetValue(True)
        elif (item.planned_action == 'ready'):
          self.rbPlayer8r.SetValue(True)
        else:
          self.rbPlayer8.SetValue(True)   
      elif (item.index == 9):
        self.txInitiative9.SetValue(item.init)
        self.cbPlayerDead9.SetValue(item.dead)
        if (item.status == "Ready"):
          self.bActivateP9.SetBackgroundColour(wx.Colour(0,128,0))
        elif (item.status == "Acted"):
          self.bActivateP9.SetBackgroundColour(wx.Colour(255,0,0))
        self.spHitPointsP9.SetValue(item.HP)
        self.cbPlayer9.SetValue(item.name)
        if (item.dead):
          self.OnKillPlayer9()
        if (item.planned_action == 'delay'):
          self.rbPlayer9d.SetValue(True)
        elif (item.planned_action == 'ready'):
          self.rbPlayer9r.SetValue(True)
        else:
          self.rbPlayer9.SetValue(True)   
      elif (item.index == 10):
        self.txInitiative10.SetValue(item.init)
        self.cbPlayerDead10.SetValue(item.dead)
        if (item.status == "Ready"):
          self.bActivateP10.SetBackgroundColour(wx.Colour(0,128,0))
        elif (item.status == "Acted"):
          self.bActivateP10.SetBackgroundColour(wx.Colour(255,0,0))
        self.spHitPointsP10.SetValue(item.HP)
        self.cbPlayer10.SetValue(item.name)
        if (item.dead):
          self.OnKillPlayer10()
        if (item.planned_action == 'delay'):
          self.rbPlayer10d.SetValue(True)
        elif (item.planned_action == 'ready'):
          self.rbPlayer10r.SetValue(True)
        else:
          self.rbPlayer10.SetValue(True)   
      elif (item.index == 11):
        self.txInitiative11.SetValue(item.init)
        self.cbPlayerDead11.SetValue(item.dead)
        if (item.status == "Ready"):
          self.bActivateP11.SetBackgroundColour(wx.Colour(0,128,0))
        elif (item.status == "Acted"):
          self.bActivateP11.SetBackgroundColour(wx.Colour(255,0,0))
        self.spHitPointsP11.SetValue(item.HP)
        self.cbPlayer11.SetValue(item.name)
        if (item.dead):
          self.OnKillPlayer11()
        if (item.planned_action == 'delay'):
          self.rbPlayer11d.SetValue(True)
        elif (item.planned_action == 'ready'):
          self.rbPlayer11r.SetValue(True)
        else:
          self.rbPlayer11.SetValue(True)   
      elif (item.index == 12):
        self.txInitiative12.SetValue(item.init)
        self.cbPlayerDead12.SetValue(item.dead)
        if (item.status == "Ready"):
          self.bActivateP12.SetBackgroundColour(wx.Colour(0,128,0))
        elif (item.status == "Acted"):
          self.bActivateP12.SetBackgroundColour(wx.Colour(255,0,0))
        self.spHitPointsP12.SetValue(item.HP)
        self.cbPlayer12.SetValue(item.name)
        if (item.dead):
          self.OnKillPlayer12()
        if (item.planned_action == 'delay'):
          self.rbPlayer12d.SetValue(True)
        elif (item.planned_action == 'ready'):
          self.rbPlayer12r.SetValue(True)
        else:
          self.rbPlayer12.SetValue(True)   
      elif (item.index == 13):
        self.txInitiative13.SetValue(item.init)
        self.cbPlayerDead13.SetValue(item.dead)
        if (item.status == "Ready"):
          self.bActivateP13.SetBackgroundColour(wx.Colour(0,128,0))
        elif (item.status == "Acted"):
          self.bActivateP13.SetBackgroundColour(wx.Colour(255,0,0))
        self.spHitPointsP13.SetValue(item.HP)
        self.cbPlayer13.SetValue(item.name)
        if (item.dead):
          self.OnKillPlayer13()
        if (item.planned_action == 'delay'):
          self.rbPlayer13d.SetValue(True)
        elif (item.planned_action == 'ready'):
          self.rbPlayer13r.SetValue(True)
        else:
          self.rbPlayer13.SetValue(True)   
      elif (item.index == 14):
        self.txInitiative14.SetValue(item.init)
        self.cbPlayerDead14.SetValue(item.dead)
        if (item.status == "Ready"):
          self.bActivateP14.SetBackgroundColour(wx.Colour(0,128,0))
        elif (item.status == "Acted"):
          self.bActivateP14.SetBackgroundColour(wx.Colour(255,0,0))
        self.spHitPointsP14.SetValue(item.HP)
        self.cbPlayer14.SetValue(item.name)
        if (item.dead):
          self.OnKillPlayer14()
        if (item.planned_action == 'delay'):
          self.rbPlayer14d.SetValue(True)
        elif (item.planned_action == 'ready'):
          self.rbPlayer14r.SetValue(True)
        else:
          self.rbPlayer14.SetValue(True)   
      elif (item.index == 15):
        self.txInitiative15.SetValue(item.init)
        self.cbPlayerDead15.SetValue(item.dead)
        if (item.status == "Ready"):
          self.bActivateP15.SetBackgroundColour(wx.Colour(0,128,0))
        elif (item.status == "Acted"):
          self.bActivateP15.SetBackgroundColour(wx.Colour(255,0,0))
        self.spHitPointsP15.SetValue(item.HP)
        self.cbPlayer15.SetValue(item.name)
        if (item.dead):
          self.OnKillPlayer15()
        if (item.planned_action == 'delay'):
          self.rbPlayer15d.SetValue(True)
        elif (item.planned_action == 'ready'):
          self.rbPlayer15r.SetValue(True)
        else:
          self.rbPlayer15.SetValue(True)

    return

  def OnKillPlayer1(self, event=None):
    """dim the player name and action radio buttons if the checkbox has been checked"""
    if (event):
      flag = not(event.GetEventObject().IsChecked())
    else:
      flag = False
    self.bActivateP1.SetBackgroundColour(wx.Colour(0,0,0))
    self.bActivateP1.Enable(flag)
    self.cbPlayer1.Enable(flag)
    self.rbPlayer1.Enable(flag)
    self.rbPlayer1r.Enable(flag)
    self.rbPlayer1d.Enable(flag)
    return
  def OnKillPlayer2(self, event=None):
    """dim the player name and action radio buttons if the checkbox has been checked"""
    if (event):
      flag = not(event.GetEventObject().IsChecked())
    else:
      flag = False

    self.bActivateP2.SetBackgroundColour(wx.Colour(0,0,0))
    self.bActivateP2.Enable(flag)
    self.cbPlayer2.Enable(flag)
    self.rbPlayer2.Enable(flag)
    self.rbPlayer2r.Enable(flag)
    self.rbPlayer2d.Enable(flag)
    return
  def OnKillPlayer3(self, event=None):
    """dim the player name and action radio buttons if the checkbox has been checked"""
    if (event):
      flag = not(event.GetEventObject().IsChecked())
    else:
      flag = False

    self.bActivateP3.SetBackgroundColour(wx.Colour(0,0,0))
    self.bActivateP3.Enable(flag)
    self.cbPlayer3.Enable(flag)
    self.rbPlayer3.Enable(flag)
    self.rbPlayer3r.Enable(flag)
    self.rbPlayer3d.Enable(flag)
    return
  def OnKillPlayer4(self, event=None):
    """dim the player name and action radio buttons if the checkbox has been checked"""
    if (event):
      flag = not(event.GetEventObject().IsChecked())
    else:
      flag = False

    self.bActivateP4.SetBackgroundColour(wx.Colour(0,0,0))
    self.bActivateP4.Enable(flag)
    self.cbPlayer4.Enable(flag)
    self.rbPlayer4.Enable(flag)
    self.rbPlayer4r.Enable(flag)
    self.rbPlayer4d.Enable(flag)
    return
  def OnKillPlayer5(self, event=None):
    """dim the player name and action radio buttons if the checkbox has been checked"""
    if (event):
      flag = not(event.GetEventObject().IsChecked())
    else:
      flag = False

    self.bActivateP5.SetBackgroundColour(wx.Colour(0,0,0))
    self.bActivateP5.Enable(flag)
    self.cbPlayer5.Enable(flag)
    self.rbPlayer5.Enable(flag)
    self.rbPlayer5r.Enable(flag)
    self.rbPlayer5d.Enable(flag)
    return
  def OnKillPlayer6(self, event=None):
    """dim the player name and action radio buttons if the checkbox has been checked"""
    if (event):
      flag = not(event.GetEventObject().IsChecked())
    else:
      flag = False

    self.bActivateP6.SetBackgroundColour(wx.Colour(0,0,0))
    self.bActivateP6.Enable(flag)
    self.cbPlayer6.Enable(flag)
    self.rbPlayer6.Enable(flag)
    self.rbPlayer6r.Enable(flag)
    self.rbPlayer6d.Enable(flag)
    return
  def OnKillPlayer7(self, event=None):
    """dim the player name and action radio buttons if the checkbox has been checked"""
    if (event):
      flag = not(event.GetEventObject().IsChecked())
    else:
      flag = False

    self.bActivateP7.SetBackgroundColour(wx.Colour(0,0,0))
    self.bActivateP7.Enable(flag)
    self.cbPlayer7.Enable(flag)
    self.rbPlayer7.Enable(flag)
    self.rbPlayer7r.Enable(flag)
    self.rbPlayer7d.Enable(flag)
    return
  def OnKillPlayer8(self, event=None):
    """dim the player name and action radio buttons if the checkbox has been checked"""
    if (event):
      flag = not(event.GetEventObject().IsChecked())
    else:
      flag = False

    self.bActivateP8.SetBackgroundColour(wx.Colour(0,0,0))
    self.bActivateP8.Enable(flag)
    self.cbPlayer8.Enable(flag)
    self.rbPlayer8.Enable(flag)
    self.rbPlayer8r.Enable(flag)
    self.rbPlayer8d.Enable(flag)
    return
  def OnKillPlayer9(self, event=None):
    """dim the player name and action radio buttons if the checkbox has been checked"""
    if (event):
      flag = not(event.GetEventObject().IsChecked())
    else:
      flag = False

    self.bActivateP9.SetBackgroundColour(wx.Colour(0,0,0))
    self.bActivateP9.Enable(flag)
    self.cbPlayer9.Enable(flag)
    self.rbPlayer9.Enable(flag)
    self.rbPlayer9r.Enable(flag)
    self.rbPlayer9d.Enable(flag)
    return
  def OnKillPlayer10(self, event=None):
    """dim the player name and action radio buttons if the checkbox has been checked"""
    if (event):
      flag = not(event.GetEventObject().IsChecked())
    else:
      flag = False

    self.bActivateP10.SetBackgroundColour(wx.Colour(0,0,0))
    self.bActivateP10.Enable(flag)
    self.cbPlayer10.Enable(flag)
    self.rbPlayer10.Enable(flag)
    self.rbPlayer10r.Enable(flag)
    self.rbPlayer10d.Enable(flag)
    return
  def OnKillPlayer11(self, event=None):
    """dim the player name and action radio buttons if the checkbox has been checked"""
    if (event):
      flag = not(event.GetEventObject().IsChecked())
    else:
      flag = False

    self.bActivateP11.SetBackgroundColour(wx.Colour(0,0,0))
    self.bActivateP11.Enable(flag)
    self.cbPlayer11.Enable(flag)
    self.rbPlayer11.Enable(flag)
    self.rbPlayer11r.Enable(flag)
    self.rbPlayer11d.Enable(flag)
    return
  def OnKillPlayer12(self, event=None):
    """dim the player name and action radio buttons if the checkbox has been checked"""
    if (event):
      flag = not(event.GetEventObject().IsChecked())
    else:
      flag = False

    self.bActivateP12.SetBackgroundColour(wx.Colour(0,0,0))
    self.bActivateP12.Enable(flag)
    self.cbPlayer12.Enable(flag)
    self.rbPlayer12.Enable(flag)
    self.rbPlayer12r.Enable(flag)
    self.rbPlayer12d.Enable(flag)
    return
  def OnKillPlayer13(self, event=None):
    """dim the player name and action radio buttons if the checkbox has been checked"""
    if (event):
      flag = not(event.GetEventObject().IsChecked())
    else:
      flag = False

    self.bActivateP13.SetBackgroundColour(wx.Colour(0,0,0))
    self.bActivateP13.Enable(flag)
    self.cbPlayer13.Enable(flag)
    self.rbPlayer13.Enable(flag)
    self.rbPlayer13r.Enable(flag)
    self.rbPlayer13d.Enable(flag)
    return
  def OnKillPlayer14(self, event=None):
    """dim the player name and action radio buttons if the checkbox has been checked"""
    if (event):
      flag = not(event.GetEventObject().IsChecked())
    else:
      flag = False

    self.bActivateP14.SetBackgroundColour(wx.Colour(0,0,0))
    self.bActivateP14.Enable(flag)
    self.cbPlayer14.Enable(flag)
    self.rbPlayer14.Enable(flag)
    self.rbPlayer14r.Enable(flag)
    self.rbPlayer14d.Enable(flag)
    return

  def OnKillPlayer15(self, event=None):
    """dim the player name and action radio buttons if the checkbox has been checked"""
    if (event):
      flag = not(event.GetEventObject().IsChecked())
    else:
      flag = False

    self.bActivateP15.SetBackgroundColour(wx.Colour(0,0,0))
    self.bActivateP15.Enable(flag)
    self.cbPlayer15.Enable(flag)
    self.rbPlayer15.Enable(flag)
    self.rbPlayer15r.Enable(flag)
    self.rbPlayer15d.Enable(flag)
    return

  def OnActivatePlayer(self, event):
    """Change the background color of the button to red.  All of the activation buttons point to this function."""
    color = event.GetEventObject().GetBackgroundColour()
    if (color == wx.Colour(0,128,0)): #if the current button is green, change to red
      color = wx.Colour(255,0,0)
    else:  #any other color, change to green
      color = wx.Colour(0,128,0)
    event.GetEventObject().SetBackgroundColour(color)
    return

  def OnAddNames(self, event):
    """Add a name to the available drop-down list of players"""
    dlg = TextEntryDialog(self, self.names_list)
    result = dlg.ShowModal()
    if (result):
      text = dlg.txNames.GetValue()
      self.names_list = text.split('\n')
      self.SetComboBoxNames(self.names_list)
    dlg.Destroy()
    return

  def SetComboBoxNames(self, PlayerDataList):
    textlist = []
    for item in PlayerDataList:
      textlist.append(item)

    s1 = self.cbPlayer1.GetValue()
    s2 = self.cbPlayer2.GetValue()
    s3 = self.cbPlayer3.GetValue()
    s4 = self.cbPlayer4.GetValue()
    s5 = self.cbPlayer5.GetValue()
    s6 = self.cbPlayer6.GetValue()
    s7 = self.cbPlayer7.GetValue()
    s8 = self.cbPlayer8.GetValue()
    s9 = self.cbPlayer9.GetValue()
    s10 = self.cbPlayer10.GetValue()
    s11 = self.cbPlayer11.GetValue()
    s12 = self.cbPlayer12.GetValue()
    s13 = self.cbPlayer13.GetValue()
    s14 = self.cbPlayer14.GetValue()
    s15 = self.cbPlayer15.GetValue()

    self.cbPlayer1.Clear()
    self.cbPlayer2.Clear()
    self.cbPlayer3.Clear()
    self.cbPlayer4.Clear()
    self.cbPlayer5.Clear()
    self.cbPlayer6.Clear()
    self.cbPlayer7.Clear()
    self.cbPlayer8.Clear()
    self.cbPlayer9.Clear()
    self.cbPlayer10.Clear()
    self.cbPlayer11.Clear()
    self.cbPlayer12.Clear()
    self.cbPlayer13.Clear()
    self.cbPlayer14.Clear()
    self.cbPlayer15.Clear()

    self.cbPlayer1.AppendItems(textlist)
    self.cbPlayer2.AppendItems(textlist)
    self.cbPlayer3.AppendItems(textlist)
    self.cbPlayer4.AppendItems(textlist)
    self.cbPlayer5.AppendItems(textlist)
    self.cbPlayer6.AppendItems(textlist)
    self.cbPlayer7.AppendItems(textlist)
    self.cbPlayer8.AppendItems(textlist)
    self.cbPlayer9.AppendItems(textlist)
    self.cbPlayer10.AppendItems(textlist)
    self.cbPlayer11.AppendItems(textlist)
    self.cbPlayer12.AppendItems(textlist)
    self.cbPlayer13.AppendItems(textlist)
    self.cbPlayer14.AppendItems(textlist)
    self.cbPlayer15.AppendItems(textlist)
    if s1 in textlist:
      self.cbPlayer1.SetValue(s1)
    if s2 in textlist:
      self.cbPlayer2.SetValue(s2)
    if s3 in textlist:
      self.cbPlayer3.SetValue(s3)
    if s4 in textlist:
      self.cbPlayer4.SetValue(s4)
    if s5 in textlist:
      self.cbPlayer5.SetValue(s5)
    if s6 in textlist:
      self.cbPlayer6.SetValue(s6)
    if s7 in textlist:
      self.cbPlayer7.SetValue(s7)
    if s8 in textlist:
      self.cbPlayer8.SetValue(s8)
    if s9 in textlist:
      self.cbPlayer9.SetValue(s9)
    if s10 in textlist:
      self.cbPlayer10.SetValue(s10)
    if s11 in textlist:
      self.cbPlayer11.SetValue(s11)
    if s12 in textlist:
      self.cbPlayer12.SetValue(s12)
    if s13 in textlist:
      self.cbPlayer13.SetValue(s13)
    if s14 in textlist:
      self.cbPlayer14.SetValue(s14)
    if s15 in textlist:
      self.cbPlayer15.SetValue(s15)
    return

  def OnResetRound(self, event):
    self.OnNextRound()
    self.current_round = 1
    self.stCurrentRound.SetLabel(str(self.current_round))
    return

  def OnResetAllValues(self, event):
    """Reset the text fields and the round counter"""
    #Clear all of the player name fields
    self.cbPlayer1.Clear()
    self.cbPlayer2.Clear()
    self.cbPlayer3.Clear()
    self.cbPlayer4.Clear()
    self.cbPlayer5.Clear()
    self.cbPlayer6.Clear()
    self.cbPlayer7.Clear()
    self.cbPlayer8.Clear()
    self.cbPlayer9.Clear()
    self.cbPlayer10.Clear()
    self.cbPlayer11.Clear()
    self.cbPlayer12.Clear()
    self.cbPlayer13.Clear()
    self.cbPlayer14.Clear()
    self.cbPlayer15.Clear()

    #Reset the dead checkboxes
    self.cbPlayerDead1.SetValue(False)
    self.cbPlayerDead2.SetValue(False)
    self.cbPlayerDead3.SetValue(False)
    self.cbPlayerDead4.SetValue(False)
    self.cbPlayerDead5.SetValue(False)
    self.cbPlayerDead6.SetValue(False)
    self.cbPlayerDead7.SetValue(False)
    self.cbPlayerDead8.SetValue(False)
    self.cbPlayerDead9.SetValue(False)
    self.cbPlayerDead10.SetValue(False)
    self.cbPlayerDead11.SetValue(False)
    self.cbPlayerDead12.SetValue(False)
    self.cbPlayerDead13.SetValue(False)
    self.cbPlayerDead14.SetValue(False)
    self.cbPlayerDead15.SetValue(False)
    self.OnNextRound()
    
    startID = PyMapperDialogs.p1Init
    endID = PyMapperDialogs.p15Init+1
    for item in range(startID, endID, 8):
      widget = self.FindWindowById(item)
      widget.SetValue("0")

    self.current_round = 1
    self.stCurrentRound.SetLabel(str(self.current_round))
    return

  def OnNextRound(self, event=None):
    """Reset all of the action buttons, and the radio groups"""
    self.current_round += 1
    self.stCurrentRound.SetLabel(str(self.current_round))

    if (not self.cbPlayerDead1.IsChecked()):
      self.bActivateP1.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
    self.rbPlayer1.SetValue( True )
    if (not self.cbPlayerDead2.IsChecked()):
      self.bActivateP2.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
    self.rbPlayer2.SetValue( True )
    if (not self.cbPlayerDead3.IsChecked()):
      self.bActivateP3.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
    self.rbPlayer3.SetValue( True )
    if (not self.cbPlayerDead4.IsChecked()):
      self.bActivateP4.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
    self.rbPlayer4.SetValue( True )
    if (not self.cbPlayerDead5.IsChecked()):
      self.bActivateP5.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
    self.rbPlayer5.SetValue( True )
    if (not self.cbPlayerDead6.IsChecked()):
      self.bActivateP6.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
    self.rbPlayer6.SetValue( True )
    if (not self.cbPlayerDead7.IsChecked()):
      self.bActivateP7.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
    self.rbPlayer7.SetValue( True )
    if (not self.cbPlayerDead8.IsChecked()):
      self.bActivateP8.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
    self.rbPlayer8.SetValue( True )
    if (not self.cbPlayerDead9.IsChecked()):
      self.bActivateP9.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
    self.rbPlayer9.SetValue( True )
    if (not self.cbPlayerDead10.IsChecked()):
      self.bActivateP10.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
    self.rbPlayer10.SetValue( True )
    if (not self.cbPlayerDead11.IsChecked()):
      self.bActivateP11.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
    self.rbPlayer11.SetValue( True )
    if (not self.cbPlayerDead12.IsChecked()):
      self.bActivateP12.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
    self.rbPlayer12.SetValue( True )
    if (not self.cbPlayerDead13.IsChecked()):
      self.bActivateP13.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
    self.rbPlayer13.SetValue( True )
    if (not self.cbPlayerDead14.IsChecked()):
      self.bActivateP14.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
    self.rbPlayer14.SetValue( True )
    if (not self.cbPlayerDead15.IsChecked()):
      self.bActivateP15.SetBackgroundColour( wx.Colour( 0, 128, 0 ) )
    self.rbPlayer15.SetValue( True )
    return

  def OnClose(self, event):
    if (self.cbSaveData.IsChecked()):
      self.SavePlayerData()
    self.Show(False)
    return

  def OnHelp(self, event):
    text = "This dialog helps in keeping track of combat stats.\n\nThe first checkbox will determine if the player is deceased if it is checked.\n\nThe next button (defaults to green) shows the current status of the player.  Green is ready to act, Red indicates that an action has been taken, and if it shows black, dead.\n\nHit points are tracked in the next dialog, along with the name of the PC or NPC. Initiative values are entered, and the status is recorded with the radio buttons.\n\nMultiple names can be added with the Add Names... button, and once initiative values have been entered, the Sort Initiative button will order the combat.\n\nClick on the Next Round button to advance the round counter at the top of the dialog."
    helpDlg = HelpDialog(self, text)
    helpDlg.ShowModal()
    return

class ProgramFoundationDialog(PyMapperDialogs.ProgramFoundationDialogBase):
  def __init__(self, parent):
    olddir = os.getcwd()
    os.chdir(gv.root_directory)  #this is necessary so that bitmap paths are read by the dialog code correctly
    PyMapperDialogs.ProgramFoundationDialogBase.__init__(self, parent)
    os.chdir(olddir)
    return

  def OnClose(self, event):
    self.EndModal(True)
    return

class SecondaryMapDialog(PyMapperDialogs.SecondaryMapDialogBase):
  """Displays a copy of the map window on a secondary dialog, with the option to draw 
  on a projector or secondary monitor"""
  def __init__(self, parent):
    olddir = os.getcwd()
    os.chdir(gv.root_directory)
    PyMapperDialogs.SecondaryMapDialogBase.__init__(self, parent)
    os.chdir(olddir)
    self.MapBitmap = None
    self.FogBitmap = None
    self.scale = 1.0
    
    self.pnSecondaryMap.EnableScrolling(True, True)
    self.pnSecondaryMap.SetScrollbars(20,20,50,50)
    self.pnSecondaryMap.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
    self.UpdateImage()
    app.frame.menubar.Enable(PyMapperDialogs.mViewUpdateToFTP, True)
    app.frame.menubar.Enable(PyMapperDialogs.mViewUpdateFog, True)
    return
  
  def UpdateFTP(self,event=None):
    self.UpdateImage()
    if (not gv.FTP_Password) or (not gv.FTP_Filename) or (not gv.FTP_Username) or (not gv.FTP_Server):
      #must have valid credentials to log in to remote site.
      dlg = FTP_OptionsDialogCore(self)
      if (not dlg.ShowModal()):  #could not get information from the user
        return
      
    try:
      session = ftplib.FTP(gv.FTP_Server, gv.FTP_Username, gv.FTP_Password)
      self.MapBitmap.SaveFile(gv.FTP_Filename, wx.BITMAP_TYPE_PNG)
      transferfile = open(gv.FTP_Filename, 'rb')
      command = 'STOR '+ gv.FTP_Filename
      session.storbinary(command, transferfile)
      transferfile.close()
      session.quit()
      wx.MessageBox("Image Updated", "FTP Transfer")
    except:
      wx.MessageBox("Could not update to ftp server.", "FTP Error")
      logging.error("Could not update to ftp server.")
    return

  def UpdatePlayerView(self, event):
    self.UpdateImage()
    return
  
  def UpdateImage(self):
    #get updated images
    app.DrawMapWindow()
    
    mapImage = wx.ImageFromBitmap(app.MapBuffer)
    
    xsize = mapImage.GetWidth() * self.scale
    ysize = mapImage.GetHeight() * self.scale
    
    self.MapBitmap = wx.BitmapFromImage(mapImage.Scale(xsize, ysize, wx.IMAGE_QUALITY_NORMAL))
    
    xsize = app.MapFogImage.GetWidth() * self.scale
    ysize = app.MapFogImage.GetHeight() * self.scale
    fogImage = app.MapFogImage.Scale(xsize, ysize, wx.IMAGE_QUALITY_NORMAL)
    
    self.FogMask = wx.Mask(wx.BitmapFromImage(fogImage), gv.MapFogColor)
    self.MapBitmap.SetMask(self.FogMask)
    bitmapSize = self.MapBitmap.GetSize()
    panelSize = self.pnSecondaryMap.GetSize()
    width = max(panelSize.GetWidth(), bitmapSize.GetWidth())
    height = max(panelSize.GetHeight(), bitmapSize.GetHeight())
    self.SecondaryMapBuffer = wx.Bitmap(width, height)

    self.pnSecondaryMap.SetVirtualSize(wx.Size(width, height))
    self.SecondaryMapDC = wx.BufferedDC(None, self.SecondaryMapBuffer, wx.BUFFER_VIRTUAL_AREA)
    self.pnSecondaryMap.SetBackgroundColour(gv.SecondaryPanelBackgroundColor)
    self.pnSecondaryMap.SetScrollRate(gv.ScrollIncrement, gv.ScrollIncrement)

    self.SecondaryMapDC.DrawBitmap(self.MapBitmap,0,0,True)
    self.SecondaryMapDC.SelectObject(wx.NullBitmap)
    self.pnSecondaryMap.Refresh()
    return

  def OnPaint(self, event):
    dc = wx.BufferedPaintDC(self.pnSecondaryMap, self.SecondaryMapBuffer, wx.BUFFER_VIRTUAL_AREA)
    event.Skip()
    return

  def ResetZoom(self, event):
    self.scale = 1.0
    self.UpdateImage()
    return
    
  def OnZoomIn(self, event):
    self.scale += 0.2
    if (self.scale >= 3.0):
      self.bZoomIn.Enable(False)
    else:
      self.bZoomIn.Enable(True)
      self.bZoomOut.Enable(True)
    self.UpdateImage()
    return

  def OnZoomOut(self, event):
    self.scale -= 0.2
    if (self.scale <= 0.2):
      self.bZoomOut.Enable(False)
      self.scale = 0.2
    else:
      self.bZoomIn.Enable(True)
      self.bZoomOut.Enable(True)
    self.UpdateImage()
    return

  def ResizeBitmap(self, bitmap, scale):
    """
    bitmap is taken directly from the main display.  This function will 
    change the size to match the display as needed.

    """
    bitmapsize = bitmap.GetSize()
    panelsize = self.pnSecondaryMap.GetSize()
    CurrentImage = None

    pilImage = wx.ImageFromBitmap(bitmap)
    if (not pilImage.IsOk()):
      logging.critical("SecondaryMapDialog::ResizeBitmap: Could not create bitmap")
      pilImage = app.ImageNotFound

    width = pilImage.GetWidth()
    height = pilImage.GetHeight()
    aspect_image = float(width)/float(height)
    aspect_panel = float(panelsize.width)/float(panelsize.height)

    if (aspect_image < 1.0):
      #height > width
      if (height > panelsize.height):
        height = int(panelsize.height)# * 0.85)
        width = int(aspect_image * height)
    elif (aspect_image == 1.0):
      #height = width
      if ((height > panelsize.height) or (width > panelsize.width)):
        width = int(panelsize.width)# * 0.85)
        height = int(panelsize.height)# * 0.85)
    elif (aspect_image > 1.0):
      # width > height
      if (width > panelsize.width):
        width = int(panelsize.width)# * 0.85)
        height = int((width / aspect_image))
    width *= scale
    height *= scale
    pilImage = pilImage.Scale(width, height, wx.IMAGE_QUALITY_HIGH)

    return wx.BitmapFromImage(pilImage) 

  def OnSaveImage(self, event):
    temp_dir = os.getcwd()
    try:
      os.chdir(gv.image_directory)
    except OSError:
      logging.error("SecondaryMapDialog:OnSaveImage could not change folder")
      text = "Error in OnPrintImage: Could not change to ", gv.image_directory
      wx.MessageBox(message=text, caption="Error", style=wx.ICON_EXCLAMATION)
      return False
    dlg = wx.FileDialog(self, message="Save image as...",
                        defaultDir=os.getcwd(), defaultFile="",
                        wildcard=export_wildcard, style=wx.SAVE | wx.FD_OVERWRITE_PROMPT)
    if (dlg.ShowModal() == wx.ID_OK):
      if (dlg.GetFilterIndex() == 0):
        #jpg image
        try:
          self.SecondaryMapBuffer.SaveFile(dlg.GetPath(),wx.BITMAP_TYPE_JPEG)
        except:
          logging.critical("SecondaryMapDialog:OnSaveImage: Could not allocate memory for image save")
      elif (dlg.GetFilterIndex() == 1):
        #png image
        try:
          self.SecondaryMapBuffer.SaveFile(dlg.GetPath(),wx.BITMAP_TYPE_PNG)
        except:
          logging.critical("SecondaryMapDialog:OnSaveImage: Could not allocate memory for image save")
    dlg.Destroy()
    os.chdir(temp_dir)
    return

  
  def OnClose(self, event):
    self.Show(False)
    app.frame.menubar.Enable(PyMapperDialogs.mViewUpdateToFTP, False)
    app.frame.menubar.Enable(PyMapperDialogs.mViewUpdateFog, False)
    gv.SecondaryScreen = None
    if (fog.FogToolsDialog):
      fog.FogToolsDialog.bUpdateFog.Enable(False)
      fog.FogToolsDialog.bUpdateFogOnline.Enable(False)
    return

class IsometricMapDialog(PyMapperDialogs.IsometricMapDialogBase):
  """Displays an isometric projection copy of the map window on a modeless dialog"""
  def __init__(self, parent):
    olddir = os.getcwd()
    os.chdir(gv.root_directory)
    PyMapperDialogs.IsometricMapDialogBase.__init__(self, parent)
    os.chdir(olddir)
    self.MapBitmap = None
    self.FogBitmap = None
    self.scale = 1.0
    
    self.pnIsometricMap.EnableScrolling(True, True)
    self.pnIsometricMap.SetScrollbars(20,20,50,50)
    self.pnIsometricMap.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
    self.UpdateIsometricView()
    return

  def UpdateIsometricView(self, event=None):
    #get updated images by updating the app.MapBuffer
    gv.DrawMapDiagonals = True
    app.DrawMapWindow()
    
    #image = wx.Image()
    bufferImage = wx.ImageFromBitmap(app.MapBuffer)
    xdim = bufferImage.GetWidth()
    ydim = bufferImage.GetHeight()
    mapX = app.MapStruct.columns * gv.MapZoomFactor
    mapY = app.MapStruct.rows * gv.MapZoomFactor
    imageX = min(xdim, mapX)
    imageY = min(ydim, mapY)
    subImageRect = wx.Rect(0,0,imageX, imageY)
    image = bufferImage.GetSubImage(subImageRect)
    centerPoint = wx.Point(int(imageX/2), int(imageY/2))
    rotationAngle = math.pi/4  #angle is in radians
    
    quality = wx.IMAGE_QUALITY_HIGH
    RotateImage = image.Rotate(rotationAngle, centerPoint)
    xdim = RotateImage.GetWidth()
    ydim = RotateImage.GetHeight()*0.577 #isometric compression shrinks by 57.7%
    IsometricImage = RotateImage.Rescale(xdim,ydim,quality)
    
    xsize = IsometricImage.GetWidth() * self.scale
    ysize = IsometricImage.GetHeight() * self.scale
    
    self.MapBitmap = wx.BitmapFromImage(IsometricImage.Scale(xsize, ysize, wx.IMAGE_QUALITY_HIGH))
    
    bitmapSize = self.MapBitmap.GetSize()
    panelSize = self.pnIsometricMap.GetSize()
    width = max(panelSize.GetWidth(), bitmapSize.GetWidth())
    height = max(panelSize.GetHeight(), bitmapSize.GetHeight())
    self.IsometricBuffer = wx.Bitmap(width, height)

    self.pnIsometricMap.SetVirtualSize(wx.Size(width, height))
    self.IsometricMapDC = wx.BufferedDC(None, self.IsometricBuffer, wx.BUFFER_VIRTUAL_AREA)
    self.pnIsometricMap.SetBackgroundColour(gv.SecondaryPanelBackgroundColor)
    self.pnIsometricMap.SetScrollRate(gv.ScrollIncrement, gv.ScrollIncrement)

    self.IsometricMapDC.DrawBitmap(self.MapBitmap,0,0,True)
    self.IsometricMapDC.SelectObject(wx.NullBitmap)
    self.pnIsometricMap.Refresh()
    gv.DrawMapDiagonals = False
    app.DrawMapWindow()
    return

  def OnPaint(self, event):
    dc = wx.BufferedPaintDC(self.pnIsometricMap, self.IsometricBuffer, wx.BUFFER_VIRTUAL_AREA)
    event.Skip()
    return

  def ResetZoom(self, event):
    self.scale = 1.0
    self.UpdateIsometricView()
    return
    
  def OnZoomIn(self, event):
    self.scale += 0.2
    if (self.scale >= 3.0):
      self.bZoomIn.Enable(False)
    else:
      self.bZoomIn.Enable(True)
      self.bZoomOut.Enable(True)
    self.UpdateIsometricView()
    return

  def OnZoomOut(self, event):
    self.scale -= 0.2
    if (self.scale <= 0.2):
      self.bZoomOut.Enable(False)
      self.scale = 0.2
    else:
      self.bZoomIn.Enable(True)
      self.bZoomOut.Enable(True)
    self.UpdateIsometricView()
    return

  def ResizeBitmap(self, bitmap, scale):
    """
    bitmap is taken directly from the main display.  This function will 
    change the size to match the display as needed.

    """
    bitmapsize = bitmap.GetSize()
    panelsize = self.pnIsometricMap.GetSize()
    CurrentImage = None

    pilImage = wx.ImageFromBitmap(bitmap)
    if (not pilImage.IsOk()):
      logging.critical("Could not create bitmap")
      pilImage = app.ImageNotFound

    width = pilImage.GetWidth()
    height = pilImage.GetHeight()
    aspect_image = float(width)/float(height)
    aspect_panel = float(panelsize.width)/float(panelsize.height)

    if (aspect_image < 1.0):
      #height > width
      if (height > panelsize.height):
        height = int(panelsize.height)# * 0.85)
        width = int(aspect_image * height)
    elif (aspect_image == 1.0):
      #height = width
      if ((height > panelsize.height) or (width > panelsize.width)):
        width = int(panelsize.width)# * 0.85)
        height = int(panelsize.height)# * 0.85)
    elif (aspect_image > 1.0):
      # width > height
      if (width > panelsize.width):
        width = int(panelsize.width)# * 0.85)
        height = int((width / aspect_image))
    width *= scale
    height *= scale
    pilImage = pilImage.Scale(width, height, wx.IMAGE_QUALITY_HIGH)

    return wx.BitmapFromImage(pilImage) 

  def OnSaveImage(self, event):
    temp_dir = os.getcwd()
    try:
      os.chdir(gv.image_directory)
    except OSError:
      logging.error("Could not change folder")
      text = "Error in SaveImage: Could not change to ", gv.image_directory
      wx.MessageBox(message=text, caption="Error", style=wx.ICON_EXCLAMATION)
      return False
    dlg = wx.FileDialog(self, message="Save image as...",
                        defaultDir=os.getcwd(), defaultFile="",
                        wildcard=export_wildcard, style=wx.SAVE | wx.FD_OVERWRITE_PROMPT)
    if (dlg.ShowModal() == wx.ID_OK):
      if (dlg.GetFilterIndex() == 0):
        #jpg image
        try:
          self.IsometricBuffer.SaveFile(dlg.GetPath(),wx.BITMAP_TYPE_JPEG)
        except:
          logging.critical("Could not allocate memory for image save")
      elif (dlg.GetFilterIndex() == 1):
        #png image
        try:
          self.IsometricBuffer.SaveFile(dlg.GetPath(),wx.BITMAP_TYPE_PNG)
        except:
          logging.critical("Could not allocate memory for image save")
    dlg.Destroy()
    os.chdir(temp_dir)
    return

  
  def OnClose(self, event):
    self.Show(False)
    gv.SecondaryScreen = None
    gv.DrawMapDiagonals = False
    return
  
#---------End IsometricMapDialog -----------------------

class DrawToolsDialog(PyMapperDialogs.DrawingToolsDialogBase):
  def __init__(self, parent):
    olddir = os.getcwd()
    os.chdir(gv.root_directory)
    PyMapperDialogs.DrawingToolsDialogBase.__init__(self, parent)
    os.chdir(olddir)
    self.current_tool = None
    self.oldtool = None
    self.bChooseFillColor.SetColour(gv.DrawFillColor)
    self.slFillTransparency.SetValue(gv.DrawFillColor.alpha)
    self.bChooseOutlineColor.SetColour(gv.DrawOutlineColor)
    self.PenStyle = gv.DrawingToolPen.GetStyle()
    self.BrushStyle = gv.DrawingToolBrush.GetStyle()
    return

  def OnChangeTransparency(self, event):
    color = self.bChooseFillColor.GetColour()
    alpha = self.slFillTransparency.GetValue()
    setcolor = wx.Colour(color.Red(), color.Green(), color.Blue(), alpha)
    gv.DrawingToolBrush = wx.Brush(setcolor)
    self.UpdateLineSample()
    return

  def OnResetLineStyle(self, event):
    self.PenStyle = wx.SOLID
    self.stLineStyle.SetLabel("Line Style: Solid")
    self.UpdateLineSample()
    return

  def UpdateLineSample(self):
    panelsize = self.pnLineStyleExample.GetSize()
    gv.DrawingToolPen = wx.Pen(self.bChooseOutlineColor.GetColour(),
                               self.spLineWidth.GetValue(), self.PenStyle)
    brushColor = self.bChooseFillColor.GetColour()
    gv.DrawingToolBrush = wx.Brush((brushColor.red, brushColor.green, brushColor.blue,
                                    self.slFillTransparency.GetValue()), self.BrushStyle)
    dc = wx.ClientDC(self.pnLineStyleExample)
    gc = wx.GraphicsContext.Create(dc)
    penColor = self.bChooseOutlineColor.GetColour()
    penWidth = self.spLineWidth.GetValue()
    gc.SetBrush(wx.WHITE_BRUSH)
    pen = wx.BLACK_PEN
    pen.SetWidth(2)
    gc.SetPen(pen)
    gc.DrawRectangle(0,0,panelsize.x, panelsize.y)
    interval = panelsize.x/10
    for x in range(1,10):
      gc.StrokeLine(x*interval,0, x*interval, panelsize.y)

    gc.SetPen(gv.DrawingToolPen)
    gc.SetBrush(gv.DrawingToolBrush)
    gc.DrawRectangle(0,0,panelsize.x, panelsize.y)
    gc.StrokeLine(0, (panelsize.y/2), panelsize.x, (panelsize.y/2))
    for item in app.DrawingList:
      if (item.selected == True):

        item.pen = gv.DrawingToolPen
        item.brush = gv.DrawingToolBrush
        app.DrawMapWindow()
        break
    return

  def OnChangeLineWidth(self, event):
    self.UpdateLineSample()
    return

  def OnChangeLineStyleUp(self, event):
    if (self.PenStyle == wx.SOLID):
      self.PenStyle = wx.VERTICAL_HATCH
      self.stLineStyle.SetLabel("Line Style: Vertical Hatch")
    elif (self.PenStyle == wx.TRANSPARENT):
      self.PenStyle = wx.SOLID
      self.stLineStyle.SetLabel("Line Style: Solid")
    elif (self.PenStyle == wx.DOT):
      self.PenStyle = wx.TRANSPARENT
      self.stLineStyle.SetLabel("Line Style: None")
    elif (self.PenStyle == wx.LONG_DASH):
      self.PenStyle = wx.DOT
      self.stLineStyle.SetLabel("Line Style: Dots")
    elif (self.PenStyle == wx.SHORT_DASH):
      self.PenStyle = wx.LONG_DASH
      self.stLineStyle.SetLabel("Line Style: Long Dash")
    elif (self.PenStyle == wx.DOT_DASH):
      self.PenStyle = wx.SHORT_DASH
      self.stLineStyle.SetLabel("Line Style: Short Dash")
    elif (self.PenStyle == wx.BDIAGONAL_HATCH):
      self.PenStyle = wx.DOT_DASH
      self.stLineStyle.SetLabel("Line Style: Dot/Dash")
    elif (self.PenStyle == wx.CROSSDIAG_HATCH):
      self.PenStyle = wx.BDIAGONAL_HATCH
      self.stLineStyle.SetLabel("Line Style: Backward Hatch")
    elif (self.PenStyle == wx.FDIAGONAL_HATCH):
      self.PenStyle = wx.CROSSDIAG_HATCH
      self.stLineStyle.SetLabel("Line Style: Diagonal Hatch")
    elif (self.PenStyle == wx.CROSS_HATCH):
      self.PenStyle = wx.FDIAGONAL_HATCH
      self.stLineStyle.SetLabel("Line Style: Forward Hatch")
    elif (self.PenStyle == wx.HORIZONTAL_HATCH):
      self.PenStyle = wx.CROSS_HATCH
      self.stLineStyle.SetLabel("Line Style: Cross Hatch")
    elif (self.PenStyle == wx.VERTICAL_HATCH):
      self.PenStyle = wx.HORIZONTAL_HATCH
      self.stLineStyle.SetLabel("Line Style: Horiz. Hatch")
    self.UpdateLineSample()
    return

  def OnChangeLineStyleDown(self, event):
    if (self.PenStyle == wx.SOLID):
      self.PenStyle = wx.TRANSPARENT
      self.stLineStyle.SetLabel("Line Style: None")
    elif (self.PenStyle == wx.TRANSPARENT):
      self.PenStyle = wx.DOT
      self.stLineStyle.SetLabel("Line Style: Dots")
    elif (self.PenStyle == wx.DOT):
      self.PenStyle = wx.LONG_DASH
      self.stLineStyle.SetLabel("Line Style: Long Dash")
    elif (self.PenStyle == wx.LONG_DASH):
      self.PenStyle = wx.SHORT_DASH
      self.stLineStyle.SetLabel("Line Style: Short Dash")
    elif (self.PenStyle == wx.SHORT_DASH):
      self.PenStyle = wx.DOT_DASH
      self.stLineStyle.SetLabel("Line Style: Dot/Dash")
    elif (self.PenStyle == wx.DOT_DASH):
      self.PenStyle = wx.BDIAGONAL_HATCH
      self.stLineStyle.SetLabel("Line Style: Backwark Hatch")
    elif (self.PenStyle == wx.BDIAGONAL_HATCH):
      self.PenStyle = wx.CROSSDIAG_HATCH
      self.stLineStyle.SetLabel("Line Style: Diagonal Hatch")
    elif (self.PenStyle == wx.CROSSDIAG_HATCH):
      self.PenStyle = wx.FDIAGONAL_HATCH
      self.stLineStyle.SetLabel("Line Style: Forward Hatch")
    elif (self.PenStyle == wx.FDIAGONAL_HATCH):
      self.PenStyle = wx.CROSS_HATCH
      self.stLineStyle.SetLabel("Line Style: Cross Hatch")
    elif (self.PenStyle == wx.CROSS_HATCH):
      self.PenStyle = wx.HORIZONTAL_HATCH
      self.stLineStyle.SetLabel("Line Style: Horiz. Hatch")
    elif (self.PenStyle == wx.HORIZONTAL_HATCH):
      self.PenStyle = wx.VERTICAL_HATCH
      self.stLineStyle.SetLabel("Line Style: Vertical Hatch")
    elif (self.PenStyle == wx.VERTICAL_HATCH):
      self.PenStyle = wx.SOLID
      self.stLineStyle.SetLabel("Line Style: Solid")
    self.UpdateLineSample()
    return

  def OnPaint(self, event):
    self.UpdateLineSample()
    event.Skip()
    return

  def OnShowHandles(self, event=None):
    if (gv.DrawHandles):
      gv.DrawHandles = False
      self.bShowHandles.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_show_no_handles.png'), wx.BITMAP_TYPE_PNG))
    else:
      gv.DrawHandles = True
      self.bShowHandles.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_show_handles.png'), wx.BITMAP_TYPE_PNG))
    app.DrawMapWindow()
    app.frame.toolbar.ToggleTool(PyMapperDialogs.tShowDrawingHandles, gv.DrawHandles)
    return

  def ChangeToolBitmaps(self, newtool):
    if (self.oldtool == 'Select'):
      self.bSelectItem.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_select.png'), wx.BITMAP_TYPE_PNG))
    elif (self.oldtool == 'Delete'):
      self.bDeleteItem.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_DeleteIcon.png'), wx.BITMAP_TYPE_PNG))
    elif (self.oldtool == 'FillCircle'):
      self.bDrawFilledCircle.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_filled_circle.png'), wx.BITMAP_TYPE_PNG))
    elif (self.oldtool == 'OutlineCircle'):
      self.bDrawOutlinedCircle.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_open_circle.png'), wx.BITMAP_TYPE_PNG))
    elif (self.oldtool == 'FillRect'):
      self.bDrawFilledRectangle.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_filled_rectangle.png'), wx.BITMAP_TYPE_PNG))
    elif (self.oldtool == 'OutlineRect'):
      self.bDrawOutlinedRectangle.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_open_rectangle.png'), wx.BITMAP_TYPE_PNG))
    elif (self.oldtool == 'Line'):
      self.bDrawLine.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_line.png'), wx.BITMAP_TYPE_PNG))
    elif (self.oldtool == 'Multiline'):
      self.bDrawMultiline.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_line_segments.png'), wx.BITMAP_TYPE_PNG))
    elif (self.oldtool == 'Freehand'):
      self.bDrawFreehand.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_freehand.png'), wx.BITMAP_TYPE_PNG))
    elif (self.oldtool == 'Image'):
      self.bImportCustomImage.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_insert_custom.png'), wx.BITMAP_TYPE_PNG))
    elif (self.oldtool == 'GetProperty'):
      self.bGetProperties.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_get_properties.png'), wx.BITMAP_TYPE_PNG))
    elif (self.oldtool == 'ChangeProperty'):
      self.bChangeProperties.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_change_properties.png'), wx.BITMAP_TYPE_PNG))
    elif (self.oldtool == 'Point'):
      self.bDrawPoint.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_point.png'), wx.BITMAP_TYPE_PNG))

    if (newtool == 'Select'):
      self.bSelectItem.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_select_selected.png'), wx.BITMAP_TYPE_PNG))
      self.bShowHandles.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_show_handles.png'), wx.BITMAP_TYPE_PNG))
      gv.DrawHandles = True
    elif (newtool == 'Point'):
      self.bDrawPoint.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_point_selected.png'), wx.BITMAP_TYPE_PNG))
    elif (newtool == 'Delete'):
      self.bDeleteItem.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_DeleteIcon_selected.png'), wx.BITMAP_TYPE_PNG))
    elif (newtool == 'FillCircle'):
      self.bDrawFilledCircle.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_filled_circle_selected.png'), wx.BITMAP_TYPE_PNG))
    elif (newtool == 'OutlineCircle'):
      self.bDrawOutlinedCircle.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_open_circle_selected.png'), wx.BITMAP_TYPE_PNG))
    elif (newtool == 'FillRect'):
      self.bDrawFilledRectangle.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_filled_rectangle_selected.png'), wx.BITMAP_TYPE_PNG))
    elif (newtool == 'OutlineRect'):
      self.bDrawOutlinedRectangle.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_open_rectangle_selected.png'), wx.BITMAP_TYPE_PNG))
    elif (newtool == 'Line'):
      self.bDrawLine.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_line_selected.png'), wx.BITMAP_TYPE_PNG))
    elif (newtool == 'Multiline'):
      self.bDrawMultiline.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_line_segments_selected.png'), wx.BITMAP_TYPE_PNG))
    elif (newtool == 'Freehand'):
      self.bDrawFreehand.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_freehand_selected.png'), wx.BITMAP_TYPE_PNG))
    elif (newtool == 'Image'):
      self.bImportCustomImage.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_insert_custom_selected.png'), wx.BITMAP_TYPE_PNG))
    elif (newtool == 'GetProperty'):
      self.bGetProperties.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_get_properties_selected.png'), wx.BITMAP_TYPE_PNG))
    elif (newtool == 'ChangeProperty'):
      self.bChangeProperties.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_change_properties_selected.png'), wx.BITMAP_TYPE_PNG))

    self.oldtool = newtool
    if (newtool == 'Select') or (newtool == 'Delete'):
      app.DrawMapWindow()
      return
    else:
      self.DeSelectItem()
      app.DrawMapWindow()
    return

  def DeSelectItem(self):
    for item in app.DrawingList:
      if (item.selected):
        item.selected = False
        break
    return

  def OnSelectItem( self, event ):
    gv.DrawingTool = 'Select'
    self.ChangeToolBitmaps('Select')
    return

  def OnChooseOutlineColor( self, event ):
    gv.DrawOutlineColor = self.bChooseOutlineColor.GetColour()
    self.UpdateLineSample()
    return

  def OnChooseFillColor( self, event ):
    color = self.bChooseFillColor.GetColour()
    alpha = self.slFillTransparency.GetValue()
    setcolor = wx.Colour(color.Red(), color.Green(), color.Blue(), alpha)
    gv.DrawingToolBrush = wx.Brush(setcolor)
    self.UpdateLineSample()
    return

  def OnDeleteItem( self, event ):
    gv.DrawingTool = 'Delete'
    self.ChangeToolBitmaps('Delete')
    return

  def OnDrawFilledCircle( self, event ):
    gv.DrawingTool = 'FillCircle'
    self.ChangeToolBitmaps('FillCircle')
    return

  def OnDrawOutlinedCircle( self, event ):
    gv.DrawingTool = 'OutlineCircle'
    self.ChangeToolBitmaps('OutlineCircle')
    return

  def OnDrawFilledRectangle( self, event ):
    gv.DrawingTool = 'FillRect'
    self.ChangeToolBitmaps('FillRect')
    return

  def OnDrawOutlinedRectangle( self, event ):
    gv.DrawingTool = 'OutlineRect'
    self.ChangeToolBitmaps('OutlineRect')
    return

  def OnChangeProperty(self, event):
    gv.DrawingTool = 'ChangeProperty'
    self.ChangeToolBitmaps('ChangeProperty')
    return

  def OnGetProperty(self, event):
    gv.DrawingTool = 'GetProperty'
    self.ChangeToolBitmaps('GetProperty')
    return

  def OnDrawLine( self, event ):
    gv.DrawingTool = 'Line'
    self.ChangeToolBitmaps('Line')
    return

  def OnDrawMultiline( self, event ):
    gv.DrawingTool = 'Multiline'
    self.ChangeToolBitmaps('Multiline')
    return

  def OnDrawFreehand( self, event ):
    gv.DrawingTool = 'Freehand'
    self.ChangeToolBitmaps('Freehand')
    return

  def OnImportCustomImage( self, event ):
    gv.DrawingTool = 'Image'
    self.ChangeToolBitmaps('Image')
    return
  
  def OnDrawPoint(self, event):
    gv.DrawingTool = 'Point'
    self.ChangeToolBitmaps('Point')
    return


class TilesetManifestDialog(PyMapperDialogs.TilesetManifestDialogBase):
  def __init__(self, parent, text_string):
    olddir = os.getcwd()
    os.chdir(gv.root_directory)  #this is necessary so that bitmap paths are read by the dialog code correctly
    
    PyMapperDialogs.TilesetManifestDialogBase.__init__(self, parent)
    os.chdir(olddir)
    self.txTextBox.ChangeValue(text_string)
    return

  def OnClose( self, event ):
    self.EndModal(True)
    return

  def OnCopyToClipboard( self, event ):
    self.txTextBox.Copy()
    return

class Page_Record():
  def __init__(self, page=None, zoom=None, x=None, y=None, name=None):
    self.PageID = page  #index
    self.ZoomFactor = zoom
    self.ShowGrid = False  #show the grid on each individual page?
    self.ShowIconNames = False  #show the icon names (labels) on the page?
    self.Xscroll = x
    self.Yscroll = y
    self.PageName = name
    self.tilesets = []  #list of tilesets displayed on this page
    self.background = None #wx image format; used to facilitate rotation
    self.bg_displaymode = None #may be Register, Tile, Center
    self.bg_x_dimension = 0  #size of the background in squares
    self.bg_y_dimension = 0  
    self.background_filename = None #original path for the filename of the image
    self.background_filepath = None #original path where located
    return

    
########################################################################
class TilesetBuilderCompositeDialog(PyMapperDialogs.TilesetBuilderDialogCore):
  """Create a tileset using a single composite image"""

  #----------------------------------------------------------------------
  def __init__(self, parent):
    """Constructor"""
    olddir = os.getcwd()
    os.chdir(gv.root_directory)  #this is necessary so that bitmap paths are read by the dialog code correctly
    PyMapperDialogs.TilesetBuilderDialogCore.__init__(self, parent)
    os.chdir(olddir)
    
    return

class ManifestPrintPreview(PyMapperDialogs.ManifestPreviewDialogBase):
  #----------------------------------------------------------------------
  def __init__(self, parent, pagelist, numPages):
    """pagelist is a list of bitmaps for the display"""
    olddir = os.getcwd()
    os.chdir(gv.root_directory)  #this is necessary so that bitmap paths are read by the dialog code correctly
    PyMapperDialogs.ManifestPreviewDialogBase.__init__(self, parent)
    
    os.chdir(olddir)
    self.pagelist = pagelist
    self.numpages = len(pagelist)
    self.current_page = 0
    
    self.bFirstPage.Enable(False)
    self.bPreviousPage.Enable(False)
    self.stNumPages.SetLabel(str(self.numpages)+" pages")
    
    if (self.numpages > 1):
      self.bNextPage.Enable(True)
      self.bLastPage.Enable(True)
    elif (self.numpages == 1):
      self.bLastPage.Enable(False)
      self.bNextPage.Enable(False)
    return
  
  def OnCancel(self, event):
    self.EndModal(False)
    return
  
  def OnPrint(self, event):
    self.EndModal(True)
    return
  
  def GoToPreviousPage(self, event):
    self.current_page -= 1
    if (self.current_page == 0):
      self.bFirstPage.Enable(False)
      self.bPreviousPage.Enable(False)
    self.bNextPage.Enable(True)
    self.bLastPage.Enable(True)
    self.Refresh()
    return
  
  def GoToFirstPage(self, event):
    self.current_page = 0
    self.Refresh()
    self.bFirstPage.Enable(False)
    self.bPreviousPage.Enable(False)
    self.bLastPage.Enable(True)
    self.bNextPage.Enable(True)
    self.Refresh()
    return
  
  def GoToNextPage(self, event):
    self.current_page += 1
    if (self.current_page == (self.numpages-1)): #click advanced us to last page
      self.bLastPage.Enable(False)
      self.bNextPage.Enable(False)
    else:
      self.bLastPage.Enable(True)
    self.bPreviousPage.Enable(True)
    self.bFirstPage.Enable(True)
    self.Refresh()
    return
  
  def GoToLastPage(self, event):
    self.current_page = self.numpages-1
    self.bNextPage.Enable(False)
    self.bLastPage.Enable(False)
    self.bFirstPage.Enable(True)
    self.bPreviousPage.Enable(True)
    self.Refresh()
    return
  
  def OnPaint(self, event):
    event.Skip()
    dc = wx.PaintDC(self.pnPagePanel)
    dc.DrawBitmap(self.pagelist[self.current_page], 0,0,True)
    return
  
  
  
#-----End of ManifestPrintPreview class -----
  
class RandomGeomorphDungeonDialog(PyMapperDialogs.RandomGeomorphDungeonDialogBase):
  def __init__(self, parent):
    olddir = os.getcwd()
    os.chdir(gv.root_directory)  #this is necessary so that bitmap paths are read by the dialog code correctly
    PyMapperDialogs.RandomGeomorphDungeonDialogBase.__init__(self, parent)
    os.chdir(olddir)

    self.bitmap = wx.Bitmap(180,210)
    self.ImagePanelDC = wx.ClientDC(self.pnImagePanel)
    self.ImagePanelDC.DrawBitmap(self.bitmap,0,0,True)

    self.pnImagePanel.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)

    self.pnImagePanel.Bind(wx.EVT_PAINT, self.OnPaint)

    self.filenames = []
    self.filepaths = []
    self.LimitGeomorphs = True
    self.cbLimitGeomorphUsage.SetValue(self.LimitGeomorphs)

  def LimitGeomorphUsage(self, event):
    if (self.LimitGeomorphs):
      self.stLimitText1.Enable(False)
      self.stLimitText2.Enable(False)
      self.spGeomorphUseLimit.Enable(False)
    else:
      self.stLimitText1.Enable(True)
      self.stLimitText2.Enable(True)
      self.spGeomorphUseLimit.Enable(True)
    return

  def OnGeomorphList(self, evt):
    index = self.lbGeomorphList.GetSelection()
    if (index != wx.NOT_FOUND):
      bitmap_path = self.filepaths[index]
      bitmap_path += ".bmp"
      self.bitmap = wx.Bitmap(bitmap_path, wx.BITMAP_TYPE_BMP)
      if (not self.bitmap.IsOk()):
        self.bitmap = wx.BitmapFromImage(app.ImageNotFound)
        logging.error("RandomGeomorphDungeonDialog:OnGeomorphList -->Could not find: %s",bitmap_path)
      self.ImagePanelDC.DrawBitmap(self.bitmap,0,0,True)
    return

  def GenerateDungeon(self, event):
    if (app.MapStruct.geomorph):
      app.MapStruct.geomorph = False
      app.DrawMapWindow(app.maplist)

    if (self.filepaths == []):
      return
    self.SetCursor(wx.StockCursor(wx.CURSOR_WAIT))
    geomorphList = []
    app.maplist = []
    gv.RoomList = []
    app.textlist = []
    for item in self.filepaths:
      gm = app.ReadGeomorphFile(item)
      if (gm == False):
        #some error caused an abort
        self.SetCursor(wx.StockCursor(wx.CURSOR_DEFAULT))
        return
      gm.filepath = item
      geomorphList.append(gm)
    columns = self.spHorizontalSize.GetValue()
    rows = self.spVerticalSize.GetValue()
    Voffset = 14
    Hoffset = 12
    choosing = True

    gm_array = []

    while (choosing):      #select the first geomorph
      active_geomorph = Geomorph_Record()
      active_geomorph = random.choice(geomorphList)

      if (active_geomorph.geomorphRight > 0):  #must have a connection on right side
        choosing = False

    active_geomorph.used += 1
    gm_array.append(active_geomorph)

    app.MapStruct.rows = rows * 14
    app.MapStruct.columns = columns * 12
    index = 0

    for j in range(rows): #number of rows
      for i in range(columns): #number of columns
        if (i == 0) and (j == 0): #top left corner
          pass  #we have already selected this geomorph
        elif (i > 0) and (j == 0):  #top row, so any top oriented connection is ok
          top_value = -1
          side_index = app.IJtoX(i-1, j, columns)
          side_value = gm_array[side_index].geomorphRight
          active_geomorph = self.SelectRandomGeomorph(geomorphList, top_value, side_value)
          gm_array.append(active_geomorph)
        elif (i == 0) and (j > 0):  #first column, so any connection to the left is ok
          side_value = -1
          top_index = app.IJtoX(i, j-1, columns)
          top_value = gm_array[top_index].geomorphBottom
          active_geomorph = self.SelectRandomGeomorph(geomorphList, top_value, side_value)
          gm_array.append(active_geomorph)
        else:
          top_index = app.IJtoX(i, j-1, columns)
          top_value = gm_array[top_index].geomorphBottom
          side_index = app.IJtoX(i-1, j, columns)
          side_value = gm_array[side_index].geomorphRight
          active_geomorph = self.SelectRandomGeomorph(geomorphList, top_value, side_value)
          gm_array.append(active_geomorph)

    index = 0
    Ncolumns = 0
    Nrows = 0
    #adjust the placement of tiles for each geomorph
    for gm in gm_array:
      for tile in gm.TileList:
        newtile = app.CopyTile(tile)
        newtile.MapPosition.x += (Hoffset * Ncolumns)
        newtile.MapPosition.y += (Voffset * Nrows)
        newtile.MapRect.x = newtile.MapPosition.x
        newtile.MapRect.y = newtile.MapPosition.y
        newtile.page = gv.MapPageList[app.nbMapNotebook.GetSelection()].PageName
        app.maplist.append(newtile)
      for room in gm.RoomList:
        newRoom = room.__deepcopy__(room)
        newRoom.MapRect.x += (Hoffset * Ncolumns)
        newRoom.MapRect.y += (Voffset * Nrows)
        newRoom.x += (Hoffset * Ncolumns)
        newRoom.y += (Voffset * Nrows)
        newRoom.page = gv.MapPageList[app.nbMapNotebook.GetSelection()].PageName
        gv.RoomList.append(newRoom)
      for text in gm.TextList:
        newText = text.__deepcopy__(text)
        newText.x += (Hoffset * Ncolumns)
        newText.y += (Voffset * Nrows)
        newText.page = gv.MapPageList[app.nbMapNotebook.GetSelection()].PageName
        app.textlist.append(newText)

      Ncolumns += 1
      if (Ncolumns >= columns):
        Nrows += 1
        Ncolumns = 0

    app.MapStruct.geomorph = False
    app.CalculateMapExtents(app.maplist)
    app.RMapClickShowAll()
    app.DrawMapWindow()
    self.SetCursor(wx.StockCursor(wx.CURSOR_DEFAULT))
    return

  def AddTileToMaplist(self, edge, tile, side, point):
    if (side == 'B'):
      tile.showingBside = True
    else:
      tile.showingBside = False
    
    tile.GenerateMapDisplay(gv.MapZoomFactor)
    tile.selected = False

    newtile = app.CopyTile(tile)
    newtile.layer = gv.ActiveLayer
    app.maplist.append(newtile)
    for tset in gv.tilesets:
      if tset.SetID == newtile.tilesetID:
        tset.used = True
    newtile.index = app.MasterIndex
    app.MasterIndex += 1
    newtile.order = len(app.maplist)

    newtile.MapRect = wx.Rect2D(newtile.MapPosition.x, newtile.MapPosition.y, Yscale, Xscale)
    app.UndoActionEvent(flag="ADD_TILE", tile=newtile)
    tile.num_used += 1
    if ((gv.LimitTiles == True) and (tile.num_used >= tile.copies)):
      tile.dimmed = True
      app.DrawTileWindow()
    return

  def SelectRandomGeomorph(self, geomorph_list, top_value, side_value):
    """geomorph_list = list of Geomorph_Records to choose from
    top_value = the value to match on the top side
    side_value = the value to match with the left side
    Returns a Geomorph_Record() for use"""
    gm = Geomorph_Record()
    new_gm = Geomorph_Record()
    candidate_list = []

    #build the list of candidate geomorphs that match the search criteria
    if (top_value == -1):  #don't check the top side;  any match is allowed for this side
      for geo in geomorph_list:
        if (self.LimitGeomorphs and geo.used >= self.spGeomorphUseLimit.GetValue()):
          continue  #can't choose this geomorph, it has too many copies already
        if (geo.geomorphLeft & side_value): #found a match
          candidate_list.append(geo)
    elif (side_value == -1):  #don't check the side;  any match is allowed for this side
      for geo in geomorph_list:
        if (self.LimitGeomorphs and geo.used >= self.spGeomorphUseLimit.GetValue()):
          continue  #can't choose this geomorph, it has too many copies already
        if (geo.geomorphTop & top_value): #found a match
          candidate_list.append(geo)
    else:  #check both sides
      for geo in geomorph_list:
        if (self.LimitGeomorphs and geo.used >= self.spGeomorphUseLimit.GetValue()):
          continue  #can't choose this geomorph, it has too many copies already
        if (geo.geomorphLeft & side_value) and (geo.geomorphTop & top_value): #found a match
          candidate_list.append(geo)

    if (candidate_list == []):
      #nothing found, return a random geomorph instead
      gm = random.choice(geomorph_list)
    else:
      gm = random.choice(candidate_list)
    gm.used += 1
    #copy the geomorph and return it
    x = gm.__deepcopy__(gm)
    return x

  def UpdateListBox(self, names=None, clear=False):
    if (clear):
      self.lbGeomorphList.Clear()
    if (names):
      self.lbGeomorphList.AppendItems(names)
    return

  def OnPaint(self, event):
    dc = wx.PaintDC(self.pnImagePanel)
    dc.DrawBitmap(self.bitmap, 0, 0, True)
    event.Skip()
    return

  def LoadGeomorphs(self, evt):
    dlg = wx.FileDialog(self, message="Choose geomorphs to open", defaultDir=gv.geomorphs_directory,
                        defaultFile="", wildcard=geomorph_wildcard,
                        style=wx.OPEN | wx.FD_MULTIPLE | wx.CHANGE_DIR)
    result = dlg.ShowModal()
    if (result):
      filenames = dlg.GetFilenames()
      paths = dlg.GetPaths()
      for fn in filenames:
        self.filenames.append(fn)
      for pth in paths:
        self.filepaths.append(pth)
      self.UpdateListBox(names=self.filenames, clear=True)
      dlg.Destroy()
      if (filenames):
        self.bGenerateDungeon.Enable(True)
    else:
      return

  def UnloadGeomorphs(self, evt):
    index = self.lbGeomorphList.GetSelection()
    if (index != wx.NOT_FOUND):
      self.filenames.pop(index)
      self.filepaths.pop(index)
      self.ImagePanelDC.Clear()
      self.UpdateListBox(self.filenames, True)
      if (self.filenames == []):
        self.bGenerateDungeon.Enable(False)
    return

  def OnOK(self, evt):
    #keep the maplist as generated
    self.Show(False)
    return True

  def OnCANCEL(self, evt):
    #clear the maplist, random dungeon not kept
    for x in app.selectlist:
      x.selected = False
    app.selectlist = []
    app.maplist = []
    gv.RoomList = []
    app.textlist =[]
    app.CalculateMapExtents(app.maplist)
    app.RMapClickShowAll()
    app.DrawMapWindow()
    self.Show(False)
    return False

  def OnHelp(self, evt):
    text = "Use this dialog to generate a random map using predefined geomorphs.\n\nThe listbox shows the available geomorphs, and the panel to the right shows a preview of it.\n\nAll of the geomorphs shown will be available to pymapper for use, but due to the random nature of things, not all of them may be used.  The number of times an individual geomorph is used can be limited by checking the box below the list.\n\nPyMapper will randomly select a geomorph to start with, and attempt to line up the connection points on following geomorphs.  If a suitable connection cannot be found then another random geomorph is selected.  This may cause some discontinuity that you will have to correct manually."
    dlg = HelpDialog(self, text)
    dlg.ShowModal()
    dlg.Destroy()
    return

class GeomorphSaveDialog(PyMapperDialogs.GeomorphSettingsDialogBase):
  def __init__(self, parent, bitmap, geomorph=None):
    olddir = os.getcwd()
    os.chdir(gv.root_directory)  #this is necessary so that bitmap paths are read by the dialog code correctly
    PyMapperDialogs.GeomorphSettingsDialogBase.__init__(self, parent)
    os.chdir(olddir)
    
    # Define variables for the controls, bind event handlers
    self.ImagePanel = self.pnImagePanel
    self.Bind(wx.EVT_PAINT, self.OnPaint)
    self.BitmapDisplay = self.ResizeImage(bitmap)

    if (geomorph):
      self.geomorphRight = geomorph.geomorphRight
      self.geomorphLeft = geomorph.geomorphLeft
      self.geomorphTop = geomorph.geomorphTop
      self.geomorphBottom = geomorph.geomorphBottom
      self.SetToggleButtons(geomorph)
    else:
      self.geomorphRight = 0
      self.geomorphLeft = 0
      self.geomorphTop = 0
      self.geomorphBottom = 0

    self.ImagePanel.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
    self.Update()
    return

  def SetToggleButtons(self, geomorph):
    if (not geomorph):
      return
    else:
      value = geomorph.geomorphTop
      if (value >= 32):
        self.tTop32.SetValue(True)
        value -= 32
      if (value >= 16):
        self.tTop16.SetValue(True)
        value -= 16
      if (value >= 8):
        self.tTop8.SetValue(True)
        value -= 8
      if (value >= 4):
        self.tTop4.SetValue(True)
        value -= 4
      if (value >= 2):
        self.tTop2.SetValue(True)
        value -= 2
      if (value >= 1):
        self.tTop1.SetValue(True)
        value -= 1

      value = geomorph.geomorphLeft
      if (value >= 64):
        self.tLeft64.SetValue(True)
        value -= 64
      if (value >= 32):
        self.tLeft32.SetValue(True)
        value -= 32
      if (value >= 16):
        self.tLeft16.SetValue(True)
        value -= 16
      if (value >= 8):
        self.tLeft8.SetValue(True)
        value -= 8
      if (value >= 4):
        self.tLeft4.SetValue(True)
        value -= 4
      if (value >= 2):
        self.tLeft2.SetValue(True)
        value -= 2
      if (value >= 1):
        self.tLeft1.SetValue(True)
        value -= 1

      value = geomorph.geomorphRight
      if (value >= 64):
        self.tRight64.SetValue(True)
        value -= 64
      if (value >= 32):
        self.tRight32.SetValue(True)
        value -= 32
      if (value >= 16):
        self.tRight16.SetValue(True)
        value -= 16
      if (value >= 8):
        self.tRight8.SetValue(True)
        value -= 8
      if (value >= 4):
        self.tRight4.SetValue(True)
        value -= 4
      if (value >= 2):
        self.tRight2.SetValue(True)
        value -= 2
      if (value >= 1):
        self.tRight1.SetValue(True)
        value -= 1

      value = geomorph.geomorphBottom
      if (value >= 32):
        self.tBottom32.SetValue(True)
        value -= 32
      if (value >= 16):
        self.tBottom16.SetValue(True)
        value -= 16
      if (value >= 8):
        self.tBottom8.SetValue(True)
        value -= 8
      if (value >= 4):
        self.tBottom4.SetValue(True)
        value -= 4
      if (value >= 2):
        self.tBottom2.SetValue(True)
        value -= 2
      if (value >= 1):
        self.tBottom1.SetValue(True)
        value -= 1
    return

  def OnOK(self, evt):
    bottom_value = 0
    if (self.tBottom1.GetValue()):
      bottom_value += 1
    if (self.tBottom2.GetValue()):
      bottom_value += 2
    if (self.tBottom4.GetValue()):
      bottom_value += 4
    if (self.tBottom8.GetValue()):
      bottom_value += 8
    if (self.tBottom16.GetValue()):
      bottom_value += 16
    if (self.tBottom32.GetValue()):
      bottom_value += 32
    self.geomorphBottom = bottom_value

    top_value = 0
    if (self.tTop1.GetValue()):
      top_value += 1
    if (self.tTop2.GetValue()):
      top_value += 2
    if (self.tTop4.GetValue()):
      top_value += 4
    if (self.tTop8.GetValue()):
      top_value += 8
    if (self.tTop16.GetValue()):
      top_value += 16
    if (self.tTop32.GetValue()):
      top_value += 32
    self.geomorphTop = top_value

    left_value = 0
    if (self.tLeft1.GetValue()):
      left_value += 1
    if (self.tLeft2.GetValue()):
      left_value += 2
    if (self.tLeft4.GetValue()):
      left_value += 4
    if (self.tLeft8.GetValue()):
      left_value += 8
    if (self.tLeft16.GetValue()):
      left_value += 16
    if (self.tLeft32.GetValue()):
      left_value += 32
    if (self.tLeft64.GetValue()):
      left_value += 64
    self.geomorphLeft = left_value

    right_value = 0
    if (self.tRight1.GetValue()):
      right_value += 1
    if (self.tRight2.GetValue()):
      right_value += 2
    if (self.tRight4.GetValue()):
      right_value += 4
    if (self.tRight8.GetValue()):
      right_value += 8
    if (self.tRight16.GetValue()):
      right_value += 16
    if (self.tRight32.GetValue()):
      right_value += 32
    if (self.tRight64.GetValue()):
      right_value += 64
    self.geomorphRight = right_value
    self.EndModal(True)
    return

  def OnPaint(self, event):
    dc = wx.PaintDC(self.ImagePanel)
    dc.DrawBitmap(self.BitmapDisplay, 0, 0, True)
    event.Skip()
    return

  def OnSelectNoEdges(self, event):
    self.tTop32.SetValue(False)
    self.tTop16.SetValue(False)
    self.tTop8.SetValue(False)
    self.tTop4.SetValue(False)
    self.tTop2.SetValue(False)
    self.tTop1.SetValue(False)

    self.tLeft64.SetValue(False)
    self.tLeft32.SetValue(False)
    self.tLeft16.SetValue(False)
    self.tLeft8.SetValue(False)
    self.tLeft4.SetValue(False)
    self.tLeft2.SetValue(False)
    self.tLeft1.SetValue(False)

    self.tRight64.SetValue(False)
    self.tRight32.SetValue(False)
    self.tRight16.SetValue(False)
    self.tRight8.SetValue(False)
    self.tRight4.SetValue(False)
    self.tRight2.SetValue(False)
    self.tRight1.SetValue(False)

    self.tBottom32.SetValue(False)
    self.tBottom16.SetValue(False)
    self.tBottom8.SetValue(False)
    self.tBottom4.SetValue(False)
    self.tBottom2.SetValue(False)
    self.tBottom1.SetValue(False)
    return

  def OnSelectAllEdges(self, event):
    self.tTop32.SetValue(True)
    self.tTop16.SetValue(True)
    self.tTop8.SetValue(True)
    self.tTop4.SetValue(True)
    self.tTop2.SetValue(True)
    self.tTop1.SetValue(True)

    self.tLeft64.SetValue(True)
    self.tLeft32.SetValue(True)
    self.tLeft16.SetValue(True)
    self.tLeft8.SetValue(True)
    self.tLeft4.SetValue(True)
    self.tLeft2.SetValue(True)
    self.tLeft1.SetValue(True)

    self.tRight64.SetValue(True)
    self.tRight32.SetValue(True)
    self.tRight16.SetValue(True)
    self.tRight8.SetValue(True)
    self.tRight4.SetValue(True)
    self.tRight2.SetValue(True)
    self.tRight1.SetValue(True)

    self.tBottom32.SetValue(True)
    self.tBottom16.SetValue(True)
    self.tBottom8.SetValue(True)
    self.tBottom4.SetValue(True)
    self.tBottom2.SetValue(True)
    self.tBottom1.SetValue(True)
    return

  def ResizeImage(self, bitmap):
    base_point = wx.Point()
    crop_area = wx.Rect(gv.MapZoomFactor, gv.MapZoomFactor,
                        gv.MapZoomFactor*12, gv.MapZoomFactor*14)
    image = wx.ImageFromBitmap(bitmap)
    image = image.GetSubImage(crop_area)
    image = image.Scale(180,210)
    bmp = wx.BitmapFromImage(image)
    return bmp

  def OnCancel(self, evt):
    self.EndModal(False)
    return

  def OnHelp(self, evt):
    text = "Select the toggle buttons on the sides to define the connection points for the geomorph.\n\nThe dungeon randomizer uses these connection points when matching edges during the selection process.\n\nCancel from this dialog will cancel the saving of the file."
    dlg = HelpDialog(self, text)
    dlg.ShowModal()
    dlg.Destroy()
    return

class Geomorph_Record():
  def __init__(self):
    self.TileList = []
    self.RoomList = []
    self.TextList = []
    self.LayerList = []
    self.LayerDisplay = []
    self.background_filename = None
    self.filepath = None
    self.preview = None  #bitmap image of the geomorph
    self.geomorphRight = 0
    self.geomorphLeft = 0
    self.geomorphTop = 0
    self.geomorphBottom = 0
    self.checked = False  #have we checked this GM in the random selector?
    self.index = 0  #index used in the gm_array
    self.used = 0 #how many times has this been used in the random dungeon?
    return

  def __deepcopy__(self, gm):
    new_gm = Geomorph_Record()
    new_gm.background_filename = gm.background_filename
    new_gm.filepath = gm.filepath
    new_gm.geomorphBottom = gm.geomorphBottom
    new_gm.geomorphLeft = gm.geomorphLeft
    new_gm.geomorphRight = gm.geomorphRight
    new_gm.geomorphTop = gm.geomorphTop
    new_gm.index = gm.index
    new_gm.checked = gm.checked
    new_gm.preview = gm.preview
    for item in gm.LayerDisplay:
      new_gm.LayerDisplay.append(item)
    for item in gm.LayerList:
      new_gm.LayerList.append(item)
    for item in gm.RoomList:
      new_gm.RoomList.append(item)
    for item in gm.TextList:
      new_gm.TextList.append(item)
    for item in gm.TileList:
      new_gm.TileList.append(item)
    return new_gm


class SRD_Progress_Dialog(PyMapperDialogs.SRD_Progress_DialogBase):
  def __init__(self, parent, mode):
    """mode is what kind of information is being loaded:  DnD5 or PFd20"""
    olddir = os.getcwd()
    os.chdir(gv.root_directory)  #this is necessary so that bitmap paths are read by the dialog code correctly
    
    PyMapperDialogs.SRD_Progress_DialogBase.__init__(self, parent)
    os.chdir(olddir)
    self.owner = parent
    
    if (mode == 'DnD5'):
      self.gClassSkillsGauge.Hide()
      self.gClassTableGauge.Hide()
      self.gFeatsGauge.Hide()
      self.gClassSkillsGauge.Hide()
      self.gClassTableGauge.Hide()
      # self.gRacesGauge.Hide()  # don't hide the races gauge; we use it for the npc update bar
      self.gRacialBonusesGauge.Hide()
      self.gNamesGauge.Hide()
      self.stNames.Hide()
      self.stClassSkills.Hide()
      self.stClassTable.Hide()
      self.stFeats.Hide()
      self.stClassSkills.Hide()
      self.stClassTable.Hide()
      self.stRaces.SetLabel("NPC File:")
      self.stRacialBonuses.Hide()
      self.Fit()
    elif (mode == 'PFd20'):
      pass
      
    return


class Filenames_Record():
  def __init__(self):
    self.importName = None
    self.importRenamed = None
    return

class TreasuresDialog(PyMapperDialogs.TreasureDialogBase):
  def __init__(self, parent, start_treasure=None, add_icon=False, open_xml=True):
    olddir = os.getcwd()
    os.chdir(gv.root_directory)  #this is necessary so that bitmap paths are read by the dialog code correctly
    PyMapperDialogs.TreasureDialogBase.__init__(self, parent)
    os.chdir(olddir)

    self.Treasure = TreasureItem()
    self.add_icon = add_icon
    self.open_xml = open_xml
    if (start_treasure):
      self.txCP.SetValue(start_treasure.cp)
      self.txSP.SetValue(start_treasure.sp)
      self.txGP.SetValue(start_treasure.gp)
      self.txPP.SetValue(start_treasure.pp)
    return

  def PrintTreasureText(self):
    text = self.txDescription.GetValue() + "\n"
    if (self.txCP.GetValue() != '0'):
      text += str(self.txCP.GetValue()) + " CP\n"
    if (self.txSP.GetValue() != '0'):
      text += str(self.txSP.GetValue()) + " SP\n"
    if (self.txGP.GetValue() != '0'):
      text += str(self.txGP.GetValue()) + " GP\n"
    if (self.txPP.GetValue() != '0'):
      text += str(self.txPP.GetValue()) + " PP\n"
    for item in self.Treasure.goods:
      text += item + '\n'
    for item in self.Treasure.magic:
      text += item + '\n'
    for item in self.Treasure.other:
      text += item + '\n'
    for item in self.Treasure.gem10:
      text += item + ' (average value: 10 GP)\n'
    for item in self.Treasure.gem50:
      text += item + ' (average value: 50 GP)\n'
    for item in self.Treasure.gem100:
      text += item + ' (average value: 100 GP)\n'
    for item in self.Treasure.gem500:
      text += item + ' (average value: 500 GP)\n'
    for item in self.Treasure.gem1000:
      text += item + ' (average value: 1000 GP)\n'
    for item in self.Treasure.gem5000:
      text += item + ' (average value: 5000 GP)\n'
    for item in self.Treasure.ArtList55:
      text += item + ' (average value: 55 GP)\n'
    for item in self.Treasure.ArtList105:
      text += item + ' (average value: 105 GP)\n'
    for item in self.Treasure.ArtList350:
      text += item + ' (average value: 350 GP)\n'
    for item in self.Treasure.ArtList550:
      text += item + ' (average value: 550 GP)\n'
    for item in self.Treasure.ArtList700:
      text += item + ' (average value: 700 GP)\n'
    for item in self.Treasure.ArtList1050:
      text += item + ' (average value: 1050 GP)\n'
    for item in self.Treasure.ArtList1400:
      text += item + ' (average value: 1400 GP)\n'
    for item in self.Treasure.ArtList1750:
      text += item + ' (average value: 1750 GP)\n'
    for item in self.Treasure.ArtList2500:
      text += item + ' (average value: 2500 GP)\n'
    for item in self.Treasure.ArtList3500:
      text += item + ' (average value: 3500 GP)\n'
    for item in self.Treasure.ArtList5000:
      text += item + ' (average value: 5000 GP)\n'

    return text

  def OnOK(self, evt):
    self.Treasure.description = self.txDescription.GetValue()
    self.EndModal(True)
    room = RoomInfo()
    room.Description = self.txDescription.GetValue()
    room.Icon = app.TreasureIcon
    room.IconType = 'Treasure'
    gv.RoomList.append(room)
    text = self.PrintTreasureText()
    if (self.open_xml):
      position = (0,0)
      xml_editor = IconEditorFrame(self, room.Description, room, position, text)
      xml_editor.Show()
      xml_editor.Raise()
      gv.rtc_open = True
      gv.rtc_icon = room
    return True

  def OnCancel(self, evt):
    self.EndModal(False)
    return False

  def GenerateStandardTreasure(self, event):
    level = self.spEncounterLevel.GetValue()
    #roll for coins
    diceroll = app.RollDice('1d100')
    self.Treasure = self.CalculateCoins(level, diceroll)
    #roll for goods
    diceroll = app.RollDice('1d100')
    goods = self.CalculateGoods(level, diceroll)
    self.Treasure = self.AddTreasures(goods, self.Treasure)
    #roll for magic/mundane items
    diceroll = app.RollDice('1d100')
    items = self.CalculateItems(level, diceroll)
    self.Treasure = self.AddTreasures(items, self.Treasure)

    #set text fields
    self.txCP.SetValue(str(self.Treasure.cp))
    self.txSP.SetValue(str(self.Treasure.sp))
    self.txGP.SetValue(str(self.Treasure.gp))
    self.txPP.SetValue(str(self.Treasure.pp))
    #add art and gems to the display list
    self.lbGoods.Clear()
    self.lbMagicItems.Clear()
    self.lbMundaneItems.Clear()

    for item in self.Treasure.ArtList55:
      text = item + ' (avg. value 55 gp)'
      self.lbGoods.Append(text)
    for item in self.Treasure.ArtList105:
      text = item + ' (avg. value 105 gp)'
      self.lbGoods.Append(text)
    for item in self.Treasure.ArtList350:
      text = item + ' (avg. value 350 gp)'
      self.lbGoods.Append(text)
    for item in self.Treasure.ArtList550:
      text = item + ' (avg. value 550 gp)'
      self.lbGoods.Append(text)
    for item in self.Treasure.ArtList700:
      text = item + ' (avg. value 700 gp)'
      self.lbGoods.Append(text)
    for item in self.Treasure.ArtList1050:
      text = item + ' (avg. value 1050 gp)'
      self.lbGoods.Append(text)
    for item in self.Treasure.ArtList1400:
      text = item + ' (avg. value 1400 gp)'
      self.lbGoods.Append(text)
    for item in self.Treasure.ArtList1750:
      text = item + ' (avg. value 1750 gp)'
      self.lbGoods.Append(text)
    for item in self.Treasure.ArtList2500:
      text = item + ' (avg. value 2500 gp)'
      self.lbGoods.Append(text)
    for item in self.Treasure.ArtList3500:
      text = item + ' (avg. value 3500 gp)'
      self.lbGoods.Append(text)
    for item in self.Treasure.ArtList5000:
      text = item + ' (avg. value 5000 gp)'
      self.lbGoods.Append(text)
    for item in self.Treasure.ArtList7000:
      text = item + ' (avg. value 7000 gp)'
      self.lbGoods.Append(text)
    for item in self.Treasure.gem10:
      text = item + ' (avg. value 10 gp)'
      self.lbGoods.Append(text)
    for item in self.Treasure.gem50:
      text = item + ' (avg. value 50 gp)'
      self.lbGoods.Append(text)
    for item in self.Treasure.gem100:
      text = item + ' (avg. value 100 gp)'
      self.lbGoods.Append(text)
    for item in self.Treasure.gem500:
      text = item + ' (avg. value 500 gp)'
      self.lbGoods.Append(text)
    for item in self.Treasure.gem1000:
      text = item + ' (avg. value 1000 gp)'
      self.lbGoods.Append(text)
    for item in self.Treasure.gem5000:
      text = item + ' (avg. value 5000 gp)'
      self.lbGoods.Append(text)


    if (self.lbGoods.IsEmpty()):
      self.lbGoods.Append('None')
    if (self.Treasure.magic == []):
      self.lbMagicItems.Append('None')
    else:
      self.lbMagicItems.AppendItems(self.Treasure.magic)
    if (self.Treasure.other == []):
      self.lbMundaneItems.Append('None')
    else:
      self.lbMundaneItems.AppendItems(self.Treasure.other)
    return

  def CalculateCoins(self, EL, diceroll):
    CP = 0
    SP = 0
    GP = 0
    PP = 0

    if (EL == 1):
      if (diceroll >= 15) and (diceroll <= 29):
        CP = app.RollDice('1d6')*1000
      elif (diceroll >= 30) and (diceroll <= 52):
        SP = app.RollDice('1d8')*100
      elif (diceroll >= 53) and (diceroll <= 95):
        GP = app.RollDice('2d8')*10
      elif (diceroll >= 96):
        PP = app.RollDice('1d4')*10
    elif (EL == 2):
      if (diceroll >= 14) and (diceroll <= 23):
        CP = app.RollDice('1d10')*1000
      elif (diceroll >= 24) and (diceroll <= 43):
        SP = app.RollDice('2d10')*100
      elif (diceroll >= 44) and (diceroll <= 95):
        GP = app.RollDice('4d10')*10
      elif (diceroll >= 96):
        PP = app.RollDice('2d8')*10
    elif (EL == 3):
      if (diceroll >= 12) and (diceroll <= 21):
        CP = app.RollDice('2d10')*1000
      elif (diceroll >= 22) and (diceroll <= 41):
        SP = app.RollDice('4d8')*100
      elif (diceroll >= 42) and (diceroll <= 95):
        GP = app.RollDice('1d4')*100
      elif (diceroll >= 96):
        PP = app.RollDice('1d10')*10
    elif (EL == 4):
      if (diceroll >= 12) and (diceroll <= 21):
        CP = app.RollDice('3d10')*1000
      elif (diceroll >= 22) and (diceroll <= 41):
        SP = app.RollDice('4d12')*1000
      elif (diceroll >= 42) and (diceroll <= 95):
        GP = app.RollDice('1d6')*100
      elif (diceroll >= 96):
        PP = app.RollDice('1d8')*10
    elif (EL == 5):
      if (diceroll >= 11) and (diceroll <= 19):
        CP = app.RollDice('1d4')*10000
      elif (diceroll >= 20) and (diceroll <= 38):
        SP = app.RollDice('1d6')*1000
      elif (diceroll >= 39) and (diceroll <= 95):
        GP = app.RollDice('1d8')*100
      elif (diceroll >= 96):
        PP = app.RollDice('1d10')*10
    elif (EL == 6):
      if (diceroll >= 11) and (diceroll <= 18):
        CP = app.RollDice('1d6')*10000
      elif (diceroll >= 19) and (diceroll <= 37):
        SP = app.RollDice('1d8')*1000
      elif (diceroll >= 38) and (diceroll <= 95):
        GP = app.RollDice('1d10')*100
      elif (diceroll >= 96):
        PP = app.RollDice('1d12')*10
    elif (EL == 7):
      if (diceroll >= 12) and (diceroll <= 18):
        CP = app.RollDice('1d10')*10000
      elif (diceroll >= 19) and (diceroll <= 35):
        SP = app.RollDice('1d12')*1000
      elif (diceroll >= 36) and (diceroll <= 93):
        GP = app.RollDice('2d6')*100
      elif (diceroll >= 94):
        PP = app.RollDice('3d4')*10
    elif (EL == 8):
      if (diceroll >= 11) and (diceroll <= 15):
        CP = app.RollDice('1d12')*10000
      elif (diceroll >= 16) and (diceroll <= 29):
        SP = app.RollDice('2d6')*1000
      elif (diceroll >= 30) and (diceroll <= 87):
        GP = app.RollDice('2d8')*100
      elif (diceroll >= 88):
        PP = app.RollDice('3d6')*10
    elif (EL == 9):
      if (diceroll >= 11) and (diceroll <= 15):
        CP = app.RollDice('2d6')*10000
      elif (diceroll >= 16) and (diceroll <= 29):
        SP = app.RollDice('2d8')*1000
      elif (diceroll >= 30) and (diceroll <= 85):
        GP = app.RollDice('5d4')*100
      elif (diceroll >= 86):
        PP = app.RollDice('2d12')*10
    elif (EL == 10):
      if (diceroll >= 11) and (diceroll <= 24):
        SP = app.RollDice('2d10')*1000
      elif (diceroll >= 25) and (diceroll <= 79):
        GP = app.RollDice('6d4')*100
      elif (diceroll >= 80):
        PP = app.RollDice('5d6')*10
    elif (EL == 11):
      if (diceroll >= 9) and (diceroll <= 14):
        SP = app.RollDice('3d10')*1000
      elif (diceroll >= 15) and (diceroll <= 75):
        GP = app.RollDice('4d8')*100
      elif (diceroll >= 76):
        PP = app.RollDice('4d10')*10
    elif (EL == 12):
      if (diceroll >= 9) and (diceroll <= 14):
        SP = app.RollDice('3d12')*1000
      elif (diceroll >= 15) and (diceroll <= 75):
        GP = app.RollDice('1d4')*1000
      elif (diceroll >= 76):
        PP = app.RollDice('1d4')*10
    elif (EL == 13):
      if (diceroll >= 9) and (diceroll <= 75):
        GP = app.RollDice('1d4')*1000
      elif (diceroll >= 76):
        PP = app.RollDice('1d10')*100
    elif (EL == 14):
      if (diceroll >= 9) and (diceroll <= 75):
        GP = app.RollDice('1d6')*1000
      elif (diceroll >= 76):
        PP = app.RollDice('1d12')*100
    elif (EL == 15):
      if (diceroll >= 4) and (diceroll <= 74):
        GP = app.RollDice('1d8')*1000
      elif (diceroll >= 75):
        PP = app.RollDice('3d4')*100
    elif (EL == 16):
      if (diceroll >= 4) and (diceroll <= 74):
        GP = app.RollDice('1d12')*1000
      elif (diceroll >= 75):
        PP = app.RollDice('3d4')*100
    elif (EL == 17):
      if (diceroll >= 4) and (diceroll <= 68):
        GP = app.RollDice('3d4')*1000
      elif (diceroll >= 69):
        PP = app.RollDice('2d10')*100
    elif (EL == 18):
      if (diceroll >= 3) and (diceroll <= 65):
        GP = app.RollDice('3d6')*1000
      elif (diceroll >= 66):
        PP = app.RollDice('5d4')*100
    elif (EL == 19):
      if (diceroll >= 3) and (diceroll <= 65):
        GP = app.RollDice('3d8')*1000
      elif (diceroll >= 66):
        PP = app.RollDice('3d10')*100
    elif (EL == 20):
      if (diceroll >= 3) and (diceroll <= 65):
        GP = app.RollDice('4d8')*1000
      elif (diceroll >= 66):
        PP = app.RollDice('4d10')*100

    coins = TreasureItem()
    coins.cp = CP
    coins.sp = SP
    coins.gp = GP
    coins.pp = PP
    return coins

  def AddTreasures(self, treasure1, treasure2):
    total = TreasureItem()
    total.cp = treasure1.cp + treasure2.cp
    total.sp = treasure1.sp + treasure2.sp
    total.gp = treasure1.cp + treasure2.gp
    total.pp = treasure1.cp + treasure2.pp

    total.gem10 = treasure1.gem10 + treasure2.gem10
    total.gem100 = treasure1.gem100 + treasure2.gem100
    total.gem500 = treasure1.gem500 + treasure2.gem500
    total.gem1000 = treasure1.gem1000 + treasure2.gem1000
    total.gem5000 = treasure1.gem5000 + treasure2.gem5000

    total.goods = treasure1.goods + treasure2.goods
    total.magic = treasure1.magic + treasure2.magic
    total.other = treasure1.other + treasure2.other

    total.ArtList55 = treasure1.ArtList55 + treasure2.ArtList55
    total.ArtList105 = treasure1.ArtList105 + treasure2.ArtList105
    total.ArtList350 = treasure1.ArtList350 + treasure2.ArtList350
    total.ArtList550 = treasure1.ArtList550 + treasure2.ArtList550
    total.ArtList700 = treasure1.ArtList700 + treasure2.ArtList700
    total.ArtList1050 = treasure1.ArtList1050 + treasure2.ArtList1050
    total.ArtList1400 = treasure1.ArtList1400 + treasure2.ArtList1400
    total.ArtList1750 = treasure1.ArtList1750 + treasure2.ArtList1750
    total.ArtList2500 = treasure1.ArtList2500 + treasure2.ArtList2500
    total.ArtList3500 = treasure1.ArtList3500 + treasure2.ArtList3500
    total.ArtList5000 = treasure1.ArtList5000 + treasure2.ArtList5000
    total.ArtList7000 = treasure1.ArtList7000 + treasure2.ArtList7000

    return total

  def DetermineGemValue(self, diceroll):
    treasure = TreasureItem()
    if (diceroll >= 1) and (diceroll <= 25):
      index = random.randint(0, len(ts.GemList10)-1)
      treasure.gem10.append(ts.GemList10[index])
    elif (diceroll >= 26) and (diceroll <= 50):
      index = random.randint(0, len(ts.GemList50)-1)
      treasure.gem50.append(ts.GemList50[index])
    elif (diceroll >= 51) and (diceroll <= 70):
      index = random.randint(0, len(ts.GemList100)-1)
      treasure.gem100.append(ts.GemList100[index])
    elif (diceroll >= 71) and (diceroll <= 90):
      index = random.randint(0, len(ts.GemList500)-1)
      treasure.gem500.append(ts.GemList500[index])
    elif (diceroll >= 91) and (diceroll <= 99):
      index = random.randint(0, len(ts.GemList1000)-1)
      treasure.gem1000.append(ts.GemList1000[index])  
    elif (diceroll == 100):
      index = random.randint(0, len(ts.GemList5000)-1)
      treasure.gem5000.append(ts.GemList5000[index])
    return treasure

  def DetermineArtValue(self, diceroll):
    treasure = TreasureItem()
    if (diceroll <= 10):
      index = random.randint(0, len(ts.ArtList55)-1)
      treasure.ArtList55.append(ts.ArtList55[index])
    elif (diceroll <=25):
      index = random.randint(0, len(ts.ArtList105)-1)
      treasure.ArtList105.append(ts.ArtList105[index])
    elif (diceroll <=40):
      index = random.randint(0, len(ts.ArtList350)-1)
      treasure.ArtList350.append(ts.ArtList350[index])
    elif (diceroll <=50):
      index = random.randint(0, len(ts.ArtList550)-1)
      treasure.ArtList550.append(ts.ArtList550[index])
    elif (diceroll <=60):
      index = random.randint(0, len(ts.ArtList700)-1)
      treasure.ArtList700.append(ts.ArtList700[index])
    elif (diceroll <=70):
      index = random.randint(0, len(ts.ArtList1050)-1)
      treasure.ArtList1050.append(ts.ArtList1050[index])
    elif (diceroll <=80):
      index = random.randint(0, len(ts.ArtList1400)-1)
      treasure.ArtList1400.append(ts.ArtList1400[index])
    elif (diceroll <=85):
      index = random.randint(0, len(ts.ArtList1750)-1)
      treasure.ArtList1750.append(ts.ArtList1750[index])
    elif (diceroll <=90):
      index = random.randint(0, len(ts.ArtList2500)-1)
      treasure.ArtList2500.append(ts.ArtList2500[index])
    elif (diceroll <=95):
      index = random.randint(0, len(ts.ArtList3500)-1)
      treasure.ArtList3500.append(ts.ArtList3500[index])
    elif (diceroll <=99):
      index = random.randint(0, len(ts.ArtList5000)-1)
      treasure.ArtList5000.append(ts.ArtList5000[index])
    elif (diceroll == 100):
      index = random.randint(0, len(ts.ArtList7000)-1)
      treasure.ArtList7000.append(ts.ArtList7000[index])
    return treasure

  def CalculateItems(self, EL, diceroll):
    """Calculate the possibility of magic and/or mundane items in the hoard"""
    goods = TreasureItem()
    gem = []
    art = []
    if (EL == 1):
      if (diceroll >= 72) and (diceroll <= 95):
        item = self.DetermineMundaneItem()
        goods.other.append(item)
      elif (diceroll >= 96) and (diceroll <= 100):
        item = self.DetermineMagicItem('Minor')
        goods.magic.append(item)
    elif (EL == 2):
      if (diceroll >= 50) and (diceroll <= 85):
        item = self.DetermineMundaneItem()
        goods.other.append(item)
      elif (diceroll >= 86) and (diceroll <= 100):
        item = self.DetermineMagicItem('Minor')
        goods.magic.append(item)
    elif (EL == 3):
      if (diceroll >= 50) and (diceroll <= 79):
        num_items = app.RollDice('1d3')
        for i in range(num_items):
          item = self.DetermineMundaneItem()
          goods.other.append(item)
      elif (diceroll >= 80) and (diceroll <= 100):
        item = self.DetermineMagicItem('Minor')
        goods.magic.append(item)
    elif (EL == 4):
      if (diceroll >= 43) and (diceroll <= 62):
        num_items = app.RollDice('1d4')
        for i in range(num_items):
          item = self.DetermineMundaneItem()
          goods.other.append(item)
      elif (diceroll >= 63) and (diceroll <= 100):
        item = self.DetermineMagicItem('Minor')
        goods.magic.append(item)
    elif (EL == 5):
      if (diceroll >= 58) and (diceroll <= 67):
        num_items = app.RollDice('1d4')
        for i in range(num_items):
          item = self.DetermineMundaneItem()
          goods.other.append(item)
      elif (diceroll >= 68) and (diceroll <= 100):
        num_items = app.RollDice('1d3')
        for i in range(num_items):
          item = self.DetermineMagicItem('Minor')
          goods.magic.append(item)
    elif (EL == 6):
      if (diceroll >= 55) and (diceroll <= 59):
        num_items = app.RollDice('1d4')
        for i in range(num_items):
          item = self.DetermineMundaneItem()
          goods.other.append(item)
      elif (diceroll >= 60) and (diceroll <= 99):
        num_items = app.RollDice('1d3')
        for i in range(num_items):
          item = self.DetermineMagicItem('Minor')
          goods.magic.append(item)
      elif (diceroll >= 100) and (diceroll <= 100):
        item = self.DetermineMagicItem('Medium')
        goods.magic.append(item)
    elif (EL == 7):
      if (diceroll >= 52) and (diceroll <= 97):
        num_items = app.RollDice('1d3')
        for i in range(num_items):
          item = self.DetermineMagicItem('Minor')
          goods.magic.append(item)
      elif (diceroll >= 98) and (diceroll <= 100):
        item = self.DetermineMagicItem('Medium')
        goods.magic.append(item)
    elif (EL == 8):
      if (diceroll >= 49) and (diceroll <= 96):
        num_items = app.RollDice('1d4')
        for i in range(num_items):
          item = self.DetermineMagicItem('Minor')
          goods.magic.append(item)
      elif (diceroll >= 97) and (diceroll <= 100):
        item = self.DetermineMagicItem('Medium')
        goods.magic.append(item)
    elif (EL == 9):
      if (diceroll >= 44) and (diceroll <= 91):
        num_items = app.RollDice('1d4')
        for i in range(num_items):
          item = self.DetermineMagicItem('Minor')
          goods.magic.append(item)
      elif (diceroll >= 92) and (diceroll <= 100):
        item = self.DetermineMagicItem('Medium')
        goods.magic.append(item)
    elif (EL == 10):
      if (diceroll >= 41) and (diceroll <= 88):
        num_items = app.RollDice('1d4')
        for i in range(num_items):
          item = self.DetermineMagicItem('Minor')
          goods.magic.append(item)
      elif (diceroll >= 89) and (diceroll <= 99):
        item = self.DetermineMagicItem('Medium')
        goods.magic.append(item)
      elif (diceroll == 100):
        item = self.DetermineMagicItem('Major')
        goods.magic.append(item)
    elif (EL == 11):
      if (diceroll >= 32) and (diceroll <= 84):
        num_items = app.RollDice('1d4')
        for i in range(num_items):
          item = self.DetermineMagicItem('Minor')
          goods.magic.append(item)
      elif (diceroll >= 85) and (diceroll <= 99):
        item = self.DetermineMagicItem('Medium')
        goods.magic.append(item)
      elif (diceroll == 100):
        item = self.DetermineMagicItem('Major')
        goods.magic.append(item)
    elif (EL == 12):
      if (diceroll >= 28) and (diceroll <= 82):
        num_items = app.RollDice('1d6')
        for i in range(num_items):
          item = self.DetermineMagicItem('Minor')
          goods.magic.append(item)
      elif (diceroll >= 83) and (diceroll <= 97):
        item = self.DetermineMagicItem('Medium')
        goods.magic.append(item)
      elif (diceroll >= 98) and (diceroll <= 100):
        item = self.DetermineMagicItem('Major')
        goods.magic.append(item)
    elif (EL == 13):
      if (diceroll >= 20) and (diceroll <= 73):
        num_items = app.RollDice('1d6')
        for i in range(num_items):
          item = self.DetermineMagicItem('Minor')
          goods.magic.append(item)
      elif (diceroll >= 74) and (diceroll <= 95):
        item = self.DetermineMagicItem('Medium')
        goods.magic.append(item)
      elif (diceroll >= 96) and (diceroll <= 100):
        item = self.DetermineMagicItem('Major')
        goods.magic.append(item)
    elif (EL == 14):
      if (diceroll >= 20) and (diceroll <= 58):
        num_items = app.RollDice('1d6')
        for i in range(num_items):
          item = self.DetermineMagicItem('Minor')
          goods.magic.append(item)
      elif (diceroll >= 59) and (diceroll <= 92):
        item = self.DetermineMagicItem('Medium')
        goods.magic.append(item)
      elif (diceroll >= 93) and (diceroll <= 100):
        item = self.DetermineMagicItem('Major')
        goods.magic.append(item)
    elif (EL == 15):
      if (diceroll >= 12) and (diceroll <= 46):
        num_items = app.RollDice('1d10')
        for i in range(num_items):
          item = self.DetermineMagicItem('Minor')
          goods.magic.append(item)
      elif (diceroll >= 47) and (diceroll <= 90):
        item = self.DetermineMagicItem('Medium')
        goods.magic.append(item)
      elif (diceroll >= 91) and (diceroll <= 100):
        item = self.DetermineMagicItem('Major')
        goods.magic.append(item)
    elif (EL == 16):
      if (diceroll >= 41) and (diceroll <= 46):
        num_items = app.RollDice('1d10')
        for i in range(num_items):
          item = self.DetermineMagicItem('Minor')
          goods.magic.append(item)
      elif (diceroll >= 47) and (diceroll <= 90):
        num_items = app.RollDice('1d3')
        for i in range(num_items):
          item = self.DetermineMagicItem('Medium')
          goods.magic.append(item)
      elif (diceroll >= 91) and (diceroll <= 100):
        item = self.DetermineMagicItem('Major')
        goods.magic.append(item)
    elif (EL == 17):
      if (diceroll >= 34) and (diceroll <= 83):
        num_items = app.RollDice('1d3')
        for i in range(num_items):
          item = self.DetermineMagicItem('Medium')
          goods.magic.append(item)
      elif (diceroll >= 84) and (diceroll <= 100):
        item = self.DetermineMagicItem('Major')
        goods.magic.append(item)
    elif (EL == 18):
      if (diceroll >= 25) and (diceroll <= 80):
        num_items = app.RollDice('1d4')
        for i in range(num_items):
          item = self.DetermineMagicItem('Medium')
          goods.magic.append(item)
      elif (diceroll >= 81) and (diceroll <= 100):
        item = self.DetermineMagicItem('Major')
        goods.magic.append(item)
    elif (EL == 19):
      if (diceroll >= 5) and (diceroll <= 70):
        num_items = app.RollDice('1d4')
        for i in range(num_items):
          item = self.DetermineMagicItem('Medium')
          goods.magic.append(item)
      elif (diceroll >= 71) and (diceroll <= 100):
        item = self.DetermineMagicItem('Major')
        goods.magic.append(item)
    elif (EL == 20):
      if (diceroll >= 26) and (diceroll <= 65):
        num_items = app.RollDice('1d4')
        for i in range(num_items):
          item = self.DetermineMagicItem('Medium')
          goods.magic.append(item)
      elif (diceroll >= 66) and (diceroll <= 100):
        num_items = app.RollDice('1d3')
        for i in range(num_items):
          item = self.DetermineMagicItem('Major')
          goods.magic.append(item)
    return goods

  def DetermineMundaneItem(self):
    typeroll = app.RollDice('1d100')
    item_roll = app.RollDice('1d100')
    treasure = None
    if (typeroll <= 17):  #alchemical item
      if (item_roll <= 12):
        treasure= 'Alchemists fire (1d4 flasks, 20 gp each)'
      elif (item_roll <= 24):
        treasure = 'Acid (2d4 flasks, 10 gp each)'
      elif (item_roll <= 36):
        treasure = 'Smokesticks (1d4 sticks, 20 gp each)'
      elif (item_roll <=48):
        treasure = 'Holy water (1d4 flasks, 25 gp each)'
      elif (item_roll <=62):
        treasure = 'Antitoxin (1d4 doses, 50 gp each)'
      elif (item_roll <=74):
        treasure = 'Everburning torch'
      elif (item_roll <=88):
        treasure = 'Tanglefoot bags (1d4 bags, 50 gp each)'
      elif (item_roll <=100):
        treasure = 'Thunderstones (1d4 stones, 30 gp each)'
    elif (typeroll <= 50): #armor item
      if (item_roll <=12):
        treasure = 'Chain shirt (100 gp)'
      elif (item_roll <=18):
        treasure = 'Masterwork studded leather (175 gp)'
      elif (item_roll <=26):
        treasure = 'Breastplate (200 gp)'
      elif (item_roll <=34):
        treasure = 'Banded mail (250 gp)'
      elif (item_roll <=54):
        treasure = 'Half-plate (600 gp)'
      elif (item_roll <=80):
        treasure = 'Full plate (1,500 gp)'
      elif (item_roll <=90):
        #darkwood item
        sub_roll = app.RollDice('1d100')
        if (sub_roll <= '50'):
          treasure = 'Darkwood Buckler (205 gp)'
        else:
          treasure = 'Darkwood Shield (257 gp)'
      elif (item_roll <=100):  #masterwork shield item
        sub_roll = app.RollDice('1d100')
        if (sub_roll <= '17'):
          treasure = 'Masterwork buckler (165 gp)'
        if (sub_roll <= '40'):
          treasure = 'Masterwork light wooden shield (153 gp)'
        if (sub_roll <= '60'):
          treasure = 'Masterwork light steel shield (159 gp)'
        if (sub_roll <= '83'):
          treasure = 'Masterwork heavy wooden shield (157 gp)'
        if (sub_roll <= '100'):
          treasure = 'Masterwork heavy steel shield (170 gp)'
    elif (typeroll <= 83): #weapons
      if (item_roll <= 50):
        treasure = 'Masterwork common melee weapon'
      elif (item_roll <= 70):
        treasure = 'Masterwork uncommon melee weapon'
      elif (item_roll <= 100):
        treasure = 'Masterwork common ranged weapon'
    elif (typeroll <=100): #tools and gear
      if (item_roll <=3):
        treasure = 'Backpack, empty (2 gp)'
      elif (item_roll <=6):
        treasure = 'Crowbar (2 gp)'
      elif (item_roll <=11):
        treasure = 'Lantern, bullseye (12 gp)'
      elif (item_roll <=16):
        treasure = 'Lock, simple (20 gp)'
      elif (item_roll <=21):
        treasure = 'Lock, average (40 gp)'
      elif (item_roll <=28):
        treasure = 'Lock, good (80 gp)'
      elif (item_roll <=35):
        treasure = 'Lock, superior (150 gp)'
      elif (item_roll <=40):
        treasure = 'Manacles, masterwork (50 gp)'
      elif (item_roll <=43):
        treasure = 'Mirror, small steel (10 gp)'
      elif (item_roll <=46):
        treasure = 'Rope, silk (50 ft.) (10 gp)'
      elif (item_roll <=53):
        treasure = 'Spyglass (1,000 gp)'
      elif (item_roll <=58):
        treasure = 'Artisans tools, masterwork (55 gp)'
      elif (item_roll <=63):
        treasure = 'Climbers kit (80 gp)'
      elif (item_roll <=68):
        treasure = 'Disguise kit (50 gp)'
      elif (item_roll <=73):
        treasure = 'Healers kit (50 gp)'
      elif (item_roll <=77):
        treasure = 'Holy symbol, silver (25 gp)'
      elif (item_roll <=81):
        treasure = 'Hourglass (25 gp)'
      elif (item_roll <=88):
        treasure = 'Magnifying glass (100 gp)'
      elif (item_roll <=95):
        treasure = 'Musical instrument, masterwork (100 gp)'
      elif (item_roll <=100):
        treasure = 'Thieves tools, masterwork (50 gp)'
    return treasure

  def DetermineMagicItem(self, value):
    """value is either Minor, Medium, or Major.  The item name and value is returned as a text string"""
    if (value == 'Minor'):
      text = 'Minor magic item; Average value 1000 gp'
    elif (value == 'Medium'):
      text = 'Medium magic item; Average value 10,000 gp'
    elif (value == 'Major'):
      text = 'Major magic item; Average value 40,000 gp'
    return text

  def CalculateGoods(self, EL, diceroll):
    """Calculate the possibility of gems, artwork, or other valuables"""
    goods = TreasureItem()
    gem = []
    art = []
    if (EL == 1):
      if (diceroll >= 91) and (diceroll <= 95):
        roll = app.RollDice('1d100')
        gem = self.DetermineGemValue(roll)
        goods = self.AddTreasures(goods, gem)
      elif (diceroll >= 96) and (diceroll <= 100):
        roll = app.RollDice('1d100')
        art = self.DetermineArtValue(roll)
        goods = self.AddTreasures(goods, art)
    elif (EL == 2):
      if (diceroll >= 82) and (diceroll <= 95):
        num_gems = app.RollDice('1d3')
        for i in range(num_gems):
          gem_roll = app.RollDice('1d100')
          gem = self.DetermineGemValue(gem_roll)
          goods = self.AddTreasures(goods, gem)
      elif (diceroll >= 96):
        num_art = app.RollDice('1d3')
        for i in range(num_art):
          art_roll = app.RollDice('1d100')
          art = self.DetermineArtValue(art_roll)
          goods = self.AddTreasures(goods, art)
    elif (EL == 3):
      if (diceroll >= 78) and (diceroll <= 95):
        num_gems = app.RollDice('1d3')
        for i in range(num_gems):
          gem_roll = app.RollDice('1d100')
          gem = self.DetermineGemValue(gem_roll)
          goods = self.AddTreasures(goods, gem)
      elif (diceroll >= 96):
        num_art = app.RollDice('1d3')
        for i in range(num_art):
          art_roll = app.RollDice('1d100')
          art = self.DetermineArtValue(art_roll)
          goods = self.AddTreasures(goods, art)
    elif (EL == 4):
      if (diceroll >= 71) and (diceroll <= 95):
        num_gems = app.RollDice('1d4')
        for i in range(num_gems):
          gem_roll = app.RollDice('1d100')
          gem = self.DetermineGemValue(gem_roll)
          goods = self.AddTreasures(goods, gem)
      elif (diceroll >= 96):
        num_art = app.RollDice('1d3')
        for i in range(num_art):
          art_roll = app.RollDice('1d100')
          art = self.DetermineArtValue(art_roll)
          goods = self.AddTreasures(goods, art)
    elif (EL == 5):
      if (diceroll >= 61) and (diceroll <= 95):
        num_gems = app.RollDice('1d4')
        for i in range(num_gems):
          gem_roll = app.RollDice('1d100')
          gem = self.DetermineGemValue(gem_roll)
          goods = self.AddTreasures(goods, gem)
      elif (diceroll >= 96):
        num_art = app.RollDice('1d3')
        for i in range(num_art):
          art_roll = app.RollDice('1d100')
          art = self.DetermineArtValue(art_roll)
          goods = self.AddTreasures(goods, art)
    elif (EL == 6):
      if (diceroll >= 57) and (diceroll <= 92):
        num_gems = app.RollDice('1d4')
        for i in range(num_gems):
          gem_roll = app.RollDice('1d100')
          gem = self.DetermineGemValue(gem_roll)
          goods = self.AddTreasures(goods, gem)
      elif (diceroll >= 93):
        num_art = app.RollDice('1d4')
        for i in range(num_art):
          art_roll = app.RollDice('1d100')
          art = self.DetermineArtValue(art_roll)
          goods = self.AddTreasures(goods, art)
    elif (EL == 7):
      if (diceroll >= 49) and (diceroll <= 88):
        num_gems = app.RollDice('1d4')
        for i in range(num_gems):
          gem_roll = app.RollDice('1d100')
          gem = self.DetermineGemValue(gem_roll)
          goods = self.AddTreasures(goods, gem)
      elif (diceroll >= 89):
        num_art = app.RollDice('1d4')
        for i in range(num_art):
          art_roll = app.RollDice('1d100')
          art = self.DetermineArtValue(art_roll)
          goods = self.AddTreasures(goods, art)
    elif (EL == 8):
      if (diceroll >= 46) and (diceroll <= 85):
        num_gems = app.RollDice('1d6')
        for i in range(num_gems):
          gem_roll = app.RollDice('1d100')
          gem = self.DetermineGemValue(gem_roll)
          goods = self.AddTreasures(goods, gem)
      elif (diceroll >= 86):
        num_art = app.RollDice('1d4')
        for i in range(num_art):
          art_roll = app.RollDice('1d100')
          art = self.DetermineArtValue(art_roll)
          goods = self.AddTreasures(goods, art)
    elif (EL == 9):
      if (diceroll >= 41) and (diceroll <= 80):
        num_gems = app.RollDice('1d8')
        for i in range(num_gems):
          gem_roll = app.RollDice('1d100')
          gem = self.DetermineGemValue(gem_roll)
          goods = self.AddTreasures(goods, gem)
      elif (diceroll >= 81):
        num_art = app.RollDice('1d4')
        for i in range(num_art):
          art_roll = app.RollDice('1d100')
          art = self.DetermineArtValue(art_roll)
          goods = self.AddTreasures(goods, art)
    elif (EL == 10):
      if (diceroll >= 36) and (diceroll <= 79):
        num_gems = app.RollDice('1d8')
        for i in range(num_gems):
          gem_roll = app.RollDice('1d100')
          gem = self.DetermineGemValue(gem_roll)
          goods = self.AddTreasures(goods, gem)
      elif (diceroll >= 80):
        num_art = app.RollDice('1d6')
        for i in range(num_art):
          art_roll = app.RollDice('1d100')
          art = self.DetermineArtValue(art_roll)
          goods = self.AddTreasures(goods, art)
    elif (EL == 11):
      if (diceroll >= 25) and (diceroll <= 74):
        num_gems = app.RollDice('1d10')
        for i in range(num_gems):
          gem_roll = app.RollDice('1d100')
          gem = self.DetermineGemValue(gem_roll)
          goods = self.AddTreasures(goods, gem)
      elif (diceroll >= 75):
        num_art = app.RollDice('1d6')
        for i in range(num_art):
          art_roll = app.RollDice('1d100')
          art = self.DetermineArtValue(art_roll)
          goods = self.AddTreasures(goods, art)
    elif (EL == 12):
      if (diceroll >= 18) and (diceroll <= 70):
        num_gems = app.RollDice('1d10')
        for i in range(num_gems):
          gem_roll = app.RollDice('1d100')
          gem = self.DetermineGemValue(gem_roll)
          goods = self.AddTreasures(goods, gem)
      elif (diceroll >= 71):
        num_art = app.RollDice('1d8')
        for i in range(num_art):
          art_roll = app.RollDice('1d100')
          art = self.DetermineArtValue(art_roll)
          goods = self.AddTreasures(goods, art)
    elif (EL == 13):
      if (diceroll >= 12) and (diceroll <= 66):
        num_gems = app.RollDice('1d12')
        for i in range(num_gems):
          gem_roll = app.RollDice('1d100')
          gem = self.DetermineGemValue(gem_roll)
          goods = self.AddTreasures(goods, gem)
      elif (diceroll >= 67):
        num_art = app.RollDice('1d10')
        for i in range(num_art):
          art_roll = app.RollDice('1d100')
          art = self.DetermineArtValue(art_roll)
          goods = self.AddTreasures(goods, art)
    elif (EL == 14):
      if (diceroll >= 12) and (diceroll <= 66):
        num_gems = app.RollDice('2d8')
        for i in range(num_gems):
          gem_roll = app.RollDice('1d100')
          gem = self.DetermineGemValue(gem_roll)
          goods = self.AddTreasures(goods, gem)
      elif (diceroll >= 67):
        num_art = app.RollDice('2d6')
        for i in range(num_art):
          art_roll = app.RollDice('1d100')
          art = self.DetermineArtValue(art_roll)
          goods = self.AddTreasures(goods, art)
    elif (EL == 15):
      if (diceroll >= 10) and (diceroll <= 65):
        num_gems = app.RollDice('2d10')
        for i in range(num_gems):
          gem_roll = app.RollDice('1d100')
          gem = self.DetermineGemValue(gem_roll)
          goods = self.AddTreasures(goods, gem)
      elif (diceroll >= 66):
        num_art = app.RollDice('2d8')
        for i in range(num_art):
          art_roll = app.RollDice('1d100')
          art = self.DetermineArtValue(art_roll)
          goods = self.AddTreasures(goods, art)
    elif (EL == 16):
      if (diceroll >= 8) and (diceroll <= 64):
        num_gems = app.RollDice('4d6')
        for i in range(num_gems):
          gem_roll = app.RollDice('1d100')
          gem = self.DetermineGemValue(gem_roll)
          goods = self.AddTreasures(goods, gem)
      elif (diceroll >= 65):
        num_art = app.RollDice('2d10')
        for i in range(num_art):
          art_roll = app.RollDice('1d100')
          art = self.DetermineArtValue(art_roll)
          goods = self.AddTreasures(goods, art)
    elif (EL == 17):
      if (diceroll >= 5) and (diceroll <= 63):
        num_gems = app.RollDice('4d8')
        for i in range(num_gems):
          gem_roll = app.RollDice('1d100')
          gem = self.DetermineGemValue(gem_roll)
          goods = self.AddTreasures(goods, gem)
      elif (diceroll >= 64):
        num_art = app.RollDice('3d8')
        for i in range(num_art):
          art_roll = app.RollDice('1d100')
          art = self.DetermineArtValue(art_roll)
          goods = self.AddTreasures(goods, art)
    elif (EL == 18):
      if (diceroll >= 5) and (diceroll <= 54):
        num_gems = app.RollDice('3d12')
        for i in range(num_gems):
          gem_roll = app.RollDice('1d100')
          gem = self.DetermineGemValue(gem_roll)
          goods = self.AddTreasures(goods, gem)
      elif (diceroll >= 55):
        num_art = app.RollDice('3d10')
        for i in range(num_art):
          art_roll = app.RollDice('1d100')
          art = self.DetermineArtValue(art_roll)
          goods = self.AddTreasures(goods, art)
    elif (EL == 19):
      if (diceroll >= 4) and (diceroll <= 50):
        num_gems = app.RollDice('6d6')
        for i in range(num_gems):
          gem_roll = app.RollDice('1d100')
          gem = self.DetermineGemValue(gem_roll)
          goods = self.AddTreasures(goods, gem)
      elif (diceroll >= 51):
        num_art = app.RollDice('6d6')
        for i in range(num_art):
          art_roll = app.RollDice('1d100')
          art = self.DetermineArtValue(art_roll)
          goods = self.AddTreasures(goods, art)
    elif (EL == 20):
      if (diceroll >= 3) and (diceroll <= 38):
        num_gems = app.RollDice('4d10')
        for i in range(num_gems):
          gem_roll = app.RollDice('1d100')
          gem = self.DetermineGemValue(gem_roll)
          goods = self.AddTreasures(goods, gem)
      elif (diceroll >= 39):
        num_art = app.RollDice('7d6')
        for i in range(num_art):
          art_roll = app.RollDice('1d100')
          art = self.DetermineArtValue(art_roll)
          goods = self.AddTreasures(goods, art)

    return goods

  def OnHelp(self, evt):
    text = "The description is used as the icon popup text.\n\nTreasures are generated according to the random tables found in the d20 SRD.  You may change any of the values in the text fields.  Press the OK button to save the treasure in an icon on the map."
    dlg = HelpDialog(self, text)
    dlg.ShowModal()
    dlg.Destroy()
    return

#-----------------------------------------------------------
#--------------End of TreasuresDialog class-----------------
#-----------------------------------------------------------

class Spells5EDialogCore(PyMapperDialogs.Spellbook5EBase):
  def __init__(self, Parent, selector=False):
    """selector = True when coming from the icon editor"""
    olddir = os.getcwd()
    os.chdir(gv.root_directory)  #this is necessary so that bitmap paths are read by the dialog code correctly
    PyMapperDialogs.Spellbook5EBase.__init__(self, parent=Parent)
    os.chdir(olddir)
    
    #populate the spell list
    self.RefreshSpellList()
    return
  
  def RefreshSpellList(self, event=None):
    self.lbSpellList.Clear()
    """Filter and refresh the spell list"""
    #check if any filters are active
    levelFilters = ()
    filterItemsLevel = False
    classFilters = ()
    filterItemsClass = False
    schoolFilters = ()
    filterItemsSchool = False
    filterItemsBasic = False
    
    targetFilterValue = 0
    if (self.cbLevelFilter.IsChecked()):
      #filter by level
      levelFilters = self.lbLevelFilter.GetSelections()
      filterItemsLevel = True
      targetFilterValue += 1
    if (self.cbClassFilter.IsChecked()):
      #filter by class
      cFilters = self.lbClassFilter.GetSelections() #returns a tuple of index numbers
      classFilters = []
      for i in cFilters:  #convert filters to text; that is what is stored in the spellList
        classFilters.append(self.lbClassFilter.GetString(i))
      
      filterItemsClass = True
      targetFilterValue += 2
    if (self.cbSchoolFilter.IsChecked()):
      #filter by school
      sFilters = self.lbSchoolFilter.GetSelections()
      schoolFilters = []
      for i in sFilters:
        schoolFilters.append(self.lbSchoolFilter.GetString(i))
        
      filterItemsSchool = True
      targetFilterValue += 4
    if (self.cbBasicRules.IsChecked()):
      filterItemsBasic = True
      targetFilterValue += 8
      
    spell = srd.Spell5E_Record()
    
    for spell in gv.Spells5E:
      if (spell.deleted):
        spell.show = False
        continue
      if ((not filterItemsBasic) and (not filterItemsLevel) and (not filterItemsClass) and (not filterItemsSchool)):
        #filters were all turned off, show all spells
        spell.show = True
        self.lbSpellList.Append(spell.Name)
      else:
        spell.show = False
        spell.filterValue = 0 #by default, not shown when filters are active
      
        for LVL in levelFilters:
          if (spell.Level == LVL):
            spell.filterValue += 1
        for CLS in classFilters:
          if (CLS in spell.CasterClass):
            spell.filterValue += 2
            break
        for SCH in schoolFilters:
          if (spell.School == SCH):
            spell.filterValue += 4
            break
        if (spell.BasicSpell and filterItemsBasic):
          spell.filterValue += 8
          
        if (spell.filterValue == targetFilterValue):
          spell.show = True
          self.lbSpellList.Append(spell.Name)
    return
  
  def ClearDetailFields(self, event=None):
    #reset all fields to default/empty values
    self.txSpellName.SetValue("")
    self.cxSpellLevel.SetSelection(0)
    self.lbClassType1.DeselectAll()
    self.lbClassType2.DeselectAll()
    self.cxMagicSchool.SetSelection(0)
    self.cbBasicSpell.SetValue(False)
    self.cbRitualSpell.SetValue(False)
    self.txCastingTime.SetValue("")
    self.txSpellRange.SetValue("")
    self.cbVerbal.SetValue(False)
    self.cbSomatic.SetValue(False)
    self.cbMaterial.SetValue(False)
    self.cbFocus.SetValue(False)
    self.txSpellDuration.SetValue("")
    self.txDamage.SetValue("")
    self.txDescription.SetValue("")
    self.stSourceText.SetLabel("")
    return
  
  def OnListBoxSelect(self, event):
    self.ClearDetailFields()
    selection = self.lbSpellList.GetStringSelection()
    if (selection == wx.NOT_FOUND):
      return False
    spell = srd.Spell5E_Record()
    for spell in gv.Spells5E:
      if (spell.Name == selection):
        break
      
    self.bDeleteSpell.Enable(spell.UserDefined)  #only allow user-defined spells to be deleted
    
    if (spell.Level == 0):
      description = spell.School + " Cantrip"
    elif (spell.Level == 1):
      description = "1st Level " + spell.School + " Spell"
    elif (spell.Level == 2):
      description = "2nd Level " + spell.School + " Spell"
    elif (spell.Level == 3):
      description = "3rd Level " + spell.School + " Spell"
    else:
      description = str(spell.Level) + "th Level " + spell.School + " Spell"
    self.stSpellDescriptor.SetLabel(description)
    
      
    self.txSpellName.SetValue(spell.Name)
    self.cxSpellLevel.SetSelection(spell.Level)
    for cls in spell.CasterClass:
      self.lbClassType1.SetStringSelection(cls)
      self.lbClassType2.SetStringSelection(cls)
    self.cxMagicSchool.SetStringSelection(spell.School)
    self.cbBasicSpell.SetValue(spell.BasicSpell)
    self.cbRitualSpell.SetValue(spell.Ritual)
    self.cbConcentrationSpell.SetValue(spell.Concentration)
    self.txCastingTime.SetValue(spell.CastTime)
    self.txSpellRange.SetValue(spell.SpellRange)
    self.cbVerbal.SetValue(spell.VerbalComponent)
    self.cbSomatic.SetValue(spell.SomaticComponent)
    self.cbMaterial.SetValue(spell.MaterialComponent)
    self.cbFocus.SetValue(spell.FocusComponent)
    self.txSpellDuration.SetValue(spell.Duration)
    self.txDamage.SetValue(spell.BaseDamage)
    self.txDescription.SetValue(spell.Description)
    self.stSourceText.SetLabel(spell.SourceMaterial)
    return True
  
  def AddNewSpell(self, event):
    spell = srd.Spell5E_Record()
    
    spell.Name = self.txSpellName.GetValue()
    for i in gv.Spells5E:
      if (i.Name == spell.Name):
        note = "Spell must have a unique name.  "+spell.Name+ " is already in the spellbook."
        wx.MessageBox(note)
        return
    spell.School = self.cxMagicSchool.GetStringSelection()
    for i in self.lbClassType1.GetSelections():
      spell.CasterClass.append(self.lbClassType1.GetString(i))
    for i in self.lbClassType2.GetSelections():
      spell.CasterClass.append(self.lbClassType2.GetString(i))
    spell.Level = self.cxSpellLevel.GetSelection()
    spell.VerbalComponent = self.cbVerbal.IsChecked()
    spell.MaterialComponent = self.cbMaterial.IsChecked()
    spell.SomaticComponent = self.cbSomatic.IsChecked()
    spell.FocusComponent = self.cbFocus.IsChecked()
    spell.CastTime = self.txCastingTime.GetValue()
    spell.SpellRange = self.txSpellRange.GetValue()
    spell.Target = 'None'
    spell.Duration = self.txSpellDuration.GetValue()
    spell.Concentration = self.cbConcentrationSpell.IsChecked()
    spell.BaseDamage = self.txDamage.GetValue()
    spell.DamageType = self.cxDamageType.GetStringSelection()
    spell.Description = self.txDescription.GetValue()
    spell.Ritual = self.cbRitualSpell.IsChecked()
    spell.BasicSpell = False
    spell.SourceMaterial = "User Defined Spell"
    spell.SourceCode = 'USER'
    spell.UserDefined = True
    spell.selected = False
    spell.filterValue = 15
    spell.MasterIndex = gv.UserSpell5E_NextIndex
    gv.UserSpell5E_NextIndex += 1
    gv.Spells5E.append(spell)
    
    self.RefreshSpellList()
    return
  
  def UpdateCurrentSpell(self, event):
    """Updates currently selected spell to new field values"""
    
    spell = srd.Spell5E_Record()
    selection = self.lbSpellList.GetStringSelection()
    
    for spell in gv.Spells5E:
      if (selection == spell.Name):
        break
    spell.Name = self.txSpellName.GetValue()
    spell.School = self.cxMagicSchool.GetStringSelection()
    for i in self.lbClassType1.GetSelections():
      spell.CasterClass.append(self.lbClassType1.GetString(i))
    for i in self.lbClassType2.GetSelections():
      spell.CasterClass.append(self.lbClassType2.GetString(i))
    spell.Level = self.cxSpellLevel.GetSelection()
    spell.VerbalComponent = self.cbVerbal.IsChecked()
    spell.MaterialComponent = self.cbMaterial.IsChecked()
    spell.SomaticComponent = self.cbSomatic.IsChecked()
    spell.FocusComponent = self.cbFocus.IsChecked()
    spell.CastTime = self.txCastingTime.GetValue()
    spell.SpellRange = self.txSpellRange.GetValue()
    spell.Target = 'None'
    spell.Duration = self.txSpellDuration.GetValue()
    spell.Concentration = self.cbConcentrationSpell.IsChecked()
    spell.BaseDamage = self.txDamage.GetValue()
    spell.DamageType = self.cxDamageType.GetStringSelection()
    spell.Description = self.txDescription.GetValue()
    spell.Ritual = self.cbRitualSpell.IsChecked()
    spell.BasicSpell = False
    spell.SourceMaterial = "User Defined Spell"
    spell.SourceCode = 'USER'

    return
  
  def DeleteUserSpell(self, event):
    """Only user-defined spells can be deleted"""
    selection = self.lbSpellList.GetStringSelection()
    if (selection == wx.NOT_FOUND):
      return False
    spell = srd.Spell5E_Record()
    for spell in gv.Spells5E:
      if (spell.Name == selection):
        break
    note = "Are you sure you want to delete " + spell.Name + " from the spellbook?"
    warning = wx.MessageDialog(self, note, "Confirm deletion", wx.YES_NO | wx.ICON_WARNING)
    result = warning.ShowModal()
    if (result ==  wx.ID_CANCEL):
      return
    
    spell.deleted = True
    self.RefreshSpellList()
    return
  
  def FilterBasicSpells(self, event):
    self.RefreshSpellList()
    return

  def FilterByClass(self, event):
    if (self.cbClassFilter.IsChecked()):
      self.lbClassFilter.Enable(True)
    else:
      self.lbClassFilter.Enable(False)
    self.RefreshSpellList()
    return
  
  def FilterByLevel(self,event):
    if (self.cbLevelFilter.IsChecked()):
      self.lbLevelFilter.Enable(True)
    else:
      self.lbLevelFilter.Enable(False)
    self.RefreshSpellList()
    return
  
  def FilterBySchool(self, event):
    if (self.cbSchoolFilter.IsChecked()):
      self.lbSchoolFilter.Enable(True)
    else:
      self.lbSchoolFilter.Enable(False)
    self.RefreshSpellList()
    return
  
  def OnOK(self, event):
    self.Show(False)  #.Show(False) is used instead of EndModal because it is a modeless dialog
    return
  
  def OnCancel(self, event):
    self.Show(False)
    return
  
#--------------------------------------------------------------------------

class IconEditorFrame(PyMapperDialogs.IconEditorBase):
  def __init__(self, par, caption, room, position, text=None):
    olddir = os.getcwd()
    os.chdir(gv.root_directory)  #this is necessary so that bitmap paths are read by the dialog code correctly
    PyMapperDialogs.IconEditorBase.__init__(self, parent=par)
    self.SetTitle(room.Description)
    self.Move(room.windowPosition)
    os.chdir(olddir)
    self.room = room
    wx.CallAfter(self.rtc.SetFocus)
    if (gv.d20_SRD_data_available):
      self.mRpg.Enable(PyMapperDialogs.NPC_menuID, True)
      self.mRpg.Enable(PyMapperDialogs.Trap_menuID, True)
      self.mRpg.Enable(PyMapperDialogs.Monster_menuID, True)
      self.mRpg.Enable(PyMapperDialogs.Treasure_menuID, True)
      self.mRpg.Enable(PyMapperDialogs.NPC5E_menuID, True)
      self.mRpg.Enable(PyMapperDialogs.Monster5E_menuID, True)
    else:
      self.mRpg.Enable(PyMapperDialogs.NPC_menuID, False)
      self.mRpg.Enable(PyMapperDialogs.Trap_menuID, False)
      self.mRpg.Enable(PyMapperDialogs.Monster_menuID, False)
      self.mRpg.Enable(PyMapperDialogs.Treasure_menuID, False)
      self.mRpg.Enable(PyMapperDialogs.NPC5E_menuID, False)
      self.mRpg.Enable(PyMapperDialogs.Monster5E_menuID, False)

    if (room.IconType == 'Trap'):
      self.tbIconTools.ToggleTool(PyMapperDialogs.trapID, True)
    elif (room.IconType == 'Monster'):
      self.tbIconTools.ToggleTool(PyMapperDialogs.monsterID, True)
    elif (room.IconType == 'Room'):
      self.tbIconTools.ToggleTool(PyMapperDialogs.roomID, True)
    elif (room.IconType == 'NPC'):
      self.tbIconTools.ToggleTool(PyMapperDialogs.npcID, True)
    elif (room.IconType == 'Treasure'):
      self.tbIconTools.ToggleTool(PyMapperDialogs.treasureID, True)
    elif (room.IconType == 'Marker'):
      self.tbIconTools.ToggleTool(PyMapperDialogs.markerID, True)
      if (room.Marker):
        self.SetStatusText("Marker "+room.Marker.name+" is set for map window display", 1)  
    self.cxIconSize.SetSelection(self.room.IconSize-1)  #subtract 1 since the selection is 0 based
    
    rt.RichTextBuffer.AddHandler(rt.RichTextHTMLHandler())
    rt.RichTextBuffer.AddHandler(rt.RichTextXMLHandler())
    # This is needed for the view as HTML option since we tell it to store the images in the memory file system.
    wx.FileSystem.AddHandler(wx.MemoryFSHandler())
    self.rtc.GetBuffer().Modify(False)
    gv.rtc_open = True
    gv.rtc_icon = room
    self.monsterUniqueID = None
    if (room.xml_file):
      #check for the file in the given path
      testPath1 = os.path.join(room.xml_path,room.xml_file)
      if (not(os.access(testPath1, os.F_OK))):
        #if not in the given path, try the folder where the map was located
        tempPath = os.path.join(gv.maps_directory, room.xml_file)
        if (not(os.access(tempPath, os.F_OK))):
          #could not find either path
          path_dlg = wx.DirDialog(self, message="Could not find source directory for room file",defaultPath=gv.maps_directory)
          found = path_dlg.ShowModal()
          if (not found):
            #skip loading this room
            logging.error("Could not find path for the XML file:%s %s", room.xml_path, room.xml_file)
            return
          else:
            room.xml_path = path_dlg.GetPath()
            path_dlg.Destroy()
        else:
          room.xml_path = gv.maps_directory
      self.LoadFile(room.xml_path, room.xml_file)
      self.rtc.SetCaretPosition(self.rtc.GetLastPosition())
      self.SetStatusText("Currently editing: " + room.xml_file)
    else:
      self.SetStatusText("Filename not set")
    if (text):
      self.rtc.WriteText(text)
      self.room.npc = self.ReadTags(text)
    return
  
  def ReadTags(self, text):
    """Read the :: tags for NPC or Monster information"""
    npc = srd.NPC_Record()

    for line in text:
      data = line.split("::")
      index = 0
      for item in data:
        if (item == 'AC'):
          npc.AC = int(data[index+1])
        elif (item == 'HP'):
          npc.HP = int(data[index+1])
        elif (item == 'monsterID'):
          self.monsterUniqueID = int(data[index+1])
          for monster in gv.MonsterList:
            if (monster.uniqueID == self.monsterUniqueID):
              self.room.monster = monster
              self.tbIconTools.ToggleTool(PyMapperDialogs.monsterID, True)
              break
        index += 1
    return

  def SetFontStyle(self, fontColor = None, fontBgColor = None, fontFace = None, fontSize = None,
                   fontBold = None, fontItalic = None, fontUnderline = None):
    if fontColor:
      self.textAttr.SetTextColour(fontColor)
    if fontBgColor:
      self.textAttr.SetBackgroundColour(fontBgColor)
    if fontFace:
      self.textAttr.SetFontFaceName(fontFace)
    if fontSize:
      self.textAttr.SetFontSize(fontSize)
    if fontBold != None:
      if fontBold:
        self.textAttr.SetFontWeight(wx.FONTWEIGHT_BOLD)
      else:
        self.textAttr.SetFontWeight(wx.FONTWEIGHT_NORMAL)
    if fontItalic != None:
      if fontItalic:
        self.textAttr.SetFontStyle(wx.FONTSTYLE_ITALIC)
      else:
        self.textAttr.SetFontStyle(wx.FONTSTYLE_NORMAL)
    if fontUnderline != None:
      if fontUnderline:
        self.textAttr.SetFontUnderlined(True)
      else:
        self.textAttr.SetFontUnderlined(False)
    self.rtc.SetDefaultStyle(self.textAttr)
    return

  def OnURL(self, evt):
    wx.MessageBox(evt.GetString(), "URL Clicked")
    return

  def LoadFile(self, folder, filename):
    if (os.access(filename, os.F_OK)):  #does the file exist in the current folder?
      self.rtc.LoadFile(filename)
    else:
      loadpath = os.path.join(folder, filename)
      if (os.access(loadpath, os.F_OK)):  #if not, try the path+file
        self.rtc.LoadFile(loadpath)
      else:
        logging.error("Could not find folder or file to load: %s %s", folder, filename)
    self.rtc.GetBuffer().Modify(False)
    return

  def OnFileOpen(self, evt):
    dlg = wx.FileDialog(self, "Choose a filename", wildcard=xml_wildcard, style=wx.OPEN)
    if dlg.ShowModal() == wx.ID_OK:
      path = dlg.GetPath()
      file_name = dlg.GetFilename()
      folder_name = dlg.GetDirectory()
      if path:
        self.rtc.LoadFile(folder_name+"/"+file_name)
        self.rtc.GetBuffer().Modify(False)
        self.room.xml_file = file_name
        self.room.xml_path = folder_name
        try:
          textfile = open(path)
        except IOError:
          logging.critical("IconEditorFrame::OnFileOpen   Could not open file %s'", path)
          return False
        self.room.npc = self.ReadTags(textfile)
    dlg.Destroy()
    return

  def OnFilePrint(self, evt):
    rt_printing = rt.RichTextPrinting()
    rt_buffer = self.rtc.GetBuffer()
    rt_printing.PrintBuffer(rt_buffer)
    return

  def OnFileSave(self, evt):
    if not self.rtc.GetFilename():
      self.OnFileSaveAs(evt)
      return
    self.rtc.SaveFile()
    return

  def OnFileSaveAs(self, evt):
    dlg = wx.FileDialog(self, "Choose a filename", wildcard=xml_wildcard,
                        defaultDir = gv.encounters_directory, defaultFile=self.room.Description,
                        style=wx.SAVE | wx.FD_OVERWRITE_PROMPT)
    if dlg.ShowModal() == wx.ID_OK:
      path = dlg.GetPath()
      if path:
        self.rtc.SaveFile(path)
        self.room.xml_file = dlg.GetFilename()
        self.room.xml_path = dlg.GetDirectory()
        gv.encounters_directory = dlg.GetDirectory()
    dlg.Destroy()
    return

  def OnFileViewHTML(self, evt):
    # Get an instance of the html file handler, use it to save the
    # document to a StringIO stream, and then display the
    # resulting html text in a dialog with a HtmlWindow.
    handler = rt.RichTextHTMLHandler()
    handler.SetFlags(rt.RICHTEXT_HANDLER_SAVE_IMAGES_TO_MEMORY)
    handler.SetFontSizeMapping([7,9,11,12,14,22,100])

    import cStringIO
    stream = cStringIO.StringIO()
    if not handler.SaveStream(self.rtc.GetBuffer(), stream):
      return

    import wx.html
    dlg = wx.Dialog(self, title="HTML", style=wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER)
    html = wx.html.HtmlWindow(dlg, size=(500,400), style=wx.BORDER_SUNKEN)
    html.SetPage(stream.getvalue())
    btn = wx.Button(dlg, wx.ID_CANCEL)
    sizer = wx.BoxSizer(wx.VERTICAL)
    sizer.Add(html, 1, wx.ALL|wx.EXPAND, 5)
    sizer.Add(btn, 0, wx.ALL|wx.CENTER, 10)
    dlg.SetSizer(sizer)
    sizer.Fit(dlg)
    dlg.ShowModal()
    handler.DeleteTemporaryImages()
    return

  def OnFileExit(self, evt):
    if (self.rtc.IsModified()):
      warning = wx.MessageDialog(self, "Save Room Description?", "", wx.YES_NO |wx.CANCEL | wx.ICON_QUESTION)
      result = warning.ShowModal()
      if (result == wx.ID_YES):
        self.OnFileSave(evt)
      elif (result == wx.ID_CANCEL):
        return
    if (self.tbIconTools.GetToolState(PyMapperDialogs.roomID)):
      self.room.Icon = app.RoomIcon
      self.room.IconType = 'Room'
    elif (self.tbIconTools.GetToolState(PyMapperDialogs.monsterID)):
      self.room.Icon = app.MonsterIcon
      self.room.IconType = 'Monster'
      if (not self.room.monster): #Monster icon choosen, but no info
        pass
    elif (self.tbIconTools.GetToolState(PyMapperDialogs.trapID)):
      self.room.Icon = app.TrapIcon
      self.room.IconType = 'Trap'
    elif (self.tbIconTools.GetToolState(PyMapperDialogs.npcID)):
      self.room.Icon = app.NPC_Icon
      self.room.IconType = 'NPC'
    elif (self.tbIconTools.GetToolState(PyMapperDialogs.treasureID)):
      self.room.Icon = app.TreasureIcon
      self.room.IconType = 'Treasure'
    elif (self.tbIconTools.GetToolState(PyMapperDialogs.markerID)):
      self.room.IconType = 'Marker'
    #update window to current position on screen
    self.room.windowPosition = self.GetPosition()
    self.Close(True)
    self.Destroy()
    gv.rtc_open = False
    app.DrawMapWindow()
    return

  def OnBold(self, evt):
    self.rtc.ApplyBoldToSelection()
    return

  def OnItalic(self, evt): 
    self.rtc.ApplyItalicToSelection()
    return

  def OnUnderline(self, evt):
    self.rtc.ApplyUnderlineToSelection()
    return

  def OnAlignLeft(self, evt):
    self.rtc.ApplyAlignmentToSelection(wx.TEXT_ALIGNMENT_LEFT)
    return

  def OnAlignRight(self, evt):
    self.rtc.ApplyAlignmentToSelection(wx.TEXT_ALIGNMENT_RIGHT)
    return

  def OnAlignCenter(self, evt):
    self.rtc.ApplyAlignmentToSelection(wx.TEXT_ALIGNMENT_CENTRE)
    return

  def OnIndentMore(self, evt):
    attr = rt.TextAttrEx()
    attr.SetFlags(wx.TEXT_ATTR_LEFT_INDENT)
    ip = self.rtc.GetInsertionPoint()
    if self.rtc.GetStyle(ip, attr):
      r = rt.RichTextRange(ip, ip)
      if self.rtc.HasSelection():
        r = self.rtc.GetSelectionRange()

      attr.SetLeftIndent(attr.GetLeftIndent() + 100)
      attr.SetFlags(wx.TEXT_ATTR_LEFT_INDENT)
      self.rtc.SetStyle(r, attr)
    return

  def OnIndentLess(self, evt):
    attr = rt.TextAttrEx()
    attr.SetFlags(wx.TEXT_ATTR_LEFT_INDENT)
    ip = self.rtc.GetInsertionPoint()
    if self.rtc.GetStyle(ip, attr):
      r = rt.RichTextRange(ip, ip)
      if self.rtc.HasSelection():
        r = self.rtc.GetSelectionRange()

    if attr.GetLeftIndent() >= 100:
      attr.SetLeftIndent(attr.GetLeftIndent() - 100)
      attr.SetFlags(wx.TEXT_ATTR_LEFT_INDENT)
      self.rtc.SetStyle(r, attr)
    return

  def OnParagraphSpacingMore(self, evt):
    attr = rt.TextAttrEx()
    attr.SetFlags(wx.TEXT_ATTR_PARA_SPACING_AFTER)
    ip = self.rtc.GetInsertionPoint()
    if self.rtc.GetStyle(ip, attr):
      r = rt.RichTextRange(ip, ip)
      if self.rtc.HasSelection():
        r = self.rtc.GetSelectionRange()
      attr.SetParagraphSpacingAfter(attr.GetParagraphSpacingAfter() + 20);
      attr.SetFlags(rt.TEXT_ATTR_PARA_SPACING_AFTER)
      self.rtc.SetStyle(r, attr)
    return

  def OnParagraphSpacingLess(self, evt):
    attr = rt.TextAttrEx()
    attr.SetFlags(wx.TEXT_ATTR_PARA_SPACING_AFTER)
    ip = self.rtc.GetInsertionPoint()
    if self.rtc.GetStyle(ip, attr):
      r = rt.RichTextRange(ip, ip)
      if self.rtc.HasSelection():
        r = self.rtc.GetSelectionRange()
      if attr.GetParagraphSpacingAfter() >= 20:
        attr.SetParagraphSpacingAfter(attr.GetParagraphSpacingAfter() - 20);
        attr.SetFlags(rt.TEXT_ATTR_PARA_SPACING_AFTER)
        self.rtc.SetStyle(r, attr)
    return

  def OnLineSpacingSingle(self, evt): 
    attr = rt.TextAttrEx()
    attr.SetFlags(rt.TEXT_ATTR_LINE_SPACING)
    ip = self.rtc.GetInsertionPoint()
    if self.rtc.GetStyle(ip, attr):
      r = rt.RichTextRange(ip, ip)
      if self.rtc.HasSelection():
        r = self.rtc.GetSelectionRange()
      attr.SetFlags(wx.TEXT_ATTR_LINE_SPACING)
      attr.SetLineSpacing(10)
      self.rtc.SetStyle(r, attr)
    return

  def OnLineSpacingHalf(self, evt):
    attr = rt.TextAttrEx()
    attr.SetFlags(rt.TEXT_ATTR_LINE_SPACING)
    ip = self.rtc.GetInsertionPoint()
    if self.rtc.GetStyle(ip, attr):
      r = rt.RichTextRange(ip, ip)
      if self.rtc.HasSelection():
        r = self.rtc.GetSelectionRange()
      attr.SetFlags(wx.TEXT_ATTR_LINE_SPACING)
      attr.SetLineSpacing(15)
      self.rtc.SetStyle(r, attr)
    return

  def OnLineSpacingDouble(self, evt):
    attr = rt.TextAttrEx()
    attr.SetFlags(rt.TEXT_ATTR_LINE_SPACING)
    ip = self.rtc.GetInsertionPoint()
    if self.rtc.GetStyle(ip, attr):
      r = rt.RichTextRange(ip, ip)
      if self.rtc.HasSelection():
        r = self.rtc.GetSelectionRange()
      attr.SetFlags(rt.TEXT_ATTR_LINE_SPACING)
      attr.SetLineSpacing(20)
      self.rtc.SetStyle(r, attr)
    return

  def OnFont(self, evt):
    if not self.rtc.HasSelection():
      return
    r = self.rtc.GetSelectionRange()
    fontData = wx.FontData()
    fontData.EnableEffects(False)
    attr = rt.TextAttrEx()
    attr.SetFlags(wx.TEXT_ATTR_FONT)
    if self.rtc.GetStyle(self.rtc.GetInsertionPoint(), attr):
      fontData.SetInitialFont(attr.GetFont())
    dlg = wx.FontDialog(self, fontData)
    if dlg.ShowModal() == wx.ID_OK:
      fontData = dlg.GetFontData()
      font = fontData.GetChosenFont()
      if font:
        attr.SetFlags(wx.TEXT_ATTR_FONT)
        attr.SetFont(font)
        self.rtc.SetStyle(r, attr)
    dlg.Destroy()
    return
  
  def SetIconSize(self, event):
    self.room.IconSize = (self.cxIconSize.GetSelection())+1  #add 1, since the selection is 0 based
    return
  
  def ForwardEvent(self, evt):
    # The RichTextCtrl can handle menu and update events for undo,
    # redo, cut, copy, paste, delete, and select all, so just
    # forward the event to it.
    self.rtc.ProcessEvent(evt)
    return

  def OnColour(self, evt):
    colourData = wx.ColourData()
    attr = rt.TextAttrEx()
    attr.SetFlags(wx.TEXT_ATTR_TEXT_COLOUR)
    if self.rtc.GetStyle(self.rtc.GetInsertionPoint(), attr):
      colourData.SetColour(attr.GetTextColour())

    dlg = wx.ColourDialog(self, colourData)
    if dlg.ShowModal() == wx.ID_OK:
      colourData = dlg.GetColourData()
      colour = colourData.GetColour()
      if colour:
        if not self.rtc.HasSelection():
          self.rtc.BeginTextColour(colour)
        else:
          r = self.rtc.GetSelectionRange()
          attr.SetFlags(wx.TEXT_ATTR_TEXT_COLOUR)
          attr.SetTextColour(colour)
          self.rtc.SetStyle(r, attr)
    dlg.Destroy()
    return

  def OnUpdateBold(self, evt):
    self.rtc.ApplyBoldToSelection()
    return

  def OnUpdateItalic(self, evt): 
    self.rtc.ApplyItalicToSelection()
    return

  def OnUpdateUnderline(self, evt): 
    self.rtc.ApplyUnderlineToSelection()
    return

  def OnUpdateAlignLeft(self, evt):
    self.rtc.ApplyAlignmentToSelection(wx.TEXT_ALIGNMENT_LEFT)
    return

  def OnUpdateAlignCenter(self, evt):
    self.rtc.ApplyAlignmentToSelection(wx.TEXT_ALIGNMENT_CENTRE)
    return

  def OnUpdateAlignRight(self, evt):
    self.rtc.ApplyAlignmentToSelection(wx.TEXT_ALIGNMENT_RIGHT)
    return

  def EditDescription(self, event):
    dlg = wx.TextEntryDialog(parent=self, message="Enter new description:",
                             caption="Change Icon Text Description",
                             defaultValue=self.room.Description)
    if (dlg.ShowModal() == wx.ID_OK):
      self.room.Description = dlg.GetValue()
      self.SetLabel(self.room.Description)
    dlg.Destroy()
    return

  def AddTrap(self, event):
    dlg = TrapsDialog(self)
    dlg.ID_OK.SetLabel("Select Trap")
    dlg.bAddTrap.Show(False)
    dlg.bDeleteTrap.Show(False)
    dlg.bClearSelection.Show(False)
    dlg.bUpdateSelectedTrap.Show(False)
    result = dlg.ShowModal()
    if (result == True):
      text = dlg.PrintStatBlock(dlg.selected_trap)
      self.rtc.WriteText(text)
      self.tbIconTools.ToggleTool(PyMapperDialogs.trapID, True)
      if (dlg.selected_trap != None):
        self.room.trap = dlg.selected_trap
      else:
        self.room.trap = None
    dlg.Destroy()
    return

  def AddNPC(self, event):
    dlg = NPC_GeneratorDialog(self)
    result = dlg.ShowModal()
    if (result == True):
      text = dlg.PrintStatBlock(dlg.CompiledNPC)
      self.rtc.WriteText(text)
      self.room.npc = dlg.CompiledNPC
      self.tbIconTools.ToggleTool(PyMapperDialogs.npcID, True)
    dlg.Destroy()
    return

  def Add5E_NPC(self, event):
    dlg = Monsters5EDialog(self, '5E_NPC')
    dlg.ID_OK.SetLabel("Select NPC")
    add_npc = dlg.ShowModal()
    if (add_npc) and (dlg.MonsterUniqueID != None):
      self.tbIconTools.ToggleTool(PyMapperDialogs.npcID, True)
      self.rtc.WriteText("::monsterID::"+str(dlg.MonsterUniqueID)+"::")
      self.monsterUniqueID = dlg.MonsterUniqueID
      for room in gv.RoomList:
        if (self.room.Index == room.Index):
          for monster in gv.NPC_5E:
            if (monster.uniqueID == self.monsterUniqueID):
              room.monster = copy.deepcopy(monster)
              break
          break
    dlg.Destroy()
    return

  def Add5E_Monster(self, event):
    dlg = Monsters5EDialog(self, '5E')
    dlg.ID_OK.SetLabel("Select Monster")
    add_monster = dlg.ShowModal()
    if (add_monster) and (dlg.MonsterUniqueID != None):
      self.tbIconTools.ToggleTool(PyMapperDialogs.monsterID, True)
      self.rtc.WriteText("::monsterID::"+str(dlg.MonsterUniqueID)+"::")
      self.monsterUniqueID = dlg.MonsterUniqueID
      for room in gv.RoomList:
        if (self.room.Index == room.Index):
          for monster in gv.Monsters5E:
            if (monster.uniqueID == self.monsterUniqueID):
              room.monster = copy.deepcopy(monster)
              break
          break
    dlg.Destroy()
    return

  def AddMonster(self, event):
    dlg = MonstersDialog(self)
    add_monster = dlg.ShowModal()
    if (add_monster) and (dlg.MonsterUniqueID != None):
      self.tbIconTools.ToggleTool(PyMapperDialogs.monsterID, True)
      self.rtc.WriteText("::monsterID::"+str(dlg.MonsterUniqueID)+"::")
      self.monsterUniqueID = dlg.MonsterUniqueID
      #find the Monster_Record in the master list
          
      for room in gv.RoomList:
        if (self.room.Index == room.Index):
          for monster in gv.MonsterList:
            if (monster.uniqueID == self.monsterUniqueID):
              room.monster = copy.deepcopy(monster)
              break
          break
        
    dlg.Destroy()
    return
  
  def SelectMarker(self):
    dlg = SymbolMarkerManagerDialog(self, app.SymbolList, app.MarkerList, 'MarkersOnly')
    changeMarker = dlg.ShowModal()
    if (dlg.lbMarkers.GetStringSelection() == wx.NOT_FOUND) or (not changeMarker):
      #nothing selected, or cancel selected;  reset icon to room icon
      self.room.IconType = 'Room'
      self.tbIconTools.ToggleTool(PyMapperDialogs.roomID, True)
    else:
      markerSelection = dlg.lbMarkers.GetStringSelection()
      marker = MarkerRecord()
      for marker in app.MarkerList:
        if (marker.name == markerSelection):
          self.room.Icon = marker.image
          self.room.MapRect.width = marker.size*gv.MapZoomFactor
          self.room.MapRect.height = marker.size*gv.MapZoomFactor
          self.room.IconType = 'Marker'
          self.room.Marker = marker
          self.SetStatusText("Marker "+marker.name+" selected for map window display", number=1)
          break
    dlg.Destroy()
    return

  def AddTreasure(self, event):
    dlg = TreasuresDialog(self, open_xml=False)
    dlg.ID_OK.SetLabel("Add to text")
    if (dlg.ShowModal() == True):
      text = dlg.PrintTreasureText()
      self.rtc.WriteText(text)
    return


#End of IconEditorFrame class ----------------------------------------------------------------------

########################################################################
class RoomInfo:
  """Holds information for room descriptions, icon images, etc"""
  #----------------------------------------------------------------------
  def __init__(self):
    """Constructor"""
    self.Icon = None               #wx.Image of the icon displayed on the map
    self.IconType = 'Room'         #set to Room, Trap, NPC, Treasure, Monster, or Marker; defines which icon to display
    self.IconSize = 1              #How big of icon to display on the map(1 = 1x1, 2 = 2x2, etc.  Max 5x5)
    self.Description = None        #Used as a 'title' on the RichTextCtrl frame
    self.Index = len(gv.RoomList)  #unique ID of the RoomInfo
    self.Layer = 0                 #which layer index to display on.
    self.MapRect = wx.Rect2D(0,0,0,0) #current position and size on the map
    self.x = 0.0                   #float value.  Multiply by ZoomFactor to get position
    self.y = 0.0                   #float value.  Multiply by ZoomFactor to get position
    self.selected = False
    self.xml_file = False          #name of the file if saved
    self.xml_path = None           #name of the secondary search path
    self.placed = False            #True if placed on the map, False if held in memory
    self.page = None               #Mapbook pagename where located for display
    self.npc = None                #NPC_Record information
    self.windowPosition = wx.Point(100,100)  #default editor position on the screen
    self.windowSize = None         #wx.Size()    size of the room, if changed from default
    self.Marker = None             #if assigned, this is the MarkerRecord in app.MarkerList
    self.monster = None            #Monster5E_Record;  also includes 5E NPC's
    self.trap = None               #srd.TrapInfo record
    self.highlightColor = wx.Colour(255,255,0,255)  #yellow background color
    return

  def __deepcopy__(self, source):
    newRoom = RoomInfo()
    newRoom.Icon = source.Icon
    newRoom.IconType = source.IconType
    newRoom.IconSize = source.IconSize
    newRoom.Description = source.Description
    newRoom.Layer = source.Layer
    newRoom.MapRect = wx.Rect2D()
    newRoom.MapRect.x = source.MapRect.x
    newRoom.MapRect.y = source.MapRect.y
    newRoom.MapRect.width = source.MapRect.width
    newRoom.MapRect.height = source.MapRect.height
    newRoom.x = source.x
    newRoom.y = source.y
    newRoom.selected = source.selected
    newRoom.xml_file = source.xml_file
    newRoom.xml_path = source.xml_path
    newRoom.placed = source.placed
    newRoom.monster = source.monster
    newRoom.highlightColor = source.highlightColor
    return newRoom

#-----------------------------------------------------------------------

class TreasureItem:
  def __init__(self):
    self.description = None
    self.cp = 0
    self.sp = 0
    self.gp = 0
    self.pp = 0
    self.goods = []
    self.magic = []
    self.other = []
    self.gem10 = []
    self.gem50 = []
    self.gem100 = []
    self.gem500 = []
    self.gem1000 = []
    self.gem5000 = []
    self.ArtList55 = []
    self.ArtList105 = []
    self.ArtList350 = []
    self.ArtList550 = []
    self.ArtList700 = []
    self.ArtList1050 = []
    self.ArtList1400 = []
    self.ArtList1750 = []
    self.ArtList2500 = []
    self.ArtList3500 = []
    self.ArtList5000 = []
    self.ArtList7000 = []
    return


class ConditionColorsDialog(PyMapperDialogs.ConditionsLegendBase):
  def __init__(self, parent):
    PyMapperDialogs.ConditionsLegendBase.__init__(self, parent)
    self.cpkBlinded.SetColour(gv.ConditionColors.BlindedColor)
    self.cpkCharmed.SetColour(gv.ConditionColors.CharmedColor)
    self.cpkConcentrating.SetColour(gv.ConditionColors.ConcentratingColor)
    self.cpkDeafened.SetColour(gv.ConditionColors.DeafenedColor)
    self.cpkFrightened.SetColour(gv.ConditionColors.FrightenedColor)
    self.cpkGrappled.SetColour(gv.ConditionColors.GrappledColor)
    self.cpkIncapacitated.SetColour(gv.ConditionColors.IncapacitatedColor)
    self.cpkInvisible.SetColour(gv.ConditionColors.InvisibleColor)
    self.cpkParalyzed.SetColour(gv.ConditionColors.ParalyzedColor)
    self.cpkPetrified.SetColour(gv.ConditionColors.PetrifiedColor)
    self.cpkPoisoned.SetColour(gv.ConditionColors.PoisonedColor)
    self.cpkRestrained.SetColour(gv.ConditionColors.RestrainedColor)
    self.cpkStunned.SetColour(gv.ConditionColors.StunnedColor)
    self.cpkTurned.SetColour(gv.ConditionColors.TurnedColor)
    self.cpkUnconscious.SetColour(gv.ConditionColors.UnconsciousColor)
    return

  def OnCloseDialog(self, event):
    event.Skip()
    self.Destroy()
    app.frame.ConditionColorsDialog = None
    return
  
  def ChangeConditionColor(self, event):
    if (event.GetId() == PyMapperDialogs.idxBlinded):
      gv.ConditionColors.ChangeColor('Blinded', self.cpkBlinded.GetColour())
    elif (event.GetId() == PyMapperDialogs.idxCharmed):
      gv.ConditionColors.ChangeColor('Charmed', self.cpkBlinded.GetColour())
    elif (event.GetId() == PyMapperDialogs.idxConcentrating):
      gv.ConditionColors.ChangeColor('Concentrating', self.cpkBlinded.GetColour())
    elif (event.GetId() == PyMapperDialogs.idxDeafened):
      gv.ConditionColors.ChangeColor('Deafened', self.cpkDeafened.GetColour())
    elif (event.GetId() == PyMapperDialogs.idxFrightened):
      gv.ConditionColors.ChangeColor('Frightened', self.cpkFrightened.GetColour())
    elif (event.GetId() == PyMapperDialogs.idxGrappled):
      gv.ConditionColors.ChangeColor('Grappled', self.cpkGrappled.GetColour())
    elif (event.GetId() == PyMapperDialogs.idxIncapacitated):
      gv.ConditionColors.ChangeColor('Incapacitated', self.cpkIncapacitated.GetColour())
    elif (event.GetId() == PyMapperDialogs.idxInvisible):
      gv.ConditionColors.ChangeColor('Invisible', self.cpkInvisible.GetColour())
    elif (event.GetId() == PyMapperDialogs.idxParalyzed):
      gv.ConditionColors.ChangeColor('Paralyzed', self.cpkParalyzed.GetColour())
    elif (event.GetId() == PyMapperDialogs.idxPetrified):
      gv.ConditionColors.ChangeColor('Petrified', self.cpkPetrified.GetColour())
    elif (event.GetId() == PyMapperDialogs.idxPoisoned):
      gv.ConditionColors.ChangeColor('Poisoned', self.cpkPoisoned.GetColour())
    elif (event.GetId() == PyMapperDialogs.idxProne):
      gv.ConditionColors.ChangeColor('Prone', self.cpkProne.GetColour())
    elif (event.GetId() == PyMapperDialogs.idxRestrained):
      gv.ConditionColors.ChangeColor('Restrained', self.cpkRestrained.GetColour())
    elif (event.GetId() == PyMapperDialogs.idxStunned):
      gv.ConditionColors.ChangeColor('Stunned', self.cpkStunned.GetColour())
    elif (event.GetId() == PyMapperDialogs.idxTurned):
      gv.ConditionColors.ChangeColor('Turned', self.cpkTurned.GetColour())
    elif (event.GetId() == PyMapperDialogs.idxUnconscious):
      gv.ConditionColors.ChangeColor('Unconscious', self.cpkUnconscious.GetColour())
    app.DrawMapWindow()  #call in order to update the colors on screen
    return

class NPC_GeneratorDialog(PyMapperDialogs.NPC_GeneratorDialogBase):
  """The finished NPC_Record is stored in self.CompiledNPC
  """
  def AssignSpells(self, NPC, CasterLevel):
    SpellLevel_0= []
    SpellLevel_1= []
    SpellLevel_2= []
    SpellLevel_3= []
    SpellLevel_4= []
    SpellLevel_5= []
    SpellLevel_6= []
    SpellLevel_7= []
    SpellLevel_8= []
    SpellLevel_9= []

    if (NPC.ClassOne == 'Wizard'):
      NPC.MagicType = 'Sorcerer/Wizard'
    elif (NPC.ClassOne == 'Sorcerer'):
      NPC.MagicType = 'Sorcerer/Wizard'
    elif (NPC.ClassOne == 'Bard'):
      NPC.MagicType = 'Bard'
    elif (NPC.ClassOne == 'Cleric') or (NPC.ClassOne == 'Adept'):
      NPC.MagicType = 'Cleric'
    elif (NPC.ClassOne == 'Druid'):
      NPC.MagicType = 'Druid'
    elif (NPC.ClassOne == 'Paladin') and (NPC.LevelOne >= 4):
      NPC.MagicType = 'Paladin'
    elif (NPC.ClassOne == 'Ranger') and (NPC.LevelOne >= 4):
      NPC.MagicType = 'Ranger'
    else:  # no spells for the selected class
      return
    for spell in gv.d20_Spell_List:
      #sort spells by level for the class
      for item in spell.level:
        item = item.lstrip()
        ClassLevel = item.split(' ')
        if (ClassLevel[0] == NPC.MagicType):
          if (ClassLevel[1] == '0'):
            SpellLevel_0.append(spell)
          if (ClassLevel[1] == '1'):
            SpellLevel_1.append(spell)
          elif (ClassLevel[1] == '2'):
            SpellLevel_2.append(spell)
          elif (ClassLevel[1] == '3'):
            SpellLevel_3.append(spell)
          elif (ClassLevel[1] == '4'):
            SpellLevel_4.append(spell)
          elif (ClassLevel[1] == '5'):
            SpellLevel_5.append(spell)
          elif (ClassLevel[1] == '6'):
            SpellLevel_6.append(spell)
          elif (ClassLevel[1] == '7'):
            SpellLevel_7.append(spell)
          elif (ClassLevel[1] == '8'):
            SpellLevel_8.append(spell)
          elif (ClassLevel[1] == '9'):
            SpellLevel_9.append(spell)
    NPC.spells_memorized = ""
    if (NPC.spell_0 > 0):
      NPC.spells_memorized = "Level 0 spells: "
      for i in range(NPC.spell_0):
        index = random.randint(0, len(SpellLevel_0)-1)
        NPC.spells_memorized += SpellLevel_0[index].name 
        if (i == NPC.spell_0-1):
          NPC.spells_memorized += "\n"
        else:
          NPC.spells_memorized += ", "
    if (NPC.spell_1 > 0):
      NPC.spells_memorized += "Level 1 spells: "
      for i in range(NPC.spell_1):
        index = random.randint(0, len(SpellLevel_1)-1)
        NPC.spells_memorized += SpellLevel_1[index].name 
        if (i == NPC.spell_1-1):
          NPC.spells_memorized += "\n"
        else:
          NPC.spells_memorized += ", "
    if (NPC.spell_2 > 0):
      NPC.spells_memorized += "Level 2 spells: "
      for i in range(NPC.spell_2):
        index = random.randint(0, len(SpellLevel_2)-1)
        NPC.spells_memorized += SpellLevel_2[index].name 
        if (i == NPC.spell_2-1):
          NPC.spells_memorized += "\n"
        else:
          NPC.spells_memorized += ", "
    if (NPC.spell_3 > 0):
      NPC.spells_memorized += "Level 3 spells: "
      for i in range(NPC.spell_3):
        index = random.randint(0, len(SpellLevel_3)-1)
        NPC.spells_memorized += SpellLevel_3[index].name 
        if (i == NPC.spell_3-1):
          NPC.spells_memorized += "\n"
        else:
          NPC.spells_memorized += ", "
    if (NPC.spell_4 > 0):
      NPC.spells_memorized += "Level 4 spells: "
      for i in range(NPC.spell_4):
        index = random.randint(0, len(SpellLevel_4)-1)
        NPC.spells_memorized += SpellLevel_4[index].name 
        if (i == NPC.spell_4-1):
          NPC.spells_memorized += "\n"
        else:
          NPC.spells_memorized += ", "
    if (NPC.spell_5 > 0):
      NPC.spells_memorized += "Level 5 spells: "
      for i in range(NPC.spell_5):
        index = random.randint(0, len(SpellLevel_5)-1)
        NPC.spells_memorized += SpellLevel_5[index].name 
        if (i == NPC.spell_5-1):
          NPC.spells_memorized += "\n"
        else:
          NPC.spells_memorized += ", "
    if (NPC.spell_6 > 0):
      NPC.spells_memorized += "Level 6 spells: "
      for i in range(NPC.spell_6):
        index = random.randint(0, len(SpellLevel_6)-1)
        NPC.spells_memorized += SpellLevel_6[index].name 
        if (i == NPC.spell_6-1):
          NPC.spells_memorized += "\n"
        else:
          NPC.spells_memorized += ", "
    if (NPC.spell_7 > 0):
      NPC.spells_memorized += "Level 7 spells: "
      for i in range(NPC.spell_7):
        index = random.randint(0, len(SpellLevel_7)-1)
        NPC.spells_memorized += SpellLevel_7[index].name 
        if (i == NPC.spell_7-1):
          NPC.spells_memorized += "\n"
        else:
          NPC.spells_memorized += ", "
    if (NPC.spell_8 > 0):
      NPC.spells_memorized += "Level 8 spells: "
      for i in range(NPC.spell_8):
        index = random.randint(0, len(SpellLevel_8)-1)
        NPC.spells_memorized += SpellLevel_8[index].name 
        if (i == NPC.spell_8-1):
          NPC.spells_memorized += "\n"
        else:
          NPC.spells_memorized += ", "
    if (NPC.spell_9 > 0):
      NPC.spells_memorized += "Level 9 spells: "
      for i in range(NPC.spell_9):
        index = random.randint(0, len(SpellLevel_9)-1)
        NPC.spells_memorized += SpellLevel_9[index].name 
        if (i == NPC.spell_9-1):
          NPC.spells_memorized += "\n"
        else:
          NPC.spells_memorized += ", "
    return

  def __init__(self, parent):
    olddir = os.getcwd()
    os.chdir(gv.root_directory)  #this is necessary so that bitmap paths are read by the dialog code correctly
    PyMapperDialogs.NPC_GeneratorDialogBase.__init__(self,parent)
    os.chdir(olddir)
    
    self.cbxAlignment.AppendItems(gv.NPC_Alignments)
    self.cbxGender.AppendItems(gv.NPC_Sex)
    self.cbxRace.AppendItems(gv.NPC_Races)
    self.cbxClass1.AppendItems(gv.NPC_Classes)
    self.cbxClass2.AppendItems(gv.NPC_Classes)
    self.cbxClass3.AppendItems(gv.NPC_Classes)
    self.cbxClass1.Delete(0)
    self.cbxClass3.SetValue("None")
    self.cbxClass2.SetValue("None")
    self.cbxAlignment.SetSelection(0)
    self.cbxClass1.SetSelection(0)
    self.cbxGender.SetSelection(0)
    self.cbxRace.SetSelection(0)

    self.cbxAbilityScoreGen.AppendItems(gv.NPC_AbilityGeneration)
    self.cbxAbilityScoreGen.SetSelection(0)

    self.cbxClass2.Enable(False)
    self.cbxClass3.Enable(False)
    self.cbClass2Random.Enable(False)
    self.cbClass3Random.Enable(False)
    self.spClass1Level.Enable(False)
    self.spClass2Level.Enable(False)
    self.spClass3Level.Enable(False)

    self.ID_OK.Enable(False)
    self.CompiledNPC = None
    self.AC = None
    return

  def OnCheckbox_cbClass1Random(self, evt):
    if (self.cbClass1Random.IsChecked()):
      self.spClass1Level.Enable(False)
    else:
      self.spClass1Level.Enable(True)
    return

  def OnCheckbox_cbClass2Random(self, evt):
    if (self.cbClass2Random.IsChecked()):
      self.spClass2Level.Enable(False)
    else:
      self.spClass2Level.Enable(True)
    return

  def OnCheckbox_cbClass3Random(self, evt):
    if (self.cbClass3Random.IsChecked()):
      self.spClass3Level.Enable(False)
    else:
      self.spClass3Level.Enable(True)
    return

  def Add_NPC(self, evt):
    #gv.NPC_List.append(self.CompiledNPC)
    #the calling function is responsible to extract the info from self.compiledNPC
    self.EndModal(True)
    return

  def OnCancel(self, evt):
    self.EndModal(False)
    return

  def OnHelp(self, evt):
    text = "At a minimum, the Gender, Race, Class, and Alignment must be set to a value.  The value may be set as 'any' to generate a random result.\n\nThe abiltity generation methods are as follows:\n  Straight 3d6 rolls three six sided dice, taking the results as they come.\n  Best of 4d6 rolls 4 dice and drops the lowest value.\n  Modified 4d6 rolls dice same as the 'Best of 4d6' method, but the lowest dice is changed to a 6.\n  Straight 18's gives an 18 to each ability score.\n\nNote that racial bonuses are applied after rolling dice.\n\nWhen generating random characters, the selection of classes may override the alignment selection.\n\nMulticlass characters are currently disabled."
    dlg = HelpDialog(self, text)
    dlg.ShowModal()
    dlg.Destroy()
    return

  def GenerateNPC(self, event=None):
    #validate that all of the necessary information has been set
    #The finished npc is stored in self.CompiledNPC
    self.CompiledNPC = None
    process = True
    if (self.cbxAlignment.GetValue() == ""):
      process = False
    if (self.cbxClass1.GetValue() == ""):
      process = False
    if (self.cbxGender.GetValue() == ""):
      process = False
    if (self.cbxAbilityScoreGen.GetValue() == ""):
      process = False
    if (self.cbxRace.GetValue() == ""):
      process = False
    if (process == False):
      dlg = wx.MessageDialog(self,"Not enough data to create an NPC.  Please enter at least an Alignment, Race, Gender, and Class",
                             "Insufficient Data!", style=wx.OK|wx.ICON_EXCLAMATION)
      result = dlg.ShowModal()
      dlg.Destroy()
      return

    NPC = srd.NPC_Record()
    NPC.Gender = self.cbxGender.GetValue()
    if (NPC.Gender == 'Any'):
      sex = random.randint(1,2)
      if (sex == 1):
        NPC.Gender = 'Male'
      else:
        NPC.Gender = 'Female'

    #Set the law/chaos and good/evil axis
    NPC.Alignment = self.cbxAlignment.GetValue()
    dice = random.randint(1,100)
    if (dice <= 20):  # GE = Good/Evil axis
      NPC.GoodEvilAxis = 'Good'
    elif (dice <= 50):
      NPC.GoodEvilAxis = 'Neutral'
    else:
      NPC.GoodEvilAxis = 'Evil'
    dice = random.randint(1,3)
    if (dice == 1):  # LC = Law/Chaos axis
      NPC.LawChaosAxis = 'Lawful'
    elif (dice == 2):
      NPC.LawChaosAxis = 'Neutral'
    else:
      NPC.LawChaosAxis = 'Chaotic'

    if (NPC.Alignment == 'Any'):
      NPC.Alignment = NPC.LawChaosAxis + " " + NPC.GoodEvilAxis
    elif (NPC.Alignment == 'Any Good'):
      NPC.GoodEvilAxis = 'Good'
      NPC.Alignment = NPC.LawChaosAxis + ' Good'
    elif (NPC.Alignment == 'Any Neutral'):
      NPC.LawChaosAxis = 'Neutral'
      NPC.Alignment = 'Neutral ' + GE
    elif (NPC.Alignment == 'Any Evil'):
      NPC.GoodEvilAxis = 'Evil'
      NPC.Alignment = NPC.LawChaosAxis + ' Evil'
    # if none of these, then a specific alignment was chosen.
    elif (NPC.Alignment == 'Lawful Good'):
      NPC.LawChaosAxis = 'Lawful'
      NPC.GoodEvilAxis = 'Good'
    elif (NPC.Alignment == 'Lawful Neutral'):
      NPC.LawChaosAxis = 'Lawful'
      NPC.GoodEvilAxis = 'Neutral'
    elif (NPC.Alignment == 'Lawful Evil'):
      NPC.LawChaosAxis = 'Lawful'
      NPC.GoodEvilAxis = 'Evil'
    elif (NPC.Alignment == 'Chaotic Good'):
      NPC.LawChaosAxis = 'Chaotic'
      NPC.GoodEvilAxis = 'Good'
    elif (NPC.Alignment == 'Chaotic Neutral'):
      NPC.LawChaosAxis = 'Chaotic'
      NPC.GoodEvilAxis = 'Neutral'
    elif (NPC.Alignment == 'Chaotic Evil'):
      NPC.LawChaosAxis = 'Chaotic'
      NPC.GoodEvilAxis = 'Evil'
    elif (NPC.Alignment == 'True Neutral'):
      NPC.LawChaosAxis = 'Neutral'
      NPC.GoodEvilAxis = 'Neutral '
    elif (NPC.Alignment == 'Neutral Good'):
      NPC.LawChaosAxis = 'Neutral'
      NPC.GoodEvilAxis = 'Good'
    elif (NPC.Alignment == 'Any Evil'):
      NPC.LawChaosAxis = 'Neutral'
      NPC.GoodEvilAxis = 'Evil'

    #assign the race if random requested
    dlg_race = self.cbxRace.GetValue()
    if (dlg_race == 'Any'):
      dice = random.randint(0,len(gv.NPC_Races))
      NPC.race = gv.SRD_RacesList[dice]
    else:
      for item in gv.SRD_RacesList:
        if (dlg_race == item.Name):
          NPC.race = item

    #check the selected race against the usual alignment
    if (NPC.race.GoodEvilAxis != 'Any'):
      NPC.GoodEvilAxis = NPC.race.GoodEvilAxis
    if (NPC.race.LawChaosAxis != 'Any'):
      NPC.LawChaosAxis = NPC.race.LawChaosAxis

    #generate the Height and Weight
    if (NPC.Gender == 'Male'):
      NPC.height_ft = NPC.race.maleStatHeightFeet
      NPC.height_in = NPC.race.maleStatHeightInches
      NPC.weight = NPC.race.maleStatWeight
      #check SRD to vary height, weight
      combo = str(NPC.race.maleStatHeightModDieQty)+"d"+str(NPC.race.maleStatHeightModDie)
      dHeight = app.RollDice(combo)
      inches = dHeight % 12
      feet = dHeight//12
      NPC.height_ft += feet
      NPC.height_in += inches
      if (NPC.height_in >= 12):
        NPC.height_ft += 1
        NPC.height_in -= 12
    else:
      NPC.height_ft = NPC.race.femaleStatHeightFeet
      NPC.height_in = NPC.race.femaleStatHeightInches
      NPC.weight = NPC.race.femaleStatWeight
      #check SRD to vary height, weight
      combo = str(NPC.race.femaleStatHeightModDieQty)+"d"+str(NPC.race.femaleStatHeightModDie)
      dHeight = app.RollDice(combo)
      inches = dHeight % 12
      feet = dHeight//12
      NPC.height_ft += feet
      NPC.height_in += inches
      if (NPC.height_in >= 12):
        NPC.height_ft += 1
        NPC.height_in -= 12

    #generate the ability scores
    if (self.cbxAbilityScoreGen.GetSelection() == 0): #Straight 3d6
      NPC.STR = app.RollDice('3d6') + NPC.race.STR_bonus
      NPC.INT = app.RollDice('3d6') + NPC.race.INT_bonus
      NPC.DEX = app.RollDice('3d6') + NPC.race.DEX_bonus
      NPC.CON = app.RollDice('3d6') + NPC.race.CON_bonus
      NPC.WIS = app.RollDice('3d6') + NPC.race.WIS_bonus
      NPC.CHA = app.RollDice('3d6') + NPC.race.CHA_bonus
    elif (self.cbxAbilityScoreGen.GetSelection() == 1): #Best of 4d6
      dice = [app.RollDice('1d6'), app.RollDice('1d6'),
              app.RollDice('1d6'), app.RollDice('1d6')]
      dice.sort()
      NPC.STR = dice[1]+dice[2]+dice[3] + NPC.race.STR_bonus
      dice = [app.RollDice('1d6'), app.RollDice('1d6'),
              app.RollDice('1d6'), app.RollDice('1d6')]
      dice.sort()
      NPC.INT = dice[1]+dice[2]+dice[3] + NPC.race.INT_bonus
      dice = [app.RollDice('1d6'), app.RollDice('1d6'),
              app.RollDice('1d6'), app.RollDice('1d6')]
      dice.sort()
      NPC.DEX = dice[1]+dice[2]+dice[3] + NPC.race.DEX_bonus
      dice = [app.RollDice('1d6'), app.RollDice('1d6'),
              app.RollDice('1d6'), app.RollDice('1d6')]
      dice.sort()
      NPC.CON = dice[1]+dice[2]+dice[3] + NPC.race.CON_bonus
      dice = [app.RollDice('1d6'), app.RollDice('1d6'),
              app.RollDice('1d6'), app.RollDice('1d6')]
      dice.sort()
      NPC.WIS = dice[1]+dice[2]+dice[3] + NPC.race.WIS_bonus
      dice = [app.RollDice('1d6'), app.RollDice('1d6'),
              app.RollDice('1d6'), app.RollDice('1d6')]
      dice.sort()
      NPC.CHA = dice[1]+dice[2]+dice[3] + NPC.race.CHA_bonus
    elif (self.cbxAbilityScoreGen.GetSelection() == 2): #Modified 4d6
      dice = [app.RollDice('1d6'), app.RollDice('1d6'),
              app.RollDice('1d6'), app.RollDice('1d6')]
      dice.sort()
      NPC.STR = 6+dice[2]+dice[3] + NPC.race.STR_bonus
      dice = [app.RollDice('1d6'), app.RollDice('1d6'),
              app.RollDice('1d6'), app.RollDice('1d6')]
      dice.sort()
      NPC.INT = 6+dice[2]+dice[3] + NPC.race.INT_bonus
      dice = [app.RollDice('1d6'), app.RollDice('1d6'),
              app.RollDice('1d6'), app.RollDice('1d6')]
      dice.sort()
      NPC.DEX = 6+dice[2]+dice[3] + NPC.race.DEX_bonus
      dice = [app.RollDice('1d6'), app.RollDice('1d6'),
              app.RollDice('1d6'), app.RollDice('1d6')]
      dice.sort()
      NPC.CON = 6+dice[2]+dice[3] + NPC.race.CON_bonus
      dice = [app.RollDice('1d6'), app.RollDice('1d6'),
              app.RollDice('1d6'), app.RollDice('1d6')]
      dice.sort()
      NPC.WIS = 6+dice[2]+dice[3] + NPC.race.WIS_bonus
      dice = [app.RollDice('1d6'), app.RollDice('1d6'),
              app.RollDice('1d6'), app.RollDice('1d6')]
      dice.sort()
      NPC.CHA = dice[1]+dice[2]+dice[3] + NPC.race.CHA_bonus
    elif(self.cbxAbilityScoreGen.GetSelection() == 3):  #Straight 18
      NPC.STR = 18 + NPC.race.STR_bonus
      NPC.INT = 18 + NPC.race.INT_bonus
      NPC.DEX = 18 + NPC.race.DEX_bonus
      NPC.CON = 18 + NPC.race.CON_bonus
      NPC.WIS = 18 + NPC.race.WIS_bonus
      NPC.CHA = 18 + NPC.race.CHA_bonus

    #assign class levels
    if (self.cbClass1Random.IsChecked()):
      NPC.LevelOne = app.RollDice('1d20')
    else:
      NPC.LevelOne = self.spClass1Level.GetValue()

    #if (self.cbClass2Random.IsChecked()):
    #  NPC.LevelTwo = app.RollDice('1d20')
    #else:
    #  NPC.LevelTwo = self.spClass2Level.GetValue()

    #if (self.cbClass3Random.IsChecked()):
    #  NPC.LevelThree = app.RollDice('1d20')
    #else:
    #  NPC.LevelThree = self.spClass3Level.GetValue()

    NPC.HD = NPC.LevelOne + NPC.LevelTwo + NPC.LevelThree
    #assign classes
    if (self.cbxClass1.GetValue() == 'Any'):
      dice = app.RollDice('1d100')
      if (dice <= 75) and (NPC.race.PrefClass != 'Any'):  #75% chance that the NPC is in his race's preferred class 
        NPC.ClassOne = NPC.race.PrefClass
      else:
        #generate random class
        dice = random.randint(2,len(gv.NPC_Classes)-1)
        NPC.ClassOne = gv.NPC_Classes[dice]
    else:
      NPC.ClassOne = self.cbxClass1.GetValue()

    #if (self.cbxClass2.GetValue() == 'Any'):
    #  dice = app.RollDice('1d100')
    #  if (dice <= 75) and (NPC.race.PrefClass != 'Any'):  #75% chance that the NPC is in his race's preferred class 
    #    NPC.ClassTwo = NPC.race.PrefClass
    #  else:
    #    #generate random class
    #    dice = random.randint(2,len(gv.NPC_Classes)-1)
    #    NPC.ClassTwo = gv.NPC_Classes[dice]
    #else:
    #  NPC.ClassTwo = self.cbxClass2.GetValue()

    #if (self.cbxClass3.GetValue() == 'Any'):
    #  dice = app.RollDice('1d100')
    #  if (dice <= 75) and (NPC.race.PrefClass != 'Any'):  #75% chance that the NPC is in his race's preferred class 
    #    NPC.ClassThree = NPC.race.PrefClass
    #  else:
    #    #generate random class
    #    dice = random.randint(2,len(gv.NPC_Classes)-1)
    #    NPC.ClassThree = gv.NPC_Classes[dice]
    #else:
    #  NPC.ClassThree = self.cbxClass3.GetValue()

    #check to see if the class is restricted by the alignments chosen
    self.ClassList = []
    self.ClassList.append(self.cbxClass1.GetValue())
    #self.ClassList.append(self.cbxClass2.GetValue())
    #self.ClassList.append(self.cbxClass3.GetValue())
    for item in self.ClassList:
      if (item == 'Bard') or (item == 'Barbarian'):  #any non-lawful
        dice = random.randint(1,2)
        if (dice == 1):
          NPC.LawChaosAxis = 'Neutral'
        else:
          NPC.LawChaosAxis = 'Chaotic'
      elif (item == 'Druid'):  #any neutral
        dice = random.randint(1,2)
        if (dice == 1):
          NPC.LawChaosAxis = 'Neutral'
        else:
          NPC.GoodEvilAxis = 'Neutral'
      elif (item == 'Monk'): #any lawful
        NPC.LawChaosAxis =  'Lawful'
      elif (item == 'Paladin'):  #lawful good only
        NPC.LawChaosAxis = 'Lawful'
        NPC.GoodEvilAxis = 'Good'

    #generate a name
    if (NPC.race.Name == 'Dwarf'):
      NamePrefix = gv.NPC_Names.DwarfPrefix[random.randint(0,len(gv.NPC_Names.DwarfPrefix)-1)]
      if (NPC.Gender == 'Male'):
        NameSuffix = gv.NPC_Names.DwarfMaleSuffix[random.randint(0,len(gv.NPC_Names.DwarfMaleSuffix)-1)]
      else:
        NameSuffix = gv.NPC_Names.DwarfFemaleSuffix[random.randint(0,len(gv.NPC_Names.DwarfFemaleSuffix)-1)]
      NPC.Name = NamePrefix + NameSuffix
    elif (NPC.race.Name == 'Elf'):
      if (NPC.Gender == 'Male'):
        NamePrefix = gv.NPC_Names.MaleElfPrefix[random.randint(0,len(gv.NPC_Names.MaleElfPrefix)-1)]
        NameMidfix = gv.NPC_Names.MaleElfMidfix[random.randint(0,len(gv.NPC_Names.MaleElfMidfix)-1)] 
        NameSuffix = gv.NPC_Names.MaleElfSuffix[random.randint(0,len(gv.NPC_Names.MaleElfSuffix)-1)]
      else:
        NamePrefix = gv.NPC_Names.FemaleElfPrefix[random.randint(0,len(gv.NPC_Names.FemaleElfPrefix)-1)]
        NameMidfix = gv.NPC_Names.FemaleElfMidfix[random.randint(0,len(gv.NPC_Names.FemaleElfMidfix)-1)] 
        NameSuffix = gv.NPC_Names.FemaleElfSuffix[random.randint(0,len(gv.NPC_Names.FemaleElfSuffix)-1)]
      NPC.Name = NamePrefix + NameMidfix + NameSuffix
    elif (NPC.race.Name == 'Gnome'):
      if (NPC.Gender == 'Male'):
        NPC.Name = gv.NPC_Names.MaleGnomeNames[random.randint(0,len(gv.NPC_Names.MaleGnomeNames)-1)]
      else:
        NPC.Name = gv.NPC_Names.FemaleGnomeNames[random.randint(0,len(gv.NPC_Names.FemaleGnomeNames)-1)]
    elif (NPC.race.Name == 'Halfling'):
      if (NPC.Gender == 'Male'):
        NPC.Name = gv.NPC_Names.MaleHalflingNames[random.randint(0,len(gv.NPC_Names.MaleHalflingNames)-1)]
      else:
        NPC.Name = gv.NPC_Names.FemaleHalflingNames[random.randint(0,len(gv.NPC_Names.FemaleHalflingNames)-1)]
    elif (NPC.race.Name == 'Human'):
      if (NPC.Gender == 'Male'):
        NPC.Name = gv.NPC_Names.MaleHumanNames[random.randint(0,len(gv.NPC_Names.MaleHumanNames)-1)]
      else:
        NPC.Name = gv.NPC_Names.FemaleHumanNames[random.randint(0,len(gv.NPC_Names.FemaleHumanNames)-1)]
    else:
      NamePrefix = gv.NPC_Names.MonsterPrefix[random.randint(0,len(gv.NPC_Names.MonsterPrefix)-1)]
      NameMidfix = gv.NPC_Names.MonsterMidfix[random.randint(0,len(gv.NPC_Names.MonsterMidfix)-1)] 
      NameSuffix = gv.NPC_Names.MonsterSuffix[random.randint(0,len(gv.NPC_Names.MonsterSuffix)-1)]
      NPC.Name = NamePrefix + NameMidfix + NameSuffix
    NPC.Name = NPC.Name.capitalize()

    #Set the languages
    if (NPC.race == 'Human'):
      NPC.Languages.append(gv.NPC_Languages[0])
    elif (NPC.race == 'Elf'):
      NPC.Languages.append(gv.NPC_Languages[0]) #common
      NPC.Languages.append(gv.NPC_Languages[1]) #elf
      NPC.Languages.append(gv.NPC_Languages[10]) #draconic
      NPC.Languages.append(gv.NPC_Languages[12]) #gnoll
      NPC.Languages.append(gv.NPC_Languages[3])
      NPC.Languages.append(gv.NPC_Languages[8]) 
      NPC.Languages.append(gv.NPC_Languages[5])
      NPC.Languages.append(gv.NPC_Languages[6])
    elif (NPC.race == 'Dwarf'):
      NPC.Languages.append(gv.NPC_Languages[0])
      NPC.Languages.append(gv.NPC_Languages[2])  #dwarf
      NPC.Languages.append(gv.NPC_Languages[12]) #giant
      NPC.Languages.append(gv.NPC_Languages[3]) #gnome
      NPC.Languages.append(gv.NPC_Languages[8]) #goblin\
      NPC.Languages.append(gv.NPC_Languages[5]) #orc
      NPC.Languages.append(gv.NPC_Languages[10]) #terran
      NPC.Languages.append(gv.NPC_Languages[9]) #undercommon
    elif (NPC.race == 'Gnome'):
      NPC.Languages.append(gv.NPC_Languages[0])
      NPC.Languages.append(gv.NPC_Languages[3])
      NPC.Languages.append(gv.NPC_Languages[11]) #draconic
      NPC.Languages.append(gv.NPC_Languages[2])
      NPC.Languages.append(gv.NPC_Languages[1])
      NPC.Languages.append(gv.NPC_Languages[12])
      NPC.Languages.append(gv.NPC_Languages[5])
      NPC.Languages.append(gv.NPC_Languages[8])
    elif (NPC.race == 'Halfling'):
      NPC.Languages.append(gv.NPC_Languages[0])
      NPC.Languages.append(gv.NPC_Languages[4])
      NPC.Languages.append(gv.NPC_Languages[2])
      NPC.Languages.append(gv.NPC_Languages[1])
      NPC.Languages.append(gv.NPC_Languages[3])
      NPC.Languages.append(gv.NPC_Languages[8])
      NPC.Languages.append(gv.NPC_Languages[5])
    elif (NPC.race == 'HalfOrc'):
      NPC.Languages.append(gv.NPC_Languages[0])
      NPC.Languages.append(gv.NPC_Languages[5])
      NPC.Languages.append(gv.NPC_Languages[2])
      NPC.Languages.append(gv.NPC_Languages[12])
      NPC.Languages.append(gv.NPC_Languages[13])
      NPC.Languages.append(gv.NPC_Languages[13])
      NPC.Languages.append(gv.NPC_Languages[16])
    else:
      NPC.Languages.append(gv.NPC_Languages[0])

    #Calculate the hit points
    bonus = self.GetStatBonus(NPC.CON)
    calc = True
    level = 1

    if ((NPC.ClassOne == 'Wizard') or (NPC.ClassOne == 'Sorcerer') or (NPC.ClassOne == 'Commoner')):
      hit_die = '1d4'
      hp = 4  #version 5.1:  First level gets max HP
    elif ((NPC.ClassOne == 'Bard') or (NPC.ClassOne == 'Rogue') or (NPC.ClassOne == 'Adept') or (NPC.ClassOne == 'Expert')):
      hit_die = '1d6'
      hp = 6
    elif ((NPC.ClassOne == 'Aristocrat') or (NPC.ClassOne == 'Cleric') or (NPC.ClassOne == 'Druid') or
          (NPC.ClassOne == 'Monk') or (NPC.ClassOne == 'Ranger') or (NPC.ClassOne == 'Warrior')):
      hit_die = '1d8'
      hp = 8
    elif ((NPC.ClassOne == 'Fighter') or (NPC.ClassOne == 'Paladin')):
      hit_die = '1d10'
      hp = 10
    elif ((NPC.ClassOne == 'Barbarian')):
      hit_die = '1d12'
      hp = 12

    if (level < NPC.LevelOne):
      while (calc):
        hp = app.RollDice(hit_die) + bonus
        if (hp < 1):
          hp = 1
        NPC.HP += hp
        level += 1 
        if (level >= NPC.LevelOne):
          calc = False

    if (NPC.LevelTwo > 0):
      if ((NPC.ClassTwo == 'Wizard') or (NPC.ClassTwo == 'Sorcerer') or (NPC.ClassTwo == 'Commoner')):
        hit_die = '1d4'
      elif ((NPC.ClassTwo == 'Bard') or (NPC.ClassTwo == 'Adept') or (NPC.ClassTwo == 'Expert')):
        hit_die = '1d6'
      elif ((NPC.ClassTwo == 'Aristocrat') or (NPC.ClassTwo == 'Cleric') or (NPC.ClassTwo == 'Druid') or
            (NPC.ClassTwo == 'Monk') or (NPC.ClassTwo == 'Ranger') or (NPC.ClassTwo == 'Warrior')):
        hit_die = '1d8'
      elif ((NPC.ClassTwo == 'Fighter') or (NPC.ClassTwo == 'Paladin')):
        hit_die = '1d10'
      elif ((NPC.ClassTwo == 'Barbarian')):
        hit_die = '1d12'
      calc = True
      level = 1
      while (calc):
        hp = app.RollDice(hit_die) + bonus
        if (hp < 1):
          hp = 1
        NPC.HP += hp
        level += 1
        if (level > NPC.LevelTwo):
          calc = False

    if (NPC.LevelThree > 0):
      if ((NPC.ClassThree == 'Wizard') or (NPC.ClassThree == 'Sorcerer') or (NPC.ClassThree == 'Commoner')):
        hit_die = '1d4'
      elif ((NPC.ClassThree == 'Bard') or (NPC.ClassThree == 'Adept') or (NPC.ClassThree == 'Expert')):
        hit_die = '1d6'
      elif ((NPC.ClassThree == 'Aristocrat') or (NPC.ClassThree == 'Cleric') or (NPC.ClassThree == 'Druid') or
            (NPC.ClassThree == 'Monk') or (NPC.ClassThree == 'Ranger') or (NPC.ClassThree == 'Warrior')):
        hit_die = '1d8'
      elif ((NPC.ClassThree == 'Fighter') or (NPC.ClassThree == 'Paladin')):
        hit_die = '1d10'
      elif ((NPC.ClassThree == 'Barbarian')):
        hit_die = '1d12'
      calc = True
      level = 1
      while (calc):
        hp = app.RollDice(hit_die) + bonus
        if (hp < 1):
          hp = 1
        NPC.HP += hp
        level += 1
        if (level > NPC.LevelThree):
          calc = False

    bab1 = None
    bab2 = None
    bab3 = None
    #calculate the saves (FORT, WIll, REF)
    for item in gv.NPC_Class_Info:
      if ((item.class_name == NPC.ClassOne) and (item.level == NPC.LevelOne)):
        NPC.FORT += item.FORT
        NPC.WILL += item.WILL
        NPC.REF += item.REF
        bab1 = item.BAB
      if ((item.class_name == NPC.ClassTwo) and (item.level == NPC.LevelTwo)):
        NPC.FORT += item.FORT
        NPC.WILL += item.WILL
        NPC.REF += item.REF
        bab2 = item.BAB
      if ((item.class_name == NPC.ClassThree) and (item.level == NPC.LevelThree)):
        NPC.FORT += item.FORT
        NPC.WILL += item.WILL
        NPC.REF += item.REF
        bab3 = item.BAB

    #determine the number of attacks and bonuses
    info1 = bab1.split('/')
    if (bab2 != None):
      info2 = bab2.split('/')
    else:
      info2 = []
    if (bab3 != None):
      info3 = bab3.split('/')
    else:
      info3 = []

    NPC.BAB = []
    for i in range(4):  #This is to set to minimum of 4 attacks
      info1.append('0')
      info2.append('0')
      info3.append('0')
      NPC.BAB.append('0')

    for i in range(4):
      NPC.BAB[i] = int(info1[i]) + int(info2[i]) + int(info3[i])

    #calculate the melee and ranged attack bonuses
    MAbonus = self.GetStatBonus(NPC.STR)
    MRbonus = self.GetStatBonus(NPC.DEX)

    NPC.AttackMelee = '+'+str(NPC.BAB[0]+MAbonus)
    NPC.AttackRanged = '+'+str(NPC.BAB[0]+MRbonus)
    if (NPC.BAB[1] > 0):
      NPC.AttackMelee += '/+'+str(NPC.BAB[1]+MAbonus)
      NPC.AttackRanged += '/+'+str(NPC.BAB[1]+MRbonus)
    if (NPC.BAB[2] > 0):
      NPC.AttackMelee += '/+'+str(NPC.BAB[2]+MAbonus)
      NPC.AttackRanged += '/+'+str(NPC.BAB[2]+MRbonus)
    if (NPC.BAB[3] > 0):
      NPC.AttackMelee += '/+'+str(NPC.BAB[3]+MAbonus)
      NPC.AttackRanged += '/+'+str(NPC.BAB[3]+MRbonus)

    #calculate the skill points
    if ((NPC.ClassOne == 'Wizard') or (NPC.ClassOne == 'Sorcerer') or (NPC.ClassOne == 'Adept') 
        or (NPC.ClassOne == 'Fighter') or (NPC.ClassOne == 'Warrior') or (NPC.ClassOne == 'Cleric')
        or (NPC.ClassOne == 'Commoner') or (NPC.ClassOne == 'Paladin')):
      factor1 = 2
    elif ((NPC.ClassOne == 'Bard')  or (NPC.ClassOne == 'Expert') or (NPC.ClassOne == 'Ranger')):
      factor1 = 6
    elif ((NPC.ClassOne == 'Aristocrat') or (NPC.ClassOne == 'Druid') or (NPC.ClassOne == 'Barbarian') or
          (NPC.ClassOne == 'Rogue') or (NPC.ClassOne == 'Monk')):
      factor1 = 4

    if (NPC.ClassTwo == 'None'):
      factor2 = 0
    else:
      if ((NPC.ClassTwo == 'Wizard') or (NPC.ClassTwo == 'Sorcerer') or (NPC.ClassTwo == 'Adept') 
          or (NPC.ClassTwo == 'Fighter') or (NPC.ClassTwo == 'Warrior') or (NPC.ClassTwo == 'Cleric')
          or (NPC.ClassTwo == 'Commoner') or (NPC.ClassTwo == 'Paladin')):
        factor2 = 2
      elif ((NPC.ClassTwo == 'Bard')  or (NPC.ClassTwo == 'Expert') or (NPC.ClassTwo == 'Ranger')):
        factor2 = 6
      elif ((NPC.ClassTwo == 'Aristocrat') or (NPC.ClassTwo == 'Druid') or (NPC.ClassTwo == 'Barbarian') or
            (NPC.ClassOne == 'Rogue') or (NPC.ClassTwo == 'Monk')):
        factor2 = 4

    if (NPC.ClassThree == 'None'):
      factor3 = 0
    else:
      if ((NPC.ClassThree == 'Wizard') or (NPC.ClassThree == 'Sorcerer') or (NPC.ClassThree == 'Adept') 
          or (NPC.ClassThree == 'Fighter') or (NPC.ClassThree == 'Warrior') or (NPC.ClassThree == 'Cleric')
          or (NPC.ClassThree == 'Commoner') or (NPC.ClassThree == 'Paladin')):
        factor3 = 2
      elif ((NPC.ClassThree == 'Bard')  or (NPC.ClassThree == 'Expert') or (NPC.ClassThree == 'Ranger')):
        factor3 = 6
      elif ((NPC.ClassThree == 'Aristocrat') or (NPC.ClassThree == 'Druid') or (NPC.ClassThree == 'Barbarian') or
            (NPC.ClassOne == 'Rogue') or (NPC.ClassThree == 'Monk')):
        factor3 = 4

    #--------------------------------------------
    # add support for multiclass after this point
    #--------------------------------------------

    points = (factor1 + self.GetStatBonus(NPC.INT)) * 4
    points += (factor1 + self.GetStatBonus(NPC.INT))* (NPC.LevelOne-1) # all but first level
    points = max(0, points)

    for item in gv.NPC_Skill_Info:
      if (item.name == NPC.ClassOne):
        NPC.skills = item.skills
        NPC.ranks = item.ranks
        NPC.CCranks = item.CCranks
        NPC.CCskills = item.CCskills
    #One of two methods will be used to assign ranks:
    #  1:  Even distribution
    #  2:  Random distribution
    #  3:  Max random
    value = app.RollDice('1d100')
    if (value < 25) :  #even distribution
      for index in range(len(NPC.ranks)):
        NPC.ranks[index] += 1
        points -= 1
        if (points <= 0):
          break
        if (index == range(len(NPC.ranks)-1)):
          index = 0
        points -= 2
        CCslot = random.randint(0,len(NPC.CCranks)-1)
        NPC.CCranks[CCslot] += 1
        if (points <= 0):
          break
        if (index == range(len(NPC.CCranks)-1)):
          index = 0

    elif (value < 60): #random max
      assign = True
      while (assign == True):
        slot = random.randint(0,len(NPC.ranks)-1)
        CCslot = random.randint(0,len(NPC.CCranks)-1)
        if (NPC.ranks[slot] >= NPC.LevelOne+3):
          if (NPC.CCranks[CCslot] >= NPC.LevelOne+3):
            continue
          else:
            NPC.CCranks[CCslot] += 1
            points -= 2
        else:
          if (points > (NPC.LevelOne+3)):
            delta = NPC.LevelOne+3
          else:
            delta = points
          points -= delta
          NPC.ranks[slot] += delta
        if (points <= 0):
          assign = False
    else:  #random distribution
      assign = True
      while (assign == True):
        slot = random.randint(0,len(NPC.ranks)-1)
        CCslot = random.randint(0,len(NPC.CCranks)-1)
        if (NPC.ranks[slot] >= NPC.LevelOne+3):
          if (NPC.CCranks[CCslot] >= NPC.LevelOne+3):
            continue
          else:
            NPC.CCranks[CCslot] += 1
            points -= 2
        else:
          NPC.ranks[slot] += 1
          points -= 1
        if (points <= 0):
          assign = False
    #note that the SRD does not provide info on how many feats per level a NPC
    #has, so we're going to simply assume 1 feat per 3 levels.  Fighters have a
    #bonus feat at level 1 also.
    num_feats = NPC.LevelOne % 3 + 1
    if (NPC.ClassOne == 'Fighter'):
      num_feats += 1

    #assign feats
    templist = []
    if ((NPC.ClassOne == 'Sorcerer') or (NPC.ClassOne == 'Wizard')):
      #build temporary list of feats
      for item in gv.NPC_Feat_Info:
        if (item.subset == 4):
          templist.append(item)
    elif ((NPC.ClassOne == 'Fighter') or (NPC.ClassOne == 'Barbarian') or
          (NPC.ClassOne == 'Paladin') or (NPC.ClassOne == 'Cleric')):
      #build temporary list of feats
      for item in gv.NPC_Feat_Info:
        if (item.subset == 2):
          templist.append(item)
    elif ((NPC.ClassOne == 'Ranger') or (NPC.ClassOne == 'Bard')):
      #build temporary list of feats
      for item in gv.NPC_Feat_Info:
        if (item.subset == 3):
          templist.append(item)

    #add the rest of the general feats
    for item in gv.NPC_Feat_Info:
      if (item.subset == 1):
        templist.append(item)

    assign = True
    while(assign):
      index = random.randint(0, len(templist)-1)
      index2 = 0
      item = templist[index]
      add_feats = True
      while (add_feats) and (num_feats >= 1):
        NPC.Feats.append(item.featlist[index2])
        index2 += 1
        num_feats -= 1
        if (len(item.featlist) <= index2):
          add_feats = False
      templist.pop(index)
      if (num_feats < 1):
        assign = False

    #if necessary, add spells
    item = srd.NPC_Class_Info_Record()
    for item in gv.NPC_Class_Info:
      if (item.class_name == NPC.ClassOne) and (item.level == NPC.LevelOne):
        text = "Spells("
        if (item.spells_available_0 > 0):
          text += "0th:"+item.spells_available_0
          NPC.spell_0 = int(item.spells_available_0)
        if (item.spells_available_1 > 0):
          text += "; 1st:"+item.spells_available_1
          NPC.spell_1 = int(item.spells_available_1)
        if (item.spells_available_2 > 0):
          text += "; 2nd:"+item.spells_available_2
          NPC.spell_2 = int(item.spells_available_2)
        if (item.spells_available_3 > 0):
          text += "; 3rd:"+item.spells_available_3
          NPC.spell_3 = int(item.spells_available_3)
        if (item.spells_available_4 > 0):
          text += "; 4th:"+item.spells_available_4
          NPC.spell_4 = int(item.spells_available_4)
        if (item.spells_available_5 > 0):
          text += "; 5th:"+item.spells_available_5
          NPC.spell_5 = int(item.spells_available_5)
        if (item.spells_available_6 > 0):
          text += "; 6th:"+item.spells_available_6
          NPC.spell_6 = int(item.spells_available_6)
        if (item.spells_available_7 > 0):
          text += "; 7th:"+item.spells_available_7
          NPC.spell_7 = int(item.spells_available_7)
        if (item.spells_available_8 > 0):
          text += "; 8th:"+item.spells_available_8
          NPC.spell_8 = int(item.spells_available_8)
        if (item.spells_available_9 > 0):
          text += "; 9th:"+item.spells_available_9
          NPC.spell_9 = int(item.spells_available_9)
        text += ")\n"
        NPC.spells = text
        self.AssignSpells(NPC, item.level)

    txt = self.PrintStatBlock(NPC)

    self.txStatBlock.Clear()
    self.txStatBlock.AppendText(txt)

    self.CompiledNPC = NPC
    self.ID_OK.Enable(True)
    return
  #end of GenerateNPC

  def GetStatBonus(self, stat):
    if (stat == 1):
      bonus = -5
    elif (stat <= 3):
      bonus = -4
    elif (stat <=5):
      bonus = -3
    elif (stat <=7):
      bonus = -2
    elif (stat <=9):
      bonus = -1
    elif (stat <=11):
      bonus = 0
    elif (stat <=13):
      bonus = 1
    elif (stat <=15):
      bonus = 2
    elif (stat <=17):
      bonus = 3
    elif (stat <=19):
      bonus = 4
    elif (stat <=21):
      bonus = 5
    elif (stat <=23):
      bonus = 6
    elif (stat <=25):
      bonus = 7
    elif (stat <=27):
      bonus = 8
    elif (stat <=29):
      bonus = 9
    elif (stat <=31):
      bonus = 10
    elif (stat <=33):
      bonus = 11
    elif (stat <=35):
      bonus = 12
    elif (stat <=37):
      bonus = 13
    else:
      bonus = 14

    return bonus

  def SetBarbarianAttributes(self, npc, level):
    npc = srd.NPC_Record()
    item = srd.NPC_Class_Info_Record()
    for item in gv.NPC_Class_Info:
      if ((item.class_name == 'Barbarian') and (item.level == level)):
        return item

  def PrintStatBlock(self, npc):
    """
    Return a text string with the NPC info.
    The use of :: is a tag for certain NPC information that is loaded into the Character information dialog.
    It is both the start and ending tag"""
    text = "::Name::"+ npc.Name +"::, "+ npc.Gender +" "+ npc.race.Name +", "+ npc.ClassOne + str(npc.LevelOne)

    if (npc.ClassTwo != 'None'):
      text += '/'+npc.ClassTwo + str(npc.LevelTwo)
    if (npc.ClassThree != 'None'):
      text += '/'+npc.ClassThree + str(npc.LevelThree)
    text += '; CR ' + str(npc.CR) +"; Size "+ npc.size + " ("+str(npc.height_ft)+" ft "+str(npc.height_in)+" in tall, weight "+str(npc.weight)+" lbs.)\n"
    text += 'HD ' + str(npc.HD) + '; ::HP::'+ str(npc.HP) +'::, '
    if (npc.init > 0):
      text += 'Init +'+ str(npc.init) + '; '
    else:
      text += 'Init '+str(npc.init) + '; '
    text += 'Speed ' + str(npc.speed) + ' ft.; AC<AC>' + str(npc.AC) + '</AC>\n'
    text += '::Melee::' + npc.AttackMelee + ' or ' + npc.AttackRanged + ' ranged; '
    if (npc.FORT >= 0):
      text += 'SV: Fort +' + str(npc.FORT)
    else:
      text += 'SV: Fort ' + str(npc.FORT)
    if (npc.WILL >= 0):
      text += ', Will +' + str(npc.WILL)
    else:
      text += ', Will ' + str(npc.WILL)
    if (npc.REF >= 0):
      text += ', Ref +' + str(npc.REF)
    else:
      text += ', Ref ' + str(npc.REF)
    text += ';\nAlignment: '+ npc.Alignment + '; Str: '+str(npc.STR)+ ', Dex: '+str(npc.DEX)+', Con: '+str(npc.CON)+', Int: '+str(npc.INT)+', Wis: '+str(npc.WIS)+', Cha: '+str(npc.CHA)+';\n'
    text += 'Languages spoken: '
    for lang in npc.Languages:
      text += ' ' + lang
    text += '\n'
    text += 'Skills: '
    for index in range(len(npc.skills)):
      if (npc.ranks[index] > 0):
        text += str(npc.skills[index]) + ' +' + str(npc.ranks[index]) + ', '
    for index in range(len(npc.CCskills)):
      if (npc.CCranks[index] > 0):
        text += str(npc.CCskills[index]) + ' +' + str(npc.CCranks[index]) + ', '
    text += '\n'
    text += 'Feats: '
    for item in npc.Feats:
      text += item + ';  '

    #add the spells information
    if (npc.spells != 'Spells()\n'):
      text += (npc.spells + "\n")
      text += npc.spells_memorized

    return text

class MonstersDialog(PyMapperDialogs.MonstersDialogBase):
  def __init__(self, parent, showIndex=None, displayPoint=None):
    """
    If showIndex is set, hide the selection box, and show the monster info.
    Used for the hover dialog
    """
    olddir = os.getcwd()
    os.chdir(gv.root_directory)  #this is necessary so that bitmap paths are read by the dialog code correctly    
    PyMapperDialogs.MonstersDialogBase.__init__(self, parent)
    os.chdir(olddir)
    
    self.MonsterFilter = srd.Monster_Record()

    self.cbxSize.AppendItems(gv.NPC_Size)
    self.cbxType.AppendItems(gv.MonsterTypes)
    self.cbxSize.SetValue('Any')
    self.cbxType.SetValue('Any')
    self.txChallengeRating.SetValue('0')

    self.MonsterUniqueID = None
    
    self.monsterListPF = []
    self.BuildMonsterList()
    self.UpdateListBox()
    if (showIndex):
      position = displayPoint 
      position.x -= 30
      position.y -= 30
      self.Move(position)
      
      self.bAddMonster.Hide()
      self.bUpdateMonster.Hide()
      self.bDeleteMonster.Hide()
      self.pnFilterPanel.Hide()
      self.lbMonsterList.Hide()
      self.ID_CANCEL.Hide()
      self.ID_OK.Hide()
      self.bHelp.Hide()
      
      self.Fit()
      for m in self.monsterListPF:
        if (m.uniqueID == showIndex):
          self.AssignMonsterFields(m)
          break
    return

  def BuildMonsterList(self):
    self.monsterListPF = []
    for m in gv.MonsterList:
      if ((m.version == '5E_NPC') or (m.version == '5E') or (m.version == '5E_OLD')):
        continue  #skip 5th edition items
      else:
        m.show = True
        self.monsterListPF.append(m)
    return

  def UpdateListBox(self, event=None):
    i = 0
    m_list = []
    self.lbMonsterList.Clear()
    for monster in self.monsterListPF:
      if (monster.show):
        monster.index = i
        i += 1
        m_list.append(monster.name)
    self.lbMonsterList.AppendItems(m_list)
    return

  def EnableFilterCR(self, event):
    if (self.cbFilterByCR.IsChecked()):
      self.lbCRFilter.Enable(True)
    else:
      self.lbCRFilter.Enable(False)
    self.FilterMonsterList()
    return

  def EnableFilterMonsterType(self, event):
    if (self.cbFilterByMonsterType.IsChecked()):
      self.lbMonsterFilter.Enable(True)
    else:
      self.lbMonsterFilter.Enable(False)
    self.FilterMonsterList()
    return
  

  def ClearFilter(self, evt):
    self.FilterMonsterList(False)
    self.ClearFields()
    return

  def ClearFields(self, event=None):
    self.txFamily.Clear()
    self.txName.Clear()
    self.cbxSize.SetValue('Any')
    self.cbxType.SetValue('Any')
    self.txChallengeRating.SetValue('0')
    self.txHitDice.Clear()
    self.spInitiative.SetValue(0)
    self.txSpeed.Clear()
    self.txArmorClass.Clear()
    self.txBaseAttack.Clear()
    self.txGrapple.Clear()
    self.txAttack.Clear()
    self.txFullAttack.Clear()
    self.txSpace.Clear()
    self.txReach.Clear()
    self.txSpecialAttacks.Clear()
    self.txSpecialQualities.Clear()
    self.txSpecialAbilities.Clear()
    self.txTreasure.Clear()
    self.txAlignment.Clear()
    return

  def OnUpdateMonster(self, evt):
    # Replace with event handler code
    logging.error("OnButton_bUpdateMonster():  No code")
    return

  def OnOK(self, evt):
    self.EndModal(True)
    gv.SaveSRD_Monsters = True
    return

  def OnCancel(self, evt):
    self.EndModal(False)
    return

  def OnHelp(self, evt):
    text = "To add a new monster, fill in the values in the fields and select the 'Add New Monster' button.\n\nUser defined monsters (if any) will be saved when you click the OK button."
    dlg = HelpDialog(self, text)
    dlg.ShowModal()
    dlg.Destroy()

  def OnListbox_lbMonsterList(self, evt):
    index = self.lbMonsterList.GetSelection()
    if (index == wx.NOT_FOUND):
      return
    monsterName = self.lbMonsterList.GetString(index)
    for monster in gv.MonsterList:
      if (monster.name == monsterName) and (monster.version != '5E') and (monster.version != '5E_NPC'):
        break
    self.AssignMonsterFields(monster)
    if (monster.user_defined == True):
      self.bDeleteMonster.Enable(True)
      self.bUpdateMonster.Enable(True)
    else:
      self.bDeleteMonster.Enable(False)
      self.bUpdateMonster.Enable(False)

    return

  def AssignMonsterFields(self, item):
    '''item = srd.Monster_Record()
    '''
    self.txFamily.SetValue(item.family)
    self.txName.SetValue(item.name)
    self.cbxSize.SetValue(item.size)
    self.cbxType.SetValue(item.monster_type)
    self.txHitDice.SetValue(item.HD)
    self.spInitiative.SetValue(item.init)
    self.txSpeed.SetValue(item.speed)
    self.txArmorClass.SetValue(item.AC)
    self.txBaseAttack.SetValue(item.BAB)
    self.txGrapple.SetValue(item.grapple)
    self.txAttack.SetValue(item.attack)
    self.txFullAttack.SetValue(item.full_attack)
    self.txSpace.SetValue(item.space)
    self.txReach.SetValue(item.reach)
    self.txSpecialAttacks.SetValue(item.SA)
    self.txSpecialQualities.SetValue(item.SQ)
    self.txSpecialAbilities.SetValue(item.SA_text)
    self.spHitPoints.SetValue(item.HP)
    if (item.CR == 0.5):
      text = '1/2' 
    elif (item.CR == 0.25):
      text = '1/4' 
    elif (item.CR == 0.3):
      text = '1/3'
    elif (item.CR == 0.1):
      text = '1/10'
    elif (item.CR == 0.125):
      text = '1/8' 
    elif (item.CR == 0):
      text = '0' 
    elif (item.CR == 0.166):
      text = '1/6'
    else:
      text = str(item.CR)
    self.txChallengeRating.SetValue(text)
    self.txTreasure.SetValue(item.treasure)
    self.txAlignment.SetValue(item.alignment)
    self.MonsterUniqueID = item.uniqueID
    return

  def AddMonster(self, evt):
    NewMonster = srd.Monster_Record()
    NewMonster.user_defined = True
    NewMonster.family = self.txFamily.GetValue()
    NewMonster.name = self.txName.GetValue()
    NewMonster.size = self.cbxSize.GetValue()
    NewMonster.monster_type = self.cbxType.GetValue()
    NewMonster.HD = self.txHitDice.GetValue()
    NewMonster.init = self.spInitiative.GetValue()
    NewMonster.speed = self.txSpeed.GetValue()
    NewMonster.AC = self.txArmorClass.GetValue()
    NewMonster.BAB = self.txBaseAttack.GetValue()
    NewMonster.grapple = self.txGrapple.GetValue()
    NewMonster.attack = self.txAttack.GetValue()
    NewMonster.full_attack = self.txFullAttack.GetValue()
    NewMonster.space = self.txSpace.GetValue()
    NewMonster.reach = self.txReach.GetValue()
    NewMonster.SA = self.txSpecialAttacks.GetValue()
    NewMonster.SQ = self.txSpecialQualities.GetValue()
    NewMonster.SA_text = self.txSpecialAbilities.GetValue()
    NewMonster.CR = int(self.txChallengeRating.GetValue())
    NewMonster.treasure = self.txTreasure.GetValue()
    NewMonster.alignment = self.txAlignment.GetValue()
    NewMonster.uniqueID = gv.NextMonsterIndex
    gv.NextMonsterIndex += 1
    gv.MonsterList.append(NewMonster)
    self.BuildMonsterList()
    self.UpdateListBox()


  def OnDeleteMonster(self, evt):
    # Replace with event handler code
    logging.error("OnButton_bDeleteMonster():  No Code")
    return



  def FilterMonsterList(self, event=None):
    """SetFilter = True to filter according to the fields with an entry.
    SetFilter = False will clear the filter and show all entries."""
    CR_Filters = []
    MT_Filters = []
    filterItems = False
    filterItemsCR = False
    filterItemsMT = False
  
    if (self.cbFilterByCR.IsChecked()):
      CR_Filters = self.lbCRFilter.GetSelections()
      filterItemsCR = True
    if (self.cbFilterByMonsterType.IsChecked()):
      MT_Filters = self.lbMonsterFilter.GetSelections()
      filterItemsMT = True
  
    self.lbMonsterList.Clear()
  
    for monster in self.monsterListPF:
      monster.show = False
      if (filterItemsCR and filterItemsMT):
        for MTfilterItem in MT_Filters:
          if (self.CompareMonsterType(monster.monster_type, MTfilterItem)):
            for CRfilterItem in CR_Filters:
              if ((monster.CR == '1/8') or (monster.CR == '1/4') or (monster.CR == '1/2') or (monster.CR == '0')):
                if (CRfilterItem == 0):
                  monster.show = True
              elif (CRfilterItem == int(monster.CR)):
                monster.show = True
      elif (filterItemsMT):
        for MTfilterItem in MT_Filters:
          if (self.CompareMonsterType(monster.monster_type, MTfilterItem)):
            monster.show = True
      elif (filterItemsCR):
        for CRfilterItem in CR_Filters:
          if ((monster.CR == '1/8') or (monster.CR == '1/4') or (monster.CR == '1/2') or (monster.CR == '0')):
            if (CRfilterItem == 0):
              monster.show = True
          elif (CRfilterItem == int(monster.CR)):
            monster.show = True
      else:  #clear the filters
        monster.show = True
    self.UpdateListBox()
    return
  
  def CompareMonsterType(self, monsterType, monsterFilterID):
    monsterFilterName = None
    if (monsterFilterID == 0):
      monsterFilterName = 'Aberration'
    elif (monsterFilterID == 1):
      monsterFilterName = 'Beast'
    elif (monsterFilterID == 2):
      monsterFilterName = 'Celestial'
    elif (monsterFilterID == 3):
      monsterFilterName = 'Construct'
    elif (monsterFilterID == 4):
      monsterFilterName = 'Dragon'
    elif (monsterFilterID == 5):
      monsterFilterName = 'Elemental'
    elif (monsterFilterID == 6):
      monsterFilterName = 'Fey'
    elif (monsterFilterID == 7):
      monsterFilterName = 'Fiend'
    elif (monsterFilterID == 8):
      monsterFilterName = 'Giant'
    elif (monsterFilterID == 9):
      monsterFilterName = 'Humanoid'
    elif (monsterFilterID == 10):
      monsterFilterName = 'Monstrosity'
    elif (monsterFilterID == 11):
      monsterFilterName = 'Ooze'
    elif (monsterFilterID == 12):
      monsterFilterName = 'Plant'
    elif (monsterFilterID == 13):
      monsterFilterName = 'Undead'

    if (monsterFilterName == monsterType):
      return True
    else:
      return False
  
class Monsters5EDialog(PyMapperDialogs.Monsters5E_DialogBase):
  """recordType may be either 5E_NPC or 5E (which is treated as a monster internal to pymapper)
     Note that both monsters and NPC's are stored in the monsters list.  The
     recordType is used to filter the records
  """
  def __init__(self, parent, recordType):
    olddir = os.getcwd()
    os.chdir(gv.root_directory)  #this is necessary so that bitmap paths are read by the dialog code correctly
    PyMapperDialogs.Monsters5E_DialogBase.__init__(self, parent)
    os.chdir(olddir)
    
    self.recordType = recordType
    if (self.recordType == '5E_NPC'):
      self.SetLabel("Fifth Edition NPC Editor")
      self.stRecordType.SetLabel("NPC Name")
      self.bNewMonster.SetLabel("New NPC")
      self.bUpdateMonster.SetLabel("Update NPC")
      self.bDeleteMonster.SetLabel("Delete NPC")
      self.chRace.Show()
      self.chClass.Show()
      self.stTypeOrRace.SetLabel("Race")
      self.stCRorLevel.SetLabel("Level")
    elif (self.recordType == '5E'):
      self.SetLabel("Fifth Edition Monster Editor")
      self.stRecordType.SetLabel("Monster Name")
      self.bNewMonster.SetLabel("New Monster")
      self.chClass.Hide()
      self.stClass.Hide()
      self.chType.Show()
      self.stTypeOrRace.SetLabel("Type")
      self.stCRorLevel.SetLabel("Challenge Rating:")

    self.MonsterUniqueID = None  #unique id of the monster currently selected
    self.chSize.SetSelection(2)
    self.chType.SetSelection(9)
    self.txChallengeRating.SetValue('1')
    self.bUpdateMonster.Enable(False)
    self.bbSelectCustomImage.Enable(False)
    
    if (gv.PymapperUser):
      self.cbBasicMonster.Enable(True)
    else:
      self.cbBasicMonster.Enable(False)
    
    #unpack the spell list information
    self.SpellRootMain = self.trAllSpellList.AddRoot("Available Spells")
    self.CantripsRootMain = self.trAllSpellList.AppendItem(self.SpellRootMain, "Cantrips")
    self.Level1RootMain = self.trAllSpellList.AppendItem(self.SpellRootMain, "Level 1 Spells")
    self.Level2RootMain = self.trAllSpellList.AppendItem(self.SpellRootMain, "Level 2 Spells")
    self.Level3RootMain = self.trAllSpellList.AppendItem(self.SpellRootMain, "Level 3 Spells")
    self.Level4RootMain = self.trAllSpellList.AppendItem(self.SpellRootMain, "Level 4 Spells")
    self.Level5RootMain = self.trAllSpellList.AppendItem(self.SpellRootMain, "Level 5 Spells")
    self.Level6RootMain = self.trAllSpellList.AppendItem(self.SpellRootMain, "Level 6 Spells")
    self.Level7RootMain = self.trAllSpellList.AppendItem(self.SpellRootMain, "Level 7 Spells")
    self.Level8RootMain = self.trAllSpellList.AppendItem(self.SpellRootMain, "Level 8 Spells")
    self.Level9RootMain = self.trAllSpellList.AppendItem(self.SpellRootMain, "Level 9 Spells")
    
    if (self.recordType == '5E'):
      self.SpellRootMonster = self.trCreatureSpellList.AddRoot("Monster Spells")
    else:
      self.SpellRootMonster = self.trCreatureSpellList.AddRoot("NPC Spells")
    self.CantripsRootMonster = self.trCreatureSpellList.AppendItem(self.SpellRootMonster, "Cantrips")
    self.Level1RootMonster = self.trCreatureSpellList.AppendItem(self.SpellRootMonster, "Level 1 Spells")
    self.Level2RootMonster = self.trCreatureSpellList.AppendItem(self.SpellRootMonster, "Level 2 Spells")
    self.Level3RootMonster = self.trCreatureSpellList.AppendItem(self.SpellRootMonster, "Level 3 Spells")
    self.Level4RootMonster = self.trCreatureSpellList.AppendItem(self.SpellRootMonster, "Level 4 Spells")
    self.Level5RootMonster = self.trCreatureSpellList.AppendItem(self.SpellRootMonster, "Level 5 Spells")
    self.Level6RootMonster = self.trCreatureSpellList.AppendItem(self.SpellRootMonster, "Level 6 Spells")
    self.Level7RootMonster = self.trCreatureSpellList.AppendItem(self.SpellRootMonster, "Level 7 Spells")
    self.Level8RootMonster = self.trCreatureSpellList.AppendItem(self.SpellRootMonster, "Level 8 Spells")
    self.Level9RootMonster = self.trCreatureSpellList.AppendItem(self.SpellRootMonster, "Level 9 Spells")
    self.spellSlots = {'Slot0':'0','Slot1':'0', 'Slot2':'0','Slot3':'0','Slot4':'0','Slot5':'0','Slot6':'0','Slot7':'0','Slot8':'0','Slot9':'0'}
    self.spells = {'Level0': [],'Level1': [],'Level2': [],'Level3': [],'Level4': [],'Level5': [],'Level6': [],'Level7': [],'Level8': [],'Level9': []}
    
    self.UpdateMainSpellBook()
    
    self.trCreatureSpellList.Enable(False)
    self.trAllSpellList.Enable(False)
    self.stSpellFilterText.Enable(False)
    self.cbxSpellFilter.Enable(False)
    
    self.stSpellAttack.Enable(False)
    self.stSpellDC.Enable(False)
    self.spSpellAttack.Enable(False)
    self.spSpellDC.Enable(False)
    
    self.monsterList5E = []
    self.BuildMonsterList()
    
    self.proficencySkills = []  #updates as skills are checked or unchecked
    
    self.UpdateListBox()
    self.UpdateSkills()
    self.updateMasterMonsterList = False #set to True if we need to save the master file on disk
    self.Fit()
    self.MoveXY(0,0)
    return
  
  def OnSelectCustomImage(self, event):
    """Selects a custom image for display on the map window"""
    dlg = wx.FileDialog(self, message="Choose custom image", defaultDir=gv.tokens_directory,
                        defaultFile="", wildcard=images_wildcard, style=wx.OPEN | wx.CHANGE_DIR)
    if (dlg.ShowModal()==wx.ID_OK):
      filename = dlg.GetFilename()
      dlg.Destroy()
      
      #find the monster record selected
      monsterName = self.lbMonsterList.GetStringSelection()
      if (monsterName == wx.NOT_FOUND):
        return
      if (self.recordType == '5E'):
        for monster in gv.Monsters5E:
          if (monster.name == monsterName) and (monster.version == self.recordType):
            break
      elif (self.recordType == '5E_NPC'):
        for monster in gv.NPC_5E:
          if (monster.name == monsterName) and (monster.version == self.recordType):
            break
      else:
        return  #wrong record type for some reason
      
      image = wx.Image(os.path.join(gv.tokens_directory,filename), wx.BITMAP_TYPE_ANY)
      monster.filename = filename
      #set the image for the monster on the selector button
      xsize = image.GetWidth()
      if (xsize != 100): #resize the image
        image = image.Scale(100, 100)
      bmp = wx.BitmapFromImage(image)
      self.bbSelectCustomImage.SetBitmapLabel(bmp)
    return

  def ChangeSpellListFilter(self, event):
    self.UpdateMainSpellBook()
    return
  
  def OnCalculateHP(self, event):
    diceroll = self.txHitDice.GetValue()
    total = app.RollDice(diceroll)
    if (total):
      self.spHitPoints.SetValue(total)
    else:
      wx.MessageBox("Invalid format for dice roll")
    return
  
  def Roll3d6(self):
    total = app.RollDice('3d6')
    return total
  
  def Roll4d6x(self):
    v1 = app.RollDice('1d6')
    v2 = app.RollDice('1d6')
    v3 = app.RollDice('1d6')
    v4 = app.RollDice('1d6')
    results = []
    results.append(v1)
    results.append(v2)
    results.append(v3)
    results.append(v4)
    results.sort()
    total = (results[1] + results[2] + results[3])
    return total
  
  def Roll5d6xx(self):
    v1 = app.RollDice('1d6')
    v2 = app.RollDice('1d6')
    v3 = app.RollDice('1d6')
    v4 = app.RollDice('1d6')
    v5 = app.RollDice('1d6')
    results = []
    results.append(v1)
    results.append(v2)
    results.append(v3)
    results.append(v4)
    results.append(v5)
    results.sort()
    total = (results[2] + results[3] + results[4])
    return total
    
  
  def OnRandomizeStats(self, event):
    method = self.cxRandomizeSetting.GetString(0)
    if (method == 'Straight 3d6'):
      self.txStr.SetValue(str(self.Roll3d6()))
      self.txInt.SetValue(str(self.Roll3d6()))
      self.txDex.SetValue(str(self.Roll3d6()))
      self.txCon.SetValue(str(self.Roll3d6()))
      self.txWis.SetValue(str(self.Roll3d6()))
      self.txCha.SetValue(str(self.Roll3d6()))
    elif (method == '4d6, Drop Lowest'):
      self.txStr.SetValue(str(self.Roll4d6x()))
      self.txInt.SetValue(str(self.Roll4d6x()))
      self.txDex.SetValue(str(self.Roll4d6x()))
      self.txCon.SetValue(str(self.Roll4d6x()))
      self.txWis.SetValue(str(self.Roll4d6x()))
      self.txCha.SetValue(str(self.Roll4d6x()))
    elif (method == '5d6, Drop Two Lowest'):
      self.txStr.SetValue(str(self.Roll5d6xx()))
      self.txInt.SetValue(str(self.Roll5d6xx()))
      self.txDex.SetValue(str(self.Roll5d6xx()))
      self.txCon.SetValue(str(self.Roll5d6xx()))
      self.txWis.SetValue(str(self.Roll5d6xx()))
      self.txCha.SetValue(str(self.Roll5d6xx()))
    return

  def OnSpellcasterCheckbox(self, event):
    if (self.cbSpellcaster.IsChecked()):
      self.stSpellAttack.Enable(True)
      self.stSpellDC.Enable(True)
      self.spSpellAttack.Enable(True)
      self.spSpellDC.Enable(True)
      self.trCreatureSpellList.Enable(True)
      self.trAllSpellList.Enable(True)
      self.stSpellFilterText.Enable(True)
      self.cbxSpellFilter.Enable(True)
      self.trAllSpellList.Expand(self.SpellRootMain)
      self.trCreatureSpellList.Expand(self.SpellRootMonster)
      if (self.spells == []):  #self.spells = [] if no spells had previously been assigned to the monster
        self.spells = {'Level0': [],'Level1': [],'Level2': [],'Level3': [],'Level4': [],'Level5': [],'Level6': [],'Level7': [],'Level8': [],'Level9': []}
        self.spellSlots = {'Slot0':'0','Slot1':'0', 'Slot2':'0','Slot3':'0','Slot4':'0','Slot5':'0','Slot6':'0','Slot7':'0','Slot8':'0','Slot9':'0'}

    else:
      self.stSpellAttack.Enable(False)
      self.stSpellDC.Enable(False)
      self.spSpellAttack.Enable(False)
      self.spSpellDC.Enable(False)
      self.trCreatureSpellList.Enable(False)
      self.trAllSpellList.Enable(False)
      self.stSpellFilterText.Enable(False)
      self.cbxSpellFilter.Enable(False)
    return
  
  def OnSelectSpellItemMain(self, event):
    """User double clicked a spell in the master tree, so add it to the list for the monster/npc"""
    spellName = self.trAllSpellList.GetItemText(self.trAllSpellList.GetSelection())
    if (spellName in ['Available Spells', 'Cantrips', 'Level 1 Spells', 'Level 2 Spells', 'Level 3 Spells', 
                      'Level 4 Spells', 'Level 5 Spells', 'Level 6 Spells', 'Level 7 Spells', 'Level 8 Spells', 'Level 9 Spells']):
      #Do nothing if the title item was selected
      self.txSpellDescription.Clear()
    else:
      for spell in gv.Spells5E:
        if (spell.Name == spellName):
          self.txSpellDescription.SetValue(spell.Description)
          break
      if (spell.Level == 0):
        self.trAllSpellList.AppendItem(self.CantripsRootMonster, spell.Name)
        self.spells['Level0'].append(spell.Name)
      elif (spell.Level == 1):
        self.trAllSpellList.AppendItem(self.Level1RootMonster, spell.Name)
        self.spells['Level1'].append(spell.Name)
      elif (spell.Level == 2):
        self.trAllSpellList.AppendItem(self.Level2RootMonster, spell.Name)
        self.spells['Level2'].append(spell.Name)
      elif (spell.Level == 3):
        self.trAllSpellList.AppendItem(self.Level3RootMonster, spell.Name)
        self.spells['Level3'].append(spell.Name)
      elif (spell.Level == 4):
        self.trAllSpellList.AppendItem(self.Level4RootMonster, spell.Name)
        self.spells['Level4'].append(spell.Name)
      elif (spell.Level == 5):
        self.trAllSpellList.AppendItem(self.Level5RootMonster, spell.Name)
        self.spells['Level5'].append(spell.Name)
      elif (spell.Level == 6):
        self.trAllSpellList.AppendItem(self.Level6RootMonster, spell.Name)
        self.spells['Level6'].append(spell.Name)
      elif (spell.Level == 7):
        self.trAllSpellList.AppendItem(self.Level7RootMonster, spell.Name)
        self.spells['Level7'].append(spell.Name)
      elif (spell.Level == 8):
        self.trAllSpellList.AppendItem(self.Level8RootMonster, spell.Name)
        self.spells['Level8'].append(spell.Name)
      elif (spell.Level == 9):
        self.trAllSpellList.AppendItem(self.Level9RootMonster, spell.Name)
        self.spells['Level9'].append(spell.Name)
      self.trCreatureSpellList.Refresh()
    return
  
  def OnSelectSpellItemMonster(self, event):
    """If User double clicked on a spell in the monster/npc list, remove it from the list.
       If the spell level was selected, then change the number of slots available."""
    treeItem = self.trCreatureSpellList.GetSelection()
    selection = self.trCreatureSpellList.GetItemText(treeItem)
    if (treeItem == self.CantripsRootMonster):
      #shows the number of cantrips known
      dlg = wx.TextEntryDialog(self, 'How many cantrips are known?','Change number of cantrips known', '')
      if (dlg.ShowModal() == wx.ID_OK):
        slots = dlg.GetValue()
        name = "Cantrips ("+str(slots) + " known)"
        self.spellSlots['Slot0'] = slots
        self.trCreatureSpellList.SetItemText(treeItem, name)
        dlg.Destroy()
    elif (treeItem == self.Level1RootMonster):
      #adjust the number of slots available
      dlg = wx.TextEntryDialog(self, 'How many spell slots for this level of spell?','Change spell slots', '')
      if (dlg.ShowModal() == wx.ID_OK):
        slots = dlg.GetValue()
        name = "Level 1 Spells ("+str(slots) + " slots)"
        self.spellSlots['Slot1'] = slots
        self.trCreatureSpellList.SetItemText(treeItem, name)
        dlg.Destroy()
    elif (treeItem == self.Level2RootMonster):
      #adjust the number of slots available
      dlg = wx.TextEntryDialog(self, 'How many spell slots for this level of spell?','Change spell slots', '')
      if (dlg.ShowModal() == wx.ID_OK):
        slots = dlg.GetValue()
        name = "Level 2 Spells ("+str(slots) + " slots)"
        self.spellSlots['Slot2'] = slots
        self.trCreatureSpellList.SetItemText(treeItem, name)
        dlg.Destroy()
    elif (treeItem == self.Level3RootMonster):
      #adjust the number of slots available
      dlg = wx.TextEntryDialog(self, 'How many spell slots for this level of spell?','Change spell slots', '')
      if (dlg.ShowModal() == wx.ID_OK):
        slots = dlg.GetValue()
        name = "Level 3 Spells ("+str(slots) + " slots)"
        self.spellSlots['Slot3'] = slots
        self.trCreatureSpellList.SetItemText(treeItem, name)
        dlg.Destroy()
    elif (treeItem == self.Level4RootMonster):
      #adjust the number of slots available
      dlg = wx.TextEntryDialog(self, 'How many spell slots for this level of spell?','Change spell slots', '')
      if (dlg.ShowModal() == wx.ID_OK):
        slots = dlg.GetValue()
        name = "Level 4 Spells ("+str(slots) + " slots)"
        self.spellSlots['Slot4'] = slots
        self.trCreatureSpellList.SetItemText(treeItem, name)
        dlg.Destroy()
    elif (treeItem == self.Level5RootMonster):
      #adjust the number of slots available
      dlg = wx.TextEntryDialog(self, 'How many spell slots for this level of spell?','Change spell slots', '')
      if (dlg.ShowModal() == wx.ID_OK):
        slots = dlg.GetValue()
        name = "Level 5 Spells ("+str(slots) + " slots)"
        self.spellSlots['Slot5'] = slots
        self.trCreatureSpellList.SetItemText(treeItem, name)
        dlg.Destroy()
    elif (treeItem == self.Level6RootMonster):
      #adjust the number of slots available
      dlg = wx.TextEntryDialog(self, 'How many spell slots for this level of spell?','Change spell slots', '')
      if (dlg.ShowModal() == wx.ID_OK):
        slots = dlg.GetValue()
        name = "Level 6 Spells ("+str(slots) + " slots)"
        self.spellSlots['Slot6'] = slots
        self.trCreatureSpellList.SetItemText(treeItem, name)
        dlg.Destroy()
    elif (treeItem == self.Level7RootMonster):
      #adjust the number of slots available
      dlg = wx.TextEntryDialog(self, 'How many spell slots for this level of spell?','Change spell slots', '')
      if (dlg.ShowModal() == wx.ID_OK):
        slots = dlg.GetValue()
        name = "Level 7 Spells ("+str(slots) + " slots)"
        self.spellSlots['Slot7'] = slots
        self.trCreatureSpellList.SetItemText(treeItem, name)
        dlg.Destroy()
    elif (treeItem == self.Level8RootMonster):
      #adjust the number of slots available
      dlg = wx.TextEntryDialog(self, 'How many spell slots for this level of spell?','Change spell slots', '')
      if (dlg.ShowModal() == wx.ID_OK):
        slots = dlg.GetValue()
        name = "Level 8 Spells ("+str(slots) + " slots)"
        self.spellSlots['Slot8'] = slots
        self.trCreatureSpellList.SetItemText(treeItem, name)
        dlg.Destroy()
    elif (treeItem == self.Level9RootMonster):
      #adjust the number of slots available
      dlg = wx.TextEntryDialog(self, 'How many spell slots for this level of spell?','Change spell slots', '')
      if (dlg.ShowModal() == wx.ID_OK):
        slots = dlg.GetValue()
        name = "Level 9 Spells ("+str(slots) + " slots)"
        self.spellSlots['Slot9'] = slots
        self.trCreatureSpellList.SetItemText(treeItem, name)
        dlg.Destroy()
    else:
      #One of the spells were selected; remove the spell on a double click
      self.trCreatureSpellList.Delete(treeItem)
    return
  
  def OnDisplaySpell(self, event):
    """User clicked on a spell, so show the spell text in the description box"""
    if (event.GetId() == PyMapperDialogs.trAllSpellListID):
      #get the name of the spell selected
      spellName = self.trAllSpellList.GetItemText(self.trAllSpellList.GetSelection())
    elif (event.GetId() == PyMapperDialogs.trCreatureSpellListID):
      spellName = self.trCreatureSpellList.GetItemText(self.trCreatureSpellList.GetSelection())
    if (spellName in ['Available Spells', 'Cantrips', 'Level 1 Spells', 'Level 2 Spells', 'Level 3 Spells', 
                      'Level 4 Spells', 'Level 5 Spells', 'Level 6 Spells', 'Level 7 Spells', 'Level 8 Spells', 'Level 9 Spells']):
      self.txSpellDescription.Clear()
      return
    else:
      for spell in gv.Spells5E:
        if (spell.Name == spellName):
          self.txSpellDescription.SetValue(spell.Description)
          break
    return
  
  def ClearMonsterSpellBook(self):
    """Clear the spells in the monster list"""
    self.trCreatureSpellList.DeleteChildren(self.CantripsRootMonster)
    self.trCreatureSpellList.DeleteChildren(self.Level1RootMonster)
    self.trCreatureSpellList.DeleteChildren(self.Level2RootMonster)
    self.trCreatureSpellList.DeleteChildren(self.Level3RootMonster)
    self.trCreatureSpellList.DeleteChildren(self.Level4RootMonster)
    self.trCreatureSpellList.DeleteChildren(self.Level5RootMonster)
    self.trCreatureSpellList.DeleteChildren(self.Level6RootMonster)
    self.trCreatureSpellList.DeleteChildren(self.Level7RootMonster)
    self.trCreatureSpellList.DeleteChildren(self.Level8RootMonster)
    self.trCreatureSpellList.DeleteChildren(self.Level9RootMonster)
    return

  
  def UpdateMainSpellBook(self):
    """Update the main spell list, and filter as indicated"""
    self.trAllSpellList.DeleteChildren(self.CantripsRootMain)
    self.trAllSpellList.DeleteChildren(self.Level1RootMain)
    self.trAllSpellList.DeleteChildren(self.Level2RootMain)
    self.trAllSpellList.DeleteChildren(self.Level3RootMain)
    self.trAllSpellList.DeleteChildren(self.Level4RootMain)
    self.trAllSpellList.DeleteChildren(self.Level5RootMain)
    self.trAllSpellList.DeleteChildren(self.Level6RootMain)
    self.trAllSpellList.DeleteChildren(self.Level7RootMain)
    self.trAllSpellList.DeleteChildren(self.Level8RootMain)
    self.trAllSpellList.DeleteChildren(self.Level9RootMain)
    spellFilter = self.cbxSpellFilter.GetStringSelection()
    for spell in gv.Spells5E:
      if (spellFilter == 'All Classes'):  #add all spells
        showSpell = True
      elif (spellFilter in spell.CasterClass):
        showSpell = True
      else:
        showSpell = False

      if (showSpell):
        if (spell.Level == 0):
          self.trAllSpellList.AppendItem(self.CantripsRootMain, spell.Name)
        elif (spell.Level == 1):
          self.trAllSpellList.AppendItem(self.Level1RootMain, spell.Name)
        elif (spell.Level == 2):
          self.trAllSpellList.AppendItem(self.Level2RootMain, spell.Name)
        elif (spell.Level == 3):
          self.trAllSpellList.AppendItem(self.Level3RootMain, spell.Name)
        elif (spell.Level == 4):
          self.trAllSpellList.AppendItem(self.Level4RootMain, spell.Name)
        elif (spell.Level == 5):
          self.trAllSpellList.AppendItem(self.Level5RootMain, spell.Name)
        elif (spell.Level == 6):
          self.trAllSpellList.AppendItem(self.Level6RootMain, spell.Name)
        elif (spell.Level == 7):
          self.trAllSpellList.AppendItem(self.Level7RootMain, spell.Name)
        elif (spell.Level == 8):
          self.trAllSpellList.AppendItem(self.Level8RootMain, spell.Name)
        elif (spell.Level == 9):
          self.trAllSpellList.AppendItem(self.Level9RootMain, spell.Name)
    return
  
  
  def BuildMonsterList(self):
    """Build the custom monster list to filter out non-5E items, or 5E items that are not in the Basic rules"""
    self.monsterList5E = []
    if (self.recordType == '5E'):
      for m in gv.Monsters5E:
        if (m.user_defined) or (m.BasicMonster) or (m.SRD_Distribution):  #show only those monsters defined by the user
          m.show = True
          self.monsterList5E.append(m)
        elif (gv.PymapperUser):  #show all monsters defined by pymapper
          m.show = True
          self.monsterList5E.append(m)
        else:
          m.show = False
    elif (self.recordType == '5E_NPC'):
      for m in gv.NPC_5E:
        m.show = True 
        self.monsterList5E.append(m)
    return

  def UpdateXPfromCR(self, event):
    CRvalue = self.txChallengeRating.GetValue()
    XPvalue = 0
    if (CRvalue == '0'):
      XPvalue = 10
    elif (CRvalue == '1/8'):
      XPvalue = 25
    elif (CRvalue == '1/4'):
      XPvalue = 50
    elif (CRvalue == '1/2'):
      XPvalue = 100
    elif (CRvalue == '1'):
      XPvalue = 200
    elif (CRvalue == '2'):
      XPvalue = 450
    elif (CRvalue == '3'):
      XPvalue = 700
    elif (CRvalue == '4'):
      XPvalue = 1100
    elif (CRvalue == '5'):
      XPvalue = 1800
    elif (CRvalue == '6'):
      XPvalue = 2300
    elif (CRvalue == '7'):
      XPvalue = 2900
    elif (CRvalue == '8'):
      XPvalue = 3900
    elif (CRvalue == '9'):
      XPvalue = 5000
    elif (CRvalue == '10'):
      XPvalue = 5900
    elif (CRvalue == '11'):
      XPvalue = 7200
    elif (CRvalue == '12'):
      XPvalue = 8400
    elif (CRvalue == '13'):
      XPvalue = 10000
    elif (CRvalue == '14'):
      XPvalue = 11500
    elif (CRvalue == '15'):
      XPvalue = 13000
    elif (CRvalue == '16'):
      XPvalue = 15000
    elif (CRvalue == '17'):
      XPvalue = 18000
    elif (CRvalue == '18'):
      XPvalue = 20000
    elif (CRvalue == '19'):
      XPvalue = 22000
    elif (CRvalue == '20'):
      XPvalue = 25000
    elif (CRvalue == '21'):
      XPvalue = 33000
    elif (CRvalue == '22'):
      XPvalue = 41000
    elif (CRvalue == '23'):
      XPvalue = 50000
    elif (CRvalue == '24'):
      XPvalue = 62000
    elif (CRvalue == '25'):
      XPvalue = 75000
    elif (CRvalue == '26'):
      XPvalue = 90000
    elif (CRvalue == '27'):
      XPvalue = 105000
    elif (CRvalue == '28'):
      XPvalue = 120000
    elif (CRvalue == '29'):
      XPvalue = 135000
    elif (CRvalue == '30'):
      XPvalue = 155000
    self.txXPValue.SetValue(str(XPvalue))
    return
    
  def EnableFilterCR(self, event):
    if (self.cbFilterByCR.IsChecked()):
      self.lbCRFilter.Enable(True)
    else:
      self.lbCRFilter.Enable(False)
    self.FilterMonsterList()
    return
  
  def EnableFilterMonsterType(self, event):
    if (self.cbFilterByMonsterType.IsChecked()):
      self.lbMonsterFilter.Enable(True)
    else:
      self.lbMonsterFilter.Enable(False)
    self.FilterMonsterList()
    return
  
  def FilterMonsterList(self, event=None):
    CR_Filters = []
    MT_Filters = []
    filterItems = False
    filterItemsCR = False
    filterItemsMT = False
    filterItemsCustom = self.cbShowOnlyUserMonsters.IsChecked()
    
    if (self.cbFilterByCR.IsChecked()):
      CR_Filters = self.lbCRFilter.GetSelections()
      filterItemsCR = True
    if (self.cbFilterByMonsterType.IsChecked()):
      MT_Filters = self.lbMonsterFilter.GetSelections()
      filterItemsMT = True
    
    self.lbMonsterList.Clear()

    for monster in self.monsterList5E:
      monster.show = False
      if (filterItemsCustom and monster.BasicMonster):
        continue
      if (filterItemsCR and filterItemsMT):
        for MTfilterItem in MT_Filters:
          if (MTfilterItem == monster.monster_type):
            for CRfilterItem in CR_Filters:
              if ((monster.CR == '1/8') or (monster.CR == '1/4') or (monster.CR == '1/2') or (monster.CR == '0')):
                if (CRfilterItem == 0):
                  monster.show = True
              elif (CRfilterItem == int(monster.CR)):
                monster.show = True
      elif (filterItemsMT):
        for MTfilterItem in MT_Filters:
          if (MTfilterItem == monster.monster_type):
            monster.show = True
      elif (filterItemsCR):
        for CRfilterItem in CR_Filters:
          if ((monster.CR == '1/8') or (monster.CR == '1/4') or (monster.CR == '1/2') or (monster.CR == '0')):
            if (CRfilterItem == 0):
              monster.show = True
          elif (CRfilterItem == int(monster.CR)):
            monster.show = True
      else:  #clear the filters
        monster.show = True
    self.UpdateListBox()
    return

  def OnResetFields(self, event=None):
    self.txName.SetValue("New Monster")
    self.chSize.SetSelection(2)
    self.chType.SetSelection(9)
    self.txChallengeRating.SetValue("1")
    self.txXPValue.SetValue("200")
    self.txAlignment.SetValue("Any")
    self.spHitPoints.SetValue(1)
    self.txHitDice.SetValue("1d8")
    self.txPassivePerception.SetValue("10")
    self.txSpeed.SetValue("30")
    self.txStr.SetValue("9")
    self.txInt.SetValue("9")
    self.txDex.SetValue("9")
    self.txWis.SetValue("9")
    self.txCha.SetValue("9")
    self.txCon.SetValue("9")
    self.txActions.SetValue("")
    self.txOtherFeatures.SetValue("")
    self.txBonds.SetValue("")
    self.txIdeals.SetValue("")
    self.txTraits.SetValue("")
    self.txFlaws.SetValue("")
    
    #reset Attributes tab
    self.txSaves.SetValue("")
    self.txResistances.SetValue("")
    self.txVulnerability.SetValue("")
    self.txImmunity.SetValue("")
    self.txConditionImmunity.SetValue("")
    self.txSenses.SetValue("")

    #reset spell lists
    self.cbSpellcaster.SetValue(False)
    self.stSpellFilterText.Enable(False)
    self.cbxSpellFilter.Enable(False)
    self.trCreatureSpellList.Enable(False)
    self.trAllSpellList.Enable(False)
    self.spellSlots = {'Slot0':'0','Slot1':'0', 'Slot2':'0','Slot3':'0','Slot4':'0','Slot5':'0','Slot6':'0','Slot7':'0','Slot8':'0','Slot9':'0'}
    self.spells = {'Level0': [],'Level1': [],'Level2': [],'Level3': [],'Level4': [],'Level5': [],'Level6': [],'Level7': [],'Level8': [],'Level9': []}
    self.UpdateMainSpellBook()
    
    self.bUpdateMonster.Enable(False)
    self.bAddMonster.Enable(False)
    self.bDeleteMonster.Enable(False)
    self.bCopyMonster.Enable(False)
    
    self.proficencySkills = []
    self.cbSkill_Acrobatics.SetValue(False)
    self.cbSkill_AnimalHandling.SetValue(False)
    self.cbSkill_Arcana.SetValue(False)
    self.cbSkill_Deception.SetValue(False)
    self.cbSkill_History.SetValue(False)
    self.cbSkill_Insight.SetValue(False)
    self.cbSkill_Intimidation.SetValue(False)
    self.cbSkill_Investigation.SetValue(False)
    self.cbSkill_Medicine.SetValue(False)
    self.cbSkill_Nature.SetValue(False)
    self.cbSkill_Perception.SetValue(False)
    self.cbSkill_Performance.SetValue(False)
    self.cbSkill_Persuasion.SetValue(False)
    self.cbSkill_Religion.SetValue(False)
    self.cbSkill_SleightOfHand.SetValue(False)
    self.cbSkill_Stealth.SetValue(False)
    self.cbSkill_Survival.SetValue(False)
    return
  
  def OnMonsterNamed(self, event=None):
    self.bUpdateMonster.Enable(True)
    self.bAddMonster.Enable(True)
    return

  def UpdateListBox(self, event=None):
    i = 0
    m_list = []
    self.lbMonsterList.Clear()
    for monster in self.monsterList5E:
      if (monster.show) and (monster.version != 'DELETED'):
        monster.index = i
        i += 1
        m_list.append(monster.name)
    self.lbMonsterList.AppendItems(m_list)
    return

  def OnNewMonster(self, evt):
    self.ClearSelection()
    self.bDeleteMonster.Enable(False)
    self.bUpdateMonster.Enable(False)
    return

  def OnUpdateMonster(self, evt):
    """Updates the selected monster from the list"""
    updateValue = 0
    index = self.lbMonsterList.GetSelection()
    if (index == wx.NOT_FOUND):
      return
    
    updateValue+=20
    self.gxUpdateGauge.SetValue(updateValue)
    
    monsterName = self.lbMonsterList.GetString(index)
    if (self.recordType == '5E'):
      for monster in gv.Monsters5E:
        if (monster.name == monsterName) and (monster.version == self.recordType):
          break
    elif (self.recordType == '5E_NPC'):
      for monster in gv.NPC_5E:
        if (monster.name == monsterName) and (monster.version == self.recordType):
          break
    else:
      return  #wrong record type for some reason
      
    monster.version = self.recordType
    # monster.user_defined = True    #do not update the user_defined field, as this may be a correction to an existing monster
    monster.name = self.txName.GetValue() 
    if (self.recordType == '5E_NPC'):
      monster.npc_race = self.chRace.GetSelection()
      monster.npc_class = self.chClass.GetSelection()
    else:  #self.recordType == '5E'
      monster.monster_type = self.chType.GetSelection()
    
    monster.size = self.chSize.GetSelection()
    monster.speed = self.txSpeed.GetValue()
    monster.AC = self.spACValue.GetValue()
    monster.passive_perception = self.txPassivePerception.GetValue()
    monster.HP = self.spHitPoints.GetValue()
    monster.startHP = self.spHitPoints.GetValue()
    monster.HD = self.txHitDice.GetValue()
    monster.XP = self.txXPValue.GetValue()
    monster.STR = self.txStr.GetValue()
    monster.DEX = self.txDex.GetValue()
    monster.INT = self.txInt.GetValue()
    monster.WIS = self.txWis.GetValue()
    monster.CON = self.txCon.GetValue()
    monster.CHA = self.txCha.GetValue()
    
    monster.CR = self.txChallengeRating.GetValue()
    monster.proficiency = self.spProficiency.GetValue()
    monster.proficiencySkills = self.proficencySkills
    
    #update spell listings from selected spells
    if (self.cbSpellcaster.IsChecked()):
      monster.spellAttackDC = self.spSpellAttack.GetValue()
      monster.spellSaveDC = self.spSpellDC.GetValue()
      monster.spells = copy.deepcopy(self.spells)
      monster.spellSlots = copy.deepcopy(self.spellSlots)
    else:
      monster.spells = []
      monster.spellSlots = []
    
    monster.alignment = self.txAlignment.GetValue()
    monster.actions = self.txActions.GetValue()
    monster.legendaryAction = self.txLegendaryActions.GetValue()
    monster.other_text = self.txOtherFeatures.GetValue()
    monster.BasicMonster = self.cbBasicMonster.GetValue()
    monster.bonds = self.txBonds.GetValue()
    monster.flaws = self.txFlaws.GetValue()
    monster.ideals = self.txIdeals.GetValue()
    monster.trait = self.txTraits.GetValue()
    monster.userNotes = self.txNotes.GetValue()
    
    for updateValue in range(0,100,5):
      self.gxUpdateGauge.SetValue(updateValue)
      time.sleep(0.001)
    self.gxUpdateGauge.SetValue(0)
    
    self.updateMasterMonsterList = True
    return
  
  def UpdateSkills (self, event=None):
    if (self.recordType != '5E_NPC'):  #do not update if we editing a monster
      return
    """Update the skills information.  Checked items add the proficiency bonus to the skill"""
    proficiency = self.spProficiency.GetValue()
    bonusSTR = srd.GetAbilityScoreBonus(int(self.txStr.GetValue()))
    bonusINT = srd.GetAbilityScoreBonus(int(self.txInt.GetValue()))
    bonusCON = srd.GetAbilityScoreBonus(int(self.txCon.GetValue()))
    bonusWIS = srd.GetAbilityScoreBonus(int(self.txWis.GetValue()))
    bonusDEX = srd.GetAbilityScoreBonus(int(self.txDex.GetValue()))
    bonusCHA = srd.GetAbilityScoreBonus(int(self.txCha.GetValue()))
    
    if (self.cbSkill_Acrobatics.IsChecked()):
      result = bonusDEX + proficiency
      if 'Acrobatics' not in self.proficencySkills:
        self.proficencySkills.append('Acrobatics')
    else:
      result = bonusDEX
      if ('Acrobatics') in self.proficencySkills:
        self.proficencySkills.remove('Acrobatics')
    if (result < 0):
      modifier = str(result)
    else:
      modifier = "+"+str(result)
    self.cbSkill_Acrobatics.SetLabel(("Acrobatics "+modifier))
    
    if (self.cbSkill_AnimalHandling.IsChecked()):
      result = bonusWIS + proficiency
      if 'AnimalHandling' not in self.proficencySkills:
        self.proficencySkills.append('AnimalHandling')
    else:
      result = bonusWIS
      if ('AnimalHandling') in self.proficencySkills:
        self.proficencySkills.remove('AnimalHandling')
    if (result < 0):
      modifier = str(result)
    else:
      modifier = "+"+str(result)
    self.cbSkill_AnimalHandling.SetLabel(("Animal Handling "+modifier))
    
    if (self.cbSkill_Arcana.IsChecked()):
      result = bonusINT + proficiency
      if 'Arcana' not in self.proficencySkills:
        self.proficencySkills.append('Arcana')
    else:
      result = bonusINT
      if ('Arcana') in self.proficencySkills:
        self.proficencySkills.remove('Arcana')
    if (result < 0):
      modifier = str(result)
    else:
      modifier = "+"+str(result)
    self.cbSkill_Arcana.SetLabel(("Arcana "+modifier))
    
    if (self.cbSkill_Athletics.IsChecked()):
      result = bonusSTR + proficiency
      if 'Athletics' not in self.proficencySkills:
        self.proficencySkills.append('Athletics')
    else:
      result = bonusSTR
      if ('Athletics') in self.proficencySkills:
        self.proficencySkills.remove('Athletics')
    if (result < 0):
      modifier = str(result)
    else:
      modifier = "+"+str(result)
    self.cbSkill_Athletics.SetLabel(("Athletics "+modifier))
    
    if (self.cbSkill_Deception.IsChecked()):
      result = bonusCHA + proficiency
      if 'Deception' not in self.proficencySkills:
        self.proficencySkills.append('Deception')
    else:
      result = bonusCHA
      if ('Deception') in self.proficencySkills:
        self.proficencySkills.remove('Deception')
    if (result < 0):
      modifier = str(result)
    else:
      modifier = "+"+str(result)
    self.cbSkill_Deception.SetLabel(("Deception "+modifier))
    
    if (self.cbSkill_History.IsChecked()):
      result = bonusINT + proficiency
      if 'History' not in self.proficencySkills:
        self.proficencySkills.append('History')
    else:
      result = bonusINT
      if ('History') in self.proficencySkills:
        self.proficencySkills.remove('History')
    if (result < 0):
      modifier = str(result)
    else:
      modifier = "+"+str(result)
    self.cbSkill_History.SetLabel(("History "+modifier))
    
    if (self.cbSkill_Insight.IsChecked()):
      result = bonusWIS + proficiency
      if 'Insight' not in self.proficencySkills:
        self.proficencySkills.append('Insight')
    else:
      result = bonusWIS
      if ('Insight') in self.proficencySkills:
        self.proficencySkills.remove('Insight')
    if (result < 0):
      modifier = str(result)
    else:
      modifier = "+"+str(result)
    self.cbSkill_Insight.SetLabel(("Insight "+modifier))
    
    if (self.cbSkill_Intimidation.IsChecked()):
      result = bonusCHA + proficiency
      if 'Intimidation' not in self.proficencySkills:
        self.proficencySkills.append('Intimidation')
    else:
      result = bonusCHA
      if ('Intimidation') in self.proficencySkills:
        self.proficencySkills.remove('Intimidation')
    if (result < 0):
      modifier = str(result)
    else:
      modifier = "+"+str(result)
    self.cbSkill_Intimidation.SetLabel(("Intimidation "+modifier))
    
    if (self.cbSkill_Investigation.IsChecked()):
      result = bonusINT + proficiency
      if 'Investigation' not in self.proficencySkills:
        self.proficencySkills.append('Investigation')
    else:
      result = bonusINT
      if ('Investigation') in self.proficencySkills:
        self.proficencySkills.remove('Investigation')
    if (result < 0):
      modifier = str(result)
    else:
      modifier = "+"+str(result)
    self.cbSkill_Investigation.SetLabel(("Investigation "+modifier))
    
    if (self.cbSkill_Medicine.IsChecked()):
      result = bonusWIS + proficiency
      if 'Medicine' not in self.proficencySkills:
        self.proficencySkills.append('Medicine')
    else:
      result = bonusWIS
      if ('Medicine') in self.proficencySkills:
        self.proficencySkills.remove('Medicine')
    if (result < 0):
      modifier = str(result)
    else:
      modifier = "+"+str(result)
    self.cbSkill_Medicine.SetLabel(("Medicine "+modifier))
    
    if (self.cbSkill_Nature.IsChecked()):
      result = bonusINT + proficiency
      if 'Nature' not in self.proficencySkills:
        self.proficencySkills.append('Nature')
    else:
      result = bonusINT
      if ('Nature') in self.proficencySkills:
        self.proficencySkills.remove('Nature')
    if (result < 0):
      modifier = str(result)
    else:
      modifier = "+"+str(result)
    self.cbSkill_Nature.SetLabel(("Nature "+modifier))
    
    if (self.cbSkill_Perception.IsChecked()):
      result = bonusWIS + proficiency
      if 'Perception' not in self.proficencySkills:
        self.proficencySkills.append('Perception')
    else:
      result = bonusWIS
      if ('Perception') in self.proficencySkills:
        self.proficencySkills.remove('Perception')
    if (result < 0):
      modifier = str(result)
    else:
      modifier = "+"+str(result)
    self.cbSkill_Perception.SetLabel(("Perception "+modifier))
    
    if (self.cbSkill_Performance.IsChecked()):
      result = bonusCHA + proficiency
      if 'Performance' not in self.proficencySkills:
        self.proficencySkills.append('Performance')
    else:
      result = bonusCHA
      if ('Performance') in self.proficencySkills:
        self.proficencySkills.remove('Performance')
    if (result < 0):
      modifier = str(result)
    else:
      modifier = "+"+str(result)
    self.cbSkill_Performance.SetLabel(("Performance "+modifier))
    
    if (self.cbSkill_Persuasion.IsChecked()):
      result = bonusCHA + proficiency
      if 'Persuasion' not in self.proficencySkills:
        self.proficencySkills.append('Persuasion')
    else:
      result = bonusCHA
      if ('Persuasion') in self.proficencySkills:
        self.proficencySkills.remove('Persuasion')
    if (result < 0):
      modifier = str(result)
    else:
      modifier = "+"+str(result)
    self.cbSkill_Persuasion.SetLabel(("Persuasion "+modifier))
    
    if (self.cbSkill_Religion.IsChecked()):
      result = bonusINT + proficiency
      if 'Religion' not in self.proficencySkills:
        self.proficencySkills.append('Religion')
    else:
      result = bonusINT
      if ('Religion') in self.proficencySkills:
        self.proficencySkills.remove('Religion')
    if (result < 0):
      modifier = str(result)
    else:
      modifier = "+"+str(result)
    self.cbSkill_Religion.SetLabel(("Religion "+modifier))
    
    if (self.cbSkill_SleightOfHand.IsChecked()):
      result = bonusDEX + proficiency
      if 'Sleight of Hand' not in self.proficencySkills:
        self.proficencySkills.append('Sleight of Hand')
    else:
      result = bonusDEX
      if ('Sleight of Hand') in self.proficencySkills:
        self.proficencySkills.remove('Sleight of Hand')
    if (result < 0):
      modifier = str(result)
    else:
      modifier = "+"+str(result)
    self.cbSkill_SleightOfHand.SetLabel(("Sleight of Hand "+modifier))
    
    if (self.cbSkill_Stealth.IsChecked()):
      result = bonusDEX + proficiency
      if 'Stealth' not in self.proficencySkills:
        self.proficencySkills.append('Stealth')
    else:
      result = bonusDEX
      if ('Stealth') in self.proficencySkills:
        self.proficencySkills.remove('Stealth')
    if (result < 0):
      modifier = str(result)
    else:
      modifier = "+"+str(result)
    self.cbSkill_Stealth.SetLabel(("Stealth "+modifier))
    
    if (self.cbSkill_Survival.IsChecked()):
      result = bonusWIS + proficiency
      if 'Survival' not in self.proficencySkills:
        self.proficencySkills.append('Survival')
    else:
      result = bonusWIS
      if ('Survival') in self.proficencySkills:
        self.proficencySkills.remove('Survival')
    if (result < 0):
      modifier = str(result)
    else:
      modifier = "+"+str(result)
    self.cbSkill_Survival.SetLabel(("Survival "+modifier))

    return

  def OnUpdateUI(self, event=None):
    event.Skip()
    self.bUpdateMonster.Enable(True)
    return

  def OnOK(self, evt):

    #save the monsters and NPC file if any monsters were updated.
    if (self.updateMasterMonsterList):
      if (self.recordType == '5E_NPC'): #save the NPC information
        try:
          datafile = open(os.path.join(gv.srd_directory,"5E","npc.xml"), "w")
        except IOError:
          logging.error("Could not open the npc.xml file")
          wx.MessageBox("Could not open the npc.xml file.  Check to see that it is available for writing.")
          return
        else:
          srd.WriteNPC_5E_XML(datafile)
      else:  #save the UserMonster information
        try:
          datafile = open(os.path.join(gv.srd_directory,"5E","UserMonsters.xml"), 'w')
        except:
          logging.error("Could not open the UserMonsters.xml file")
          wx.MessageBox("Could not open the UserMonsters.xml file.  Check to see that it is available for writing.")
          return
        app.frame.SetStatusText("Saving UserMonsters xml file")
        srd.WriteMonsters5E_XML(datafile,True)
        app.frame.SetStatusText("Finished writing UserMonsters xml file")
        if (gv.PymapperUser):  #allow for system development
          try:
            datafile = open(os.path.join(gv.srd_directory,"5E","CoreMonsters.xml"), 'w')
          except:
            logging.error("Could not open the CoreMonsters.xml file")
            wx.MessageBox("Could not open the CoreMonsters.xml file.  Check to see that it is available for writing.")
            return
          app.frame.SetStatusText("Saving CoreMonsters xml file")
          srd.WriteMonsters5E_XML(datafile,False)
          app.frame.SetStatusText("Finished writing CoreMonsters xml file")
          
    self.EndModal(True)
    return

  def OnCancel(self, evt):
    self.EndModal(False)
    return

  def OnHelp(self, evt):
    text = "To add a new monster, fill in the values in the fields and select the 'Add to Master List' button.  Be sure to click on the 'Update' button to save future changes.\n\nThe text highlighting is accomplished by placing a :~ anywhere in the line.  Text prior to the :~ will be highlighted.  Internally, this stores the name of the trait from the start of the line to the :~, and the explanatory text after the :~ characters.\n"
    text += "For spells, click the checkbox if the NPC/Monster is a spellcaster.  The spell list on the right side shows available spells.  Double-click on a spell to add it to the NPC/Monster spellbook.\n"
    text += "The left side shows the spells that the NPC/Monster can cast.  Double click on a spell to remove it from the list.  Double click on the spell level caption to change the number of spell slots available for each level.\n"

    help_dlg = HelpDialog(self, text)
    help_dlg.ShowModal()
    help_dlg.Destroy()
    return

  def OnListbox_lbMonsterList(self, evt=None):
    monsterName = self.lbMonsterList.GetStringSelection()
    if (self.recordType == '5E'):
      for monster in gv.Monsters5E:
        if (monster.name == monsterName) and (monster.version != 'DELETED'):
          break
    elif (self.recordType == '5E_NPC'):
      for monster in gv.NPC_5E:
        if (monster.name == monsterName) and (monster.version != 'DELETED'):
          break
    else:
      self.bbSelectCustomImage.Enable(False)
      
    if (monster.user_defined):
      self.stUserMonster.SetLabel(">--User Defined Monster--<")
    else:
      self.stUserMonster.SetLabel("")
      
    self.MonsterUniqueID = monster.uniqueID
    self.spells = copy.deepcopy(monster.spells)
    self.spellSlots = copy.deepcopy(monster.spellSlots)
    self.proficencySkills = copy.deepcopy(monster.proficiencySkills)
    self.AssignMonsterFields(monster)
    self.bUpdateMonster.Enable(True)
    self.bDeleteMonster.Enable(True)
    self.bCopyMonster.Enable(True)
    self.bAddMonster.Enable(True)
    self.bbSelectCustomImage.Enable(True)
    return
  
  def ApplyTextHighlighting(self, item):
    """item must be a wxTextCtrl"""
    if (type(item) != wx.TextCtrl):
      return
    
    text = item.GetValue()
    
    startPosition = 0
    highlightText = False
    item.SetInsertionPoint(0)
    
    for index,char in enumerate(text):
      if (char == '~'):  #highlight from previous start to current index
        item.SetStyle(startPosition, index, wx.TextAttr("BLACK", "YELLOW"))
        startPosition = index+1
      elif (char == '^'):  #highlight legendary actions 
        item.SetStyle(startPosition, index, wx.TextAttr("WHITE", "RED"))
        startPosition = index+1
      elif (char == '\n'):  #reset the startPosition to highlight on the next line
        startPosition = index+1
    return

  def AssignMonsterFields(self, item):
    '''
    item = Monster5E_Record()
    '''
    self.MonsterUniqueID = item.uniqueID
    self.txName.SetValue(item.name)
    if (self.recordType == '5E_NPC'):
      self.chRace.SetSelection(item.npc_race)
      self.chClass.SetSelection(item.npc_class)
    else:  #self.recordType == '5E'
      self.chType.SetSelection(item.monster_type)
      
    self.chSize.SetSelection(item.size)
    
    if (item.BasicMonster):
      self.cbBasicMonster.SetValue(True)
    else:
      self.cbBasicMonster.SetValue(False)
    
    if (self.recordType == '5E') and (item.filename == None):  #set image to generic monster image
      image = wx.Image(os.path.join(gv.artwork_directory,"monster_icon.png"), wx.BITMAP_TYPE_PNG)
    elif (self.recordType == '5E_NPC') and (item.filename == None): #set image to generic NPC image
      image = wx.Image(os.path.join(gv.artwork_directory,"npc_icon.png"), wx.BITMAP_TYPE_PNG)
    elif (item.filename):  #has a custom image
      image = wx.Image(os.path.join(gv.tokens_directory, item.filename), wx.BITMAP_TYPE_ANY)
    else:
      image = wx.Image((gv.artwork_directory+"monster_icon.png"), wx.BITMAP_TYPE_PNG)
      
    xsize = image.GetWidth()
    if (xsize != 100): #resize the image
      image = image.Scale(100, 100)
    bmp = wx.BitmapFromImage(image)
    self.bbSelectCustomImage.SetBitmapLabel(bmp)
    
    self.txHitDice.SetValue(item.HD)
    self.txSpeed.SetValue(item.speed)
    self.spACValue.SetValue(item.AC)
    self.txPassivePerception.SetValue(item.passive_perception)
    self.spHitPoints.SetValue(item.HP)
    self.txStr.SetValue(item.STR)
    self.txDex.SetValue(item.DEX)
    self.txInt.SetValue(item.INT)
    self.txWis.SetValue(item.WIS)
    self.txCha.SetValue(item.CHA)
    self.txCon.SetValue(item.CON)
    self.spProficiency.SetValue(item.proficiency)
    
    #add trait data and other information stored in Monster_Record to the page section
    if (self.recordType == '5E_NPC'):  #npc record
      #set the check boxes for proficiency
      if ('Acrobatics' in item.proficiencySkills):
        self.cbSkill_Acrobatics.SetValue(True)
      else:
        self.cbSkill_Acrobatics.SetValue(False)
        
      if ('AnimalHandling' in item.proficiencySkills):
        self.cbSkill_AnimalHandling.SetValue(True)
      else:
        self.cbSkill_AnimalHandling.SetValue(False)
        
      if ('Arcana' in item.proficiencySkills):
        self.cbSkill_Arcana.SetValue(True)
      else:
        self.cbSkill_Arcana.SetValue(False)
        
      if ('Athletics' in item.proficiencySkills):
        self.cbSkill_Athletics.SetValue(True)
      else:
        self.cbSkill_Athletics.SetValue(False)
        
      if ('Deception' in item.proficiencySkills):
        self.cbSkill_Deception.SetValue(True)
      else:
        self.cbSkill_Deception.SetValue(False)
        
      if ('History' in item.proficiencySkills):
        self.cbSkill_History.SetValue(True)
      else:
        self.cbSkill_History.SetValue(False)
        
      if ('Insight' in item.proficiencySkills):
        self.cbSkill_Insight.SetValue(True)
      else:
        self.cbSkill_Insight.SetValue(False)
        
      if ('Intimidation' in item.proficiencySkills):
        self.cbSkill_Intimidation.SetValue(True)
      else:
        self.cbSkill_Intimidation.SetValue(False)
        
      if ('Investigation' in item.proficiencySkills):
        self.cbSkill_Investigation.SetValue(True)
      else:
        self.cbSkill_Investigation.SetValue(False)
        
      if ('Medicine' in item.proficiencySkills):
        self.cbSkill_Medicine.SetValue(True)
      else:
        self.cbSkill_Medicine.SetValue(False)
        
      if ('Nature' in item.proficiencySkills):
        self.cbSkill_Nature.SetValue(True)
      else:
        self.cbSkill_Nature.SetValue(False)
        
      if ('Perception' in item.proficiencySkills):
        self.cbSkill_Perception.SetValue(True)
      else:
        self.cbSkill_Perception.SetValue(False)
        
      if ('Performance' in item.proficiencySkills):
        self.cbSkill_Performance.SetValue(True)
      else:
        self.cbSkill_Performance.SetValue(False)
        
      if ('Persuasion' in item.proficiencySkills):
        self.cbSkill_Persuasion.SetValue(True)
      else:
        self.cbSkill_Persuasion.SetValue(False)
        
      if ('Religion' in item.proficiencySkills):
        self.cbSkill_Religion.SetValue(True)
      else:
        self.cbSkill_Religion.SetValue(False)
        
      if ('Sleight of Hand' in item.proficiencySkills):
        self.cbSkill_SleightOfHand.SetValue(True)
      else:
        self.cbSkill_SleightOfHand.SetValue(False)
        
      if ('Stealth' in item.proficiencySkills):
        self.cbSkill_Stealth.SetValue(True)
      else:
        self.cbSkill_Stealth.SetValue(False)
        
      if ('Survival' in item.proficiencySkills):
        self.cbSkill_Survival.SetValue(True)
      else:
        self.cbSkill_Survival.SetValue(False)
      self.UpdateSkills()  #set the +/- bonuses based on proficiency
    else:  #monster record
      pass
        
    self.txActions.SetValue(item.actions)
    self.ApplyTextHighlighting(self.txActions)

    self.txLegendaryActions.SetValue(item.legendaryAction)
    self.ApplyTextHighlighting(self.txLegendaryActions)
    
    self.txChallengeRating.SetValue(item.CR)
    self.txAlignment.SetValue(item.alignment)
    self.txXPValue.SetValue(item.XP)

    #Prepare the attributes tab
    if (item.saves != ''):
      self.txSaves.SetValue(item.saves)

    if (item.resistances != ''):
      self.txResistances.SetValue(item.resistances)

    if (item.vulnerable != ''):
      self.txVulnerability.SetValue(item.vulnerable)

    if (item.immunities != ''):
      self.txImmunity.SetValue(item.immunities)

    if (item.conditionImmune != ''):
      self.txConditionImmunity.SetValue(item.conditionImmune)

    if (item.senses != ''):
      self.txSenses.SetValue(item.senses)

    if (item.languages != ''):
      self.txLanguages.SetValue(item.languages)
    
    if (item.userNotes != ''):
      self.txNotes.SetValue(item.userNotes)
    
    text = ''
    if (item.trait != ''):
      text += (item.trait + '\n')
    if (item.abilities != ''):
      text += (item.abilities + '\n')
    self.txTraits.SetValue(text)
    self.ApplyTextHighlighting(self.txTraits)
    
    text = ''
    if (item.treasure != ''):
      text += ('Treasure:~ ' + item.treasure + '\n')
    if (item.other_text != ''):
      text += (item.other_text + '\n')
    self.txOtherFeatures.SetValue(text)
    self.ApplyTextHighlighting(self.txOtherFeatures)
    
    if (item.bonds != ''):
      self.txBonds.SetValue(item.bonds)
      self.ApplyTextHighlighting(self.txBonds)
    
    if (item.flaws != ''):
      self.txFlaws.SetValue(item.flaws)
      self.ApplyTextHighlighting(self.txFlaws)
    
    if (item.ideals != ''):
      self.txIdeals.SetValue(item.ideals)
      self.ApplyTextHighlighting(self.txIdeals)
    
    self.ClearMonsterSpellBook()
    #update spell list based on the current monster.  Clear out the previous selection of spells from the tree
    if (item.spells == []):
      self.spSpellAttack.Enable(False)
      self.spSpellDC.Enable(False)
      self.stSpellAttack.Enable(False)
      self.stSpellDC.Enable(False)
      self.cbSpellcaster.SetValue(False)
      self.trAllSpellList.Enable(False)
      self.trCreatureSpellList.Enable(False)
      self.cbxSpellFilter.Enable(False)
    else:
      self.spSpellAttack.Enable(True)
      self.spSpellDC.Enable(True)
      self.stSpellAttack.Enable(True)
      self.stSpellDC.Enable(True)
      self.spSpellAttack.SetValue(item.spellAttackDC)
      self.spSpellDC.SetValue(item.spellSaveDC)
      self.cbSpellcaster.SetValue(True)
      self.trAllSpellList.Enable(True)
      self.trCreatureSpellList.Enable(True)
      self.trAllSpellList.Expand(self.SpellRootMain)
      self.trCreatureSpellList.Expand(self.SpellRootMonster)
      self.cbxSpellFilter.Enable(True)
      
      #set the slots in the spell descriptions
      name = "Cantrips ("+str(item.spellSlots['Slot0']) + " known)"
      self.trCreatureSpellList.SetItemText(self.CantripsRootMonster, name)
      name = "Level 1 Spells ("+str(item.spellSlots['Slot1']) + " slots)"
      self.trCreatureSpellList.SetItemText(self.Level1RootMonster, name)
      name = "Level 2 Spells ("+str(item.spellSlots['Slot2']) + " slots)"
      self.trCreatureSpellList.SetItemText(self.Level2RootMonster, name)
      name = "Level 3 Spells ("+str(item.spellSlots['Slot3']) + " slots)"
      self.trCreatureSpellList.SetItemText(self.Level3RootMonster, name)
      name = "Level 4 Spells ("+str(item.spellSlots['Slot4']) + " slots)"
      self.trCreatureSpellList.SetItemText(self.Level4RootMonster, name)
      name = "Level 5 Spells ("+str(item.spellSlots['Slot5']) + " slots)"
      self.trCreatureSpellList.SetItemText(self.Level5RootMonster, name)
      name = "Level 6 Spells ("+str(item.spellSlots['Slot6']) + " slots)"
      self.trCreatureSpellList.SetItemText(self.Level6RootMonster, name)
      name = "Level 7 Spells ("+str(item.spellSlots['Slot7']) + " slots)"
      self.trCreatureSpellList.SetItemText(self.Level7RootMonster, name)
      name = "Level 8 Spells ("+str(item.spellSlots['Slot8']) + " slots)"
      self.trCreatureSpellList.SetItemText(self.Level8RootMonster, name)
      name = "Level 9 Spells ("+str(item.spellSlots['Slot9']) + " slots)"
      self.trCreatureSpellList.SetItemText(self.Level9RootMonster, name)
      for level in item.spells:
        for spell in item.spells[level]:
          if (level == 'Level0'):
            self.trAllSpellList.AppendItem(self.CantripsRootMonster, spell)
          elif (level == 'Level1'):
            self.trAllSpellList.AppendItem(self.Level1RootMonster, spell)
          elif (level == 'Level2'):
            self.trAllSpellList.AppendItem(self.Level2RootMonster, spell)
          elif (level == 'Level3'):
            self.trAllSpellList.AppendItem(self.Level3RootMonster, spell)
          elif (level == 'Level4'):
            self.trAllSpellList.AppendItem(self.Level4RootMonster, spell)
          elif (level == 'Level5'):
            self.trAllSpellList.AppendItem(self.Level5RootMonster, spell)
          elif (level == 'Level6'):
            self.trAllSpellList.AppendItem(self.Level6RootMonster, spell)
          elif (level == 'Level7'):
            self.trAllSpellList.AppendItem(self.Level7RootMonster, spell)
          elif (level == 'Level8'):
            self.trAllSpellList.AppendItem(self.Level8RootMonster, spell)
          elif (level == 'Level9'):
            self.trAllSpellList.AppendItem(self.Level9RootMonster, spell)
      self.txSpellDescription.Clear()
    return
  
  def OnCopyMonster(self, event):
    """Copy the currently selected monster into a new record"""
    #check for duplicate name in database
    index = self.lbMonsterList.GetSelection()
    if (index == wx.NOT_FOUND):
      return
    
    monsterName = self.lbMonsterList.GetString(index)
    
    if (self.recordType == '5E'):
      for monster in gv.Monsters5E:
        if (monster.name == monsterName) and (monster.version == self.recordType):
          break
    elif (self.recordType == '5E_NPC'):
      for monster in gv.NPC_5E:
        if (monster.name == monsterName) and (monster.version == self.recordType):
          break
    else:
      logging.error("Found an unrecognized recordType")
      return  #wrong record type for some reason
    newMonster = copy.deepcopy(monster)
    newMonster.user_defined = True
    newMonster.name += " (Copy)"
    newMonster.uniqueID = gv.UserMonster5E_NextIndex
    gv.UserMonster5E_NextIndex += 1
    gv.Monsters5E.append(newMonster)
    self.updateMasterMonsterList = True
    self.BuildMonsterList()
    self.UpdateListBox()
    self.lbMonsterList.SetStringSelection(newMonster.name)
    self.OnListbox_lbMonsterList()
    return

  def OnAddMonster(self, evt):
    """Add a new monster to the database, using the values in the current fields"""
    #check for duplicate name in database
    monsterName = self.txName.GetValue()
    duplicateName = False
    if (self.recordType == '5E'):
      for monster in gv.Monsters5E:
        if (monster.name == monsterName) and (monster.version == self.recordType):
          duplicateName = True
          break
    elif (self.recordType == '5E_NPC'):
      for monster in gv.NPC_5E:
        if (monster.name == monsterName) and (monster.version == self.recordType):
          duplicateName = True
          break
    else:
      logging.error("Found an unrecognized recordType")
      return  #wrong record type for some reason
    
    if (duplicateName):
      #cannot have duplicate names, prompt for new name
      wx.MessageBox(message="Duplicate monster name found.  Please enter a unique monster name.",
                    caption="Whoa!", style=wx.ICON_EXCLAMATION)
      return
    
    NewMonster = srd.Monster5E_Record()
    NewMonster.version = self.recordType
    NewMonster.user_defined = True
    NewMonster.name = self.txName.GetValue()
    NewMonster.size = self.chSize.GetSelection()
    if (self.recordType == '5E_NPC'):
      NewMonster.npc_race = self.chRace.GetSelection()
      NewMonster.npc_class = self.chClass.GetSelection()
    else:  #self.recordType == '5E'
      NewMonster.monster_type = self.chType.GetSelection()

    NewMonster.uniqueID = gv.UserMonster5E_NextIndex
    gv.UserMonster5E_NextIndex += 1

    NewMonster.speed = self.txSpeed.GetValue()
    NewMonster.AC = self.spACValue.GetValue()
    NewMonster.HP = self.spHitPoints.GetValue()
    NewMonster.XP = self.txXPValue.GetValue()
    NewMonster.STR = self.txStr.GetValue()
    NewMonster.DEX = self.txDex.GetValue()
    NewMonster.INT = self.txInt.GetValue()
    NewMonster.WIS = self.txWis.GetValue()
    NewMonster.CON = self.txCon.GetValue()
    NewMonster.CHA = self.txCha.GetValue()
    NewMonster.CR = self.txChallengeRating.GetValue()
    NewMonster.alignment = self.txAlignment.GetValue()
    NewMonster.actions = self.txActions.GetValue()
    #update spell lists
    if (self.cbSpellcaster.IsChecked()):
      NewMonster.spells = copy.deepcopy(self.spells)
      NewMonster.spellSlots = copy.deepcopy(self.spellSlots)
    else:
      NewMonster.spells = []
      NewMonster.spellSlots = []
    NewMonster.trait = self.txTraits.GetValue()
    NewMonster.bonds = self.txBonds.GetValue()
    NewMonster.flaws = self.txFlaws.GetValue()
    NewMonster.ideals = self.txIdeals.GetValue()
    NewMonster.other_text = self.txOtherFeatures.GetValue()
    
    NewMonster.startHP = NewMonster.HP
    NewMonster.HD = self.txHitDice.GetValue()
    NewMonster.passive_perception = self.txPassivePerception.GetValue()
    NewMonster.show = True
    if (self.recordType == '5E'):
      gv.Monsters5E.append(NewMonster)
    elif (self.recordType == '5E_NPC'):
      gv.NPC_5E.append(NewMonster)
    self.BuildMonsterList()
    self.UpdateListBox()
    self.updateMasterMonsterList = True
    gv.SaveSRD_Monsters = True
    return

  def OnDeleteMonster(self, evt):
    index = self.lbMonsterList.GetSelection()
    if (index == wx.NOT_FOUND):
      return
    monsterName = self.lbMonsterList.GetString(index)
    if (self.recordType == '5E'):
      for monster in gv.Monsters5E:
        if (monster.name == monsterName) and (monster.version == self.recordType):
          #The monster record is kept so as to not interfere with the
          #unique ID of the monster, which is how pymapper looks up 
          #monster information when doing hover dialogs.
          monster.version = "DELETED"
          break
    elif (self.recordType == '5E_NPC'):
      for monster in gv.NPC_5E:
        if (monster.name == monsterName) and (monster.version == self.recordType):
          #The monster record is kept so as to not interfere with the
          #unique ID of the monster, which is how pymapper looks up 
          #monster information when doing hover dialogs.
          monster.version = "DELETED"  #queue for deletion next time the NPC file is saved
          break
    self.lbMonsterList.SetSelection(wx.NOT_FOUND)
    self.UpdateListBox()
    self.OnResetFields()
    self.updateMasterMonsterList = True
    self.bDeleteMonster.Enable(False)
    self.ClearSelection()
    return

  def ClearSelection(self, evt=None):
    self.lbMonsterList.SetSelection(wx.NOT_FOUND)
    self.OnResetFields()
    self.bCopyMonster.Enable(False)
    self.bUpdateMonster.Enable(False)
    self.bDeleteMonster.Enable(False)
    return


class BackgroundRegistrationDialog(PyMapperDialogs.BackgroundRegistrationDialogBase):
  def __init__(self, parent, page):
    old_cwd = os.getcwd()
    os.chdir(gv.root_directory)
    PyMapperDialogs.BackgroundRegistrationDialogBase.__init__(self, parent)
    os.chdir(old_cwd)
    self.bDeleteImage.Enable(False)
    if (page.background_filename):
      self.background_filename = page.background_filename
    else:
      self.background_filename = None
    if (page.background_filepath):
      self.background_filepath = page.background_filepath
    else:
      self.background_filepath = None
    if (page.background):
      self.backgroundImage = page.background
      self.backgroundBitmap = wx.BitmapFromImage(self.backgroundImage) #convert to bitmap
      self.BackgroundLoaded = True
    else:
      self.backgroundImage = None
      self.backgroundBitmap = None
      self.BackgroundLoaded = False
    self.scale_multiplier = 1.0  #used to zoom in/out
    self.register = False
    self.reg_x = 150
    self.reg_y = 150
    if (page.bg_displaymode == 'Center'):
      self.rbCenterBackground.SetValue(True)
      self.RegisterGrid()
      self.pnImageDisplay.Refresh()
    elif (page.bg_displaymode == 'Register'):
      self.rbRegisterBackground.SetValue(True)
    else:
      self.rbTileBackground.SetValue(True)
    self.DisplayImage()
    return

  def TileBackground(self, evt):
    self.register = False
    self.DisplayImage()
    return

  def CenterBackground(self, evt):
    self.register = False
    self.DisplayImage()
    return

  def RegisterBackground(self, evt=None):
    self.register = True
    self.RegisterGrid()
    return

  def ZoomIn(self, evt):
    size = self.backgroundImage.GetSize()
    self.scale_multiplier += 0.1
    width = int(size.width * self.scale_multiplier)
    height = int(size.height * self.scale_multiplier)
    rescale = self.backgroundImage.Scale(width, height)
    self.backgroundBitmap = wx.BitmapFromImage(rescale)
    self.DisplayImage()
    return

  def ZoomOut(self, evt):
    size = self.backgroundImage.GetSize()
    self.scale_multiplier -= 0.1
    if (self.scale_multiplier <= 0.1):
      self.scale_multiplier = 0.1
    width = int(size.width * self.scale_multiplier)
    height = int(size.height * self.scale_multiplier)
    rescale = self.backgroundImage.Scale(width, height)
    self.backgroundBitmap = wx.BitmapFromImage(rescale)
    self.DisplayImage()
    return

  def ImportImage(self, evt):
    dlg = wx.FileDialog(self, message="Choose a file", defaultDir=os.getcwd(), defaultFile="", wildcard=images_wildcard, style=wx.OPEN | wx.CHANGE_DIR)
    if (dlg.ShowModal() == wx.ID_OK):
      self.background_filename = dlg.GetFilename()
      self.background_filepath = dlg.GetDirectory()
      imagepath = os.path.join(self.background_filepath,self.background_filename)
      dlg.Destroy()
      self.backgroundImage = wx.Image(imagepath, wx.BITMAP_TYPE_ANY)
      if (not self.backgroundImage.IsOk()):
        '''Error Log'''
        errdlg = wx.MessageDialog(self, 'Error loading background file', 'Error', wx.OK | wx.ICON_ERROR)
        logging.error("BackgroundRegistrationDialog::OnImportBackground:  Could not open %s",self.background_filename)
        errdlg.ShowModal()
        errdlg.Destroy()
        self.BackgroundLoaded = False
        self.backgroundImage = None
      else:
        gv.DisplayBackground = True
        app.frame.menubar.Enable(PyMapperDialogs.mViewBackground, True)
        app.frame.toolbar.EnableTool(PyMapperDialogs.tShowBackground, enable=True)
        app.frame.toolbar.ToggleTool(PyMapperDialogs.tShowBackground, toggle=gv.DisplayBackground)
        self.BackgroundLoaded = True
        self.bDeleteImage.Enable(True)
        self.backgroundBitmap = wx.BitmapFromImage(self.backgroundImage) #convert to bitmap
        self.DisplayImage()

  def DisplayImage(self):
    dc = wx.ClientDC(self.pnImageDisplay)
    dc.SetPen(wx.WHITE_PEN)
    dc.SetBrush(wx.WHITE_BRUSH)
    dc.DrawRectangle(0,0,300,300)
    if (self.backgroundBitmap):
      dc.DrawBitmap(self.backgroundBitmap, 0,0)
    return

  def OnPaint(self, event):
    if (self.register == True):
      self.RegisterGrid()
    else:
      self.DisplayImage()
    event.Skip()
    return

  def DeleteImage(self, evt):
    self.background = None
    self.DisplayImage()
    self.bDeleteImage.Enable(False)
    return

  def RegisterGridMouseClick(self, event):
    if (self.register):
      self.reg_x = event.GetPosition().x
      self.reg_y = event.GetPosition().y
      self.RegisterGrid()
    return

  def RegisterGrid(self, evt=None):
    if (self.backgroundBitmap == None):
      return
    else:
      self.register = True
      dc = wx.ClientDC(self.pnImageDisplay)
      dc.DrawBitmap(self.backgroundBitmap, 0,0)
      dc.SetPen(wx.RED_PEN)
      dc.SetBrush(wx.TRANSPARENT_BRUSH)
      dc.DrawCircle(self.reg_x, self.reg_x, 5)
      dc.DrawRectangle(0,0,self.reg_x, self.reg_x)
    return

  def OnOK(self, evt):
    self.grid_width = (self.backgroundBitmap.GetWidth()/self.reg_x) + 1
    self.grid_height = (self.backgroundBitmap.GetHeight()/self.reg_y) + 1
    self.EndModal(True)
    return

  def OnCANCEL(self, evt):
    self.EndModal(False)
    return

  def OnHelp(self, evt):
    text = "There are three display options for backgrounds:\n  1. Tile the background image,\n  2. Center the background on the map grid,\n  3. Align the background image to the grid.\n\nTo match up the background image to the pymapper grid, click on the Align to Grid radio button.  The red line that appears represents a 1 inch square in pymapper.  Click the corner to match this box with the background image grid.\n\n Other image options are available under the Program|Options menu."
    dlg = HelpDialog(self, text)
    dlg.ShowModal()
    dlg.Destroy()
    return
  
class TrapInfoDialog(PyMapperDialogs.TrapsHoverBase):
  """This is the hover information dialog"""
  def __init__(self, parent, room, window_position):
    #room = RoomInfo()
    PyMapperDialogs.TrapsHoverBase.__init__(self, parent)
    position = window_position
    position.x -= 30
    position.y -= 30
    self.damageDice = ''
    self.Move(position)
    if (room.trap == None):
      return
    
    #assign the trap info to the dialog
    if (room.trap.TrapType == 'magic'):
      self.stTrapType.SetLabel("Magical Trap")
    elif (room.trap.TrapType == 'mechanical'):
      self.stTrapType.SetLabel("Mechanical Trap")
    else:
      self.stTrapType.SetLabel("Other trap type")
    self.cbxTrigger.SetValue(room.trap.trigger)
    self.cbxReset.SetValue(room.trap.reset)
    self.spSearchDC.SetValue(room.trap.searchDC)
    self.spDisableDC.SetValue(room.trap.disableDC)
    self.spAttackBonus.SetValue(room.trap.attackbonus)
    self.cbxAttackType.SetValue(room.trap.attacktype)
    self.spSaveDC.SetValue(room.trap.saveDC)
    self.cbxSaveAmount.SetValue(room.trap.saveamount)
    self.txDamageEffect.SetValue(room.trap.damage)
    if (room.trap.damageDice == ''):
      self.stDamageRoll.SetLabel("No damage dice defined")
      self.bRollDamage.Enable(False)
    else:
      self.stDamageRoll.SetLabel(room.trap.damageDice)  
      self.damageDice = room.trap.damageDice
    self.cbxOptional.SetValue(room.trap.optional)
    self.txOtherFeature.SetValue(room.trap.other)
    self.spChallengeRating.SetValue(room.trap.CR)
    self.txDescription.SetValue(room.trap.desc)
    self.SetTitle(room.trap.desc)
    self.cbxSaveType.SetValue(room.trap.savetype)
    self.cbxBypass.SetValue(room.trap.bypass)
    
    return
  
  def OnRollDamage(self, event):
    dmg = app.RollDice(self.damageDice)
    dmgString = str(dmg) + " HP"
    self.stDamageRoll.SetLabel(str(dmgString))
    return

class TrapsDialog(PyMapperDialogs.TrapsDialogBase):
  def __init__(self, parent, selected_trap=None):
    olddir = os.getcwd()
    os.chdir(gv.root_directory)  #this is necessary so that bitmap paths are read by the dialog code correctly    
    PyMapperDialogs.TrapsDialogBase.__init__(self, parent)
    os.chdir(olddir)
    self.MoveXY(100,100)
    
    self.cbxSaveType.AppendItems(gv.TrapSaveType)
    self.cbxTrigger.AppendItems(gv.TrapTrigger)
    self.cbxReset.AppendItems(gv.TrapReset)
    self.cbxBypass.AppendItems(gv.TrapBypass)
    self.cbxSaveAmount.AppendItems(gv.TrapSaveAmount)
    self.cbxAttackType.AppendItems(gv.TrapAttackType)

    self.bUpdateSelectedTrap.Enable(False)
    self.bDeleteTrap.Enable(False)
    self.bClearSelection.Enable(False)
    
    self.trapIndex = None

    self.TrapFilter = srd.TrapInfo()

    self.TrapFilter.desc = 'Enter Description'        #description of the trap, text string
    self.TrapFilter.CR = -1               #challenge rating
    self.TrapFilter.TrapType = 'other'    #magic or mechanical
    self.TrapFilter.trigger = 'None'     #'Location', 'Proximity', 'Sound', 'Visual', 'Touch', 'Timed', 'Spell'
    self.TrapFilter.reset = 'None'
    self.TrapFilter.bypass = 'Enter bypass method if any.'
    self.TrapFilter.attackbonus = -1      #attack bonus
    self.TrapFilter.attacktype = 'None'  #melee, ranged, pit, other, etc.
    self.TrapFilter.damage = 'Enter description of the attack or trap effect'
    self.TrapFilter.searchDC = -1
    self.TrapFilter.disableDC = -1
    self.TrapFilter.saveDC = -1
    self.TrapFilter.savetype = 'None'    #list of saves
    self.TrapFilter.saveamount = 'Undefined'
    self.TrapFilter.GPcost = -1
    self.TrapFilter.XPcost = -1
    self.TrapFilter.optional = 'None'   #other optional trap features
    self.TrapFilter.other = "Enter other user defined text here"

    index = 0
    if (gv.TrapList != []):
      for trap in gv.TrapList:
        trap.index = index
        index += 1
        self.lbTrapList.Append(trap.desc)
        
    self.selected_trap = selected_trap
    if (selected_trap):
      self.AssignTrapFields(selected_trap)
      for trap in gv.TrapList:
        if (trap.desc == selected_trap.desc):
          self.lbTrapList.SetSelection(trap.index)
          break
    else:
      self.AssignTrapFields(self.TrapFilter)
    return

  def AssignTrapFields(self, item):
    if (item.TrapType == 'magic'):
      self.rbMagicTrap.SetValue(True)
    elif (item.TrapType == 'mechanical'):
      self.rbMechanicalTrap.SetValue(True)
    else:
      self.rbOtherTrap.SetValue(True)
    self.cbxTrigger.SetValue(item.trigger)
    self.cbxReset.SetValue(item.reset)
    self.spSearchDC.SetValue(item.searchDC)
    self.spDisableDC.SetValue(item.disableDC)
    self.spAttackBonus.SetValue(item.attackbonus)
    self.cbxAttackType.SetValue(item.attacktype)
    self.spSaveDC.SetValue(item.saveDC)
    self.cbxSaveAmount.SetValue(item.saveamount)
    self.txDamageEffect.SetValue(item.damage)
    self.txDamageDice.SetValue(item.damageDice)
    self.cbxOptional.SetValue(item.optional)
    self.txOtherFeature.SetValue(item.other)
    self.spChallengeRating.SetValue(item.CR)
    self.txDescription.SetValue(item.desc)
    self.txGPCost.SetValue(item.GPcost)
    self.txXPCost.SetValue(item.XPcost)
    self.cbxSaveType.SetValue(item.savetype)
    self.cbxBypass.SetValue(item.bypass)
    return
  
  def CheckDuplicateName(self, evt=None, operation=None):
    """
    Return TRUE if a duplcate name was found in the traplist
    operation is either ADD or UPDATE
    """
    tempName = self.txDescription.GetValue()
    foundOnce = False
    for trap in gv.TrapList:
      if (tempName == trap.desc) and (operation == 'ADD'):
        wx.MessageBox("Duplicate trap name found.  Please enter a unique trap name.")
        return True
      elif (tempName == trap.desc) and (operation == 'UPDATE'):
        if (foundOnce):
          wx.MessageBox("Duplicate trap name found.  Please enter a unique trap name.")
          return True
        else:
          foundOnce = True
    return False
        

  def UpdateSelectedTrap(self, evt):
    if (self.CheckDuplicateName(operation='UPDATE')):
      return
    
    selection = self.lbTrapList.GetStringSelection()

    for trap in gv.TrapList:
      if (trap.desc == selection):
        break

    if (self.rbMagicTrap.GetValue()):
      trap.TrapType == 'magic'
    elif (self.rbMechanicalTrap.GetValue()):
      trap.TrapType == 'mechanical'
    else:
      trap.TrapType = 'other'
    trap.SRD_Trap = False
    trap.desc = self.txDescription.GetValue()
    trap.trigger = self.cbxTrigger.GetValue()
    trap.reset = self.cbxReset.GetValue()
    trap.searchDC = self.spSearchDC.GetValue()
    trap.disableDC = self.spDisableDC.GetValue()
    trap.attackbonus = self.spAttackBonus.GetValue()
    trap.attacktype = self.cbxAttackType.GetValue()
    trap.damage = self.txDamageEffect.GetValue()
    trap.damageDice = self.txDamageDice.GetValue()
    trap.saveDC = self.spSaveDC.GetValue()
    trap.savetype = self.cbxSaveType.GetValue()
    trap.saveamount = self.cbxSaveAmount.GetValue()
    trap.optional = self.cbxOptional.GetValue()
    trap.other = self.txOtherFeature.GetValue()
    trap.bypass = self.cbxBypass.GetValue()
    trap.GPcost = self.txGPCost.GetValue()
    trap.XPcost = self.txXPCost.GetValue()
    trap.CR = self.spChallengeRating.GetValue()
    gv.SaveSRD_Traps = True
    self.ApplyFilter()
    self.UpdateTrapListBox()
    return

  def ClearSelection(self, evt):
    self.lbTrapList.SetSelection(wx.NOT_FOUND)
    self.AssignTrapFields(self.TrapFilter)
    self.bUpdateSelectedTrap.Enable(False)
    self.bDeleteTrap.Enable(False)
    self.bClearSelection.Enable(False)
    self.trapIndex = None  #no trap selected, erase the ID lookup for hover
    return

  def OnListbox_lbTrapList(self, evt):
    selectedTrap = self.lbTrapList.GetStringSelection()
    for trap in gv.TrapList:
      if (trap.desc == selectedTrap):
        #self.trapIndex = trap.index  #assign the master ID of the trap for hover lookup
        break
    self.AssignTrapFields(trap)
    self.bDeleteTrap.Enable(True)
    self.bUpdateSelectedTrap.Enable(True)
    self.bClearSelection.Enable(True)
    return

  def OnOK(self, evt):
    gv.TrapDialogPosition = self.GetPosition()
    self.EndModal(True)
    selection = self.lbTrapList.GetStringSelection()
    for trap in gv.TrapList:
      if (trap.desc == selection):
        self.selected_trap = trap
        break
    return

  def OnCancel(self, evt):
    gv.TrapDialogPosition = self.GetPosition()
    self.EndModal(False)
    return

  def OnHelp(self, evt):
    text = "Change the values of any of the items on the left side list, and click on the Apply Filter button to filter the trap list.\n\nThe filter will consider all the fields at the same time, so use the Clear Filter button to reset the fields.\n\nEnter information in the fields and press the Add Trap button to create a new trap.\nThe filter for Danger Level is based on the Save DC:\n  Annoyance = DC <10\n  Setback = DC 10-11\n  Dangerous = DC 12-15\n  Deadly = DC 16-20\n  Evil = DC >20\n "
    dlg = HelpDialog(self, text)
    dlg.ShowModal()
    dlg.Destroy()
    return

  def AddTrap(self, evt):
    #check for duplicate name in the existing trap list
    if (self.CheckDuplicateName(operation='ADD')):
      return
    
    dlg = wx.MessageDialog(self, "Add new trap to user list?", "Add Trap", 
                           style=wx.YES_NO|wx.ICON_QUESTION)
    result = dlg.ShowModal()
    if (result == wx.ID_YES):
      #add to traplist
      trap = srd.TrapInfo()
      trap.icon = TrapIcon
      trap.index = len(gv.TrapList)
      trap.SRD_Trap = False
      trap.desc = self.txDescription.GetValue()
      trap.trigger = self.cbxTrigger.GetValue()
      trap.reset = self.cbxReset.GetValue()
      trap.searchDC = self.spSearchDC.GetValue()
      trap.disableDC = self.spDisableDC.GetValue()
      trap.attackbonus = self.spAttackBonus.GetValue()
      trap.attacktype = self.cbxAttackType.GetValue()
      trap.damage = self.txDamageEffect.GetValue()
      trap.damageDice = self.txDamageDice.GetValue()
      trap.saveDC = self.spSaveDC.GetValue()
      trap.savetype = self.cbxSaveType.GetValue()
      trap.saveamount = self.cbxSaveAmount.GetValue()
      trap.optional = self.cbxOptional.GetValue()
      trap.other = self.txOtherFeature.GetValue()
      trap.bypass = self.cbxBypass.GetValue()
      trap.GPcost = self.txGPCost.GetValue()
      trap.XPcost = self.txXPCost.GetValue()
      trap.CR = self.spChallengeRating.GetValue()
      gv.TrapList.append(trap)
      gv.SaveSRD_Traps = True
    self.ApplyFilter()
    self.UpdateTrapListBox()
    self.lbTrapList.SetSelection(wx.NOT_FOUND)
    dlg.Destroy()
    return

  def UpdateTrapListBox(self):
    """Should call ApplyFilter before this function"""
    self.lbTrapList.Clear()
    index = 0
    for trap in gv.TrapList:
      trap.displayIndex = None
      if (trap.show == True):
        self.lbTrapList.Append(trap.desc)
        trap.displayIndex = index
        index += 1
    return

  def DeleteTrap(self, evt):
    index = self.lbTrapList.GetStringSelection()
    if (index == wx.NOT_FOUND):
      return
    dlg = wx.MessageDialog(self,"Please confirm deletion, because this can't be undone.","Delete Trap?",style=wx.YES_NO|wx.ICON_EXCLAMATION)
    result = dlg.ShowModal()
    dlg.Destroy()
    if (result == wx.ID_YES):
      for trap in gv.TrapList:
        if (trap.desc == index):
          gv.TrapList.remove(trap)
          break
      gv.SaveSRD_Traps = True

    self.ApplyFilter()
    self.UpdateTrapListBox()
    return

  def ApplyFilter(self, event=None):
    """Apply the selected filters"""
    filterCR = self.cbFilterByCR.IsChecked()
    filterDanger = self.cbDangerFilter.IsChecked()
    filterType = self.cbTypeFilter.IsChecked()
    filterSource = self.cbSourceFilter.IsChecked()
    
    if ((not filterCR) and (not filterDanger) and (not filterType) and (not filterSource)):
      #all of the filters are turned off, show everything
      for trap in gv.TrapList:
        trap.show = True
    else:
      #otherwise, turn everything off, and then turn on those that match the filter criteria
      for trap in gv.TrapList:
        trap.show = False
    
    if (filterCR):
      self.lbCRFilter.Enable(True)
      filters = self.lbCRFilter.GetSelections()
      for trap in gv.TrapList:
        if (filters == ''):
          trap.show = False
        else:
          for i in filters: 
            if (trap.CR == i):
              trap.show = True
    else:
      self.lbCRFilter.Enable(False)
      
    if (filterDanger):
      self.lbDangerFilter.Enable(True)
      filters = self.lbDangerFilter.GetSelections()
      for trap in gv.TrapList:
        if (filters == ()):
          trap.show = False
        else:
          for i in filters:
            if (i == 0) and (trap.saveDC < 10):  #annoyance danger level, DC <10
              trap.show = True
            elif ((i==1) and ((trap.saveDC == 10) or (trap.saveDC == 11))):  #setback danger level, DC 10-11
              trap.show = True
            elif ((i==2) and ((trap.saveDC > 11) and (trap.saveDC <16))):  #dangerous, DC 12-15
              trap.show = True
            elif ((i==3) and ((trap.saveDC >16) and (trap.saveDC <21))):  #deadly, DC 16-20
              trap.show = True
            elif ((i==4) and (trap.saveDC >20)):  #evil, DC >20
              trap.show = True
    else:
      self.lbDangerFilter.Enable(False)
       
    if (filterSource):
      self.lbSourceFilter.Enable(True)
      filters = self.lbSourceFilter.GetSelections()
      for trap in gv.TrapList:
        if (filters == ''):
          trap.show = False
        else:
          for i in filters: 
            if (trap.CR == i):
              trap.show = True
    else:
      self.lbSourceFilter.Enable(False)
      
    if (filterType):
      self.lbFilterByType.Enable(True)
      filters = self.lbFilterByType.GetSelections()
      for trap in gv.TrapList:
        if (filters == ''):
          trap.show = False
        else:
          for i in filters: 
            if (trap.CR == i):
              trap.show = True
    else:
      self.lbFilterByType.Enable(False)

    self.UpdateTrapListBox()
    return

  def PrintStatBlock(self, trap):
    text = trap.desc + "; " + trap.trigger +" trigger; " + trap.reset + " reset; " + "Search DC" + str(trap.searchDC)
    if (trap.disableDC > 0):
      text += "; Disable DC" + str(trap.disableDC) + "; "
    text += trap.attacktype +" attack +" + str(trap.attackbonus) + " " + trap.damage +"\n"
    if (trap.saveDC != 'No Save'):
      text += "Save DC" + str(trap.saveDC) + " " + trap.savetype + " " + trap.saveamount + "\n"
    if (trap.optional != 'n/a'):
      text += "Optional: " + trap.optional + "\n"
    if (trap.other != 'n/a'):
      text += "Other: " + trap.other + "\n"
    if (trap.bypass != 'n/a'):
      text += "Bypass: " + trap.bypass + "\n"
    text += "Cost: " + str(trap.GPcost) + " gp"
    if (trap.XPcost > 0):
      text += "; " + str(trap.XPcost) + " xp"
    text += "; CR " + str(trap.CR) + "\n"
    text += "; Damage: " + trap.damageDice
    return text

#--------------------------------------------------------------------------------
class DungeonEncounterDesignDialog(PyMapperDialogs.DungeonEncountersDialogBase):
  def __init__(self, parent):
    temp_dir = os.getcwd()
    os.chdir(gv.root_directory)
    PyMapperDialogs.DungeonEncountersDialogBase.__init__(self, parent)
    os.chdir(temp_dir)

    self.UpdatePlacedItemsListbox()
    self.UpdateUnplacedItemsListbox()
    return

  def UpdatePlacedItemsListbox(self):
    self.lbDescriptionsOnMap.Clear()
    index = 0
    for item in gv.RoomList:
      if (item.placed):
        self.lbDescriptionsOnMap.Append(item.Description)
        item.Index = index
        index += 1
    return

  def UpdateUnplacedItemsListbox(self):
    self.lbUnplacedIcons.Clear()
    index = 0
    for item in gv.RoomList:
      if (not item.placed):
        self.lbUnplacedIcons.Append(item.Description)
        item.Index = index
        index += 1
    return

  def dclick_lbDescriptionsOnMap(self, evt):
    item = self.lbDescriptionsOnMap.GetSelection()
    room = RoomInfo()
    for room in gv.RoomList:
      if (room.Index == item) and (room.placed == True):
        app.RMapAddIconRoom(room=room)
        break
    return

  def OnPrintMasterList(self, evt):
    # Combine all of the xml files in the display list to a single printout.
    temp_room = RoomInfo()
    master = IconEditorFrame(self, "Master List", temp_room, (0,0))
    master2 = IconEditorFrame(self, "Master List", temp_room, (0,0))
    temp = IconEditorFrame(self, "temp_file", temp_room, (0,0))
    master.rtc.WriteText("Master List\n")
    for icon in gv.RoomList:
      temp.LoadFile(icon.xml_path,icon.xml_file)
      temp.rtc.SelectAll()
      temp.rtc.Copy()

      master.rtc.BeginBold()
      master.rtc.WriteText(icon.Description)
      master.rtc.EndBold()
      master.rtc.Paste()
      master.rtc.WriteText("\n*********************************\n")
      master.rtc.SetCaretPosition(master.rtc.GetLastPosition())

    master.Show()
    master.Raise()
    gv.rtc_open = True
    return

  def DeletePlacedDescription(self, evt):
    item = self.lbDescriptionsOnMap.GetSelection()
    room = RoomInfo()
    for room in gv.RoomList:
      if (room.Index == item) and (room.placed == True):
        room.placed = False
        break
    self.UpdatePlacedItemsListbox()
    self.UpdateUnplacedItemsListbox()
    return

  def AddMonster(self, evt):
    dlg = MonstersDialog(self, app.res)
    add_monster = dlg.ShowModal()
    if (add_monster):
      index = dlg.lbMonsterList.GetSelection()
      for monster in gv.MonsterList:
        if (monster.index == index):
          text = monster.stat_block
          icon = RoomInfo()
          icon.Icon = app.MonsterIcon
          icon.IconType = 'Monster'
          icon.Description = monster.name
          icon.placed = False
          gv.RoomList.append(icon)
          self.UpdateUnplacedItemsListbox()
          pos_rect = (self.GetRect().x, self.GetRect().y)
          rtc_frame = IconEditorFrame(self, icon.Description, icon, pos_rect, text)
          rtc_frame.Show()
          rtc_frame.Raise()
          gv.rtc_open = True
          break
    return

  def AddMonsterFromFile(self, evt):
    dlg = wx.FileDialog(self, message="Choose a file", defaultDir=gv.encounters_directory,
                        defaultFile="", wildcard=xml_wildcard, style=wx.OPEN | wx.CHANGE_DIR)
    if dlg.ShowModal() == wx.ID_OK:
      path = dlg.GetPath()
      file_name = dlg.GetFilename()
      folder_name = dlg.GetDirectory()
      if path:
        room = RoomInfo()
        room.placed = False
        room.Icon = app.MonsterIcon
        room.IconType = 'Monster'
        room.xml_file = file_name
        room.xml_path = folder_name
        room.Description = file_name.rstrip('.xml')
        gv.RoomList.append(room)
        self.UpdateUnplacedItemsListbox()
    dlg.Destroy()
    return

  def AddTrap(self, evt):
    dlg = TrapsDialog(self)
    result = dlg.ShowModal()
    if (result == True):
      text = dlg.PrintStatBlock(dlg.selected_trap)
      icon = RoomInfo()
      icon.Icon = app.TrapIcon
      icon.IconType = 'Trap'
      icon.Description = dlg.selected_trap.desc
      icon.placed = False
      (icon)
      self.UpdateUnplacedItemsListbox()
      pos_rect = (self.GetRect().x, self.GetRect().y)
      rtc_frame = IconEditorFrame(self, icon.Description, icon, pos_rect, text)
      rtc_frame.Show()
      rtc_frame.Raise()
      gv.rtc_open = True
    dlg.Destroy()
    return

  def AddTrapFromFile(self, evt):
    dlg = wx.FileDialog(self, message="Choose a file", defaultDir=gv.encounters_directory,
                        defaultFile="", wildcard=xml_wildcard, style=wx.OPEN | wx.CHANGE_DIR)
    if dlg.ShowModal() == wx.ID_OK:
      path = dlg.GetPath()
      file_name = dlg.GetFilename()
      folder_name = dlg.GetDirectory()
      if path:
        room = RoomInfo()
        room.placed = False
        room.Icon = app.TrapIcon
        room.IconType = 'Trap'
        room.xml_file = file_name
        room.xml_path = folder_name
        room.Description = file_name.rstrip('.xml')
        gv.RoomList.append(room)
        self.UpdateUnplacedItemsListbox()
    dlg.Destroy()
    return

  def AddTreasure(self, evt):
    dlg = TreasuresDialog(self)
    if (dlg.ShowModal() == wx.ID_OK):
      self.UpdateUnplacedItemsListbox()
    dlg.Destroy()

    return

  def AddTreasureFromFile(self, evt):
    dlg = wx.FileDialog(self, message="Choose a file", defaultDir=gv.encounters_directory,
                        defaultFile="", wildcard=xml_wildcard, style=wx.OPEN | wx.CHANGE_DIR)
    if dlg.ShowModal() == wx.ID_OK:
      path = dlg.GetPath()
      file_name = dlg.GetFilename()
      folder_name = dlg.GetDirectory()
      if path:
        room = RoomInfo()
        room.placed = False
        room.Icon = app.MonsterIcon
        room.IconType = 'Treasure'
        room.xml_file = file_name
        room.xml_path = folder_name
        room.Description = file_name.rstrip('.xml')
        gv.RoomList.append(room)
        self.UpdateUnplacedItemsListbox()
    dlg.Destroy()
    return

  def AddNPC(self, evt):
    dlg = NPC_GeneratorDialog(self)
    result = dlg.ShowModal()
    if (result == True):
      npc = dlg.CompiledNPC
      text = dlg.PrintStatBlock(npc)
      icon = RoomInfo()
      icon.Icon = app.NPC_Icon
      icon.IconType = 'NPC'
      icon.Description = dlg.CompiledNPC.Name
      icon.placed = False
      gv.RoomList.append(icon)
      self.UpdateUnplacedItemsListbox()
      pos_rect = (self.GetRect().x, self.GetRect().y)
      rtc_frame = IconEditorFrame(self, npc.Name, icon, pos_rect, text)
      rtc_frame.Show()
      rtc_frame.Raise()
      gv.rtc_open = True
    dlg.Destroy()
    return

  def AddNPCFromFile(self, evt):
    dlg = wx.FileDialog(self, message="Choose a file", defaultDir=gv.encounters_directory,
                        defaultFile="", wildcard=xml_wildcard, style=wx.OPEN | wx.CHANGE_DIR)
    if dlg.ShowModal() == wx.ID_OK:
      path = dlg.GetPath()
      file_name = dlg.GetFilename()
      folder_name = dlg.GetDirectory()
      if path:
        room = RoomInfo()
        room.placed = False
        room.Icon = app.NPC_Icon
        room.IconType = 'NPC'
        room.xml_file = file_name
        room.xml_path = folder_name
        room.Description = file_name.rstrip('.xml')
        gv.RoomList.append(room)
        self.UpdateUnplacedItemsListbox()
    dlg.Destroy()
    return

  def dclick_lbUnplacedIcons(self, evt):
    item = self.lbUnplacedIcons.GetSelection()
    room = RoomInfo()
    for room in gv.RoomList:
      if (room.Index == item) and (room.placed == False):
        app.RMapAddIconRoom(room=room)
        break
    return

  def PlaceDescription(self, evt):
    index = self.lbUnplacedIcons.GetSelection()
    for room in gv.RoomList:
      if (room.placed == False) and (room.Index == index):
        room.placed = True
        room.x = 1
        room.y = 1
        break
    self.UpdatePlacedItemsListbox()
    self.UpdateUnplacedItemsListbox()
    app.DrawMapWindow()
    return

  def DeleteUnplacedDescription(self, evt):
    # Prompt and delete description, but not the file on disk
    item = self.lbUnplacedIcons.GetSelection()
    room = RoomInfo()
    for room in gv.RoomList:
      if (room.Index == item) and (room.placed == True):
        gv.RoomList.remove(room)
        break
    self.UpdatePlacedItemsListbox()
    self.UpdateUnplacedItemsListbox()
    return

  def OnHelp(self, evt):
    # Show help.
    text = "The top listbox shows a listing of all the icon descriptions currently placed on the map.  Individual descriptions can be edited by double clicking on the line.\n\nA description can be deleted from the map here, although the xml file on disk will not be deleted.\n\nPrinting the master list will print out each description into a single document xml file that can then be printed or saved for distribution.\n\nAdditional monsters, traps, etc. can be added to the adventure module with the several buttons.\nThe descriptions will reside in the lower box until manually placed on the map.  Double clicking on an entry will bring up the editor for that item."
    dlg = HelpDialog(self, text)
    dlg.ShowModal()
    dlg.Destroy()

  def OnClose(self, evt):
    self.Show(False)
    return

########################################################################
class UserDetailsDialog(PyMapperDialogs.UserDetailsDialogBase):
  """Collect email information from users"""

  #----------------------------------------------------------------------
  def __init__(self, parent):
    """Constructor"""
    olddir = os.getcwd()
    os.chdir(gv.root_directory)  #this is necessary so that bitmap paths are read by the dialog code correctly
    PyMapperDialogs.UserDetailsDialogBase.__init__(self, parent)
    os.chdir(olddir)
    
    if (gv.UserEmail):
      self.txUserEmail.SetValue(gv.UserEmail)
    if (gv.UserName):
      self.txUserName.SetValue(gv.UserName)
    if (gv.UserReceiveUpdates):
      self.cbReceiveUpdates.SetValue(True)
    if (gv.UserSendCrashInfo):
      self.cbSendCrashReports.SetValue(True)
    return
    
  def OnRegisterProgram(self, event):
    emailAddress = self.txUserEmail.GetValue()
    if ("@" not in emailAddress):
      wx.MessageBox("Please enter a valid email address, or cancel registration")
      return
    self.EndModal(True)
    return
  
  def OnCancel(self, event):
    self.EndModal(False)
    return
  
  def OnPrivacyInformation(self, event):
    policy = "    Thank you for using the pymapper program.  I hope that you find it to be a helpful tool for maps and adventures.\n\n    When you register, pymapper will store your email address and preferences in a file named pymapper.ini, in the folder where you installed the program.  Please note that your name and email are stored in the pymapper.ini file.  If this file is corrupted or deleted, you will be prompted to resend your registration information to us.\n\n\
    We will not share your email with anyone else, for any reason.  If you have checked the box to receive periodic updates, you will receive occasional emails about new features and when program updates are available.\n\n\
    If you checked the box to allow pymapper to send crash reports, pymapper will send the file named pymapper_errors.log to bugs@pymapper.com when the program exits abnormally. You will be prompted when this happens, and will be given the opportunity to refuse to send the file.\n\n    System information such as operating system, \
python version, execution times, and other technical information will be sent.\n\n    You can opt out at any time by sending an email to pymapper@gmail.com.\
"
    dlg = HelpDialog(self, policy)
    dlg.ShowModal()
    return

class HelpDialog(PyMapperDialogs.HelpDialogBase):
  """text is the help text string to be displayed"""
  def __init__(self, parent, text):
    olddir = os.getcwd()
    os.chdir(gv.root_directory)  #this is necessary so that bitmap paths are read by the dialog code correctly
    PyMapperDialogs.HelpDialogBase.__init__(self, parent)
    os.chdir(olddir)
    self.txTextArea.ChangeValue(text)
    self.txTextArea.SetSelection(0,0)

  def OnClose(self, evt):
    self.EndModal(True)
    return


class RandomDungeonSettings:
  def __init__(self):
    #all values range from 0-100
    self.HallwayRoomRatio = 10     #0 = all halls           100 = all rooms
    self.HallwayWidth = 20         #0 = 5' narrow           100 = 20' wide
    self.HallwayLengths = 30       #0 = 20' short           100 = 120' long
    self.HallwayStraightness = 40  #0 = all straight        100 = turn every 10'
    self.RoomSize = 10             #0 = single tile         100 = six tiles
    self.TrapFrequency = 60        #0 = 0% chance per tile  100 = 100% chance per tile
    self.DoorFrequency = 70        #0 = No doors in rooms   100 = Door on every room
    self.DecorationFrequency = 80  #0 = No decorations      100 = Decorations on every tile
    self.DoorTypes = 90            #0 = All normal doors    100 = All exotic doors
    self.DungeonLinearity = 10     #0 = Linear dungeon      100 = Intersection in every hall
    self.DungeonSize = 20          #value equals number of tiles in dungeon

class MarkerRecord():
  """Markers may act as tiles, or may be used as the display bitmap in a RoomIcon"""
  def __init__(self, name=None):
    self.name = name
    self.outlineColor = None
    self.fillColor = None
    self.textColor = None
    self.size = None
    self.shape = None
    self.image = None  #wxImage source at 100x100 resolution.  Used for resizing 
    self.index = None  #integer value; position of the marker in the marker list
    self.key_index = None  #assigned from gv.key_index when loading markers from file.
    return

########################################################################
class SymbolRecord():
  """Image files are required to be either jpg or png files.  Grid 
  size is based on the image size, with a resolution of 100 pixels
  per side.  They act as a tile on the map"""
  #----------------------------------------------------------------------
  def __init__(self, filename=None, filepath=None):
    self.filepath = filepath  #plain path, without filename
    self.filename = filename  #filename, without path
    self.image = None  #wxImage in 100x100 resolution
    self.xsize = None  #size in squares;  imagesize/100
    self.ysize = None
    self.user_defined = False #False if this came from the artwork/symbols folder
    self.key_index = None
    return

class SymbolMarkerManagerDialog(PyMapperDialogs.SymbolManagerDialogCore):
  def __init__(self, parent, symbol_list, marker_list, limits=None):
    olddir = os.getcwd()
    os.chdir(gv.root_directory)  #this is necessary so that bitmap paths are read by the dialog code correctly
    
    PyMapperDialogs.SymbolManagerDialogCore.__init__(self, parent)
    os.chdir(olddir)
    self.symbol_list = copy.copy(symbol_list)
    self.removed_symbols = []
    self.marker_list = copy.copy(marker_list)
    self.blank_bitmap = wx.Bitmap(os.path.join(gv.artwork_directory,'blank.png'))
    self.UpdateSymbolListbox()
    self.UpdateMarkerListbox()
    self.symbol_bmp = None
    self.marker_bmp = None
    self.marker_base = wx.Image(100,100)
    self.marker_base.InitAlpha()
    for x in range(100):
      for y in range(100):
        self.marker_base.SetAlpha(x,y,0)
    if (limits == 'MarkersOnly'):
      #disable the symbol items
      self.lbSymbols.Enable(False)
      self.sbSymbolDisplay.Enable(False)
      self.bAddSymbol.Enable(False)
      self.bDeleteSymbol.Enable(False)
      self.bCancel.Show(True)
      self.bOK.SetLabel("OK")
    return

  def OnHelp(self, event):
    text = "Symbols are added to the map by a right-mouse click, and then selected from the list. They act as tiles after being placed on the map.\n\nMarkers can act as tiles, or as new bitmaps for map icons.\n\nAs tiles, they show up on the 'Markers' page on the tile window.  In this mode, drag the marker off the tile window just like a tile.\n\nTo use them as a custom bitmap on an map icon, create an icon as usual (right click on the map) and then select the new marker from the xml editor.\n\nIf they are used as an icon, then you will need to be in Icon mode to modify them.\n\nDouble click a marker entry to select and close the dialog."
    dlg = HelpDialog(self, text)
    dlg.ShowModal()
    return

  def OnAddSymbol(self, event):
    """Add a user defined symbol.  A list of symbols to load will be stored in symbols.ini in the pymapper root folder"""
    dlg = wx.FileDialog(self, message="Choose images for symbol files", defaultDir=gv.root_directory,
                        defaultFile="", wildcard=images_wildcard, style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR)
    if (dlg.ShowModal() == wx.ID_OK):
      ImageList = dlg.GetFilenames()
      path = dlg.GetDirectory()

      for image in ImageList:
        sym = SymbolRecord(image, path)
        sym.user_defined = True
        sym.image = wx.Image(os.path.join(path,image), wx.BITMAP_TYPE_ANY)
        sym.xsize = max(1,sym.image.GetWidth()/100)
        sym.ysize = max(1,sym.image.GetHeight()/100)
        sym.key_index = None  #set to None so that it will be added to the tilelist on closing the dialog
        self.symbol_list.append(sym)
      self.UpdateSymbolListbox()
    return

  def SaveSymbolsFile(self):
    #check to see if any custom symbols were added, and save the filename to symbols.ini
    try:
      symbol_file = open(os.path.join(gv.root_directory,'symbols.ini'), 'w')
    except IOError:
      logging.critical("Could not open symbols.ini file")
    else:
      symbol_file.write("# This file contains the file+path of symbols used by pymapper that are not located in the symbols folder.\n")
      symbol_file.write("# The symbols folder is a subfolder of the artwork folder.\n")
      symbol_file.write("# Symbol images must have a size in multiples of 100 pixels for each edge, and in jpeg or png format image.\n")
      symbol_file.write("SYMBOLS_FILE\n")
      symbol_file.write("VERSION 1.0\n")
      symbol = SymbolRecord()
      for symbol in self.symbol_list:
        if (symbol.user_defined):
          symbol_file.write("SYMBOL\n")
          symbol_file.write(symbol.filepath+"\n")
          symbol_file.write(symbol.filename+"\n")
      symbol_file.write("END_SYMBOLS_FILE")
      symbol_file.close()
    return

  def OnOK(self, event):
    self.SaveMarkerFile()
    self.SaveSymbolsFile()
    self.EndModal(True)
    return

  def OnAddMarker(self, event):
    dlg = wx.TextEntryDialog(self, "Enter Marker Name", "Name:")
    if (dlg.ShowModal() == wx.ID_OK):
      marker = MarkerRecord(name=dlg.GetValue())
      marker.fillColor = self.cpFillColor.GetColour()
      marker.outlineColor = self.cpOutlineColor.GetColour()
      marker.size = self.spMarkerSize.GetValue()
      marker.shape = self.rbMarkerShape.GetStringSelection()
      marker.index = len(self.marker_list)
      self.marker_list.append(marker)
      self.UpdateMarkerListbox()
      self.lbMarkers.SetSelection(len(self.marker_list)-1)
      bitmap = app.UpdateMarkerImage(marker)
      marker.image = bitmap.ConvertToImage()
      self.sbMarkerDisplay.SetBitmap(bitmap)
    return

  def OnDeleteMarker(self, event):
    selection = self.lbMarkers.GetSelection()
    if (selection == wx.NOT_FOUND):
      return
    else:
      self.marker_list.pop(selection)
      self.UpdateMarkerListbox()
      self.sbMarkerDisplay.SetBitmap(self.blank_bitmap)
    return

  def SaveMarkerFile(self):
    try:
      savefile = open(os.path.join(gv.root_directory,'markers.ini'), 'w')
    except IOError:
      logging.critical("SymbolMarkerManagerDialog::SaveMarkerFile Error:  Could not open markers.ini")
      return
    savefile.write("# Marker definition file version 1.0 for PyMapper.\n")
    savefile.write("# Do not edit this file while PyMapper is running.\n")
    savefile.write("# Tag definition:\n")
    savefile.write("# \n")
    savefile.write("# VERSION 1.0\n")
    savefile.write("# MARKER OutlineRED OutlineGREEN OutlineBLUE FillRED FillGREEN FillBLUE XYsize\n")
    savefile.write("# MARKER_SHAPE shape\n")
    savefile.write("# MARKER_INDEX index\n")  #unique index for the marker
    savefile.write("# MARKER_NAME\n")   #next line contains the name
    savefile.write("# MarkerName\n")
    savefile.write("# END_MARKER\n")
    savefile.write("# END_MARKER_FILE\n")
    savefile.write("# \n")
    savefile.write("# The outline and fill color values are from 0-255.   XYsize is an integer value of the size in squares of the marker.\n")
    savefile.write("# \n")
    savefile.write("VERSION 1.0\n")
    item = MarkerRecord()
    for item in self.marker_list:
      savefile.write("MARKER %d %d %d %d %d %d %d\n" % (item.outlineColor.Red(), item.outlineColor.Green(), item.outlineColor.Blue(), item.fillColor.Red(), item.fillColor.Green(), item.fillColor.Blue(), item.size))
      savefile.write("MARKER_NAME\n")
      savefile.write(item.name+"\n")
      savefile.write("MARKER_SHAPE "+item.shape+"\n")
      savefile.write("MARKER_INDEX "+str(item.index)+"\n")
      savefile.write("END_MARKER\n")
    savefile.write("END_MARKER_FILE")
    savefile.close()
    return

  def OnMarkerShape(self, event):
    selection = self.lbMarkers.GetSelection()
    if (selection == wx.NOT_FOUND):
      return
    else:
      self.marker_list[selection].shape = self.rbMarkerShape.GetStringSelection()
      self.UpdateMarkerImage(self.marker_list[selection])
    return

  def OnDeleteSymbol(self, event):
    selection = self.lbSymbols.GetSelection()
    if (selection == wx.NOT_FOUND):
      return
    else:
      item = self.symbol_list.pop(selection)
      self.removed_symbols.append(item)
      self.UpdateSymbolListbox()
      self.sbSymbolDisplay.SetBitmap(self.blank_bitmap)
    return

  def OnSymbolListbox(self, event):
    selection = self.lbSymbols.GetSelection()
    if (selection == wx.NOT_FOUND):
      return
    else:
      image = self.symbol_list[selection].image.Scale(100,100)
      self.symbol_bmp = wx.BitmapFromImage(image)
      self.sbSymbolDisplay.SetBitmap(self.symbol_bmp)
    return

  def UpdateMarkerImage(self, marker):
    bitmap = app.UpdateMarkerImage(marker)
    self.marker_bmp = bitmap
    self.sbMarkerDisplay.SetBitmap(self.marker_bmp)
    marker.image = self.marker_bmp.ConvertToImage()
    return

  def OnChangeTextColor(self, event):
    selection = self.lbMarkers.GetSelection()
    if (selection == wx.NOT_FOUND):
      return
    else:
      self.marker_list[selection].textColor = self.cpTextColor.GetColour()
      self.UpdateMarkerImage(self.marker_list[selection])
    return

  def OnChangeOutlineColor(self, event):
    selection = self.lbMarkers.GetSelection()
    if (selection == wx.NOT_FOUND):
      return
    else:
      self.marker_list[selection].outlineColor = self.cpOutlineColor.GetColour()
      self.UpdateMarkerImage(self.marker_list[selection])
    return

  def OnChangeFillColor(self, event):
    selection = self.lbMarkers.GetSelection()
    if (selection == wx.NOT_FOUND):
      return
    else:
      self.marker_list[selection].fillColor = self.cpFillColor.GetColour()
      self.UpdateMarkerImage(self.marker_list[selection])
    return


  def OnChangeMarkerSize(self, event):
    selection = self.lbMarkers.GetSelection()
    if (selection == wx.NOT_FOUND):
      return
    else:
      self.marker_list[selection].size = self.spMarkerSize.GetValue()
    return

  def OnMarkerListbox(self, event=None):
    selection = self.lbMarkers.GetSelection()
    if (selection == wx.NOT_FOUND):
      return
    else:
      self.cpFillColor.SetColour(self.marker_list[selection].fillColor)
      self.cpOutlineColor.SetColour(self.marker_list[selection].outlineColor)
      self.spMarkerSize.SetValue(self.marker_list[selection].size)
      self.rbMarkerShape.SetStringSelection(self.marker_list[selection].shape)
      self.UpdateMarkerImage(self.marker_list[selection])
      return

  def UpdateSymbolListbox(self):
    self.lbSymbols.Clear()
    for item in self.symbol_list:
      self.lbSymbols.Append(item.filename)
    return

  def UpdateMarkerListbox(self):
    self.lbMarkers.Clear()
    for item in self.marker_list:
      self.lbMarkers.Append(item.name)
    return

  def OnCancel(self, event):
    self.EndModal(False)
    return


class LayerDisplayDialog(PyMapperDialogs.LayerDisplayDialogBase):
  """Control over the active layer, the display of layers, and the opacity(transparency) of layers
     is controlled here.  The active layer is shown as being selected.  Single click a layer to 
     change active layers.  Double click a layer to toggle the display.
  """
  def __init__(self, parent):
    
    temp_dir = os.getcwd()
    os.chdir(gv.root_directory)
    PyMapperDialogs.LayerDisplayDialogBase.__init__(self, parent)
    os.chdir(temp_dir)
    
    self.lcActiveLayer.InsertColumn(0,'Name')
    self.lcActiveLayer.InsertColumn(1,'Display')
    
    self.lcLayerDisplay.InsertColumn(0,'Name')
    self.lcLayerDisplay.InsertColumn(1,'Display')
    self.lcLayerDisplay.InsertColumn(2,'Opacity')
    
    self.UpdateLists()
    return
  
  def ChangeLayerDisplay(self, event):
    
    return
  
  
  def ChangeLayerOpacity(self, event):
    gv.LayerList[gv.ActiveLayer].opacity = self.slOpacity.GetValue()/100
    self.UpdateLists()
    return
  
  def OnLayerDown(self, event):
    destPosition = gv.ActiveLayer + 1
    moveLayer = gv.LayerList.pop(gv.ActiveLayer)
    gv.LayerList.insert(destPosition, moveLayer)
    gv.ActiveLayer += 1
    self.lcLayerDisplay.SetItemState(gv.ActiveLayer, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
    self.UpdateLists()
    return
  
  def OnLayerUp(self, event):
    destPosition = gv.ActiveLayer - 1
    moveLayer = gv.LayerList.pop(gv.ActiveLayer)
    gv.LayerList.insert(destPosition, moveLayer)
    gv.ActiveLayer -= 1
    self.lcLayerDisplay.SetItemState(gv.ActiveLayer, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
    self.UpdateLists()
    return

  def OnHelpButton(self, event):
    text = "In the layer checklist area, the selected item changes the active layer.  The checkboxes control the individual display of layers.  Note that the active layer is always visible, and cannot be deselected(ie, hidden).  If you need to hide the base layer, create a dummy layer and activate it, then deselect the base layer to hide it.\n\nIn the tileset and map window checklists, select the checkboxes to change display on the respective window.\n\nSelecting a tileset in either window has no effect on the display, or in the program."
    dlg = HelpDialog(self, text)
    dlg.ShowModal()
    dlg.Destroy()
    return
  
  def CheckLayerSelection(self, event):
    item,flag = self.lcActiveLayer.HitTest(event.GetPosition())
    if (flag == wx.LIST_HITTEST_NOWHERE):
      self.lcActiveLayer.Select(gv.ActiveLayer)
    else:
      event.Skip()
    return


  def AddLayer(self, event):
    layerName = wx.GetTextFromUser("Enter new layer name", caption="Add Layer", default_value="Name")
    if (layerName == ""):  #user hit the cancel key
      return
    for layer in gv.LayerList:  #check for duplicate name
      if (layer.name == layerName):
        wx.MessageBox("Please enter a unique name for the layer", "Rolled a 1")
        return
    
    layerIndex = -1
    for layer in gv.LayerList:
      layerIndex = max(layer.index, layerIndex)  #find the highest index number in the list
    layerIndex += 1  #then increment by one to get the next index.
    newLayer = gv.LayerItem(index=layerIndex, name=layerName)
    gv.LayerList.insert(0,newLayer)
    self.UpdateLists()
    gv.PromptSave = True
    return

  def SelectActiveLayer(self, event):
    """Check to see if the base layer is selected; dim delete layer button if that is the case"""
    gv.ActiveLayer = event.m_itemIndex
    activeLayer = gv.LayerList[gv.ActiveLayer]
    for layer in gv.LayerList:
      if (layer == activeLayer):
        layer.activeLayer = True
      else:
        layer.activeLayer = False

    if (len(gv.LayerList) == 1):
      self.bDeleteLayer.Enable(False)
      self.bLayerDown.Enable(False)
      self.bLayerUp.Enable(False)
    elif (gv.ActiveLayer == 0):
      self.bLayerUp.Enable(False)
      self.bLayerDown.Enable(True)
    elif (gv.ActiveLayer == (len(gv.LayerList)-1)):
      self.bLayerDown.Enable(False)
      self.bLayerUp.Enable(True)
    else:
      self.bLayerDown.Enable(True)
      self.bLayerUp.Enable(True)
    self.slOpacity.SetValue(gv.LayerList[gv.ActiveLayer].opacity*100)
    app.frame.cxLayerSelector.SetSelection(gv.ActiveLayer)
    return

  def RenameLayer(self, event):
    if (gv.ActiveLayer == None):
      return
    
    layerName = wx.GetTextFromUser("Enter new layer name", caption="Rename Layer")
    if (layerName == ""):
      return
    else:
      gv.LayerList[gv.ActiveLayer].name = layerName
      self.UpdateLists()
    return

  def DeleteLayer(self, event):
    if (gv.ActiveLayer == None):
      gv.ActiveLayer = 0
      return
    
    checked = False
    check = None
    LayerDeleteIndex = gv.LayerList[gv.ActiveLayer].index
    if (gv.LayerList[gv.ActiveLayer].activeLayer):  #default layer 0 to active layer
      gv.LayerList[0].activeLayer = True
    delete_list = []
    for tile in app.maplist:
      if (tile.layer == LayerDeleteIndex):
        if (checked == False):
          dlg = wx.MessageDialog(self,message="Click YES to move tiles to top layer, NO to delete them, or CANCEL to abort",
                                 caption = "Tiles found on layer being deleted", 
                                 style = wx.CANCEL|wx.YES_NO|wx.ICON_QUESTION)
          check = dlg.ShowModal()
          checked = True
        if (check == wx.ID_CANCEL):
          return
        elif (check == wx.ID_YES):
          tile.layer = gv.LayerList[0].index
        elif (check == wx.ID_NO):
          delete_list.append(tile)
    if (check == wx.ID_NO):
      for tile in delete_list:
        app.DeleteMapTile(tile)
      app.DrawMapWindow()
    gv.LayerList.pop(gv.ActiveLayer)
    gv.ActiveLayer = 0
    self.UpdateLists()
    return

  def UpdateLists(self):
    self.lcActiveLayer.DeleteAllItems()
    self.lcLayerDisplay.DeleteAllItems()
    app.frame.cxLayerSelector.Clear()
    for layer in gv.LayerList:
      app.frame.cxLayerSelector.Append(layer.name)
      ActiveIndex = self.lcActiveLayer.InsertStringItem(sys.maxint, layer.name)
      if (layer.activeLayer):
        self.lcActiveLayer.SetStringItem(ActiveIndex, 1, 'Active')
      
      DisplayIndex = self.lcLayerDisplay.InsertStringItem(sys.maxint, layer.name)
      if (layer.display):
        self.lcLayerDisplay.SetStringItem(DisplayIndex, 1, 'On')
      else:
        self.lcLayerDisplay.SetStringItem(DisplayIndex, 1, 'Off')
      value = str(int(layer.opacity*100)) + "%"
      self.lcLayerDisplay.SetStringItem(DisplayIndex, 2, value)
    self.lcActiveLayer.SetItemState(gv.ActiveLayer, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
    if (len(gv.LayerList) == 1):
      self.bLayerDown.Enable(False)
      self.bLayerUp.Enable(False)
      self.bDeleteLayer.Enable(False)
    elif (len(gv.LayerList) == (gv.ActiveLayer+1)):
      self.bLayerDown.Enable(False)
      self.bLayerUp.Enable(True)
      self.bDeleteLayer.Enable(True)
    elif (gv.ActiveLayer == 0):
      self.bLayerDown.Enable(True)
      self.bLayerUp.Enable(False)
      self.bDeleteLayer.Enable(True)
    else:
      self.bLayerDown.Enable(True)
      self.bLayerUp.Enable(True)
      self.bDeleteLayer.Enable(True)
    app.frame.cxLayerSelector.SetSelection(gv.ActiveLayer)
    return

  def OnExit(self, event):
    self.Show(False)
    gv.LayerDialog.Destroy()
    gv.LayerDialog = None
    app.frame.toolbar.ToggleTool(PyMapperDialogs.tShowLayerFilter, toggle=False)
    return

class UndoItem:
  def __init__(self):
    self.Action = None        #this is the tag that specifies the action to take
    self.tile = Tile()  #
    self.side = None          #A or B tile side
    self.text = Annotation()  #id of the text
    self.icon = RoomInfo() 
    self.MapPosition = wx.Point2D() #this is the old map coordinate position
    self.rotate = None
    self.direction = None
    self.bitmap = None
    self.dx = None
    self.dy = None
    return


class TextOptionsDialogCore(PyMapperDialogs.TextOptionsDialogBase):
  def __init__(self, parent, globalchange, label):
    temp_dir = os.getcwd()
    os.chdir(gv.root_directory)
    PyMapperDialogs.TextOptionsDialogBase.__init__(self, parent)
    os.chdir(temp_dir)
    
    # Define variables for the controls, bind event handlers

    self.Bind(wx.EVT_PAINT, self.OnPaint)

    if (globalchange == True):
      self.cpkBackgroundColor.SetColour(gv.TextBackgroundColor)
      self.BackgroundColor = gv.TextBackgroundColor
      self.ForegroundColor = gv.TextForegroundColor
      self.TextFont = gv.TextFont
      self.FontData = gv.FontData
      self.TextBoxBitmap.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
      self.rbOpaque.SetValue(gv.OpaqueBackground)
      self.cpkBackgroundColor.Enable(self.rbOpaque.GetValue())
    else:
      self.cpkBackgroundColor.SetColour(label.bg)
      self.BackgroundColor = label.bg
      self.ForegroundColor = label.fg
      self.TextFont = label.font
      self.FontData = gv.FontData
      self.TextBoxBitmap.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
      self.rbOpaque.SetValue(label.opaque)
      self.cpkBackgroundColor.Enable(self.rbOpaque.GetValue())
    return

  def OnRB_TransparentBackground(self, evt):
    self.cpkBackgroundColor.Enable(self.rbOpaque.GetValue())
    self.Refresh()
    return

  def OnRB_Opaque(self, evt):
    self.cpkBackgroundColor.Enable(self.rbOpaque.GetValue())
    self.Refresh()
    return

  def OnChangeBackgroundColor(self, evt):
    self.BackgroundColor = self.cpkBackgroundColor.GetColour()
    self.Update()
    self.Refresh()
    return
  
  def OnChangeTextColor(self, event):
    self.ForegroundColor = self.cpkTextColor.GetColour()
    self.Update()
    self.Refresh()
    return

  def OnChangeFont(self, evt):
    self.FontData.SetInitialFont(self.TextFont)
    dlg = wx.FontDialog(self, self.FontData)
    if (dlg.ShowModal() == wx.ID_OK):
      self.FontData = dlg.GetFontData()
      self.TextFont = dlg.GetFontData().GetChosenFont()
      self.ForegroundColor = dlg.GetFontData().GetColour()
      self.cpkTextColor.SetColour(self.ForegroundColor)
      self.Refresh()
    return

  def UpdateTextField(self, dc):
    string = "PyMapper!"
    dc.SetFont(self.TextFont)
    (width, height) = dc.GetTextExtent(string)
    (bmpW, bmpH) = self.TextBoxBitmap.GetSizeTuple()
    xpos = ((bmpW - width)/2)-2
    ypos = ((bmpH - height)/2)-2

    extent = wx.Rect(xpos, ypos, width+4, height+4)
    bmp = wx.Bitmap(bmpW, bmpH)
    memdc = wx.MemoryDC()
    memdc.SelectObject(bmp)
    memdc.SetBackground(wx.WHITE_BRUSH)
    memdc.Clear()
    memdc.DrawRectangle(0, 0, bmpW, bmpH)
    if (self.rbOutlineOn.GetValue()):
      #draw an outline
      memdc.SetPen(wx.BLACK_PEN)
    else:
      memdc.SetPen(wx.WHITE_PEN)
    if (self.rbTransparentBackground.GetValue()):
      #transparent bg
      memdc.SetBrush(wx.TRANSPARENT_BRUSH)
    else:
      memdc.SetBrush(wx.Brush(self.BackgroundColor, wx.SOLID))
    memdc.DrawRectangle(extent.x, extent.y, extent.width, extent.height)
    memdc.SetTextForeground(self.ForegroundColor)
    memdc.SetFont(self.TextFont)
    memdc.DrawText(string, xpos+2, ypos+2)
    memdc.SelectObject(wx.NullBitmap)
    dc.DrawBitmap(bmp, 0, 0, True)

  def OnRB_OutlineOn(self, evt):
    self.Refresh()
    return

  def OnRB_OutlineOff(self, evt):
    self.Refresh()
    return

  def OnOK(self, evt):
    self.EndModal(True)
    return

  def OnCancel(self, evt):
    self.EndModal(False)
    return

  def OnPaint(self, event):
    dc = wx.PaintDC(self.TextBoxBitmap)
    self.UpdateTextField(dc)
    event.Skip()
    return

class XStatusBar(wx.StatusBar):
  def __init__(self, parent):
    wx.StatusBar.__init__(self, parent, -1)

    # This status bar has three fields
    self.SetFieldsCount(4)
    # Sets the three fields to be relative widths to each other.
    self.SetStatusWidths([-2, -1, -2, -1])
    self.sizeChanged = False
    self.Bind(wx.EVT_SIZE, self.OnSize)
    self.Bind(wx.EVT_IDLE, self.OnIdle)

    # Field 0 ... just text
    #self.SetStatusText("A Custom StatusBar...", 0)

    # This will fall into field 1 (the second field)
    bitmapPath = os.path.join(gv.artwork_directory, 'tileselectmode.bmp')
    bitmap = wx.Bitmap(bitmapPath, wx.BITMAP_TYPE_BMP)

    rect = self.GetFieldRect(1)
    position = wx.Point(rect.x, rect.y)
    bsize = wx.Size(156, 15)
    self.selectID = 1001
    self.SelectMode = wx.BitmapButton(self, self.selectID, bitmap, position, bsize)

    # set the initial position of the checkbox
    self.Reposition()

  def OnSize(self, evt):
    self.Reposition()  # for normal size events
    # Set a flag so the idle time handler will also do the repositioning.
    # It is done this way to get around a buglet where GetFieldRect is not
    # accurate during the EVT_SIZE resulting from a frame maximize.
    self.sizeChanged = True

  def OnIdle(self, evt):
    if self.sizeChanged:
      self.Reposition()

  # reposition the checkbox
  def Reposition(self):
    rect = self.GetFieldRect(1)
    self.sizeChanged = False

class TilesetPageManagerDialog(PyMapperDialogs.TilesetPageManagerDialogBase_UX):
  """
  setlist is a list of TileSet
  pagelist is a list of Page_Record
  """
  def __init__(self, parent, setlist, pagelist):
    olddir = os.getcwd()
    os.chdir(gv.root_directory)

    #wxNotebook is handled differently in Linux/OSX than in Windows
    PyMapperDialogs.TilesetPageManagerDialogBase_UX.__init__(self, parent)
    os.chdir(olddir)
    self.init = False

    self.setlist = copy.deepcopy(setlist)

    textlist = self.UpdateTilesetListbox(self.setlist)

    self.pagelistdata = []  #this is a copy of pagelist
    self.CurrentPageSelection = 0

    #initialize for non-windows OS
    for page in pagelist:
      self.cbxPages.Append(page.PageName)
      newpage = copy.deepcopy(page)
      self.pagelistdata.append(newpage)
    self.UpdateTilesetPagesListbox()
    self.cbxPages.SetSelection(0)
    return


  def AddAllTilesetsToPage(self, event):
    PageName = self.cbxPages.GetStringSelection()
    for page in self.pagelistdata:
      if (page.PageName == PageName):
        page.tilesets = []
        for tileset in self.setlist:
          page.tilesets.append(tileset.Name)
        self.UpdateTilesetPagesListbox()
    return

  def RemoveAllTilesetsFromPage(self, event):
    PageName = self.cbxPages.GetStringSelection()
    for page in self.pagelistdata:
      if (page.PageName == PageName):
        page.tilesets = []
      self.UpdateTilesetPagesListbox()
      break
    return

  def UpdateTilesetPagesListbox(self):
    self.lbTilesetPages.Clear()
    if (self.CurrentPageSelection < 0):
      return
    for tileset in self.pagelistdata[self.CurrentPageSelection].tilesets:
      self.lbTilesetPages.Append(tileset)
    return

  def OnOK(self, evt):
    """calling function should update data from 
    self.pagelistdata for the pages
    self.setlist for the tilesets
    """
    self.EndModal(True)
    return

  def OnCancel(self, evt):
    self.EndModal(False)
    return
  
  def ChangeTilepageUX(self, event):
    self.CurrentPageSelection = event.GetSelection()
    self.UpdateTilesetPagesListbox()
    return

  def OnAddPage(self, event):
    dlg = wx.TextEntryDialog(self, "Enter Page Name:")
    dlg.SetValue("New Page Name")
    add_page = dlg.ShowModal()
    if (add_page):
      pagename = dlg.GetValue()
      newpage = Page_Record(page=len(self.pagelistdata),name=pagename)
      notebook = wx.Window(parent=self.nbTilesetPagesAvailable, id=wx.ID_ANY, size=self.nbTilesetPagesAvailable.GetSize())
      self.nbTilesetPagesAvailable.AddPage(notebook, pagename)
      self.pagelistdata.append(newpage)
    dlg.Destroy()
    return

  def OnDeletePage(self, event):

    return

  def OnRenamePage(self, event):
    dlg = wx.TextEntryDialog(self, "Enter Page Name:")
    dlg.SetValue(self.nbTilesetPagesAvailable.GetPageText(self.CurrentPageSelection))
    add_page = dlg.ShowModal()
    if (add_page):
      self.nbTilesetPagesAvailable.SetPageText(self.CurrentPageSelection,dlg.GetValue())
      self.pagelistdata[self.CurrentPageSelection].PageName = dlg.GetValue()
    return

  def UpdateTilesetListbox(self, SetList):
    textlist = []
    self.UpdateAvailableTilesetListbox()
    for ts in SetList:
      if (ts.delete == False):  #not queued for deletion
        txt = str(ts.copies) + "    " + str(ts.SetID) + "  " + str(ts.Name)
      else:
        txt = "DEL " + str(ts.SetID) + "  " + str(ts.Name)
      textlist.append(txt)
    return textlist

  def UpdateAvailableTilesetListbox(self):
    self.lbAvailableTilesets.Clear()
    for item in self.setlist:
      if (not (item.delete)):
        self.lbAvailableTilesets.Append(item.Name)
    return

  def AddTilesetToPage(self, event):
    index = self.lbAvailableTilesets.GetSelection() #returns the index of the selection
    if (index == wx.NOT_FOUND):
      return
    tileset_to_add = self.setlist[index].Name
    PageName = self.cbxPages.GetStringSelection()
    page = Page_Record()
    for page in self.pagelistdata:
      duplicate_name = False
      if (page.PageName == PageName):  #found the page we want to add tileset to
        for name in page.tilesets:
          if (name == tileset_to_add):
            duplicate_name = True
        if (not duplicate_name):
          page.tilesets.append(tileset_to_add)
    self.UpdateTilesetPagesListbox()
    return

  def RemoveTilesetFromPage(self, event):
    index = self.lbTilesetPages.GetSelection() #returns the index of the selection
    if (index == wx.NOT_FOUND):
      return
    tileset_to_remove = self.pagelistdata[self.CurrentPageSelection].tilesets[index]
    PageName = self.cbxPages.GetStringSelection()
    page = TileSet()
    for page in self.pagelistdata:
      if (page.PageName == PageName):  #found the page we want to add tileset to
        for name in page.tilesets:
          if (name == tileset_to_remove):
            page.tilesets.remove(tileset_to_remove)
    self.UpdateTilesetPagesListbox()
    return
#  End class TilesetOptionsDialog_UX

class PrintResolutionDialog(PyMapperDialogs.PrintResolutionDialogBase):
  def __init__(self, parent):
    temp_dir = os.getcwd()
    os.chdir(gv.root_directory)
    PyMapperDialogs.PrintResolutionDialogBase.__init__(self, parent)
    os.chdir(temp_dir)
    self.spResolution.SetValue(gv.PrintResolution)
    return
  
  def OnOK(self, evt):
    self.EndModal(True)
    return

  def OnCancel(self, evt):
    self.EndModal(False)
    return

class ChangeMapSizeDialogCore(PyMapperDialogs.ChangeMapSizeDialogBase):
  def __init__(self, parent, rows, columns):
    temp_dir = os.getcwd()
    os.chdir(gv.root_directory)
    PyMapperDialogs.ChangeMapSizeDialogBase.__init__(self,parent)
    os.chdir(temp_dir)
    # Define variables for the controls, bind event handlers
    self.spColumns.SetValue(columns)
    self.spRows.SetValue(rows)
    self.ExpandDirection = 'Center'
    
    self.gridBitmap = wx.Bitmap(os.path.join(gv.artwork_directory,"grid.png"), wx.BITMAP_TYPE_ANY)
    self.upLeftBitmap = wx.Bitmap(os.path.join(gv.artwork_directory,"arrow_up_left.png"), wx.BITMAP_TYPE_ANY)
    self.upBitmap = wx.Bitmap(os.path.join(gv.artwork_directory,"arrow_up.png"), wx.BITMAP_TYPE_ANY)
    self.upRightBitmap = wx.Bitmap(os.path.join(gv.artwork_directory,"arrow_up_right.png"), wx.BITMAP_TYPE_ANY)
    self.downLeftBitmap = wx.Bitmap(os.path.join(gv.artwork_directory,"arrow_down_left.png"), wx.BITMAP_TYPE_ANY)
    self.downRightBitmap = wx.Bitmap(os.path.join(gv.artwork_directory,"arrow_down_right.png"), wx.BITMAP_TYPE_ANY)
    self.downBitmap = wx.Bitmap(os.path.join(gv.artwork_directory,"arrow_down.png"), wx.BITMAP_TYPE_ANY)
    self.leftBitmap = wx.Bitmap(os.path.join(gv.artwork_directory,"arrow_left.png"), wx.BITMAP_TYPE_ANY)
    self.rightBitmap = wx.Bitmap(os.path.join(gv.artwork_directory,"arrow_right.png"), wx.BITMAP_TYPE_ANY)
    self.blankBitmap = wx.Bitmap(os.path.join(gv.artwork_directory,"arrow_blank.png"), wx.BITMAP_TYPE_ANY)
    return
  
  def ClearBitmapArrows(self):
    self.bbTopLeft.SetBitmapLabel(self.blankBitmap)
    self.bbTopCenter.SetBitmapLabel(self.blankBitmap)
    self.bbTopRight.SetBitmapLabel(self.blankBitmap)
    self.bbBottomCenter.SetBitmapLabel(self.blankBitmap)
    self.bbBottomLeft.SetBitmapLabel(self.blankBitmap)
    self.bbBottomRight.SetBitmapLabel(self.blankBitmap)
    self.bbCenter.SetBitmapLabel(self.blankBitmap)
    self.bbCenterLeft.SetBitmapLabel(self.blankBitmap)
    self.bbCenterRight.SetBitmapLabel(self.blankBitmap)
    return
  
  def OnTopLeft(self, event):
    self.ExpandDirection = 'TopLeft'
    self.ClearBitmapArrows()
    self.bbTopLeft.SetBitmapLabel(self.gridBitmap)
    self.bbCenterLeft.SetBitmapLabel(self.downBitmap)
    self.bbTopCenter.SetBitmapLabel(self.rightBitmap)
    self.bbCenter.SetBitmapLabel(self.downRightBitmap)
    return
  
  def OnTopCenter(self, event):
    self.ExpandDirection = 'TopCenter'
    self.ClearBitmapArrows()
    self.bbTopCenter.SetBitmapLabel(self.gridBitmap)
    self.bbTopLeft.SetBitmapLabel(self.leftBitmap)
    self.bbTopRight.SetBitmapLabel(self.rightBitmap)
    self.bbCenterLeft.SetBitmapLabel(self.downLeftBitmap)
    self.bbCenter.SetBitmapLabel(self.downBitmap)
    self.bbCenterRight.SetBitmapLabel(self.downRightBitmap)
    return
  
  def OnTopRight(self, event):
    self.ExpandDirection = 'TopRight'
    self.ClearBitmapArrows()
    self.bbTopRight.SetBitmapLabel(self.gridBitmap)
    self.bbTopCenter.SetBitmapLabel(self.leftBitmap)
    self.bbCenter.SetBitmapLabel(self.downLeftBitmap)
    self.bbCenterRight.SetBitmapLabel(self.downBitmap)
    return
  
  def OnCenterLeft(self, event):
    self.ExpandDirection = 'CenterLeft'
    self.ClearBitmapArrows()
    self.bbTopLeft.SetBitmapLabel(self.upBitmap)
    self.bbTopCenter.SetBitmapLabel(self.upRightBitmap)
    self.bbCenter.SetBitmapLabel(self.rightBitmap)
    self.bbBottomCenter.SetBitmapLabel(self.downRightBitmap)
    self.bbBottomLeft.SetBitmapLabel(self.downBitmap)
    return
  
  def OnCenter(self, event):
    self.ExpandDirection = 'Center'
    self.ClearBitmapArrows()
    self.bbTopLeft.SetBitmapLabel(self.upLeftBitmap)
    self.bbTopCenter.SetBitmapLabel(self.upBitmap)
    self.bbTopRight.SetBitmapLabel(self.upRightBitmap)
    self.bbCenterLeft.SetBitmapLabel(self.leftBitmap)
    self.bbCenter.SetBitmapLabel(self.gridBitmap)
    self.bbCenterRight.SetBitmapLabel(self.rightBitmap)
    self.bbBottomLeft.SetBitmapLabel(self.downLeftBitmap)
    self.bbBottomCenter.SetBitmapLabel(self.downBitmap)
    self.bbBottomRight.SetBitmapLabel(self.downRightBitmap)
    return
  
  def OnCenterRight(self, event):
    self.ExpandDirection = 'CenterRight'
    self.ClearBitmapArrows()
    self.bbTopCenter.SetBitmapLabel(self.upLeftBitmap)
    self.bbTopRight.SetBitmapLabel(self.upBitmap)
    self.bbCenter.SetBitmapLabel(self.leftBitmap)
    self.bbCenterRight.SetBitmapLabel(self.gridBitmap)
    self.bbBottomCenter.SetBitmapLabel(self.downLeftBitmap)
    self.bbBottomRight.SetBitmapLabel(self.downBitmap)
    return
  
  def OnBottomLeft(self, event):
    self.ExpandDirection = 'BottomLeft'
    self.ClearBitmapArrows()
    self.bbCenterLeft.SetBitmapLabel(self.upBitmap)
    self.bbCenter.SetBitmapLabel(self.upRightBitmap)
    self.bbBottomLeft.SetBitmapLabel(self.gridBitmap)
    self.bbBottomCenter.SetBitmapLabel(self.rightBitmap)
    return
  
  def OnBottomCenter(self, event):
    self.ExpandDirection = 'BottomCenter'
    self.ClearBitmapArrows()
    self.bbCenterLeft.SetBitmapLabel(self.upLeftBitmap)
    self.bbCenter.SetBitmapLabel(self.upBitmap)
    self.bbCenterRight.SetBitmapLabel(self.upRightBitmap)
    self.bbBottomLeft.SetBitmapLabel(self.leftBitmap)
    self.bbBottomCenter.SetBitmapLabel(self.gridBitmap)
    self.bbBottomRight.SetBitmapLabel(self.rightBitmap)
    return
  
  def OnBottomRight(self, event):
    self.ExpandDirection = 'BottomRight'
    self.ClearBitmapArrows()
    self.bbCenter.SetBitmapLabel(self.upLeftBitmap)
    self.bbCenterRight.SetBitmapLabel(self.upBitmap)
    self.bbBottomCenter.SetBitmapLabel(self.leftBitmap)
    self.bbBottomRight.SetBitmapLabel(self.gridBitmap)
    return  

  def OnOK(self, evt):
    self.EndModal(True)
    return

  def OnCancel(self, evt):
    self.EndModal(False)
    return

class MapPrintout(wx.Printout):
  def __init__(self, PageList, NumPages, PageData):
    wx.Printout.__init__(self)
    self.pagelist = PageList
    self.NumPages = NumPages
    self.PageData = PageData
    return

  def HasPage(self, page):
    if (page <= self.NumPages):
      return True
    else:
      return False

  def GetPageInfo(self):
    return (1, self.NumPages, 1, self.NumPages)

  def OnPrintPage(self, page):
    dc = self.GetDC()
    dc.SetMapMode(wx.MM_TEXT)
    (wPPI, hPPI) = self.GetPPIPrinter()
    (width, height) = dc.GetSizeTuple()
    papersize = self.PageData.GetPaperId()
    if (papersize == wx.PAPER_LETTER):
      #Set size for 8x10 printed size
      x = int(0.25*wPPI)
      y = int(0.50*hPPI)
      wide = width - (2*x)
      high = height - (2*y)
      pagerect = wx.Rect(x, y, wide, high)
    elif (papersize == wx.PAPER_LEGAL):
      #Set size for 8x13 printed size
      x = int(0.25*wPPI)
      y = int(0.50*hPPI)
      wide = width - (2*x)
      high = height - (2*y)
      pagerect = wx.Rect(x, y, wide, high)
    elif (papersize == wx.PAPER_TABLOID):
      #Set size to 10x16 printed size
      x = int(0.50*wPPI)
      y = int(0.50*hPPI)
      wide = width - (2*x)
      high = height - (2*y)
      pagerect = wx.Rect(x, y, wide, high)
    elif (papersize == wx.PAPER_CSHEET):
      #Paper size 17x22, print size 16x21
      x = int(0.50*wPPI)
      y = int(0.50*hPPI)
      wide = width - (2*x)
      high = height - (2*y)
      pagerect = wx.Rect(x, y, wide, high)
    elif (papersize == wx.PAPER_DSHEET):
      #Paper size to 22x34; print size 21x33
      x = int(0.50*wPPI)
      y = int(0.50*hPPI)
      wide = width - (2*x)
      high = height - (2*y)
      pagerect = wx.Rect(x, y, wide, high)
    elif (papersize == wx.PAPER_ESHEET):
      #Paper size to 34x44; print size 33x43
      x = int(0.50*wPPI)
      y = int(0.50*hPPI)
      wide = width - (2*x)
      high = height - (2*y)
      pagerect = wx.Rect(x, y, wide, high)
    elif (papersize == wx.PAPER_NONE):
      #Set to specific dimensions, for now default back to 8x10 printed size
      x = int(0.25*wPPI)
      y = int(0.50*hPPI)
      wide = width - (2*x)
      high = height - (2*y)
      pagerect = wx.Rect(x, y, wide, high)
    else:
      #undefined paper size, or custom margins
      TLpoint = self.PageData.GetMarginTopLeft()
      BRpoint = self.PageData.GetMarginBottomRight()
      x = (TLpoint.x/25.4)*wPPI
      y = (TLpoint.y/25.4)*hPPI
      wide = width - (((TLpoint.x + BRpoint.x)/25.4)*wPPI)
      high = height - (((TLpoint.y + BRpoint.y)/25.4)*hPPI)

    pagerect = wx.Rect(x, y, wide, high)
    Wscale = float(pagerect.width)/self.pagelist[page-1].GetWidth()
    Hscale = float(pagerect.height)/self.pagelist[page-1].GetHeight()
    pagescale = min(Wscale, Hscale)
    dc.SetUserScale(pagescale, pagescale)
    x = int(x/pagescale)
    y = int(y/pagescale)
    dc.DrawBitmap(self.pagelist[page-1], x, y, True)
    dc.EndPage()
    return True

class ManifestPrint(wx.Printout):
  def __init__(self, PageSetupDialogData, TileList):
    wx.Printout.__init__(self)
    self.pagelist = []
    self.NumPages = 0
    self.PSDD = PageSetupDialogData
    self.tilelist = TileList
    return

  def HasPage(self, page):
    if (page <= self.NumPages):
      return True
    else:
      return False

  def OnPreparePrinting(self):
    #Prepare the pagelist
    #PSDD is PageSetupDialogData
    (wPPI, hPPI) = self.GetPPIPrinter()
    border = int(hPPI * 0.25)
    papersize = self.PSDD.GetPaperSize()  #in mm
    PrintData = self.PSDD.GetPrintData()
    MarginTopLeft = self.PSDD.GetMarginTopLeft()
    MarginBottomRight = self.PSDD.GetMarginBottomRight()
    width = wPPI * int(papersize.width/25.4)
    height = hPPI * int(papersize.height/25.4)
    bottom_margin = int(MarginBottomRight.y/25.4)
    pageBMP = wx.Bitmap(width, height)
    dc = wx.MemoryDC(pageBMP)
    dc.SetPen(wx.WHITE_PEN)
    dc.SetBrush(wx.WHITE_BRUSH)
    dc.DrawRectangle(0,0,width, height)
    offsetX = int(wPPI * (MarginTopLeft.x/25.4))
    offsetY = int(hPPI * (MarginTopLeft.y/25.4))
    dc.SetTextBackground(wx.WHITE)
    dc.SetTextForeground(wx.BLACK)
    pointsize = int(12 * 4.1667)
    font = wx.Font(pointsize, 74, 90, 92, underline=False, faceName="Times New Roman")
    dc.SetFont(font)
    StartNewPage = False

    tile = Tile()
    for tile in self.tilelist:
      if (tile.num_used > 0):
        if (tile.showingBside == False):
          img = tile.sideA.Copy()
          if (tile.tilenameA != None):
            dc.DrawText(str(tile.tilenameA), offsetX+800, offsetY+200)
        else:
          img = tile.sideB.Copy()
          if (tile.tilenameB != None):
            dc.DrawText(str(tile.tilenameB), offsetX+800, offsetY+200)
        if (img.GetHeight() > img.GetWidth()):
          img_size = wx.Size(img.GetHeight(), img.GetHeight())
          img_pt = wx.Point((img.GetHeight()/2)- (img.GetWidth()/2), 0)
        else:
          img_size = wx.Size(img.GetWidth(), img.GetWidth())
          img_pt = wx.Point(0, (img.GetWidth()/2)- (img.GetHeight()/2))

        img2 = img.Resize(img_size, img_pt, 255,255,255)
        img3 = img.Rescale(wPPI, hPPI)
        bmp = wx.BitmapFromImage(img3)

        dc.DrawBitmap(bmp, offsetX, offsetY, True)
        dc.DrawText("x"+str(tile.num_used), (offsetX+650), offsetY+200)
        dc.DrawText(str(tile.tilesetID)+"  "+str(tile.tilesetName), offsetX+800, offsetY+50)
        dc.DrawText(str(tile.actualXsize)+"x"+str(tile.actualYsize), offsetX+800, offsetY+350)
        offsetY += (hPPI + border) # the info section is 1" high, with 1/4" between
        if (offsetY > (height-(hPPI+bottom_margin))):
          if (StartNewPage == True):
            dc.EndPage()
            offsetX = int(wPPI * (MarginTopLeft.x/25.4))
            offsetY = int(hPPI * (MarginTopLeft.y/25.4))
            dc.SelectObject(wx.NullBitmap)
            self.pagelist.append(pageBMP)
            self.NumPages += 1
            pageBMP = wx.Bitmap(width, height)
            dc = wx.MemoryDC(pageBMP)
            dc.SetPen(wx.WHITE_PEN)
            dc.SetBrush(wx.WHITE_BRUSH)
            dc.DrawRectangle(0,0,width, height)
            dc.SetFont(font)
            StartNewPage = False
          else:
            offsetX = width/2
            offsetY = int(hPPI * (MarginTopLeft.y/25.4))
            StartNewPage = True  #next time through, start a new page
    dc.SelectObject(wx.NullBitmap)
    dc.EndPage()
    self.pagelist.append(pageBMP)
    self.NumPages += 1
    return

  def GetPageInfo(self):
    return (1, self.NumPages, 1, self.NumPages)

  def OnPrintPage(self, page):
    dc = self.GetDC()
    dc.SetMapMode(wx.MM_TEXT)
    dc.SetUserScale(1.0, 1.0)
    dc.DrawBitmap(self.pagelist[page-1], 0, 0, True)
    dc.EndPage()
    return True

class PrintPreviewDialog(PyMapperDialogs.PrintSetupDialogBase):
  def __init__(self, parent, print_data, map_bitmap, mapsize):
    olddir = os.getcwd()
    os.chdir(gv.root_directory)  #this is necessary so that bitmap paths are read by the dialog code correctly    
    PyMapperDialogs.PrintSetupDialogBase.__init__(self, parent)
    os.chdir(olddir)
    
    self.Center()
    self.Bind(wx.EVT_PAINT, self.OnPaint)

    self.rbFit1Page.Enable(False)
    self.rbFitCustomPage.Enable(False)
    self.stPagesHigh.Enable(False)
    self.stPagesWide.Enable(False)
    self.spPagesHigh.Enable(False)
    self.spPagesWide.Enable(False)

    self.mapsize = mapsize
    self.pagelist = [] #this will hold a list of wxBitmaps for printing.
    self.cxOutlineColor.SetColour(gv.OutlineTilesColor)
    self.cbOutlineTiles.SetValue(gv.OutlineTiles)

    #printing initialization
    self.printdata = print_data
    self.pagedata = wx.PageSetupDialogData(self.printdata)
    self.printout = wx.Printout("Map Data Preview")
    self.printdlog = wx.PrintDialogData(self.printdata)

    #size the Image to clip the empty space
    left = mapsize.x * gv.PrintResolution
    width = (mapsize.width) * gv.PrintResolution
    top = mapsize.y * gv.PrintResolution
    height = (mapsize.height) * gv.PrintResolution

    newrect = wx.Rect(left, top, width, height)

    temp = wx.ImageFromBitmap(map_bitmap)

    #crop the original image
    self.PrintImage = temp.GetSubImage(newrect)
    self.PrintImageRect = wx.Rect(0,0, self.PrintImage.GetWidth(), self.PrintImage.GetHeight())

    panelsize = self.pnPreviewPanel.GetSize()

    self.PixelSquare = min(panelsize.height/mapsize.height, panelsize.width/mapsize.width)

    w = self.PixelSquare * mapsize.width
    h = self.PixelSquare * mapsize.height

    image = self.PrintImage.Scale(w, h, wx.IMAGE_QUALITY_HIGH)

    #create the preview panel image
    self.map_bmp = wx.BitmapFromImage(image)
    self.PrintScale = 1


  def DrawPreviewPanel(self):
    dc = wx.ClientDC(self.pnPreviewPanel)
    dc.Clear()
    dc.DrawBitmap(self.map_bmp, 0, 0, True)
    self.SetPageSize(self.map_bmp, dc)
    return

  def OnPaint(self, evt):
    self.DrawPreviewPanel()
    evt.Skip()

  def SetPageSize(self, bitmap, dc):
    #mapsize = wx.Size() of the GridExtents of the map

    #get the page size
    TransparentBrush = wx.TRANSPARENT_BRUSH
    dc.SetBrush(TransparentBrush)
    PaperSize = self.pagedata.GetPaperSize()
    paper_id = self.pagedata.GetPaperId()
    TLpoint = self.pagedata.GetMarginTopLeft()
    BRpoint = self.pagedata.GetMarginBottomRight()
    #adjust for margins
    PageSize = wx.Size()
    PageSize.width = PaperSize.width - (TLpoint.x + BRpoint.x)
    PageSize.height = PaperSize.height - (TLpoint.y + BRpoint.y)
    #convert to inches
    PageSize.width /= 25.4
    PageSize.height /= 25.4
    panelsize = self.pnPreviewPanel.GetSize()
    if (self.rbPrint1Scale.GetValue()):
      #calculate to 1:1 scale printing
      #calculate how many squares per page
      self.pagelist = []
      NumSqPerPageW = PageSize.width
      NumSqPerPageH = PageSize.height
      #draw lines on the panel showing each sheet
      if ((self.mapsize.width) % (NumSqPerPageW)):
        NumPagesW = int(1+(float(self.mapsize.width)/float(NumSqPerPageW)))
      else:
        NumPagesW = int(float(self.mapsize.width)/float(NumSqPerPageW))
      if ((self.mapsize.height) % float(NumSqPerPageH)):
        NumPagesH = int(1+(float(self.mapsize.height)/float(NumSqPerPageH)))
      else:
        NumPagesH = int(float(self.mapsize.height)/float(NumSqPerPageH))

      self.NumPagesTotal = NumPagesH * NumPagesW
      x = 0
      y = 0
      page = 1
      for y in range(NumPagesH):
        for x in range(NumPagesW):
          xtop = x * self.PixelSquare * NumSqPerPageW
          ytop = y * self.PixelSquare * NumSqPerPageH
          xwidth = self.PixelSquare * NumSqPerPageW
          yheight = self.PixelSquare * NumSqPerPageH
          dc.DrawRectangle(xtop, ytop, xwidth, yheight)
          PixelPerSquareW = self.PrintImage.GetWidth()/self.mapsize.GetWidth()
          PixelPerSquareH = self.PrintImage.GetHeight()/self.mapsize.GetHeight()
          pagerect = wx.Rect(x * (NumSqPerPageW*PixelPerSquareW),
                             y * (NumSqPerPageH*PixelPerSquareH),
                             (NumSqPerPageW*PixelPerSquareW),
                             (NumSqPerPageH*PixelPerSquareH))
          if (self.PrintImageRect.ContainsRect(pagerect)):
            pageimage = self.PrintImage.GetSubImage(pagerect)
          else:
            cliprect = wx.Rect()
            cliprect.x = pagerect.GetX()
            cliprect.y = pagerect.GetY()
            cliprect.width = self.PrintImageRect.width - pagerect.x
            cliprect.height = self.PrintImageRect.height - pagerect.y
            clipimage = self.PrintImage.GetSubImage(cliprect)
            pageimage = clipimage.Resize(wx.Size(pagerect.GetWidth(), pagerect.GetHeight()),
                                         wx.Point(0,0), 255, 255, 255)
          pagebitmap = wx.BitmapFromImage(pageimage)
          self.pagelist.append(pagebitmap)
          page += 1
      return
    elif (self.rbCustomScale.GetValue()):
      if (self.rbFit1Page.GetValue()):
        # Fit all on a single page
        printDC = wx.PrinterDC(self.printdata)
        pagesize = printDC.GetSize()
        self.pagelist = []
        #draw lines on the panel showing each sheet
        self.NumPagesTotal = 1
        panelsize = self.pnPreviewPanel.GetSize()
        dc.DrawRectangle(0, 0, panelsize.width, panelsize.height)

        size = printDC.GetSize()
        pil_size = self.PrintImage.GetSize()
        deltaW = size.width - pil_size.width
        deltaH = size.height - pil_size.height
        if ((deltaW > 0) and (deltaH < 0)):
          #width is OK, resize height
          aspect = float(size.height)/float(pil_size.height)
          newH = int(aspect*pil_size.height)
          newW = int(aspect*pil_size.width)
        elif ((deltaW < 0) and (deltaH > 0)):
          #height is OK, resize width
          aspect = float(size.width)/float(pil_size.width)
          newH = int(aspect*pil_size.height)
          newW = int(aspect*pil_size.width)
        elif ((deltaW < 0) and (deltaH < 0)):
          # resize height and width
          aspectW = float(size.width)/float(pil_size.width)
          aspectH = float(size.height)/float(pil_size.height)
          if (aspectW < aspectH):
            #resize to width
            newH = int(aspectW*pil_size.height)
            newW = int(aspectW*pil_size.width)
          else:
            newH = int(aspectH*pil_size.height)
            newW = int(aspectH*pil_size.width)
        elif((deltaW > 0) and (deltaH > 0)):
          #image smaller than panel, need to enlarge
          aspectW = float(size.width)/float(pil_size.width)
          aspectH = float(size.height)/float(pil_size.height)
          if (aspectW < aspectH):
            #resize to width
            newH = int(aspectW*pil_size.height)
            newW = int(aspectW*pil_size.width)
          else:
            newH = int(aspectH*pil_size.height)
            newW = int(aspectH*pil_size.width)

        pageimage = self.PrintImage.Scale(newW, newH, wx.IMAGE_QUALITY_NORMAL)
        pagebitmap = wx.BitmapFromImage(pageimage)
        self.pagelist.append(pagebitmap)
        return
      elif (self.rbFitCustomPage.GetValue()):
        # Fit on the number of pages specified
        #draw lines on the panel showing each sheet
        self.pagelist = []
        NumPagesW = self.spPagesWide.GetValue()
        NumPagesH = self.spPagesHigh.GetValue()
        self.NumPagesTotal = NumPagesH * NumPagesW

        x = 0
        y = 0
        page = 1
        for y in range(NumPagesH):
          for x in range(NumPagesW):
            xtop = x * (self.map_bmp.GetWidth()/NumPagesW)
            ytop = y * (self.map_bmp.GetHeight()/NumPagesH)
            xwidth = self.map_bmp.GetWidth()/NumPagesW
            yheight = self.map_bmp.GetHeight()/NumPagesH
            dc.DrawRectangle(xtop, ytop, xwidth, yheight)
            pagerect = wx.Rect(xtop * gv.PrintResolution,
                               ytop * gv.PrintResolution,
                               xwidth * gv.PrintResolution,
                               yheight * gv.PrintResolution)
            pageimage = self.PrintImage.GetSubImage(pagerect)
            pagebitmap = wx.BitmapFromImage(pageimage)
            self.pagelist.append(pagebitmap)
            page += 1
        return
      return

  def OnPrint1Scale(self, evt):
    self.rbFit1Page.Enable(False)
    self.rbFitCustomPage.Enable(False)
    self.stPagesHigh.Enable(False)
    self.stPagesWide.Enable(False)
    self.spPagesHigh.Enable(False)
    self.spPagesWide.Enable(False)
    self.DrawPreviewPanel()

  def OnCustomScale(self, evt):
    self.rbFit1Page.Enable(True)
    self.rbFit1Page.SetValue(True)
    self.rbFitCustomPage.Enable(False)
    if (self.rbFit1Page.GetValue()):
      self.stPagesHigh.Enable(False)
      self.stPagesWide.Enable(False)
      self.spPagesHigh.Enable(False)
      self.spPagesWide.Enable(False)
    else:
      self.stPagesHigh.Enable(True)
      self.stPagesWide.Enable(True)
      self.spPagesHigh.Enable(True)
      self.spPagesWide.Enable(True)
    self.DrawPreviewPanel()
    return

  def OnFit1Page(self, evt):
    self.stPagesHigh.Enable(False)
    self.stPagesWide.Enable(False)
    self.spPagesHigh.Enable(False)
    self.spPagesWide.Enable(False)
    self.DrawPreviewPanel()

  def OnFitCustomPage(self, evt):
    self.stPagesHigh.Enable(True)
    self.stPagesWide.Enable(True)
    self.spPagesHigh.Enable(True)
    self.spPagesWide.Enable(True)
    self.DrawPreviewPanel()

  def spNumPagesHigh(self, evt):
    self.DrawPreviewPanel()

  def spNumPagesWide(self, evt):
    self.DrawPreviewPanel()

  def OnOK(self, evt):
    self.EndModal(True)
    return

  def OnCancel(self, evt):
    self.EndModal(False)
    return

  def OnPageSetup(self, evt):
    self.pagedata.CalculatePaperSizeFromId()
    dlg = wx.PageSetupDialog(self, self.pagedata)
    result = dlg.ShowModal()
    if (result == wx.ID_OK):
      #copy info
      self.printdata = wx.PrintData(dlg.GetPageSetupData().GetPrintData())
      self.pagedata = dlg.GetPageSetupData()
    dlg.Destroy()
    self.DrawPreviewPanel()
    return

  def OnChangePrinter(self, evt):
    dlg = wx.PrintDialog(self, wx.PrintDialogData(self.printdata))
    if (dlg.ShowModal() == wx.ID_OK):
      self.printdata = wx.PrintData(dlg.GetPrintDialogData().GetPrintData())
    dlg.Destroy()
    return

class TilesetsFilterDialog(wx.MultiChoiceDialog):
  def __init__(self, parent, message, caption, choices, setlist):
    choices = self.UpdateList(setlist)
    pre = wx.PreDialog()
    self.PostCreate(pre)
    self.Center()

    self.Bind(wx.EVT_LISTBOX, self.OnListBox)

  def UpdateList(self, setlist):
    list_text = []
    for i in setlist:
      item = str(i.SetID) + "   " + str(i.Name)
      list_text.append(item)
    return list_text

  def OnListBox(self, event):
    return

class HoverTileDialogCore(PyMapperDialogs.HoverDialogBase):
  def __init__(self, parent, tile, bitmap, dest_point):
    temp_dir = os.getcwd()
    os.chdir(gv.root_directory)
    PyMapperDialogs.HoverDialogBase.__init__(self, parent)
    os.chdir(temp_dir)
    self.tile = tile
    if (tile == None):
      self.bitmap = bitmap
    else:
      if (tile.showingBside):
        self.bitmap = self.ResizeHoverImage(tile.sideA)
      elif (tile.sideB != None):
        self.bitmap = self.ResizeHoverImage(tile.sideB)
      else:
        self.bitmap = wx.Bitmap(os.path.join(gv.artwork_directory,'NoImage.bmp'), wx.BITMAP_TYPE_BMP)

    bitmap_size = wx.Size(self.bitmap.GetWidth(), self.bitmap.GetHeight())
    self.SetDimensions(dest_point.x, dest_point.y, bitmap_size.width, bitmap_size.height, wx.SIZE_FORCE)
    
    self.HoverPanel.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
    self.Bind(wx.EVT_PAINT, self.OnPaint)

    self.delta = 0 #movement delta
    self.start_pt = None
    return

  def OnMotion(self, event):
    position = event.GetPosition()
    if (self.start_pt == None):
      self.start_pt = position
    else:
      delta = (abs(self.start_pt.x - position.x) + abs(self.start_pt.y - position.y))
      if (delta > 3):
        self.Show(False)
    return

  def ResizeHoverImage(self, image):
    #reduce the tile to 200,200 max
    width = image.GetWidth()
    height = image.GetHeight()
    rect = wx.Rect(0, 0, width, height)
    maxsize = wx.Rect(0, 0, 200, 200)
    resize = True
    while (resize == True):
      if (maxsize.ContainsRect(rect)):
        resize = False
      else:
        width = int(width*0.9)
        height = int(height*0.9)
        rect = wx.Rect(0,0,width, height)

    image2 = image.Scale(width, height, wx.IMAGE_QUALITY_NORMAL)
    bitmap = wx.BitmapFromImage(image2)
    if (self.tile):
      txt = str(self.tile.copies-self.tile.num_used)+"/"+str(self.tile.copies)
      memdc = wx.MemoryDC()
      font = wx.NORMAL_FONT
      font.SetPointSize(10)
      memdc.SetFont(font)
      (textwidth, textheight) = memdc.GetTextExtent(txt)
      memdc.SelectObject(bitmap)
      memdc.SetBackground(wx.Brush(wx.WHITE, wx.SOLID))
      extent = wx.Rect(0,0, textwidth, textheight)
      #memdc.Clear()
      memdc.SetTextForeground(wx.BLACK)
      memdc.SetPen(wx.WHITE_PEN)
      memdc.SetBrush(wx.WHITE_BRUSH)
      memdc.DrawRectangle((width-textwidth-4), (height-textheight-4), (textwidth+4), (textheight+4))
      memdc.DrawText(txt,(width-textwidth-2), (height-textheight-2))
      memdc.SelectObject(wx.NullBitmap)
    return bitmap

  def OnPaint(self, event):
    dc = wx.PaintDC(self.HoverPanel)
    dc.DrawBitmap(self.bitmap,0,0,True)
    return

class TilePropertiesDialogCore(PyMapperDialogs.TilePropertiesDialogBase):
  def __init__(self, parent, tile):
    temp_dir = os.getcwd()
    os.chdir(gv.root_directory)
    PyMapperDialogs.TilePropertiesDialogBase.__init__(self, parent)
    os.chdir(temp_dir)
    self.Center()
    
    self.tile = tile

    self.stTileName.SetLabel("Tile Name: "+str(tile.tilenameA))
    self.stSetID.SetLabel("Tile SetID: "+str(tile.tilesetID))
    self.stSetName.SetLabel("Tileset Name: "+str(tile.tilesetName))
    self.stGridSize.SetLabel(str(tile.actualXsize)+" wide by "+str(tile.actualYsize)+" high")
    if (tile.filenameA):
      if (len(tile.filenameA)>35):
        tmp = tile.filenameA[(len(tile.filenameA)-35):len(tile.filenameA)]
        nameA = "..." + tmp
      else:
        nameA = tile.filenameA
    else:
      nameA = "Unnamed"
    if (tile.filenameB):
      if (len(tile.filenameB)>35):
        tmp = tile.filenameB[(len(tile.filenameB)-35):len(tile.filenameB)]
        nameB = "..." + tmp
      else:
        nameB = tile.filenameB
    else:
      nameB = "Unnamed"
      
    self.stFilenameA.SetLabel("Filename side A: \n   "+str(nameA))
    self.stFilenameB.SetLabel("Filename side B: \n   "+str(nameB))

    self.Bind(wx.EVT_PAINT, self.OnPaint)
    self.ImagePanel.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
    
    filename = os.path.join(gv.artwork_directory, 'imagepanel.bmp')
    self.background = wx.Bitmap(filename, wx.BITMAP_TYPE_BMP)

    self.bitmapA = self.ResizeImage(tile.sideA)
    if (tile.sideB != None):
      self.bitmapB = self.ResizeImage(tile.sideB)
    if (tile.sideB == None):
      self.bShowFlipSide.Enable(False)

    if (tile.showingBside):
      self.display = self.bitmapB
    else:
      self.display = self.bitmapA

    self.Update()
    return

  def ResizeImage(self, pil):
    size = self.ImagePanel.GetSize()
    pil_size = wx.Size(pil.GetWidth(), pil.GetHeight())
    deltaW = size.width - pil_size.width
    deltaH = size.height - pil_size.height
    if ((deltaW > 0) and (deltaH < 0)):
      #width is OK, resize height
      aspect = float(size.height)/float(pil_size.height)
      newH = int(aspect*pil_size.height)
      newW = int(aspect*pil_size.width)
      pil = pil.Scale(newW, newH, wx.IMAGE_QUALITY_NORMAL)
    elif ((deltaW < 0) and (deltaH > 0)):
      #height is OK, resize width
      aspect = float(size.width)/float(pil_size.width)
      newH = int(aspect*pil_size.height)
      newW = int(aspect*pil_size.width)
      pil = pil.Scale(newW, newH, wx.IMAGE_QUALITY_NORMAL)
    elif ((deltaW < 0) and (deltaH < 0)):
      # resize height and width
      aspectW = float(size.width)/float(pil_size.width)
      aspectH = float(size.height)/float(pil_size.height)
      if (aspectW < aspectH):
        #resize to width
        newH = int(aspectW*pil_size.height)
        newW = int(aspectW*pil_size.width)
        pil = pil.Scale(newW, newH, wx.IMAGE_QUALITY_NORMAL)
      else:
        newH = int(aspectH*pil_size.height)
        newW = int(aspectH*pil_size.width)
        pil = pil.Scale(newW, newH, wx.IMAGE_QUALITY_NORMAL)
    elif((deltaW > 0) and (deltaH > 0)):
      #image smaller than panel, need to enlarge
      aspectW = float(size.width)/float(pil_size.width)
      aspectH = float(size.height)/float(pil_size.height)
      if (aspectW < aspectH):
        #resize to width
        newH = int(aspectW*pil_size.height)
        newW = int(aspectW*pil_size.width)
        pil = pil.Scale(newW, newH, wx.IMAGE_QUALITY_NORMAL)
      else:
        newH = int(aspectH*pil_size.height)
        newW = int(aspectH*pil_size.width)
        pil = pil.Scale(newW, newH, wx.IMAGE_QUALITY_NORMAL)
    return wx.BitmapFromImage(pil)

  def OnPaint(self, event):
    dc = wx.PaintDC(self.ImagePanel)
    dc.DrawBitmap(self.background, 0, 0, True)
    dc.DrawBitmap(self.display, 0, 0, True)
    event.Skip()
    return

  def OnOK(self, event):
    self.Show(False)
    return

  def ShowFlipSide(self, event):
    if (self.display == self.bitmapA):
      self.display = self.bitmapB
      self.stTileName.SetLabel("Tile Name: "+str(self.tile.tilenameB))
    else:
      self.display = self.bitmapA
      self.stTileName.SetLabel("Tile Name: "+str(self.tile.tilenameA))
    self.RefreshRect(self.ImagePanel.GetRect())
    #self.Update()
    return
  
########################################################################
class FTP_OptionsDialogCore(PyMapperDialogs.FTP_Options):
  """Sets and stores ftp server information"""

  #----------------------------------------------------------------------
  def __init__(self, parent):
    """Constructor"""
    PyMapperDialogs.FTP_Options.__init__(self,parent)
    if (gv.FTP_Filename):
      self.txFilename.SetValue(gv.FTP_Filename)
    if (gv.FTP_Password):
      self.txPassword.SetValue(gv.FTP_Password)
    if (gv.FTP_Server):
      self.txServer.SetValue(gv.FTP_Server)
    if (gv.FTP_Username):
      self.txUsername.SetValue(gv.FTP_Username)
    if (gv.FTP_SaveUserInfo):
      self.cbSaveUserInformation.SetValue(True)
    return
  
  def OnOK(self, event):
    if ((self.txPassword.GetValue() == '') or (self.txUsername.GetValue() == '') 
        or (self.txFilename.GetValue() == '') or (self.txServer.GetValue() == '')):
      wx.MessageBox("Please enter a valid username, server, and/or password")
      return
    else:
      gv.FTP_Filename = self.txFilename.GetValue()
      if (".png" not in gv.FTP_Filename):
        gv.FTP_Filename += ".png"
      gv.FTP_Password = self.txPassword.GetValue()
      gv.FTP_Server = self.txServer.GetValue()
      gv.FTP_Username = self.txUsername.GetValue()
      if (self.cbSaveUserInformation.IsChecked()):
        try:
          settings = open(os.path.join(gv.root_directory, "ftp_settings.ini"), 'w')
        except:
          logging.error("Could not open ftp settings file")
          wx.MessageBox("Could not open ftp settings file.")
          return
        
        settings.write((gv.FTP_Filename+"\n"))
        settings.write((gv.FTP_Password+"\n"))
        settings.write((gv.FTP_Username+"\n"))
        settings.write((gv.FTP_Server+"\n"))
        settings.close()
    self.EndModal(True)
    return
  
  def OnCancel(self, event):
    self.EndModal(False)
    return
  
  def OnHelp(self, event):
    helpText = "The informaton for this dialog is used to log in to a remote FTP site where the current map image will be uploaded.  The image will be saved in .png format on the remote site.\n\nNote that if user information is saved on disk, it is NOT encrypted.  It is never sent to anyone, but it would be available on the disk if someone goes snooping.  Otherwise, the information is just saved for this session of pymapper."
    dlg = HelpDialog(self, helpText)
    dlg.ShowModal()
    return
    
    
  

class FilterTagsDialogCore(PyMapperDialogs.FilterTagsDialogBase):
  def __init__(self, parent, assign, tilelist=None, singletile=None):
    #assign is True when used in the Tileset Editor, when assigning tags to tiles
    #otherwise, it is False when used as the display filter
    self.assign = assign
    if (assign):
      self.tile_list = []
      self.tile_list.append(singletile)
    else:
      self.tile_list = tilelist

    temp_dir = os.getcwd()
    os.chdir(gv.root_directory)
    PyMapperDialogs.FilterTagsDialogBase.__init__(self, parent)
    os.chdir(temp_dir)
    
    # Define variables for the controls, binding event handlers 
    if (assign):
      self.bSelectAll.Show(False)
      self.bSelectNone.Show(False)
      self.bInvertSelection.Show(False)
    else:
      self.bCancel.Show(False)

    if (self.assign):
      self.DGRuneTag.Enable(True)
      self.DGDoorTag.Enable(True)
      self.DGLadderTag.Enable(True)
      self.DGLargeRoomTag.Enable(True)
      self.DGSmallRoomTag.Enable(True)
      self.DGHallwayTag.Enable(True)
      self.DGTowerSectionTag.Enable(True)
      self.DGParapetWallTag.Enable(True)
      self.DGTrapTag.Enable(True)
      self.DGStairsTag.Enable(True)
      self.DGDecorationTag.Enable(True)
      self.DGTransitionTag.Enable(True)
      self.CVPassageTag.Enable(True)
      self.CVEndTag.Enable(True)
      self.CVLargeCavernTag.Enable(True)
      self.CVPartialCavernTag.Enable(True)
      self.CVDecorationTag.Enable(True)
      self.CVTransitionTag.Enable(True)
      self.WLPondTag.Enable(True)
      self.WLTreesTag.Enable(True)
      self.WLRoadTag.Enable(True)
      self.WLStreamTag.Enable(True)
      self.WLPathTag.Enable(True)
      self.WLRuinsTag.Enable(True)
      self.WLDecorationTag.Enable(True)
      self.WLTransitionTag.Enable(True)
      self.TNTowerTag.Enable(True)
      self.TNTownTag.Enable(True)
      self.TNSmallBuildingTag.Enable(True)
      self.TNLargeBuildingTag.Enable(True)
      self.TNSewerTag.Enable(True)
      self.TNDecorationTag.Enable(True)
      self.TNLadderTag.Enable(True)
      self.TNTransitionTag.Enable(True)
      self.TNShipTag.Enable(True)

    for tile in self.tile_list:
      if tile.taglist == []:
        continue
      for tag in tile.taglist:
        if tag == 'DGRune':
          self.DGRuneTag.Enable(True)
          self.DGRuneTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'DGDoor':
          self.DGDoorTag.Enable(True)
          self.DGDoorTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'DGLadder':
          self.DGLadderTag.Enable(True)
          self.DGLadderTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'DGLargeRoom':
          self.DGLargeRoomTag.Enable(True)
          self.DGLargeRoomTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'DGSmallRoom':
          self.DGSmallRoomTag.Enable(True)
          self.DGSmallRoomTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'DGHallway':
          self.DGHallwayTag.Enable(True)
          self.DGHallwayTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'DGTowerSection':
          self.DGTowerSectionTag.Enable(True)
          self.DGTowerSectionTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'DGParapetWall':
          self.DGParapetWallTag.Enable(True)
          self.DGParapetWallTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'DGTrap':
          self.DGTrapTag.Enable(True)
          self.DGTrapTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'DGStairs':
          self.DGStairsTag.Enable(True)
          self.DGStairsTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'DGDecoration':
          self.DGDecorationTag.Enable(True)
          self.DGDecorationTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'DGTransition':
          self.DGTransitionTag.Enable(True)
          self.DGTransitionTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'CVPassage':
          self.CVPassageTag.Enable(True)
          self.CVPassageTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'CVEnd':
          self.CVEndTag.Enable(True)
          self.CVEndTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'CVLargeCavern':
          self.CVLargeCavernTag.Enable(True)
          self.CVLargeCavernTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'CVPartialCavern':
          self.CVPartialCavernTag.Enable(True)
          self.CVPartialCavernTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'CVDecoration':
          self.CVDecorationTag.Enable(True)
          self.CVDecorationTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'CVTransition':
          self.CVTransitionTag.Enable(True)
          self.CVTransitionTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'WLPond':
          self.WLPondTag.Enable(True)
          self.WLPondTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'WLTrees':
          self.WLTreesTag.Enable(True)
          self.WLTreesTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'WLRoad':
          self.WLRoadTag.Enable(True)
          self.WLRoadTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'WLStream':
          self.WLStreamTag.Enable(True)
          self.WLStreamTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'WLPath':
          self.WLPathTag.Enable(True)
          self.WLPathTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'WLRuins':
          self.WLRuinsTag.Enable(True)
          self.WLRuinsTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'WLDecoration':
          self.WLDecorationTag.Enable(True)
          self.WLDecorationTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'WLTransition':
          self.WLTransitionTag.Enable(True)
          self.WLTransitionTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'TNTower':
          self.TNTowerTag.Enable(True)
          self.TNTowerTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'TNTown':
          self.TNTownTag.Enable(True)
          self.TNTownTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'TNSmallBuilding':
          self.TNSmallBuildingTag.Enable(True)
          self.TNSmallBuildingTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'TNLargeBuilding':
          self.TNLargeBuildingTag.Enable(True)
          self.TNLargeBuildingTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'TNSewer':
          self.TNSewerTag.Enable(True)
          self.TNSewerTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'TNDecoration':
          self.TNDecorationTag.Enable(True)
          self.TNDecorationTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'TNLadder':
          self.TNLadderTag.Enable(True)
          self.TNLadderTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'TNTransition':
          self.TNTransitionTag.Enable(True)
          self.TNTransitionTag.SetValue(tile.ShowOnTilePanel)
        if tag == 'TNShip':
          self.TNShipTag.Enable(True)
          self.TNShipTag.SetValue(tile.ShowOnTilePanelue)

  def OnOK(self, event):
    if (self.assign):
      self.EndModal(True)
    else:
      self.Show(False)
    return

  def OnCancel(self, event):
    if (self.assign):
      self.EndModal(False)
    else:
      self.Show(False)
    return

#class TilesetEditorDialogCore(PyMapperDialogs.ImportTilesDialogBase):
class TilesetEditorDialogCore(PyMapperDialogs.TilesetEditor2Base):
  def __init__(self, parent):
    temp_dir = os.getcwd()
    os.chdir(gv.root_directory)
    #PyMapperDialogs.ImportTilesDialogBase.__init__(self, parent)
    PyMapperDialogs.TilesetEditor2Base.__init__(self, parent)
    os.chdir(temp_dir)
    self.PromptSave = False
    self.Center()
    self.PreviewImage = None
    self.PreviewImageResolution = None
    self.PreviewImageSize = None

    try:
      os.chdir(gv.tiles_directory)
    except OSError:
      text = "Error in ImportTileDialog: Could not change to "+gv.tiles_directory
      wx.MessageBox(message=text, caption="Error", style=wx.ICON_EXCLAMATION)
      return False
    self.TilesetLoaded = False
    self.ScaleA = 1.0
    self.ScaleB = 1.0

    #Edit tile parameters subset
    self.SideAImageIndex = None #Index of the selected side A image
    self.SideBImageIndex = None #Index of the selected side B image

    
    #Tileset subset
    self.TilesetFilename = None
    self.TilesetID = None
    self.NumSets = 1

    self.Bind(wx.EVT_PAINT, self.OnPaint)
    self.Tilelist = []
    self.SideAImage = None  #wxImage format 
    self.SideBImage = None
    self.bitmapA = None
    self.bitmapB = None
    self.taglist = []

    self.TilesetFilename = None
    self.TilesetPath = None
    self.TilesetFilenamePath = None
    self.TilesetID = None
    self.NumSets = None
    self.ImageList = []
    self.ImageListPaths = []

    #Each tile grid edge can have a definition for the random generator
    #Edge will default to connection
    self.TopBorderA = ['connect']  #describes the type of edge, either 'wall' or 'connect' from left to right
    self.BottomBorderA = ['connect']
    self.RightBorderA = ['connect']  #from top to bottom
    self.LeftBorderA = ['connect']
    self.TopBorderB = ['connect']  #describes the type of edge, either 'wall' or 'connect' from left to right
    self.BottomBorderB = ['connect']
    self.RightBorderB = ['connect']  #from top to bottom
    self.LeftBorderB = ['connect']

    self.GridColorA = wx.Colour(255,0,0)
    self.GridColorB = wx.Colour(255,0,0)
    self.TilesetOKtoSave = False  #set to true when OK to save tileset
    return
  
  def OnChangeNotebookPage(self,event):
    #update the wxListBox items
    self.UpdateTilesetBox()
    self.SetImageListBox()
    event.Skip()
    return
  
  def OnPanelAClick(self, event):
    if (self.bSetWallsSideA.GetValue()):
      mouse = event.GetPosition()
      height = self.bitmapA.GetHeight()
      width = self.bitmapA.GetWidth()
      rows = self.spYSize.GetValue()
      cols = self.spXSize.GetValue()
      Ysegment = height/rows #length of a square side
      Xsegment = width/cols 
      if (mouse.y < Ysegment/4):  #close enough to the top edge
        index = int(mouse.x/Xsegment)
        if (index > len(self.TopBorderA)):
          #clicked off the image
          return
        if (self.TopBorderA[index] == 'wall'):
          self.TopBorderA[index] = 'connect'
        elif (self.TopBorderA[index] == 'connect'):
          self.TopBorderA[index] = 'door'
        elif (self.TopBorderA[index] == 'door'):
          self.TopBorderA[index] = 'obstruction'
        elif (self.TopBorderA[index] == 'obstruction'):
          self.TopBorderA[index] = 'outside'
        else:
          self.TopBorderA[index] = 'wall'
      if (mouse.x < Xsegment/4):  #close enough to the left edge
        index = int(mouse.y/Ysegment)
        if (index > len(self.LeftBorderA)):
          return
        if (self.LeftBorderA[index] == 'wall'):
          self.LeftBorderA[index] = 'connect'
        elif (self.LeftBorderA[index] == 'connect'):
          self.LeftBorderA[index] = 'door'
        elif (self.LeftBorderA[index] == 'door'):
          self.LeftBorderA[index] = 'obstruction'
        elif (self.LeftBorderA[index] == 'obstruction'):
          self.LeftBorderA[index] = 'outside'
        else:
          self.LeftBorderA[index] = 'wall'
      if (mouse.y > (height-Ysegment/4)):  #close enough to the bottom edge
        index = int(mouse.x/Xsegment)
        if (index > len(self.BottomBorderA)):
          return
        if (self.BottomBorderA[index] == 'wall'):
          self.BottomBorderA[index] = 'connect'
        elif (self.BottomBorderA[index] == 'connect'):
          self.BottomBorderA[index] = 'door'
        elif (self.BottomBorderA[index] == 'door'):
          self.BottomBorderA[index] = 'obstruction'
        elif (self.BottomBorderA[index] == 'obstruction'):
          self.BottomBorderA[index] = 'outside'
        else:
          self.BottomBorderA[index] = 'wall'
      if (mouse.x > (width-Xsegment/4)):  #close enough to the left edge
        index = int(mouse.y/Ysegment)
        if (index > len(self.RightBorderA)):
          return
        if (self.RightBorderA[index] == 'wall'):
          self.RightBorderA[index] = 'connect'
        elif (self.RightBorderA[index] == 'connect'):
          self.RightBorderA[index] = 'door'
        elif (self.RightBorderA[index] == 'door'):
          self.RightBorderA[index] = 'obstruction'
        elif (self.RightBorderA[index] == 'obstruction'):
          self.RightBorderA[index] = 'outside'
        else:
          self.RightBorderA[index] = 'wall'
    self.DrawImagePanels(panelA=self.Setup_SideAImagePanel, panelB=self.Setup_SideBImagePanel)
    return

  def OnPanelBClick(self, event):
    if (not self.bitmapB):
      return
    if (self.bSetWallsSideB.GetValue()):
      mouse = event.GetPosition()
      height = self.bitmapB.GetHeight()
      width = self.bitmapB.GetWidth()
      rows = self.spYSize.GetValue()
      cols = self.spXSize.GetValue()
      Ysegment = height/rows #length of a square side
      Xsegment = width/cols 
      if (mouse.y < Ysegment/4):  #close enough to the top edge
        index = int(mouse.x/Xsegment)
        if (index > len(self.TopBorderB)):
          #clicked off the image
          return
        if (self.TopBorderB[index] == 'wall'):
          self.TopBorderB[index] = 'connect'
        elif (self.TopBorderB[index] == 'connect'):
          self.TopBorderB[index] = 'door'
        elif (self.TopBorderB[index] == 'door'):
          self.TopBorderB[index] = 'obstruction'
        elif (self.TopBorderB[index] == 'obstruction'):
          self.TopBorderB[index] = 'outside'
        else:
          self.TopBorderB[index] = 'wall'
      if (mouse.x < Xsegment/4):  #close enough to the left edge
        index = int(mouse.y/Ysegment)
        if (index > len(self.LeftBorderB)):
          return
        if (self.LeftBorderA[index] == 'wall'):
          self.LeftBorderB[index] = 'connect'
        elif (self.LeftBorderB[index] == 'connect'):
          self.LeftBorderB[index] = 'door'
        elif (self.LeftBorderB[index] == 'door'):
          self.LeftBorderB[index] = 'obstruction'
        elif (self.LeftBorderB[index] == 'obstruction'):
          self.LeftBorderB[index] = 'outside'
        else:
          self.LeftBorderB[index] = 'wall'
      if (mouse.y > (height-Ysegment/4)):  #close enough to the bottom edge
        index = int(mouse.x/Xsegment)
        if (index > len(self.BottomBorderB)):
          return
        if (self.BottomBorderB[index] == 'wall'):
          self.BottomBorderB[index] = 'connect'
        elif (self.BottomBorderB[index] == 'connect'):
          self.BottomBorderB[index] = 'door'
        elif (self.BottomBorderB[index] == 'door'):
          self.BottomBorderB[index] = 'obstruction'
        elif (self.BottomBorderB[index] == 'obstruction'):
          self.BottomBorderB[index] = 'outside'
        else:
          self.BottomBorderB[index] = 'wall'
      if (mouse.x > (width-Xsegment/4)):  #close enough to the left edge
        index = int(mouse.y/Ysegment)
        if (index > len(self.RightBorderB)):
          return
        if (self.RightBorderB[index] == 'wall'):
          self.RightBorderB[index] = 'connect'
        elif (self.RightBorderB[index] == 'connect'):
          self.RightBorderB[index] = 'door'
        elif (self.RightBorderB[index] == 'door'):
          self.RightBorderB[index] = 'obstruction'
        elif (self.RightBorderB[index] == 'obstruction'):
          self.RightBorderB[index] = 'outside'
        else:
          self.RightBorderB[index] = 'wall'
    self.DrawImagePanels(panelA=self.Setup_SideAImagePanel, panelB=self.Setup_SideBImagePanel)
    return

  def DrawWalls(self, dc, tileside):
    '''Draw a red segment on the side for a wall, 
    blue for a door opening, green for a connection'''
    wallPen = wx.RED_PEN
    wallPen.SetWidth(3)
    connectPen = wx.GREEN_PEN
    connectPen.SetWidth(3)
    outsideColor = wx.Colour(157,0,255,255)
    outsidePen = wx.Pen(outsideColor, width=3)
    blueColor = wx.Colour(0,0,255,255)
    doorPen = wx.Pen(blueColor, width=3)
    obst_color = wx.Colour(255,106,0)
    obstructionPen = wx.Pen(obst_color, width=3)
    xpos = 0
    ypos = 0

    if (tileside == 'SideA'):
      height = self.bitmapA.GetHeight()
      width = self.bitmapA.GetWidth()
      x_length = width / self.spXSize.GetValue()
      y_length = height / self.spYSize.GetValue()
      #check to see if the number of edges matches the number of elements in the lists
      while (self.spXSize.GetValue() > len(self.BottomBorderA)):
        self.BottomBorderA.append('connect')
      while (self.spYSize.GetValue() > len(self.RightBorderA)):
        self.RightBorderA.append('connect')
      while (self.spYSize.GetValue() > len(self.LeftBorderA)):
        self.LeftBorderA.append('connect')
      while (self.spXSize.GetValue() > len(self.TopBorderA)):
        self.TopBorderA.append('connect')

      for segment in self.TopBorderA:
        if (segment == 'wall'):
          dc.SetPen(wallPen)
        elif (segment == 'door'):
          dc.SetPen(doorPen)
        elif (segment == 'obstruction'):
          dc.SetPen(obstructionPen)
        elif (segment == 'outside'):
          dc.SetPen(outsidePen)
        else:
          dc.SetPen(connectPen)
        dc.DrawLine(xpos, ypos, xpos+x_length, ypos)
        xpos += x_length
      xpos = 0
      ypos = height
      for segment in self.BottomBorderA:
        if (segment == 'wall'):
          dc.SetPen(wallPen)
        elif (segment == 'door'):
          dc.SetPen(doorPen)
        elif (segment == 'obstruction'):
          dc.SetPen(obstructionPen)
        elif (segment == 'outside'):
          dc.SetPen(outsidePen)
        else:
          dc.SetPen(connectPen)
        dc.DrawLine(xpos, ypos, xpos+x_length, ypos)
        xpos += x_length
      xpos = 0
      ypos = 0
      for segment in self.LeftBorderA:
        if (segment == 'wall'):
          dc.SetPen(wallPen)
        elif (segment == 'door'):
          dc.SetPen(doorPen)
        elif (segment == 'obstruction'):
          dc.SetPen(obstructionPen)
        elif (segment == 'outside'):
          dc.SetPen(outsidePen)
        else:
          dc.SetPen(connectPen)
        dc.DrawLine(xpos, ypos, xpos, ypos+y_length)
        ypos += y_length
      xpos = width
      ypos = 0
      for segment in self.RightBorderA:
        if (segment == 'wall'):
          dc.SetPen(wallPen)
        elif (segment == 'door'):
          dc.SetPen(doorPen)
        elif (segment == 'obstruction'):
          dc.SetPen(obstructionPen)
        elif (segment == 'outside'):
          dc.SetPen(outsidePen)
        else:
          dc.SetPen(connectPen)
        dc.DrawLine(xpos, ypos, xpos, ypos+y_length)
        ypos += y_length
    elif ((tileside == 'SideB') and (self.bitmapB)):  #tileside == 'SideB'
      height = self.bitmapB.GetHeight()
      width = self.bitmapB.GetWidth()
      x_length = width / self.spXSize.GetValue()
      y_length = height / self.spYSize.GetValue()
      while (self.spXSize.GetValue() > len(self.BottomBorderB)):
        self.BottomBorderB.append('connect')
      while (self.spYSize.GetValue() > len(self.RightBorderB)):
        self.RightBorderB.append('connect')
      while (self.spYSize.GetValue() > len(self.LeftBorderB)):
        self.LeftBorderB.append('connect')
      while (self.spXSize.GetValue() > len(self.TopBorderB)):
        self.TopBorderB.append('connect')
      for segment in self.TopBorderB:
        if (segment == 'wall'):
          dc.SetPen(wallPen)
        elif (segment == 'door'):
          dc.SetPen(doorPen)
        elif (segment == 'obstruction'):
          dc.SetPen(obstructionPen)
        elif (segment == 'outside'):
          dc.SetPen(outsidePen)
        else:
          dc.SetPen(connectPen)
        dc.DrawLine(xpos, ypos, xpos+x_length, ypos)
        xpos += x_length
      xpos = 0
      ypos = height
      for segment in self.BottomBorderB:
        if (segment == 'wall'):
          dc.SetPen(wallPen)
        elif (segment == 'door'):
          dc.SetPen(doorPen)
        elif (segment == 'obstruction'):
          dc.SetPen(obstructionPen)
        elif (segment == 'outside'):
          dc.SetPen(outsidePen)
        else:
          dc.SetPen(connectPen)
        dc.DrawLine(xpos, ypos, xpos+x_length, ypos)
        xpos += x_length
      xpos = 0
      ypos = 0
      for segment in self.LeftBorderB:
        if (segment == 'wall'):
          dc.SetPen(wallPen)
        elif (segment == 'door'):
          dc.SetPen(doorPen)
        elif (segment == 'obstruction'):
          dc.SetPen(obstructionPen)
        elif (segment == 'outside'):
          dc.SetPen(outsidePen)
        else:
          dc.SetPen(connectPen)
        dc.DrawLine(xpos, ypos, xpos, ypos+y_length)
        ypos += y_length
      xpos = width
      ypos = 0
      for segment in self.RightBorderB:
        if (segment == 'wall'):
          dc.SetPen(wallPen)
        elif (segment == 'door'):
          dc.SetPen(doorPen)
        elif (segment == 'obstruction'):
          dc.SetPen(obstructionPen)
        elif (segment == 'outside'):
          dc.SetPen(outsidePen)
        else:
          dc.SetPen(connectPen)
        dc.DrawLine(xpos, ypos, xpos, ypos+y_length)
        ypos += y_length
    return

  def OnHelp(self, event):  #This is the help page for the Tileset page
    text = "The tileset ID is the name of the subfolder in the /tiles/ subfolder where pymapper is installed. \n\nInstructions: \nTo create a new tileset:\n  1.  Using the 'Add Images...' button, select the images you want to add to the current tileset.  Copies will be saved to a subfolder in the /tiles/ folder where PyMapper is installed. \n2.  Select an image from the list and then set the image using the 'Set Image Side' buttons.  There must always be a side A, but side B is optional.\n3.  Set the X and Y sizes of the images.  The actual size of the image does not matter;  the two image sides may have different actual size, but will be set to the same X/Y grid size.\n4.  Enter a tile name (optional).\n5.  Add the tile to the tileset list with the 'Add Current Tile to Set' button.\n6.  Be sure to save your tileset prior to exiting."
    dlg = HelpDialog(self, text)
    dlg.ShowModal()
    return
  
  def OnHelpImages(self, event):
    text = "Instructions: \nTo create a new tileset:\n  1.  Using the 'Add Images...' button, select the images you want to add to the current tileset.  Copies will be saved to a subfolder in the /tiles/ folder where PyMapper is installed. \n2.  Select an image from the list and then set the image using the 'Set Image Side' buttons.  There must always be a side A, but side B is optional.\n3.  Set the X and Y sizes of the images.  The actual size of the image does not matter;  the two image sides may have different actual size, but will be set to the same X/Y grid size.\n4.  Enter a tile name (optional).\n5.  Add the tile to the tileset list with the 'Add Current Tile to Set' button.\n6.  Be sure to save your tileset prior to exiting."
    dlg = HelpDialog(self, text)
    dlg.ShowModal()
    return

  def OnHelpSetup(self, event):
    text = "Instructions: \nTo add tiles to a tileset:\n  1.  Using the 'Add Images...' button, select the images you want to add to the current tileset.  Copies will be saved to a subfolder in the /tiles/ folder where PyMapper is installed. \n2.  Select an image from the list and then set the image using the 'Set Image Side' buttons.  There must always be a side A, but side B is optional.\n3.  Set the X and Y sizes of the images.  The actual size of the image does not matter;  the two image sides may have different actual size, but will be set to the same X/Y grid size.\n4.  Enter a tile name (optional).\n5.  Add the tile to the tileset list with the 'Add Current Tile to Set' button.\n6.  Be sure to save your tileset prior to exiting."
    dlg = HelpDialog(self, text)
    dlg.ShowModal()
    return
  
  def AddImages(self, event=None):
    dlg = wx.FileDialog(self, message="Choose files", defaultDir=os.getcwd(),
                        defaultFile="", wildcard=images_wildcard,
                        style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR)
    if (dlg.ShowModal() == wx.ID_OK):
      newImageList = dlg.GetFilenames()
      newImageListPaths = dlg.GetPaths()
      if (self.ImageList == []):
        start_index = 0
      else:
        start_index = len(self.ImageList)
      for i in range(len(newImageList)):
        self.ImageList.append(newImageList[i])
        self.ImageListPaths.append(newImageListPaths[i])
      self.ImageList.sort()
      self.ImageListPaths.sort()
      self.ImageListBox_Setup.Set(self.ImageList)
      returnval = True
    else:
      returnval = False
    dlg.Destroy()
    return returnval

  def SetImageListBox(self):
    self.ImageListBox_Setup.Set(self.ImageList)
    return

  def RefreshImages(self, event=None):
    self.DrawImagePanels(panelA=self.Setup_SideAImagePanel, panelB=self.Setup_SideBImagePanel)
    return

  def RemoveImage(self, event):
    """Remove images from the available images list"""
    rm = self.lbSetup_TilesetBox.GetSelections()
    for i in rm:
      self.ImageList.pop(i)
      self.ImageListPaths.pop(i)
      self.ImageList.insert(i, "X")
      self.ImageListPaths.insert(i, "X")
    for i in rm:
      self.ImageList.remove("X")
      self.ImageListPaths.remove("X")
    self.DrawImagePanels(panelA=self.Setup_SideAImagePanel, panelB=self.Setup_SideBImagePanel)
    self.SetImageListBox()
    return

  def BitmapImageForPanel(self, side, scale, panelA, panelB):
    """take the selected image side and return a bitmap for display"""
    if ((self.SideAImageIndex == None) and (self.SideBImageIndex == None)):
      #nothing to display
      return None
    if (self.ImageListPaths == []):
      #nothing to display
      return None
    CurrentImage = None
    if (side == self.SideAImageIndex):
      filename = self.ImageListPaths[self.SideAImageIndex]
      panelsize = panelA.GetSize()
      active_side = 'A'
    elif (side == self.SideBImageIndex):
      filename = self.ImageListPaths[self.SideBImageIndex]
      panelsize = panelB.GetSize()
      active_side = 'B'
    else:
      return False
    pilImage = wx.Image(filename, wx.BITMAP_TYPE_ANY)
    if (not pilImage.IsOk()):
      logging.error("Could not open %s",filename)
      pilImage = app.ImageNotFound

    if (active_side == 'A'):
      self.SideAImage = pilImage
    else:
      self.SideBImage = pilImage

    width = pilImage.GetWidth()
    height = pilImage.GetHeight()
    aspect_image = float(width)/float(height)
    aspect_panel = float(panelsize[0])/float(panelsize[1])

    if (aspect_image < 1.0):
      #height > width
      if (height > panelsize[1]):
        height = int(panelsize[1] * 0.85)
        width = int(aspect_image * height)
    elif (aspect_image == 1.0):
      #height = width
      if ((height > panelsize[1]) or (width > panelsize[0])):
        width = int(panelsize[0] * 0.85)
        height = int(panelsize[1] * 0.85)
    elif (aspect_image > 1.0):
      # width > height
      if (width > panelsize[0]):
        width = int(panelsize[0] * 0.85)
        height = int((width / aspect_image))
    width *= scale
    height *= scale
    pilImage = pilImage.Scale(width, height, wx.IMAGE_QUALITY_NORMAL)

    return wx.BitmapFromImage(pilImage)

  def DrawImagePanels(self, event=None, panelA=None, panelB=None):
    if (not panelA) or (not panelB):
      logging.error("panel A or B not available")
      return

    SideAImagePanelDC = wx.ClientDC(panelA)
    SideBImagePanelDC = wx.ClientDC(panelB)
    SideAImagePanelDC.SetBrush(wx.WHITE_BRUSH)
    SideBImagePanelDC.SetBrush(wx.WHITE_BRUSH)
    SideAImagePanelDC.Clear()
    SideBImagePanelDC.Clear()
    
    if ((self.SideAImageIndex == None) and (self.SideBImageIndex == None)):
      #no images to display on panels
      return 

    # Number of rows, columns available in the MapPanel
    ncolumns = self.spXSize.GetValue()
    nrows = self.spYSize.GetValue()

    if (self.SideAImageIndex != None):
      #display the Side A image
      self.bitmapA = self.BitmapImageForPanel(self.SideAImageIndex, self.ScaleA, panelA, panelB)
      SideAImagePanelDC.DrawBitmap(self.bitmapA, 0, 0, True)
    else:
      SideAImagePanelDC.Clear()

    if (self.SideBImageIndex != None):
      #display the Side B image
      self.bitmapB = self.BitmapImageForPanel(self.SideBImageIndex, self.ScaleB, panelA, panelB)
      SideBImagePanelDC.DrawBitmap(self.bitmapB, 0, 0, True)
    else:
      SideBImagePanelDC.Clear()
      bitmapB = None

    SideAImagePanelDC.SetPen(wx.RED_PEN)

    #draw the grid
    line_penA = wx.Pen(self.GridColorA, gv.GridPenWidth, gv.GridPenStyle)
    line_penB = wx.Pen(self.GridColorB, gv.GridPenWidth, gv.GridPenStyle)
    SideAImagePanelDC.SetPen(line_penA)
    SideBImagePanelDC.SetPen(line_penB)

    for x in range(ncolumns+1):
      #draw the column lines
      if (self.SideAImageIndex != None):
        xposA = (x * (self.bitmapA.GetWidth()/ncolumns))
        ypos_topA = 0
        ypos_bottomA = self.bitmapA.GetHeight()
        SideAImagePanelDC.DrawLine(xposA, ypos_topA, xposA, ypos_bottomA)
      if (self.SideBImageIndex != None):
        xposB = (x * (self.bitmapB.GetWidth()/ncolumns))
        ypos_topB = 0
        ypos_bottomB = self.bitmapB.GetHeight()
        SideBImagePanelDC.DrawLine(xposB, ypos_topB, xposB, ypos_bottomB)
    for y in range(nrows+1):
      #draw the row lines
      if (self.SideAImageIndex != None):
        yposA = (y * (self.bitmapA.GetHeight()/nrows))
        xpos_leftA = 0
        xpos_rightA = self.bitmapA.GetWidth()
        SideAImagePanelDC.DrawLine(xpos_leftA, yposA, xpos_rightA, yposA)
      if (self.SideBImageIndex != None):
        yposB = (y * (self.bitmapB.GetHeight()/nrows))
        xpos_leftB = 0
        xpos_rightB = self.bitmapB.GetWidth()
        SideBImagePanelDC.DrawLine(xpos_leftB, yposB, xpos_rightB, yposB)
    if (self.bSetWallsSideA.GetValue()):
      self.DrawWalls(SideAImagePanelDC, 'SideA')
    if (self.bSetWallsSideB.GetValue() and (self.bitmapB != None)):
      self.DrawWalls(SideBImagePanelDC, 'SideB')
    return

  def OnClearImageSelection(self, event):
    self.ImageListBox_Setup.SetSelection(wx.NOT_FOUND)
    self.PreviewImage = None
    self.PreviewImageResolution = None
    self.DrawImagePreview(panel=self.pnImagePreview_Setup)
    self.bSetImageSideA.Enable(False)
    self.bSetImageSideB.Enable(False)
    self.bSwapImageSides.Enable(False)
    return
  
  def OnChangeGridColorA_setup(self, event):
    self.GridColorA = self.cpkSideAGridColor_Setup.GetColour()
    self.DrawImagePanels(panelA=self.Setup_SideAImagePanel, panelB=self.Setup_SideBImagePanel)
    return

  def OnChangeGridColorB_setup(self, event):
    self.GridColorB = self.cpkSideBGridColor_Setup.GetColour()
    self.DrawImagePanels(panelA=self.Setup_SideAImagePanel, panelB=self.Setup_SideBImagePanel)
    return

  def OnChangeGridColorA_tileset(self, event):
    self.GridColorA = self.cpkSideAGridColor_Tileset.GetColour()
    self.DrawImagePanels(panelA=self.Tileset_SideAImagePanel, panelB=self.Tileset_SideBImagePanel)
    return

  def OnChangeGridColorB_tileset(self, event):
    self.GridColorB = self.cpkSideBGridColor_Tileset.GetColour()
    self.DrawImagePanels(panelA=self.Tileset_SideAImagePanel, panelB=self.Tileset_SideBImagePanel)
    return

  def OnImageListBox(self, event):
    """User selected an image from the available list"""
    if (event.GetId() == PyMapperDialogs.Setup_ImageListBox):
      item = self.ImageListBox_Setup.GetSelection()
      ImagePanel = self.pnImagePreview_Setup
      ImageSizeString = self.stImageSize_Setup
    if (item == wx.NOT_FOUND):
      self.PreviewImage = None
      return
    
    image = wx.Image(self.ImageListPaths[item], wx.BITMAP_TYPE_ANY)
    self.PreviewImageSize = image.GetSize()  #this is the size of the image on disk before scaling    
    ImageSizeString.SetLabel(("Source image size:  %d x %d pixels" % (self.PreviewImageSize.width, self.PreviewImageSize.height)))
    
    self.bSetImageSideA.Enable(True)
    self.bSetImageSideB.Enable(True)
    
    panelsize = ImagePanel.GetSize()
    
    width = image.GetWidth()
    height = image.GetHeight()
    aspect_image = float(width)/float(height)
    aspect_panel = float(panelsize[0])/float(panelsize[1])

    if (aspect_image < 1.0):
      #height > width
      if (height > panelsize[1]):
        height = int(panelsize[1] * 0.95)
        width = int(aspect_image * height)
    elif (aspect_image == 1.0):
      #height = width
      if ((height > panelsize[1]) or (width > panelsize[0])):
        width = int(panelsize[0] * 0.95)
        height = int(panelsize[1] * 0.95)
    elif (aspect_image > 1.0):
      # width > height
      if (width > panelsize[0]):
        width = int(panelsize[0] * 0.95)
        height = int((width / aspect_image))
    self.PreviewImage = wx.BitmapFromImage(image.Scale(width, height, wx.IMAGE_QUALITY_NORMAL))
    self.DrawImagePreview(panel=ImagePanel)
    return

  def SwapImageSides (self, event):
    tempA = self.SideAImageIndex
    tempB = self.SideBImageIndex
    self.SideAImageIndex = tempB
    self.SideBImageIndex = tempA
    self.DrawImagePanels(panelA=self.Setup_SideAImagePanel, panelB=self.Setup_SideBImagePanel)
    self.bUpdateTile.Enable(True)
    self.PromptSave = True
    return

  def RemoveImageSideA(self, event):
    self.SideAImageIndex = None
    self.taglist = []
    self.bRemoveImageSideA.Enable(False)
    self.bUpdateTile.Enable(True)
    self.DrawImagePanels(panelA=self.Setup_SideAImagePanel, panelB=self.Setup_SideBImagePanel)
    self.PromptSave = True
    return

  def RemoveImageSideB(self, event):
    self.SideBImageIndex = None
    self.bRemoveImageSideB.Enable(False)
    self.bUpdateTile.Enable(True)
    self.DrawImagePanels(panelA=self.Setup_SideAImagePanel, panelB=self.Setup_SideBImagePanel)
    self.PromptSave = True
    return

  def SetImageSideA(self, event):
    listindex = self.ImageListBox_Setup.GetSelections()
    if (listindex == ()):
      #if nothing is selected, do nothing
      return
    if (len(listindex) > 1):
      #must select a single file only for this step
      wx.MessageBox("Please select a single file only")
      return
    self.SideAImageIndex = listindex[0]
    self.bRemoveImageSideA.Enable(True)
    self.bUpdateTile.Enable(True)
    self.taglist = []  #reset the tag filters
    self.DrawImagePanels(panelA=self.Setup_SideAImagePanel, panelB=self.Setup_SideBImagePanel)
    self.PromptSave = True
    return

  def SetImageSideB(self, event):
    listindex = self.ImageListBox_Setup.GetSelections()
    if (listindex == ()):
      #if nothing is selected, do nothing
      return
    if (len(listindex) > 1):
      #must select a single file only for this step
      wx.MessageBox("Please select a single file only")
      return
    self.SideBImageIndex = listindex[0]
    self.bRemoveImageSideB.Enable(True)
    self.bUpdateTile.Enable(True)
    self.DrawImagePanels(panelA=self.Setup_SideAImagePanel, panelB=self.Setup_SideBImagePanel)
    self.PromptSave = True
    return

  def DrawImagePreview(self, event=None, panel=None):
    """Draw the image on the preview panel, panel must be a wxPanel
    """
    panelsize = panel.GetSize()
    dc = wx.ClientDC(panel)
    dc.Clear()
    dc.SetPen(wx.Pen(wx.Colour(155,174,255)))
    dc.SetBrush(wx.Brush(wx.Colour(155,174,255)))
    dc.DrawRectangle(0,0,panelsize.x, panelsize.y) #draw the black background

    if (self.PreviewImage):
      imagesizeX = self.PreviewImage.GetWidth()
      imagesizeY = self.PreviewImage.GetHeight()

      Xoffset = (panelsize.x/2) - (imagesizeX/2.0)
      Yoffset = (panelsize.y/2) - (imagesizeY/2.0)
      dc.DrawBitmap(self.PreviewImage,Xoffset,Yoffset,True)
    return
  
  def OnPaint(self, event):
    self.DrawImagePanels(panelA=self.Tileset_SideAImagePanel, panelB=self.Tileset_SideBImagePanel)
    self.DrawImagePanels(panelA=self.Setup_SideAImagePanel, panelB=self.Setup_SideBImagePanel)

    self.DrawImagePreview(panel=self.pnImagePreview_Setup)
    event.Skip()
    return

  def SetXSize(self, event):
    value = self.spXSize.GetValue()
    if (value > len(self.TopBorderA)):
      self.TopBorderA.append('connect')
      self.BottomBorderA.append('connect')
      self.TopBorderB.append('connect')
      self.BottomBorderB.append('connect')
    elif (value < len(self.TopBorderA)):
      self.TopBorderA.pop()
      self.BottomBorderA.pop()
      self.TopBorderB.pop()
      self.BottomBorderB.pop()
    self.DrawImagePanels(panelA=self.Setup_SideAImagePanel, panelB=self.Setup_SideBImagePanel)
    self.bUpdateTile.Enable(True)
    self.PromptSave = True
    return

  def SetYSize(self, event):
    value = self.spYSize.GetValue()
    if (value > len(self.RightBorderA)):
      self.RightBorderA.append('connect')
      self.LeftBorderA.append('connect')
      self.RightBorderB.append('connect')
      self.LeftBorderB.append('connect')
    elif (value < len(self.RightBorderA)):
      self.RightBorderA.pop()
      self.LeftBorderA.pop()
      self.RightBorderB.pop()
      self.LeftBorderB.pop()
    self.DrawImagePanels(panelA=self.Setup_SideAImagePanel, panelB=self.Setup_SideBImagePanel)
    self.bUpdateTile.Enable(True)
    self.PromptSave = True
    return
  
  def SetTileQuantity(self, event):
    self.bUpdateTile.Enable(True)
    return

  def SetTilenameA(self, event):
    self.bUpdateTile.Enable(True)
    return
  
  def SetTilenameB(self, event):
    self.bUpdateTile.Enable(True)
    return
    

  def AddCurrentTile(self, event):
    if (self.SideAImageIndex == None):
      wx.MessageBox("Please select an image for Side A")
      return

    newtile = Tile()
    next_index = len(self.Tilelist)+1
    newtile.tileID = next_index
    if (self.TileNameA.GetValue() == ""):
      newtile.tilenameA = self.ImageList[self.SideAImageIndex]
    else:
      newtile.tilenameA = self.TileNameA.GetValue()

    newtile.actualXsize = int(self.spXSize.GetValue())
    newtile.actualYsize = int(self.spYSize.GetValue())
    newtile.count = int(self.spTileCount.GetValue())
    newtile.imagenameA = self.ImageList[self.SideAImageIndex]
    newtile.filenameA = self.ImageListPaths[self.SideAImageIndex]
    newtile.taglist = self.taglist
    newtile.TopEdgeA = self.TopBorderA
    newtile.BottomEdgeA = self.BottomBorderA
    newtile.RightEdgeA = self.RightBorderA
    newtile.LeftEdgeA = self.LeftBorderA

    if (self.SideBImageIndex != None):
      if (self.TileNameB == ""):
        newtile.tilenameB = self.ImageList[self.SideBImageIndex]
      else:
        newtile.tilenameB = None
      newtile.imagenameB = self.ImageList[self.SideBImageIndex]
      newtile.filenameB = self.ImageListPaths[self.SideBImageIndex]
      newtile.TopEdgeB = self.TopBorderB
      newtile.BottomEdgeB = self.BottomBorderB
      newtile.RightEdgeB = self.RightBorderB
      newtile.LeftEdgeB = self.LeftBorderB
    else:
      newtile.imagenameB = None
      newtile.filenameB = None
    self.Tilelist.append(newtile)
    self.UpdateTilesetBox()
    self.bSaveTileset.Enable(True)
    self.bUpdateTile.Enable(False)
    self.PromptSave = True
    return

  def UpdateTilesetBox(self):
    tilenames = []
    for tile in self.Tilelist:
      string = tile.tilenameA
      if (tile.tilenameB):
        string += (" / " + tile.tilenameB)
      else:
        string += " / No side B"
      tilenames.append(string)
    self.lbTileset_TilesetBox.Set(tilenames)
    self.lbSetup_TilesetBox.Set(tilenames)
    if (self.TilesetFilename):
      self.bSaveTileset.Enable(True)
    self.PromptSave = True
    return

  def ZoomInPanelSideA(self, event):
    self.ScaleA += 0.50
    if (event.GetId() == PyMapperDialogs.Setup_ZoomInA):
      self.DrawImagePanels(panelA=self.Setup_SideAImagePanel, panelB=self.Setup_SideBImagePanel)
    else:
      self.DrawImagePanels(panelA=self.Tileset_SideAImagePanel, panelB=self.Tileset_SideBImagePanel)
    return

  def ZoomOutPanelSideA(self, event):
    self.ScaleA -= 0.50
    if (self.ScaleA < 1.0):
      self.ScaleA = 1.0
    if (event.GetId() == PyMapperDialogs.Setup_ZoomOutA):
      self.DrawImagePanels(panelA=self.Setup_SideAImagePanel, panelB=self.Setup_SideBImagePanel)
    else:
      self.DrawImagePanels(panelA=self.Tileset_SideAImagePanel, panelB=self.Tileset_SideBImagePanel)
    return

  def ZoomInPanelSideB(self, event):
    self.ScaleB += 0.50
    if (event.GetId() == PyMapperDialogs.Setup_ZoomInB):
      self.DrawImagePanels(panelA=self.Setup_SideAImagePanel, panelB=self.Setup_SideBImagePanel)
    else:
      self.DrawImagePanels(panelA=self.Tileset_SideAImagePanel, panelB=self.Tileset_SideBImagePanel)
    return

  def ZoomOutPanelSideB(self, event):
    self.ScaleB -= 0.50
    if (self.ScaleB < 1.0):
      self.ScaleB = 1.0
    if (event.GetId() == PyMapperDialogs.Setup_ZoomOutB):
      self.DrawImagePanels(panelA=self.Setup_SideAImagePanel, panelB=self.Setup_SideBImagePanel)
    else:
      self.DrawImagePanels(panelA=self.Tileset_SideAImagePanel, panelB=self.Tileset_SideBImagePanel)
    return

  def OnTilesetBox(self, event):
    if (event.GetId() == PyMapperDialogs.Tileset_TilesetBox):
      TilesetBox = self.lbTileset_TilesetBox
      ImageListBox = None
      self.bSetup_RemoveTile.Enable(True)
      panelA=self.Tileset_SideAImagePanel
      panelB=self.Tileset_SideBImagePanel
    elif (event.GetId() == PyMapperDialogs.Setup_TilesetBox):
      TilesetBox = self.lbSetup_TilesetBox
      ImageListBox = self.ImageListBox_Setup
      self.bUpdateTile.Enable(False)
      self.bSetup_RemoveTile.Enable(True)
      panelA = self.Setup_SideAImagePanel
      panelB = self.Setup_SideBImagePanel
    
    self.ScaleA = 1.0
    self.ScaleB = 1.0
    self.TopBorderA = []
    self.BottomBorderA = []
    self.LeftBorderA = []
    self.RightBorderA = []
    self.TopBorderB = []
    self.BottomBorderB = []
    self.LeftBorderB = []
    self.RightBorderB = []
    
    selection = TilesetBox.GetSelection()
    tile = self.Tilelist[selection]
    self.TileNameA.SetValue(tile.tilenameA)
    if (tile.tilenameB):
      self.TileNameB.SetValue(tile.tilenameB)
    else:
      self.TileNameB.SetValue("")
    self.spXSize.SetValue(tile.actualXsize)
    self.spYSize.SetValue(tile.actualYsize)
    self.spTileCount.SetValue(tile.count)
    
    index = 0
    foundA = False
    foundB = False
    for img in self.ImageListPaths:
      if (tile.filenameA == img):
        self.SideAImageIndex = index
        if (ImageListBox):
          ImageListBox.SetSelection(index)
        foundA = True
        self.bRemoveImageSideA.Enable(True)
      if (tile.filenameB == img):
        self.SideBImageIndex = index
        if (ImageListBox):
          ImageListBox.SetSelection(index)
        foundB = True
        self.bRemoveImageSideB.Enable(True)
      if (foundA and foundB):
        break
      index += 1
    

    if (tile.filenameA == None):
      self.SideAImageIndex = None
    if (tile.filenameB == None):
      self.SideBImageIndex = None
    
    self.SetImageListBox()
    self.PreviewImage = None
    self.DrawImagePreview(panel=self.pnImagePreview_Setup)

    if (tile.random_defA):
      self.bSetWallsSideA.SetValue(True)
      self.TopBorderA = tile.TopEdgeA
      self.BottomBorderA = tile.BottomEdgeA
      self.LeftBorderA = tile.LeftEdgeA
      self.RightBorderA = tile.RightEdgeA
    else:
      self.bSetWallsSideA.SetValue(False)

    if (tile.random_defB):
      self.bSetWallsSideB.SetValue(True)
      self.TopBorderB = tile.TopEdgeB
      self.BottomBorderB = tile.BottomEdgeB
      self.LeftBorderB = tile.LeftEdgeB
      self.RightBorderB = tile.RightEdgeB
    else:
      self.bSetWallsSideB.SetValue(False)
    
    self.DrawImagePanels(panelA=self.Setup_SideAImagePanel, panelB=self.Setup_SideBImagePanel)
    self.DrawImagePanels(panelA=self.Tileset_SideAImagePanel, panelB=self.Tileset_SideBImagePanel)
    return

  def OnClearTileSelection(self, event):
    if (event.GetId() == self.bTileset_ClearTileSelection):
      self.lbTileset_TilesetBox.SetSelection(wx.NOT_FOUND)
      self.bTileset_ClearTileSelection.Enable(False)
      self.bTileset_RemoveTile.Enable(False)
    return
  
  def OnRemoveTile(self, event):
    self.bUpdateTile.Enable(False)
    self.bSetup_RemoveTile.Enable(False)
    self.PromptSave = True
    index = self.lbSetup_TilesetBox.GetSelection()
    rm = self.Tilelist[index]
    self.Tilelist.remove(rm)
    self.UpdateTilesetBox()
    return

  def OnUpdateTile(self, event):
    select = self.lbSetup_TilesetBox.GetSelection()
    if (select == wx.NOT_FOUND):
      return
    tile = Tile()
    tile = self.Tilelist[select]
    
    if (self.SideAImageIndex == None):
      #must have a side A image
      wx.MessageBox("Please select an image for Side A")
      return
    
    if (self.TileNameA.GetValue() != ""):
      tile.tilenameA = self.TileNameA.GetValue()
    if (self.TileNameB.GetValue() == ""):
      tile.tilenameB = self.TileNameB.GetValue()
    else:
      tile.tilenameB = None
    tile.actualXsize = int(self.spXSize.GetValue())
    tile.actualYsize = int(self.spYSize.GetValue())
    tile.count = int(self.spTileCount.GetValue())
    tile.taglist = self.taglist
    
    if (self.SideAImageIndex):
      tile.imagenameA = self.ImageList[self.SideAImageIndex]
      tile.filenameA = self.ImageListPaths[self.SideAImageIndex]
    if (self.SideBImageIndex):
      tile.imagenameB = self.ImageList[self.SideBImageIndex]
      tile.filenameB = self.ImageListPaths[self.SideBImageIndex]
    else:
      tile.imagenameB = None
      tile.filenameB = None

    if (self.bSetWallsSideA.GetValue()):
      tile.random_defA = True
      tile.TopEdgeA = self.TopBorderA
      tile.BottomEdgeA = self.BottomBorderA
      tile.RightEdgeA = self.RightBorderA
      tile.LeftEdgeA = self.LeftBorderA
    if (self.bSetWallsSideB.GetValue()):
      tile.random_defB = True
      tile.TopEdgeB = self.TopBorderB
      tile.BottomEdgeB = self.BottomBorderB
      tile.RightEdgeB = self.RightBorderB
      tile.LeftEdgeB = self.LeftBorderB

    self.UpdateTilesetBox()
    #self.bUpdateTile.Enable(False)
    self.PromptSave = True
    return
  
  def TilesetNameChanged(self, event):
    if (self.txTilesetName.GetValue() != ""):
      self.txTilesetName.SetBackgroundColour(wx.WHITE)
    else:
      self.txTilesetName.SetBackgroundColour(wx.RED)
    return
  
  def TilesetIDChanged(self, event):
    if (self.txTilesetID.GetValue() != ""):
      self.txTilesetID.SetBackgroundColour(wx.WHITE)
    else:
      self.txTilesetID.SetBackgroundColour(wx.RED)
    return

  def SaveTileset(self, event=None):
    self.TilesetOKtoSave = True
    if (self.Tilelist == []):
      wx.MessageBox("Please create at least one tile to add to the tileset")
      self.lbTileset_TilesetBox.SetBackgroundColour(wx.RED)
      self.TilesetOKtoSave = False
    if (self.txTilesetID.GetValue() == ""):
      wx.MessageBox("Please enter a folder name for the tileset ID")
      self.txTilesetID.SetBackgroundColour(wx.RED)
      self.TilesetOKtoSave = False
    if (self.txTilesetName.GetValue() == ""):
      wx.MessageBox("Please enter a filename for the tileset name")
      self.txTilesetName.SetBackgroundColour(wx.RED)
      self.TilesetOKtoSave = False
    
    if (not self.TilesetOKtoSave):
      self.Refresh()
      return
    
    #check to see if the proper folder is available in the tiles folder.
    folderPath = os.path.join(gv.tiles_directory,self.txTilesetID.GetValue())
    if (not os.access(folderPath, os.F_OK)):
      folder = self.txTilesetID.GetValue()
      wx.MessageBox("Creating %s folder in tiles folder" % (folder))
      logging.info("Tileset Editor: creating subfolder")
      try:
        os.mkdir(folderPath)
      except OSError:
        logging.error("TilesetEditor: Could not create subfolder in /tiles/ folder")
        wx.MessageBox("Could not create folder.")
    
    self.TilesetFilename = self.txTilesetName.GetValue() + ".set"
    
    self.TilesetFilenamePath = os.path.join(folderPath,self.TilesetFilename)
    
    self.TilesetID = self.txTilesetID.GetValue()
    self.NumSets = self.spNumSets.GetValue()
    self.stCurrentTilesetName.SetLabel(self.TilesetFilenamePath)
    
    #dlg = wx.FileDialog(self, message="Save tileset file", defaultDir=os.getcwd(), defaultFile=filename, wildcard=tilesets_wildcard, style=wx.SAVE | wx.CHANGE_DIR)
    #if (dlg.ShowModal() == wx.ID_OK):
    #  filename = dlg.GetFilename() #GetPath()
    #  self.TilesetFilename = filename #self.txTilesetName.GetValue() + ".set"
    #  self.TilesetID = self.txTilesetID.GetValue()
    #  self.NumSets = self.spNumSets.GetValue()
    #  self.TilesetFilenamePath = dlg.GetPath() #os.path.join(self.TilesetPath, self.TilesetFilename)
    #  self.stCurrentTilesetName.SetLabel(self.TilesetFilenamePath)
    #else:
    #  dlg.Destroy()
    #  return
    #dlg.Destroy()

    try:
      savefile = open(self.TilesetFilenamePath, 'w')
    except IOError:
      logging.critical("TilesetEditorDialogCore::SaveTileset: Could not open for write operation %s",filename)
      wx.MessageBox("Could not open %s for writing" % (filename))
      return

    savefile.write("# Tileset file generated by PyMapper Tile import utility \n")
    savefile.write("TILESET\n")
    savefile.write("VERSION %f\n" % gv.TilesetSpecificationVersion)
    savefile.write("NAME "+ str(self.txTilesetName.GetValue()) +" \n")
    savefile.write("SET_ID "+str(self.txTilesetID.GetValue())+ " \n")
    savefile.write("NUM_SETS "+str(self.spNumSets.GetValue())+" \n")
    for tile in self.Tilelist:
      try:
        destPath = os.path.join(folderPath, tile.imagenameA)
        shutil.copy(tile.filenameA, destPath)
      except:
        logging.error("Could not copy file %s" % (tile.imagenameA))
      if (tile.imagenameB):
        try:
          destPath = os.path.join(folderPath,tile.imagenameB)
          shutil.copy(tile.filenameB, destPath)
        except:
          logging.error("Could not copy file %s" % (tile.imagenameB))
        
      
      savefile.write("TILE "+str(tile.tileID)+" \n")
      if (not self.TilesetLoaded):  # images came from new images
        savefile.write("IMAGE_A tiles/"+str(self.txTilesetID.GetValue())+"/"+str(tile.imagenameA)+ " \n")
        if (tile.imagenameB):
          savefile.write("IMAGE_B tiles/"+str(self.txTilesetID.GetValue())+"/"+str(tile.imagenameB)+ " \n")
      else:  #images came from a loaded tileset
        savefile.write("IMAGE_A "+ str(tile.imagenameA)+ " \n")
        if (tile.imagenameB):
          savefile.write("IMAGE_B "+str(tile.imagenameB)+ " \n")
          
      savefile.write("XSIZE "+str(tile.actualXsize) + " \n")
      savefile.write("YSIZE "+str(tile.actualYsize) + " \n")

      if (tile.taglist):
        savefile.write("FILTER_TAGS ")
        for tag in tile.taglist:
          savefile.write(str(tag)+ " ")
        savefile.write("\n")
      savefile.write("TILE_COUNT "+str(tile.count) + " \n")
      savefile.write("TILE_NAME_A "+str(tile.tilenameA) + " \n")
      if (tile.tilenameB):
        savefile.write("TILE_NAME_B "+str(tile.tilenameB) + " \n")
      if (tile.random_defA):
        savefile.write("BOTTOM_EDGE_A\n")
        for i in tile.BottomEdgeA:
          savefile.write(i+" ")
        savefile.write("\n")
        savefile.write("TOP_EDGE_A\n")
        for i in tile.TopEdgeA:
          savefile.write(i+" ")
        savefile.write("\n")
        savefile.write("LEFT_EDGE_A\n")
        for i in tile.LeftEdgeA:
          savefile.write(i+" ")
        savefile.write("\n")
        savefile.write("RIGHT_EDGE_A\n")
        for i in tile.RightEdgeA:
          savefile.write(i+" ")
        savefile.write("\n")
      if (tile.random_defB):
        savefile.write("BOTTOM_EDGE_B\n")
        for i in tile.BottomEdgeB:
          savefile.write(i+" ")
        savefile.write("\n")
        savefile.write("TOP_EDGE_B\n")
        for i in tile.TopEdgeB:
          savefile.write(i+" ")
        savefile.write("\n")
        savefile.write("LEFT_EDGE_B\n")
        for i in tile.LeftEdgeB:
          savefile.write(i+" ")
        savefile.write("\n")
        savefile.write("RIGHT_EDGE_B\n")
        for i in tile.RightEdgeB:
          savefile.write(i+" ")
        savefile.write("\n")

      savefile.write("ENDTILE \n")
    savefile.write("END\n")
    savefile.close()
    self.bSaveTileset.Enable(False)
    self.PromptSave = False
    return

  def AddFilterTags(self, event):
    #add the correct tile to the fcn call
    select = self.ImageListBox_Setup.GetSelections()
    tile = self.Tilelist[select[0]]
    dlg = FilterTagsDialogCore(self, True, singletile=tile)
    result = dlg.ShowModal()
    if (result):
      self.taglist = []
    else:
      dlg.Destroy()
      return
    if (dlg.DGRuneTag.GetValue()):
      self.taglist.append('DGRune')
    if (dlg.DGDoorTag.GetValue()):
      self.taglist.append('DGDoor')
    if (dlg.DGLadderTag.GetValue()):
      self.taglist.append('DGLadder')
    if (dlg.DGLargeRoomTag.GetValue()):
      self.taglist.append('DGLargeRoom')
    if (dlg.DGSmallRoomTag.GetValue()):
      self.taglist.append('DGSmallRoom')
    if (dlg.DGHallwayTag.GetValue()):
      self.taglist.append('DGHallway')
    if (dlg.DGTowerSectionTag.GetValue()):
      self.taglist.append('DGTower')
    if (dlg.DGParapetWallTag.GetValue()):
      self.taglist.append('DGParapet')
    if (dlg.DGTrapTag.GetValue()):
      self.taglist.append('DGTrap')
    if (dlg.DGStairsTag.GetValue()):
      self.taglist.append('DGStairs')
    if (dlg.DGDecorationTag.GetValue()):
      self.taglist.append('DGDecoration')
    if (dlg.DGTransitionTag.GetValue()):
      self.taglist.append('DGTransition')
    if (dlg.CVPassageTag.GetValue()):
      self.taglist.append('CVPassage')
    if (dlg.CVEndTag.GetValue()):
      self.taglist.append('CVDeadEnd')
    if (dlg.CVLargeCavernTag.GetValue()):
      self.taglist.append('CVLargeCavern')
    if (dlg.CVPartialCavernTag.GetValue()):
      self.taglist.append('CVPartialCavern')
    if (dlg.CVDecorationTag.GetValue()):
      self.taglist.append('CVDecoration')
    if (dlg.CVTransitionTag.GetValue()):
      self.taglist.append('CVTransition')
    if (dlg.WLPondTag.GetValue()):
      self.taglist.append('WLPond')
    if (dlg.WLTreesTag.GetValue()):
      self.taglist.append('WLTrees')
    if (dlg.WLRoadTag.GetValue()):
      self.taglist.append('WLRoad')
    if (dlg.WLStreamTag.GetValue()):
      self.taglist.append('WLStream')
    if (dlg.WLPathTag.GetValue()):
      self.taglist.append('WLPath')
    if (dlg.WLRuinsTag.GetValue()):
      self.taglist.append('WLRuins')
    if (dlg.WLDecorationTag.GetValue()):
      self.taglist.append('WLDecoration')
    if (dlg.WLTransitionTag.GetValue()):
      self.taglist.append('WLTransition')
    if (dlg.TNTowerTag.GetValue()):
      self.taglist.append('TNTower')
    if (dlg.TNTownTag.GetValue()):
      self.taglist.append('TNTown')
    if (dlg.TNSmallBuildingTag.GetValue()):
      self.taglist.append('TNSmallBuilding')
    if (dlg.TNLargeBuildingTag.GetValue()):
      self.taglist.append('TNLargeBuilding')
    if (dlg.TNSewerTag.GetValue()):
      self.taglist.append('TNSewer')
    if (dlg.TNDecorationTag.GetValue()):
      self.taglist.append('TNDecoration')
    if (dlg.TNLadderTag.GetValue()):
      self.taglist.append('TNLadder')
    if (dlg.TNTransitionTag.GetValue()):
      self.taglist.append('TNTransition')
    if (dlg.TNShipTag.GetValue()):
      self.taglist.append('TNShip')
    self.PromptSave = True
    dlg.Destroy()
    return
  
  def OnNewTileset(self, event):
    if (self.Tilelist):
      dlg = wx.MessageDialog(self, "Clear existing tile data?", "Clear Tileset?", wx.OK | wx.CANCEL | wx.ICON_QUESTION)
      result = dlg.ShowModal()
      if (result == wx.OK):  #clear the tileset loaded in memory
        dlg.Destroy()
        self.Tilelist = []
        self.lbTileset_TilesetBox.Clear()
        self.lbSetup_TilesetBox.Clear()
        self.txTilesetID.SetLabel("")
        self.txTilesetName.SetLabel("")
        self.spNumSets.SetValue(1)
        self.NumSets = 1
        self.ScaleA = 1.0
        self.ScaleB = 1.0
        self.TilesetLoaded = False
        self.ImageListBox_Setup.Clear()
        self.ImageListPaths = []
        self.SideAImageIndex = None
        self.SideBImageIndex = None
        self.SideAImage = None
        self.SideBImage = None
        self.taglist = []
        self.TilesetFilename = None
        self.TilesetPath = None
        self.TilesetFilenamePath = None
        self.TilesetID = None
        self.NumSets = None
        self.ImageList = []
        self.ImageListPaths = []
        
        self.TopBorderA = ['connect']  #describes the type of edge, either 'wall' or 'connect' from left to right
        self.BottomBorderA = ['connect']
        self.RightBorderA = ['connect']  #from top to bottom
        self.LeftBorderA = ['connect']
        self.TopBorderB = ['connect']  #describes the type of edge, either 'wall' or 'connect' from left to right
        self.BottomBorderB = ['connect']
        self.RightBorderB = ['connect']  #from top to bottom
        self.LeftBorderB = ['connect']
        
      elif (result == wx.CANCEL):
        dlg.Destroy()
        return
      
    NameDlg = wx.TextEntryDialog(self, "Enter name for new tileset", "New Tileset Name", "New Tileset")
    result = NameDlg.ShowModal()
    if (result == wx.CANCEL):
      NameDlg.Destroy()
      return
    
    ID_dlg = wx.TextEntryDialog(self, "Enter ID for new tileset", "New Tileset ID", "SetID")
    result = ID_dlg.ShowModal()
    if (result == wx.CANCEL):
      ID_dlg.Destroy()
      return
    self.txTilesetID.SetValue(ID_dlg.GetValue())
    self.txTilesetName.SetValue(NameDlg.GetValue())
    
    NameDlg.Destroy()
    ID_dlg.Destroy()
    
    result = self.AddImages()
    
    self.stCurrentTilesetName.SetLabel("Tileset not saved")
    self.stCurrentTilesetName.SetToolTipString("Save tileset before exiting")
    self.TilesetOKtoSave = False
    
    self.DrawImagePanels(panelA=self.Tileset_SideAImagePanel, panelB=self.Tileset_SideBImagePanel)
    
    self.UpdateTilesetBox()
    self.SetImageListBox()
    return
  
  def LoadTileset(self, event):
    if (self.Tilelist):
      dlg = wx.MessageDialog(self, "There is an existing tileset already loaded.  Should I clear the tiles before loading another tileset?", "Clear Tileset?", wx.YES_NO | wx.CANCEL | wx.ICON_QUESTION)
      result = dlg.ShowModal()
      if (result == wx.YES):  #clear the tileset loaded in memory
        dlg.Destroy()
        self.Tilelist = []
      elif (result == wx.CANCEL):
        dlg.Destroy()
        return

    dlg = wx.FileDialog(self, message="Choose tileset file", defaultDir=os.getcwd(),
                        defaultFile="", wildcard=tilesets_wildcard,
                        style=wx.OPEN | wx.CHANGE_DIR)
    if (dlg.ShowModal() == wx.ID_OK):
      self.bSetWallsSideA.SetValue(False)
      self.bSetWallsSideB.SetValue(False)
      try:
        filename = dlg.GetPath()
        setfile = open(filename, 'r')
      except IOError:
        logging.critical("TilesetEditorDialogCore::LoadTileset: Could not open Tileset %s",filename)
        return False
      self.stCurrentTilesetName.SetLabel(filename)
      self.stCurrentTilesetName.SetToolTipString(filename)
      header = True
      line = setfile.readline()
      line = line.rstrip('\n\r')
      info = line.split()
      if (info == []):
        logging.critical("TilesetEditorDialogCore::LoadTileset: Zero length tileset file %s",filename)
        return False
      while (header == True):
        if (info[0] == '#'):
          #reading comment lines
          line = setfile.readline()
          info = line.split()
        elif (info[0] != '#'):
          header = False
      if (info[0] != 'TILESET'):
        '''Not a tileset file'''
        logging.critical("TilesetEditorDialogCore::LoadTileset:  Invalid tileset file format %s", filename)
        return False
      else:
        read_file = True
        newtile = Tile()
        tileset = TileSet()
        while (read_file == True):
          line = setfile.readline()
          line = line.rstrip('\n\r')
          info = line.split()
          if (info == []):
            #read an empty line, continue on to the next line
            pass
          elif (info[0] == 'SET_ID'):
            self.TilesetID = info[1]
            newtile.tilesetID = info[1]
            self.txTilesetID.SetValue(str(self.TilesetID))
          elif ((info[0] == '#') or (info[0] == [])):
            #comment line, or an empty line, skip reading
            continue
          elif (info[0] == 'NAME'):
            info.pop(0)
            tileset.tilenameA = info[0]
            tileset.tilenameB = info[0]
            info.pop(0)
            while (len(info) > 0):
              tileset.tilenameA += " "
              tileset.tilenameA += info[0]
              tileset.tilenameB += " "
              tileset.tilenameB += info[0]
              info.pop(0)
            self.txTilesetName.SetValue(str(tileset.tilenameA))
          elif (info[0] == 'NUM_SETS'):
            self.NumSets = int(info[1])
            self.spNumSets.SetValue(int(self.NumSets))
          elif (info[0] == "TILE"):
            newtile.tileID = int(info[1])
            read_tile = True
            while (read_tile == True):
              line = setfile.readline()
              info = line.split()
              if info[0] == 'IMAGE_A':
                #the filename may have spaces, so need to join all the elements
                name = ""
                count = 1
                for i in info:
                  if i == info[0]:
                    continue
                  elif i == info[1]:
                    name = i
                  else:
                    name = name + " " + i
                self.ImageList.append(name)
                newtile.imagenameA = name
                if (tilesetVersion == None):
                  #tilesets saved previous to tileset version 2.0 (pymapper version 9.4) include a leading \ on the pathname
                  #this results in the incorrect path join (assumes an absolute path)
                  name = name.lstrip("\\")  #in case of the win32 version .set files
                  name = name.lstrip("/")   #in case of the mac version .set files
                newtile.filenameA = os.path.join(gv.root_directory,name)
                newtile.filenameA = os.path.normpath(newtile.filenameA)
                self.ImageListPaths.append(newtile.filenameA)
                newtile.sideA = wx.Image(newtile.filenameA, wx.BITMAP_TYPE_ANY)
                if (not newtile.sideA.IsOk()):
                  logging.critical("TilesetEditorDialogCore::LoadTileset:  Could not open %s",newtile.filenameA)
                  newtile.sideA = app.ImageNotFound
              elif info[0] == 'IMAGE_B':
                name = ""
                count = 1
                for i in info:
                  if i == info[0]:
                    continue
                  elif i == info[1]:
                    name = i
                  else:
                    name = name + " " + i
                newtile.imagenameB = name
                if (tilesetVersion == None):
                  #tilesets saved previous to tileset version 2.0 (pymapper version 9.4) include a leading \ on the pathname
                  #this results in the incorrect path join (assumes an absolute path)
                  name = name.lstrip("\\")  #in case of the win32 version .set files
                  name = name.lstrip("/")   #in case of the mac version .set files
                newtile.filenameB = os.path.join(gv.root_directory, name)
                newtile.filenameA = os.path.normpath(newtile.filenameB)
                self.ImageList.append(name)
                self.ImageListPaths.append(newtile.filenameB)
                newtile.sideB = wx.Image(newtile.filenameB, wx.BITMAP_TYPE_ANY)
                if (not newtile.sideB.IsOk()):
                  logging.critical("TilesetEditorDialogCore::LoadTileset:  Could not open %s",newtile.filenameB)
                  newtile.sideB = app.ImageNotFound
                  #continue reading tile
              elif info[0] == 'XSIZE':
                newtile.actualXsize = int(info[1])
              elif info[0] == 'YSIZE':
                newtile.actualYsize = int(info[1])
              elif (info[0] == 'RANDOM_DUNGEON_TAGS'):
                info.pop(0)
                newtile.random_def = info
              elif (info[0] == 'FILTER_TAGS'):
                info.pop(0)
                while (len(info) > 0):
                  newtile.taglist.append(str(info[0]))
                  info.pop(0)
              elif info[0] == 'ROTATION':
                newtile.rotation = int(info[1])
              elif info[0] == 'TILE_COUNT':
                newtile.count = int(info[1])
              elif (info[0] == 'TILE_NAME'):
                info.pop(0)
                newtile.tilenameA = info[0]
                newtile.tilenameB = info[0]
                info.pop(0)
                while (len(info) > 0):
                  newtile.tilenameA += " "
                  newtile.tilenameA += info[0]
                  newtile.tilenameB += " "
                  newtile.tilenameB += info[0]
                  info.pop(0)
              elif (info[0] == 'TILE_NAME_A'):
                info.pop(0)
                newtile.tilenameA = info[0]
                info.pop(0)
                while (len(info) > 0):
                  newtile.tilenameA += " "
                  newtile.tilenameA += info[0]
                  info.pop(0)
              elif (info[0] == 'TILE_NAME_B'):
                info.pop(0)
                newtile.tilenameB = info[0]
                info.pop(0)
                while (len(info) > 0):
                  newtile.tilenameB += " "
                  newtile.tilenameB += info[0]
                  info.pop(0)
              elif (info[0] == 'TOP_EDGE_A'):
                newtile.random_defA = True
                newtile.TopEdgeA = []
                line = setfile.readline()
                newtile.TopEdgeA = line.split()
              elif (info[0] == 'BOTTOM_EDGE_A'):
                newtile.BottomEdgeA = []
                line = setfile.readline()
                newtile.BottomEdgeA = line.split()
              elif (info[0] == 'RIGHT_EDGE_A'):
                newtile.RightEdgeA = []
                line = setfile.readline()
                newtile.RightEdgeA = line.split()
              elif (info[0] == 'LEFT_EDGE_A'):
                newtile.LeftEdgeA = []
                line = setfile.readline()
                newtile.LeftEdgeA = line.split()
              elif (info[0] == 'TOP_EDGE_B'):
                newtile.random_defB = True
                newtile.TopEdgeB = []
                line = setfile.readline()
                newtile.TopEdgeB = line.split()
              elif (info[0] == 'BOTTOM_EDGE_B'):
                newtile.BottomEdgeB = []
                line = setfile.readline()
                newtile.BottomEdgeB = line.split()
              elif (info[0] == 'RIGHT_EDGE_B'):
                newtile.RightEdgeB = []
                line = setfile.readline()
                newtile.RightEdgeB = line.split()
              elif (info[0] == 'LEFT_EDGE_B'):
                newtile.LeftEdgeB = []
                line = setfile.readline()
                newtile.LeftEdgeB = line.split()
              elif info[0] == 'ENDTILE':
                if (newtile.tilenameA == None):
                  newtile.tilenameA = "Undefined Name A"
                if (newtile.tilenameB == None):
                  newtile.tilenameB = "Undefined Name B"
                read_tile = False
                newtile.tilesetID = tileset.SetID
                #set the rest of the params
                newtile.shown = True
                newtile.text = None
                newtile.mapdisplay = None # No tile set to the MapPanel yet
                newtile.tiledisplay = newtile.sideA
                newtile.showingBside = False
                newtile.copies = (tileset.copies * newtile.count)  #total num available
                self.Tilelist.append(newtile)
                newtile = Tile()
          elif (info[0] == "END"):
            read_file = False
          else:
            setfile.close()
            logging.error("TilesetEditorDialogCore::LoadTileset:  Reached end of tileset file without reading END tag")
            return False
      setfile.close()
      self.TilesetLoaded = True
      self.UpdateTilesetBox()
      self.SetImageListBox()
      self.bSaveTileset.Enable(True)
      self.PromptSave = False
    return

  def OnOK(self, event):
    """Must make checks to see if a valid tileset can be saved.  Provide error message if set is not valid.
    """
    if (self.PromptSave):
      result = wx.MessageDialog(self, "Save current tileset? (Yes to save, No to exit, Cancel to return to editing)", "Save changes to tileset?", wx.ICON_QUESTION | wx.YES_NO | wx.CANCEL).ShowModal()
      if (result == wx.ID_YES):
        self.SaveTileset()
      elif (result == wx.ID_CANCEL):
        return
    self.EndModal(True)
    return

  def OnCancel(self, event):
    self.EndModal(False)
    return


class ProgramOptionsDialogCore(PyMapperDialogs.ProgramOptionsDialogBase):
  def __init__(self, parent):
    olddir = os.getcwd()
    os.chdir(gv.root_directory)  #this is necessary so that bitmap paths are read by the dialog code correctly    
    PyMapperDialogs.ProgramOptionsDialogBase.__init__(self, parent)
    os.chdir(olddir)
    self.Center()
    #set bindings for Grid Options
    self.GridLineStyleBitmap.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
    self.ShowGridCoordinates.SetValue(gv.ShowGridCoordinates)
    self.cbShowGrid.SetValue(gv.DisplayGrid)
    self.GridLineStylePen = gv.GridPen
    self.GridLineStyle = gv.GridPenStyle
    self.cpkGridColor.SetColour(gv.GridColor)
    self.spGridLineWidth.SetValue(gv.GridPenWidth)
    self.cbDrawGridOnTop.SetValue(gv.DrawGridOnTop)
    self.cbOpenToLastFolder.SetValue(gv.ChangeDefaultFolder)

    self.cpkIntermediateGuideColor.SetColour(gv.IntermediateGridColor)
    self.cbDrawIntermediateLines.SetValue(gv.ShowIntermediateGridLines)
    self.spGuideInterval.SetValue(gv.IntermediateGridLinesInterval)
    self.cpkMapFogColor.SetColour(gv.MapFogColor)

    #set bindings for Program Options
    self.AutoSaveTimer.SetValue(gv.AutoSaveInterval/60)
    if (gv.backup_directory):
      self.stAutoSavePath.SetLabel(gv.backup_directory)
    else:
      self.stAutoSavePath.SetLabel("No folder set")

    self.cbSaveIniFile.SetValue(gv.SaveIniFile)
    
    self.cbAutoSave.SetValue(gv.AutoSave)
    self.spGridScale.SetValue(gv.GridScale)
    self.AutoSave()  #dim/undim the appropriate controls

    #set bindings for Background Options
    self.cpkOutlineColor.SetColour(gv.OutlineTilesColor)
    self.BackgroundOpacityValue.SetValue(100*gv.BackgroundOpacity)
    self.BackgroundOpacitySpin.SetValue(100*gv.BackgroundOpacity)
    self.pnBackgroundOpacity.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
    self.cpkBackgroundColor.SetColour(gv.MapPanelBackgroundColor)
    self.cbShowBackground.SetValue(gv.DisplayBackground)
    self.cbOutlineOnHover.SetValue(gv.OutlineOnHover)
    self.OpacityBitmap = wx.Image(os.path.join(gv.artwork_directory,"opacity.png"), wx.BITMAP_TYPE_PNG)

    self.ChangeBackgroundDisplay()  #update the dim/undim

    #set bindings for Tile Options
    self.TileOpacityValue.SetValue(100*gv.TileOpacity)
    self.TileOpacitySpin.SetValue(100*gv.TileOpacity)
    self.pnTileOpacity.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
    self.HoverTimeInterval.SetValue(gv.hover_interval)
    self.rbDualDisplayTileWindow.SetValue(gv.DualDisplayTileWindow)
    self.rbUseHoverOption.SetValue(gv.DisplayOnHover)
    self.cbResetTileStats.SetValue(gv.ResetTileStatistics)
    self.HoverOption()

    self.cbReverseMouseWheel.SetValue(gv.ReverseMouseWheel)

    self.ShowGridCheckbox()
    
    #Set options for SRD files
    self.cbReadSRDFiles.SetValue(gv.ReadSRDFileData)
    self.cbRead5EditionFiles.SetValue(gv.Read5EditionFileData)
    
    #set options for map icons
    self.cbHighlightIcons.SetValue(gv.HighlightIcons)
    self.cbDisplayIconInformation.SetValue(gv.DisplayIconInformation)
    self.cbSnapIconsToGrid.SetValue(gv.SnapIconToGrid)
    return

  def OnHelp(self, event):
    text = "Several program options can be changed through this dialog.\n\nFor Grid Options, the grid can be turned on or off, as well as changing the grid color and linetype.\nThe grid coordinates can be toggled on or off.  These coordinates provide a way to locate features on the map in a text description.\n\nBackground Options change the solid color of the map window, and also a background image, if one is loaded.  Changing the background opacity makes the image fade out as the value is reduced.\n\nProgram Options affect the automatic backup feature, and also the location where backup files are saved.  The settings can be saved everytime the program exits, if you choose.  Also, the d20 SRD can be loaded automatically, or turned off for manual loading.\n\nTile Panel options can change the display of one side, or both sides of the tile.  The reverse side can be displayed when the mouse hovers over the tile.\n"
    text += "The 'Icon Information' option displays an information box when you hover over an icon with associated player data assigned to it.\n"
    dlg = HelpDialog(self, text)
    dlg.ShowModal()
    return

  def HoverOption(self, event=None):
    if (self.rbUseHoverOption.GetValue()):
      self.HoverTimeInterval.Enable(True)
      self.stHoverText.Enable(True)
    else:
      self.HoverTimeInterval.Enable(False)
      self.stHoverText.Enable(False)

  def ChangeBackgroundDisplay(self, event=None):
    if (self.cbShowBackground.GetValue() == True):
      self.BackgroundOpacityValue.Enable(True)
      self.BackgroundOpacitySpin.Enable(True)
      self.stBackgroundPath.Enable(True)
      self.stBackground2.Enable(True)
      self.stBackground3.Enable(True)
    else:
      self.BackgroundOpacityValue.Enable(False)
      self.BackgroundOpacitySpin.Enable(False)
      self.stBackgroundPath.Enable(False)
      self.stBackground2.Enable(False)
      self.stBackground3.Enable(False)
    return

  def AutoSave(self, event=None):
    if (self.cbAutoSave.GetValue() == True):
      self.AutoSaveTimer.Enable(True)
      self.stAutoSavePath.Enable(True)
      self.bAutoSavePath.Enable(True)
      self.stAutoSaveText1.Enable(True)
      self.stAutoSavePath.Enable(True)
    else:
      self.AutoSaveTimer.Enable(False)
      self.stAutoSavePath.Enable(False)
      self.bAutoSavePath.Enable(False)
      self.stAutoSaveText1.Enable(False)
      self.stAutoSavePath.Enable(False)
    return

  def OKButton(self, event):
    self.EndModal(True)
    return

  def ShowGridCheckbox(self, event=None):
    if (self.cbShowGrid.GetValue()):
      self.cpkGridColor.Enable(True)
      self.bChangeGridLinestyle.Enable(True)
      self.spGridLineWidth.Enable(True)
    else:
      self.cpkGridColor.Enable(False)
      self.bChangeGridLinestyle.Enable(False)
      self.spGridLineWidth.Enable(False)
    return

  def CancelButton(self, event):
    self.EndModal(False)
    return

  def ChangeGridLineStyle(self, event):
    if (self.GridLineStyle == wx.SOLID):
      self.GridLineStyle = wx.DOT
      self.Refresh()
      return
    elif (self.GridLineStyle == wx.DOT):
      self.GridLineStyle = wx.LONG_DASH
      self.Refresh()
      return
    elif (self.GridLineStyle == wx.LONG_DASH):
      self.GridLineStyle = wx.DOT_DASH
      self.Refresh()
      return
    elif (self.GridLineStyle == wx.DOT_DASH):
      self.GridLineStyle = wx.CROSS_HATCH
      self.Refresh()
      return
    elif (self.GridLineStyle == wx.CROSS_HATCH):
      self.GridLineStyle = wx.SOLID
      self.Refresh()
      return

  def BackgroundOpacitySlider(self, event):
    self.BackgroundOpacitySpin.SetValue(self.BackgroundOpacityValue.GetValue())
    self.Refresh()
    return

  def ChangeGridLineWidth(self, event):
    self.Refresh()
    return

  def ChangeAutoSavePath(self, event):
    dlg = wx.DirDialog(self, "Choose a folder for backup files:", gv.backup_directory, style = wx.DD_DEFAULT_STYLE)
    if (dlg.ShowModal() == wx.ID_OK):
      gv.backup_directory = dlg.GetPath()
      self.stAutoSavePath.SetLabel(gv.backup_directory)
    return

  def BackgroundOpacitySpinValue(self, event):
    self.BackgroundOpacityValue.SetValue(self.BackgroundOpacitySpin.GetValue())
    self.Refresh()
    return

  def DrawTileOpacityBitmap(self):
    dc = wx.PaintDC(self.pnTileOpacity)
    dc.Clear()
    opacity = self.TileOpacityValue.GetValue()/100.0
    image = self.OpacityBitmap.AdjustChannels(1.0,1.0,1.0, opacity)
    bitmap = wx.BitmapFromImage(image)
    dc.DrawBitmap(bitmap,0,0,True)

  def DrawBackgroundOpacityBitmap(self):
    dc = wx.PaintDC(self.pnBackgroundOpacity)
    dc.Clear()
    opacity = self.BackgroundOpacityValue.GetValue()/100.0
    image = self.OpacityBitmap.AdjustChannels(1.0,1.0,1.0, opacity)
    bitmap = wx.BitmapFromImage(image)
    dc.DrawBitmap(bitmap,0,0,True)

  def TileOpacitySlider(self, event):
    self.TileOpacitySpin.SetValue(self.TileOpacityValue.GetValue())
    self.Refresh()
    return

  def TileOpacitySpinValue(self, event):
    self.TileOpacityValue.SetValue(self.TileOpacitySpin.GetValue())
    self.Refresh()
    pass

  def OnPaint(self, event):
    self.DrawLineStyleBitmap()
    self.DrawTileOpacityBitmap()
    self.DrawBackgroundOpacityBitmap()
    event.Skip()
    return

  def DrawLineStyleBitmap(self):
    #draw the linestyle bitmap
    dc = wx.PaintDC(self.GridLineStyleBitmap)
    whitepen = wx.Pen(wx.Colour(255,255,255))
    whitebrush = wx.Brush(wx.Colour(255,255,255))
    dc.SetPen(whitepen)
    dc.SetBrush(whitebrush)
    dc.DrawRectangle(0,0, 160, 30)
    width = self.spGridLineWidth.GetValue()
    self.GridLineStylePen.SetWidth(width)
    self.GridLineStylePen.SetStyle(self.GridLineStyle)
    self.GridLineStylePen.SetColour(self.cpkGridColor.GetColour())
    dc.SetPen(self.GridLineStylePen)
    dc.DrawLine(0,15, 160,15)
    return

class NewFileDialog(PyMapperDialogs.NewMapDialogBase):
  def __init__(self, parent):
    olddir = os.getcwd()
    os.chdir(gv.root_directory)
    PyMapperDialogs.NewMapDialogBase.__init__(self, parent)
    os.chdir(olddir)
    return

  def OKButton(self, event):
    self.EndModal(True)
    return

  def CancelButton(self, event):
    self.EndModal(False)
    return

class TileSet:
  def __init__(self):
    self.delete = False #queue for deletion
    self.loaded = False #has this tileset been loaded?
    self.SetID = None #ID code for the tileset
    self.filename = None #full filepath of the tileset
    self.copies = 0 #how many copies to allow
    self.Name = None # Name of the tileset
    self.DisplayTileWindow = True #flag to display on the tile window
    self.DisplayMapWindow = True #flag to display on the map window
    self.used = False #has this set been used in the current map?
    self.queue_loading = False #should this be loaded when exiting the browser?
    self.qty_changed = False  #set to True if self.copies has changed

class IJstruct:
  def __init__(self, i=None, j=None):
    self.i = i
    self.j = j
    self.index = 0

class RandomTile:
  def __init__(self, tile, side, index):
    self.tile = tile  #reference to the tile
    self.side = side  #which side of the tile?  'A' or 'B'
    self.tilelist_index = index #index to the app.tilelist
    self.rotation = 0  #current rotation of the tile
    self.Xdim = 0 #x dimension of the tile, as placed on the map_array
    self.Ydim = 0 #y dimension of the tile, as placed on the map_array

class TilePoint:
  def __init__(self):
    self.i = 0 #row, 0 based
    self.j = 0 #column, 0 based
    self.index = 0#index of the tile placed
    self.edge = False  #Is this on the edge of the map?

class Tile:
  def __init__(self):
    self.key_index = 0 #unique index assigned to every tile loaded;  held by gv.key_index
    self.index = 0 #unique value for each tile placed in each tileset
    self.sort = False #processed by SortTilePanelBySize
    self.area = 0 #used in sorting on the tile panel
    self.sideA = None #wxImage format.  Not changed after loading from disk
    self.sideB = None #wxImage format.  Not changed after loading from disk
    self.MapPosition = None #wx.Point2D() grid square location of the image on the Map.  Will be converted to pixels based on zoomfactors
    self.TilePosition = (0,0) #pixel location of the image on the TilePanel
    self.actualXsize = 0 #size of the tile in squares
    self.actualYsize = 0 #size of the tile in squares
    self.TileRect = wx.Rect() #current rect being displayed on the TilePanel
    self.TileRectB = wx.Rect()
    self.TileGrid = wx.Point(0,0) #grid location as set by SortTilePanelGrid
    self.MapRect = None #wx.Rect2D() #current rect being displayed on the MapPanel, grid coords
    self.hotspot = wx.Point(0,0) #location on the tile where we are us
    self.ShowOnTilePanel = True #is it visible on the tilepanel (SetID filters)
    self.ShowOnMapPanel = True #is it visible on the map panel? (SetID filter)
    self.PlacedOnTilePanel = False #has it been assigned position in the TilePanelGrid?
    self.text = None # text string/annotation
    self.filenameA = None
    self.filenameB = None
    self.imagenameA = None
    self.imagenameB = None
    self.rotation = 0.0 #rotation of the mapdisplay tile in degrees
    self.showingBside = False
    self.mapdisplay = None #wxBitmap showing on the map window
    self.tiledisplay = None #wxImage for tile display.  This is the current display on the tile window.
    self.tilesetName = None # text string of the set name
    self.tileID = None # individual tile ID in the tileset
    self.tilesetID = None # text string of the set ID
    self.tilenameA = None # name for side A
    self.tilenameB = None # name for side B
    self.copies = 0 #How many total copies of this tile available for placement, ie, number of sets owned * number of tiles per set.
    self.count = 1 #How many duplicate tiles in the set?
    self.num_used = 0 #How many copies have been placed on the map panel.  This is recalculated when map pages are changed.
    self.selected = False #Is this tile selected for use?
    self.dimmed = False #this is set if all copies of the tile have been placed
    self.delete = False #is this tile queued for deletion?
    self.order = None #display order value for tile on the map window
    self.highlight = False #highlighting tile flag for the map window
    self.taglist = [] #used for filter tags
    self.random_defA = False #used for random dungeon generation, True if edges are defined.
    self.random_defB = False
    self.TopEdgeA = []  #wall, connect, door, obstruction, outside
    self.BottomEdgeA = []
    self.RightEdgeA = []
    self.LeftEdgeA = []
    self.TopEdgeB = []  #wall, connect, door, obstruction, outside
    self.BottomEdgeB = []
    self.RightEdgeB = []
    self.LeftEdgeB = []
    self.layer = 0  #index of the layer, not the name.  Default to base layer
    self.page = None  #which page name of the MapNotebook to display on?
    self.tilepages = []  #which pages can this tile appear on the tile panel?
    self.SnapToGrid = True  #set to False to position off-grid.  In this case self.MapPosition will be a wxPoint2D.
    self.marker = False    #True if it is a marker.
    return

  def HitTest(self, pt):
    rect = self.GetRect()
    return rect.InsideXY(pt.x, pt.y)
  
  def RotateTile(self, direction):
    start_angle = self.rotation
    if (direction == 'CCW'):
      self.rotation -= 90
    elif (direction == 'CW'):
      self.rotation += 90

    if (self.rotation == -90):
      self.rotation = 270
    elif (self.rotation == 360):
      self.rotation = 0
    
    width = self.MapRect.width
    height = self.MapRect.height
    self.MapRect.width = height
    self.MapRect.height = width
    return
  
  def GenerateMapDisplay(self, resolution):
    """Generate the proper mapdisplay bitmap.  Resolution is generally the current gv.MapZoomFactor.
       One exception to this is when printing or saving the screen image."""
    
    #Get the correct wxImage from either sideA or sideB
    if ((self.showingBside) and (self.sideB)):
      image = self.sideB
    else:
      self.showingBside = False
      image = self.sideA  #default to sideA if no sideB available
      
    #resize to current mapZoom
    Xscale = self.actualXsize*resolution
    Yscale = self.actualYsize*resolution
    image = image.Scale(Xscale, Yscale)
    
    #rotate to current rotation value
    if (self.rotation == 0):
      pass  #no change to rotation
    elif (self.rotation == 90):
      image = image.Rotate90(True)
    elif (self.rotation == 180):
      image = image.Rotate90(True)
      image = image.Rotate90(True)
    elif (self.rotation == 270):
      image = image.Rotate90(False)

    self.mapdisplay = wx.BitmapFromImage(image)
    return True

  def GetRect(self):
    """Return the rect of map pixel coordinates for the tile image"""
    return wx.Rect(self.MapPosition.x*gv.MapZoomFactor, self.MapPosition.y*gv.MapZoomFactor, self.mapdisplay.GetWidth(), self.mapdisplay.GetHeight())

#---------------End Tile class -----------------------------

class Annotation:
  def __init__(self):
    self.selected = False
    self.x = 0.0
    self.y = 0.0
    self.font = None #wx.Font for print output
    self.screen_font = None #wx.Font for screen display
    self.text = None #what do you want to say?
    self.bg = wx.Colour()
    self.point = None
    self.fg = wx.Colour()
    self.extent = wx.Rect()
    self.bmp = None #bitmap of the text used in dragging, display, etc.
    self.opaque = True #fill the background?
    #self.fontdata = None
    self.zoomfactor = 0
    self.index = 0 #unique identifier for the annotation
    self.layer = None      #which layer to display on?
    self.page = None  #which mapbook pagename to display on?

  def __deepcopy__(self, source):
    NewText = Annotation()
    NewText.selected = source.selected
    NewText.x = source.x
    NewText.y = source.y
    NewText.font = source.font
    NewText.screen_font = source.screen_font
    NewText.text = source.text
    NewText.bg = source.bg
    NewText.point = source.point
    NewText.fg = source.fg
    NewText.extent = wx.Rect2D()
    NewText.extent.x = source.extent.x
    NewText.extent.y = source.extent.y
    NewText.extent.height = source.extent.height
    NewText.extent.width = source.extent.width
    NewText.bmp = source.bmp
    NewText.opaque = source.opaque
    NewText.zoomfactor = source.zoomfactor
    NewText.index = source.index
    NewText.layer = source.layer
    NewText.page = source.page
    return NewText

class MapStructInfo:
  def __init__(self):
    self.name = "Pymapper"  #name of the map
    self.filename = None #filename of the .map file
    self.background = None #wx image format; used to facilitate rotation
    self.bg_displaymode = None #may be Register, Tile, Center
    self.bg_x_dimension = 0  #size of the background in squares
    self.bg_y_dimension = 0  
    self.background_filename = None #original path for the filename of the image
    self.gridcolor = wx.Colour(255,0,0,255) # (r, g, b, a) wxColourData item
    self.gridPenWidth = 1
    self.gridPenStyle = wx.SOLID
    self.rows = 40 #default values
    self.columns = 40
    self.Extents = wx.Rect(0,0,0,0) #x, y, width, height in pixels
    self.GridExtents = wx.Rect(0,0,0,0) # units in grid cells
    self.backupfilename = None
    self.geomorph = False
    self.geomorphData = Geomorph_Record()
    return


class DiceRollDialog(PyMapperDialogs.DiceRollDialogBase):
  def __init__(self, parent):
    olddir = os.getcwd()
    os.chdir(gv.root_directory)  #this is necessary so that bitmap paths are read by the dialog code correctly
    PyMapperDialogs.DiceRollDialogBase.__init__(self, parent)
    os.chdir(olddir)
    self.txResults.Clear()
    return
  
  def UpdateResultsLog(self, combo, result):
    text = combo + " = " + result + '\n'
    self.txResults.AppendText(text)
    self.Update()
    return
  
  def RollDice(self, combo):
    """combo is equivalent to 3d6+2, or 1d12."""
    result = app.RollDice(combo)
    self.UpdateResultsLog(combo, str(result))
    return result

  def OnRoll_d4(self, evt):
    value = self.RollDice('1d4')
    self.txResult_d4.SetValue(str(value))
    return

  def OnRoll_d6(self, evt):
    value = self.RollDice('1d6')
    self.txResult_d6.SetValue(str(value))
    return

  def OnRoll_d8(self, evt):
    value = self.RollDice('1d8')
    self.txResult_d8.SetValue(str(value))
    return

  def OnRoll_d10(self, evt):
    value = self.RollDice('1d10')
    self.txResult_d10.SetValue(str(value))
    return

  def OnRoll_d12(self, evt):
    value = self.RollDice('1d12')
    self.txResult_d12.SetValue(str(value))
    return

  def OnRoll_d20(self, evt):
    value = self.RollDice('1d20')
    self.txResult_d20.SetValue(str(value))
    return

  def OnRoll_d100(self, evt):
    value = self.RollDice('1d100')
    self.txResult_d100.SetValue(str(value))
    return

  def OnRoll_Custom1(self, evt):
    combo = self.txCustom1.GetValue()
    result = self.RollDice(combo)
    self.txResult_Custom1.SetValue(str(result))
    return

  def OnRoll_Custom2(self, evt):
    combo = self.txCustom2.GetValue()
    result = self.RollDice(combo)
    self.txResult_Custom2.SetValue(str(result))
    return

  def OnClose(self, evt):
    self.Show(False)
    self.Destroy()
    return

  def OnHelp(self, evt):
    text = "Custom dice roll combinations can be entered into the two custom fields.  The combo is in standard format, ie, 1d12, 2d6x3 or 3d6+4.\n\nThe format is NdSxM+A where:\nN = Number of times to roll the dice (required)\nd = Dice separator (required)\nS = Number of sides on the die (required)\nx = Multiplier separator (optional)\nM = Multiplier after all of the dice have been rolled (optional, defaults to 1 if no value given)\n+ = Additive separator (optional)\nA = Additive modifier added after dice are rolled and multiplied (optional, defaults to 0 if no value given)\n\nNon-standard dice can be used also, ie, 1d3 or 1d27."
    dlg = HelpDialog(self, text)
    dlg.ShowModal()
    dlg.Destroy()
    return

class pymSplashScreen(wx.adv.SplashScreen):
  def __init__(self, parent=None):
    aBitmap = wx.Image(name = "map_image.jpg").ConvertToBitmap()
    if (not aBitmap.IsOk()):
      logging.error("SplashScreen:  Could not find map_image.jpg")
      return False
    splashStyle = wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT
    splashDuration = 30 # milliseconds
    # Call the constructor with the above arguments in exactly the
    # following order.
    wx.SplashScreen.__init__(self, aBitmap, splashStyle, splashDuration, parent)
    self.Bind(wx.EVT_CLOSE, self.OnExit)
    wx.Yield()

  def OnExit(self, evt):
    self.Hide()
    evt.Skip()
    return


class PyMapperAppMain(wx.App):
  def OnInit(self):
    logging.basicConfig(filename="pymapper_errors.log",
                        filemode='w',
                        format='%(asctime)s %(levelname)s %(funcName)s %(lineno)d %(message)s\n',
                        level=logging.DEBUG)
    logging.debug(str(sys.version_info))
    logging.debug(str(sys.platform))
    logging.info("Pymapper Version: " + str(VERSION))
    if (SPLASH):
      gv.StartupOffset = self.SplashScreen()  #affects the import tileset progress dialog
    else:
      gv.StartupOffset = None
    
    logging.debug("Begin gv folder assignments")

    gv.root_directory = os.getcwd()
    gv.tiles_directory = os.path.join(gv.root_directory, "tiles")
    gv.maps_directory = os.path.join(gv.root_directory,"maps")
    gv.artwork_directory = os.path.join(gv.root_directory,"artwork")
    gv.srd_directory = os.path.join(gv.root_directory,"srd")
    gv.encounters_directory = os.path.join(gv.root_directory,"maps")
    gv.geomorphs_directory = os.path.join(gv.root_directory,"geomorphs")
    gv.tokens_directory = os.path.join(gv.root_directory, "tokens")
    gv.image_directory = gv.root_directory
    gv.backup_directory = gv.root_directory

    logging.debug("gv.root_directory = %s", gv.root_directory)
    logging.debug("gv.tiles_directory = %s",gv.tiles_directory)
    logging.debug("gv.maps_directory = %s",gv.maps_directory)
    logging.debug("gv.artwork_directory = %s",gv.artwork_directory)
    logging.debug("gv.srd_directory = %s",gv.srd_directory)
    logging.debug("gv.encounters_directory = %s",gv.encounters_directory)
    logging.debug("gv.geomorphs_directory = %s",gv.geomorphs_directory)
    logging.debug("gv.image_directory = %s",gv.root_directory)
    logging.debug("gv.backup_directory = %s",gv.root_directory)
    logging.debug("gv.tokens_directory = %s",gv.tokens_directory)

    #check license
    userID = os.access(os.path.join(gv.root_directory,"pymapper.license"), os.F_OK)
    if (userID):
      gv.PymapperUser = True #determines whether to display development data
      logging.info("Pymapper User detected")
    else:
      gv.PymapperUser = False
      logging.info("General User detected")

    tiles_avail = os.access(gv.tiles_directory, os.F_OK)
    maps_avail = os.access(gv.maps_directory, os.F_OK)
    encounters_avail = os.access(gv.encounters_directory, os.F_OK)
    geomorphs_avail = os.access(gv.geomorphs_directory, os.F_OK)
    tokens_avail = os.access(gv.tokens_directory, os.F_OK)
    
    if (not tokens_avail):
      try:
        os.mkdir(gv.tokens_directory)
      except OSError:
        logging.error("Could not find tokens folder, default to program folder")
        gv.tiles_directory = gv.tokens_directory

    if (not tiles_avail):
      try:
        os.mkdir(gv.tiles_directory)
      except OSError:
        logging.critical("Could not find tiles folder, default to program folder")
        gv.tiles_directory = gv.root_directory

    if (not geomorphs_avail):
      try:
        os.mkdir(gv.geomorphs_directory)
      except OSError:
        logging.error("Could not find geomorphs folder, default to program folder")
        gv.geomorphs_directory = gv.root_directory

    if (not encounters_avail):
      try:
        os.mkdir(gv.encounters_directory)
      except OSError:
        logging.error("Could not create encounters folder, defaulting to program folder")
        gv.tiles_directory = gv.root_directory

    if (not maps_avail):
      try:
        os.mkdir(gv.maps_directory)
      except OSError:
        logging.error("Could not find maps folder, default to program folder")
        gv.maps_directory = gv.root_directory

    logging.debug("Folder availability:")
    logging.debug("tiles available: %s", tiles_avail)
    logging.debug("maps available: %s", maps_avail)
    logging.debug("encounters available: %s", encounters_avail)
    logging.debug("geomorphs available: %s", geomorphs_avail)
    logging.debug("tokens available: %s", tokens_avail)
    logging.debug("----")
    self.init_frame()
    logging.debug("Frame Initialization complete")

    display = wx.Display()
    logging.debug("Set Frame Dimensions basd on wxDisplay()")
    self.frame.SetDimensions(gv.WindowExtents.x, gv.WindowExtents.y, gv.WindowExtents.width, gv.WindowExtents.height)
    logging.info("wxDisplay X, Y, W, H: %d %d %d %d" ,gv.WindowExtents.x, gv.WindowExtents.y, gv.WindowExtents.width, gv.WindowExtents.height)
    index = display.GetFromWindow(self.frame)
    gv.SashPosition = self.frame.SplitterSash.GetSashPosition()
    
    #read ftp settings, if available
    ftp_settings = os.access(os.path.join(gv.root_directory, "ftp_settings.ini"), os.F_OK)
    if (ftp_settings):
      #read the settings file
      settings = open(os.path.join(gv.root_directory, "ftp_settings.ini"), 'r')
      gv.FTP_Filename = settings.readline().rstrip('\r\n')
      gv.FTP_Password = settings.readline().rstrip('\r\n')
      gv.FTP_Username = settings.readline().rstrip('\r\n')
      gv.FTP_Server = settings.readline().rstrip('\r\n')
      settings.close()
      logging.info("FTP settings read")
    else:
      logging.info("No FTP settings on disk")
    
    if (index == wx.NOT_FOUND):
      #resize and refit window
      gv.WindowExtents = display.GetGeometry()
      self.frame.SetDimensions(gv.WindowExtents.x, gv.WindowExtents.y, gv.WindowExtents.width, gv.WindowExtents.height)

    if (gv.ReadSRDFileData == True) and (not gv.d20_SRD_data_available):   #read the SRD?
      self.OnDungeon_Load_d20_Resources()
      
    if (gv.Read5EditionFileData == True) and (not gv.DnD_5E_data_available):  #read the DnD5 material?
      self.OnDungeon_Load_DnD5_Resources()

    if (gv.ShowTips == True):  #show tip of the day?
      self.OnHelp_ShowTips()

    if (gv.ShowTutorial) and (sys.platform == 'win32'):  #value read from the .ini file, only auto-open on win32 machines.  Otherwise we get a startup crash on mac.
      gv.ShowTutorial = False
      #open pdf tutorial file
      #self.OnFileOpen(selectedFile = gv.maps_directory+'/tutorial.map')
      #self.SaveIniFile()
    os.chdir(gv.root_directory)
    
    #check for presence of email registration info  
    email_file = os.path.join(gv.root_directory,"email_info_v2.ini")
      
    if (not os.access(email_file, os.F_OK)):
      info_dlg = wx.MessageDialog(self.frame, message="Would you like to enter your email address in order to receive program updates?  You can always register later by going to the Help menu", 
                                  caption="Registration Not Found", style= wx.YES_NO|wx.ICON_QUESTION)
      register = info_dlg.ShowModal()
      if (register == wx.ID_YES):
        self.OnHelp_RegisterProgram()
      else:
        try:
          email_file = os.path.join(gv.root_directory,"email_info_v2.ini")
          email_info = open(email_file, "w")
          email_info.write("No User Information\n")
          email_info.close()
        except:
          logging.error("RegisterProgram: Could not open email_info_v2.ini for writing")
        
    logging.debug("End primary frame initialization; begin main program flow\n")
    return True
  #end OnInit

  def init_frame(self):
    logging.debug("Start init_frame")
    self.frame = PyMapperFrame()
    self.frame.Show()
    logging.debug("Executed self.frame.Show()")
    logging.debug("Is self.frame OK? %s", self.frame)
    self.MasterIndex = 0
    self.UndoList = []
    self.FileList = []  #recently used files
    self.DrawingList = []  #list of DrawingObjects 
    gv.RandomSettings = RandomDungeonSettings()

    font = wx.Font(30, 74, 90, 92, underline=False, faceName="Times New Roman")
    if (font == wx.NullFont):
      logging.warning("Could not find Times New Roman font, using system font instead")
      gv.TextFont = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
    else:
      gv.TextFont = font

    self.textlist = []
    self.TextInMotion = False

    self.IsIcon = False
    self.hovertimer = wx.Timer(self.frame, 5) #the 5 is the eventID for this timer.
    self.HighlightTimer = wx.Timer(self.frame, 9) #the 9 is the eventID for this timer.
    self.HighlightTimer.Start(1)
    self.MouseOnTilePanel = False #used in hovering to determine where the mouse is

    self.Bind(wx.EVT_TIMER, self.OnTimer)

    self.DrawTools = None  #set to the dialog instance when gv.SelectMode == 'draw'

    self.frame.SetLabel('PyMapper '+VERSION)

    ProgramIcon = wx.Icon(os.path.join(gv.artwork_directory,'pymapper.ico'), wx.BITMAP_TYPE_ICO, 16,16)
    self.frame.SetIcon(ProgramIcon)

    self.FindTilesetFiles()

    self.ImageNotFound = wx.Image(os.path.join(gv.artwork_directory,"not_found.png"), wx.BITMAP_TYPE_PNG)
    self.RoomIcon = wx.Image(os.path.join(gv.artwork_directory,"scroll.png"), wx.BITMAP_TYPE_PNG)
    self.TrapIcon = wx.Image(os.path.join(gv.artwork_directory,"trap_icon.png"), wx.BITMAP_TYPE_PNG)
    self.MonsterIcon = wx.Image(os.path.join(gv.artwork_directory,"monster_icon.png"), wx.BITMAP_TYPE_PNG)
    self.NPC_Icon = wx.Image(os.path.join(gv.artwork_directory,"npc_icon.png"), wx.BITMAP_TYPE_PNG)
    self.TreasureIcon = wx.Image(os.path.join(gv.artwork_directory,"treasure_icon.png"), wx.BITMAP_TYPE_PNG)

    self.TileSelectButton = self.frame.tgTileMode
    self.IconSelectButton = self.frame.tgIconMode
    self.DrawSelectButton = self.frame.tgDrawMode
    self.FogSelectButton = self.frame.tgFogMode
    self.SelectBGColor = self.TileSelectButton.GetBackgroundColour()
    self.SelectFGColor = self.TileSelectButton.GetForegroundColour()
    self.UnSelectBGColor = self.IconSelectButton.GetBackgroundColour()
    self.UnSelectFGColor = self.IconSelectButton.GetForegroundColour()

    self.frame.Bind(wx.EVT_CLOSE, self.OnExit)

    for i in range(5):  #initialize the recent files list
      self.FileList.append("-----")

    self.ReadRecentFileList()

    self.frame.Bind(wx.EVT_MENU, self.OnRecentFile, self.frame.RecentFile1)
    self.frame.Bind(wx.EVT_MENU, self.OnRecentFile, self.frame.RecentFile2)
    self.frame.Bind(wx.EVT_MENU, self.OnRecentFile, self.frame.RecentFile3)
    self.frame.Bind(wx.EVT_MENU, self.OnRecentFile, self.frame.RecentFile4)
    self.frame.Bind(wx.EVT_MENU, self.OnRecentFile, self.frame.RecentFile5)
    
    self.MapPanel = self.frame.MapWindow
    if (not self.MapPanel):
      logging.critical("init_frame:  Could not create self.MapPanel")
    gv.MapPanelPosition = self.MapPanel.GetPosition()
    self.BindMapPanel(self, self.MapPanel)
    gv.MapPanelList.append(self.MapPanel)

    #MapStruct info
    size = self.MapPanel.GetSize()
    self.MapStruct = MapStructInfo()
    self.MapStruct.rows = 2*(size.height // gv.MapZoomFactor)
    self.MapStruct.columns = 2*(size.width // gv.MapZoomFactor)
    self.MapStruct.Extents.x = 2*size.width
    self.MapStruct.Extents.y = 2*size.height
    self.MapStruct.Extents.height = 0
    self.MapStruct.Extents.width = 0
    self.MapStruct.GridExtents.x = 2*size.width
    self.MapStruct.GridExtents.y = 2*size.height
    self.MapStruct.GridExtents.height = 0
    self.MapStruct.GridExtents.width = 0

    self.frame.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)

    #self.MapBuffer is the map display of all tiles, etc.
    self.MapBuffer = wx.Bitmap(self.MapStruct.rows*gv.MapZoomFactor, 
                                    self.MapStruct.columns*gv.MapZoomFactor)
    if (self.MapBuffer):
      logging.debug("init_frame:  MapBuffer initialized")
    else:
      logging.critical("init_frame:  MapBuffer is NONE")
    #self.MapFogImage (wxImage) is the fog of war overlay on the player screen
    self.MapFogImage = wx.Image(self.MapStruct.columns*gv.MapZoomFactor, 
                                    self.MapStruct.rows*gv.MapZoomFactor)
    self.MapPanelDC = wx.BufferedDC(None, self.MapBuffer)
    self.MapPanel.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
    self.MapPanelDC.Clear()
    self.MapPanelDC.SetBackground(wx.Brush(gv.MapPanelBackgroundColor))
    self.VirtualMapPanel = wx.Size(self.MapStruct.columns*gv.MapZoomFactor, 
                                   self.MapStruct.rows*gv.MapZoomFactor)

    self.TilePanel = self.frame.TileWindow
    self.BindTilePanel(self, self.TilePanel)
    self.TilePanel.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
    size = self.TilePanel.GetSize()
    gv.TilePanelList.append(self.TilePanel)

    #notebook items
    self.nbMapNotebook = wx.Notebook(self.frame)
    self.nbTileNotebook = wx.Notebook(self.frame)

    self.nbMapNotebook = self.frame.nbMapNotebook
    page = self.nbMapNotebook.GetSelection()
    self.nbMapNotebook.SetPageText(page, "Map")
    (x,y) = self.MapPanel.GetViewStart()
    newpage = Page_Record(page, gv.MapZoomFactor, x, y, "Map")
    gv.MapPageList.append(newpage)

    self.nbTileNotebook = self.frame.nbTileNotebook
    page = self.nbTileNotebook.GetSelection()
    self.nbTileNotebook.SetPageText(page, "Tiles")
    (x,y) = self.TilePanel.GetViewStart()
    newtilepage = Page_Record(page, gv.TileZoomFactor, x, y, "Tiles")
    gv.TilePageList.append(newtilepage)

    self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightClickMapNotebook, self.nbMapNotebook)
    self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightClickTileNotebook, self.nbTileNotebook)
    self.Bind(wx.EVT_LEFT_DCLICK, self.RMapbookChangePageName, self.nbMapNotebook)
    self.Bind(wx.EVT_LEFT_DCLICK, self.RTilebookChangePageName, self.nbTileNotebook)
    self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.ChangeMapNotebookPage, self.nbMapNotebook)
    self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.ChangeTileNotebookPage, self.nbTileNotebook)

    self.TileBuffer = wx.Bitmap(size.width, size.height)
    Brush = wx.Brush(gv.TilePanelBackgroundColor)
    Pen = wx.Pen(gv.TilePanelBackgroundColor)
    self.TilePanel.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
    self.TilePanelDC = wx.BufferedDC(None, self.TileBuffer)
    self.TilePanelDC.SetBrush(Brush)
    self.TilePanelDC.SetPen(Pen)
    self.TilePanelDC.DrawRectangle(0,0, size.width, size.height)

    self.TilePanelFiltered = False # have any filters been set for the TilePanel?
    self.TilePanelDC.SetBackground(wx.Brush(gv.TilePanelBackgroundColor))
    
    panelsize = self.TilePanel.GetSize()
    #number of rows, columns available in the TilePanel
    ncolumns = int(panelsize.width/gv.TileZoomFactor)
    nrows = int(panelsize.height/gv.TileZoomFactor)

    self.VirtualTilePanel = wx.Size(ncolumns, nrows)

    self.backgroundDC = None
    gv.GridPen = wx.Pen(wx.RED, 1, wx.SOLID)

    self.tilelist = []       # list of the tiles showing in the tilewindow
    self.MasterTilelist = [] #list of all tiles loaded
    self.maplist = []        #list of the tiles showing on the map window
    self.selectlist = []     #list of tiles for multi-select
    self.SymbolList = []     #list of available symbols
    self.MarkerList = []     #list of MarkerRecord items

    self.LoadSymbolFiles(True)
    self.LoadMarkerFiles()

    self.AllowDrag = False #A tile has been selected and can be placed
    self.dragImage = None #Which image is being moved around the MapPanel
    self.TileInMotion = False #are we moving a tile from the tile window?
    self.PanWindow = False # are we moving the map window around?
    self.hiliteShape = None
    self.StartDragPos = None

    self.frame.Bind(wx.EVT_ICONIZE, self.OnIconize)
    #File Menu
    self.frame.Bind(wx.EVT_MENU, self.OnFileNew, id=PyMapperDialogs.mFileNew)
    self.frame.Bind(wx.EVT_MENU, self.OnFileNew, id=PyMapperDialogs.mFileNewGeomorph)
    self.frame.Bind(wx.EVT_MENU, self.OnFileOpen, id=PyMapperDialogs.mFileOpen)
    self.frame.Bind(wx.EVT_MENU, self.OnFileOpen, id=PyMapperDialogs.mFileOpenGeomorph)
    self.frame.Bind(wx.EVT_MENU, self.OnFileOpen, id=PyMapperDialogs.mFileImportFile)
    self.frame.Bind(wx.EVT_MENU, self.OnFileSave, id=PyMapperDialogs.mFileSave)
    self.frame.Bind(wx.EVT_MENU, self.OnFileSaveAs, id=PyMapperDialogs.mFileSaveAs)
    self.frame.Bind(wx.EVT_MENU, self.OnImportBackground, id=PyMapperDialogs.mFileImportBackground)
    self.frame.Bind(wx.EVT_MENU, self.OnExit, id=PyMapperDialogs.mFileExit)  # CTRL+Q
    logging.debug("File menu binding complete")
    
    #Tileset Menu
    self.frame.Bind(wx.EVT_MENU, self.OnTilesetEdit, id=PyMapperDialogs.mTilesetEdit)
    self.frame.Bind(wx.EVT_MENU, self.OnTilesetBrowser, id=PyMapperDialogs.mTilesetBrowser)
    self.frame.Bind(wx.EVT_MENU, self.OnTilesetCreateFromCompositeImage, id=PyMapperDialogs.mTilesetCreateMaster)

    #Options Menu
    self.frame.Bind(wx.EVT_MENU, self.OnOptionsProgram, id=PyMapperDialogs.mOptionsProgram)
    self.frame.Bind(wx.EVT_MENU, self.OnOptionsTilesets, id=PyMapperDialogs.mOptionsTilesets)
    self.frame.Bind(wx.EVT_MENU, self.OnOptionsSymbolsMarkers, id=PyMapperDialogs.mOptionsSymbolsMarkers)
    self.frame.Bind(wx.EVT_MENU, self.OnOptionsText, id=PyMapperDialogs.mOptionsText)
    self.frame.Bind(wx.EVT_MENU, self.OnOptionsIniFile, id=PyMapperDialogs.mOptionsInifile)
    self.frame.Bind(wx.EVT_MENU, self.OnOptionsFTP, id=PyMapperDialogs.mOptionsFTP)
    logging.debug("Options menu binding complete")

    #Help Menu
    self.frame.Bind(wx.EVT_MENU, self.OnHelp_About, id=PyMapperDialogs.mHelpAbout)
    self.frame.Bind(wx.EVT_MENU, self.OnHelp_ShowTips, id=PyMapperDialogs.mHelpShowTips)
    self.frame.Bind(wx.EVT_MENU, self.OnHelp_Contents, id=PyMapperDialogs.mHelpContents)
    self.frame.Bind(wx.EVT_MENU, self.OnHelp_OpenTutorial, id=PyMapperDialogs.mHelpOpenTutorial)
    self.frame.Bind(wx.EVT_MENU, self.OnHelp_KeyboardShortcuts, id=PyMapperDialogs.mHelpKeyboardShortcuts)
    self.frame.Bind(wx.EVT_MENU, self.OnHelp_ProgramFoundation, id=PyMapperDialogs.mHelpProgramFoundation)
    self.frame.Bind(wx.EVT_MENU, self.OnHelp_RegisterProgram, id=PyMapperDialogs.mHelpRegisterProgram)
    logging.debug("Help menu binding complete")

    #Edit Menu
    self.frame.Bind(wx.EVT_MENU, self.OnEditMapSize, id = PyMapperDialogs.mEditMapSize)
    self.frame.Bind(wx.EVT_MENU, self.OnUndoAction, id = PyMapperDialogs.mEditUndo)
    logging.debug("Edit menu binding complete")

    #Reports Menu
    self.frame.Bind(wx.EVT_MENU, self.OnReportsManifest, id = PyMapperDialogs.mReportsManifest)
    self.frame.Bind(wx.EVT_MENU, self.OnReportsTilesets, id = PyMapperDialogs.mReportsTilesets)
    self.frame.Bind(wx.EVT_MENU, self.OnMapsRandomDungeon, id = PyMapperDialogs.mMapsRandomDungeon)
    logging.debug("Reports menu binding complete")

    #Print Menu
    self.frame.Bind(wx.EVT_MENU, self.OnPrintMap, id = PyMapperDialogs.mPrintMap)
    self.frame.Bind(wx.EVT_MENU, self.OnChangePrintResolution, id = PyMapperDialogs.mPrintChangeResolution)
    self.frame.Bind(wx.EVT_MENU, self.OnPrintImage, id = PyMapperDialogs.mPrintImage)
    logging.debug("Print menu binding complete")
    
    #View Menu
    self.frame.Bind(wx.EVT_MENU, self.OnViewViewAll, id = PyMapperDialogs.mViewViewAll)
    self.frame.Bind(wx.EVT_MENU, self.OnViewFilterTags, id = PyMapperDialogs.mViewFilterTags)
    self.frame.Bind(wx.EVT_MENU, self.OnViewTilesetLayerFilter, id = PyMapperDialogs.mViewViewTilesetLayerFilter)
    self.frame.Bind(wx.EVT_MENU, self.OnViewBackground, id = PyMapperDialogs.mViewBackground)
    self.frame.Bind(wx.EVT_MENU, self.OnViewGridCoordinates, id = PyMapperDialogs.mViewGridCoordinates)
    self.frame.Bind(wx.EVT_MENU, self.OnViewGrid, id = PyMapperDialogs.mViewGrid)
    self.frame.Bind(wx.EVT_MENU, self.OnViewDualTileSides, id = PyMapperDialogs.mViewDualTileDisplay)
    self.frame.Bind(wx.EVT_MENU, self.OnViewHighlightIcons, id = PyMapperDialogs.mViewHighlightIcons)
    self.frame.Bind(wx.EVT_MENU, self.OnViewSecondaryScreen, id = PyMapperDialogs.mViewSecondaryScreen)
    self.frame.Bind(wx.EVT_MENU, self.OutlineTiles, id=PyMapperDialogs.mViewOutlineTiles)
    self.frame.Bind(wx.EVT_MENU, self.OnUpdateToFTP, id=PyMapperDialogs.mViewUpdateToFTP)
    self.frame.Bind(wx.EVT_MENU, self.OnUpdateFogImage, id=PyMapperDialogs.mViewUpdateFog)
    logging.debug("View menu binding complete")
    
    #Dungeon Menu
    #disable until the data files have been loaded
    self.frame.menubar.Enable(PyMapperDialogs.mDungeonEncounters, False)
    self.frame.menubar.Enable(PyMapperDialogs.mDungeonTreasures, False)
    self.frame.menubar.Enable(PyMapperDialogs.mDungeonPathfinderMagicItems, False)
    #self.frame.menubar.Enable(PyMapperDialogs.mDungeonCombatTracking, False)
    self.frame.menubar.Enable(PyMapperDialogs.mDungeonD20Spells, False)
    self.frame.menubar.Enable(PyMapperDialogs.mDungeonD20Feats, False)
    self.frame.menubar.Enable(PyMapperDialogs.mDungeonTraps, False)
    self.frame.menubar.Enable(PyMapperDialogs.mDungeonNPCGenerator, False)
    self.frame.menubar.Enable(PyMapperDialogs.mDungeonMonster, False)
    self.frame.menubar.Enable(PyMapperDialogs.mDungeonMonster5E, False)
    self.frame.menubar.Enable(PyMapperDialogs.mDungeonNPC_5E, False)
    self.frame.menubar.Enable(PyMapperDialogs.mDungeonSpell_5E, False)
    
    if (not gv.PymapperUser):
      self.frame.menubar.Enable(PyMapperDialogs.mDungeonEncounters, False) #disable for non-pymapper user while in development

    self.frame.Bind(wx.EVT_MENU, self.OnDungeon_Encounters, id=PyMapperDialogs.mDungeonEncounters)
    self.frame.Bind(wx.EVT_MENU, self.OnDungeon_Monsters, id=PyMapperDialogs.mDungeonMonster)
    self.frame.Bind(wx.EVT_MENU, self.OnDungeon_5EMonsters, id=PyMapperDialogs.mDungeonMonster5E)
    self.frame.Bind(wx.EVT_MENU, self.OnDungeon_5E_NPC, id=PyMapperDialogs.mDungeonNPC_5E)
    self.frame.Bind(wx.EVT_MENU, self.OnDungeon_5E_Spells, id=PyMapperDialogs.mDungeonSpell_5E)
    self.frame.Bind(wx.EVT_MENU, self.OnDungeon_Traps, id=PyMapperDialogs.mDungeonTraps)
    self.frame.Bind(wx.EVT_MENU, self.OnDungeon_Treasures, id=PyMapperDialogs.mDungeonTreasures)
    self.frame.Bind(wx.EVT_MENU, self.OnDungeon_NPCgenerator, id=PyMapperDialogs.mDungeonNPCGenerator)
    self.frame.Bind(wx.EVT_MENU, self.OnDungeon_Load_d20_Resources, id=PyMapperDialogs.mDungeonLoadD20Files)
    self.frame.Bind(wx.EVT_MENU, self.OnDungeon_Load_DnD5_Resources, id=PyMapperDialogs.mDungeonLoadDnD5Files)
    self.frame.Bind(wx.EVT_MENU, self.OnDungeon_Pathfinder_MagicItems, id=PyMapperDialogs.mDungeonPathfinderMagicItems)
    self.frame.Bind(wx.EVT_MENU, self.OnDungeon_Pathfinder_Monsters, id=PyMapperDialogs.mDungeonPathfinderMonsters)
    self.frame.Bind(wx.EVT_MENU, self.OnDungeon_d20Spells, id=PyMapperDialogs.mDungeonD20Spells)
    self.frame.Bind(wx.EVT_MENU, self.OnDungeon_d20Feats, id=PyMapperDialogs.mDungeonD20Feats)
    self.frame.Bind(wx.EVT_MENU, self.OnDungeon_About, id=PyMapperDialogs.mDungeonAbout)
    self.frame.Bind(wx.EVT_MENU, self.OnDungeon_ShowIcons, id=PyMapperDialogs.mDungeonShowIcons)
    self.frame.Bind(wx.EVT_MENU, self.OnDungeon_DiceRoller, id=PyMapperDialogs.mDungeonDiceRoller)
    self.frame.Bind(wx.EVT_MENU, self.OnDungeon_CombatTracking, id=PyMapperDialogs.mDungeonCombatTracking)
    logging.debug("Dungeon menu binding complete")

    #Accelerator shortcuts
    accel_list = []
    accel_list.append(wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('N'), PyMapperDialogs.mFileNew))
    accel_list.append(wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('O'), PyMapperDialogs.mFileOpen))
    accel_list.append(wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('S'), PyMapperDialogs.mFileSave))
    accel_list.append(wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('I'), PyMapperDialogs.mTilesetEdit))
    accel_list.append(wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('T'), PyMapperDialogs.mTilesetBrowser))
    accel_list.append(wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('Q'), PyMapperDialogs.mFileExit))
    accel_list.append(wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('Z'), PyMapperDialogs.mEditUndo))
    accel_list.append(wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('X'), PyMapperDialogs.mEditCut))
    accel_list.append(wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('C'), PyMapperDialogs.mEditCopy))
    accel_list.append(wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('V'), PyMapperDialogs.mEditPaste))
    accel_list.append(wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('A'), PyMapperDialogs.mEditSelectAll))
    accel_list.append(wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('P'), PyMapperDialogs.mPrintMap))
    accel_list.append(wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('G'), PyMapperDialogs.mViewGrid))
    accel_list.append(wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('F'), PyMapperDialogs.mViewFilterTags))
    accel_list.append(wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('B'), PyMapperDialogs.mViewBackground))
    accel_list.append(wx.AcceleratorEntry(wx.ACCEL_NORMAL, wx.WXK_F1, PyMapperDialogs.mHelpContents))
    accel_list.append(wx.AcceleratorEntry(wx.ACCEL_NORMAL, wx.WXK_F2, PyMapperDialogs.mPrintImage))
    accel_list.append(wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('D'), PyMapperDialogs.mDungeonDiceRoller))
    accel_list.append(wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('W'), PyMapperDialogs.mViewUpdateToFTP))
    accel_list.append(wx.AcceleratorEntry(wx.ACCEL_CTRL, ord('Y'), PyMapperDialogs.mViewUpdateFog))

    self.AccelTable = wx.AcceleratorTable(accel_list)
    self.frame.SetAcceleratorTable(self.AccelTable)
    logging.debug("Accelerators binding complete")

    #toolbar widgets

    self.bmpTQ_Single = wx.Bitmap(os.path.join(gv.artwork_directory,'TQ_single.png'), wx.BITMAP_TYPE_PNG)
    self.bmpTQ_Owned = wx.Bitmap(os.path.join(gv.artwork_directory,'TQ_owned.png'), wx.BITMAP_TYPE_PNG)
    self.bmpTQ_Unlimited = wx.Bitmap(os.path.join(gv.artwork_directory,'TQ_unlimited.png'), wx.BITMAP_TYPE_PNG)

    self.frame.toolbar.EnableTool(PyMapperDialogs.tEditUndo,False)
    self.frame.toolbar.EnableTool(PyMapperDialogs.tShowBackground,False)
    self.frame.toolbar.ToggleTool(PyMapperDialogs.tSnapToGrid,toggle=gv.SnapToGrid)
    self.frame.toolbar.ToggleTool(PyMapperDialogs.tShowFogObjects, toggle=gv.ShowFogObjects)
    

    #right click menu
    if not hasattr(self, "popupID1"):
      #300 series is for the tile right click
      self.popupID301 = wx.Window.NewControlId()
      self.popupID302 = wx.Window.NewControlId()
      self.popupID303 = wx.Window.NewControlId()
      self.Bind(wx.EVT_MENU, self.RTilebookAddPage, id=self.popupID301)
      self.Bind(wx.EVT_MENU, self.RTilebookChangePageName, id=self.popupID302)
      self.Bind(wx.EVT_MENU, self.RTilebookDeletePage, id=self.popupID303)

      #600 series is for the map right click
      self.popupID601 = wx.Window.NewControlId()
      self.popupID602 = wx.Window.NewControlId()
      self.popupID603 = wx.Window.NewControlId()

      self.Bind(wx.EVT_MENU, self.RMapbookAddPage, id=self.popupID601)
      self.Bind(wx.EVT_MENU, self.RMapbookChangePageName, id=self.popupID602)
      self.Bind(wx.EVT_MENU, self.RMapbookDeletePage, id=self.popupID603)
      
      self.popupID1 = wx.Window.NewControlId()
      self.popupID2 = wx.Window.NewControlId()
      self.popupID3 = wx.Window.NewControlId()
      self.popupID4 = wx.Window.NewControlId()
      self.popupID5 = wx.Window.NewControlId()
      self.popupID6 = wx.Window.NewControlId()
      self.popupID7 = wx.Window.NewControlId()
      self.popupID8 = wx.Window.NewControlId()
      self.popupID9 = wx.Window.NewControlId()
      self.popupID10 = wx.Window.NewControlId()
      self.popupID11 = wx.Window.NewControlId()
      self.popupID12 = wx.Window.NewControlId()
      self.popupID13 = wx.Window.NewControlId()
      self.popupID14 = wx.Window.NewControlId()
      self.popupID16 = wx.Window.NewControlId()
      self.popupID17 = wx.Window.NewControlId()  #change highlight submenu
      self.popupID18 = wx.Window.NewControlId()  #copy icon
      
      self.popupID20 = wx.Window.NewControlId() #highlight color submenu
      self.popupID21 = wx.Window.NewControlId()
      self.popupID22 = wx.Window.NewControlId()
      self.popupID23 = wx.Window.NewControlId()
      self.popupID24 = wx.Window.NewControlId()
      
      self.popupID31 = wx.Window.NewControlId()   # Add NPC
      self.popupID32 = wx.Window.NewControlId()   # Add Room Description
      self.popupID33 = wx.Window.NewControlId()   # Add Monster
      self.popupID35 = wx.Window.NewControlId()   # Add Trap
      
      self.popupID200 = wx.Window.NewControlId()
      self.popupID201 = wx.Window.NewControlId()
      self.popupID202 = wx.Window.NewControlId()
      self.popupID203 = wx.Window.NewControlId()
      self.popupID204 = wx.Window.NewControlId()
      self.popupID205 = wx.Window.NewControlId()
      self.popupID206 = wx.Window.NewControlId()
      self.popupID207 = wx.Window.NewControlId()
      self.popupID208 = wx.Window.NewControlId()
      self.popupID209 = wx.Window.NewControlId()
      self.popupID210 = wx.Window.NewControlId()
      self.popupID211 = wx.Window.NewControlId()
      self.popupID212 = wx.Window.NewControlId()
      self.popupID213 = wx.Window.NewControlId()
      self.popupID214 = wx.Window.NewControlId()
      self.popupID215 = wx.Window.NewControlId()
      self.popupID216 = wx.Window.NewControlId()

      self.Bind(wx.EVT_MENU, self.RMapClickZoomIn, id=self.popupID1)
      self.Bind(wx.EVT_MENU, self.RMapClickZoomOut, id=self.popupID2)
      self.Bind(wx.EVT_MENU, self.RMapClickDeleteTile, id=self.popupID3)
      self.Bind(wx.EVT_MENU, self.RMapClickRotateCW, id=self.popupID4)
      self.Bind(wx.EVT_MENU, self.RMapClickRotateCCW, id=self.popupID5)
      self.Bind(wx.EVT_MENU, self.OnViewViewAll, id=self.popupID6) #RMapClickShowAll needs to have DrawMapWindow() called after
      self.Bind(wx.EVT_MENU, self.RMapClickAddText, id=self.popupID7)
      self.Bind(wx.EVT_MENU, self.RMapClickEditTextFontData, id=self.popupID8)
      self.Bind(wx.EVT_MENU, self.RMapClickDisplayUp, id=self.popupID9)
      self.Bind(wx.EVT_MENU, self.RMapClickDisplayTop, id=self.popupID10)
      self.Bind(wx.EVT_MENU, self.RMapClickDisplayDown, id=self.popupID11)
      self.Bind(wx.EVT_MENU, self.RMapClickDisplayBottom, id=self.popupID12)
      self.Bind(wx.EVT_MENU, self.RMapClickRotate180, id=self.popupID13)
      self.Bind(wx.EVT_MENU, self.RMapClickAssignLayer, id=self.popupID14)
      self.Bind(wx.EVT_MENU, self.RMapClickDeleteIcon, id=self.popupID16)
      self.Bind(wx.EVT_MENU, self.RMapClickChangeIconHighlight, id=self.popupID17)
      self.Bind(wx.EVT_MENU, self.RMapClickCopyIcon, id=self.popupID18)

      self.Bind(wx.EVT_MENU, self.RMapClickAddSymbol, id=self.popupID200)

    if not hasattr(self, "popupID51"):
      self.popupID51 = wx.Window.NewControlId()
      self.popupID52 = wx.Window.NewControlId()
      self.popupID53 = wx.Window.NewControlId()
      self.popupID54 = wx.Window.NewControlId()
      self.popupID55 = wx.Window.NewControlId()
      self.popupID56 = wx.Window.NewControlId()
      self.popupID57 = wx.Window.NewControlId()
      self.popupID58 = wx.Window.NewControlId()

      self.Bind(wx.EVT_MENU, self.RTileClickZoomIn, id=self.popupID51)
      self.Bind(wx.EVT_MENU, self.RTileClickZoomOut, id=self.popupID52)
      self.Bind(wx.EVT_MENU, self.RTileClickProperties, id=self.popupID53)
      self.Bind(wx.EVT_MENU, self.RTileClickFilterTile, id=self.popupID54)
      self.Bind(wx.EVT_MENU, self.RTileClickFilterTileset, id=self.popupID55)
      self.Bind(wx.EVT_MENU, self.RTileClickClearFilters, id=self.popupID56)
      self.Bind(wx.EVT_MENU, self.RTileClickFlipAllTiles, id=self.popupID57)
      self.Bind(wx.EVT_MENU, self.RTileClickShowTileOnMap, id=self.popupID58)


    self.frame.MapWindowZoomSlider.SetValue(gv.MapZoomFactor)
    logging.debug("Set map window slider")
    self.frame.TileWindowZoomSlider.SetValue(gv.TileZoomFactor)
    logging.debug("Set tile window slider")

    self.frame.Bind(wx.EVT_SCROLL, self.MapWindowZoom, self.frame.MapWindowZoomSlider)
    self.frame.Bind(wx.EVT_SCROLL_THUMBTRACK, self.MapWindowZoomChanging, self.frame.MapWindowZoomSlider)
    self.frame.Bind(wx.EVT_SCROLL_THUMBRELEASE, self.MapWindowZoomChanged, self.frame.MapWindowZoomSlider)
    
    self.frame.Bind(wx.EVT_SCROLL_THUMBRELEASE, self.TileWindowZoom, self.frame.TileWindowZoomSlider)

    self.frame.Bind(wx.EVT_IDLE, self.OnIdle)

    gv.GridPen = wx.Pen(gv.GridColor, gv.GridPenWidth, gv.GridPenStyle)
    gv.SelectionPen = wx.Pen(gv.SelectionColor, gv.SelectionPenWidth, gv.SelectionPenStyle)
    gv.HighlightPen = wx.Pen(gv.HighlightColor, gv.HighlightPenWidth, gv.HighlightPenStyle)

    self.ReadIniFile()
    self.DrawTileWindow(True)
    logging.debug("Initial DrawTileWindow executed")
    self.DrawMapWindow()
    logging.debug("Initial DrawMapWindow executed")
    self.oldTilePanelSize = self.TilePanel.GetSize() #returns (width, height)

    self.backuptimer = wx.Timer(self.frame, 1)

    self.PrintData = wx.PrintData()
    self.PrintData.SetPaperId(wx.PAPER_LETTER) #default paper size
    self.PageData = wx.PageSetupDialogData(self.PrintData)
    self.PageData.EnableMargins(True)

    if (gv.AutoSave == True):
      self.backuptimer.Start(gv.AutoSaveInterval*1000)
      self.MapStruct.backupfilename = os.path.join(gv.backup_directory,"backup.map")
    else:
      self.MapStruct.backupfilename = None
    return

  def ReadDrawingItems(self, datafile, importFilePageNames):
    """datafile = file object being read
       importFilePageNames = list of page names changed due to duplicate pages during import
    """
    ReadFile = True
    while (ReadFile):
      info = datafile.readline().rstrip(" \n\r").split()
      if (info[0] == 'DRAW_FREEHAND'):
        ReadItem = True
        item = gv.DrawingObject_Record()
        item.tool = 'Freehand'
        while (ReadItem):
          info = datafile.readline().rstrip(" \n\r").split()
          if (info[0] == 'XY_POINT'):
            item.line.append(wx.Point2D(float(info[1]), float(info[2])))
          elif (info[0] == 'LINE_COLOR'):
            pencolor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
          elif (info[0] == 'LINE_WIDTH'):
            width = int(info[1])
          elif (info[0] == 'LINE_STYLE'):
            style = int(info[1])
          elif (info[0] == 'BRUSH_COLOR'):
            brushcolor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
          elif (info[0] == 'PAGE_INDEX'):
            item.page_name = gv.MapPageList[int(info[1])].PageName
          elif (info[0] == 'PAGE_NAME'):
            page = datafile.readline().rstrip("\n\r")
            if (importFilePageNames != []):
              for item in importFilePageNames:
                if (item.importName == page):
                  page = item.importRenamed
                  break
            item.page_name = page
          elif (info[0] == 'FOG_ITEM'):
            item.object_type = 'fog'
          elif (info[0] == 'END_FREEHAND'):
            item.brush = wx.Brush(brushcolor, wx.SOLID)
            item.pen = wx.Pen(pencolor, width, style)
            ReadItem = False
            self.DrawingList.append(item)
      elif (info[0] == 'DRAW_LINE'):
        ReadItem = True
        item = gv.DrawingObject_Record()
        item.tool = 'Line'
        while (ReadItem):
          info = datafile.readline().rstrip(" \n\r").split()
          if (info[0] == 'XY_POINT'):
            item.line.append(wx.Point2D(float(info[1]), float(info[2])))
          elif (info[0] == 'LINE_COLOR'):
            pencolor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
          elif (info[0] == 'LINE_WIDTH'):
            width = int(info[1])
          elif (info[0] == 'LINE_STYLE'):
            style = int(info[1])
          elif (info[0] == 'BRUSH_COLOR'):
            brushcolor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
          elif (info[0] == 'PAGE_INDEX'):  #not used from v9.1 onward
            item.page_name = gv.MapPageList[int(info[1])].PageName
          elif (info[0] == 'PAGE_NAME'):
            page = datafile.readline().rstrip("\n\r")
            if (importFilePageNames != []):
              for item in importFilePageNames:
                if (item.importName == page):
                  page = item.importRenamed
                  break
            item.page_name = page
          elif (info[0] == 'END_LINE'):
            item.brush = wx.Brush(brushcolor, wx.SOLID)
            item.pen = wx.Pen(pencolor, width, style)
            ReadItem = False
            self.DrawingList.append(item)
          elif (info[0] == 'FOG_ITEM'):
            item.object_type = 'fog'
      elif (info[0] == 'DRAW_MULTILINE'):
        ReadItem = True
        item = gv.DrawingObject_Record()
        item.tool = 'Multiline'
        while (ReadItem):
          info = datafile.readline().rstrip(" \n\r").split()
          if (info[0] == 'XY_POINT'):
            item.line.append(wx.Point2D(float(info[1]), float(info[2])))
          elif (info[0] == 'LINE_COLOR'):
            pencolor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
          elif (info[0] == 'LINE_WIDTH'):
            width = int(info[1])
          elif (info[0] == 'LINE_STYLE'):
            style = int(info[1])
          elif (info[0] == 'BRUSH_COLOR'):
            brushcolor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
          elif (info[0] == 'PAGE_INDEX'):
            item.page_name = gv.MapPageList[int(info[1])].PageName
          elif (info[0] == 'PAGE_NAME'):
            page = datafile.readline().rstrip("\n\r")
            if (importFilePageNames != []):
              for item in importFilePageNames:
                if (item.importName == page):
                  page = item.importRenamed
                  break
            item.page_name = page
          elif (info[0] == 'END_MULTILINE'):
            item.brush = wx.Brush(brushcolor, wx.SOLID)
            item.pen = wx.Pen(pencolor, width, style)
            ReadItem = False
            self.DrawingList.append(item)
          elif (info[0] == 'FOG_ITEM'):
            item.object_type = 'fog'
      elif (info[0] == 'DRAW_OUTLINE_RECT'):
        ReadItem = True
        item = gv.DrawingObject_Record()
        item.tool = 'OutlineRect'
        while (ReadItem):
          info = datafile.readline().rstrip(" \n\r").split()
          if (info[0] == 'RECT'):
            item.rect = wx.Rect2D(float(info[1]), float(info[2]), float(info[3]), float(info[4]))
          elif (info[0] == 'LINE_COLOR'):
            pencolor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
          elif (info[0] == 'LINE_WIDTH'):
            width = int(info[1])
          elif (info[0] == 'LINE_STYLE'):
            style = int(info[1])
          elif (info[0] == 'BRUSH_COLOR'):
            brushcolor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
          elif (info[0] == 'PAGE_INDEX'):
            item.page_name = gv.MapPageList[int(info[1])].PageName
          elif (info[0] == 'PAGE_NAME'):
            page = datafile.readline().rstrip("\n\r")
            if (importFilePageNames != []):
              for item in importFilePageNames:
                if (item.importName == page):
                  page = item.importRenamed
                  break
              item.page_name = page
          elif (info[0] == 'END_OUTLINE_RECT'):
            item.brush = wx.Brush(brushcolor, wx.SOLID)
            item.pen = wx.Pen(pencolor, width, style)
            ReadItem = False
            self.DrawingList.append(item)
          elif (info[0] == 'FOG_ITEM'):
            item.object_type = 'fog'
      elif (info[0] == 'DRAW_FILL_RECT'):
        ReadItem = True
        item = gv.DrawingObject_Record()
        item.tool = 'FillRect'
        while (ReadItem):
          info = datafile.readline().rstrip(" \n\r").split()
          if (info[0] == 'RECT'):
            item.rect = wx.Rect2D(float(info[1]), float(info[2]), float(info[3]), float(info[4]))
          elif (info[0] == 'LINE_COLOR'):
            pencolor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
          elif (info[0] == 'LINE_WIDTH'):
            width = int(info[1])
          elif (info[0] == 'LINE_STYLE'):
            style = int(info[1])
          elif (info[0] == 'BRUSH_COLOR'):
            brushcolor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
          elif (info[0] == 'PAGE_INDEX'):
            item.page_name = gv.MapPageList[int(info[1])].PageName
          elif (info[0] == 'PAGE_NAME'):
            page = datafile.readline().rstrip("\n\r")
            if (importFilePageNames != []):
              for item in importFilePageNames:
                if (item.importName == page):
                  page = item.importRenamed
                  break
            item.page_name = page
          elif (info[0] == 'END_FILL_RECT'):
            item.brush = wx.Brush(brushcolor, wx.SOLID)
            item.pen = wx.Pen(pencolor, width, style)
            ReadItem = False
            self.DrawingList.append(item)
          elif (info[0] == 'FOG_ITEM'):
            item.object_type = 'fog'
      elif (info[0] == 'DRAW_OUTLINE_CIRCLE'):
        ReadItem = True
        item = gv.DrawingObject_Record()
        item.tool = 'OutlineCircle'
        while (ReadItem):
          info = datafile.readline().rstrip(" \n\r").split()
          if (info[0] == 'CIRCLE'):
            item.circle.append(wx.Point2D(float(info[1]), float(info[2])))
            item.circle.append(float(info[3]))
          elif (info[0] == 'LINE_COLOR'):
            pencolor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
          elif (info[0] == 'LINE_WIDTH'):
            width = int(info[1])
          elif (info[0] == 'LINE_STYLE'):
            style = int(info[1])
          elif (info[0] == 'BRUSH_COLOR'):
            brushcolor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
          elif (info[0] == 'PAGE_INDEX'):
            index = int(info[1])
            if (importFilePageNames != []):
              item.page_name = importFilePageNames[index].importRenamed
            else:
              item.page_name = gv.MapPageList[index].PageName
          elif (info[0] == 'PAGE_NAME'):
            page = datafile.readline().rstrip("\n\r")
            if (importFilePageNames != []):
              for item in importFilePageNames:
                if (item.importName == page):
                  page = item.importRenamed
                  break
            item.page_name = page
          elif (info[0] == 'END_OUTLINE_CIRCLE'):
            item.brush = wx.Brush(brushcolor, wx.SOLID)
            item.pen = wx.Pen(pencolor, width, style)
            ReadItem = False
            self.DrawingList.append(item)
          elif (info[0] == 'FOG_ITEM'):
            item.object_type = 'fog'
      elif (info[0] == 'DRAW_FILLED_CIRCLE'):
        ReadItem = True
        item = gv.DrawingObject_Record()
        item.tool = 'FillCircle'
        while (ReadItem):
          info = datafile.readline().rstrip(" \n\r").split()
          if (info[0] == 'CIRCLE'):
            item.circle.append(wx.Point2D(float(info[1]), float(info[2])))
            item.circle.append(float(info[3]))
          elif (info[0] == 'LINE_COLOR'):
            pencolor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
          elif (info[0] == 'LINE_WIDTH'):
            width = int(info[1])
          elif (info[0] == 'LINE_STYLE'):
            style = int(info[1])
          elif (info[0] == 'BRUSH_COLOR'):
            brushcolor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
          elif (info[0] == 'PAGE_INDEX'):
            item.page_name = gv.MapPageList[int(info[1])].PageName
          elif (info[0] == 'PAGE_NAME'):
            page = datafile.readline().rstrip("\n\r")
            if (importFilePageNames != []):
              for item in importFilePageNames:
                if (item.importName == page):
                  page = item.importRenamed
                  break
            item.page_name = page
          elif (info[0] == 'END_FILLED_CIRCLE'):
            item.brush = wx.Brush(brushcolor, wx.SOLID)
            item.pen = wx.Pen(pencolor, width, style)
            ReadItem = False
            self.DrawingList.append(item)
          elif (info[0] == 'FOG_ITEM'):
            item.object_type = 'fog'
      elif (info[0] == 'DRAW_IMAGE'):
        ReadItem = True
        item = gv.DrawingObject_Record()
        item.tool = 'Image'
        while (ReadItem):
          info = datafile.readline().rstrip(" \n\r").split()
          if (info[0] == 'RECT'):
            item.rect = wx.Rect2D(float(info[1]), float(info[2]), float(info[3]), float(info[4]))
          elif (info[0] == 'IMAGE_FILENAME'):
            filename = datafile.readline().rstrip("\n\r")
          elif (info[0] == 'IMAGE_PATH'):
            filepath = datafile.readline().rstrip("\n\r")
          elif (info[0] == 'PAGE_INDEX'):
            item.page_name = gv.MapPageList[int(info[1])].PageName
          elif (info[0] == 'PAGE_NAME'):
            page = datafile.readline().rstrip("\n\r")
            if (importFilePageNames != []):
              for item in importFilePageNames:
                if (item.importName == page):
                  page = item.importRenamed
                  break
            item.page_name = page
          elif (info[0] == 'END_IMAGE'):
            path = os.getcwd()
            foundpath = path+filename
            if (not os.access(foundpath, os.F_OK)):
              foundpath = filepath+filename
              if (not os.access(foundpath, os.F_OK)):
                caption = "Cannot locate "+filename
                dlg = wx.FileDialog(self.frame, caption , wildcard=images_wildcard, style=wx.OPEN)
                if (dlg.ShowModal() == wx.ID_OK):
                  filename = dlg.GetFilename()
                  filepath = dlg.GetDirectory()
                  dlg.Destroy()
            item.image_filename = filename
            item.image_path = filepath
            item.image = wx.Image((filepath+filename), wx.BITMAP_TYPE_ANY)
            if (not item.image.IsOk()):
              item.image = self.ImageNotFound
            ReadItem = False
            self.DrawingList.append(item)
      elif (info[0] == 'END_DRAWING_ITEMS'):
        ReadFile = False
    return

  def OnIconize(self, event):
    self.IsIcon = event.Iconized()
    if (gv.hoverDlg):
      self.DisplayHoverInformation(False)
    event.Skip()
    return

  def BindTilePanel(self, app, panel):
    panel.Bind(wx.EVT_CONTEXT_MENU, app.OnTileRightClick)
    panel.Bind(wx.EVT_LEFT_DCLICK, app.TileWindowDClick, panel)
    panel.Bind(wx.EVT_CHAR, app.OnKeyboardEvent)
    panel.Bind(wx.EVT_LEFT_DOWN, app.TileWindowLClickDown, panel)
    panel.Bind(wx.EVT_PAINT, app.OnPaint)
    panel.Bind(wx.EVT_LEAVE_WINDOW, app.OnTilePanelLeave)
    panel.Bind(wx.EVT_MOTION, app.OnTilePanelMotion)
    return

  def BindMapPanel(self, app, panel):
    panel.Bind(wx.EVT_CONTEXT_MENU, app.OnMapRightClick)  #EVT_CONTEXT_MENU
    panel.Bind(wx.EVT_LEFT_DCLICK, app.MapWindowDClick, panel)
    panel.Bind(wx.EVT_LEFT_UP, app.MapWindowLClickUp, panel)
    panel.Bind(wx.EVT_LEFT_DOWN, app.MapWindowLClickDown, panel)
    panel.Bind(wx.EVT_MIDDLE_UP, app.MapWindowCenterClickUp, panel)
    panel.Bind(wx.EVT_MIDDLE_DOWN, app.MapWindowCenterClickDown, panel)
    panel.Bind(wx.EVT_MOUSEWHEEL, app.MapWindowMouseWheel, panel)

    panel.Bind(wx.EVT_SCROLLWIN_BOTTOM, app.ScrollMapPanelBottom)
    panel.Bind(wx.EVT_SCROLLWIN_LINEUP, app.ScrollMapPanelLineup)
    panel.Bind(wx.EVT_SCROLLWIN_LINEDOWN, app.ScrollMapPanelLinedown)
    panel.Bind(wx.EVT_SCROLLWIN_PAGEUP, app.ScrollMapPanelPageup)
    panel.Bind(wx.EVT_SCROLLWIN_PAGEDOWN, app.ScrollMapPanelPagedown)
    panel.Bind(wx.EVT_SCROLLWIN_THUMBTRACK, app.ScrollMapPanelThumbtrack)
    panel.Bind(wx.EVT_SCROLLWIN_THUMBRELEASE, app.ScrollMapPanelThumbrelease)

    panel.Bind(wx.EVT_CHAR, app.OnKeyboardEvent)
    panel.Bind(wx.EVT_PAINT, app.OnPaint)
    panel.Bind(wx.EVT_LEAVE_WINDOW, app.OnMapPanelLeave)
    panel.Bind(wx.EVT_MOTION, app.OnMapPanelMotion)
    return

  def OnHelp_ShowTips(self, event=None):
    logging.debug("Show tips")
    filename = os.path.join(gv.root_directory,"tips.txt")
    tipProvider = wx.CreateFileTipProvider(filename, gv.LastTip)
    gv.ShowTips = wx.ShowTip(self.frame, tipProvider)
    gv.LastTip = tipProvider.GetCurrentTip()
    return

  def OnMaximize(self, event):
    self.IsIcon = False
    return

  def ChangeTileNotebookPage(self, event=None):
    for tile in self.tilelist:
      tile.selected = False
    self.TilePanel = gv.TilePanelList[event.GetSelection()]
    self.DrawTileWindow(True)
    return

  def ChangeMapNotebookPage(self, event=None):
    #page = Page_Record()
    found = False

    for tile in self.selectlist:
      tile.selected = False
    self.selectlist = []

    for page in gv.MapPageList:
      if (event.GetOldSelection() == page.PageID): #set values for the old page
        page.ZoomFactor = gv.MapZoomFactor
        page.ShowGrid = gv.DisplayGrid
        page.ShowIconNames = gv.ShowIconNamesOnMap
        (x,y) = self.MapPanel.GetViewStart()
        page.Xscroll = x
        page.Yscroll = y
        page.PageName = self.nbMapNotebook.GetPageText(page.PageID)
        break

    for page in gv.MapPageList:  #set values for the newly selected page
      if (event.GetSelection() == page.PageID):
        gv.MapZoomFactor = page.ZoomFactor
        gv.DisplayGrid = page.ShowGrid
        gv.ShowIconNamesOnMap = page.ShowIconNames
        self.frame.menubar.Check(id=PyMapperDialogs.mViewGrid, check=gv.DisplayGrid)
        self.frame.toolbar.ToggleTool(id=PyMapperDialogs.tShowGrid, toggle=gv.DisplayGrid)
        self.frame.menubar.Check(id=PyMapperDialogs.mShowIconNamesOnMap, check=gv.ShowIconNamesOnMap)
        self.frame.toolbar.ToggleTool(id=PyMapperDialogs.tShowLabels, toggle=gv.ShowIconNamesOnMap)
        self.MapPanel = gv.MapPanelList[page.PageID]
        self.MapPanel.Scroll(page.Xscroll, page.Yscroll)
        for tile in self.maplist:
          if (tile.page == page.PageName):
            tile.GenerateMapDisplay(gv.MapZoomFactor)
        found = True
        break
    if (not found):
      index = self.nbMapNotebook.GetSelection()
      newpage = Page_Record(index,25, 0, 0, self.nbMapNotebook.GetPageText(index))
      gv.DisplayGrid = page.ShowGrid
      gv.ShowIconNamesOnMap = page.ShowIconNames
      self.frame.menubar.Check(id=PyMapperDialogs.mViewGrid, check=gv.DisplayGrid)
      self.frame.toolbar.ToggleTool(id=PyMapperDialogs.tShowGrid, toggle=gv.DisplayGrid)
      self.frame.menubar.Check(id=PyMapperDialogs.mShowIconNamesOnMap, check=gv.ShowIconNamesOnMap)
      self.frame.toolbar.ToggleTool(id=PyMapperDialogs.tShowLabels, toggle=gv.ShowIconNamesOnMap)
      gv.MapPageList.append(newpage)
      self.MapPanel = gv.MapPanelList[index]
      
    self.UpdateTileQuantity(page.PageName)
    self.DrawMapWindow()
    return

  def OnRightClickTileNotebook(self, evt):
    menu = wx.Menu()
    item = wx.MenuItem(menu, self.popupID301,"Add Page")
    item2 = wx.MenuItem(menu, self.popupID302,"Rename Current Page")
    item3 = wx.MenuItem(menu, self.popupID303,"Delete Current Page")
    bmp1 = wx.Bitmap(os.path.join(gv.artwork_directory,"add_page.png"), wx.BITMAP_TYPE_PNG)
    bmp2 = wx.Bitmap(os.path.join(gv.artwork_directory,"rename_icon.png"), wx.BITMAP_TYPE_PNG)
    bmp3 = wx.Bitmap(os.path.join(gv.artwork_directory,"DeleteIcon.png"), wx.BITMAP_TYPE_PNG)
    item.SetBitmap(bmp1)
    item2.SetBitmap(bmp2)
    item3.SetBitmap(bmp3)
    menu.AppendItem(item)
    menu.AppendItem(item2)
    if (self.nbTileNotebook.GetPageCount() > 1):
      menu.AppendItem(item3)

    self.nbTileNotebook.PopupMenu(menu)
    menu.Destroy()
    return

  def OnRightClickMapNotebook(self, evt):
    menu = wx.Menu()
    item = wx.MenuItem(menu, self.popupID601,"Add Page")
    item2 = wx.MenuItem(menu, self.popupID602,"Rename Current Page")
    item3 = wx.MenuItem(menu, self.popupID603,"Delete Current Page")
    bmp1 = wx.Bitmap(os.path.join(gv.artwork_directory,"add_page.png"), wx.BITMAP_TYPE_PNG)
    bmp2 = wx.Bitmap(os.path.join(gv.artwork_directory,"rename_icon.png"), wx.BITMAP_TYPE_PNG)
    bmp3 = wx.Bitmap(os.path.join(gv.artwork_directory,"DeleteIcon.png"), wx.BITMAP_TYPE_PNG)
    item.SetBitmap(bmp1)
    item2.SetBitmap(bmp2)
    item3.SetBitmap(bmp3)
    menu.AppendItem(item)
    menu.AppendItem(item2)
    if (self.nbMapNotebook.GetPageCount() > 1):
      menu.AppendItem(item3)
      
    self.nbMapNotebook.PopupMenu(menu)
    menu.Destroy()
    return

  def RMapbookAddPage(self, event=None, name=None, new_page=None):
    if (name == None):  #creating page from a right-click event
      dlg = wx.TextEntryDialog(self.frame, "Name:", "Enter Page Name")
      result = dlg.ShowModal()
      if (result == wx.ID_OK):
        name = dlg.GetValue()
        if (name == ''):
          wx.MessageBox(message="Pages must have a unique name.",
                        caption="Whoa!", style=wx.ICON_EXCLAMATION)
          return
        for page in gv.MapPageList:
          if (page.PageName == name):
            wx.MessageBox(message="PyMapper cannot have pages with duplicate names.",
                          caption="Whoa!", style=wx.ICON_EXCLAMATION)
            return
        dlg.Destroy()
      else:  #Cancel page creation
        dlg.Destroy()
        return
    panel = wx.ScrolledWindow(self.nbMapNotebook, id=wx.Window.NewControlId(), pos=gv.MapPanelPosition)
    self.BindMapPanel(self, panel)
    page_index = len(gv.MapPageList)
    if (new_page): #Page_Record created during reading of map file
      gv.MapPageList.append(new_page)
    else:  #we need to create a new default value page
      page = Page_Record(page=page_index, zoom=25, x=0, y=0, name=name)
      gv.MapPageList.append(page)
    gv.MapPanelList.append(panel)
    self.nbMapNotebook.AddPage(panel, name)
    self.DrawMapWindow()
    return

  def RMapbookDeletePage(self, event):
    index = self.nbMapNotebook.GetSelection()
    pagename = self.nbMapNotebook.GetPageText(index)
    tile = Tile()
    delete_list = []
    for tile in self.maplist:
      if (tile.page == pagename):
        delete_list.append(tile)
    for tile in delete_list:
      self.DeleteMapTile(tile)

    self.UndoActionEvent(flag='DELETE_MAP_PAGE', text=pagename)
    self.nbMapNotebook.SetSelection(0)
    self.nbMapNotebook.DeletePage(index)

    gv.MapPanelList.pop(index)
    gv.MapPageList.pop(index)
    self.MapPanel = gv.MapPanelList[0]
    self.DrawMapWindow()
    return

  def RMapbookChangePageName(self, event):
    old_name = self.nbMapNotebook.GetPageText(self.nbMapNotebook.GetSelection())
    dlg = wx.TextEntryDialog(self.frame, "Name:", "Enter Page Name")
    dlg.SetValue(old_name)
    result = dlg.ShowModal()
    if (result == wx.ID_OK):
      name = dlg.GetValue()
      for page in gv.MapPageList:
        if (page.PageName == name):
          wx.MessageBox(message="PyMapper cannot have pages with duplicate names.",
                        caption="Whoa!", style=wx.ICON_EXCLAMATION)
          return
      for page in gv.MapPageList:
        if (page.PageName == old_name):
          page.PageName = name
          break
      self.nbMapNotebook.SetPageText(self.nbMapNotebook.GetSelection(),name)
      for tile in self.maplist:
        if (tile.page == old_name):
          tile.page = name
      for text in self.textlist:
        if (text.page == old_name):
          text.page = name
      for icon in gv.RoomList:
        if (icon.page == old_name):
          icon.page = name
      for draw in self.DrawingList:
        if (draw.page_name == old_name):
          draw.page_name = name
    dlg.Destroy()
    return

  def RTilebookChangePageName(self, event):
    dlg = wx.TextEntryDialog(self.frame, "Name:", "Enter New Page Name")
    result = dlg.ShowModal()
    if (result == wx.ID_OK):
      name = dlg.GetValue()
      for page in gv.TilePageList:
        if (page.PageName == name):
          wx.MessageBox(message="PyMapper cannot have pages with duplicate names.",
                        caption="Whoa!", style=wx.ICON_EXCLAMATION)
          return
      old_name = self.nbTileNotebook.GetPageText(self.nbTileNotebook.GetSelection())
      for page in gv.TilePageList:
        if (page.PageName == old_name):
          page.PageName = name
          break
      self.nbTileNotebook.SetPageText(self.nbTileNotebook.GetSelection(),name)
    dlg.Destroy()
    return

  def RTilebookAddPage(self, event=None, name=None):
    if (name == None):
      dlg = wx.TextEntryDialog(self.frame, "Name:", "Enter Page Name")
      result = dlg.ShowModal()
      if (result == wx.ID_OK):
        name = dlg.GetValue()
        if (name == ''):
          wx.MessageBox(message="Pages must have a name.",
                        caption="Whoa!", style=wx.ICON_EXCLAMATION)
          return
        for page in gv.TilePageList:
          if (page.PageName == name):
            wx.MessageBox(message="PyMapper cannot have pages with duplicate names.",
                          caption="Whoa!", style=wx.ICON_EXCLAMATION)
            return
        dlg.Destroy()
      else:
        dlg.Destroy()
        return
    else:
      for page in gv.TilePageList:
        if (page.PageName == name):
          return
    page = Page_Record(self.nbTileNotebook.GetSelection(),gv.TileZoomFactor,0,0,name)
    panel = wx.ScrolledWindow(self.nbTileNotebook, id=wx.Window.NewControlId())
    panel.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
    self.BindTilePanel(self, panel)
    gv.TilePanelList.append(panel)
    gv.TilePageList.append(page)
    self.nbTileNotebook.AddPage(panel, name)
    self.DrawTileWindow()
    return
  
  def RTilebookDeletePage(self, event=None):
    index = self.nbTileNotebook.GetSelection()
    pagename = self.nbTileNotebook.GetPageText(index)
    tile = Tile()
    delete_list = []
    self.UndoActionEvent(flag='DELETE_TILE_PAGE', text=pagename)
    self.nbTileNotebook.SetSelection(0)
    self.nbTileNotebook.DeletePage(index)
    gv.TilePageList.pop(index)
    gv.TilePanelList.pop(index)
    self.TilePanel = gv.TilePanelList[0]
    self.DrawTileWindow()
    return

  def OnDungeon_Traps(self, evt):
    dlg = TrapsDialog(self.frame)
    if (gv.TrapDialogPosition):
      dlg.Move(gv.TrapDialogPosition)
    dlg.ShowModal()
    dlg.Destroy()
    return

  def OnDungeon_Monsters(self, event):
    dlg = MonstersDialog(self.frame)
    dlg.ShowModal()
    return
  
  def OnDungeon_5EMonsters(self, event):
    dlg = Monsters5EDialog(self.frame, '5E')  #this is for a monster record
    dlg.ShowModal()
    return
  
  def OnDungeon_5E_NPC(self, event):
    dlg = Monsters5EDialog(self.frame, '5E_NPC')  #this is for an NPC
    dlg.ShowModal()
    return
  
  def OnDungeon_5E_Spells(self, event):
    dlg = Spells5EDialogCore(self.frame)
    dlg.ShowModal()
    return

  def OnDungeon_Treasures(self, event):
    dlg = TreasuresDialog(self.frame, add_icon=True)
    dlg.ShowModal()
    return

  def OnDungeon_Encounters(self, evt):
    dlg = DungeonEncounterDesignDialog(self.frame)
    value = dlg.Show(True)
    return

  def OnDungeon_DiceRoller(self, evt):
    dlg = DiceRollDialog(self.frame)
    result = dlg.Show(True)
    return

  def OnDungeon_CombatTracking(self, event):
    dlg = CombatTrackingDialog(self.frame)
    dlg.Show(True)
    return

  def OnDungeon_NPCgenerator(self, evt):
    dlg = NPC_GeneratorDialog(self.frame)
    result = dlg.ShowModal()
    return

  def OnDungeon_Pathfinder_MagicItems(self, evt):
    logging.info("OnMenu_Dungeon_Pathfinder_MagicItems()")
    return

  def OnDungeon_Pathfinder_Monsters(self, evt):
    logging.info("OnMenu_Dungeon_Pathfinder_Monsters()")
    return
  
  def OnDungeon_Load_DnD5_Resources(self, evt=None):
    dlg = SRD_Progress_Dialog(self.frame, 'DnD5')
    dlg.Show(True)
    dlg.Update()
    result = srd.ReadDnD5_Files(dlg.gSpellsGauge, dlg.gMonsterGauge, dlg.gRacesGauge, dlg.gTrapsGauge)
    dlg.Destroy()
    
    if (result == 'Files Loaded'):
      gv.DnD_5E_data_available = True
      logging.info("DnD5 Resources loaded successfully")
      self.frame.menubar.Enable(PyMapperDialogs.mDungeonLoadDnD5Files, False)
      self.frame.menubar.Enable(PyMapperDialogs.mDungeonMonster5E, True)
      self.frame.menubar.Enable(PyMapperDialogs.mDungeonNPC_5E, True)
      self.frame.menubar.Enable(PyMapperDialogs.mDungeonSpell_5E, True)
      self.frame.menubar.Enable(PyMapperDialogs.mDungeonTraps, True)
    else:
      gv.DnD_5E_data_available = False
      wx.MessageBox("Error loading some resources: %s" % result)
      logging.error("Error loading DnD5 resources: %s" % result)
    return

  def OnDungeon_Load_d20_Resources(self, event=None, pos=None):
    logging.debug("Begin loading d20 Resources")
    SRD_Dialog = SRD_Progress_Dialog(self.frame, 'PFd20')
    if (pos):
      offset_pt = wx.Point(pos.GetX()+pos.GetWidth(), pos.GetY())
      SRD_Dialog.Move(offset_pt)
    SRD_Dialog.Show(True)
    SRD_Dialog.Update()
    srd.ReadD20_Files(SRD_Dialog.gTrapsGauge, SRD_Dialog.gMonsterGauge, SRD_Dialog.gSpellsGauge, SRD_Dialog.gFeatsGauge,
                      SRD_Dialog.gClassSkillsGauge, SRD_Dialog.gClassTableGauge, SRD_Dialog.gNamesGauge, SRD_Dialog.gRacesGauge,
                      SRD_Dialog.gRacialBonusesGauge)
    SRD_Dialog.Show(False)
    SRD_Dialog.Destroy()
    if (False):  #This is here for the conversion of the monster database to calc hit points
      for monster in gv.MonsterList:
        if (not monster.version):
          info = monster.HD.split()
          monster.HP = self.RollDice(info[0])
          gv.SaveSRD_Monsters = True
      
    self.frame.menubar.Enable(PyMapperDialogs.mDungeonLoadD20Files, False)
    if (gv.PymapperUser):  #disable for non-pymapper user while this feature in development
      self.frame.menubar.Enable(PyMapperDialogs.mDungeonEncounters, True)
    self.frame.menubar.Enable(PyMapperDialogs.mDungeonNPCGenerator, True)
    self.frame.menubar.Enable(PyMapperDialogs.mDungeonTraps, True)
    self.frame.menubar.Enable(PyMapperDialogs.mDungeonMonster, True)
    self.frame.menubar.Enable(PyMapperDialogs.mDungeonTreasures, True)

    
    gv.d20_SRD_data_available = True
    logging.debug("End loading d20 resources")
    return

  def OnDungeon_d20Spells(self, evt):
    logging.info("OnMenu_Dungeon_d20Spells()")
    return

  def OnDungeon_d20Feats(self, evt):
    logging.info("OnMenu_Dungeon_d20Feats()")
    return

  def OnDungeon_About(self, evt):
    description = """The d20 information presented in PyMapper is provided under version 1.0a of \nthe Open Game License provided by Wizards of the Coast.  \nA copy of this license is available in the /srd/ folder where pymapper \nis installed, and also at Wizards of the Coast."""
    licence = """Open Game License 1.0a"""
    info = wx.AboutDialogInfo()
    temp1 = os.path.join(gv.srd_directory,'d20')
    d20_logo_path = os.path.join(temp1,'D20_logo.png')
    info.SetIcon(wx.Icon(d20_logo_path, wx.BITMAP_TYPE_PNG))
    info.SetName('System Reference Document')
    info.SetVersion('1.0a')
    info.SetDescription(description)
    info.SetCopyright('(C)Copyright 2000 Wizards of the Coast')
    info.SetWebSite('http://www.wizards.com/default.asp?x=d20/article/srdarchive')
    info.SetLicence(licence)
    wx.AboutBox(info)
    return

  def OnDungeon_ShowIcons(self, evt):
    gv.ShowIcons = self.frame.menubar.IsChecked(PyMapperDialogs.mDungeonShowIcons)
    self.DrawMapWindow()
    return

  def OnOptionsText(self, event):
    dlg = TextOptionsDialogCore(self.frame, True, None)
    if (dlg.ShowModal() == True):
      gv.TextBackgroundColor = dlg.BackgroundColor
      gv.TextForegroundColor = dlg.ForegroundColor
      gv.FontData = dlg.FontData
      gv.TextFont = dlg.TextFont
      gv.OpaqueBackground = dlg.rbOpaque.GetValue()
      if (dlg.rbTransparentBackground.GetValue() == True):
        gv.TextBackgroundColor.Alpha == 0
      else:
        gv.TextBackgroundColor.Alpha == 255
      gv.OutlineText = dlg.rbOutlineOn.GetValue()
      if (dlg.bApplyGlobal.GetValue() == True):
        for label in self.textlist:
          label.font = gv.TextFont
          label.fg = gv.TextForegroundColor
          label.bg = gv.TextBackgroundColor
          label.font = gv.TextFont
          #label.fontdata = gv.FontData
          label.opaque = gv.OpaqueBackground
          label = self.CreateTextLabelBitmap(label, gv.MapZoomFactor)
      self.DrawMapWindow()

  def CreateTextLabelBitmap(self, label, resolution):
    """
      CreateTextLableBitmap(self, label, resolution)
        label = Annotation()
        resolution = print or map zoom resolution

        Creates the text label bitmap from an existing Annotation()

    """
    memdc = wx.MemoryDC()
    if (not memdc.IsOk()):
      label.bmp = wx.BitmapFromImage(self.ImageNotFound)
      return label
    memdc.SetMapMode(wx.MM_TEXT)
    memdc.SetFont(label.font)
    (print_width, print_height) = memdc.GetTextExtent(label.text)
    gamma = print_height/(1.0*label.font.GetPointSize())
    alpha = (label.font.GetPointSize()*resolution)/72.0
    print_size = label.font.GetPointSize()
    label.font.SetPointSize(int(alpha/gamma))
    memdc.SetFont(label.font)
    (width, height) = memdc.GetTextExtent(label.text)
    label.font.SetPointSize(print_size)
    label.bmp = wx.Bitmap(width, height)
    memdc.SelectObject(label.bmp)
    memdc.SetBackground(wx.Brush(label.bg, wx.SOLID))
    label.zoomfactor = resolution
    label.extent = wx.Rect2D((label.x*resolution), (label.y*resolution), width, height)  #changed from wxRect to wxRect2D
    memdc.Clear()
    memdc.SetTextForeground(label.fg)
    memdc.DrawText(label.text, 0, 0)
    memdc.SelectObject(wx.NullBitmap)
    if (not label.opaque):
      mask = wx.Mask(label.bmp, label.bg)
      label.bmp.SetMask(mask)
    if (not label.bmp.IsOk()):
      logging.error("Could not create annotation bitmap")
    return label #returns an Annotation()

  def OnRestore(self, event):
    return

  def OnOptionsTilesets(self, event=None):
    setlist = []
    for item in gv.tilesets:
      if (item.loaded):
        setlist.append(item)
    dlg = TilesetPageManagerDialog(self.frame, setlist, gv.TilePageList)
    result = dlg.ShowModal()
    if (result == True):
      #adjust to number of pages
      temp_index = 0
      while (len(gv.TilePageList) < len(dlg.pagelistdata)):
        #add pages
        pagename = 'TempPageName'+str(temp_index)
        self.RTilebookAddPage(name=pagename)
        temp_index += 1
      while (len(gv.TilePageList) > len(dlg.pagelistdata)):
        #delete pages
        self.RTilebookDeletePage()

      page = Page_Record()
      dlg_page = Page_Record()
      for page in gv.TilePageList:
        for dlg_page in dlg.pagelistdata:
          if (dlg_page.PageName == page.PageName):
            page.tilesets = copy.deepcopy(dlg_page.tilesets)
      self.DrawTileWindow(True)
    dlg.Destroy()
    return

  def OutlineTiles(self, event):
    gv.OutlineTiles = self.frame.menubar.IsChecked(id=PyMapperDialogs.mViewOutlineTiles)
    self.DrawMapWindow()
    return

  def OnMapsIsometric(self, event):
    if (gv.IsometricViewer):
      gv.IsometricViewer.Show(True)
    else:
      gv.IsometricViewer = IsometricMapDialog(self.frame)
      gv.IsometricViewer.Show(True)
      gv.DrawMapDiagonals = True
    return

  def OnMapsRandomDungeon(self, event):
    dlg = RandomGeomorphDungeonDialog(self.frame, app.res)
    dlg.ShowModal()
    return

  def OnOptionsSymbolsMarkers(self, event):
    dlg = SymbolMarkerManagerDialog(self.frame, self.SymbolList, self.MarkerList)
    result = dlg.ShowModal()
    if (result):
      self.SymbolList = dlg.symbol_list
      self.MarkerList = dlg.marker_list
      #update any markers in the tilelist that may have been changed.
      new_markers_list = []  #add these to self.tilelist after checking everything

      for marker in self.MarkerList:
        found_match = False
        for tile in self.tilelist:
          if (marker.key_index == tile.key_index):
            #these markers are already present in the list
            found_match = True
            tile.area = marker.size * marker.size
            tile.sideA = marker.image
            tile.sideB = marker.image
            tile.tiledisplay = marker.image
            tile.actualXsize = marker.size
            tile.actualYsize = marker.size
            break
        for maptile in self.maplist:
          if (marker.key_index == maptile.key_index):
            #these markers are already present in the list
            found_match = True
            maptile.area = marker.size * marker.size
            maptile.sideA = marker.image
            maptile.sideB = marker.image
            maptile.tiledisplay = marker.image
            maptile.actualXsize = marker.size
            maptile.actualYsize = marker.size
            maptile.MapRect.width = marker.size
            maptile.MapRect.height = marker.size
            break
        if (not found_match):
          #new marker, add to the tilelist
          newtile = Tile()
          newtile.key_index = gv.key_index
          gv.key_index += 1
          newtile.area = marker.size * marker.size
          newtile.sideA = marker.image
          newtile.sideB = marker.image
          newtile.tiledisplay = marker.image
          newtile.actualXsize = marker.size
          newtile.actualYsize = marker.size
          newtile.copies = 99
          newtile.index = marker.index
          newtile.layer = 0
          newtile.page = 'Markers'
          newtile.tilesetID = 'MARKERS'
          newtile.tilesetName = 'Markers'
          newtile.tileID = newtile.key_index
          newtile.shown = True
          new_markers_list.append(newtile)

      for new_marker in new_markers_list:
        self.tilelist.append(new_marker)
    index = 0
    for symbol in self.SymbolList:
      if (symbol.key_index == None):
        #add another symbol to the tilelist
        newtile = Tile()
        newtile.key_index = gv.key_index
        symbol.key_index = gv.key_index
        gv.key_index += 1
        newtile.area = symbol.xsize * symbol.ysize
        newtile.sideA = symbol.image
        newtile.sideB = symbol.image
        newtile.tiledisplay = symbol.image
        newtile.actualXsize = symbol.xsize
        newtile.actualYsize = symbol.ysize
        newtile.copies = 99
        newtile.index = index
        index += 1
        newtile.layer = 0
        newtile.page = 'Symbols'
        newtile.tilesetID = 'SYMBOLS'
        newtile.tilesetName = 'Symbols'
        newtile.tileID = index
        newtile.shown = True
        self.tilelist.append(newtile)
    for symbol in dlg.removed_symbols:
      for tile in self.tilelist:
        if (symbol.key_index == tile.key_index):
          self.tilelist.remove(tile)
          break

    dlg.Destroy()
    self.DrawTileWindow(True)
    self.DrawMapWindow()
    return

  def LoadSymbolFiles(self, ResizeFiles=False):
    """Load all symbol image files located in the root/artwork/symbols folder.
       Also load files from the symbols.ini file, if any
    """
    symbol_count = 0  #how many symbols have we loaded?
    symbol_path = os.path.join(gv.artwork_directory,"symbols")
    
    if (os.access(symbol_path, os.F_OK)):
      #check for png format files
      os.chdir(symbol_path)
      png_files = glob.glob('*.png')
      for filename in png_files:
        sym = SymbolRecord(filename, symbol_path)
        sym.image = wx.Image(os.path.join(symbol_path,filename),wx.BITMAP_TYPE_ANY)
        sym.xsize = max(1,sym.image.GetWidth()/100)
        sym.ysize = max(1,sym.image.GetHeight()/100)
        self.SymbolList.append(sym)
        
      jpg_files = glob.glob('*.jpg')
      for filename in jpg_files:
        sym = SymbolRecord(image, symbol_path)
        sym.image = wx.Image(os.path.join(symbol_path,filename),wx.BITMAP_TYPE_ANY)
        sym.xsize = max(1,sym.image.GetWidth()/100)  #image dimension must be multiples of 100
        sym.ysize = max(1,sym.image.GetHeight()/100)
        self.SymbolList.append(sym)
      if (ResizeFiles):
        #take the loaded files and resize them if needed
        #reserve for possible resizing in the future.
        #for now, symbols must be 100x100
        #MSS 05/25/2011
        pass
      
      
    try:
      loadfile = open(os.path.join(gv.root_directory,"symbols.ini"))
    except IOError:
      logging.critical("PymapperAppMain::LoadSymbolFiles: Could not open symbols.ini")
      return None

    read_file = True
    while (read_file):
      line = loadfile.readline()
      line.rstrip("\n\r")
      info = line.split()
      if (info[0] == '#'):
        #This is a comment line;  skip to the next line
        pass
      elif (info[0] == 'VERSION'):
        version = float(info[1])
      elif (info[0] == 'SYMBOL'):
        filepath = loadfile.readline().rstrip("\n\r")
        filename = loadfile.readline().rstrip("\n\r")
        symbol = SymbolRecord(filename, filepath)

        symbol.image = wx.Image(os.path.join(filepath,filename))
        symbol.xsize = max(1,symbol.image.GetWidth()/100) #image dimension must be multiples of 100
        symbol.ysize = max(1,symbol.image.GetHeight()/100)
        symbol.user_defined = True
        self.SymbolList.append(symbol)
        symbol_count += 1
        logging.debug("Read symbol file: %s", filename)
      elif (info[0] == 'END_SYMBOLS_FILE'):
        read_file = False
        loadfile.close()
        logging.debug("Read %d symbols; closed symbols.ini", symbol_count)
    if (self.SymbolList != []):
      if (sys.platform == 'win32'):
        logging.debug("Add Symbols Page to TilePanel")
        self.RTilebookAddPage(name='Symbols')
        logging.debug("Symbols page added")
        for page in gv.TilePageList:
          if (page.PageName == 'Symbols'):
            page.tilesets.append('Symbols')
            break
      index = 0
      for symbol in self.SymbolList:
        #setup the symbol as a tile and store in self.tilelist
        newtile = Tile()
        newtile.key_index = gv.key_index
        symbol.key_index = gv.key_index
        gv.key_index += 1
        newtile.area = symbol.xsize * symbol.ysize
        newtile.sideA = symbol.image
        newtile.sideB = symbol.image
        newtile.tiledisplay = symbol.image
        newtile.actualXsize = symbol.xsize
        newtile.actualYsize = symbol.ysize
        newtile.copies = 99
        newtile.index = index
        index += 1
        newtile.layer = 0
        newtile.page = 'Symbols'
        newtile.tilesetID = 'SYMBOLS'
        newtile.tilesetName = 'Symbols'
        newtile.filenameA = symbol.filepath + symbol.filename
        newtile.filenameB = None
        newtile.tileID = index
        newtile.shown = True
        self.tilelist.append(newtile)
      #setup the symbols as a tileset
      tileset = TileSet()
      tileset.copies = 1
      tileset.loaded = True
      tileset.SetID = 'SYMBOLS'
      tileset.Name = 'Symbols'
      tileset.filename = 'Internal Tileset Only'
      gv.tilesets.append(tileset)
    logging.debug("LoadSymbolFiles complete")
    return

  def LoadMarkerFiles(self):
    try:
      loadfile = open(os.path.join(gv.root_directory,'markers.ini'), 'r')
    except IOError:
      logging.error("PyMapperAppMain::LoadMarkerFile error:  Could not open markers.ini")
      self.MarkerList = []
      return False
    logging.debug("PyMapperAppMain::LoadMarkerFile:  markers.ini open")
    read_file = True
    marker_count = 0
    while (read_file):
      line = loadfile.readline()
      line.rstrip("\n\r")
      info = line.split()
      if (info[0] == '#'):
        #This is a comment line;  skip to the next line
        pass
      elif (info[0] == 'VERSION'):
        version = float(info[1])
      elif (info[0] == 'MARKER'):
        marker = MarkerRecord()
        marker.outlineColor = wx.Colour(int(info[1]), int(info[2]), int(info[3]))
        marker.fillColor = wx.Colour(int(info[4]), int(info[5]), int(info[6]))
        marker.size = int(info[7])
      elif (info[0] == 'MARKER_SHAPE'):
        marker.shape = info[1]
      elif (info[0] == 'MARKER_INDEX'):
        marker.index = info[1]
      elif (info[0] == 'MARKER_NAME'):
        marker.name = loadfile.readline().rstrip("\n\r")
      elif (info[0] == 'END_MARKER'):
        marker_count += 1
        if (marker.index == None): #this is for backward compatibility prior to v7.2
          marker.index = marker_count
        self.MarkerList.append(marker)
        logging.debug("%s marker read and added.", marker.name)
      elif (info[0] == 'END_MARKER_FILE'):
        read_file = False
        logging.debug("Read %d marker files; Closing markers.ini", marker_count)
        loadfile.close()
    if (self.MarkerList != []):
      if (sys.platform == 'win32'):
        logging.debug("Add Markers page to TilePanel")
        self.RTilebookAddPage(name='Markers')
        logging.debug("Markers Page added")
        for page in gv.TilePageList:
          if (page.PageName == 'Markers'):
            page.tilesets.append('Markers')
            break
      index = 0
      for marker in self.MarkerList:
        bitmap = self.UpdateMarkerImage(marker)
        if (not bitmap):
          logging.error("LoadMarkerFiles: Uninitialized bitmap in %s", marker.name)
          continue
        marker.image = bitmap.ConvertToImage()
        #setup the marker as a tile
        newtile = Tile()
        newtile.key_index = gv.key_index
        marker.key_index = gv.key_index
        gv.key_index += 1
        newtile.area = marker.size * marker.size
        newtile.sideA = marker.image
        newtile.sideB = marker.image
        newtile.tiledisplay = marker.image
        newtile.actualXsize = marker.size
        newtile.actualYsize = marker.size
        newtile.copies = 99
        newtile.index = index
        index += 1
        newtile.layer = 0
        newtile.page = 'Markers'
        newtile.tilesetID = 'MARKERS'
        newtile.tilesetName = 'Markers'
        newtile.tileID = index
        newtile.shown = True
        self.tilelist.append(newtile)
      #setup the Markers as a tileset
      tileset = TileSet()
      tileset.copies = 1
      tileset.loaded = True
      tileset.SetID = 'MARKERS'
      tileset.Name = 'Markers'
      tileset.filename = 'Internal Tileset Only'
      gv.tilesets.append(tileset)
    logging.debug("LoadMarkerFiles Complete")
    return

  def UpdateMarkerImage(self, marker):
    """Return a bitmap of the marker"""
    bitmap = wx.Bitmap(100,100)
    folderPath = os.path.join(gv.artwork_directory,'markers')
    if (not bitmap):
      logging.critical("Could not create wxBitmap")
      return False
    if (marker.shape == 'Circle'):
      logging.debug("Creating circle mask")
      bitmapPath = os.path.join(folderPath, 'circle_template.png')
      bitmap_mask = wx.Mask(wx.Bitmap(bitmapPath, wx.BITMAP_TYPE_PNG), wx.BLACK)
      bitmap.SetMask(bitmap_mask)
      dc = wx.MemoryDC(bitmap)
      pen = wx.Pen(marker.outlineColor,5)
      dc.SetPen(pen)
      brush = wx.Brush(marker.fillColor)
      dc.SetBrush(brush)
      dc.DrawCircle(50,50,35)
      dc.SetFont(gv.TextFont)
      dc.SetTextForeground(marker.textColor)
      (textX, textY) = dc.GetTextExtent(marker.name)
      offsetX = max(0, (50-textX/2))
      offsetY = max(0, (50-textY/2))
#      dc.DrawText(marker.name, offsetX, offsetY)
      logging.debug("Circle image complete")
    elif (marker.shape == 'Triangle'):
      logging.debug("Creating triangle mask")
      bitmapPath = os.path.join(folderPath, 'triangle_template.png')
      bitmap_mask = wx.Mask(wx.Bitmap(bitmapPath, wx.BITMAP_TYPE_PNG), wx.BLACK)
      bitmap.SetMask(bitmap_mask)
      pen = wx.Pen(marker.outlineColor,5)
      brush = wx.Brush(marker.fillColor)
      dc = wx.MemoryDC(bitmap)
      dc.SetBrush(brush)
      dc.SetPen(pen)
      dc.DrawRectangle(0,0,100,100)
      dc.DrawLine(50,0,0,100)
      dc.DrawLine(50,0,100,100)
      dc.DrawLine(0,95,100,95)
      dc.SetFont(gv.TextFont)
      dc.SetTextForeground(marker.textColor)
      (textX, textY) = dc.GetTextExtent(marker.name)
      offsetX = max(0, (50-textX/2))
      offsetY = max(0, (70-textY/2))
#      dc.DrawText(marker.name, offsetX, offsetY)
      logging.debug("triangle image complete")
    elif (marker.shape == 'Square'):
      logging.debug("Creating square mask")
      bitmapPath = os.path.join(folderPath, 'square_template.png')
      bitmap_mask = wx.Mask(wx.Bitmap(bitmapPath, wx.BITMAP_TYPE_PNG), wx.BLACK)
      bitmap.SetMask(bitmap_mask)
      pen = wx.Pen(marker.outlineColor,5)
      brush = wx.Brush(marker.fillColor)
      dc = wx.MemoryDC(bitmap)
      dc.SetBrush(brush)
      dc.SetPen(pen)
      dc.DrawRectangle(10,10,80,80)
      dc.SetFont(gv.TextFont)
      dc.SetTextForeground(marker.textColor)
      (textX, textY) = dc.GetTextExtent(marker.name)
      offsetX = max(0, (50-textX/2))
      offsetY = max(0, (50-textY/2))
#      dc.DrawText(marker.name, offsetX, offsetY)
      logging.debug("square image complete")
    elif (marker.shape == 'InvTriangle'):
      logging.debug("Creating InvTriangle mask")
      bitmapPath = os.path.join(folderPath, 'invert_triangle_template.png')
      bitmap_mask = wx.Mask(wx.Bitmap(bitmapPath, wx.BITMAP_TYPE_PNG), wx.BLACK)
      bitmap.SetMask(bitmap_mask)
      pen = wx.Pen(marker.outlineColor,5)
      brush = wx.Brush(marker.fillColor)
      dc = wx.MemoryDC(bitmap)
      dc.SetBrush(brush)
      dc.SetPen(pen)
      dc.DrawRectangle(0,0,100,100)
      dc.DrawLine(0,0,100,0)
      dc.DrawLine(50,100,0,0)
      dc.DrawLine(50,100,100,0)
      dc.SetFont(gv.TextFont)
      dc.SetTextForeground(marker.textColor)
      (textX, textY) = dc.GetTextExtent(marker.name)
      offsetX = max(0, (50-textX/2))
      offsetY = max(0, (30-textY/2))
#      dc.DrawText(marker.name, offsetX, offsetY)
      logging.debug("invtriangle image complete")
    elif (marker.shape == 'Diamond'):
      logging.debug("Creating diamond mask")
      bitmapPath = os.path.join(folderPath, 'diamond_template.png')
      bitmap_mask = wx.Mask(wx.Bitmap(bitmapPath, wx.BITMAP_TYPE_PNG), wx.BLACK)
      bitmap.SetMask(bitmap_mask)
      pen = wx.Pen(marker.outlineColor,5)
      brush = wx.Brush(marker.fillColor)
      dc = wx.MemoryDC(bitmap)
      dc.SetBrush(brush)
      dc.SetPen(pen)
      dc.DrawRectangle(0,0,100,100)
      dc.DrawLine(50,0,0,50)
      dc.DrawLine(48,0,98,50)
      dc.DrawLine(53,100,3,50)
      dc.DrawLine(48,100,100,48)
      dc.SetFont(gv.TextFont)
      dc.SetTextForeground(marker.textColor)
      (textX, textY) = dc.GetTextExtent(marker.name)
      offsetX = max(0, (50-textX/2))
      offsetY = max(0, (50-textY/2))
#      dc.DrawText(marker.name, offsetX, offsetY)
      logging.debug("diamond image complete")
    elif (marker.shape == 'Hexagon'):
      logging.debug("Creating hexagon mask")
      bitmapPath = os.path.join(folderPath, 'hexagon_template.png')
      bitmap_mask = wx.Mask(wx.Bitmap(bitmapPath, wx.BITMAP_TYPE_PNG), wx.BLACK)
      bitmap.SetMask(bitmap_mask)
      pen = wx.Pen(marker.outlineColor,5)
      brush = wx.Brush(marker.fillColor)
      dc = wx.MemoryDC(bitmap)
      dc.SetBrush(brush)
      dc.SetPen(pen)
      dc.DrawRectangle(0,0,100,100)
      dc.DrawLine(50,0,0,25)
      dc.DrawLine(50,0,100,25)
      dc.DrawLine(3,25,3,75)
      dc.DrawLine(97,25,97,75)
      dc.DrawLine(50,100,0,75)
      dc.DrawLine(50,100,100,75)
      dc.SetFont(gv.TextFont)
      dc.SetTextForeground(marker.textColor)
      (textX, textY) = dc.GetTextExtent(marker.name)
      offsetX = max(0, (50-textX/2))
      offsetY = max(0, (50-textY/2))
#      dc.DrawText(marker.name, offsetX, offsetY)
      logging.debug("hexagon image complete")
    dc.SelectObject(wx.NullBitmap)
    logging.debug("Returning bitmap")
    return bitmap

  def OnReportsTilesets(self, event):
    map_tilesets = []
    found = False
    for tile in self.maplist:
      found = False
      for tileset in map_tilesets:
        if (tileset == tile.tilesetName):
          found = True
          break
      if (not found):
        map_tilesets.append(tile.tilesetName)
        found = False
    text = "Tilesets used:\n"
    if (map_tilesets == []):
      text += "None"
    else:
      for set_text in map_tilesets:
        text += set_text + "\n"

    dlg = TilesetManifestDialog(self.frame, text_string=text)

    index = dlg.ShowModal()
    dlg.Destroy()
    return

  def OnReportsManifest(self, event):
    if (self.maplist == []):
      wx.MessageBox(message="No tiles on the map, cannot create report!", caption="Whoa!", style=wx.ICON_EXCLAMATION)
      return
    else:
      #set up the pages for the preview dialog
      pagelist = []
      NumPages = 0
      (wPPI, hPPI) = (600,600) #self.GetPPIPrinter()
      border = int(hPPI * 0.25)
      papersize = wx.Size(216,279) #self.PSDD.GetPaperSize()  #in mm

      MarginTopLeft = wx.Point(13,13) #self.PSDD.GetMarginTopLeft()
      MarginBottomRight = wx.Point(13,25) #self.PSDD.GetMarginBottomRight()
      width = wPPI * int(papersize.width/25.4)
      height = hPPI * int(papersize.height/25.4)
      bottom_margin = int(MarginBottomRight.y/25.4)
      pageBMP = wx.Bitmap(width, height)
      dc = wx.MemoryDC(pageBMP)
      dc.SetPen(wx.WHITE_PEN)
      dc.SetBrush(wx.WHITE_BRUSH)
      dc.DrawRectangle(0,0,width, height)
      offsetX = int(wPPI * (MarginTopLeft.x/25.4))
      offsetY = int(hPPI * (MarginTopLeft.y/25.4))
      dc.SetTextBackground(wx.WHITE)
      dc.SetTextForeground(wx.BLACK)
      font = wx.Font(48, 74, 90, 92, underline=False, faceName="Times New Roman")
      dc.SetFont(font)
      StartNewPage = False
  
      tile = Tile()
      self.UpdateTilelistManifest()
      for tile in self.maplist:
        if (tile.num_used > 0):
          if (tile.showingBside == False):
            img = tile.sideA.Copy()
            if (tile.tilenameA != None):
              dc.DrawText(str(tile.tilenameA), offsetX+800, offsetY+200)
          else:
            img = tile.sideB.Copy()
            if (tile.tilenameB != None):
              dc.DrawText(str(tile.tilenameB), offsetX+800, offsetY+200)
          if (img.GetHeight() > img.GetWidth()):
            img_size = wx.Size(img.GetHeight(), img.GetHeight())
            img_pt = wx.Point((img.GetHeight()/2)- (img.GetWidth()/2), 0)
          else:
            img_size = wx.Size(img.GetWidth(), img.GetWidth())
            img_pt = wx.Point(0, (img.GetWidth()/2)- (img.GetHeight()/2))
  
          img2 = img.Resize(img_size, img_pt, 255,255,255)
          img3 = img.Rescale(wPPI, hPPI)
          bmp = wx.BitmapFromImage(img3)
  
          dc.DrawBitmap(bmp, offsetX, offsetY, True)
          #dc.DrawText("x"+str(tile.num_used), (offsetX+650), offsetY+200)   #removed in 8.3, until I can figure out how to remove duplicate entries from displaying in the manifest
          dc.DrawText(str(tile.tilesetID)+"  "+str(tile.tilesetName), offsetX+800, offsetY+50)
          dc.DrawText(str(tile.actualXsize)+"x"+str(tile.actualYsize), offsetX+800, offsetY+350)
          offsetY += (hPPI + border) # the info section is 1" high, with 1/4" between
          if (offsetY > (height-(hPPI+bottom_margin))):
            if (StartNewPage == True):
              dc.EndPage()
              offsetX = int(wPPI * (MarginTopLeft.x/25.4))
              offsetY = int(hPPI * (MarginTopLeft.y/25.4))
              dc.SelectObject(wx.NullBitmap)
              image = wx.ImageFromBitmap(pageBMP)
              image.Rescale(425, 550)
              pageBMP = wx.BitmapFromImage(image)
              pagelist.append(pageBMP)
              NumPages += 1
              pageBMP = wx.Bitmap(width, height)
              dc = wx.MemoryDC(pageBMP)
              dc.SetPen(wx.WHITE_PEN)
              dc.SetBrush(wx.WHITE_BRUSH)
              dc.DrawRectangle(0,0,width, height)
              dc.SetFont(font)
              StartNewPage = False
            else:
              offsetX = width/2
              offsetY = int(hPPI * (MarginTopLeft.y/25.4))
              StartNewPage = True  #next time through, start a new page
      dc.SelectObject(wx.NullBitmap)
      dc.EndPage()
      image = wx.ImageFromBitmap(pageBMP)
      image.Rescale(425, 550)
      pageBMP = wx.BitmapFromImage(image)
      pagelist.append(pageBMP)
      NumPages += 1

      PreviewDialog = ManifestPrintPreview(self.frame, pagelist, NumPages)
      if (PreviewDialog.ShowModal() == False):
        return
      PageSetupData = wx.PageSetupDialogData()
      #default 1/2 inch margins for top, bottom, R side.  1" for left side
      PageSetupData.SetMarginTopLeft(wx.Point(25,13))
      PageSetupData.SetMarginBottomRight(wx.Point(13,13))

      PageSetupDlg = wx.PageSetupDialog(self.frame, PageSetupData)
      if (PageSetupDlg.ShowModal() == wx.ID_OK):
        PageSetupDialogData = PageSetupDlg.GetPageSetupData()
        PrintData = PageSetupDialogData.GetPrintData()
        PrintDialogData = wx.PrintDialogData(PrintData)

        papersize = PageSetupDialogData.GetPaperSize()  #in mm
        MarginTopLeft = PageSetupDialogData.GetMarginTopLeft()
        MarginBottomRight = PageSetupDialogData.GetMarginBottomRight()


        if (self.maplist == []):
          #no matching tiles between tilepanel and mappanel
          errdlg = wx.MessageDialog(self.frame, 'Could not create manifest list', 'Error:OnReportsManifest', wx.OK | wx.ICON_ERROR)
          errdlg.ShowModal()
          errdlg.Destroy()
          return
        printout = ManifestPrint(PageSetupDialogData, self.tilelist)
        printer = wx.Printer(PrintDialogData)
        
        printer.Print(self.frame, printout, True)
        printout.Destroy()
      PageSetupDlg.Destroy()
    return

  def UpdateTilelistManifest(self):
    """Updates the number of tiles used from the tilepanel to tiles in the map panel."""
    for maptile in self.maplist:
      for tile in self.tilelist:
        if (tile.key_index == maptile.key_index):
          maptile.num_used = tile.num_used
    return

  def OnPrintImage(self, event):
    temp_dir = os.getcwd()
    try:
      os.chdir(gv.image_directory)
    except OSError:
      text = "Error in OnPrintImage: Could not change to ", gv.image_directory
      wx.MessageBox(message=text, caption="Error", style=wx.ICON_EXCLAMATION)
      return False
    dlg = wx.FileDialog(self.frame, message="Save image as...", 
                        defaultDir=os.getcwd(), defaultFile="", 
                        wildcard=export_wildcard, style=wx.SAVE | wx.FD_OVERWRITE_PROMPT)
    if (dlg.ShowModal() == wx.ID_OK):
      gv.image_directory = dlg.GetDirectory()
      self.DrawMapWindow(printing=True)
      #saveimage = wx.ImageFromBitmap(self.MapBuffer)
      #if (not saveimage.IsOk()):
      #  logging.error("OnPrintImage:  Could not obtain valid image from self.MapBuffer")
      #  return
      if (dlg.GetFilterIndex() == 0):
        #jpg image
        self.PrintBuffer.SaveFile(dlg.GetPath(),wx.BITMAP_TYPE_JPEG)  #used prior to v9.3
        #saveimage.SaveFile(dlg.GetPath(),wx.BITMAP_TYPE_JPEG)
      elif (dlg.GetFilterIndex() == 1):
        #png image
        try:
          self.PrintBuffer.SaveFile(dlg.GetPath(),wx.BITMAP_TYPE_PNG)  #used prior to v9.3
          #saveimage.SaveFile(dlg.GetPath(),wx.BITMAP_TYPE_PNG)  #added v9.3.  
        except:
          logging.critical("OnPrintImage: Could not allocate memory for image save")
    dlg.Destroy()
    os.chdir(temp_dir)
    return

  def OnPrintSetup(self, event):
    psdd = wx.PageSetupDialogData(self.PrintData)
    psdd.CalculatePaperSizeFromId()
    dlg = wx.PageSetupDialog(self.frame, psdd)
    if (dlg.ShowModal() == wx.ID_OK):
      self.PrintData = wx.PrintData( dlg.GetPageSetupData().GetPrintData() )
    dlg.Destroy()
    return

  def OnPrintMap(self, event):
    #need to send the correct paper size to the printer
    self.DrawMapWindow(True)
    if ((self.MapStruct.GridExtents.width == 0) or (self.MapStruct.GridExtents.height == 0)):
      wx.MessageBox(message="No tiles to print!", caption="Whoa!", style=wx.ICON_EXCLAMATION)
      return
    dlg = PrintPreviewDialog(self.frame, self.PrintData,
                             self.PrintBuffer, self.MapStruct.GridExtents)
    result = dlg.ShowModal()
    if (result == False):
      return

    gv.OutlineTiles = dlg.cbOutlineTiles.GetValue()
    gv.OutlineTilesColor = dlg.cxOutlineColor.GetColour()
    #PrintData holds print job settings (number of pages, num copies, etc)
    PrintData = wx.PrintDialogData(dlg.printdata)
    PrintData.SetToPage(dlg.NumPagesTotal)

    #PageData holds info relative to the paper being used;  wx.PageSetupDialogData
    self.PageData = dlg.pagedata

    printout = MapPrintout(dlg.pagelist, dlg.NumPagesTotal, self.PageData)
    printer = wx.Printer(PrintData)
    printer.Print(self.frame, printout, True)
    if (printer.GetLastError() == wx.PRINTER_ERROR):
      wx.MessageBox("There was a problem printing.\nPerhaps your current printer is not set correctly?", "Printing", wx.OK)
    elif (printer.GetLastError() == wx.PRINTER_CANCELLED):
      pass
      #wx.MessageBox("Printing Cancelled", "Printing", wx.OK)
    else: #wx.PRINTER_NO_ERROR
      self.PrintData = wx.PrintData(printer.GetPrintDialogData().GetPrintData())
    printout.Destroy()
    dlg.Destroy()
    return

  def OnChangePrintResolution(self, event):
    result = wx.MessageBox(message="Increasing print resolution may cause program to crash when \nprinting, due to lack of memory.  Save map file before printing!\n\nMaximum resolution factor is 200, recommended range is 50-100",
                           caption="Warning!", style=wx.ICON_EXCLAMATION | wx.OK | wx.CANCEL)
    if (result == wx.CANCEL):
      return
    dlg = PrintResolutionDialog(self.frame)
    if(dlg.ShowModal() == True):
      gv.PrintResolution = dlg.spResolution.GetValue()
      gv.SavePrintResolution = dlg.cbSaveToINI.GetValue()
    return

  def UndoActionEvent(self, flag=None, tile=None, dx=None, dy=None,
                      point=None, rotate=None, direction=None,
                      text=None, bitmap=None, icon=None):
    #flag is the action that was just taken
    undo = UndoItem()
    if (flag == 'ADD_TILE'):
      undo.tile = tile
      undo.Action = flag
    elif (flag == 'DELETE_MAP_PAGE'):
      undo.Action = flag
      undo.text = text
    elif (flag == 'DELETE_TILE_PAGE'):
      undo.Action = flag
      undo.text = text
    elif (flag == 'ROTATE_TILE'):
      undo.tile = tile
      undo.Action = flag
      undo.rotate = rotate
      undo.bitmap = bitmap
      undo.dx = dx
      undo.dy = dy
    elif (flag =='MOVE_TILE'):
      undo.tile = tile
      undo.Action = flag
      undo.MapPosition.x = point.x
      undo.MapPosition.y = point.y
    elif (flag == 'DELETE_TILE'):
      undo.tile = tile
      undo.Action = flag
    elif (flag == 'ADD_TEXT'):
      undo.Action = flag
      undo.text = text
    elif (flag == 'DELETE_TEXT'):
      undo.text = text
      undo.Action = flag
    elif (flag == 'MOVE_TEXT'):
      undo.text = text
      undo.Action = flag
      undo.dx = dx
      undo.dy = dy
    elif (flag == 'ADD_ICON'):
      undo.Action = flag
      undo.icon = icon
    elif (flag == 'FLIP_TILE'):
      undo.tile = tile
      undo.Action = flag
    elif (flag == 'DELETE_ICON'):
      undo.icon = icon
      undo.Action = flag
    elif (flag == 'MOVE_ICON'):
      undo.icon = icon
      undo.Action = flag
      undo.dx = dx
      undo.dy = dy
    self.UndoList.append(undo)
    self.frame.menubar.Enable(PyMapperDialogs.mEditUndo, True)
    self.frame.toolbar.EnableTool(id=PyMapperDialogs.tEditUndo,enable=True)
    gv.PromptSave = True
    return

  def OnUndoAction(self, event):
    if (self.UndoList == []):
      self.frame.menubar.Enable(PyMapperDialogs.mEditUndo, False)
      self.frame.toolbar.EnableTool(id=PyMapperDialogs.tEditUndo,enable=False)
      return
    undo = self.UndoList.pop()
    if (undo.Action == 'ADD_TILE'):
      for tile in self.maplist:
        if (undo.tile.index == tile.index):
          self.maplist.remove(tile)
          if (self.selectlist != []):
            self.selectlist.remove(self.selectlist[0])
          for y in self.tilelist:
            if ((y.tilesetID == tile.tilesetID) and (y.tileID == tile.tileID)):
              y.num_used -= 1
              y.dimmed = False
              self.DrawTileWindow()
          if (self.dragImage):
            self.dragImage = None
          self.DrawMapWindow()
    elif (undo.Action == 'ADD_TEXT'):
      for item in self.textlist:
        if (item == undo.text):
          self.textlist.remove(item)
        self.DrawMapWindow()
    elif (undo.Action == 'DELETE_MAP_PAGE'):
      self.RMapbookAddPage(name=undo.text)
    elif (undo.Action == 'DELETE_TILE_PAGE'):
      self.RTilebookAddPage(name=undo.text)
    elif (undo.Action == 'DELETE_TEXT'):
      self.textlist.append(undo.text)
      self.DrawMapWindow()
    elif (undo.Action == 'MOVE_TEXT'):
      for item in self.textlist:
        if (item == undo.text):
          item.x = undo.dx
          item.y = undo.dy
          self.DrawMapWindow()
          break
    elif (undo.Action == 'DELETE_ICON'):
      gv.RoomList.append(undo.icon)
      self.DrawMapWindow()
    elif (undo.Action == 'ADD_ICON'):
      for item in gv.RoomList:
        if (item == undo.icon):
          gv.RoomList.remove(item)
        self.DrawMapWindow()
        break
    elif (undo.Action == 'MOVE_ICON'):
      for item in gv.RoomList:
        if (item == undo.icon):
          item.MapRect.x = undo.dx
          item.MapRect.y = undo.dy
          self.DrawMapWindow()
          break
    elif (undo.Action == 'ROTATE_TILE'):
      for tile in self.maplist:
        if (tile.index == undo.tile.index):
          tile.rotation = undo.rotate
          tile.MapRect.width = undo.dx
          tile.MapRect.height = undo.dy
          tile.GenerateMapDisplay(gv.MapZoomFactor)
          self.DrawMapWindow()
    elif (undo.Action == 'MOVE_TILE'):
      for tile in self.maplist:
        if (tile.index == undo.tile.index):
          tile.MapPosition.x = undo.MapPosition.x
          tile.MapPosition.y = undo.MapPosition.y
          tile.MapRect.x = undo.MapPosition.x
          tile.MapRect.y = undo.MapPosition.y
          self.DrawMapWindow()
          break
    elif (undo.Action == 'FLIP_TILE'):
      for tile in self.maplist:
        if (tile.index == undo.tile.index):
          tile.GenerateMapDisplay(gv.MapZoomFactor)
          self.DrawMapWindow()
    elif (undo.Action == 'DELETE_TILE'):
      self.maplist.append(undo.tile)
      gv.PromptSave = True
      undo.tile.index = self.MasterIndex
      self.MasterIndex += 1
      undo.tile.order = len(self.maplist)
      self.UndoActionEvent(flag="ADD_TILE", tile=undo.tile)
      for tile in self.tilelist:
        if ((tile.tileID == undo.tile.tileID) and 
            (tile.tilesetID == undo.tile.tilesetID)):
          tile.num_used += 1
          if (gv.LimitTiles == True):
            tile.dimmed = True
          self.DrawTileWindow()
          break
      self.DrawMapWindow()

    if (self.UndoList == []):
      #disable the button if the last item was processed
      self.frame.menubar.Enable(PyMapperDialogs.mEditUndo, False)
      self.frame.toolbar.EnableTool(id=PyMapperDialogs.tEditUndo,enable=False)
    return

  def OnEditMapSize(self, event):
    dlg = ChangeMapSizeDialogCore(self.frame, self.MapStruct.rows, self.MapStruct.columns)
    result = dlg.ShowModal()
    if (result == True):
      if (dlg.ExpandDirection == 'TopLeft'):
        #no adjustment needed, map expands to the right, and down
        xOffset = 0
        yOffset = 0
      elif (dlg.ExpandDirection == 'TopCenter'):
        xOffset = (dlg.spColumns.GetValue() - self.MapStruct.columns)//2
        yOffset = 0
      elif (dlg.ExpandDirection == 'TopRight'):
        xOffset = (dlg.spColumns.GetValue() - self.MapStruct.columns)
        yOffset = 0
      elif (dlg.ExpandDirection == 'CenterLeft'):
        xOffset = 0
        yOffset = (dlg.spRows.GetValue() - self.MapStruct.rows)//2
      elif (dlg.ExpandDirection == 'Center'):
        xOffset = (dlg.spColumns.GetValue() - self.MapStruct.columns)//2
        yOffset = (dlg.spRows.GetValue() - self.MapStruct.rows)//2
      elif (dlg.ExpandDirection == 'CenterRight'):
        xOffset = (dlg.spColumns.GetValue() - self.MapStruct.columns)
        yOffset = (dlg.spRows.GetValue() - self.MapStruct.rows)//2
      elif (dlg.ExpandDirection == 'BottomLeft'):
        xOffset = 0
        yOffset = (dlg.spRows.GetValue() - self.MapStruct.rows)
      elif (dlg.ExpandDirection == 'BottomCenter'):
        xOffset = (dlg.spColumns.GetValue() - self.MapStruct.columns)//2
        yOffset = (dlg.spRows.GetValue() - self.MapStruct.rows)
      elif (dlg.ExpandDirection == 'BottomRight'):
        xOffset = (dlg.spColumns.GetValue() - self.MapStruct.columns)
        yOffset = (dlg.spRows.GetValue() - self.MapStruct.rows)

      for tile in self.maplist:
        #move tiles
        tile.MapPosition.x += xOffset
        tile.MapPosition.y += yOffset
        tile.MapRect.x += xOffset
        tile.MapRect.y += yOffset
        
      for room in gv.RoomList:
        #move room and monster icons
        room.x += xOffset
        room.y += yOffset
        
      for text in self.textlist:
        #move text annotations
        text.x += xOffset
        text.y += yOffset
        
      for item in self.DrawingList:
        #move drawing items
        if (item.tool == 'Freehand') or (item.tool == 'Line') or (item.tool == 'Multiline'):
          for point in item.line:
            point.x += xOffset
            point.y += yOffset
        elif (item.tool == 'OutlineRect') or (item.tool == 'FillRect'):
          item.rect.x += xOffset
          item.rect.y += yOffset
        elif (item.tool == 'OutlineCircle') or (item.tool == 'FillCircle'):
          xValue,yValue = item.circle[0]
          xValue += xOffset
          yValue += yOffset
          item.circle[0] = wx.Point2D(xValue,yValue)
        elif (item.tool == 'Image'):
          item.rect.x += xOffset
          item.rect.y += yOffset
        
      self.MapStruct.rows = dlg.spRows.GetValue()
      self.MapStruct.columns = dlg.spColumns.GetValue()
      
      self.DrawMapWindow()
    dlg.Destroy()
    return

  def MoveUpDisplayOrder(self, delta):
    for tile in self.maplist:
      if (tile.selected == True):
        if (delta == 'TOP'):
          i = self.maplist.index(tile)
          x = self.maplist.pop(i)
          self.maplist.append(x)
          break
        elif (delta == 'SINGLE'):
          i = self.maplist.index(tile)
          if (i==(len(self.maplist)-1)):
            return
          x = self.maplist.pop(i)
          self.maplist.insert(i+1, x)
          break
    gv.PromptSave = True
    self.DrawMapWindow()
    return

  def MoveDownDisplayOrder(self, delta):
    for tile in self.maplist:
      if (tile.selected == True):
        if (delta == 'BOTTOM'):
          i = self.maplist.index(tile)
          x = self.maplist.pop(i)
          self.maplist.insert(0,x)
          for x in self.selectlist:
            x.selected = False
          self.selectlist = []
          break
        elif (delta == 'SINGLE'):
          i = self.maplist.index(tile)
          if (i==0):
            return
          x = self.maplist.pop(i)
          self.maplist.insert(i-1, x)
          break
    self.DrawMapWindow()
    gv.PromptSave = True
    return
  
  def DisplayHighlightTile(self, displayHover):
    if (gv.OutlineOnHover) and (displayHover):
      #search the tile list in order to highlight the tile
      for tile in self.maplist:
        if tile.HitTest(gv.LastPoint):
          tile.highlight = True
        else:
          tile.highlight = False
      self.DrawMapWindow()
    return

  def DisplayHoverInformation(self, display):
    """Displays labels, monster dialog info, and outlines the object under the mouse(option turned on by gv.OutlineOnHover)"""
    icon_found = False
    tile_found = False
    tile = None

    if ((display == True) and (not self.MouseOnTilePanel)):
      if (gv.DisplayIconInformation):  #check icons for hover
        if (gv.hoverDlg == None):  # not currently displaying a hoverDlg
          for room in gv.RoomList:
            currentPage = self.nbMapNotebook.GetSelection()
            if (room.page != gv.MapPageList[currentPage].PageName):
              continue  #skip search if the room icon is not on the current page
            else:
              rect = wx.Rect(int(room.x * gv.MapZoomFactor), int(room.y * gv.MapZoomFactor), room.MapRect.width, room.MapRect.height)
              gridpoint = self.MapPanel.CalcUnscrolledPosition(gv.LastPoint)
              icon_found = rect.Contains(gridpoint)
              if (icon_found):
                break
          if (icon_found):  #display icon hover dialog
            if (room.IconType == 'NPC') and (room.npc):  #used for 3.5/PF NPC's
              gv.hoverDlg = CharacterInfoDialog(self.frame, room, gv.HoverPoint)
            elif (room.IconType == 'NPC') and (room.monster):  #treat as a 5E NPC
              gv.hoverDlg = MonsterHoverDialog(self.frame, room, gv.HoverPoint)
              gv.hoverMonsterInfo = room.monster
            elif (room.IconType == 'Monster') and (room.monster):  #must have valid monster data
              if ((room.monster.version == '5E') or (room.monster.version == '5E_OLD')):
                gv.hoverDlg = MonsterHoverDialog(self.frame, room, gv.HoverPoint)
                gv.hoverMonsterInfo = room.monster
              else:  #pre 5E monser, ie, Pathfinder or 3.5
                gv.hoverDlg = MonstersDialog(self.frame, room.monster.uniqueID, gv.HoverPoint)
                gv.hoverMonsterInfo = room.monster
            elif (room.IconType == 'Trap'):
              gv.hoverDlg = TrapInfoDialog(self.frame, room, gv.HoverPoint)
            else:  #the following code will show the name of the icon in a small text field.
              memdc = wx.MemoryDC()
              if (not memdc.IsOk()):
                return
              memdc.SetMapMode(wx.MM_TEXT)
              font = wx.NORMAL_FONT
              font.SetPointSize(10)
              memdc.SetFont(font)
              (width, height) = memdc.GetTextExtent(room.Description)
              width += 3  #add a border to the hover image
              height += 3
              bmp = wx.Bitmap(width, height)
              memdc.SelectObject(bmp)
              memdc.Clear()
              memdc.DrawText(room.Description, 2, 0)
              memdc.SelectObject(wx.NullBitmap)
              gv.HoverPoint.x += 15  #this is to offset the text from the mouse
              gv.hoverDlg = HoverTileDialogCore(self.frame, None, bmp, gv.HoverPoint)
            gv.hoverDlg.Show(True)
          elif (not icon_found) and (gv.hoverDlg):
            gv.hoverDlg.Show(False)
            gv.hoverDlg.Destroy()
            gv.hoverDlg = None
    elif ((display == True) and (self.MouseOnTilePanel)):  #file the hover on the tile panel
      if (gv.hoverDlg == None):
        tile = self.FindTileOnTilePanel(gv.LastPoint)
        if (tile == None):
          return
        if (gv.DisplayOnHover):
          gv.HoverPoint.x += 15  #this is to offset the tile from the mouse
          gv.hoverDlg = HoverTileDialogCore(self.frame, tile, None, gv.HoverPoint)
          if (gv.hoverDlg):
            gv.hoverDlg.Show(True)
    else:  #end display of the hover dialog;  store monster info if appropriate
      if (gv.hoverDlg):
        if (gv.hoverMonsterInfo) and ((gv.hoverMonsterInfo.version == '5E_NPC') or (gv.hoverMonsterInfo.version == '5E') or (gv.hoverMonsterInfo.version == '5E_OLD')):
          gv.hoverDlg.room.windowSize = gv.hoverDlg.GetSize()
          gv.hoverMonsterInfo.AC = gv.hoverDlg.spArmorClass.GetValue()
          gv.hoverMonsterInfo.HP = gv.hoverDlg.spHitPoints.GetValue()
          gv.hoverMonsterInfo.con1 = gv.hoverDlg.cxCondition1.GetStringSelection()
          gv.hoverMonsterInfo.con2 = gv.hoverDlg.cxCondition2.GetStringSelection()
          gv.hoverMonsterInfo.con3 = gv.hoverDlg.cxCondition3.GetStringSelection()
          gv.hoverMonsterInfo.con4 = gv.hoverDlg.cxCondition4.GetStringSelection()
          gv.hoverMonsterInfo.startHP = gv.hoverDlg.StartHP
          gv.hoverMonsterInfo.userNotes = gv.hoverDlg.txNotes.GetValue()
          gv.hoverMonsterInfo.deathSaveFail = 0
          gv.hoverMonsterInfo.deathSavePass = 0
          if (gv.hoverDlg.cbDeathSaveFail1.IsChecked()):
            gv.hoverMonsterInfo.deathSaveFail += 1
          if (gv.hoverDlg.cbDeathSaveFail2.IsChecked()):
            gv.hoverMonsterInfo.deathSaveFail += 1
          if (gv.hoverDlg.cbDeathSaveFail3.IsChecked()):
            gv.hoverMonsterInfo.deathSaveFail += 1
            
          if (gv.hoverDlg.cbDeathSavePass1.IsChecked()):
            gv.hoverMonsterInfo.deathSavePass += 1
          if (gv.hoverDlg.cbDeathSavePass2.IsChecked()):
            gv.hoverMonsterInfo.deathSavePass += 1
          if (gv.hoverDlg.cbDeathSavePass3.IsChecked()):
            gv.hoverMonsterInfo.deathSavePass += 1
            
        gv.hoverMonsterInfo = None
        self.DrawMapWindow(drawOnly='ICONS')
        gv.hoverDlg.Show(False)
        gv.hoverDlg.Destroy()
        gv.hoverDlg = None
    return # End of DisplayHoverTile

  def OnIdle(self, event):
    if (self.hovertimer.IsRunning() == False):
      self.hovertimer.Start(gv.hover_interval)
    if (not self.IsIcon):
      if (gv.FrameSize != self.frame.GetSize()):
        gv.FrameSize = self.frame.GetSize()
        self.RefreshWindows(True)
    return

  def OnTimer(self, event):
    if (event.GetId() == 5):
      self.DisplayHoverInformation(True)
    elif (event.GetId() == 1):
      if (gv.backup_directory == None):
        wx.MessageBox(message="No backup folder specified in program options.\nAutomatic backup disabled.\nGo to Program|Options to restore.",
                      caption="Whoa!", style=wx.ICON_EXCLAMATION)
        gv.AutoSave = False
        logging.error("Could not AutoSave backup file")
      else:
        self.MapStruct.backupfilename = os.path.join(gv.backup_directory,"backup.map")
        self.SaveMapFile(self.MapStruct.backupfilename)
        self.backuptimer.Start(gv.AutoSaveInterval*1000)
    elif (event.GetId() == 9) and (gv.OutlineOnHover):
      self.DisplayHighlightTile(True)
    return

  def ChangeMapOffset(self, direction, value):
    if (direction == "x_pos"):
      gv.MapOffset.x = gv.MapOffset.x + value
    elif (direction == "x_neg"):
      gv.MapOffset.x = gv.MapOffset.x - value
      if (gv.MapOffset.x < 0):
        gv.MapOffset.x = 0
    elif (direction == "y_pos"):
      gv.MapOffset.y = gv.MapOffset.y + value
    elif (direction == "x_neg"):
      gv.MapOffset.y = gv.MapOffset.y - value
      if (gv.MapOffset.y < 0):
        gv.MapOffset.y = 0
    #End of ChangeMapOffset
    return

  def OnViewViewAll(self, event):
    self.RMapClickShowAll()
    self.DrawMapWindow()
    return

  def OnViewTilesetLayerFilter(self, event):
    if (gv.LayerDialog):
      gv.LayerDialog.Show(False)
      gv.LayerDialog.Destroy()
      gv.LayerDialog = None
    else:
      #build the tilesets list
      tileset_list = []
      for item in gv.tilesets:
        text = str(item.SetID) + " " + str(item.Name)
        tileset_list.append(text)
      gv.LayerDialog = LayerDisplayDialog(self.frame)
      gv.LayerDialog.Show(True)
    return

  def OnViewIcons(self, event):
    gv.ShowIcons = self.frame.toolbar.GetToolState(id=PyMapperDialogs.tShowIcons)
    self.DrawMapWindow()
    return

  def OnViewDrawingObjects(self, event):
    gv.ShowDrawingObjects = self.frame.toolbar.GetToolState(id=PyMapperDialogs.tShowDrawingObjects)
    self.DrawMapWindow()
    return
  
  def OnViewFogObjects(self, event):
    gv.ShowFogObjects = self.frame.toolbar.GetToolState(id=PyMapperDialogs.tShowFogObjects)
    self.DrawMapWindow()
    return
  
  def OnViewShowIconNames(self, event):
    if (event.GetId() == PyMapperDialogs.tShowLabels):  #from the toolbar
      gv.ShowIconNamesOnMap = self.frame.toolbar.GetToolState(PyMapperDialogs.tShowLabels)
      self.frame.menubar.Check(PyMapperDialogs.mShowIconNamesOnMap, gv.ShowIconNamesOnMap)
    else:  #from the menu item
      gv.ShowIconNamesOnMap = self.frame.menubar.IsChecked(PyMapperDialogs.mShowIconNamesOnMap)
      self.frame.toolbar.ToggleTool(PyMapperDialogs.tShowLabels, gv.ShowIconNamesOnMap)
    self.DrawMapWindow()
    return

  def OnViewDrawingHandles(self, event):
    gv.DrawHandles = self.frame.toolbar.GetToolState(id=PyMapperDialogs.tShowDrawingHandles)
    self.DrawMapWindow()
    return

  def OnViewBackground(self, event):
    if (event.GetId() == PyMapperDialogs.tShowBackground):
      gv.DisplayBackground = self.frame.toolbar.GetToolState(id=PyMapperDialogs.tShowBackground)
      self.frame.menubar.Check(id=PyMapperDialogs.mViewBackground, check=gv.DisplayBackground)
    else:
      gv.DisplayBackground = self.frame.menubar.IsChecked(id=PyMapperDialogs.mViewBackground)
      self.frame.toolbar.ToggleTool(id=PyMapperDialogs.tShowBackground, toggle=gv.DisplayBackground)
    self.DrawMapWindow()
    return

  def OnViewGridCoordinates(self, event):
    gv.ShowGridCoordinates = self.frame.menubar.IsChecked(PyMapperDialogs.mViewGridCoordinates)
    self.DrawMapWindow()
    return

  def OnViewDualTileSides(self, event):
    gv.DualDisplayTileWindow = self.frame.menubar.IsChecked(PyMapperDialogs.mViewDualTileDisplay)
    gv.DisplayOnHover = not gv.DualDisplayTileWindow
    self.DrawTileWindow(True)
    return

  def OnViewSecondaryScreen(self, event=None):
    """
    Secondary screen is for the player display on multi-monitor systems.
    Will also bring up fog-of-war tools.
    """
    if (gv.SecondaryScreen):
      #The secondary screen is already up.
      gv.SecondaryScreen.Show(True)
      return
    else:
      #show the second screen and the tools for fog of war
      gv.SecondaryScreen = SecondaryMapDialog(self.frame)
      gv.SecondaryScreen.Show(True)
    return
  
  def OnViewFogTools(self, event):
    if (not fog.FogToolsDialog):
      fog.FogToolsDialog = fog.FogToolsDialogCore(self.frame)
      fog.FogToolsDialog.Show()
    else:
      fog.FogToolsDialog.Raise()
    
    return

  def OnViewHighlightIcons(self, event):
    gv.HighlightIcons = self.frame.menubar.IsChecked(PyMapperDialogs.mViewHighlightIcons)
    self.DrawMapWindow()
    return

  def OnViewGrid(self, event):
    if (event.GetId() == PyMapperDialogs.tShowGrid):  #event came from the toolbar
      gv.DisplayGrid = self.frame.toolbar.GetToolState(PyMapperDialogs.tShowGrid)
      self.frame.menubar.Check(id=PyMapperDialogs.mViewGrid, check=gv.DisplayGrid)
    else:  #event came from the menu item
      gv.DisplayGrid = self.frame.menubar.IsChecked(id=PyMapperDialogs.mViewGrid)
      self.frame.toolbar.ToggleTool(id=PyMapperDialogs.tShowGrid, toggle=gv.DisplayGrid)
    self.DrawMapWindow()
    return

  def OnViewFilterTags(self, event):
    self.filter_dlg = FilterTagsDialogCore(self.frame, False, self.tilelist)
    self.filter_dlg.Show(True)
    return

  def MapWindowMouseWheel(self, event):
    if (gv.ReverseMouseWheel):
      if (event.GetWheelRotation() > 0):
        gv.MapZoomFactor += 1
        if (gv.MapZoomFactor > 75):
          gv.MapZoomFactor = 75
      else:
        gv.MapZoomFactor -= 1
        if (gv.MapZoomFactor < 10):
          gv.MapZoomFactor = 10
    else:
      if (event.GetWheelRotation() < 0):
        gv.MapZoomFactor += 1
        if (gv.MapZoomFactor > 75):
          gv.MapZoomFactor = 75
      else:
        gv.MapZoomFactor -= 1
        if (gv.MapZoomFactor < 10):
          gv.MapZoomFactor = 10
    self.frame.MapWindowZoomSlider.SetValue(gv.MapZoomFactor)
    self.MapWindowZoom()
    return

  #----------------------------------------------------------------------
  def MapWindowZoomChanging(self, event):
    """User is actively changing the zoom via the slider"""
    #print "Changing Zoom"
    return
    
  def MapWindowZoomChanged(self, event):
    """User has changed the map window zoom via the slider.  """
    #print "Zoom changed"
    return

  def MapWindowZoom(self, event=None):
    gv.MapZoomFactor = self.frame.MapWindowZoomSlider.GetValue()
    for tile in self.maplist:
      # when changing the zoom, must resize the MapRect for each tile
      tile.GenerateMapDisplay(gv.MapZoomFactor)
    self.DrawMapWindow()
    return

  def TileWindowZoom(self, event):
    gv.TileZoomFactor = self.frame.TileWindowZoomSlider.GetValue()
    self.DrawTileWindow(True)
    self.TilePanel.Refresh()
    return

  def RefreshWindows(self, event=None):
    self.DrawTileWindow(True)
    self.DrawMapWindow()
    if (gv.hoverDlg):
      self.DisplayHoverInformation(False)
    return

  def OnOptionsIniFile(self, event):
    success = self.SaveIniFile()
    if (success == True):
      wx.MessageBox("Settings file saved", "Rolled a 20! Save Confirmed.")
    else:
      wx.MessageBox("Error: Could not save settings")

  def OnHelp_Contents(self, event):
    filename = os.path.join(gv.root_directory,"pymapper.chm")
    if (sys.platform == 'win32'): #os.startfile does not work on non-win32 system OS
      os.startfile(filename)
    else:
      opener ="open" if sys.platform == "darwin" else "xdg-open"
      subprocess.call([opener, filename])
    return
  
  def OnHelp_OpenTutorial(self, event):
    filename = os.path.join(gv.root_directory,"PymapperTutorial.pdf")
    if (sys.platform == 'win32'): #os.startfile does not work on non-win32 system OS
      os.startfile(filename)
    else:
      opener ="open" if sys.platform == "darwin" else "xdg-open"
      subprocess.call([opener, filename])
    return  

  def OnKeyboardEvent(self, event):
    #event.Skip()
    if (event.GetKeyCode() == wx.WXK_F12):
      self.ChangeSelectionMode(event=None, programActivation=True)
      event.Skip()
      return
    if (gv.SelectMode == 'icon'):  #working in text/icon mode
      if (event.GetKeyCode() == wx.WXK_DELETE):
        #delete the current selected text
        for item in self.textlist:
          if (item.selected == True):
            self.UndoActionEvent(flag='DELETE_TEXT', text=item)
            self.textlist.remove(item)
        self.DrawMapWindow()
        event.Skip()
      return #exit, since the following code is for tiles
    elif (gv.SelectMode == 'draw'):
      if (event.GetKeyCode() == wx.WXK_SPACE):
        if (gv.DrawingTool == 'Multiline'):
          gv.DrawingObject.zoomfactor = gv.MapZoomFactor
          self.DrawingList.append(gv.DrawingObject)
          gv.DrawingObject = None
          gv.DrawingToolStartPoint = None
          gv.DrawingToolPrevious = None
          gv.DrawingNextStep = 'start'
          self.DrawMapWindow()
          event.Skip()
    else:
      if (self.selectlist): #if no tiles selected, just skip keyboard events
        if (event.GetKeyCode() == wx.WXK_DELETE):
          self.DeleteMapTile(self.selectlist[0])
          event.Skip()
        elif((event.GetKeyCode() == wx.WXK_LEFT) and (not event.GetModifiers() == wx.MOD_SHIFT)):
          #rotate CCW 90 degrees
          tile = self.ChangeTileRotation(self.selectlist[0], 'CCW')
        elif((event.GetKeyCode() == wx.WXK_RIGHT) and (not event.GetModifiers() == wx.MOD_SHIFT)):
          #rotate CW 90 degrees
          tile = self.ChangeTileRotation(self.selectlist[0], 'CW')
        elif ((event.GetKeyCode() == wx.WXK_RIGHT) and (event.GetModifiers() == wx.MOD_SHIFT)):
          #move tiles right 1 square
          for tile in self.selectlist:
            tile.MapPosition.x += 1
            tile.MapRect.x += 1
        elif ((event.GetKeyCode() == wx.WXK_LEFT) and (event.GetModifiers() == wx.MOD_SHIFT)):
          #move tiles left 1 square
          for tile in self.selectlist:
            tile.MapPosition.x -= 1
            tile.MapRect.x -= 1
        elif ((event.GetKeyCode() == wx.WXK_UP) and (event.GetModifiers() == wx.MOD_SHIFT)):
          #move tiles up 1 square
          for tile in self.selectlist:
            tile.MapPosition.y -= 1
            tile.MapRect.y -= 1
        elif ((event.GetKeyCode() == wx.WXK_DOWN) and (event.GetModifiers() == wx.MOD_SHIFT)):
          #move tiles down 1 square
          for tile in self.selectlist:
            tile.MapPosition.y += 1
            tile.MapRect.y += 1
        elif(event.GetKeyCode() == wx.WXK_PAGEUP):
          if (event.GetModifiers() == wx.MOD_SHIFT):
            self.MoveUpDisplayOrder('TOP')
          else:
            self.MoveUpDisplayOrder('SINGLE')
        elif(event.GetKeyCode() == wx.WXK_PAGEDOWN):
          if (event.GetModifiers() == wx.MOD_SHIFT):
            self.MoveDownDisplayOrder('BOTTOM')
          else:
            self.MoveDownDisplayOrder('SINGLE')
        self.MapStruct.GridExtents = self.CalculateMapExtents(self.maplist)
        self.DrawMapWindow()
      if (event.GetKeyCode() == wx.WXK_SPACE):
        if (self.selectlist) and (not self.TileInMotion) and (self.MouseOnTilePanel == False):
          self.selectlist[0].selected = False
          x = self.selectlist.pop(0)
          self.selectlist.append(x)
          self.selectlist[0].selected = True
          self.dragImage = wx.DragImage(self.selectlist[0].mapdisplay, wx.StockCursor(wx.CURSOR_HAND))
          self.DrawMapWindow()
          event.Skip()
        if (self.MouseOnTilePanel == True):
          for tile in self.tilelist:
            if (tile.showingBside):
              tile.showingBside = False
              tile.tiledisplay = tile.sideA
            else:
              tile.showingBside = True
              if (tile.sideB):  #check this in case there is no sideB image (it is optional)
                tile.tiledisplay = tile.sideB
              else:
                tile.tiledisplay = tile.sideA
          event.Skip()
          self.DrawTileWindow()
      return

  def DeleteMapTile(self, tile):
    self.maplist.remove(tile)
    self.UndoActionEvent(flag="DELETE_TILE", tile=tile)
    if (self.selectlist != []):
      self.selectlist.remove(self.selectlist[0])
    for y in self.tilelist:
      if ((y.tilesetID == tile.tilesetID) and (y.tileID == tile.tileID)):
        y.num_used -= 1
        y.dimmed = False
        self.DrawTileWindow()
    if (self.dragImage):
      self.dragImage = None
    return

  def ChangeTileRotation(self, tile, direction):
    tile.RotateTile(direction)
    self.UndoActionEvent(flag='ROTATE_TILE', tile=tile, dx=tile.MapRect.width, dy=tile.MapRect.height,
                         rotate=tile.rotation, bitmap=tile.mapdisplay)
    tile.GenerateMapDisplay(gv.MapZoomFactor)
    return tile

  def MapWindowCenterClickUp(self, event):
    # end pan of the map window
    if (self.PanWindow):
      self.PanWindow = False
      self.DrawMapWindow()
    return

  def MapWindowCenterClickDown(self, event):
    #begin pan of the map window
    point = event.GetPosition()
    delta = abs(point[0] - gv.StartPan[0]) + abs(point[1] - gv.StartPan[1])

    if (delta > 5):
      #difference between current mouse and MapOffset, so start panning
      self.PanWindow = True
      #we haven't moved anywhere yet, so start and end are the same.
      gv.StartPan = point
      gv.EndPan = point
    else:
      self.PanWindow = False
    return

  def OnFileNew(self, event):
    if (event.GetId() == PyMapperDialogs.mFileNew) or (event.GetId() == PyMapperDialogs.tFileNew):
      folder = gv.maps_directory
      wcard = map_wildcard
      name = "NewMap"
      geomorphFlag = False
      DialogCaption = "New Map File"
    else:
      folder = gv.geomorphs_directory
      wcard = geomorph_wildcard
      name = "NewGeomorph"
      geomorphFlag = True
      DialogCaption = "New Geomorph File"
    if (gv.PromptSave == True):
      msg_dlg = wx.MessageDialog(self.frame, "Save existing map?", "Warning",
                                 wx.YES_NO | wx.CANCEL | wx.ICON_QUESTION)
      result = msg_dlg.ShowModal()
      if (result == wx.ID_YES):
        self.SaveMapFile(self.MapStruct.filename)
        msg_dlg.Destroy()
      elif (result == wx.ID_CANCEL):
        msg_dlg.Destroy()
        return

    dlg = wx.FileDialog(self.frame, message=DialogCaption, defaultDir=folder, defaultFile=name, wildcard=wcard, style=wx.OPEN | wx.CHANGE_DIR)

    if (dlg.ShowModal() == wx.ID_OK):
      if (not geomorphFlag):
        self.MapStruct.geomorph = False
        if (sys.platform == 'win32'):
          self.MapStruct.filename = dlg.GetPath()
        else:
          self.MapStruct.filename = dlg.GetPath() + ".map"
      else:
        self.MapStruct.geomorph = True
        self.MapStruct.geomorphData = Geomorph_Record()
        if (sys.platform == 'win32'):
          self.MapStruct.filename = dlg.GetPath()
        else:
          self.MapStruct.filename = dlg.GetPath() + ".pgf"
    else:
      dlg.Destroy()
      return
    
    dlg.Destroy()
    if (self.MapStruct.filename):
      self.frame.menubar.Enable(PyMapperDialogs.mFileSave, True)
      if (not self.MapStruct.geomorph):
        dlg = NewFileDialog(self.frame)
        new_map = dlg.ShowModal()
        if (new_map):
          gv.GridColor = dlg.cpkGridColor.GetColour()
          self.MapStruct.rows = dlg.RowSpinner.GetValue()
          self.MapStruct.columns = dlg.ColumnSpinner.GetValue()
          gv.DisplayGrid = dlg.UseGridOption.GetValue()
        else:
          return
      else:  #set up new geomorph
        new_map = True
        self.MapStruct.rows = 16
        self.MapStruct.columns = 14
        gv.DisplayGrid = True
      self.frame.SetLabel("PyMapper "+VERSION+": " + self.MapStruct.filename)
      if (new_map):
        self.MapStruct.Extents = wx.Rect(0,0,0,0)
        self.MapStruct.GridExtents = wx.Rect(0,0,0,0)
        self.MapStruct.background = None
        self.MapStruct.background_filename = None
        self.DrawTileWindow()
        self.DrawMapWindow()
        self.frame.menubar.Enable(PyMapperDialogs.mFileSave, False)
      dlg.Destroy()
      if (not self.tilelist):
        self.OnTilesetBrowser(event)
        
    #reset the Fog Mask
    self.MapFogImage = wx.Image(self.MapStruct.rows*gv.MapZoomFactor, self.MapStruct.columns*gv.MapZoomFactor)
    
    #reset the undo list
    self.UndoList = []

    #reset the icons list
    gv.RoomList = []

    #reset the textlist
    self.textlist = []

    #reset the maplist
    self.maplist = []

    #reset the drawing items
    self.DrawingList = []

    #reset the notebook pages
    self.nbMapNotebook.DeleteAllPages()
    gv.MapPageList = []
    gv.MapPanelList = []
    self.RMapbookAddPage(name='Map')
    self.MapPanel = gv.MapPanelList[0]
    
    #reset the layers
    gv.LayerList = []
    gv.LayerList.append(gv.LayerItem(index=0, name='Base'))
    self.frame.UpdateLayerSelector()
    if (gv.LayerDialog):
      gv.LayerDialog.UpdateLists()

    #reset the tilelist
    for tile in self.tilelist:
      tile.num_used = 0
      tile.selected = False
      tile.dimmed = False
      tile.mapdisplay = None
    
    gv.PromptSave = False
    self.UpdateFileList(self.MapStruct.filename)
    self.RefreshWindows()
    return

  def OnUpdateToFTP(self, event):
    """Updates the current MapBuffer to a remote server"""
    if (gv.SecondaryScreen):
      gv.SecondaryScreen.UpdateFTP()
    return
  
  def OnUpdateFogImage(self, event):
    """Update the secondary map viewer with the current fog-of-war overlay"""
    if (gv.SecondaryScreen):
      gv.SecondaryScreen.UpdateImage()
    return
    
  def OnOptionsFTP(self, event):
    """Set the username, password, and site for the ftp remote server"""
    dlg = FTP_OptionsDialogCore(self.frame)
    dlg.ShowModal()
    return

  def OnOptionsProgram (self, event):
    os.chdir(gv.root_directory)
    dlg = ProgramOptionsDialogCore(self.frame)
    result = dlg.ShowModal()
    if (result):
      #Grid Options subpanel
      gv.DisplayGrid = dlg.cbShowGrid.GetValue()
      self.frame.menubar.Check(PyMapperDialogs.mViewGrid, gv.DisplayGrid)
      gv.GridColor = dlg.cpkGridColor.GetColour()
      gv.GridPenStyle = dlg.GridLineStyle
      gv.GridPenWidth = dlg.spGridLineWidth.GetValue()
      gv.GridPen = dlg.GridLineStylePen
      gv.ShowGridCoordinates = dlg.ShowGridCoordinates.GetValue()
      gv.DrawGridOnTop = dlg.cbDrawGridOnTop.GetValue()
      gv.ChangeDefaultFolder = dlg.cbOpenToLastFolder.GetValue()
      gv.ReverseMouseWheel = dlg.cbReverseMouseWheel.GetValue()
      gv.ShowIntermediateGridLines = dlg.cbDrawIntermediateLines.GetValue()
      gv.IntermediateGridColor = dlg.cpkIntermediateGuideColor.GetColour()
      gv.IntermediateGridLinesInterval = dlg.spGuideInterval.GetValue()
      gv.GridScale = dlg.spGridScale.GetValue()
      gv.MapFogColor = dlg.cpkMapFogColor.GetColour()

      #background subpanel
      gv.DisplayBackground = dlg.cbShowBackground.GetValue()
      self.frame.menubar.Check(PyMapperDialogs.mViewBackground, gv.DisplayBackground)
      gv.BackgroundOpacity = dlg.BackgroundOpacityValue.GetValue()/100.0
      gv.MapPanelBackgroundColor = dlg.cpkBackgroundColor.GetColour()
      gv.OutlineTilesColor = dlg.cpkOutlineColor.GetColour()

      #program options subpanel
      gv.AutoSave = dlg.cbAutoSave.GetValue()
      gv.AutoSaveInterval = (dlg.AutoSaveTimer.GetValue()*60)
      gv.backup_directory = dlg.stAutoSavePath.GetLabel()
      if (gv.AutoSave == True):
        self.backuptimer.Start(gv.AutoSaveInterval*1000)
      gv.SaveIniFile = dlg.cbSaveIniFile.GetValue()
      gv.ReadSRDFileData = dlg.cbReadSRDFiles.GetValue()
      gv.Read5EditionFileData = dlg.cbRead5EditionFiles.GetValue()

      #tile options subpanel
      gv.TileOpacity = dlg.TileOpacityValue.GetValue()/100.0
      gv.hover_interval = dlg.HoverTimeInterval.GetValue()
      gv.DisplayOnHover = dlg.rbUseHoverOption.GetValue()
      gv.ResetTileStatistics = dlg.cbResetTileStats.GetValue()
      
      dual_value = gv.DualDisplayTileWindow
      gv.DualDisplayTileWindow = dlg.rbDualDisplayTileWindow.GetValue()
      if (gv.DualDisplayTileWindow):
        gv.DisplayOnHover = False
      if (dual_value == gv.DualDisplayTileWindow): #if we changed the display type, rebuild the grid
        self.DrawTileWindow(False)
      else:
        self.DrawTileWindow(True)
        
      #map icons subpanel
      gv.HighlightIcons = dlg.cbHighlightIcons.GetValue()
      gv.DisplayIconInformation = dlg.cbDisplayIconInformation.GetValue()
      gv.SnapIconToGrid = dlg.cbSnapIconsToGrid.GetValue()

      self.DrawMapWindow()
    dlg.Destroy()
    return

  def OnRecentFile(self, event):
    if (event.GetId() == PyMapperDialogs.mFileRecentFile1):
      if (self.FileList[4] == '-----'):
        return
      else:
        self.OnFileOpen(event, AddFile = False, selectedFile=self.FileList[4])
    elif (event.GetId() == PyMapperDialogs.mFileRecentFile2):
      if (self.FileList[3] == '-----'):
        return
      else:
        self.OnFileOpen(event, AddFile = False, selectedFile=self.FileList[3])
    elif (event.GetId() == PyMapperDialogs.mFileRecentFile3):
      if (self.FileList[2] == '-----'):
        return
      else:
        self.OnFileOpen(event, AddFile = False, selectedFile=self.FileList[2])
    elif (event.GetId() == PyMapperDialogs.mFileRecentFile4):
      if (self.FileList[1] == '-----'):
        return
      else:
        self.OnFileOpen(event, AddFile = False, selectedFile=self.FileList[1])
    elif (event.GetId() == PyMapperDialogs.mFileRecentFile5):
      if (self.FileList[0] == '-----'):
        return
      else:
        self.OnFileOpen(event, AddFile = False, selectedFile=self.FileList[0])
    return

  # Called whenever a paint event occurs on the main window
  def OnPaint(self, event):
    if (event.GetEventObject() == self.MapPanel):
      dc = wx.BufferedPaintDC(self.MapPanel, self.MapBuffer, wx.BUFFER_VIRTUAL_AREA)
    if (event.GetEventObject() == self.TilePanel):
      dc = wx.BufferedPaintDC(self.TilePanel, self.TileBuffer, wx.BUFFER_VIRTUAL_AREA)
    event.Skip()
    return

  def OnHelp_KeyboardShortcuts(self, event):
    text = ("The following keyboard shortcuts are available:\nF1\tHelp\nF12\tSwitch between tile, icon, and draw modes.\nDEL\tDelete current selected item.\nSPACE\tFlip tiles on the tile window.\nPgUp\tMove selected tile up in display order.\nPgDn\tMove selected tile down in display order.\nShift+PgUp\tMove to top of display order.\nShift+PgDn\tMove to bottom of display order.\nArrow keys\tRotate selected tile on map window.\nShift+Arrows\tMove selected tile 1 square in direction of arrow\n")
    dlg = HelpDialog(self.frame, text)
    dlg.ShowModal()
    dlg.Destroy()
    return

  def OnHelp_ProgramFoundation(self, event):
    dlg = ProgramFoundationDialog(self.frame)
    dlg.ShowModal()
    dlg.Destroy()
    return
  
  def OnHelp_RegisterProgram(self, event=None):
    dlg = UserDetailsDialog(self.frame)
    register = dlg.ShowModal()
    
    if (register):
      #process the user information and send it back to pymapper
      gv.UserEmail = dlg.txUserEmail.GetValue()
      gv.UserName = dlg.txUserName.GetValue()
      gv.UserReceiveUpdates = dlg.cbReceiveUpdates.GetValue()
      gv.UserSendCrashInfo = dlg.cbSendCrashReports.GetValue()
      gv.UserComments = dlg.txUserComments.GetValue()
      
      #Prepare and send email
      txt = "Please register "+gv.UserName+ " "+gv.UserEmail+" as a pymapper user.\n"
      txt += "Pymapper version " + str(VERSION) + " "
      if (gv.UserComments != ""):
        txt += "They had this to say about the program: " + gv.UserComments
      if (gv.UserReceiveUpdates):
        txt += "\n\nPlease send notification of program updates.\n"
      
      mail = MIMEText(txt)
      mail['subject'] = "Pymapper Registration"
      
      mailTo = 'register@pymapper.com'
      mail['to'] = "register@pymapper.com"
      
      mailFrom = 'register@pymapper.com'
      mail['from'] = 'register@pymapper.com'
      
      unm = 'register@pymapper.com'
      pd = '6LTuSvZoVgGxnIBt'
      
      try:
        server = smtplib.SMTP('mail.pymapper.com',26)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(unm, pd)
        server.sendmail(mailFrom, [mailTo], mail.as_string())
        server.quit()
      except:
        logging.error("RegisterProgram: Could not send registration email")
        wx.MessageBox("Pymapper encountered an unknown email server error.  Please email your registration info to help@pymapper.com")
        
      try:
        email_file = os.path.join(gv.root_directory,"email_info_v2.ini")
        email_info = open(email_file, "w")
      except:
        logging.error("RegisterProgram: Could not open email_info_v2.ini for writing")
    
        return False
      email_info.write((gv.UserName+"\n")) 
      email_info.write((gv.UserEmail+"\n"))
      email_info.write(("Receive Updates: "+str(gv.UserReceiveUpdates)))
      email_info.close()
      logging.info("Email registration recorded")
      wx.MessageBox("Thank you for registering pymapper!")
      
    dlg.Destroy()
    return register

  def OnHelp_About(self, event):
    description = """PyMapper is for use in preparing tile based maps for Role Playing Games.\n  It was written using Python 2.6, wxPython, and wxFormBuilder"""
    licence = """Contributions are welcome and will encourage the developer to continue updating and improving the software.

      Some parts of this program are used under license from other entities:
      Python v2.7.6,  http://www.python.org
      wxPython v2.8.12.1, http://www.wxpython.org

      Code editing and debugging performed using the excellent Wing IDE, http://www.wingware.com

      This software is distributed under the GNU public license.
      A copy of this license is located in the installation folder of this program, or online at http://www.gnu.org/licenses/gpl.txt
      Please contact us at bugs@pymapper.com for questions and bug reports."""
    info = wx.AboutDialogInfo()
    iconPath = os.path.join(gv.artwork_directory,'pymapper.png')
    info.SetIcon(wx.Icon(iconPath, wx.BITMAP_TYPE_PNG))
    info.SetName('PyMapper')
    info.SetVersion(VERSION)
    info.SetDescription(description)
    info.SetCopyright('(C)Copyright 2009-2015 Michael Seely')
    info.SetWebSite('http://www.pymapper.com/')
    info.SetLicence(licence)
    info.AddDeveloper('Michael Seely')
    info.AddDocWriter('Michael Seely')
    info.AddArtist('Richard Seely')
    #info.AddTranslator('Name')
    info.WebSite = ("http://www.pymapper.com/")
    wx.AboutBox(info)

  def ReadIniFile(self):
    #needs a tag
    logging.debug("Begin Reading pymapper.ini file")
    gv.DrawingSelectPen = wx.Pen(wx.Colour(255,0,0,255))
    self.frame.toolbar.ToggleTool(PyMapperDialogs.tShowIcons, True)
    self.frame.toolbar.ToggleTool(PyMapperDialogs.tShowDrawingObjects, True)

    self.frame.menubar.Enable(PyMapperDialogs.mEditCut, False)
    self.frame.menubar.Enable(PyMapperDialogs.mEditCopy, False)
    self.frame.menubar.Enable(PyMapperDialogs.mEditPaste, False)
    self.frame.menubar.Enable(PyMapperDialogs.mFileSave, False)

    self.frame.menubar.Enable(PyMapperDialogs.mEditSelectAll, False)
    self.frame.menubar.Enable(PyMapperDialogs.mEditUndo, False)

    self.frame.menubar.Enable(PyMapperDialogs.mViewZoomIn, False)
    self.frame.menubar.Enable(PyMapperDialogs.mViewZoomOut, False)
    self.frame.menubar.Enable(PyMapperDialogs.mViewBackground, False)
    logging.debug("End menubar enables")

    filename = os.path.join(gv.root_directory,"pymapper.ini")

    read_file = True
    settings_version = 2.2 #this is the last version without this tag
    gv.AutoSave = False #set to false unless BACKUP tag is read in
    pagelist = []

    if (not(os.access(filename, os.F_OK))):
      self.SaveIniFile()  #create default file
      logging.debug("pymapper.ini not found, created default file instead")

    try:
      ini = open(filename, 'r')
    except IOError:
      logging.warning("Could not open .ini file for reading %s", filename)
      read_file = False

    if (read_file == True):
      header = True
      line = ini.readline()
      line = line.rstrip('\n\r')
      info = line.split()
      if (info == []):
        logging.warning("ReadIniFile:  Could not read .ini file; empty file")
        ini.close()
        return
      while (header == True):
        if (info[0] == '#'):
          #reading and empty line, or a comment lines
          line = ini.readline()
          info = line.split()
        if ((info == []) or (info[0] != '#')):
          header = False
      while (read_file == True):
        if (info == []):
          #read an empty line, continue on to the next line
          pass
        elif (info[0] == 'SHOW_TIPS'):
          line = ini.readline()
          dataline = line.rstrip(' \n\r')
          info = line.split()
          if (info[0] == 'True'):
            gv.ShowTips = True
          else:
            gv.ShowTips = False
          gv.LastTip = int(info[1])
        elif (info[0] == 'SETTINGS_VERSION'):
          settings_version = float(info[1])
        elif (info[0] == 'NO_TUTORIAL'):
          gv.ShowTutorial = False
        elif (info[0] == 'SNAP_ICONS'):
          if (info[1] == 'True'):
            gv.SnapIconToGrid = True
          else:
            gv.SnapIconToGrid = False
        elif (info[0] == 'SHOW_ICON_NAMES'):
          if (info[1] == 'True'):
            gv.ShowIconNamesOnMap = True
          else:
            gv.ShowIconNamesOnMap = False
          self.frame.menubar.Check(PyMapperDialogs.mShowIconNamesOnMap, gv.ShowIconNamesOnMap)
        elif (info[0] == 'SHOW_GRID_COORDINATES'):
          if (info[1] == 'True'):
            gv.ShowGridCoordinates = True
          else:
            gv.ShowGridCoordinates = False
          self.frame.menubar.Check(PyMapperDialogs.mViewGridCoordinates, gv.ShowGridCoordinates)
        elif (info[0] == 'GRID_SCALE'):
          gv.GridScale = int(info[1])
        elif (info[0] == 'RESET_TILE_STATISTICS_BY_PAGE'):
          if (info[1] == 'True'):
            gv.ResetTileStatistics = True
          else:
            gv.ResetTileStatistics = False
        elif (info[0] == 'LIMIT_TILE_USAGE'):
          if (info[1] == 'True'):
            gv.LimitTiles = True
            self.frame.toolbar.SetToolNormalBitmap(PyMapperDialogs.tTileQuantity, self.bmpTQ_Single)
          else:
            gv.LimitTiles = False
            self.frame.toolbar.SetToolNormalBitmap(PyMapperDialogs.tTileQuantity, self.bmpTQ_Unlimited)
        elif (info[0] == 'PRINT_RESOLUTION'):
          gv.PrintResolution = int(info[1])
          gv.SavePrintResolution = True
        elif (info[0] == 'OUTLINE_ON_HOVER'):
          if (info[1] == 'True'):
            gv.OutlineOnHover = True
          else:
            gv.OutlineOnHover = False
        elif (info[0] == 'SHOW_DRAWING_HANDLES'):
          if (info[1] == 'True'):
            gv.DrawHandles = True
            self.frame.toolbar.ToggleTool(PyMapperDialogs.tShowDrawingHandles, True)
          else:
            gv.DrawHandles = False
            self.frame.toolbar.ToggleTool(PyMapperDialogs.tShowDrawingHandles, False)
        elif (info[0] == 'PYMAPPER_WINDOW'):
          gv.WindowExtents.x = int(info[1])
          gv.WindowExtents.y = int(info[2])
          gv.WindowExtents.width = int(info[3])
          gv.WindowExtents.height = int(info[4])
        elif (info[0] == 'TILESET_PAGES'):
          read_pages = True
          while (read_pages):
            line = ini.readline().rstrip('\n\r')
            if (line == 'END_TILE_PAGES'):
              read_pages = False
              for pagename in pagelist:
                self.RTilebookAddPage(name=pagename)
            else:
              pagelist.append(line)
        elif (info[0] == 'TILESET'):
          pagelist = []
          setfile = ini.readline().rstrip(' \n\r')
          if (settings_version >= 3.0):
            setname = ini.readline().rstrip('\n\r')
            for page in gv.TilePageList:
              for tileset in page.tilesets:
                if (tileset == setname):
                  pagelist.append(page.PageName)
          else:
            pagelist = []
          self.ReadTilesetFile(setfile, False)
        elif (info[0] == 'TILESET_PAGE_ASSIGNMENT'):
          pagelist = [] #this is a list of tilesets assigned to a page
          read_lines = int(info[1]) #this is the number of tilesets assigned to the page
          target_page = ini.readline().rstrip('\n\r') #This is the page name
          while (read_lines):
            line = ini.readline().rstrip('\n\r') #this is the tileset name
            if (not(line in pagelist)):
              pagelist.append(line)
            read_lines -= 1
          page = Page_Record()
          for page in gv.TilePageList:
            if (page.PageName == target_page):
              #reset the pagelist since ReadTilesets will append items 
              page.tilesets = []
              for tileset_name in pagelist:
                empty_page = True
                for tileset in gv.tilesets:
                  if (tileset_name == tileset.Name) and (tileset.loaded):
                    empty_page = False
                    break
                if (not empty_page):
                  page.tilesets.append(tileset_name)
              break
        elif (info[0] == 'BACKUP'):
          line = ini.readline()
          folder = line.rstrip(' \n\r')
          if (os.access(folder, os.F_OK)):
            gv.backup_directory = folder
            gv.AutoSave = True
          else:
            wx.MessageBox(message="Invalid backup folder specified.\nCheck program options to specify folder", caption="Error reading .ini file", style=wx.ICON_EXCLAMATION)
            gv.AutoSave = False
        elif (info[0] == 'TILE_ZOOM'):
          line = ini.readline()
          info = line.split()
          gv.TileZoomFactor = int(info[0])
          gv.TileZoomIncrement = int(info[1])
        elif (info[0] == 'MAP_ZOOM'):
          line = ini.readline()
          info = line.split()
          gv.MapZoomFactor = int(info[0])
          gv.MapZoomIncrement = int(info[1])
        elif (info[0] == 'TILE_BORDER'):
          line = ini.readline()
          info = line.split()
          gv.tileborderwidth = int(info[0])
        elif (info[0] == 'CONDITION_COLOR_BLINDED'):
          gv.ConditionColors.BlindedColor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
        elif (info[0] == 'CONDITION_COLOR_CHARMED'):
          gv.ConditionColors.CharmedColor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
        elif (info[0] == 'CONDITION_COLOR_CONCENTRATING'):
          gv.ConditionColors.ConcentratingColor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
        elif (info[0] == 'CONDITION_COLOR_DEAFENED'):
          gv.ConditionColors.DeafenedColor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
        elif (info[0] == 'CONDITION_COLOR_FRIGHTENED'):
          gv.ConditionColors.FrightenedColor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
        elif (info[0] == 'CONDITION_COLOR_GRAPPLED'):
          gv.ConditionColors.GrappledColor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
        elif (info[0] == 'CONDITION_COLOR_INCAPACITATED'):
          gv.ConditionColors.IncapacitatedColor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
        elif (info[0] == 'CONDITION_COLOR_INVISIBLE'):
          gv.ConditionColors.InvisibleColor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
        elif (info[0] == 'CONDITION_COLOR_PARALYZED'):
          gv.ConditionColors.ParalyzedColor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
        elif (info[0] == 'CONDITION_COLOR_PETRIFIED'):
          gv.ConditionColors.PetrifiedColor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
        elif (info[0] == 'CONDITION_COLOR_POISONED'):
          gv.ConditionColors.PoisonedColor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
        elif (info[0] == 'CONDITION_COLOR_PRONE'):
          gv.ConditionColors.ProneColor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
        elif (info[0] == 'CONDITION_COLOR_RESTRAINED'):
          gv.ConditionColors.RestrainedColor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
        elif (info[0] == 'CONDITION_COLOR_STUNNED'):
          gv.ConditionColors.StunnedColor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
        elif (info[0] == 'CONDITION_COLOR_TURNED'):
          gv.ConditionColors.TurnedColor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
        elif (info[0] == 'CONDITION_COLOR_UNCONSCIOUS'):
          gv.ConditionColors.UnconsciousColor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
        elif (info[0] == 'CONDITION_BAR_THICKNESS'):
          gv.ConditionBarThickness = int(info[1])
        elif (info[0] == 'TILE_BACKGROUND'):
          line = ini.readline()
          info = line.split()
          gv.TilePanelBackgroundColor = wx.Colour(int(info[0]), int(info[1]),
                                                  int(info[2]), int(info[3]))
        elif (info[0] == 'MAP_BACKGROUND'):
          line = ini.readline()
          info = line.split()
          gv.MapPanelBackgroundColor = wx.Colour(int(info[0]), int(info[1]),
                                                 int(info[2]), int(info[3]))
        elif (info[0] == 'GRID_OPTIONS'):
          line = ini.readline()
          info = line.split()
          if (info[0] == 'True'):
            gv.DisplayGrid = True
            self.frame.menubar.Check(PyMapperDialogs.mViewGrid, True)
            self.frame.toolbar.ToggleTool(PyMapperDialogs.tShowGrid, True)
          else:
            gv.DisplayGrid = False
            self.frame.menubar.Check(PyMapperDialogs.mViewGrid, False)
            self.frame.toolbar.ToggleTool(PyMapperDialogs.tShowGrid, False)
          gv.GridColor = wx.Colour(int(info[1]), int(info[2]), int(info[3]), int(info[4]))
          gv.GridPenWidth = int(info[5])
          gv.GridPenStyle = int(info[6])
        elif (info[0] == 'GRID_ON_TOP'):
          gv.DrawGridOnTop = True
        elif (info[0] == 'KEEP_DEFAULT_FOLDERS'):
          gv.ChangeDefaultFolder = False
        elif (info[0] == 'HOVER_OPTIONS'):
          line = ini.readline()
          info = line.split()
          gv.hover_interval = int(info[0])
          #info[1] was the flag to set the gv.DisplayOnHover variable.
          #Removed in v5.1 but retained in the .ini file for backward compatibility.
        elif (info[0] == 'DUAL_TILE_DISPLAY'):
          if (info[1] == 'True'):
            gv.DualDisplayTileWindow = True
            gv.DisplayOnHover = False
          else:
            gv.DualDisplayTileWindow = False
            gv.DisplayOnHover = True
          self.frame.menubar.Check(PyMapperDialogs.mViewDualTileDisplay, gv.DualDisplayTileWindow)
        elif (info[0] == 'SELECTION_OPTIONS'):
          line = ini.readline()
          info = line.split()
          gv.SelectionColor = wx.Colour(int(info[0]), int(info[1]),
                                        int(info[2]), int(info[3]))
          gv.SelectionPenWidth = int(info[4])
          gv.SelectionPenStyle = int(info[5])
        elif (info[0] == 'BACKGROUND_OPTIONS'):
          line = ini.readline()
          info = line.split()
          if (info[0] == 'True'):
            gv.DisplayBackground = True
            self.frame.menubar.Check(PyMapperDialogs.mViewBackground, True)
            self.frame.toolbar.ToggleTool(PyMapperDialogs.tShowBackground, True)
          else:
            gv.DisplayBackground = False
            self.frame.menubar.Check(PyMapperDialogs.mViewBackground, False)
            self.frame.toolbar.ToggleTool(PyMapperDialogs.tShowBackground, False)
          gv.BackgroundOpacity = float(info[1])
          self.MapStruct.bg_displaymode = str(info[2])
          self.MapStruct.bg_x_dimension = int(info[3])
          self.MapStruct.bg_y_dimension = int(info[4])
          f_name = ini.readline()
          f_name = f_name.rstrip('\n\r')
          self.MapStruct.background_filename = f_name
        elif (info[0] == 'AUTO_SAVE'):
          line = ini.readline()
          info = line.split()
          if (info[0] == 'True'):
            gv.AutoSave = True
          else:
            gv.AutoSave = False
          gv.AutoSaveInterval = float(info[1])
        elif (info[0] == 'READ_SRD_ON_STARTUP'):
          line = ini.readline()
          info = line.split()
          if (info[0] == 'True'):
            gv.ReadSRDFileData = True
          else:
            gv.ReadSRDFileData = False
        elif (info[0] == 'READ_5E_ON_STARTUP'):
          line = ini.readline()
          info = line.split()
          if (info[0] == 'True'):
            gv.Read5EditionFileData = True
          else:
            gv.Read5EditionFileData = False
        elif (info[0] == 'SAVE_INI_ON_CLOSE'):
          line = ini.readline()
          info = line.split()
          if (info[0] == 'True'):
            gv.SaveIniFile = True
          else:
            gv.SaveIniFile = False
        elif ((info[0] == '#') or (info[0] == [])):
          #comment line, or an empty line, skip reading
          continue
        #add other ini things here
        elif (info[0] == 'END_INI'):
          read_file = False
        line = ini.readline()
        line = line.rstrip('\n\r')
        info = line.split()

      ini.close()

    if (gv.FontData == None):
      gv.FontData = wx.FontData()

    if (gv.backup_directory == None):
      gv.backup_directory = os.path.join(gv.root_directory,"backup")
      try:
        os.mkdir(gv.backup_directory)
      except OSError:
        gv.backup_directory = gv.root_directory

    return True

  def OnNotImplemented(self, event):
    wx.MessageBox('Option not yet implemented')

  def TileWindowDClick(self, event):
    if (sys.platform == 'win32'):
      if (gv.SelectMode == 'draw'):
        #tile window is inactive while drawing
        return
      mouse_pos = self.TilePanel.CalcUnscrolledPosition(event.GetPosition().x, event.GetPosition().y)
      position = wx.Point(mouse_pos[0], mouse_pos[1])
      for tile in self.tilelist:
        foundtile = tile.TileRect.Contains(position) 
        if (foundtile):
          if (tile.showingBside):
            tile.showingBside = False
            tile.tiledisplay = tile.sideA
          elif (tile.sideB != None):
            tile.showingBside = True
            tile.tiledisplay = tile.sideB
          self.DrawTileWindow()
      else:
        #Since dragging off of the tile panel does not work in non-windows systems, 
        #we double click to get a tile into the map panel
        self.AddTileFromTilePanel()
    return

  def FindTilesetFiles(self):
    """Find the installed tilesets and populate gv.tilesets"""
    start_dir = os.getcwd()
    dir_listing = os.listdir(gv.tiles_directory)
    folders = []

    #find the folders in the tiles folder
    for item in dir_listing:
      if (os.path.isdir(os.path.join(gv.tiles_directory,item))):
        folders.append(item)
    tempsets = gv.tilesets
    #find the tileset files

    for folder in folders:
      if ('__px' in folder):  #check for special case tileset without a .set file
        os.chdir(os.path.join(gv.tiles_directory, folder))
        images = glob.glob('*.jpg') + glob.glob('*.png')
        info = folder.split('_')
        try:  
          #look to see if we can determine the resolution from the folder name.  Should be '100_px'
          resolution = int(info[0])
          if (resolution <= 0):
            continue
        except:
          continue
        if (sys.platform == 'win32'):  #This is here to allow for backward compatibility with loading
          px_filename = folder+".set"  #of _mac tilesets that are still in the old tileset files.
        else:
          px_filename = folder+'_mac.set'
        pxTileset = open(px_filename, 'w')
        pxTileset.write("# PX Abbreviated Tileset automatically generated by PyMapper::FindTilesetFiles.   Do not edit this file.\n")
        pxTileset.write("TILESET\n")
        pxTileset.write("VERSION %f\n" % gv.TilesetSpecificationVersion)
        pxTileset.write("NAME "+ folder + "\n")
        pxTileset.write("SET_ID "+folder+ "\n")
        pxTileset.write("NUM_SETS 1\n")
        index = 0
        for image in images:
          pxTileset.write("TILE %d\n" % index)
          pxTileset.write("IMAGE_A tiles/%s/%s\n" % (folder, image))
          pxTileset.write("NO_IMAGE_B\n")
          pxTileset.write("TILE_COUNT 1\n")
          tempImage = wx.Image(image, wx.BITMAP_TYPE_ANY)
          (xsize, ysize) = tempImage.GetSize()
          pxTileset.write("XSIZE %d\n" % max(1,(xsize//resolution))) #provide a minimum size of 1 square
          pxTileset.write("YSIZE %d\n" % max(1,(ysize//resolution)))
          pxTileset.write("ENDTILE\n")
          index +=1
        pxTileset.write("END\n")
        pxTileset.close()
      
    for folder in folders:
      tileset_record = TileSet()
      os.chdir(os.path.join(gv.tiles_directory,folder))
      if (sys.platform == 'win32'):      #v9.6: for compatibility with Tileset file selection based on OS
        contents = glob.glob('*.set')
      else:
        contents = glob.glob('*_mac.set')
      for item in contents:
        tileset_record.filename = os.path.join(gv.tiles_directory,folder,item)
        tileset_record.SetID = folder
        gv.tilesets.append(tileset_record)
        
    tileset = TileSet()
    for tileset in gv.tilesets:
      try:
        setfile = open(tileset.filename)
      except IOError:
        logging.critical("Could not open %s in PymapperAppMain::FindTilesetFiles", tileset.filename)
        return False
      name_found = False
      setID_found = False
      num_sets_found = False
      read_file = True
      while (read_file):
        if (name_found and setID_found and num_sets_found):
          read_file = False
        line = setfile.readline()
        info = line.rstrip(" \n\r").split()
        if (info[0] == 'NAME'):
          info.pop(0) #remove the tag
          tileset.Name = info[0]
          info.pop(0)
          while (len(info) > 0):
            tileset.Name += " "
            tileset.Name += info[0]
            info.pop(0)
          name_found = True
        elif (info[0] == 'NUM_SETS'):
          tileset.copies = int(info[1])
          num_sets_found = True
        elif (info[0] == 'SET_ID'):
          tileset.SetID = info[1]
          setID_found = True
      setfile.close()

    return

  def FindTileOnTilePanel(self, position):
    found = False
    for tile in self.tilelist:
      if (tile.ShowOnTilePanel == True):
        found = tile.TileRect.Contains(position)
        if (found):
          return tile
    return None

  def TileWindowLClickDown(self, event):
    if (gv.SelectMode == 'draw') or (gv.SelectMode == 'fog'):
      #tile window is inactive while drawing or fog tools are active
      return
    mouse_pos = self.TilePanel.CalcUnscrolledPosition(event.GetPosition().x, event.GetPosition().y)
    position = wx.Point(mouse_pos[0], mouse_pos[1])
    foundtile = False
    for tile in self.tilelist:
      if ((tile.ShowOnTilePanel == True) and (tile.dimmed == False)):
        foundtile = tile.TileRect.Contains(position)
        if (foundtile):
          tile.selected = True
          self.AllowDrag = True #allow dragging of image on the MapPanel
          mapimage = tile.tiledisplay
          Xscale = tile.actualXsize*gv.MapZoomFactor
          Yscale = tile.actualYsize*gv.MapZoomFactor
          mapimage = mapimage.Scale(Xscale, Yscale, wx.IMAGE_QUALITY_HIGH)
          mapimage = wx.BitmapFromImage(mapimage)
          self.dragImage = wx.DragImage(mapimage, wx.StockCursor(wx.CURSOR_HAND)) #this is the image to move on the MapPanel
          #do not break out of loop, need to deselect other tiles also
        else:
          #check for the B side display when showing both sides
          if (gv.DualDisplayTileWindow) and (tile.sideB):
            foundtile = tile.TileRectB.Contains(position)
            if (foundtile):
              tile.selected = True
              self.AllowDrag = True #allow dragging of image on the MapPanel
              mapimage = tile.sideB
              tile.showingBside = True
              Xscale = tile.actualXsize*gv.MapZoomFactor
              Yscale = tile.actualYsize*gv.MapZoomFactor
              mapimage = mapimage.Scale(Xscale, Yscale, wx.IMAGE_QUALITY_HIGH)
              mapimage = wx.BitmapFromImage(mapimage)
              self.dragImage = wx.DragImage(mapimage, wx.StockCursor(wx.CURSOR_HAND))
            else:
              tile.selected = False
          else:
            tile.selected = False #deselect all the other tiles
    #if no tile was selected, de-select highlighting on map tiles
    if (not foundtile):
      for tile in self.maplist:
        tile.highlight = False
    self.DrawMapWindow()
    self.DrawTileWindow()
    if (gv.rtc_open == False):
      self.TilePanel.SetFocus()
    return

  def OnChangeTileQuantity(self, event):
    if (gv.LimitTiles):
      self.frame.toolbar.SetToolNormalBitmap(PyMapperDialogs.tTileQuantity, self.bmpTQ_Unlimited)
      gv.LimitTiles = False
    else:
      self.frame.toolbar.SetToolNormalBitmap(PyMapperDialogs.tTileQuantity, self.bmpTQ_Single)
      gv.LimitTiles = True
    for tile in self.tilelist:
      if ((gv.LimitTiles == True) and (tile.num_used >= tile.copies)):
        tile.dimmed = True
      else:
        tile.dimmed = False
    self.DrawTileWindow()
    return

  def OnImportBackground(self, event):
    pageindex = self.nbMapNotebook.GetSelection()
    page = gv.MapPageList[pageindex]
    old_file = page.background_filename
    dlg = BackgroundRegistrationDialog(self.frame, page)
    if (dlg.ShowModal()):
      if (dlg.rbShowOnCurrentPage.GetValue()):
        #show on the current selected page
        page.background = dlg.backgroundImage
        page.background_filename = dlg.background_filename
        page.background_filepath = dlg.background_filepath
        if (dlg.rbCenterBackground.GetValue() == True):
          page.bg_displaymode = 'Center'
        elif (dlg.rbRegisterBackground.GetValue() == True):
          page.bg_displaymode = 'Register'
        elif (dlg.rbTileBackground.GetValue() == True):
          page.bg_displaymode = 'Tile'
        page.bg_x_dimension = dlg.grid_width
        page.bg_y_dimension = dlg.grid_height
      elif (dlg.rbShowOnAllPages.GetValue()):
        #show the selected image on all pages
        for item in gv.MapPageList:
          item.background = dlg.backgroundImage
          item.background_filename = dlg.background_filename
          item.background_filepath = dlg.background_filepath
          if (dlg.rbCenterBackground.GetValue() == True):
            item.bg_displaymode = 'Center'
          elif (dlg.rbRegisterBackground.GetValue() == True):
            item.bg_displaymode = 'Register'
          elif (dlg.rbTileBackground.GetValue() == True):
            item.bg_displaymode = 'Tile'
          item.bg_x_dimension = dlg.grid_width
          item.bg_y_dimension = dlg.grid_height
    gv.DisplayBackground = True
    dlg.Destroy()
    self.DrawMapWindow()
    return

  def OnExit(self, event=None):
    if (not self.frame):
      return
    if (gv.SaveIniFile == True):
      self.SaveIniFile()
    #Closes the application
    self.SaveRecentFileList()
    if (gv.PromptSave):
      warning = wx.MessageDialog(self.frame, "Save Existing Map?", "Unsaved changes found!", wx.YES_NO |wx.CANCEL | wx.ICON_QUESTION)
      result = warning.ShowModal()
      if (result == wx.ID_CANCEL):
        return
      elif (result == wx.ID_YES):
          self.SaveMapFile(self.MapStruct.filename)
    dlg = wx.MessageDialog(self.frame, "Exit the program?", "Exit PyMapper", wx.YES_NO | wx.ICON_QUESTION)
    if dlg.ShowModal() == wx.ID_YES:
      if (gv.SaveSRD_Traps):
        #pickle the SRD data files
        self.frame.SetStatusText("Saving Traps file")
        datafile = open(os.path.join(gv.srd_directory,"d20","traps.obj"), 'w')
        pickle.dump(gv.TrapList, datafile)
        self.frame.SetStatusText("Saving Traps file")
        datafile.close()

      if (gv.SaveSRD_Monsters):
        datafile = open(os.path.join(gv.srd_directory,"d20","monsters.obj"), 'w')
        self.frame.SetStatusText("Saving Monsters file")
        pickle.dump(gv.MonsterList, datafile)
        self.frame.SetStatusText("Monsters file saved")
        datafile.close()

      if (gv.SaveSRD_Spells):
        self.frame.SetStatusText("Saving Spells file")
        datafile = open(os.path.join(gv.srd_directory,"d20","spells.obj"), 'w')
        pickle.dump(gv.d20_Spell_List, datafile)
        datafile.close()
        self.frame.SetStatusText("Saving Spells file")

      if (gv.SaveSRD_Feats):
        self.frame.SetStatusText("Saving Feats file")
        datafile = open(os.path.join(gv.srd_directory,"d20","feats.obj"), 'w')
        pickle.dump(gv.NPC_Feat_Info, datafile)
        datafile.close()
        self.frame.SetStatusText("Saving Feats file")

      if (gv.SaveSRD_ClassSkills):
        self.frame.SetStatusText("Saving Class Skills file")
        datafile = open(os.path.join(gv.srd_directory,"d20","class_skills.obj"), 'w')
        pickle.dump(gv.NPC_Skill_Info, datafile)
        datafile.close()
        self.frame.SetStatusText("Saving Class Skills file")

      if (gv.SaveSRD_ClassTable):
        self.frame.SetStatusText("Saving Class Table file")
        datafile = open(os.path.join(gv.srd_directory,"d20","class_table.obj"), 'w')
        pickle.dump(gv.NPC_Class_Info, datafile)
        datafile.close()
        self.frame.SetStatusText("Saving Class Table file")
        
      if (gv.SaveSRD_Names):
        self.frame.SetStatusText("Saving Names file")
        datafile = open(os.path.join(gv.srd_directory,"d20","names.obj"), 'w')
        pickle.dump(gv.NPC_Names, datafile)
        datafile.close()
        self.frame.SetStatusText("Saving Names file")

      if (gv.SaveSRD_Races):
        self.frame.SetStatusText("Saving Races file")
        datafile = open(os.path.join(gv.srd_directory,"d20","races.obj"), 'w')
        pickle.dump(gv.SRD_RacesList, datafile)
        datafile.close()
        self.frame.SetStatusText("Saving Races file")
        
      dlg.Destroy()
      self.frame.Destroy()  # release the frame memory
      logging.debug("PymapperAppMain::OnExit")
      logging.shutdown()
    return

  def OnFileOpen(self, event=None, AddFile=True, selectedFile=None):
    ImportFile = False
    if (event):
      if (event.GetId() == PyMapperDialogs.mFileOpen) or (event.GetId() == PyMapperDialogs.tFileOpen):
        folder = gv.maps_directory
        wcard = map_wildcard
        name = "NewMap"
        geomorphFlag = False
        DialogCaption = "Open Map File"
        ImportFile = False
      elif (event.GetId() == PyMapperDialogs.mFileImportFile):
        #import to a new page
        folder = gv.maps_directory
        wcard = map_wildcard
        name = "ImportMap"
        geomorphFlag = False
        DialogCaption = "Import Map File"
        ImportFile = True
        #self.RMapbookAddPage()  #removed in 9.1: We should open the file and import whatever pages are defined therein.
        #self.nbMapNotebook.SetSelection(len(gv.MapPanelList)-1)
        #self.ChangeMapNotebookPage()
      else:
        folder = gv.geomorphs_directory
        wcard = geomorph_wildcard
        name = "NewGeomorph"
        geomorphFlag = True
        DialogCaption = "Open Geomorph File"
        ImportFile = False
    if (selectedFile):  #change current working directory to the given path
      if (sys.platform == 'win32'):
        position = selectedFile.rfind('\\')
      else:
        position = selectedFile.rfind('/')
      folder = selectedFile[0:position]
      if (os.path.isdir(folder)):
        os.chdir(folder)  #set the current working directory
      else:
        #could not find the specified path
        logging.warning("Could not find %s", folder)
        text = "Could not find the folder named " + folder
        wx.MessageBox(message=text, caption="Error", style=wx.ICON_ERROR)
        return
    if (gv.PromptSave == True):
      warning = wx.MessageDialog(self.frame, "Save existing map?", "", wx.YES_NO |wx.CANCEL | wx.ICON_QUESTION)
      result = warning.ShowModal()
      if (result == wx.ID_CANCEL):
        return
      elif (result == wx.ID_YES):
        self.SaveMapFile(self.MapStruct.filename)
    if (selectedFile == None):
      dlg = wx.FileDialog(self.frame, message=DialogCaption, defaultDir=folder,
                          defaultFile="", wildcard=wcard, style=wx.OPEN | wx.CHANGE_DIR)
      if dlg.ShowModal() == wx.ID_OK:
        selectedFile = dlg.GetPath()
        if (gv.ChangeDefaultFolder):
          gv.maps_directory = dlg.GetDirectory()
          os.chdir(gv.maps_directory)  #change to selected map folder
        self.frame.SetLabel("PyMapper "+VERSION+": " + selectedFile)
        dlg.Destroy()
      else:
        dlg.Destroy()
        return

    #reset the data lists
    if (not ImportFile):  #we are opening a file from disk, clear all lists
      self.maplist = []
      self.textlist = []
      gv.RoomList = []
      self.DrawingList = []
      gv.MapPanelList = []
      gv.MapPageList = []
      self.nbMapNotebook.DeleteAllPages()

      #reset the tilelists
      for tile in self.tilelist:
        tile.num_used = 0
        tile.selected = False
        tile.dimmed = False
        tile.mapdisplay = None

    result = self.ReadMapFile(selectedFile, ImportFile)

    if (result == True):
      self.MapStruct.filename = selectedFile
      if (AddFile):
        self.UpdateFileList(selectedFile)
      self.frame.menubar.Enable(PyMapperDialogs.mFileSave, True)
      self.MapStruct.GridExtents = self.CalculateMapExtents(self.maplist)
      #if there are any rooms, read the tags that might be in them
      
      #set up the layer filters
      if (gv.LayerDialog):
        gv.ActiveLayer = 0  #default to base layer
        gv.LayerDialog.UpdateLists()
      self.RMapClickShowAll()
    else:  #failed ReadMapFile for some reason.  We need a valid MapPanel to draw on
      self.RMapbookAddPage(name='Map')
    self.DrawMapWindow()
      
    return


  def ReadRecentFileList(self):
    filename = os.path.join(gv.root_directory,"filelist.ini")
    try:
      listfile = open(filename, 'r')
    except IOError:
      logging.error("Could not open file %s", filename)
      self.FileList = []
      return
    done = False
    while (done == False):
      line = listfile.readline()
      if (line == ""):
        done = True
      else:
        line = line.rstrip("\n\r")
        self.UpdateFileList(line)
    listfile.close()
    return

  def SaveRecentFileList(self):
    filename = gv.root_directory + "filelist.ini"
    try:
      listfile = open(filename, 'w')
    except IOError:
      logging.error("Could not save recent file list")
      return
    for text in self.FileList:
      listfile.write(str(text)+"\n")
    listfile.close()
    return

  def UpdateFileList(self, filename):
    self.FileList.append(filename)
    if (len(self.FileList) > 5):
      del self.FileList[0]
    self.frame.RecentFile5.SetItemLabel(self.FileList[0])
    self.frame.RecentFile4.SetItemLabel(self.FileList[1])
    self.frame.RecentFile3.SetItemLabel(self.FileList[2])
    self.frame.RecentFile2.SetItemLabel(self.FileList[3])
    self.frame.RecentFile1.SetItemLabel(self.FileList[4])
    return

  def OnFileSave(self, event):
    # this is called from selecting File | Save
    if (self.MapStruct.geomorph):
      if (self.selectlist != []):
        for x in self.selectlist:
          x.selected = False
        self.selectlist = []
        self.DrawMapWindow()
      pgf_dlg = GeomorphSaveDialog(self.frame, self.MapBuffer, self.MapStruct.geomorphData)
      result = pgf_dlg.ShowModal()
      if (result):
        self.MapStruct.geomorphData.geomorphBottom = pgf_dlg.geomorphBottom
        self.MapStruct.geomorphData.geomorphLeft = pgf_dlg.geomorphLeft
        self.MapStruct.geomorphData.geomorphRight = pgf_dlg.geomorphRight
        self.MapStruct.geomorphData.geomorphTop = pgf_dlg.geomorphTop
        self.MapStruct.geomorph = True
        self.MapStruct.geomorphData.preview = self.MapStruct.filename + ".bmp"
        pgf_dlg.BitmapDisplay.SaveFile(self.MapStruct.geomorphData.preview, wx.BITMAP_TYPE_BMP)
      else: #canceled off of the geomorph dialog
        return
    self.SaveMapFile(self.MapStruct.filename)
    gv.PromptSave = False
    return

  def OnTilesetEdit(self, event):
    dlg = TilesetEditorDialogCore(self.frame)
    if (dlg.ShowModal() == True):
      if (dlg.TilesetFilenamePath != None):
        result = self.ReadTilesetFile(dlg.TilesetFilenamePath, False)
        if result == True:
          self.DrawTileWindow(True)
          if (gv.LayerDialog):
            gv.LayerDialog.UpdateLists()  #rebuild the list and display
    dlg.Destroy()
    return

  def OnTilesetBrowser(self, event):
    main_tileset = TileSet()
    dlg_tileset = TileSet()
    sets_changed = False
    dlg = TilesetBrowserDialog(self.frame)

    result = dlg.ShowModal()
    if (result == True):
      if (dlg.rbImportToCurrentPage.GetValue()):
        gv.TileImportLocation = 'CurrentPage'
      elif (dlg.rbImportToNewPage.GetValue()):
        gv.TileImportLocation = 'NewPage'
      for index in range(0,len(gv.tilesets)):
        if (dlg.lsTilesetList.GetItemBackgroundColour(index) == dlg.LoadQueueColor):
          set_name = dlg.lsTilesetList.GetItemText(index)
          for tileset in gv.tilesets:
            if (tileset.SetID == 'MARKERS'):
              #the markers are internal and cannot be loaded this way
              continue
            elif (tileset.Name == set_name) and (not tileset.loaded):
              result = self.ReadTilesetFile(tileset.filename, False)
              if (result == False):
                msg_dlg = wx.MessageDialog(self.frame, 'Error at OnTilesetBrowser', 'Tileset Read Error', wx.OK | wx.ICON_ERROR)
                result = msg_dlg.ShowModal()
                msg_dlg.Destroy()
              else:
                sets_changed = True
              break
        if (dlg.lsTilesetList.GetItemBackgroundColour(index) == dlg.UnloadQueueColor):
          set_name = dlg.lsTilesetList.GetItemText(index)
          #check page assignments and remove
          for page in gv.TilePageList:
            try:
              page.tilesets.remove(set_name)
            except ValueError:
              #set name was not shown on this list, skip
              pass
              
          removal_list = []
          for tileset in gv.tilesets:
            if (tileset.SetID == 'MARKERS'):
              #the markers are internal and cannot be unloaded.
              continue
            elif (tileset.Name == set_name) and (tileset.loaded):
              tileset.loaded = False
              sets_changed = True
              for tile in self.tilelist:
                if (tile.tilesetID == tileset.SetID):
                  removal_list.append(tile)
          for tile in removal_list:
            self.tilelist.remove(tile)

    if (sets_changed):
      self.DrawTileWindow(True)

    return
  
  def OnTilesetCreateFromCompositeImage(self,event):
    '''Create a tileset using a single composite image.  Individual tiles are extracted from the image and saved in a folder under the /tiles/ folder.'''
    dlg = TilesetBuilderCompositeDialog(self.frame)
    dlg.ShowModal()
    return
  
  
  #Load a set of tiles from a chosen file
  def OnImportTilesetFromDialog(self, event):
    dlg = wx.FileDialog(self.frame, message="Choose a tileset", defaultDir=gv.tiles_directory, defaultFile="", wildcard=tilesets_wildcard, style=wx.OPEN)
    if dlg.ShowModal() == wx.ID_OK:
      TilesetFile = dlg.GetFilename()
      TilesetPathName = dlg.GetPath()
      result = self.ReadTilesetFile(TilesetPathName, False)
      if result == False:
        msg_dlg = wx.MessageDialog(self.frame, 'Error at ReadTilesetFile', 'Tileset Read Error', wx.OK | wx.ICON_ERROR)
        logging.error("ImportTilesetFromDialog: Tileset Read Error")
        result = msg_dlg.ShowModal()
        msg_dlg.Destroy()
        return False
      else:
        #Arrange all of the tiles in the available space of the tile window
        self.frame.menubar.Enable(PyMapperDialogs.mFileOpen, True)
        self.DrawTileWindow(True)
        if (gv.LayerDialog):
          gv.LayerDialog.UpdateLists()  #rebuild the list and display
    dlg.Destroy()
    return

  def TileBackground(self, dc):
    sz = self.GetClientSize()
    w = self.bg_bmp.GetWidth()
    h = self.bg_bmp.GetHeight()
    x = 0
    while x < sz.width:
      y = 0
      while y < sz.height:
        dc.DrawBitmap(self.bg_bmp, x, y)
        y = y + h
      x = x + w
    return

  def DrawHexagon(self, dc, hex_type, xposition, yposition, radius):
    """hex_type is 'A' or 'B', xposition and yposition are the index from the map grid, radius is usually the gv.MapZoomFactor value"""
    center_point = wx.Point(0,0)
    cos30MZF = int(radius * 0.86602) #cos(30 deg)
    sin30MZF = int(radius * 0.5)  # sine(30 deg)
    HexCenterPoints = []

    if (hex_type == 'A'):  #draw a hex with point on top
      if (yposition % 2):
        Hoffset = (cos30MZF * (2*xposition))
      else:
        Hoffset = (cos30MZF * (2*xposition))+ cos30MZF

      if (xposition % 2):
        Voffset = (yposition*radius) + ((yposition*sin30MZF) + radius)
      else:
        Voffset = (yposition*radius) + ((yposition*sin30MZF) + 2*sin30MZF)

      center_point.x += Hoffset
      center_point.y += Voffset

      if ((center_point.x - cos30MZF) < 0):
        return
      if ((center_point.y - radius) < 0):
        return
      point0 = wx.Point(center_point.x, center_point.y-radius)
      point1 = wx.Point(center_point.x+cos30MZF, center_point.y-sin30MZF)
      point2 = wx.Point(center_point.x+cos30MZF, center_point.y+sin30MZF)
      point3 = wx.Point(center_point.x, center_point.y+radius)
      point4 = wx.Point(center_point.x-cos30MZF, center_point.y+sin30MZF)
      point5 = wx.Point(center_point.x-cos30MZF, center_point.y-sin30MZF)

    elif (hex_type == 'B'): #draw a hex with flat edge on top
      if (xposition % 2):  #odd column
        Hoffset = (xposition*radius) + ((xposition+2)*sin30MZF)
        Voffset = (2*(yposition)*cos30MZF)+(2*cos30MZF)
      else:
        Hoffset = ((xposition*radius) + radius)+(xposition*sin30MZF)
        Voffset = (2*yposition*cos30MZF) + cos30MZF

      center_point.x += Hoffset
      center_point.y += Voffset

      if ((center_point.x - gv.MapZoomFactor) < 0):
        return
      if ((center_point.y - cos30MZF) < 0):
        return
      point0 = wx.Point(center_point.x+sin30MZF, center_point.y-cos30MZF)
      point1 = wx.Point(center_point.x+radius, center_point.y)
      point2 = wx.Point(center_point.x+sin30MZF, center_point.y+cos30MZF)
      point3 = wx.Point(center_point.x-sin30MZF, center_point.y+cos30MZF)
      point4 = wx.Point(center_point.x-radius, center_point.y)
      point5 = wx.Point(center_point.x-sin30MZF, center_point.y-cos30MZF)

    dc.DrawLine(point0.x, point0.y, point1.x, point1.y)
    dc.DrawLine(point1.x, point1.y, point2.x, point2.y)
    dc.DrawLine(point2.x, point2.y, point3.x, point3.y)
    dc.DrawLine(point3.x, point3.y, point4.x, point4.y)
    dc.DrawLine(point4.x, point4.y, point5.x, point5.y)
    dc.DrawLine(point5.x, point5.y, point0.x, point0.y)
    DrawHexCenterDot = True
    if (DrawHexCenterDot):
      dc.DrawCircle(center_point.x, center_point.y, 2)
    HexCenterPoints.append(center_point)
    return

  def DrawMapGrid(self, dc, resolution):
    if ((dc) and (gv.DisplayGrid)):
      if (self.MapStruct.geomorph == True):  #working on a geomorph file
        ncolumns = 14
        nrows = 16
        dc.SetPen(wx.Pen(wx.BLUE))
        dc.SetBrush(wx.BLUE_BRUSH)
        for x in range(3,12,4): #draw the top and bottom row
          dc.DrawRectangle(x*resolution,0, 2*resolution, resolution)
          dc.DrawRectangle(x*resolution,15*resolution, 2*resolution, resolution)
        for y in range(3,14,4): #draw the left and right sides
          dc.DrawRectangle(0,y*resolution, resolution, 2*resolution)
          dc.DrawRectangle(13*resolution,y*resolution, resolution, 2*resolution)
        dc.SetPen(wx.GREEN_PEN)
        dc.SetBrush(wx.GREEN_BRUSH)
        for x in range(1,12,4): #draw the top and bottom row
          dc.DrawRectangle(x*resolution,0, 2*resolution, resolution)
          dc.DrawRectangle(x*resolution,15*resolution, 2*resolution, resolution)
        for y in range(1,14,4): #draw the left and right sides
          dc.DrawRectangle(0,y*resolution, resolution, 2*resolution)
          dc.DrawRectangle(13*resolution,y*resolution, resolution, 2*resolution)
      else:
        # Number of rows, columns available in the MapPanel
        ncolumns = self.MapStruct.columns
        nrows = self.MapStruct.rows

      if ((ncolumns == 0) or (nrows == 0)):
        logging.critical("DrawMapGrid: zero rows or columns")
        return

      line_pen = wx.Pen(gv.GridColor, gv.GridPenWidth, gv.GridPenStyle)
      intermediate_pen = wx.Pen(gv.IntermediateGridColor, gv.GridPenWidth, gv.GridPenStyle)
      dc.SetPen(line_pen)
      
      if (gv.DrawMapDiagonals): #draw map diagonals for an isometric map
        #draw diagonals from right to left to show as vertical lines on the isometric display
        dc.SetPen(line_pen)
        Xdimension = gv.MapZoomFactor * ncolumns
        Ydimension = gv.MapZoomFactor * nrows
        for x in range(1,ncolumns+1):
          Xoffset = x * gv.MapZoomFactor
          Yoffset = x * gv.MapZoomFactor
          dc.DrawLine(Xoffset, 0, 0, Yoffset)
          dc.DrawLine(Xdimension-Xoffset,Xdimension, Xdimension, Xdimension-Xoffset)
        for y in range(1, nrows+1):
          Xoffset = y * gv.MapZoomFactor
          Yoffset = y * gv.MapZoomFactor
          dc.DrawLine(Xoffset, 0, 0, Yoffset)
          dc.DrawLine(Ydimension-Xoffset,Ydimension, Ydimension, Ydimension-Xoffset)
      
      for x in range(ncolumns+1):
        xpos = (x * resolution)
        ypos_top = 0
        ypos_bottom = (self.MapStruct.rows * resolution)
        if (gv.ShowIntermediateGridLines) and (x % gv.IntermediateGridLinesInterval):
          dc.SetPen(intermediate_pen)
        else:
          dc.SetPen(line_pen)
        dc.DrawLine(xpos, ypos_top, xpos, ypos_bottom)
      for y in range(nrows+1):
        ypos = (y * resolution)
        xpos_left = 0
        xpos_right = (self.MapStruct.columns * resolution)
        if (gv.ShowIntermediateGridLines) and (y % gv.IntermediateGridLinesInterval):
          dc.SetPen(intermediate_pen)
        else:
          dc.SetPen(line_pen)
        dc.DrawLine(xpos_left, ypos, xpos_right, ypos)
    else:
      return

  def DrawBackgroundImage(self, dc, resolution):
    drawingX = True
    drawingY = True
    offsetX = 0
    offsetY = 0
    pageindex = self.nbMapNotebook.GetSelection()
    page = gv.MapPageList[pageindex]
    if (page.background == None) or (not page.background.IsOk()):
      return
    image = page.background.AdjustChannels(1.0,1.0,1.0,gv.BackgroundOpacity)
    bitmap = wx.BitmapFromImage(image)
    mapsize = wx.Size((self.MapStruct.columns*resolution), 
                      (self.MapStruct.rows*resolution))
    imagesize = wx.Size(bitmap.GetWidth(), bitmap.GetHeight())
    if (page.bg_displaymode == 'Tile'):
      while (drawingX == True):
        while (drawingY == True):
          dc.DrawBitmap(bitmap, offsetX, offsetY, True)
          if (offsetY > mapsize.height):
            offsetY = 0
            drawingY = False
          offsetY += imagesize.height
        if (offsetX > mapsize.width):
          drawingX = False
        offsetY = 0
        offsetX += imagesize.width
        drawingY = True
    elif (page.bg_displaymode == 'Center'): #Center the background on the map
      offsetX = (mapsize.width/2) - imagesize.width
      if (offsetX < 0):
        offsetX = 0
      offsetY = (mapsize.height/2) - imagesize.height
      if (offsetY < 0):
        offsetY = 0
      dc.DrawBitmap(bitmap, offsetX, offsetY, True)
    elif (page.bg_displaymode == 'Register'):
      offsetX = 0
      offsetY = 0
      newXsize = gv.MapZoomFactor * page.bg_x_dimension
      newYsize = gv.MapZoomFactor * page.bg_y_dimension
      image = page.background.Scale(newXsize, newYsize, wx.IMAGE_QUALITY_HIGH)
      bitmap = wx.BitmapFromImage(image)
      dc.DrawBitmap(bitmap, offsetX, offsetY, True)
    return

  def DrawDrawingObjects(self, gc, resolution):
    """This routine utilizes the wxGraphicsContext method in gc, not a wxDC"""
    if (not gv.ShowDrawingObjects):
      return
    if (gc == None):
      gc = wx.GraphicsContext()
      path = wx.GraphicsPath()
    pageindex = self.nbMapNotebook.GetSelection()
    page_name = gv.MapPageList[pageindex].PageName
    #item = gv.DrawingObject_Record()
    for item in self.DrawingList:
      if (item.page_name != page_name):
        continue
      if (item.object_type == 'fog'):  #fog-of-war objects are stored in this list, but are drawn in a separate function (DrawFogOfWarObjects)
        continue
      if (item.tool == 'Line') or (item.tool == 'Multiline') or (item.tool == 'Freehand'):
        ScaledPoints = []
        for point in item.line:
          scale_point = self.DecodeDrawingPoint(point, resolution)
          ScaledPoints.append(scale_point)
        if (item.selected):
          gv.DrawingSelectPen.SetWidth(item.pen.GetWidth()+2)
          gc.SetPen(gv.DrawingSelectPen)
          gc.SetBrush(item.brush)
          gc.StrokeLines(ScaledPoints)
        path = gc.CreatePath()
        gc.SetPen(item.pen)
        gc.SetBrush(item.brush)
        path.MoveToPoint(ScaledPoints[0])
        ScaledPoints.pop(0)
        for point in ScaledPoints:
          path.AddLineToPoint(point)
        gc.StrokePath(path)
        if (gv.DrawHandles):
          self.DrawHandles(item, resolution, gc)
      elif (item.tool == 'OutlineCircle') or (item.tool == 'FillCircle') or (item.tool == 'Point'):
        scale_point = self.DecodeDrawingPoint(item.circle[0], resolution)
        scale_radius = item.circle[1]*resolution
        if (item.selected):
          gv.DrawingSelectPen.SetWidth(item.pen.GetWidth()+2)
          gc.SetPen(gv.DrawingSelectPen)
          gc.SetBrush(item.brush)
          path = gc.CreatePath()
          path.AddCircle(scale_point.x,scale_point.y, scale_radius)
          gc.DrawPath(path)
        path = gc.CreatePath()
        gc.SetPen(item.pen)
        gc.SetBrush(item.brush)
        path.AddCircle(scale_point.x,scale_point.y, scale_radius)
        if (item.tool == 'FillCircle'):
          gc.DrawPath(path)
        else:
          gc.StrokePath(path)
        if (gv.DrawHandles):
          self.DrawHandles(item, resolution, gc)
      elif (item.tool == 'OutlineRect') or (item.tool == 'FillRect'):
        draw_rect = self.DecodeDrawingRect(item.rect, resolution)
        if (item.selected):
          gv.DrawingSelectPen.SetWidth(item.pen.GetWidth()+2)
          gc.SetPen(gv.DrawingSelectPen)
          gc.SetBrush(item.brush)
          path = gc.CreatePath()
          path.AddRectangle(draw_rect.x, draw_rect.y, draw_rect.width, draw_rect.height)
          gc.DrawPath(path)
        path = gc.CreatePath()
        gc.SetPen(item.pen)
        gc.SetBrush(item.brush)
        path.AddRectangle(draw_rect.x, draw_rect.y, draw_rect.width, draw_rect.height)
        if (item.tool == 'FillRect'):
          gc.DrawPath(path)
        else: 
          gc.StrokePath(path)
        if (gv.DrawHandles):
          self.DrawHandles(item, resolution, gc)
      elif (item.tool == 'Image'):
        draw_rect = self.DecodeDrawingRect(item.rect, resolution)
        if (item.selected):
          gv.DrawingSelectPen.SetWidth(item.pen.GetWidth()+2)
          gc.SetPen(gv.DrawingSelectPen)
          gc.SetBrush(item.brush)
          path = gc.CreatePath()
          path.AddRectangle(draw_rect.x, draw_rect.y, draw_rect.width, draw_rect.height)
          gc.DrawPath(path)
        gc.DrawBitmap(wx.BitmapFromImage(item.image), draw_rect.x, draw_rect.y, draw_rect.width, draw_rect.height)
        if (gv.DrawHandles):
          self.DrawHandles(item, resolution, gc)
    return

  def DrawHandles(self, item, resolution, gc):
    """create list of wxRect2D for handle detection"""
    #item = gv.DrawingObject_Record()
    #gc = wx.GraphicsContext()
    HandleSize = 3  #this is half the size
    path = gc.CreatePath()
    gc.SetPen(wx.BLACK_PEN)
    gc.SetBrush(wx.WHITE_BRUSH)
    item.handles = []
    if (item.tool == 'Line') or (item.tool == 'Multiline') or (item.tool == 'Freehand'):
      for list_point in item.line:
        point = self.DecodeDrawingPoint(list_point, resolution)
        gc.DrawRectangle(point.x-HandleSize, point.y-HandleSize, (HandleSize*2), (HandleSize*2))
        rect = wx.Rect2D(point.x-HandleSize, point.y-HandleSize, (HandleSize*2), (HandleSize*2))
        item.handles.append(rect)
    elif (item.tool == 'Image') or (item.tool == 'FillRect') or (item.tool == 'OutlineRect'):
      draw_rect = self.DecodeDrawingRect(item.rect, resolution)
      width = draw_rect.width
      height = draw_rect.height
      gc.DrawRectangle(draw_rect.x-HandleSize, draw_rect.y-HandleSize, (HandleSize*2), (HandleSize*2))
      rect = wx.Rect2D(draw_rect.x-HandleSize, draw_rect.y-HandleSize, (HandleSize*2), (HandleSize*2))
      item.handles.append(rect)

      gc.DrawRectangle((width+draw_rect.x-HandleSize), draw_rect.y-HandleSize, (HandleSize*2), (HandleSize*2))
      rect = wx.Rect2D((width+draw_rect.x-HandleSize), draw_rect.y-HandleSize, (HandleSize*2), (HandleSize*2))
      item.handles.append(rect)

      gc.DrawRectangle(draw_rect.x-HandleSize+width, draw_rect.y-HandleSize+height, (HandleSize*2), (HandleSize*2))
      rect = wx.Rect2D(draw_rect.x-HandleSize+width, draw_rect.y-HandleSize+height, (HandleSize*2), (HandleSize*2))
      item.handles.append(rect)

      gc.DrawRectangle(draw_rect.x-HandleSize, draw_rect.y-HandleSize+height, (HandleSize*2), (HandleSize*2))
      rect = wx.Rect2D(draw_rect.x-HandleSize, draw_rect.y-HandleSize+height, (HandleSize*2), (HandleSize*2))
      item.handles.append(rect)
      #index 4 is the center handle for moving.
      gc.DrawRectangle(draw_rect.x+(width/2)-HandleSize, draw_rect.y+(height/2)-HandleSize, (HandleSize*2), (HandleSize*2))
      rect = wx.Rect2D(draw_rect.x+(width/2)-HandleSize, draw_rect.y+(height/2)-HandleSize, (HandleSize*2), (HandleSize*2))
      item.handles.append(rect)
    elif (item.tool == 'FillCircle') or (item.tool == 'OutlineCircle') or (item.tool == 'Point'):
      point = self.DecodeDrawingPoint(item.circle[0], resolution)
      radius = item.circle[1]*resolution
      #index 0 is the centerpoint
      gc.DrawRectangle(point.x-HandleSize, point.y-HandleSize, (HandleSize*2), (HandleSize*2))
      rect = wx.Rect2D(point.x-HandleSize, point.y-HandleSize, (HandleSize*2), (HandleSize*2))
      item.handles.append(rect)
      if (item.tool == 'Point'):  #don't draw the sides if just a point
        return
      #index 1 is right
      gc.DrawRectangle(point.x+radius-HandleSize, point.y-HandleSize, (HandleSize*2), (HandleSize*2))
      rect = wx.Rect2D(point.x+radius-HandleSize, point.y-HandleSize, (HandleSize*2), (HandleSize*2))
      item.handles.append(rect)
      #index 2 is left
      gc.DrawRectangle(point.x-radius-HandleSize, point.y-HandleSize, (HandleSize*2), (HandleSize*2))
      rect = wx.Rect2D(point.x-radius-HandleSize, point.y-HandleSize, (HandleSize*2), (HandleSize*2))
      item.handles.append(rect)
      #index 3 is top
      gc.DrawRectangle(point.x-HandleSize, point.y-radius-HandleSize, (HandleSize*2), (HandleSize*2))
      rect = wx.Rect2D(point.x-HandleSize, point.y-radius-HandleSize, (HandleSize*2), (HandleSize*2))
      item.handles.append(rect)
      #index 4 is bottom
      gc.DrawRectangle(point.x-HandleSize, point.y+radius-HandleSize, (HandleSize*2), (HandleSize*2))
      rect = wx.Rect2D(point.x-HandleSize, point.y+radius-HandleSize, (HandleSize*2), (HandleSize*2))
      item.handles.append(rect)
    return

  def DrawMapIcons(self, dc, resolution):
    if (not gv.ShowIcons):
      return
    
    pageindex = self.nbMapNotebook.GetSelection()
    for room in gv.RoomList:
      if (room.page != self.nbMapNotebook.GetPageText(pageindex)):
        continue

      show_icon = False
      for layer in gv.LayerList:
        if (room.Layer == layer.index):
          show_icon = True
      if (room.placed and show_icon):
        if (room.IconType == 'Marker'):
          if (gv.HighlightIcons):
            highlightPen = wx.Pen(gv.HighlightIconColor, 1, wx.SOLID)
            highlightBrush = wx.Brush(gv.HighlightIconColor)
            dc.SetBrush(highlightBrush)
            dc.SetPen(highlightPen)
            dc.DrawRectangle(int(room.x*resolution)-gv.tileborderwidth,int(room.y*resolution)-gv.tileborderwidth,int(room.MapRect.width)+2*gv.tileborderwidth,int(room.MapRect.height)+2*gv.tileborderwidth)
          scaleImage = room.Icon.Scale(room.MapRect.width, room.MapRect.height)
          bitmap = wx.BitmapFromImage(scaleImage)
          dc.DrawBitmap(bitmap, int(room.x*resolution),int(room.y*resolution), True)
        else:
          scale = int(resolution * gv.IconScaleFactor) * room.IconSize
          if (isinstance(room.monster, srd.Monster5E_Record) and (room.monster) and (room.monster.image)):  #a custom image was loaded
            scaleImage = room.monster.image.Scale(scale, scale)
          else:
            scaleImage = room.Icon.Scale(scale, scale)
          offset = wx.Point(((room.IconSize*resolution) - scale)/2, ((room.IconSize*resolution) - scale)/2)
          resizeImage = scaleImage.Resize((room.IconSize*resolution,room.IconSize*resolution), offset)
          bitmap = wx.BitmapFromImage(resizeImage)
          
          if (room.monster):  #base MapRect on the size of the monster
            room.MapRect.width = max(room.monster.size-1, 1)*resolution  #size is based on index, not squares; see srd.py module
            room.MapRect.height = max(room.monster.size-1, 1)*resolution
          else:
            room.MapRect.width = resolution
            room.MapRect.height = resolution
          if (gv.HighlightIcons):
            if (room.monster):
              #change color of highlight based on the monster remaining HP
              if (room.monster.startHP == 0):
                room.monster.startHP = room.monster.HP
              remainingHP = room.monster.HP / room.monster.startHP
              if (remainingHP <= 0):
                #change background to black if 0 or less HP
                highlightPen = wx.BLACK_PEN
                highlightBrush = wx.BLACK_BRUSH
              elif (remainingHP <= 0.3):
                highlightBrush = wx.RED_BRUSH
                highlightPen = wx.RED_PEN
              elif (remainingHP <= 0.5):
                #highlight in orange
                highlightBrush = wx.Brush(wx.Colour(255,106,0), wx.SOLID)
                highlightPen = wx.Pen(wx.Colour(255,106,0), 1, wx.SOLID)
              elif (remainingHP <= 0.7):
                #highlight in yellow
                highlightBrush = wx.Brush(wx.Colour(255,255,0), wx.SOLID)
                highlightPen = wx.Pen(wx.Colour(255,255,0), 1, wx.SOLID)
              else: #(remainingHP > 0.7):
                #highlight in green
                highlightBrush = wx.Brush(wx.Colour(0,255,0), wx.SOLID)
                highlightPen = wx.Pen(wx.Colour(0,255,0), 1, wx.SOLID)
            else:
              highlightPen = wx.Pen(room.highlightColor, 1, wx.SOLID)
              highlightBrush = wx.Brush(room.highlightColor)
            dc.SetBrush(highlightBrush)
            dc.SetPen(highlightPen)
            dc.DrawCircle((int((room.x*resolution)+room.MapRect.width/2.0)),(int((room.y*resolution)+room.MapRect.height/2.0)),(room.IconSize*resolution)/2)
          if (room.selected):
            selection_pen = wx.Pen(gv.SelectionColor, gv.SelectionPenWidth,gv.SelectionPenStyle)
            dc.SetPen(selection_pen)
            dc.DrawRectangle((room.x*resolution)-gv.tileborderwidth,(room.y*resolution)-gv.tileborderwidth,int(room.MapRect.width)+2*gv.tileborderwidth,int(room.MapRect.height)+2*gv.tileborderwidth)
          if (gv.ShowIconNamesOnMap):
            memdc = wx.MemoryDC()
            if (not memdc.IsOk()):
              return
            memdc.SetMapMode(wx.MM_TEXT)
            font = wx.NORMAL_FONT
            font.SetPointSize(10)
            memdc.SetFont(font)
            textLabel = ''
            if (room.monster):
              if (room.monster.customName):
                textLabel = room.monster.customName
              else:
                textLabel = room.monster.name

              if (room.monster.size == 3):   # offset for Large monster
                labelOffset = resolution * 2
              elif (room.monster.size == 4): # offset for Huge monster
                labelOffset = resolution * 3
              elif (room.monster.size == 5): # offset for Gargantuan monster
                labelOffset = resolution * 4
              else:                          # offset for all other sizes
                labelOffset = resolution
            else:
              textLabel = room.Description
              labelOffset = resolution
              
            (width, textheight) = memdc.GetTextExtent(textLabel)
            width += 5  #add a border to the hover image
            textheight += 3  #add a border to the hover image
            
            nameBitmap = wx.Bitmap(width, textheight)
            memdc.SelectObject(nameBitmap)
            memdc.Clear()
            memdc.DrawText(textLabel, 2, 0)
            memdc.SelectObject(wx.NullBitmap)
            
            dc.DrawBitmap(nameBitmap, (int(room.x*resolution)+labelOffset),int(room.y*resolution), True)
            
            if (room.monster):
              #add pixels to the height for each condition color; then draw the appropriate color bar below the text label
              height = 0
              if (room.monster.con1 != 'None') or (room.monster.con2 != 'None') or (room.monster.con3 != 'None') or (room.monster.con4 != 'None'):
                height += gv.ConditionBarThickness
                
              width = 0
              if (room.monster.con1 != 'None'):
                width += gv.ConditionBarThickness
              if (room.monster.con2 != 'None'):
                width += gv.ConditionBarThickness
              if (room.monster.con3 != 'None'):
                width += gv.ConditionBarThickness
              if (room.monster.con4 != 'None'):
                width += gv.ConditionBarThickness
                
              if (height > 0) and (width > 0):
                conditionBitmap = wx.Bitmap(width, height)
                memdc.SelectObject(conditionBitmap)
                offset = 0
                if (room.monster.con1 != 'None'):
                  color = gv.ConditionColors.GetConditionColor(room.monster.con1)
                  pen = wx.Pen(color, 1)
                  brush = wx.Brush(color)
                  memdc.SetPen(pen)
                  memdc.SetBrush(brush)
                  memdc.DrawRectangle(offset,0, gv.ConditionBarThickness, gv.ConditionBarThickness)
                  offset += gv.ConditionBarThickness
                if (room.monster.con2 != 'None'):
                  color = gv.ConditionColors.GetConditionColor(room.monster.con2)
                  pen = wx.Pen(color, 1)
                  brush = wx.Brush(color)
                  memdc.SetPen(pen)
                  memdc.SetBrush(brush)
                  memdc.DrawRectangle(offset,0, gv.ConditionBarThickness, gv.ConditionBarThickness)
                  offset += gv.ConditionBarThickness
                if (room.monster.con3 != 'None'):
                  color = gv.ConditionColors.GetConditionColor(room.monster.con3)
                  pen = wx.Pen(color, 1)
                  brush = wx.Brush(color)
                  memdc.SetPen(pen)
                  memdc.SetBrush(brush)
                  memdc.DrawRectangle(offset,0, gv.ConditionBarThickness, gv.ConditionBarThickness)
                  offset += gv.ConditionBarThickness
                if (room.monster.con4 != 'None'):
                  color = gv.ConditionColors.GetConditionColor(room.monster.con4)
                  pen = wx.Pen(color, 1)
                  brush = wx.Brush(color)
                  memdc.SetPen(pen)
                  memdc.SetBrush(brush)
                  memdc.DrawRectangle(offset,0, gv.ConditionBarThickness, gv.ConditionBarThickness)
                  offset += gv.ConditionBarThickness
                memdc.SelectObject(wx.NullBitmap)
                dc.DrawBitmap(conditionBitmap, (int(room.x*resolution)+labelOffset),(textheight+int(room.y*resolution)), True)
          dc.DrawBitmap(bitmap, int(room.x*resolution),int(room.y*resolution), True)
    return

  def DrawFogOfWarObjects(self, dc, gc1, resolution):
    if (not gv.ShowFogObjects) or (self.DrawingList == []):
      return
    
    fog_size = self.MapBuffer.GetSize()
    
    #set up the fog overlay
    overlayBitmap = wx.Bitmap(fog_size.x, fog_size.y)
    
    overlayDC = wx.MemoryDC(overlayBitmap)
    fogPen = wx.Pen(gv.MapFogColor)
    fogBrush = wx.Brush(gv.MapFogColor)
    overlayDC.SetPen(fogPen)
    overlayDC.SetBrush(fogBrush)
    overlayDC.DrawRectangle(0,0,fog_size.x, fog_size.y)
    overlayDC.SelectObject(wx.NullBitmap)
    
    
    fogBitmap = wx.Bitmap(fog_size.x, fog_size.y)
    fogDC = wx.MemoryDC(fogBitmap)
    fogDC.SetPen(wx.BLACK_PEN)
    fogDC.SetBrush(wx.BLACK_BRUSH)

    """This routine utilizes the wxGraphicsContext method in gc, not a wxDC."""
    gc = wx.GraphicsContext.Create(dc)

    pageindex = self.nbMapNotebook.GetSelection()
    page_name = gv.MapPageList[pageindex].PageName
    path = gc.CreatePath()

    #item = gv.DrawingObject_Record()
    
    for item in self.DrawingList:
      if (item.page_name != page_name):
        continue
      if (item.object_type == 'draw'):  #drawing objects are stored in this list, but are drawn in a separate function (DrawDrawingObjects)
        continue
      fogDC.SetPen(item.pen)
      fogDC.SetBrush(item.brush)
      if (item.tool == 'Line') or (item.tool == 'Multiline') or (item.tool == 'Freehand'):
        ScaledPoints = []
        for point in item.line:
          scale_point = self.DecodeDrawingPoint(point, resolution, 'INT')
          ScaledPoints.append(scale_point)
        if (item.selected):
          fogDC.SetPen(gv.DrawingSelectPen)
          gv.DrawingSelectPen.SetWidth(item.pen.GetWidth()+2)
          gc.StrokeLines(ScaledPoints)
          fogDC.SetPen(wx.BLACK_PEN)
        fogDC.DrawLines(ScaledPoints)

      elif (item.tool == 'FillCircle'):
        scale_point = self.DecodeDrawingPoint(item.circle[0], resolution, 'INT')
        scale_radius = item.circle[1]*resolution
        if (item.selected):
          gv.DrawingSelectPen.SetWidth(item.pen.GetWidth()+2)
          fogDC.SetPen(gv.DrawingSelectPen)
          fogDC.DrawCircle(scale_point.x, scale_point.y, scale_radius)
          fogDC.SetPen(wx.BLACK_PEN)
        fogDC.DrawCircle(scale_point.x, scale_point.y, scale_radius)

      elif (item.tool == 'FillRect'):
        draw_rect = self.DecodeDrawingRect(item.rect, resolution, 'INT')
        if (item.selected):
          gv.DrawingSelectPen.SetWidth(item.pen.GetWidth()+2)
          fogDC.SetPen(gv.DrawingSelectPen)
          fogDC.DrawRectangle(draw_rect.x, draw_rect.y, draw_rect.width, draw_rect.height)
        fogDC.DrawRectangle(draw_rect.x, draw_rect.y, draw_rect.width, draw_rect.height)
      elif (item.tool == 'Point'):  #Generic light source
        scale_point = self.DecodeDrawingPoint(item.circle[0], resolution, 'INT')
        scale_radius = int(item.circle[1]*resolution)
        fogDC.SetBrush(wx.WHITE_BRUSH)
        fogDC.DrawCircle(scale_point.x, scale_point.y, scale_radius)
        pass  #skip and draw the lights separately
    
    fogDC.SelectObject(wx.NullBitmap)  #free the fogBitmap
    
    fogMask = wx.Mask(fogBitmap)
    overlayBitmap.SetMask(fogMask)
    self.MapFogImage = wx.ImageFromBitmap(overlayBitmap)
    MapFogImage = self.MapFogImage.AdjustChannels(1.0,1.0,1.0,gv.MainFogDensity)
    
    MapFogBitmap = wx.BitmapFromImage(MapFogImage)
    self.MapPanelDC.DrawBitmap(MapFogBitmap,0,0,True)

    return

  def DrawMapWindow(self, printing=False,drawOnly=False):
    """
    drawOnly flag is set when it is desired to only redraw part of the map window
    drawOnly may be ICONS, TILES, ANNOTATION, COORD, DRAW_OBJ, FOG
    """
    if (printing == True):
      #redirecting output to the printing DC
      resolution = gv.PrintResolution
      MapWidth = self.MapStruct.columns*gv.PrintResolution
      MapHeight = self.MapStruct.rows*gv.PrintResolution
      self.PrintBuffer = wx.Bitmap(MapWidth, MapHeight)
      dc = wx.MemoryDC(self.PrintBuffer)
      self.MapPanelGC = wx.GraphicsContext.Create(dc)
    else:
      MapWidth = self.MapStruct.columns*gv.MapZoomFactor
      MapHeight = self.MapStruct.rows*gv.MapZoomFactor
      PanelSize = self.MapPanel.GetSize()
      width = max(MapWidth, PanelSize.width)
      height = max(MapHeight, PanelSize.height)
      self.VirtualMapPanel = wx.Size(width, height)
      self.MapPanel.SetVirtualSize(self.VirtualMapPanel)

      self.MapBuffer = wx.Bitmap(self.VirtualMapPanel.width, self.VirtualMapPanel.height)
      self.MapPanelDC = wx.BufferedDC(None, self.MapBuffer)
      self.MapPanel.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
      self.MapPanel.SetScrollRate(gv.ScrollIncrement, gv.ScrollIncrement)
      dc = self.MapPanelDC
      self.MapPanelGC = wx.GraphicsContext.Create(self.MapPanelDC)
      resolution = gv.MapZoomFactor

    Brush = wx.Brush(gv.MapPanelBackgroundColor)
    Pen = wx.Pen(gv.MapPanelBackgroundColor)
    dc.SetBrush(Brush)
    dc.SetPen(Pen)
    dc.DrawRectangle(0,0, MapWidth, MapHeight)

    if (gv.DisplayBackground == True):
      self.DrawBackgroundImage(dc,resolution)

    if (not gv.DrawGridOnTop):
      self.DrawMapGrid(dc, resolution)

    index = self.nbMapNotebook.GetSelection()
    pagename = self.nbMapNotebook.GetPageText(index)
    #check for filter by notebook page, layer display, and by tileset
    for tile in self.maplist:
      if (tile.page != pagename):  #filter by pagename
        tile.ShowOnMapPanel = False
        continue
      
      for layer in gv.LayerList:  #filter by layer
        if (layer.index == tile.layer):
          tile.ShowOnMapPanel = layer.display
          break #break out of layer list
        
      for tset in gv.tilesets:  #filter by tilesets
        if (tset.SetID == tile.tilesetID):
          if (tset.DisplayMapWindow == True):
            tile.ShowOnMapPanel = True
          else:
            tile.ShowOnMapPanel = False
          break

    if (self.maplist != []):
      for tile in self.maplist:
        if ((tile.mapdisplay) and (tile.ShowOnMapPanel)):
          #9.1b:  Do not recalculate the mapdisplay on every call to DrawMapWindow
          #       Except when printing, since there is a new temporary resolution to deal with
          if (printing):
            tile.GenerateMapDisplay(resolution)
          
          xpos = (tile.MapPosition.x*resolution)
          ypos = (tile.MapPosition.y*resolution)
          dc.DrawBitmap(tile.mapdisplay, xpos, ypos, True) #draw the map tile
          if (tile.highlight):
            Xsize = resolution*tile.actualXsize #calculate the pixel size of the tile
            Ysize = resolution*tile.actualYsize
            #highlighted tiles
            HLpen = wx.Pen(gv.HighlightColor, gv.HighlightPenWidth, gv.HighlightPenStyle)
            dc.SetPen(HLpen)
            dc.SetBrush(wx.TRANSPARENT_BRUSH)
            dc.DrawRectangle(xpos, ypos, Xsize, Ysize)
          
          if (gv.OutlineTiles):
            #outline tiles for printing
            HLpen = wx.Pen(gv.OutlineTilesColor, gv.HighlightPenWidth, gv.HighlightPenStyle)
            dc.SetPen(HLpen)
            x1 = xpos
            y1 = ypos
            x2 = xpos + tile.mapdisplay.GetWidth()-gv.HighlightPenWidth
            y2 = ypos + tile.mapdisplay.GetHeight()-gv.HighlightPenWidth
            dc.DrawLine(x1, y1, x2, y1)
            dc.DrawLine(x2, y1, x2, y2)
            dc.DrawLine(x2, y2, x1, y2)
            dc.DrawLine(x1, y2, x1, y1)
    if (drawOnly):
      if (drawOnly == 'TILES'):
        self.DrawSelectedMapTiles(dc, resolution)
      elif (drawOnly == 'ANNOTATIONS'):
        self.DrawMapAnnotations(dc, resolution)
      elif (drawOnly == 'COORD'):
        self.DrawMapCoordinates(dc, resolution)
      elif (drawOnly == 'ICONS'):
        self.DrawMapIcons(dc, resolution)
      elif (drawOnly == 'DRAW_OBJ'):
        self.DrawDrawingObjects(self.MapPanelGC, resolution)
      elif (drawOnly == 'FOG'):
        self.DrawFogOfWarObjects(dc, self.MapPanelGC, resolution)
    else:
      self.DrawSelectedMapTiles(dc, resolution)
      self.DrawMapAnnotations(dc, resolution)
      self.DrawMapCoordinates(dc, resolution)
      self.DrawMapIcons(dc, resolution)
      self.DrawDrawingObjects(self.MapPanelGC, resolution)
      self.DrawFogOfWarObjects(dc, self.MapPanelGC, resolution)

    if (gv.DrawGridOnTop):
      self.DrawMapGrid(dc, resolution)
    
    self.MapPanel.Refresh()
    if (printing):
      #restore the tile.MapDisplay images to the correct zoom factor
      for tile in self.maplist:
        tile.GenerateMapDisplay(gv.MapZoomFactor)
    return
  # END of DrawMapWindow

  def DrawMapCoordinates(self, dc, resolution):
    if (gv.ShowGridCoordinates):
      #Draw letters across the top, numbers down the side.
      Hoffset = resolution/8
      Voffset = resolution/8
      x1 = 65
      x2 = 64
      for x in range(self.MapStruct.columns):
        coord = Annotation()
        coord.fg = gv.TextForegroundColor
        coord.bg = gv.TextBackgroundColor
        coord.font = gv.TextFont
        coord.opaque = gv.OpaqueBackground
        coord.zoomfactor = gv.MapZoomFactor

        if (x > 25):  #need to do 2 letters for the column code
          if (x1 > 90):
            x1 = 65
            x2 += 1
          coord.text = chr(x2) + chr(x1)
        else:
          coord.text = chr(x1)
        x1 += 1

        txt = self.CreateTextLabelBitmap(coord, resolution)
        dc.DrawBitmap(txt.bmp, int(x*resolution+Hoffset), int(Voffset), True)

      Voffset = resolution/2
      for x in range(self.MapStruct.rows):
        coord = Annotation()
        coord.fg = gv.TextForegroundColor
        coord.bg = gv.TextBackgroundColor
        coord.font = gv.TextFont
        coord.opaque = gv.OpaqueBackground
        coord.zoomfactor = gv.MapZoomFactor
        coord.text = str(x)
        txt = self.CreateTextLabelBitmap(coord, resolution)
        dc.DrawBitmap(txt.bmp, int(Hoffset), int(x*resolution+Voffset), True)
    return


  def DrawSelectedMapTiles(self, dc, resolution):
    if (self.selectlist == []):
      return
    else:
      selection_pen = wx.Pen(gv.SelectionColor, gv.SelectionPenWidth, gv.SelectionPenStyle)
      dash_selection_pen = wx.Pen(gv.SelectionColor, gv.SelectionPenWidth, wx.SHORT_DASH)
      dc.SetPen(dash_selection_pen)
      dc.SetBrush(wx.TRANSPARENT_BRUSH)
      for tile in self.selectlist:
        if (tile.mapdisplay):
          #9.1b:  Do not recalculate mapdisplay for each tile
          (Xsize, Ysize) = tile.mapdisplay.GetSize()
          xpos = (tile.MapPosition.x*resolution)
          ypos = (tile.MapPosition.y*resolution)
          dc.DrawRectangle(xpos-gv.tileborderwidth, ypos-gv.tileborderwidth,
                           Xsize+2*gv.tileborderwidth, Ysize+2*gv.tileborderwidth)
          dc.DrawBitmap(tile.mapdisplay, xpos, ypos, True)
   
      tile = self.selectlist[0] #always draw this one last so it is on top of a selection stack
      if (tile.mapdisplay):
        (Xsize, Ysize) = tile.mapdisplay.GetSize()
        xpos = (tile.MapPosition.x*resolution)
        ypos = (tile.MapPosition.y*resolution)
        dc.SetPen(selection_pen)
        dc.SetBrush(wx.TRANSPARENT_BRUSH)
        dc.DrawRectangle(xpos-gv.tileborderwidth, ypos-gv.tileborderwidth,
                         Xsize+2*gv.tileborderwidth, Ysize+2*gv.tileborderwidth)
        dc.DrawBitmap(tile.mapdisplay, xpos, ypos, True)
    return
  # END DrawSelectedMapTiles

  def DrawMapAnnotations(self, dc, resolution):
    if (self.textlist != []):
      pageindex = self.nbMapNotebook.GetSelection()
      for txt in self.textlist:
        if (txt.page != self.nbMapNotebook.GetPageText(pageindex)):
          continue
        txt = self.CreateTextLabelBitmap(txt, resolution)
        if (not txt.bmp.IsOk()):
          logging.error("Invalid bitmap.  Annotation index %d",txt.index)
          continue
        if (txt.selected):
          selection_pen = wx.Pen(gv.SelectionColor, gv.SelectionPenWidth, gv.SelectionPenStyle)
          dc.SetPen(selection_pen)
          dc.DrawRectangle((txt.x*resolution)-gv.tileborderwidth,
                           (txt.y*resolution)-gv.tileborderwidth,
                           txt.extent.width+2*gv.tileborderwidth,
                           txt.extent.height+2*gv.tileborderwidth)
        dc.DrawBitmap(txt.bmp, int(txt.x*resolution), int(txt.y*resolution), True)
    return

  def XtoIJ(self, index, columns):
    if ((columns < 0) or (index < 0)):
      return None
    ij = IJstruct()
    ij.i = index / columns
    ij.j = index % columns
    return ij

  def IJtoX(self, i, j, columns):
    x = (j*columns) + i
    return x

  def SortTilePanelBySize(self, maxrows, maxcols):
    """This is the quick way to sort tiles.  SortTilePanelGrid is the space efficient way."""
    process_tilelist = True #keep checking self.tilelist.  False indicates we are done
    row = 1
    col = 1
    sort_count = 0 #how many tiles have been sorted?
    list_length = 0
    for tile in self.tilelist:
      if (tile.ShowOnTilePanel == True):
        list_length += 1
        tile.sort = False  #reset the sorting flag only for those tiles to be displayed
    
    if (list_length == 0):
      #nothing to sort
      return wx.Size(0,0)
    
    skip_count = True
    size = 1 #tiles of this height are currently being placed
    while (sort_count < list_length):
      for tile in self.tilelist:
        if ((tile.sort == False) and (tile.ShowOnTilePanel == True)):
          if (tile.actualYsize == size):
            if ((tile.actualXsize+col+1) > maxcols):
              if (gv.DualDisplayTileWindow):
                row = row + (tile.actualYsize*2) + 1
              else:
                row = row + tile.actualYsize + 1
              col = 1
            tile.sort = True
            tile.TileGrid.x = col
            tile.TileGrid.y = row
            sort_count += 1
            skip_count = False
            col = tile.actualXsize + col + 1
      if (skip_count):
        row += 1
      else:
        if (gv.DualDisplayTileWindow):
          row = row + (size*2) +1
        else:
          row = row + size +1
      skip_count = True
      size += 1
      col = 1


    for tile in self.tilelist:
      tile.sort = False #reset all tiles so they are eligible for display

    return wx.Size(maxcols, row+12) #are there any tiles >12 spaces high?

  def UpdateTileQuantity(self, pagename):
    """Update the number of tiles used on the current map page"""
    
    if (gv.ResetTileStatistics):  # reset the number of tiles used for each map page
      for tile in self.tilelist:
        tile.num_used = 0
        tile.dimmed = False
        for maptile in self.maplist:
          if (pagename == maptile.page) and (tile.key_index == maptile.key_index):
            tile.num_used += 1
            if ((gv.LimitTiles == True) and (tile.num_used >= tile.copies)):
              tile.dimmed = True
            else:
              tile.dimmed = False
    else:  # count the number of tiles used across all pages, ie, the entire maplist
      for tile in self.tilelist:
        tile.num_used = 0
        tile.dimmed = False
        for maptile in self.maplist:
          if (tile.key_index == maptile.key_index):
            tile.num_used += 1
            if ((gv.LimitTiles == True) and (tile.num_used >= tile.copies)):
              tile.dimmed = True
            else:
              tile.dimmed = False
    self.DrawTileWindow()
    return

  def AddTileFromTilePanel(self):
    # An image was selected
    selected_tile = self.FindSelectedTileInLists()
    final_point = wx.Point2D(0,0)

    if (selected_tile and gv.SelectedFromTilePanel):
      selected_tile.GenerateMapDisplay(gv.MapZoomFactor)
      selected_tile.selected = False

      newtile = self.CopyTile(selected_tile)
      newtile.layer = gv.ActiveLayer
      index = self.nbMapNotebook.GetSelection()
      newtile.page = self.nbMapNotebook.GetPageText(index)
      self.maplist.append(newtile)
      gv.PromptSave = True
      for tset in gv.tilesets:
        if tset.SetID == newtile.tilesetID:
          tset.used = True
      newtile.index = self.MasterIndex
      self.MasterIndex += 1
      newtile.order = len(self.maplist)
      
      newtile.MapPosition = final_point
      (Xscale, Yscale) = newtile.mapdisplay.GetSize()
      newtile.MapRect = wx.Rect2D(final_point.x, final_point.y, Xscale, Yscale)

      self.UndoActionEvent(flag="ADD_TILE", tile=newtile)
      selected_tile.num_used += 1

      self.UpdateTileQuantity(newtile.page)
      self.DrawMapWindow()
    return

  def ChangeSelectionMode(self, event=None, programActivation=None):
    """Change the bitmaps and gv.SelectMode.  programActivation is where pymapper internally switches modes"""
    if (programActivation):
      if (gv.SelectMode == 'tile'): #cycle to icon mode
        self.frame.SplitterSash.Unsplit()
        gv.SelectMode = 'icon'
        gv.ShowIcons = True
        self.frame.toolbar.ToggleTool(PyMapperDialogs.tShowIcons, True)
        for x in self.selectlist:
          x.selected = False
        self.selectlist = []
        self.DrawMapWindow()
        self.DrawTileWindow()
        #change colors on buttons
        self.TileSelectButton.SetBackgroundColour(self.UnSelectBGColor)
        self.TileSelectButton.SetForegroundColour(self.UnSelectFGColor)
        self.IconSelectButton.SetBackgroundColour(self.SelectBGColor)
        self.IconSelectButton.SetForegroundColour(self.SelectFGColor)
        self.DrawSelectButton.SetBackgroundColour(self.UnSelectBGColor)
        self.DrawSelectButton.SetForegroundColour(self.UnSelectFGColor)
        self.FogSelectButton.SetBackgroundColour(self.UnSelectBGColor)
        self.FogSelectButton.SetForegroundColour(self.UnSelectFGColor)
        if (self.DrawTools):
          self.DrawTools.Show(False)
          self.DrawTools = None
        if (fog.FogToolsDialog):
          fog.FogToolsDialog.Show(False)
          fog.FogToolsDialog = None
        gv.DrawingObject = None
        gv.DrawingToolStartPoint = None
        gv.DrawingToolPrevious = None
      elif (gv.SelectMode == 'icon'):  #cycle to draw mode
        self.frame.SplitterSash.Unsplit()
        gv.ShowDrawingObjects = True
        self.frame.toolbar.ToggleTool(PyMapperDialogs.tShowDrawingObjects, True)
        for x in self.selectlist:
          x.selected = False
        self.selectlist = []
        for label in self.textlist:
          label.selected = False
        for item in gv.RoomList:
          item.selected = False
        self.DrawTileWindow()
        #change the buttons
        self.TileSelectButton.SetBackgroundColour(self.UnSelectBGColor)
        self.TileSelectButton.SetForegroundColour(self.UnSelectFGColor)
        self.IconSelectButton.SetBackgroundColour(self.UnSelectBGColor)
        self.IconSelectButton.SetForegroundColour(self.UnSelectFGColor)
        self.DrawSelectButton.SetBackgroundColour(self.SelectBGColor)
        self.DrawSelectButton.SetForegroundColour(self.SelectFGColor)
        self.FogSelectButton.SetBackgroundColour(self.UnSelectBGColor)
        self.FogSelectButton.SetForegroundColour(self.UnSelectFGColor)
        if (not self.DrawTools):
          self.DrawTools = DrawToolsDialog(self.frame)
          self.DrawTools.Show(True)
        if (fog.FogToolsDialog):
          fog.FogToolsDialog.Show(False)
          fog.FogToolsDialog = None
      elif (gv.SelectMode == 'draw'):  #cycle to fog mode now
        self.frame.SplitterSash.Unsplit()
        gv.SelectMode = 'fog'
        if (not fog.FogToolsDialog):
          fog.FogToolsDialog = fog.FogToolsDialogCore(self.frame)
          fog.FogToolsDialog.Show(True)
          app.OnViewSecondaryScreen()
      else:        #cycle back to tile mode
        self.frame.SplitterSash.SplitVertically(self.frame.pnMapBasePanel, self.frame.pnTileBasePanel, gv.SashPosition)
        gv.SelectMode = 'tile'
        for label in self.textlist:
          label.selected = False
        for item in gv.RoomList:
          item.selected = False
        self.DrawMapWindow()
        self.DrawTileWindow(True)
        self.RefreshWindows()
        #change colors on buttons
        self.TileSelectButton.SetBackgroundColour(self.SelectBGColor)
        self.TileSelectButton.SetForegroundColour(self.SelectFGColor)
        self.IconSelectButton.SetBackgroundColour(self.UnSelectBGColor)
        self.IconSelectButton.SetForegroundColour(self.UnSelectFGColor)
        self.DrawSelectButton.SetBackgroundColour(self.UnSelectBGColor)
        self.DrawSelectButton.SetForegroundColour(self.UnSelectFGColor)
        self.FogSelectButton.SetBackgroundColour(self.UnSelectBGColor)
        self.FogSelectButton.SetForegroundColour(self.UnSelectFGColor)
        if (self.DrawTools):
          self.DrawTools.Show(False)
          self.DrawTools = None
        if (fog.FogToolsDialog):
          fog.FogToolsDialog.Show(False)
          fog.FogToolsDialog = None
        gv.DrawingObject = None
        gv.DrawingToolStartPoint = None
        gv.DrawingToolPrevious = None
      return
    elif (event.GetId() == self.TileSelectButton.GetId()):      #change to Tile mode
      self.frame.SplitterSash.SplitVertically(self.frame.pnMapBasePanel, self.frame.pnTileBasePanel, gv.SashPosition)
      gv.SelectMode = 'tile'
      for label in self.textlist:
        label.selected = False
      for item in gv.RoomList:
        item.selected = False
      self.DrawMapWindow()
      self.DrawTileWindow()
      #change colors on buttons
      self.TileSelectButton.SetBackgroundColour(self.SelectBGColor)
      self.TileSelectButton.SetForegroundColour(self.SelectFGColor)
      self.IconSelectButton.SetBackgroundColour(self.UnSelectBGColor)
      self.IconSelectButton.SetForegroundColour(self.UnSelectFGColor)
      self.DrawSelectButton.SetBackgroundColour(self.UnSelectBGColor)
      self.DrawSelectButton.SetForegroundColour(self.UnSelectFGColor)
      self.FogSelectButton.SetBackgroundColour(self.UnSelectBGColor)
      self.FogSelectButton.SetForegroundColour(self.UnSelectFGColor)      
      if (self.DrawTools):
        self.DrawTools.Show(False)
        self.DrawTools = None
      if (fog.FogToolsDialog):
        fog.FogToolsDialog.Show(False)
        fog.FogToolsDialog = None
      gv.DrawingObject = None
      gv.DrawingToolStartPoint = None
      gv.DrawingToolPrevious = None
    elif (event.GetId() == self.IconSelectButton.GetId()):      #change to icon/text mode
      #hide the tile panel
      self.frame.SplitterSash.Unsplit()
      gv.SelectMode = 'icon'
      gv.ShowIcons = True
      self.frame.toolbar.ToggleTool(PyMapperDialogs.tShowIcons, True)
      for x in self.selectlist:
        x.selected = False
      self.selectlist = []
      self.nbMapNotebook.Refresh()
      self.DrawMapWindow()
      #self.DrawTileWindow()
      #change colors on buttons
      self.TileSelectButton.SetBackgroundColour(self.UnSelectBGColor)
      self.TileSelectButton.SetForegroundColour(self.UnSelectFGColor)
      self.IconSelectButton.SetBackgroundColour(self.SelectBGColor)
      self.IconSelectButton.SetForegroundColour(self.SelectFGColor)
      self.DrawSelectButton.SetBackgroundColour(self.UnSelectBGColor)
      self.DrawSelectButton.SetForegroundColour(self.UnSelectFGColor)
      self.FogSelectButton.SetBackgroundColour(self.UnSelectBGColor)
      self.FogSelectButton.SetForegroundColour(self.UnSelectFGColor)      
      if (self.DrawTools):
        self.DrawTools.Show(False)
        self.DrawTools = None
      if (fog.FogToolsDialog):
        fog.FogToolsDialog.Show(False)
        fog.FogToolsDialog = None
      gv.DrawingObject = None
      gv.DrawingToolStartPoint = None
      gv.DrawingToolPrevious = None
    elif (event.GetId() == self.DrawSelectButton.GetId()):      #change to draw mode
      self.frame.SplitterSash.Unsplit()
      gv.SelectMode = 'draw'
      gv.ShowDrawingObjects = True
      self.frame.toolbar.ToggleTool(PyMapperDialogs.tShowDrawingObjects, True)
      for x in self.selectlist:
        x.selected = False
      self.selectlist = []
      for label in self.textlist:
        label.selected = False
      for item in gv.RoomList:
        item.selected = False
      self.nbMapNotebook.Refresh()
      #self.DrawTileWindow()
      self.DrawMapWindow()
      #change the buttons
      self.TileSelectButton.SetBackgroundColour(self.UnSelectBGColor)
      self.TileSelectButton.SetForegroundColour(self.UnSelectFGColor)
      self.IconSelectButton.SetBackgroundColour(self.UnSelectBGColor)
      self.IconSelectButton.SetForegroundColour(self.UnSelectFGColor)
      self.DrawSelectButton.SetBackgroundColour(self.SelectBGColor)
      self.DrawSelectButton.SetForegroundColour(self.SelectFGColor)
      self.FogSelectButton.SetBackgroundColour(self.UnSelectBGColor)
      self.FogSelectButton.SetForegroundColour(self.UnSelectFGColor)
      if (not self.DrawTools):
        self.DrawTools = DrawToolsDialog(self.frame)
        self.DrawTools.Show(True)
      if (fog.FogToolsDialog):
        fog.FogToolsDialog.Show(False)
        fog.FogToolsDialog = None
    elif (event.GetId() == self.FogSelectButton.GetId()):      #change to fog mode
      self.frame.SplitterSash.Unsplit()
      gv.SelectMode = 'fog'
      gv.ShowDrawingObjects = True
      self.frame.toolbar.ToggleTool(PyMapperDialogs.tShowDrawingObjects, True)
      for x in self.selectlist:
        x.selected = False
      self.selectlist = []
      for label in self.textlist:
        label.selected = False
      for item in gv.RoomList:
        item.selected = False
      #self.DrawTileWindow()  #dim out the tiles
      #change the buttons
      self.nbMapNotebook.Refresh()
      self.DrawMapWindow()
      
      self.TileSelectButton.SetBackgroundColour(self.UnSelectBGColor)
      self.TileSelectButton.SetForegroundColour(self.UnSelectFGColor)
      self.IconSelectButton.SetBackgroundColour(self.UnSelectBGColor)
      self.IconSelectButton.SetForegroundColour(self.UnSelectFGColor)
      self.DrawSelectButton.SetBackgroundColour(self.UnSelectBGColor)
      self.DrawSelectButton.SetForegroundColour(self.UnSelectFGColor)
      self.FogSelectButton.SetBackgroundColour(self.SelectBGColor)
      self.FogSelectButton.SetForegroundColour(self.SelectFGColor)
      if (self.DrawTools):
        self.DrawTools.Show(False)
        self.DrawTools = None
      if (not fog.FogToolsDialog):
        fog.FogToolsDialog = fog.FogToolsDialogCore(self.frame)
        fog.FogToolsDialog.Show(True)
    return

  def DrawTileWindow(self, RebuildSortGrid=False):
    if (not gv.SelectMode == 'tile'):
      #tile window is inactive while in some other mode than tile mode
      return
    
    if (not gv.SashPosition):
      panelsize = self.TilePanel.GetSize()
    else:
      (frameWidth, frameHeight) = self.frame.GetClientSizeTuple()  #excludes scrollbars, menu, etc
      panelWidth = frameWidth - gv.SashPosition
      panelsize = wx.Size(panelWidth, frameHeight)
    if (panelsize.width == 0) or (panelsize.height == 0):
      #zero size tile panel
      logging.critical("DrawTileWindow: Zero size self.TilePanel")
      return
    if (self.tilelist == []): #empty tilelist, no tiles, therefore exit
      #still need to erase older panel if we unloaded a tileset

      self.TileBuffer = wx.Bitmap(panelsize.width, panelsize.height)
      Brush = wx.Brush(gv.TilePanelBackgroundColor)
      Pen = wx.Pen(gv.TilePanelBackgroundColor)
      self.TilePanel.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
      self.TilePanelDC = wx.BufferedDC(None, self.TileBuffer)
      self.TilePanelDC.SetBrush(Brush)
      self.TilePanelDC.SetPen(Pen)
      self.TilePanelDC.DrawRectangle(0,0, panelsize.width, panelsize.height)
      self.TilePanelDC.Clear()
      self.TilePanel.Refresh()
      return
    
    #number of rows, columns available in the TilePanel
    ncolumns = int(panelsize.width/gv.TileZoomFactor)
    nrows = int(panelsize.height/gv.TileZoomFactor)
    
    #filter according to the selected tile notebook page
    pageindex = self.nbTileNotebook.GetSelection()
    pagename = self.nbTileNotebook.GetPageText(pageindex)
    for tile in self.tilelist:
      tile.ShowOnTilePanel = False
    for page in gv.TilePageList:
      if (page.PageName == pagename):
        for tileset in page.tilesets:
          for tile in self.tilelist:
            if (tile.tilesetName == tileset):
              tile.ShowOnTilePanel = True

    if (RebuildSortGrid):
      tilearray = self.SortTilePanelBySize(nrows, ncolumns) #quickly arrange the tiles for display

      arraysize = wx.Size(ncolumns*gv.TileZoomFactor, tilearray.height*gv.TileZoomFactor)
      #check for minimum tile panel size
      self.VirtualTilePanel.width = max(panelsize.width, arraysize.width)
      self.VirtualTilePanel.height = max(panelsize.height, arraysize.height)

    self.TilePanel.SetVirtualSize(self.VirtualTilePanel)
    self.TileBuffer = wx.Bitmap(self.VirtualTilePanel.width, self.VirtualTilePanel.height)
    self.TilePanelDC = wx.BufferedDC(None, self.TileBuffer)
    Brush = wx.Brush(gv.TilePanelBackgroundColor)
    Pen = wx.Pen(gv.TilePanelBackgroundColor)
    self.TilePanel.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
    self.TilePanelDC.SetBrush(Brush)
    self.TilePanelDC.SetPen(Pen)
    self.TilePanelDC.DrawRectangle(0,0, self.VirtualTilePanel.width, self.VirtualTilePanel.height)
    self.TilePanel.SetScrollRate(20,20)
    cur_columns = 1
    cur_rows = 1 #sqares coordinate of the next tile to be placed
    max_tile_rows = 1 # How many rows in the largest tile on this row? At least 1 tile wide minimum
    xdist = gv.tileborderwidth
    ydist = gv.tileborderwidth #pixels coordinate of the next tile

    if ncolumns <= 0:
      logging.critical("Zero ncolumns")
      return
    else:
      if (gv.HighlightPen):
        self.TilePanelDC.SetPen(gv.HighlightPen)
      for tile in self.tilelist:
        if (tile.ShowOnTilePanel == True): #display of tile may be filtered off
          Xscale = gv.TileZoomFactor*tile.actualXsize #calculate the pixel size of the tile
          Yscale = gv.TileZoomFactor*tile.actualYsize
          if (gv.DualDisplayTileWindow) and (tile.sideB):
            imageA = tile.sideA.Scale(Xscale, Yscale)
            imageB = tile.sideB.Scale(Xscale, Yscale)
            bmpA = wx.BitmapFromImage(imageA)
            bmpB = wx.BitmapFromImage(imageB)
          else:
            thumb_tile = tile.tiledisplay
            size = Xscale, Yscale
            thumb_tile = thumb_tile.Scale(Xscale, Yscale)
            bitmap = wx.BitmapFromImage(thumb_tile)
          xdist = (tile.TileGrid.x * gv.TileZoomFactor) + gv.TilePanelHOffset
          ydist = (tile.TileGrid.y * gv.TileZoomFactor) + gv.TilePanelVOffset
          tile.TilePosition = (xdist, ydist)
          tile.TileRect = wx.Rect(xdist, ydist, Xscale, Yscale)
          if (gv.DualDisplayTileWindow) and (tile.sideB):
            tile.TileRectB = wx.Rect(xdist, (ydist+Yscale), Xscale, Yscale)
          if (tile.selected):
            self.TilePanelDC.SetPen(gv.SelectionPen)
            Brush = wx.Brush(gv.SelectionColor)
            self.TilePanelDC.SetBrush(Brush)
            self.TilePanelDC.DrawRectangle(xdist-gv.tileborderwidth, ydist-gv.tileborderwidth, Xscale+2*gv.tileborderwidth, Yscale+2*gv.tileborderwidth)
          if (gv.LimitTiles == True):
            if (tile.dimmed == False) and (gv.SelectMode == 'tile'):  #if in text select mode, dim all tiles
              if (gv.DualDisplayTileWindow) and (tile.sideB):
                self.TilePanelDC.DrawBitmap(bmpA, xdist, ydist, True)
                self.TilePanelDC.DrawBitmap(bmpB, xdist, ydist+Yscale, True)
                self.TilePanelDC.DrawLine(xdist,ydist+Yscale, xdist+Xscale, ydist+Yscale)
              else:
                self.TilePanelDC.DrawBitmap(bitmap, xdist, ydist, True)
            else:
              if (gv.DualDisplayTileWindow) and (tile.sideB):
                imageA = tile.sideA.Scale(Xscale, Yscale)
                imageB = tile.sideB.Scale(Xscale, Yscale)
                imageA = imageA.AdjustChannels(1.0, 1.0, 1.0, gv.TileDimFactor)
                imageB = imageB.AdjustChannels(1.0, 1.0, 1.0, gv.TileDimFactor)
                bmpA = wx.BitmapFromImage(imageA)
                bmpB = wx.BitmapFromImage(imageB)
                self.TilePanelDC.DrawBitmap(bmpA, xdist, ydist, True)
                self.TilePanelDC.DrawBitmap(bmpB, xdist, ydist+Yscale, True)
                self.TilePanelDC.SetPen(gv.HighlightPen)
                self.TilePanelDC.DrawLine(xdist,ydist+Yscale, xdist+Xscale, ydist+Yscale)
              else:
                dim_image = thumb_tile.AdjustChannels(1.0, 1.0, 1.0, gv.TileDimFactor)
                bitmap = wx.BitmapFromImage(dim_image)
                self.TilePanelDC.DrawBitmap(bitmap, xdist, ydist, True)
          else:
            if (gv.DualDisplayTileWindow) and (tile.sideB):
              self.TilePanelDC.DrawBitmap(bmpA, xdist, ydist, True)
              self.TilePanelDC.DrawBitmap(bmpB, xdist, ydist+Yscale, True)
              self.TilePanelDC.SetPen(gv.HighlightPen)
              self.TilePanelDC.DrawLine(xdist,ydist+Yscale, xdist+Xscale, ydist+Yscale)
            else:
              self.TilePanelDC.DrawBitmap(bitmap, xdist, ydist, True)
      self.TilePanel.Refresh()
      return

  def OnSnapToGrid(self, event):
    gv.SnapToGrid = self.frame.toolbar.GetToolState(id=PyMapperDialogs.tSnapToGrid)
    return

  def SnapTileToMapGrid (self, drop_point, tile):
    """drop_point is the mouse coordinate on screen
    tile is the selected tile to snap
    returns the grid location of the image"""
    if (gv.SnapToGrid):
      #find the grid cell on the map
      gridpoint = self.MapPanel.CalcUnscrolledPosition(drop_point)
      Xdest = gridpoint[0] / (gv.MapZoomFactor)
      Ydest = gridpoint[1] / (gv.MapZoomFactor)
      mapgrid_point = wx.Point(Xdest, Ydest)
      #find the grid point on the tile
      size = wx.Point(tile.actualXsize*gv.MapZoomFactor,
                      tile.actualYsize*gv.MapZoomFactor)
      Xtile = tile.hotspot[0] / (gv.MapZoomFactor)
      Ytile = tile.hotspot[1] / (gv.MapZoomFactor)
      tilegrid_point = wx.Point(Xtile, Ytile)
      final = mapgrid_point - tilegrid_point
      tile.SnapToGrid = True
      return wx.Point2D(final.x, final.y)
    else:
      #find the grid cell on the map for sandbox mode
      gridpoint = self.MapPanel.CalcUnscrolledPosition(drop_point)
      Xdest = gridpoint[0] / (gv.MapZoomFactor*1.0)
      Ydest = gridpoint[1] / (gv.MapZoomFactor*1.0)
      mapgrid_point = wx.Point2D(Xdest, Ydest)
      #find the grid point on the tile
      size = wx.Point2D(tile.actualXsize*gv.MapZoomFactor,tile.actualYsize*gv.MapZoomFactor)
      Xtile = tile.hotspot[0] / (gv.MapZoomFactor*1.0)
      Ytile = tile.hotspot[1] / (gv.MapZoomFactor*1.0)
      tilegrid_point = wx.Point2D(Xtile, Ytile)
      final = mapgrid_point - tilegrid_point
      tile.SnapToGrid = False
      return final

  def FindSelectedTileInLists(self):
    for tile in self.tilelist:
      if (tile.selected):
        gv.SelectedFromTilePanel = True
        return tile
    if (self.selectlist):
      tile = self.selectlist[0]
      gv.SelectedFromTilePanel = False
      return tile
    return None

  def FindTileOnMap(self, mousepoint):
    gridpoint = self.MapPanel.CalcUnscrolledPosition(mousepoint)
    foundtile = False
    for tile in self.maplist:
      rect = wx.Rect2D(tile.MapRect.x*gv.MapZoomFactor, tile.MapRect.y*gv.MapZoomFactor,
                       tile.MapRect.width*gv.MapZoomFactor, tile.MapRect.height*gv.MapZoomFactor)
      foundtile = rect.Contains(gridpoint)
      if (foundtile):
        return tile
    return None

  def OnTilePanelLeave(self, event):
    # Mouse left the TilePanel
    self.MouseOnTilePanel = False
    foundtile = self.FindSelectedTileInLists()
    if (foundtile):
      #a tile was selected and is dragging
      gv.AddTile = True
    else:
      gv.AddTile = False
    return

  def MapWindowLClickDown(self, event):
    gv.RubberBandStart = event.GetPosition()
    gv.RubberBandPrevious = None
    gv.RubberBandEnd = event.GetPosition()
    for tile in self.tilelist:
      #de-select tiles on the tile panel
      tile.selected = False
    self.DrawTileWindow()

    mouse_pos = event.GetPosition()
    gridpoint = self.MapPanel.CalcUnscrolledPosition(mouse_pos)
    if ((event.ControlDown()) or (gv.SelectMode == 'icon')): #selecting text or room icon
      #check for room icons first
      found = False
      for room in gv.RoomList:
        rect = wx.Rect2D((room.x * gv.MapZoomFactor), (room.y * gv.MapZoomFactor),
                         room.MapRect.width, room.MapRect.height)
        gridpoint2D = wx.Point2D(gridpoint.x, gridpoint.y)
        found = rect.Contains(gridpoint2D)
        if (found == True):
          room.selected = True
          self.StartDragPos = gridpoint
          self.AllowDrag = True #allow dragging of text on the MapPanel
          scale = int(gv.MapZoomFactor * gv.IconScaleFactor)
          scaleImage = room.Icon.Scale(scale, scale)
          self.dragImage = wx.DragImage(wx.BitmapFromImage(scaleImage), wx.StockCursor(wx.CURSOR_HAND)) #this is the image to move on the MapPanel
          gv.AddTile = False
        else:
          room.selected = False
      if (not found): #check for text annotations if no icon found
        for text in self.textlist:
          gridpoint2D = wx.Point2D(gridpoint.x, gridpoint.y)
          found = text.extent.Contains(gridpoint2D)
          if (found == True):
            text.selected = True
            self.StartDragPos = gridpoint
            self.AllowDrag = True #allow dragging of text on the MapPanel
            self.dragImage = wx.DragImage(text.bmp, wx.StockCursor(wx.CURSOR_HAND)) #this is the image to move on the MapPanel
            gv.AddTile = False
          else:
            text.selected = False
            self.MapPanel.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
    elif (gv.SelectMode == 'draw') or (gv.SelectMode == 'fog'):
      found = False
      pageIndex = self.nbMapNotebook.GetSelection()
      pageName = gv.MapPageList[pageIndex].PageName
      if (gv.DrawingTool == 'Freehand'):
        self.MapPanel.SetCursor(wx.StockCursor(wx.CURSOR_PENCIL))
        gv.DrawingToolStartPoint = self.MapPanel.CalcUnscrolledPosition(event.GetPosition())
        begin_point = self.EncodeDrawingPoint(gv.DrawingToolStartPoint, gv.MapZoomFactor)
        gv.DrawingObject = gv.DrawingObject_Record(startpoint=begin_point,
                                                   tool_type='Freehand', init_brush=wx.TRANSPARENT_BRUSH,
                                                   init_pen=gv.DrawingToolPen, init_page_name=pageName)
      elif (gv.DrawingTool == 'FillRect') or (gv.DrawingTool == 'OutlineRect'):
        self.MapPanel.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))
        gv.DrawingToolStartPoint = self.MapPanel.CalcUnscrolledPosition(event.GetPosition())
        begin_point = self.EncodeDrawingPoint(gv.DrawingToolStartPoint, gv.MapZoomFactor)
        if (gv.DrawingTool == 'OutlineRect'):
          gv.DrawingObject = gv.DrawingObject_Record(startpoint=begin_point,
                                                     tool_type='OutlineRect',
                                                     init_brush=wx.TRANSPARENT_BRUSH,
                                                     init_pen=gv.DrawingToolPen,
                                                     init_page_name=pageName)
        else:
          gv.DrawingObject = gv.DrawingObject_Record(startpoint=begin_point,
                                                     tool_type='FillRect', init_brush=gv.DrawingToolBrush,
                                                     init_pen=gv.DrawingToolPen, init_page_name=pageName)
      elif (gv.DrawingTool == 'OutlineCircle') or (gv.DrawingTool == 'FillCircle'):
        self.MapPanel.SetCursor(wx.StockCursor(wx.CURSOR_BULLSEYE))
        gv.DrawingToolStartPoint = self.MapPanel.CalcUnscrolledPosition(event.GetPosition())
        begin_point = self.EncodeDrawingPoint(gv.DrawingToolStartPoint, gv.MapZoomFactor)
        if (gv.DrawingTool == 'OutlineCircle'):
          gv.DrawingObject = gv.DrawingObject_Record(startpoint=begin_point,
                                                     tool_type='OutlineCircle',
                                                     init_brush=wx.TRANSPARENT_BRUSH,
                                                     init_pen=gv.DrawingToolPen,
                                                     init_page_name=pageName)
        else:
          gv.DrawingObject = gv.DrawingObject_Record(startpoint=begin_point,
                                                     tool_type='FillCircle',
                                                     init_brush=gv.DrawingToolBrush,
                                                     init_pen=gv.DrawingToolPen,
                                                     init_page_name=pageName)
      elif (gv.DrawingTool == 'Multiline'):
        self.MapPanel.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))
        gv.DrawingToolStartPoint = self.MapPanel.CalcUnscrolledPosition(event.GetPosition())
        begin_point = self.EncodeDrawingPoint(gv.DrawingToolStartPoint, gv.MapZoomFactor)
        if (gv.DrawingObject):
          #add a line point
          point = self.EncodeDrawingPoint(self.MapPanel.CalcUnscrolledPosition(event.GetPosition()), gv.MapZoomFactor)
          gv.DrawingObject.line.append(point)  #set the endpoint of the previous segment
          gv.DrawingToolPrevious = gv.DrawingToolStartPoint
          gv.DrawingToolStartPoint = self.MapPanel.CalcUnscrolledPosition(event.GetPosition())
        else:
          gv.DrawingObject = gv.DrawingObject_Record(startpoint=begin_point, tool_type='Multiline',
                                                     init_brush=wx.TRANSPARENT_BRUSH, init_pen=gv.DrawingToolPen,
                                                     init_page_name=pageName)
      elif (gv.DrawingTool == 'Line'):
        #set the start point of the line
        self.MapPanel.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))
        gv.DrawingToolStartPoint = self.MapPanel.CalcUnscrolledPosition(event.GetPosition())
        begin_point = self.EncodeDrawingPoint(gv.DrawingToolStartPoint, gv.MapZoomFactor)
        pageIndex = self.nbMapNotebook.GetSelection()
        gv.DrawingObject = gv.DrawingObject_Record(startpoint=begin_point, tool_type='Line',
                                                   init_brush=wx.TRANSPARENT_BRUSH,
                                                   init_pen=gv.DrawingToolPen, init_page_name=pageName)
      if ((gv.DrawingTool == 'Select') or (gv.DrawingTool == 'Delete')
          or (gv.DrawingTool == 'GetProperty') or (gv.DrawingTool == 'ChangeProperty')):
        mpoint = self.MapPanel.CalcUnscrolledPosition(event.GetPosition())
        mousepoint = wx.Point2D(mpoint.x, mpoint.y)
        for item in self.DrawingList:
          index = 0
          for rect in item.handles:
            found = rect.Contains(mousepoint)
            if (found):
              if (gv.DrawingTool == 'Delete'):
                self.DrawingList.remove(item)
              elif (gv.DrawingTool == 'Select'):
                item.handle_index = index
                gv.DrawingObject = item
                item.selected = True
              elif (gv.DrawingTool == 'GetProperty'):
                self.UpdateDrawingToolsSelectedItem(item, 'GetProperty')
              elif (gv.DrawingTool == 'ChangeProperty'):
                self.UpdateDrawingToolsSelectedItem(item, 'ChangeProperty')
              break  #break out of the handles list
            else:
              item.handle_index = None
              item.selected = False
              index += 1
          if (found):
            break  #break out of the drawing list

      if (not found) and (gv.DrawingTool == 'Select'):
        #needed to erase highlighting if something was previously selected
        self.DrawMapWindow()
        return
    elif ((self.selectlist != []) and (event.m_shiftDown)): #multiple tiles selected and SHIFT key down, so move the group
      rect = self.CalculateMapExtents(self.selectlist)
      dragImage = wx.Bitmap(rect.width*gv.MapZoomFactor,
                                 rect.height*gv.MapZoomFactor)
      memDC = wx.MemoryDC()
      memDC.SelectObject(dragImage)
      for tile in self.selectlist:
        source = wx.MemoryDC(tile.mapdisplay)
        x = int((tile.MapRect.x - rect.x)*gv.MapZoomFactor)
        y = int((tile.MapRect.y - rect.y)*gv.MapZoomFactor)
        memDC.Blit(x, y, tile.mapdisplay.GetWidth(), tile.mapdisplay.GetHeight(),
                   source, 0,0)
      memDC.SelectObject(wx.NullBitmap)
      mask = wx.Mask(dragImage, wx.BLACK)
      dragImage.SetMask(mask)
      self.dragImage = wx.DragImage(dragImage, wx.StockCursor(wx.CURSOR_HAND))
      self.AllowDrag = True
      gv.AddTile = False
    else:  #selecting a single tiles
      count = 0
      for x in self.selectlist:
        x.selected = False
      self.selectlist = []
      foundtile = False
      for tile in self.maplist:
        if ((tile.layer == gv.ActiveLayer) and
            (tile.page == gv.MapPageList[self.nbMapNotebook.GetSelection()].PageName)):
          # SnapToGrid changed from wxRect to wxRect2D; gridpoint to gridpoint2D
          rect = wx.Rect2D(tile.MapRect.x*gv.MapZoomFactor,
                           tile.MapRect.y*gv.MapZoomFactor,
                           tile.MapRect.width*gv.MapZoomFactor,
                           tile.MapRect.height*gv.MapZoomFactor)
          gridpoint2D = wx.Point2D(gridpoint.x, gridpoint.y)
          foundtile = rect.Contains(gridpoint2D)

          if (foundtile):
            count += 1
            #tolerance for movement
            self.StartDragPos = gridpoint
            if (self.selectlist):
              self.selectlist.insert(0,tile)
            else:
              self.selectlist.append(tile)
      if (count == 0):
        self.MapPanel.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
        for x in self.selectlist:
          x.selected = False
        self.selectlist = []
      if (self.selectlist):
        for tile in self.selectlist:
          tile.selected = False
        self.AllowDrag = True #allow dragging of image on the MapPanel
        self.dragImage = wx.DragImage(self.selectlist[0].mapdisplay, wx.StockCursor(wx.CURSOR_HAND)) #this is the image to move on the MapPanel
        gv.AddTile = False
        self.selectlist[0].selected = True
    self.DrawMapWindow()
    if (gv.rtc_open == False):
      self.MapPanel.SetFocus()
    return

  def MapWindowDClick(self, event):
    found = False
    mouse_pos = event.GetPosition()
    screenpoint = self.MapPanel.CalcUnscrolledPosition(mouse_pos)
    gridpoint = wx.Point2D(screenpoint.x, screenpoint.y)
    if ((event.ControlDown()) or (gv.SelectMode == 'icon')): #check for text or icons
      for room in gv.RoomList:
        rect = wx.Rect2D((room.x * gv.MapZoomFactor), (room.y * gv.MapZoomFactor),
                         room.MapRect.width, room.MapRect.height)
        found = rect.Contains(gridpoint)
        if (found):
          self.RMapAddIconRoom(room=room)
          break
      if (self.textlist == []):
        return
      if (not found):
        for text in self.textlist:
          found = text.extent.Contains(gridpoint)
          if (found == True):
            dlg = wx.TextEntryDialog(self.frame, "Enter Text Annotation", "Text:")
            dlg.SetValue(text.text)
            result = dlg.ShowModal()
            if (result == wx.ID_OK):
              text.text = dlg.GetValue()
              text = self.CreateTextLabelBitmap(text, gv.MapZoomFactor)
            dlg.Destroy()
    elif (gv.SelectMode == 'draw') or (gv.SelectMode == 'fog'):
      if (gv.DrawingTool == 'Multiline'):
        self.MapPanel.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
        endpoint = self.EncodeDrawingPoint(self.MapPanel.CalcUnscrolledPosition(event.GetPosition()), gv.MapZoomFactor)
        gv.DrawingObject.line.append(endpoint)
        self.DrawingList.append(gv.DrawingObject)
        gv.DrawingObject = None
        gv.DrawingToolStartPoint = None
        gv.DrawingToolPrevious = None
        gv.DrawingNextStep = 'start'
        gv.PromptSave = True
        self.DrawMapWindow()
    else:  #check the tiles on the map window
      if (self.selectlist):
        tile = self.selectlist[0]
        rect = wx.Rect2D(tile.MapRect.x*gv.MapZoomFactor, tile.MapRect.y*gv.MapZoomFactor,
                         tile.MapRect.width*gv.MapZoomFactor, tile.MapRect.height*gv.MapZoomFactor)
        foundtile = rect.Contains(gridpoint)
        if (foundtile) and (tile.sideB == None):
          wx.MessageBox("No reverse side to display")
          return
        if (foundtile):
          self.UndoActionEvent(flag='FLIP_TILE',tile=tile)
          if (tile.showingBside): #currently on the B side, so flip over the tile
            tile.showingBside = False
          elif (tile.sideB): # was on the A side, show the B side
            tile.showingBside = True
          tile.GenerateMapDisplay(gv.MapZoomFactor)
    self.DrawMapWindow()
    return

  def UpdateDrawingToolsSelectedItem(self, item, mode):
    '''change the color selection and other properties'''
    if (mode == 'GetProperty'):
      gv.DrawingToolPen = item.pen
      if (self.DrawTools):
        self.DrawTools.spLineWidth.SetValue(item.pen.GetWidth())
      gv.DrawOutlineColor = item.pen.GetColour()
      gv.DrawingToolBrush = item.brush
      gv.DrawFillColor = item.brush.GetColour()
      self.DrawTools.slFillTransparency.SetValue(gv.DrawFillColor.Alpha())
      self.DrawTools.bChooseFillColor.SetColour(gv.DrawFillColor)
      self.DrawTools.bChooseOutlineColor.SetColour(gv.DrawOutlineColor)
      self.DrawTools.UpdateLineSample()
    elif (mode == 'ChangeProperty'):
      if (self.DrawTools):
        item.pen.SetWidth(self.DrawTools.spLineWidth.GetValue())
      item.pen.SetColour(gv.DrawOutlineColor)
      item.brush = gv.DrawingToolBrush
    return

  def DecodeDrawingPoint(self, data, resolution, typedef='FLOAT'):
    """Convert a decimal location point2D to screen coordinates. Return wxPoint2D unless typedef is set to INT
      resolution should be set to either gv.MapZoomFactor or gv.PrintResolution"""
    #need to use resolution instead of mapzoomfactor
    if (typedef == 'INT'):
      newdata = wx.Point(data.x*resolution, data.y*resolution)
    else:  # typedef == 'FLOAT'
      newdata = wx.Point2D(data.x*resolution, data.y*resolution)
    return newdata

  def DecodeDrawingRect(self, data, resolution, typedef='FLOAT'):
    if (typedef == 'INT'):
      newdata = wx.Rect(data.x*resolution, data.y*resolution, 
                        data.width*resolution, data.height*resolution)
    else:
      newdata = wx.Rect2D(data.x*resolution, data.y*resolution, 
                          data.width*resolution, data.height*resolution)
    return newdata

  def EncodeDrawingPoint(self, data, resolution, datatype='POINT'):
    """Convert screen coordinates to decimal location.  Return wxPoint2D or wxRect2D depending on datatype (POINT or RECT)"""
    if (datatype == 'POINT'):
      newdata = wx.Point2D(data.x/(1.0*resolution), data.y/(1.0*resolution))
    elif (datatype == 'RECT'):
      newdata = wx.Rect2D(data.x/(1.0*resolution), data.y/(1.0*resolution),
                          data.width/(1.0*resolution), data.height/(1.0*resolution))
    return newdata

  def MapWindowLClickUp(self, event=None):
    if ((event.ControlDown()) or (gv.SelectMode == 'icon')):  # text or icon was moving
      if ((self.dragImage) and (self.AllowDrag)):
        if (not self.TextInMotion):
          self.dragImage = None
          self.AllowDrag = False
          self.selected = False
          return
        #check icon first
        for room in gv.RoomList:
          if (room.selected):
            mouse = event.GetPosition()
            gridpoint = self.MapPanel.CalcUnscrolledPosition(mouse)
            self.UndoActionEvent(flag='MOVE_ICON', icon=room,
                                 dx=room.MapRect.x, dy=room.MapRect.y)
            if (gv.SnapIconToGrid):
              room.x = gridpoint.x//(1.0*gv.MapZoomFactor)
              room.y = gridpoint.y//(1.0*gv.MapZoomFactor)
            else:
              room.x = gridpoint.x/(1.0*gv.MapZoomFactor)
              room.y = gridpoint.y/(1.0*gv.MapZoomFactor)
            #self.dragImage.Move(gridpoint)
            #self.dragImage.Hide()
            self.dragImage.EndDrag()
            self.dragImage = None
            self.AllowDrag = False
            self.TextInMotion = False
            room.selected = False
            self.DrawMapWindow()
            break
        if (self.TextInMotion):  #didn't find an icon, keep checking text list
          if (self.textlist == []):
            return
          for txt in self.textlist:
            if (txt.selected):
              mouse = event.GetPosition()
              gridpoint = self.MapPanel.CalcUnscrolledPosition(mouse)
              self.UndoActionEvent(flag='MOVE_TEXT', text=txt, dx=txt.x, dy=txt.y)
              txt.x = gridpoint.x/(1.0*gv.MapZoomFactor)
              txt.y = gridpoint.y/(1.0*gv.MapZoomFactor)
              txt.extent.x = gridpoint.x
              txt.extent.y = gridpoint.y
              self.dragImage.Move(gridpoint)
              self.dragImage.Hide()
              self.dragImage.EndDrag()
              self.dragImage = None
              self.AllowDrag = False
              self.TextInMotion = False
              txt.selected = False
              self.DrawMapWindow()
              break
    elif (gv.SelectMode == 'draw') or (gv.SelectMode == 'fog'):
      pageIndex = self.nbMapNotebook.GetSelection()
      if (gv.DrawingTool == 'Select') or (gv.DrawingTool == 'Delete'):
        slope_tolerance = 0.5
        circle_tolerance = 3
        line_tolerance = 3
        checkVertical = False
        found_item = False
        mpoint = self.MapPanel.CalcUnscrolledPosition(event.GetPosition())
        if (gv.DrawingNextStep == 'modify'):
          #moved a handle in the item
          for item in self.DrawingList:
            if (item.selected):
              found_item = True
              if (item.tool == 'Line') or (item.tool == 'Multiline'):
                item.line[item.handle_index] = self.EncodeDrawingPoint(gv.DrawingToolPrevious, gv.MapZoomFactor)
                self.DrawMapWindow()
                gv.DrawingObject = None
                gv.DrawingToolStartPoint = None
                gv.DrawingToolPrevious = None
                gv.DrawingNextStep = 'start'
                item.handle_index = None
                gv.PromptSave = True
                break
              elif (item.tool == 'OutlineRect') or (item.tool == 'FillRect') or (item.tool == 'Image'):
                if (item.handle_index == 4):
                  #move the rect
                  newrect = self.DecodeDrawingRect(item.rect, gv.MapZoomFactor)
                  offset = gv.DrawingToolStartPoint - gv.DrawingToolPrevious
                  newrect.x -= offset.x
                  newrect.y -= offset.y
                else:
                  #move a corner
                  newrect = wx.RectPP(gv.DrawingToolPrevious, gv.DrawingToolStartPoint)
                item.rect = self.EncodeDrawingPoint(newrect, gv.MapZoomFactor, 'RECT')
                self.DrawMapWindow()
                gv.DrawingObject = None
                gv.DrawingToolStartPoint = None
                gv.DrawingToolPrevious = None
                gv.DrawingNextStep = 'start'
                item.handle_index = None
                gv.PromptSave = True
                break
              elif (item.tool == 'OutlineCircle') or (item.tool == 'FillCircle'):
                if (item.handle_index == 0):
                  item.circle[0] = self.EncodeDrawingPoint(gv.DrawingToolPrevious, gv.MapZoomFactor)
                else:
                  distance_point = gv.DrawingToolPrevious - gv.DrawingToolStartPoint
                  radius = (math.sqrt(math.pow(distance_point.x, 2) + math.pow(distance_point.y,2))/(1.0*gv.MapZoomFactor))
                  item.circle[1] = radius
                self.DrawMapWindow()
                gv.DrawingObject = None
                gv.DrawingToolStartPoint = None
                gv.DrawingToolPrevious = None
                gv.DrawingNextStep = 'start'
                item.handle_index = None
                gv.PromptSave = True
                break
              elif (item.tool == 'Freehand'):
                item.line[item.handle_index] = self.EncodeDrawingPoint(gv.DrawingToolPrevious, gv.MapZoomFactor)
                self.DrawMapWindow()
                gv.DrawingObject = None
                gv.DrawingToolStartPoint = None
                gv.DrawingToolPrevious = None
                item.handle_index = None
                gv.DrawingNextStep = 'start'
                gv.PromptSave = True
          if (not found_item):
            gv.DrawingObject = None
            gv.DrawingToolStartPoint = None
            gv.DrawingToolPrevious = None
            gv.DrawIntermediate = False
            gv.DrawingNextStep = 'start'
      elif (gv.DrawingTool == 'Line') or (gv.DrawingTool == 'Fog_Line'):
        self.MapPanel.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
        endpoint = self.EncodeDrawingPoint(self.MapPanel.CalcUnscrolledPosition(event.GetPosition()), gv.MapZoomFactor)
        gv.DrawingObject.layer = gv.LayerList[gv.ActiveLayer].index
        gv.DrawingObject.line.append(endpoint)
        self.DrawingList.append(gv.DrawingObject)
        gv.DrawingObject = None
        gv.DrawingToolStartPoint = None
        gv.DrawingToolPrevious = None
        gv.DrawingNextStep = 'start'
        gv.PromptSave = True
        self.DrawMapWindow()
      elif (gv.DrawingTool == 'Multiline'):
        pass
      elif (gv.DrawingTool == 'OutlineCircle') or (gv.DrawingTool == 'FillCircle') or (gv.DrawingTool == 'Fog_FillCircle'):
        self.MapPanel.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
        endpoint = self.MapPanel.CalcUnscrolledPosition(event.GetPosition())
        distance_point = endpoint - self.DecodeDrawingPoint(gv.DrawingObject.circle[0], gv.MapZoomFactor, 'INT')
        radius = (math.sqrt(math.pow(distance_point.x, 2) + math.pow(distance_point.y,2))/(1.0*gv.MapZoomFactor))
        gv.DrawingObject.circle.append(radius)
        gv.DrawingObject.zoomfactor = gv.MapZoomFactor
        gv.DrawingObject.layer = gv.LayerList[gv.ActiveLayer].index
        self.DrawingList.append(gv.DrawingObject)
        gv.DrawingObject = None
        gv.DrawingToolStartPoint = None
        gv.DrawingToolPrevious = None
        gv.DrawingNextStep = 'start'
        self.DrawMapWindow()
      elif (gv.DrawingTool == 'FillRect') or (gv.DrawingTool == 'OutlineRect') or (gv.DrawingTool == 'Fog_FillRect'):
        self.MapPanel.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
        endpoint = self.MapPanel.CalcUnscrolledPosition(event.GetPosition())
        newrect = wx.RectPP(endpoint, gv.DrawingToolStartPoint)
        gv.DrawingObject.rect = self.EncodeDrawingPoint(data=newrect, resolution=gv.MapZoomFactor, datatype='RECT')
        gv.DrawingObject.layer = gv.LayerList[gv.ActiveLayer].index
        self.DrawingList.append(gv.DrawingObject)
        gv.DrawingObject = None
        gv.DrawingToolStartPoint = None
        gv.DrawingToolPrevious = None
        gv.DrawingNextStep = 'start'
        gv.PromptSave = True
        self.DrawMapWindow()
      elif (gv.DrawingTool == 'Freehand') or (gv.DrawingTool == 'Fog_AddFreehand') or (gv.DrawingTool == 'Fog_EraseFreehand'):
        #temp_list = []
        #for point in gv.DrawingObject.line:
        #  p1 = self.DecodeDrawingPoint(point, 'INT')
        #  p2 = self.MapPanel.CalcScrolledPosition(p1)
        #  p3 = self.EncodeDrawingPoint(p2)
        #  temp_list.append(p3)
        #gv.DrawingObject.line = temp_list
        self.MapPanel.SetCursor(wx.StockCursor(wx.CURSOR_DEFAULT))
        gv.DrawingObject.zoomfactor = gv.MapZoomFactor
        gv.DrawingObject.layer = gv.LayerList[gv.ActiveLayer].index
        self.DrawingList.append(gv.DrawingObject)
        gv.DrawingObject = None
        gv.DrawingToolStartPoint = None
        gv.DrawingToolPrevious = None
        gv.DrawIntermediate = False
        gv.DrawingNextStep = 'start'
        gv.PromptSave = True
        self.DrawMapWindow()
      elif (gv.DrawingTool == 'Point'):
        gv.DrawingToolStartPoint = self.MapPanel.CalcUnscrolledPosition(event.GetPosition())
        begin_point = self.EncodeDrawingPoint(gv.DrawingToolStartPoint, gv.MapZoomFactor)
        gv.DrawingObject = gv.DrawingObject_Record(startpoint=begin_point, tool_type='Point', init_brush=gv.DrawingToolBrush, init_pen=gv.DrawingToolPen, init_page_name=gv.MapPageList[pageIndex].PageName)
        if (gv.SelectMode == 'draw'):
          gv.DrawingObject.circle.append(gv.DrawingToolPen.GetWidth()/gv.MapZoomFactor)  #radius of the point
        elif (gv.SelectMode == 'fog'):
          gv.DrawingObject.circle.append(fog.FogToolsDialog.spLightRadius.GetValue()/gv.MapZoomFactor)  #radius of the point
        gv.DrawingObject.zoomfactor = gv.MapZoomFactor
        gv.DrawingObject.layer = gv.LayerList[gv.ActiveLayer].index
        self.DrawingList.append(gv.DrawingObject)
        gv.DrawingObject = None
        gv.DrawingToolStartPoint = None
        gv.DrawingToolPrevious = None
        gv.DrawingNextStep = 'start'
        self.DrawMapWindow()
      elif (gv.DrawingTool == 'Image'):
        if (gv.DrawingNextStep == 'start'):
          dlg = wx.FileDialog(self.frame, message="Choose image to import", defaultDir=gv.root_directory,
                              defaultFile="", wildcard=images_wildcard, style=wx.OPEN | wx.CHANGE_DIR)
          result = dlg.ShowModal()
          if (result == wx.ID_OK):
            filename = dlg.GetFilename()
            path = dlg.GetPath()
            mousepoint = self.MapPanel.CalcUnscrolledPosition(event.GetPosition())
            gv.DrawingObject = gv.DrawingObject_Record(startpoint=gv.DrawingToolStartPoint,
                                                       tool_type='Image',
                                                       init_page_name=pageName)
            gv.DrawingObject.image = wx.Image(path, wx.BITMAP_TYPE_ANY)
            gv.DrawingObject.image_filename = filename
            gv.DrawingObject.image_path = dlg.GetDirectory()
            newrect = wx.Rect(mousepoint.x, mousepoint.y, gv.DrawingObject.image.GetWidth(), gv.DrawingObject.image.GetHeight())
            gv.DrawingObject.rect = self.EncodeDrawingPoint(newrect, gv.MapZoomFactor, 'RECT')
            gv.DrawingObject.layer = gv.LayerList[gv.ActiveLayer].index
            self.DrawingList.append(gv.DrawingObject)
            gv.DrawingObject = None
            gv.DrawingToolStartPoint = None
            gv.DrawingToolPrevious = None
            gv.DrawingNextStep = 'start'
            gv.DrawingTool = 'Select'
            gv.PromptSave = True
            self.DrawTools.ChangeToolBitmaps('Select')
            self.DrawMapWindow()
            dlg.Destroy()
      else:
        gv.DrawingObject = None
        gv.DrawingToolStartPoint = None
        gv.DrawingToolPrevious = None
        gv.DrawIntermediate = False
        gv.DrawingNextStep = 'start'
      return
    else: # gv.SelectMode = tile
      if ((self.dragImage) and (self.AllowDrag) and (self.TileInMotion)):
        # An image was selected, and we were dragging it around
        selected_tile = self.FindSelectedTileInLists()
        mouse = event.GetPosition()
        previous_point = wx.Point2D()
        final_point = self.SnapTileToMapGrid(mouse, selected_tile)
        #self.dragImage.Move(final_point)   #don't think we need to do the final .Move command
        #self.dragImage.Hide()
        self.dragImage.EndDrag()
        self.dragImage = None
        self.AllowDrag = False
        if (gv.SelectedFromTilePanel):
          selected_tile.GenerateMapDisplay(gv.MapZoomFactor)
          selected_tile.selected = False

          newtile = self.CopyTile(selected_tile)
          newtile.layer = gv.ActiveLayer
          index = self.nbMapNotebook.GetSelection()
          newtile.page = self.nbMapNotebook.GetPageText(index)
          newtile.layer = gv.LayerList[gv.ActiveLayer].index
          self.maplist.append(newtile)
          gv.PromptSave = True
          for tset in gv.tilesets:
            if tset.SetID == newtile.tilesetID:
              tset.used = True
          newtile.index = self.MasterIndex
          self.MasterIndex += 1
          newtile.order = len(self.maplist)
          newtile.MapPosition = final_point
          newtile.MapRect = wx.Rect2D(final_point.x, final_point.y, selected_tile.actualXsize, selected_tile.actualYsize)

          self.UndoActionEvent(flag="ADD_TILE", tile=newtile)
          selected_tile.num_used += 1

          self.UpdateTileQuantity(newtile.page)
          self.DrawTileWindow()
        else:
          if (event.m_shiftDown):
            FromRect = self.CalculateMapExtents(self.selectlist)
            offset = wx.Point2D(FromRect.x-final_point.x, FromRect.y-final_point.y)
            for tile in self.selectlist:
              tile.MapRect.x -= offset.x
              tile.MapRect.y -= offset.y
              previous_point.x = tile.MapPosition.x
              previous_point.y = tile.MapPosition.y
              tile.MapPosition -= offset
              self.UndoActionEvent(flag="MOVE_TILE", tile=tile, point=previous_point)
          else:
            FromRect = self.selectlist[0].MapRect
            offset = wx.Point2D(FromRect.x-final_point.x, FromRect.y-final_point.y)
            self.selectlist[0].MapRect.x -= offset.x
            self.selectlist[0].MapRect.y -= offset.y
            previous_point.x = self.selectlist[0].MapPosition.x
            previous_point.y = self.selectlist[0].MapPosition.y
            self.selectlist[0].MapPosition -= offset
            self.UndoActionEvent(flag="MOVE_TILE", tile=self.selectlist[0], point=previous_point)

        self.TileInMotion = False 
        self.MapStruct.GridExtents = self.CalculateMapExtents(self.maplist)

        gv.AddTile = False
      if self.hiliteShape:
        self.MapPanel.RefreshRect(self.hiliteShape.GetRect())
        self.hiliteShape = None

    if (gv.RubberBandEnd):
      # selection box created
      TopLeft = wx.Point()
      BottomRight = wx.Point()
      RBStart = self.MapPanel.CalcUnscrolledPosition(gv.RubberBandStart)
      RBEnd = self.MapPanel.CalcUnscrolledPosition(gv.RubberBandEnd)
      if (RBStart.x > RBEnd.x):
        #Start is on right side of end point
        if (RBStart.y > RBEnd.y):
          BottomRight = RBStart
          TopLeft = RBEnd
        else:
          BottomRight.x = RBStart.x
          BottomRight.y = RBEnd.y
          TopLeft.x = RBEnd.x
          TopLeft.y = RBStart.y
      else:
        #Start is on left side of end point
        if (RBStart.y < RBEnd.y):
          BottomRight = RBEnd
          TopLeft = RBStart
        else:
          BottomRight.x = RBEnd.x
          BottomRight.y = RBStart.y
          TopLeft.x = RBStart.x
          TopLeft.y = TopLeft.y
      SelectionRect = wx.Rect2D(TopLeft.x, TopLeft.y, BottomRight.x-TopLeft.x, BottomRight.y-TopLeft.y)
      for tile in self.maplist:
        if (tile.page == gv.MapPageList[self.nbMapNotebook.GetSelection()].PageName):
          rect = wx.Rect2D(tile.MapRect.x*gv.MapZoomFactor, tile.MapRect.y*gv.MapZoomFactor,
                           tile.MapRect.width*gv.MapZoomFactor, tile.MapRect.height*gv.MapZoomFactor)
          if (SelectionRect.ContainsRect(rect)):
            self.selectlist.append(tile)
      self.DrawMapWindow()
      #reset the rubberband
      gv.RubberBandStart = None
      gv.RubberBandEnd = None
      gv.RubberBandPrevious = None
      if (gv.SelectMode == 'tile'):
        self.MapPanel.SetCursor(wx.StockCursor(wx.CURSOR_ARROW))
    self.AllowDrag = False
    self.DrawMapWindow()
  # END of MapWindowLClickUp

  def OnFileSaveAs(self, event=None):
    if (self.MapStruct.geomorph):
      folder = gv.geomorphs_directory
      if (self.selectlist != []):
        self.selectlist = []
        self.DrawMapWindow()
    else:
      folder = gv.maps_directory
    dlg = wx.FileDialog(self.frame, message="Save file as...", defaultDir=folder, defaultFile="", wildcard=files_wildcard, style=wx.SAVE)
    if (dlg.ShowModal() == wx.ID_OK):
      if (gv.ChangeDefaultFolder):
        gv.maps_directory = dlg.GetDirectory()
      if (dlg.GetFilterIndex() == 0):  #save map file format
        self.MapStruct.geomorph = False
        if (sys.platform == 'win32'):
          self.MapStruct.filename = dlg.GetPath()
        else:
          self.MapStruct.filename = dlg.GetPath() + ".map"

      else: #save geomorph file format
        if (sys.platform == 'win32'):
          self.MapStruct.filename = dlg.GetPath()
        else:
          self.MapStruct.filename = dlg.GetPath() + ".pgf"
        pgf_dlg = GeomorphSaveDialog(dlg, self.MapBuffer)
        result = pgf_dlg.ShowModal()
        if (result):
          self.MapStruct.geomorphData.geomorphBottom = pgf_dlg.geomorphBottom
          self.MapStruct.geomorphData.geomorphLeft = pgf_dlg.geomorphLeft
          self.MapStruct.geomorphData.geomorphRight = pgf_dlg.geomorphRight
          self.MapStruct.geomorphData.geomorphTop = pgf_dlg.geomorphTop
          self.MapStruct.geomorph = True
          self.MapStruct.geomorphData.preview = self.MapStruct.filename + ".bmp"
          pgf_dlg.BitmapDisplay.SaveFile(self.MapStruct.geomorphData.preview, wx.BITMAP_TYPE_BMP)
        else: #cancelled off of the geomorph dialog
          return
      self.SaveMapFile(self.MapStruct.filename)
      self.frame.SetLabel("PyMapper "+VERSION+": " + self.MapStruct.filename)
      self.frame.menubar.Enable(PyMapperDialogs.mFileSave, True)
    dlg.Destroy()
    return


  def CopyTile(self, oldtile):
    newtile = Tile()
    newtile.sideA = oldtile.sideA  #PIL image format.  Not changed after loading from disk
    newtile.sideB = oldtile.sideB #PIL image format.  Not changed after loading from disk
    newtile.MapPosition = copy.deepcopy(oldtile.MapPosition) #pixel location of the image on the MapPanel
    newtile.TilePosition = copy.deepcopy(oldtile.TilePosition) #pixel location of the image on the TilePanel
    newtile.actualXsize = oldtile.actualXsize #size of the tile in squares
    newtile.actualYsize = oldtile.actualYsize #size of the tile in squares
    newtile.TileRect = copy.deepcopy(oldtile.TileRect) #current rect being displayed on the TilePanel
    newtile.TileRectB = copy.deepcopy(oldtile.TileRectB)
    newtile.MapRect = copy.deepcopy(oldtile.MapRect) #current rect being displayed on the MapPanel
    newtile.hotspot = copy.deepcopy(oldtile.hotspot)
    newtile.ShowOnMapPanel = copy.deepcopy(oldtile.ShowOnMapPanel)
    newtile.ShowOnTilePanel = copy.deepcopy(oldtile.ShowOnTilePanel)
    newtile.PlacedOnTilePanel = copy.deepcopy(oldtile.PlacedOnTilePanel)
    newtile.shown = oldtile.shown #is it visible?
    newtile.text = copy.deepcopy(oldtile.text) #is this a text string/annotation
    newtile.filenameA = oldtile.filenameA
    newtile.filenameB = oldtile.filenameB
    newtile.tilenameA = oldtile.tilenameA
    newtile.tilenameB = oldtile.tilenameB
    newtile.rotation = oldtile.rotation #rotation of the mapdisplay tile
    newtile.showingBside = oldtile.showingBside 
    newtile.mapdisplay = oldtile.mapdisplay #wxImage bitmap for map display.  This is the current display on the map window.
    newtile.tiledisplay = oldtile.tiledisplay #wxImage image for tile display.  This is the current display on the tile window.
    newtile.tilesetName = oldtile.tilesetName
    newtile.tileID = oldtile.tileID
    newtile.tilesetID = oldtile.tilesetID
    newtile.tilesetName = oldtile.tilesetName
    newtile.copies = oldtile.copies #How many copies of this tile, ie, number of sets owned
    newtile.selected = oldtile.selected #Is this tile selected for use?
    newtile.count = oldtile.count
    newtile.key_index = oldtile.key_index
    newtile.RightEdgeA = oldtile.RightEdgeA
    newtile.RightEdgeB = oldtile.RightEdgeB
    newtile.LeftEdgeA = oldtile.LeftEdgeA
    newtile.LeftEdgeB = oldtile.LeftEdgeB
    newtile.BottomEdgeA = oldtile.BottomEdgeA
    newtile.BottomEdgeB = oldtile.BottomEdgeB
    newtile.TopEdgeA = oldtile.TopEdgeA
    newtile.TopEdgeB = oldtile.TopEdgeB
    newtile.page = oldtile.page
    return newtile

  def OnTilePanelMotion(self, event):
    if (gv.SelectMode == 'draw'):
      #tile window is inactive while drawing
      return
    #dragging off the TilePanel
    gv.AddTile = True
    gv.HoverPoint = self.TilePanel.ClientToScreen(event.GetPosition())
    xy = self.TilePanel.CalcUnscrolledPosition(event.GetPosition().x, event.GetPosition().y)
    gv.LastPoint = wx.Point(xy[0], xy[1])
    self.hovertimer.Stop()
    self.DisplayHoverInformation(False)
    self.MouseOnTilePanel = True
    if (gv.rtc_open == False):
      self.TilePanel.SetFocus()

  def OnMapPanelMotion(self, event):
    gv.HoverPoint = self.MapPanel.ClientToScreen(event.GetPosition())
    gv.LastPoint = event.GetPosition()
    self.hovertimer.Stop()
    self.DisplayHoverInformation(False)  #displays labels, monster dialog, etc.
    self.MouseOnTilePanel = False
    if (gv.rtc_open == False):
      self.MapPanel.SetFocus()

    if (self.PanWindow): # The mouse is moving, check if we have the middle button down
      self.HighlightTimer.Stop()
      gv.StartPan = event.GetPosition()
      delta = gv.StartPan - gv.EndPan
      gv.MapOffset = gv.MapOffset + delta
      if (gv.MapOffset.x<0):
        gv.MapOffset.x = 0
      if (gv.MapOffset.y<0):
        gv.MapOffset.y = 0
      self.MapPanel.Scroll(gv.MapOffset.x, gv.MapOffset.y)
      gv.EndPan = gv.StartPan

    if (not self.dragImage) and (self.selectlist == []) and (event.Dragging()) and (gv.SelectMode == 'tile'):
      if (event.LeftIsDown()): #no images, but mouse is dragging;  form a rubberband to select multiple tiles
        self.HighlightTimer.Stop()
        self.MapPanel.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))
        dc = wx.ClientDC(self.MapPanel)
        RBpen = wx.Pen(wx.BLACK)
        dc.SetPen(RBpen)
        dc.SetBrush(wx.TRANSPARENT_BRUSH)
        if (gv.RubberBandPrevious):
          #erase the previous box
          dc.SetLogicalFunction(wx.INVERT)
          width = gv.RubberBandPrevious.x - gv.RubberBandStart.x
          height = gv.RubberBandPrevious.y - gv.RubberBandStart.y
          dc.DrawRectangle(gv.RubberBandStart.x, gv.RubberBandStart.y,
                           width, height)
        if (gv.RubberBandStart):
          gv.RubberBandEnd = event.GetPosition()
          width = gv.RubberBandEnd.x - gv.RubberBandStart.x
          height = gv.RubberBandEnd.y - gv.RubberBandStart.y
          dc.DrawRectangle(gv.RubberBandStart.x, gv.RubberBandStart.y,
                           width, height)
          gv.RubberBandPrevious = gv.RubberBandEnd
    # Ignore mouse movement if we're not dragging a tile.

    if (self.StartDragPos):  #start dragging of the image, if tolerance is met
      distance = self.StartDragPos - self.MapPanel.CalcUnscrolledPosition(event.GetPosition())
      delta = abs(distance[0] + distance[1])
      if (delta < 3):  # arbitrary movement tolerance of 3 pixels
        return

    if ((event.ControlDown()) or (gv.SelectMode == 'icon')) and (self.AllowDrag):  #moving text or room icon
      self.HighlightTimer.Stop()
      if (not self.TextInMotion):
        for room in gv.RoomList:
          if (room.selected):
            mouse_pos = self.MapPanel.CalcUnscrolledPosition(event.GetPosition())
            self.MapPanel.Update()
            Xoffset = (mouse_pos.x - room.MapRect.x)
            Yoffset = (mouse_pos.y - room.MapRect.y)
            hotspot = wx.Point(0, 0)
            self.dragImage.BeginDrag(hotspot, self.MapPanel, False) #set to true for full screen dragging
            self.dragImage.Move(event.GetPosition())
            self.dragImage.Show()
            self.TextInMotion = True
            break
        if (self.textlist == []):
          return
        if (not self.TextInMotion): #did not find an icon, so check text annotations
          for text in self.textlist:
            if (text.selected):
              mouse_pos = self.MapPanel.CalcUnscrolledPosition(event.GetPosition())
              self.MapPanel.Update()
              rect = wx.Rect(int(text.x*gv.MapZoomFactor), 
                             int(text.y*gv.MapZoomFactor),
                             int(text.extent.width*gv.MapZoomFactor),
                             int(text.extent.height*gv.MapZoomFactor))
              Xoffset = (mouse_pos.x - rect.x)
              Yoffset = (mouse_pos.y - rect.y)
              hotspot = wx.Point(0, 0)
              self.dragImage.BeginDrag(hotspot, self.MapPanel, False) #set to true for full screen dragging
              self.dragImage.Move(event.GetPosition())
              self.dragImage.Show()
              self.TextInMotion = True
              break
      elif (self.TextInMotion):  #found a text or icon in previous call to OnMapPanelMotion
        self.dragImage.Move(event.GetPosition())
    elif ((gv.SelectMode == 'draw') or (gv.SelectMode == 'fog')) and (gv.DrawingObject):
      self.HighlightTimer.Stop()
      if (gv.DrawingObject.tool == 'Line'):
        dc = wx.ClientDC(self.MapPanel)
        dc.SetPen(gv.DrawingObject.pen)
        dc.SetBrush(wx.TRANSPARENT_BRUSH)
        if (gv.DrawingToolPrevious):
          #erase the previous line
          dc.SetLogicalFunction(wx.INVERT)
          point1 = self.MapPanel.CalcScrolledPosition(gv.DrawingToolStartPoint)
          point2 = self.MapPanel.CalcScrolledPosition(gv.DrawingToolPrevious)
          dc.DrawLine(point1.x, point1.y, point2.x, point2.y)
        if (gv.DrawingToolStartPoint):
          gv.DrawingToolPrevious = self.MapPanel.CalcUnscrolledPosition(event.GetPosition())
          point1 = self.MapPanel.CalcScrolledPosition(gv.DrawingToolStartPoint)
          point2 = self.MapPanel.CalcScrolledPosition(gv.DrawingToolPrevious)
          dc.DrawLine(point1.x, point1.y, point2.x, point2.y)
      elif (gv.DrawingObject.tool == 'Freehand'):
        dc = wx.ClientDC(self.MapPanel)
        dc.SetPen(gv.DrawingObject.pen)
        dc.SetBrush(wx.TRANSPARENT_BRUSH)
        dc.SetLogicalFunction(wx.INVERT)
        point = self.MapPanel.CalcUnscrolledPosition(event.GetPosition())
        encode_point = self.EncodeDrawingPoint(point, gv.MapZoomFactor)
        gv.DrawingObject.line.append(encode_point)
        tempPoints = []
        for point in gv.DrawingObject.line:
          decode_point = self.DecodeDrawingPoint(point, gv.MapZoomFactor, 'INT')
          point = self.MapPanel.CalcScrolledPosition(decode_point)
          tempPoints.append(point)
        dc.DrawLines(tempPoints)
      elif (gv.DrawingObject.tool == 'Multiline'):
        if (gv.DrawingObject == None):
          return
        dc = wx.ClientDC(self.MapPanel)
        dc.SetPen(gv.DrawingObject.pen)
        dc.SetBrush(wx.TRANSPARENT_BRUSH)
        dc.SetLogicalFunction(wx.COPY)
        DrawIntermediate = False
        if (gv.DrawingObject.handle_index != None) and (gv.DrawingToolPrevious == None):
          if (gv.DrawingObject.handle_index == 0):
            gv.DrawingToolPrevious = self.DecodeDrawingPoint(gv.DrawingObject.line[0], gv.MapZoomFactor, 'INT')
            gv.DrawingToolStartPoint = self.DecodeDrawingPoint(gv.DrawingObject.line[1], gv.MapZoomFactor, 'INT')
            gv.DrawIntermediate = False
          elif (gv.DrawingObject.handle_index == (len(gv.DrawingObject.handles)-1)):
            gv.DrawingToolPrevious = self.DecodeDrawingPoint(gv.DrawingObject.line[(len(gv.DrawingObject.handles)-1)], gv.MapZoomFactor, 'INT')
            gv.DrawingToolStartPoint = self.DecodeDrawingPoint(gv.DrawingObject.line[(len(gv.DrawingObject.handles)-2)], gv.MapZoomFactor, 'INT')
            gv.DrawIntermediate = False
          else:  #intermediate point
            gv.DrawingToolPrevious = self.DecodeDrawingPoint(gv.DrawingObject.line[gv.DrawingObject.handle_index], gv.MapZoomFactor, 'INT')
            gv.DrawingToolStartPoint = self.DecodeDrawingPoint(gv.DrawingObject.line[(len(gv.DrawingObject.handles)-2)], gv.MapZoomFactor, 'INT')
            gv.DrawIntermediate = True
          gv.DrawingNextStep = 'modify'
        if (gv.DrawingToolPrevious):
          if (gv.DrawIntermediate) and (gv.DrawingObject.handle_index):
            #erase the previous line
            dc.SetLogicalFunction(wx.INVERT)
            point1 = self.MapPanel.CalcScrolledPosition(self.DecodeDrawingPoint(gv.DrawingObject.line[gv.DrawingObject.handle_index-1], gv.MapZoomFactor, 'INT'))
            point2 = self.MapPanel.CalcScrolledPosition(gv.DrawingToolPrevious)
            point3 = self.MapPanel.CalcScrolledPosition(self.DecodeDrawingPoint(gv.DrawingObject.line[gv.DrawingObject.handle_index+1], gv.MapZoomFactor, 'INT'))
            dc.DrawLine(point1.x, point1.y, point2.x, point2.y)
            dc.DrawLine(point3.x, point3.y, point2.x, point2.y)
          else:
            #erase the previous line
            dc.SetLogicalFunction(wx.INVERT)
            point1 = self.MapPanel.CalcScrolledPosition(gv.DrawingToolStartPoint)
            point2 = self.MapPanel.CalcScrolledPosition(gv.DrawingToolPrevious)
            dc.DrawLine(point1.x, point1.y, point2.x, point2.y)
        if (gv.DrawingToolStartPoint):
          if (gv.DrawIntermediate) and (gv.DrawingObject.handle_index):
            gv.DrawingToolPrevious = self.MapPanel.CalcUnscrolledPosition(event.GetPosition())
            point1 = self.MapPanel.CalcScrolledPosition(self.DecodeDrawingPoint(gv.DrawingObject.line[gv.DrawingObject.handle_index-1], gv.MapZoomFactor, 'INT'))
            point2 = self.MapPanel.CalcScrolledPosition(gv.DrawingToolPrevious)
            point3 = self.MapPanel.CalcScrolledPosition(self.DecodeDrawingPoint(gv.DrawingObject.line[gv.DrawingObject.handle_index+1], gv.MapZoomFactor, 'INT'))
            dc.DrawLine(point1.x, point1.y, point2.x, point2.y)
            dc.DrawLine(point3.x, point3.y, point2.x, point2.y)
          else:
            gv.DrawingToolPrevious = self.MapPanel.CalcUnscrolledPosition(event.GetPosition())
            point1 = self.MapPanel.CalcScrolledPosition(gv.DrawingToolStartPoint)
            point2 = self.MapPanel.CalcScrolledPosition(gv.DrawingToolPrevious)
            dc.DrawLine(point1.x, point1.y, point2.x, point2.y)

          ScaledPoints = []
          for point in gv.DrawingObject.line:
            scale_point = self.DecodeDrawingPoint(point, gv.MapZoomFactor)
            ScaledPoints.append(scale_point)
          gc = self.MapPanelGC
          path = gc.CreatePath()
          gc.SetPen(gv.DrawingObject.pen)
          gc.SetBrush(gv.DrawingObject.brush)
          path.MoveToPoint(ScaledPoints[0])
          ScaledPoints.pop(0)
          for point in ScaledPoints:
            path.AddLineToPoint(point)
            gc.StrokePath(path)
          if (gv.DrawHandles):
            self.DrawHandles(gv.DrawingObject, gv.MapZoomFactor, gc)
      elif (gv.DrawingObject.tool == 'OutlineRect') or (gv.DrawingObject.tool == 'FillRect') or (gv.DrawingObject.tool == 'Image'):
        dc = wx.ClientDC(self.MapPanel)
        dc.SetPen(gv.DrawingObject.pen)
        if (gv.DrawingObject.tool == 'OutlineRect') or (gv.DrawingObject.tool == 'Image'):
          dc.SetBrush(wx.TRANSPARENT_BRUSH)
        else:
          dc.SetBrush(gv.DrawingObject.brush)
        if (gv.DrawingObject.handle_index != None) and (gv.DrawingToolPrevious == None):
          if (gv.DrawingObject.handle_index == 0): #index 0 is at top left
            rect = self.DecodeDrawingRect(gv.DrawingObject.rect,gv.MapZoomFactor, 'RECT')
            gv.DrawingToolPrevious = wx.Point(rect.x, rect.y)
            gv.DrawingToolStartPoint = wx.Point(rect.x+rect.width, rect.y+rect.height)
          elif (gv.DrawingObject.handle_index == 1): #top right corner
            rect = self.DecodeDrawingRect(gv.DrawingObject.rect,gv.MapZoomFactor, 'RECT')
            gv.DrawingToolPrevious = wx.Point(rect.x+rect.width, rect.y)
            gv.DrawingToolStartPoint = wx.Point(rect.x, rect.y+rect.height)
          elif (gv.DrawingObject.handle_index == 2): #bottom right point
            rect = self.DecodeDrawingRect(gv.DrawingObject.rect,gv.MapZoomFactor, 'RECT')
            gv.DrawingToolPrevious = wx.Point(rect.x+rect.width, rect.y+rect.height)
            gv.DrawingToolStartPoint = wx.Point(rect.x, rect.y)
          elif (gv.DrawingObject.handle_index == 3): #bottom left
            rect = self.DecodeDrawingRect(gv.DrawingObject.rect,gv.MapZoomFactor, 'RECT')
            gv.DrawingToolPrevious = wx.Point(rect.x, rect.y+rect.height)
            gv.DrawingToolStartPoint = wx.Point(rect.x+rect.width, rect.y)
          elif (gv.DrawingObject.handle_index == 4): #center for moving
            rect = self.DecodeDrawingRect(gv.DrawingObject.rect,gv.MapZoomFactor, 'RECT')
            gv.DrawingToolPrevious = wx.Point(rect.x+(rect.width/2), rect.y+(rect.height/2))
            gv.DrawingToolStartPoint = wx.Point(rect.x+(rect.width/2), rect.y+(rect.height/2))
          gv.DrawingNextStep = 'modify'
        if (gv.DrawingToolPrevious):
          dc.SetLogicalFunction(wx.INVERT) #erase the previous rect
          if (gv.DrawingObject.handle_index == 4):
            #move the rect
            offset = gv.DrawingToolStartPoint - gv.DrawingToolPrevious
            new_rect = self.DecodeDrawingRect(gv.DrawingObject.rect, gv.MapZoomFactor)
            new_rect.x -= offset.x
            new_rect.y -= offset.y
          else:
            #move a corner
            point1 = self.MapPanel.CalcScrolledPosition(gv.DrawingToolStartPoint)
            point2 = self.MapPanel.CalcScrolledPosition(gv.DrawingToolPrevious)
            new_rect = wx.RectPP(point1, point2)
          dc.DrawRectangle(new_rect.x, new_rect.y, new_rect.width, new_rect.height)
        if (gv.DrawingToolStartPoint):
          if (gv.DrawingObject.handle_index == 4):
            #move the rect
            gv.DrawingToolPrevious = self.MapPanel.CalcUnscrolledPosition(event.GetPosition())
            offset = gv.DrawingToolStartPoint - gv.DrawingToolPrevious
            new_rect = self.DecodeDrawingRect(gv.DrawingObject.rect, gv.MapZoomFactor)
            new_rect.x -= offset.x
            new_rect.y -= offset.y
          else:
            #move a corner
            gv.DrawingToolPrevious = self.MapPanel.CalcUnscrolledPosition(event.GetPosition())
            point1 = self.MapPanel.CalcScrolledPosition(gv.DrawingToolStartPoint)
            point2 = self.MapPanel.CalcScrolledPosition(gv.DrawingToolPrevious)
            new_rect = wx.RectPP(point1, point2)
          dc.DrawRectangle(new_rect.x, new_rect.y, new_rect.width, new_rect.height)
      elif (gv.DrawingObject.tool == 'OutlineCircle') or (gv.DrawingObject.tool == 'FillCircle') or (gv.DrawingObject.tool == 'Point'):
        dc = wx.ClientDC(self.MapPanel)
        dc.SetPen(gv.DrawingObject.pen)
        if (gv.DrawingObject.tool == 'OutlineCircle'):
          dc.SetBrush(wx.TRANSPARENT_BRUSH)
        else:
          dc.SetBrush(gv.DrawingObject.brush)
        if (gv.DrawingObject.handle_index != None) and (gv.DrawingToolPrevious == None):
          if (gv.DrawingObject.handle_index == 0):
            #move the circle at the centerpoint
            gv.DrawingToolPrevious = self.DecodeDrawingPoint(gv.DrawingObject.circle[0], gv.MapZoomFactor, 'INT')
            gv.DrawingToolStartPoint = self.DecodeDrawingPoint(gv.DrawingObject.circle[0], gv.MapZoomFactor, 'INT')
          elif (gv.DrawingObject.handle_index == 1): #far right point
            point = self.DecodeDrawingPoint(gv.DrawingObject.circle[0], gv.MapZoomFactor, 'INT')
            radius = gv.DrawingObject.circle[1]*gv.MapZoomFactor
            point.x += radius
            gv.DrawingToolPrevious = point
            gv.DrawingToolStartPoint = self.DecodeDrawingPoint(gv.DrawingObject.circle[0], gv.MapZoomFactor, 'INT')
          elif (gv.DrawingObject.handle_index == 2): #far left point
            point = self.DecodeDrawingPoint(gv.DrawingObject.circle[0], gv.MapZoomFactor, 'INT')
            radius = gv.DrawingObject.circle[1]*gv.MapZoomFactor
            point.x -= radius
            gv.DrawingToolPrevious = point
            gv.DrawingToolStartPoint = self.DecodeDrawingPoint(gv.DrawingObject.circle[0], gv.MapZoomFactor, 'INT')
          elif (gv.DrawingObject.handle_index == 3): #top point
            point = self.DecodeDrawingPoint(gv.DrawingObject.circle[0], gv.MapZoomFactor, 'INT')
            radius = gv.DrawingObject.circle[1]*gv.MapZoomFactor
            point.y -= radius
            gv.DrawingToolPrevious = point
            gv.DrawingToolStartPoint = self.DecodeDrawingPoint(gv.DrawingObject.circle[0], gv.MapZoomFactor, 'INT')
          elif (gv.DrawingObject.handle_index == 4): #bottom point
            point = self.DecodeDrawingPoint(gv.DrawingObject.circle[0], gv.MapZoomFactor, 'INT')
            radius = gv.DrawingObject.circle[1]*gv.MapZoomFactor
            point.y += radius
            gv.DrawingToolPrevious = point
            gv.DrawingToolStartPoint = self.DecodeDrawingPoint(gv.DrawingObject.circle[0], gv.MapZoomFactor, 'INT')
          gv.DrawingNextStep = 'modify'
        if (gv.DrawingToolPrevious):
          dc.SetLogicalFunction(wx.INVERT) #erase the previous circle
          if (gv.DrawingObject.handle_index == 0):
            radius = gv.DrawingObject.circle[1]*gv.MapZoomFactor
            point = self.MapPanel.CalcScrolledPosition(gv.DrawingToolPrevious)
            dc.DrawCircle(point.x, point.y, radius)
          else:
            point1 = self.MapPanel.CalcScrolledPosition(gv.DrawingToolStartPoint)
            point2 = self.MapPanel.CalcScrolledPosition(gv.DrawingToolPrevious)
            distance_point = point1 - point2
            radius = math.sqrt(math.pow(distance_point.x, 2) + math.pow(distance_point.y,2))
            dc.DrawCircle(point1.x, point1.y, radius)
        if (gv.DrawingToolStartPoint):
          if (gv.DrawingObject.handle_index == 0):
            gv.DrawingToolPrevious = self.MapPanel.CalcUnscrolledPosition(event.GetPosition())
            radius = gv.DrawingObject.circle[1]*gv.MapZoomFactor
            point = self.MapPanel.CalcScrolledPosition(gv.DrawingToolPrevious)
            dc.DrawCircle(point.x, point.y, radius)
          else:
            gv.DrawingToolPrevious = self.MapPanel.CalcUnscrolledPosition(event.GetPosition())
            point1 = self.MapPanel.CalcScrolledPosition(gv.DrawingToolStartPoint)
            point2 = self.MapPanel.CalcScrolledPosition(gv.DrawingToolPrevious)
            distance_point = point1 - point2
            radius = math.sqrt(math.pow(distance_point.x, 2) + math.pow(distance_point.y,2))
            dc.DrawCircle(point1.x, point1.y, radius)
    elif (self.AllowDrag and event.Dragging()): #moving tiles
      self.HighlightTimer.Stop()
      if (not self.TileInMotion): # no tile moving yet, get the tile out of the tilelist
        tile = self.FindSelectedTileInLists()
        if (not tile):
          return
        mouse_pos = self.MapPanel.CalcUnscrolledPosition(event.GetPosition())
        startpoint = event.GetPosition() # this is to handle the offset created by many tiles and a fast moving mouse
        self.MapPanel.Update()
        if (gv.AddTile):
          #tile selected from the tilepanel, set hotspot to center of tile
          xdist = int((tile.actualXsize/2.0)*gv.MapZoomFactor)
          ydist = int((tile.actualYsize/2.0)*gv.MapZoomFactor)
          tile.hotspot = wx.Point(xdist, ydist)  #0,0
        else:
          if (event.m_shiftDown):
            Xrect = self.CalculateMapExtents(self.selectlist)
            rect = wx.Rect2D(Xrect.x*gv.MapZoomFactor, Xrect.y*gv.MapZoomFactor,
                             Xrect.width*gv.MapZoomFactor, Xrect.height*gv.MapZoomFactor)
            if ((mouse_pos.x-rect.x) < 0):
              Xoffset = 0
            elif ((mouse_pos.x-rect.x) > rect.width):
              Xoffset = rect.width
            else:
              Xoffset = (mouse_pos.x - rect.x)
            if ((mouse_pos.y-rect.y) < 0):
              Yoffset = 0
            elif ((mouse_pos.y-rect.y) > rect.height):
              Yoffset = rect.height
            else:
              Yoffset = (mouse_pos.y - rect.y)
            self.selectlist[0].hotspot = wx.Point(Xoffset, Yoffset)
          else:
            Xrect = self.selectlist[0].MapRect
            rect = wx.Rect2D((Xrect.x)*gv.MapZoomFactor, (Xrect.y)*gv.MapZoomFactor,
                             (Xrect.width)*gv.MapZoomFactor, (Xrect.height)*gv.MapZoomFactor)
            if ((mouse_pos.x-rect.x) < 0):
              Xoffset = 0
            elif ((mouse_pos.x-rect.x) > rect.width):
              Xoffset = rect.width
            else:
              Xoffset = (mouse_pos.x - rect.x)
            if ((mouse_pos.y-rect.y) < 0):
              Yoffset = 0
            elif ((mouse_pos.y-rect.y) > rect.height):
              Yoffset = rect.height
            else:
              Yoffset = (mouse_pos.y - rect.y)
            self.selectlist[0].hotspot = wx.Point(Xoffset, Yoffset)
        self.dragImage.BeginDrag(tile.hotspot, self.MapPanel, False) #set to true for full screen dragging
        self.dragImage.Move(startpoint)  #was event.GetPosition()
        self.dragImage.Show()
        self.TileInMotion = True
      elif (self.TileInMotion):
        self.dragImage.Move(event.GetPosition())
    else:
      if (not self.HighlightTimer.IsRunning()):
        self.HighlightTimer.Start(1)
  # End of onMapPanelMotion

  def OnMapPanelLeave(self, event):
    if (self.PanWindow):
      self.PanWindow = False
    return


  def OnLayerSelect(self, event):
    logging.info("OnLayerSelect:  Select layer")
    return

  def ReadMapFile(self, filename, ImportFile=False):
    """Changes made to the tag structure in this function must be made in ReadGeomorphFile() as well."""
    tilesets_loaded = False
    version = 2.1 #This is the original format, default to this version unless otherwise set.
    try:
      mapfile = open(filename, 'r')
    except IOError:
      '''Log error of mapfile read'''
      logging.error("PymapperAppMain::ReadMapFile:  Could not open %s",filename)
      return False
    else:
      line = mapfile.readline()
      line.rstrip("\n\r")
      info = line.split()
      header = True
      while (header == True):
        if (info[0] == '#'):
          #reading comment lines
          line = mapfile.readline()
          info = line.split()
        elif (info[0] != '#'):
          header = False
      if info[0] != 'MAPFILE':
        logging.error("ReadMapFile:  No MAPFILE tag read, invalid mapfile")
        #Not a map file, so exit
        mapfile.close()
        return False
      else:
        read_file = True
        while (read_file == True):
          line = mapfile.readline()
          line.rstrip("\n\r")
          info = line.split()
          newtile = Tile()
          if (info[0] == 'TILESET'):
            if (version == 2.1):
              result = self.ReadTilesetFile(info[1], False)
              if (result == False):
                logging.critical("Error in ReadMapFile: Could not open tileset file %s", str(info[1]))
            elif (version == 2.2):
              set_loaded = self.CheckDuplicateTileset(info[1])
              result = False
              if not(set_loaded):
                TilesetPath = os.path.join(gv.tiles_directory,str(info[1]))
                os.chdir(TilesetPath)
                filelist = glob.glob('*.set')
                if (filelist == []):
                  logging.warning("No tileset file found in %s",TilesetPath)
                  result = False
                else:
                  filename = os.path.join(str(info[1]),str(filelist[0]))
                  result = self.ReadTilesetFile(filename, True)
                if (result == False):
                  text = "Error in ReadMapFile: Could not open tileset file ", str(info[1])
                  wx.MessageBox(message=text, caption="Error", style=wx.ICON_EXCLAMATION)
            else:
              #reading current version, ie 2.4
              #check for spaces in filenames
              if (len(info) > 3):
                while (len(info) > 3):
                  length = len(info)
                  info[1] = (info[1]) +" " + (info[2])
                  info.remove(info[2])
              set_loaded = self.CheckDuplicateTileset(info[2])
              result = False
              if not(set_loaded):
                #try to load based on tileset ID
                TilesetPath = os.path.join(gv.tiles_directory,str(info[2]))
                try:
                  os.chdir(TilesetPath)
                except OSError:
                  text = "Error in ReadMapFile: Could not change to "+TilesetPath+"\n"
                  wx.MessageBox(message=text, caption="Error", style=wx.ICON_EXCLAMATION)
                  return False
                filelist = glob.glob('*.set')
                if (filelist == []):
                  result = self.ReadTilesetFile(info[1], False)
                else:
                  filename = os.path.join(str(info[2]),str(filelist[0]))
                  result = self.ReadTilesetFile(filename, True)
                if (result == False):
                  text = "Error in ReadMapFile: Could not open tileset file ", str(info[1])
                  wx.MessageBox(message=text, caption="Error", style=wx.ICON_EXCLAMATION)
            if (result == True):
              tilesets_loaded = True
          elif info[0] == 'VIEWGRID':
            if (info[1] == 'ON'):
              gv.DisplayGrid = True
            else:
              gv.DisplayGrid = False
          elif (info[0] == 'LOAD_DUNGEON_RESOURCES'):  #deprecated tag; removed in v9.4
            if (not gv.d20_SRD_data_available):  #ignore if resources already loaded
              self.OnDungeon_Load_d20_Resources()
            if (not gv.DnD_5E_data_available):
              self.OnDungeon_Load_DnD5_Resources()
          elif (info[0] == 'LOAD_D20_RESOURCES'): #New in v8.6
            if (not gv.d20_SRD_data_available):  #ignore if resources already loaded
              self.OnDungeon_Load_d20_Resources()
          elif (info[0] == 'LOAD_DND5_RESOURCES'): #new in v9.4
            if (not gv.DnD_5E_data_available):
              self.OnDungeon_Load_DnD5_Resources()
          elif (info[0] == 'GEOMORPH_RIGHT'):
            self.MapStruct.geomorph = True
            self.MapStruct.geomorphData.geomorphRight = int(info[1])
          elif (info[0] == 'GEOMORPH_LEFT'):
            self.MapStruct.geomorph = True
            self.MapStruct.geomorphData.geomorphLeft = int(info[1])
          elif (info[0] == 'GEOMORPH_TOP'):
            self.MapStruct.geomorph = True
            self.MapStruct.geomorphData.geomorphTop = int(info[1])
          elif (info[0] == 'GEOMORPH_BOTTOM'):
            self.MapStruct.geomorph = True
            self.MapStruct.geomorphData.geomorphBottom = int(info[1])
          elif (info[0] == 'MAP_PAGES'):
            loading_pages = True
            importFilePageNames = []
            while (loading_pages):
              line = mapfile.readline()
              line.rstrip("\n\r")
              info = line.split()
              if (info[0] == 'START_PAGE'):
                page = Page_Record()
              elif (info[0] == 'PAGE_BACKGROUND_FILENAME'):
                page.background_filename = mapfile.readline().rstrip("\n\r")
                page.background_filepath = mapfile.readline().rstrip("\n\r")
                if (page.background_filename == 'None'):
                  page.background_filename = None
                  page.background_filepath = None
                else:
                  imagepath = os.path.join(page.background_filepath,page.background_filename)
                  validPath = os.access(imagepath, os.F_OK)
                  if (not validPath):
                    imagepath = os.path.join(os.getcwd(),page.background_filename)
                  page.background = wx.Image(imagepath, wx.BITMAP_TYPE_ANY)
                  page.background_filepath = os.getcwd()
                  if (not page.background.IsOk()):
                    imagepath = os.path.join(os.getcwd(),page.background_filename)
                    page.background = wx.Image(imagepath, wx.BITMAP_TYPE_ANY)
                    page.background_filepath = os.getcwd()
                    if (not page.background.IsOk()):
                      logging.debug("Could not locate background image %s", imagepath)
                      caption = "I cannot locate "+imagepath
                      dlg = wx.FileDialog(self.frame, caption , wildcard=images_wildcard, style=wx.OPEN)
                      if (dlg.ShowModal() == wx.ID_OK):
                        page.background_filename = dlg.GetFilename()
                        page.background_filepath = dlg.GetDirectory()
                        dlg.Destroy()
                        imagepath = os.path.join(page.background_filepath,page.background_filename)
                        page.background = wx.Image(imagepath, wx.BITMAP_TYPE_ANY)
                        logging.debug("Loaded background image %s", imagepath)
                      else:
                        page.background = None
                        page.background_filename = None
                        page.background = None
                    else:
                      logging.debug("Loaded background image %s", imagepath)
              elif (info[0] == 'PAGE_BACKGROUND_DISPLAY_MODE'):
                page.bg_displaymode = info[1]
              elif (info[0] == 'PAGE_BACKGROUND_DIMENSION'):
                page.bg_x_dimension = float(info[1])
                page.bg_y_dimension = float(info[2])
              elif (info[0] == 'PAGE_ZOOM'):
                page.ZoomFactor = int(info[1])
              elif (info[0] == 'PAGE_XSCROLL'):
                page.Xscroll = int(info[1])
              elif (info[0] == 'PAGE_YSCROLL'):
                page.Yscroll = int(info[1])
              elif (info[0] == 'PAGE_NAME'):
                nameline = mapfile.readline().rstrip("\n\r")
                if (ImportFile):  #check to see if there is a duplicate name in the page list
                  foundDuplicate = False
                  for pageitem in gv.MapPageList:
                    if pageitem.PageName == nameline:
                      pageNameRecord = Filenames_Record()
                      pageNameRecord.importName = nameline
                      nameline += "_duplicatedPageName"
                      pageNameRecord.importRenamed = nameline
                      importFilePageNames.append(pageNameRecord)
                      foundDuplicate = True
                  if (not foundDuplicate):  #adding these non-duplicate records help to translate when PageIndex is still in use
                    pageNameRecord = Filenames_Record()
                    pageNameRecord.importName = nameline
                    pageNameRecord.importRenamed = nameline
                    importFilePageNames.append(pageNameRecord)
                page.PageName = nameline
              elif (info[0] == 'END_PAGE'):
                #check to see if a page with the same name exists
                existing_found = False
                for existing_page in gv.MapPageList:
                  if (page.PageName == existing_page.PageName):
                    #set values read from mapfile to this page
                    existing_page.ZoomFactor = page.ZoomFactor
                    existing_page.Xscroll = page.Xscroll
                    existing_page.Yscroll = page.Yscroll
                    existing_page.background = page.background
                    existing_page.background_filename = page.background_filename
                    existing_page.background_filepath = page.background_filepath
                    existing_page.bg_displaymode = page.bg_displaymode
                    existing_page.bg_x_dimension = page.bg_x_dimension
                    existing_page.bg_y_dimension = page.bg_y_dimension
                    existing_found = True
                    break
                if (not existing_found):
                  page.PageID = len(gv.MapPageList)
                  self.RMapbookAddPage(name=page.PageName, new_page=page)
              elif (info[0] == 'END_MAP_PAGES'):
                loading_pages = False
          elif (info[0] == 'MAP_LAYERS'):
            gv.LayerList = []
            readtext = True
            while (readtext == True):
              line = mapfile.readline()
              line = line.rstrip("\n\r")
              info = line.split()
              if (info[0] == "END_LAYERS"):
                readtext = False
              else:
                layer = gv.LayerItem()
                layer.name = info[0]
                if (info[1] == 'True'):
                  layer.display = True
                else:
                  layer.display = False
                if (version >= 2.6):  #additional information available
                  layer.index = int(info[2])
                  layer.opacity = float(info[3])
                else:  #default values for older mapfiles
                  layer.index = 0
                  layer.opacity = 1.0
                gv.LayerList.append(layer)
            self.frame.UpdateLayerSelector()
          elif (info[0] == 'VERSION'):
            version = float(info[1])
          elif (info[0] == 'ROOM_ICONS'):
            readtext = True
            while (readtext == True):
              line = mapfile.readline()
              line = line.rstrip("\n\r")
              info = line.split()
              if (info[0] == 'ROOM_INFO_START'):
                room = RoomInfo()
                room.Icon = self.RoomIcon
              elif (info[0] == 'ROOM_DESCRIPTION'):
                if (version >= 2.4):
                  line = mapfile.readline()
                  line = line.rstrip("\n\r")
                  room.Description = line
                else:
                  room.Description = info[1]
              elif (info[0] == 'ROOM_LAYER'):
                #Layer tracking changed in v9.5 from name of layer to an index number
                if (version < 2.6):
                  room.Layer = 0  #default all to layer 0
                else:
                  room.Layer = int(info[1])
              elif (info[0] == 'ROOM_HIGHLIGHT_COLOR'):
                red = int(info[1])
                blue = int(info[2])
                green = int(info[3])
                alpha = int(info[4])
                room.highlightColor = wx.Colour(red, blue, green, alpha)
              elif (info[0] == 'ROOM_PAGE'):
                page = mapfile.readline().rstrip('\n\r')
                if (ImportFile): #check if the import file had duplicated page names
                  for item in importFilePageNames:
                    if (item.importName == page):
                      page = item.importRenamed
                      break
                room.page = page
              elif (info[0] == 'ROOM_ICON'):
                if (info[1] == 'Trap'):
                  room.Icon = self.TrapIcon
                  room.IconType = 'Trap'
                elif (info[1] == 'Monster'):
                  room.Icon = self.MonsterIcon
                  room.IconType = 'Monster'
                elif (info[1] == 'NPC'):
                  room.Icon = self.NPC_Icon
                  room.IconType = 'NPC'
                elif (info[1] == 'Treasure'):
                  room.Icon = self.TreasureIcon
                  room.IconType = 'Treasure'
                else:
                  room.Icon = self.RoomIcon
                  room.IconType = 'Room'
              elif (info[0] == 'TRAP_UNIQUE_ID'):
                #v9.1 onward traps are not tracked by unique ID, but by unique name
                if (version >= 2.5):
                  line = mapfile.readline()
                  line = line.rstrip("\n\r")
                  trapName = line
                  for trap in gv.TrapList:
                    if (trapName == trap.desc):
                      room.trap = trap
                      break
                else:
                  pass  #this code was: room.trap = gv.TrapList[int(info[1])]
              elif (info[0] == 'MONSTER_5E_NPC_UNIQUE_ID'):
                #check if the SRD files have been read previously
                for npc in gv.NPC_5E:
                  if (int(info[1]) == npc.uniqueID):
                    room.monster = copy.deepcopy(npc)
                    room.monster.startHP = room.monster.HP
                    if (room.monster.filename):  #set up the wxImage
                      room.monster.image = wx.Image(os.path.join(gv.tokens_directory,room.monster.filename), wx.BITMAP_TYPE_ANY)
                      if (not room.monster.image.IsOk()):
                        logging.error("Could not read custom npc image %s from tokens folder", room.monster.filename)
                        room.monster.image = None
                    if (isinstance(room.monster.size, int)):
                      if ((room.monster.size == 0) or (room.monster.size == 1) or (room.monster.size == 2)):
                        room.IconSize = 1
                      elif (room.monster.size == 3):  # Large
                        room.IconSize = 2
                      elif (room.monster.size == 4):  # Huge
                        room.IconSize = 3
                      elif (room.monster.size == 5):  #Gargantuan
                        room.IconSize = 4
                    else:
                      room.IconSize = 1  #default to medium size
                    break
              elif (info[0] == 'MONSTER_5E_UNIQUE_ID'):
                #check if the SRD files have been read previously
                for monster in gv.Monsters5E:
                  if (int(info[1]) == monster.uniqueID):
                    room.monster = copy.deepcopy(monster)
                    room.monster.startHP = room.monster.HP
                    if (room.monster.filename):  #set up the wxImage
                      room.monster.image = wx.Image(os.path.join(gv.tokens_directory,room.monster.filename), wx.BITMAP_TYPE_ANY)
                      if (not room.monster.image.IsOk()):
                        logging.error("Could not read custom monster image %s from tokens folder", room.monster.filename)
                        room.monster.image = None
                    if (isinstance(room.monster.size, int)):
                      if ((room.monster.size == 0) or (room.monster.size == 1) or (room.monster.size == 2)):
                        room.IconSize = 1
                      elif (room.monster.size == 3): # Large
                        room.IconSize = 2
                      elif (room.monster.size == 4): # Huge
                        room.IconSize = 3
                      elif (room.monster.size == 5): # Gargantuan
                        room.IconSize = 4
                    else:
                      room.IconSize = 1  # default to Medium size
                      logging.error("Read 5E monster without size info: Monster ID %d", room.monster.uniqueID)
                    break
              elif (info[0] == 'MONSTER_UNIQUE_ID'):
                #check if the SRD files have been read previously
                for monster in gv.MonsterList:
                  if (int(info[1]) == monster.uniqueID):
                    room.monster = copy.deepcopy(monster)
                    room.monster.startHP = room.monster.HP
                    break
              elif (info[0] == 'MONSTER_HP'):
                if (room.monster):
                  room.monster.HP = int(info[1])
                else:
                  logging.error("Read MONSTER_HP tag without monster information")
              elif (info[0] == 'MONSTER_CUSTOM_NAME'):
                if (room.monster):
                  room.monster.customName = mapfile.readline().rstrip('\n\r')
                else:
                  logging.error("Read MONSTER_CUSTOM_NAME tag without monster information")
              elif (info[0] == 'MONSTER_CUSTOM_IMAGE'):
                room.monster.filename = mapfile.readline().rstrip('\n\r')
                room.monster.image = wx.Image(os.path.join(gv.tokens_directory,room.monster.filename), wx.BITMAP_TYPE_ANY)
                if (not room.monster.image.IsOk()):
                  logging.error("Could not find custom monster image %s in the tokens folder", room.monster.filename)
                  room.monster.image = None
              elif (info[0] == 'ROOM_POSITION'):
                room.x = float(info[1])
                room.y = float(info[2])
                room.placed = True
              elif (info[0] == 'ROOM_XML_FILE'):
                room.xml_file = mapfile.readline().rstrip('\n\r')
              elif (info[0] == 'ROOM_XML_PATH'):
                room.xml_path = mapfile.readline().rstrip('\n\r')
              elif (info[0] == 'ROOM_INFO_END'):
                gv.RoomList.append(room)
              elif (info[0] == 'ROOM_ICONS_END'):
                readtext = False
          elif (info[0] == 'ANNOTATIONS'):
            readtext = True
            text = Annotation()
            while (readtext == True):
              line = mapfile.readline()
              line = line.rstrip("\n\r")
              info = line.split()
              if (info[0] == 'TEXT'):
                text.x = float(info[1])
                text.y = float(info[2])
                info.pop(0)
                info.pop(0)
                info.pop(0)
                text.text = info[0]
                info.pop(0)
                while (len(info) > 0):
                  text.text += " "
                  text.text += info[0]
                  info.pop(0)
              elif(info[0] == 'FONT_PT_SIZE'):
                pt_size = int(info[1])
              elif(info[0] == 'ANNO_PAGE'):
                page = mapfile.readline().rstrip("\n\r")
                if (ImportFile): #check if the import file had duplicated page names
                  for item in importFilePageNames:
                    if (item.importName == page):
                      page = item.importRenamed
                      break
                text.page = page
              elif(info[0] == 'FONT_FAMILY'):
                family = int(info[1])
              elif(info[0] == 'FONT_STYLE'):
                style = int(info[1])
              elif(info[0] == 'FONT_WEIGHT'):
                weight = int(info[1])
              elif(info[0] == 'FONT_FACENAME'):
                info.pop(0)
                facename = info[0]
                info.pop(0)
                while (len(info) != 0):
                  facename += " "
                  facename += info[0]
                  info.pop(0)
              elif(info[0] == 'TEXT_BG'):
                text.bg = wx.Colour(int(info[1]), int(info[2]), int(info[3]))
              elif(info[0] == 'TEXT_FG'):
                text.fg = wx.Colour(int(info[1]), int(info[2]), int(info[3]))
              elif(info[0] == 'OPAQUE'):
                if (info[1] == 'ON'):
                  text.opaque = True
                elif (info[1] == 'OFF'):
                  text.opaque = False
              elif(info[0] == 'END_TEXT'):
                text.font = wx.Font(pt_size, family, style, weight,
                                    False, facename, wx.FONTENCODING_DEFAULT)
                self.textlist.append(text)
                text = Annotation()
              elif(info[0] == 'END_ANNOTATIONS'):
                readtext = False
                logging.debug("End reading of annotations from map file.  Initial create bitmaps step")
                for label in self.textlist:
                  label = self.CreateTextLabelBitmap(label, gv.MapZoomFactor)
          elif (info[0] == 'BACKGROUND'):
            #this tag was removed from use in v6.3.5;  Background information is now stored with the page information
            #this is here to provide some level of backward compatibility
            filename = info[1]
            if (filename == 'None') or (filename == 'NONE'):
              filename = None
            else:
              pageindex = self.nbMapNotebook.GetSelection()
              page = gv.MapPageList[pageindex]
              page.background = wx.Image(filename, wx.BITMAP_TYPE_ANY)
          elif (info[0] == 'BEGIN_DRAWING_ITEMS'):
            self.ReadDrawingItems(mapfile, importFilePageNames)
          elif (info[0] == 'SNAP_GRID'):
            if (info[1] == 'ON'):
              gv.SnapToGrid == True
            else:
              gv.SnapToGrid == False
          elif (info[0] == 'GRID_COLOR'):
            if (info[1] != 'NONE'):
              self.MapStruct.gridcolor = wx.Colour(int(info[1]), int(info[2]),int(info[3]), int(info[4]))
          elif (info[0] == 'MAP_ZOOM'):
            gv.MapZoomFactor = int(info[1])
          elif (info[0] == 'ROWS'):
            self.MapStruct.rows = int(info[1])
          elif (info[0] == 'COLUMNS'):
            self.MapStruct.columns = int(info[1])
          elif (info[0] == 'BEGIN_MAP_DEFINITION'):
            if (version < 2.5) and (self.nbMapNotebook.GetPageCount() == 0):
              #mapfile versions 2.4 and earlier may not have stored page information
              #create default map page for items
              page = Page_Record()
              page.ZoomFactor = gv.MapZoomFactor
              page.Xscroll = 0
              page.Yscroll = 0
              page.PageName = "Dungeon Map"
              page.PageID = len(gv.MapPageList)
              self.RMapbookAddPage(name=page.PageName, new_page=page)
            read_map = True
            while (read_map == True):
              line = mapfile.readline()
              info = line.split()
              if (info[0] == 'TILE'):
                newtile.tilesetID = info[1]
                newtile.tileID = int(info[2])
                for tile in self.tilelist:
                  if ((newtile.tilesetID == tile.tilesetID) and (newtile.tileID == tile.tileID)):
                    newtile.key_index = tile.key_index
                    newtile.tilesetName = tile.tilesetName
                    tile.num_used += 1
                    for tset in gv.tilesets:
                      if (tset.SetID == tile.tilesetID):
                        tset.used = True
                    if (tile.num_used >= tile.copies):
                      newtile.dimmed = True
                      tile.dimmed = True
                    break
                newtile.dimmed = True
              elif (info[0] == 'TILE_LAYER'):
                newtile.layer = int(info[1])
              elif (info[0] == 'TILE_PAGE'):
                page = mapfile.readline().rstrip('\n\r')
                if (ImportFile): #check if the import file had duplicated page names
                  for item in importFilePageNames:
                    if (item.importName == page):
                      page = item.importRenamed
                      break
                newtile.page = page
              elif (info[0] == 'POSITION'):
                if (self.MapStruct.geomorph):
                  newtile.MapPosition = wx.Point2D(float(info[1])+1, float(info[2])+1)
                else:
                  newtile.MapPosition = wx.Point2D(float(info[1]), float(info[2]))
              elif (info[0] == 'A_SIDE'):
                newtile.showingBside = False
              elif (info[0] == 'B_SIDE'):
                newtile.showingBside = True
              elif (info[0] == 'ROTATION'):
                newtile.rotation = float(info[1])
              elif (info[0] == 'END_TILE'):
                addtile = self.ioAssignMapTileValues(newtile)
                self.maplist.append(addtile)
                newtile = Tile()
              elif (info[0] == 'END_MAP_DEFINITION'):
                read_map = False
          elif (info[0] == 'END_MAP_FILE'):
            mapfile.close()
            #check for room icons without a page set
            for room in gv.RoomList:
              if (room.page == None):
                if (ImportFile):
                  pageindex = self.nbMapNotebook.GetSelection()
                  room.page = self.nbMapNotebook.GetPageText(pageindex)
                else:
                  room.page = self.nbMapNotebook.GetPageText(0)
            #check for annotations without a page set
            for text in self.textlist:
              if (text.page == None):
                if (ImportFile):
                  pageindex = self.nbMapNotebook.GetSelection()
                  text.page = self.nbMapNotebook.GetPageText(pageindex)
                else:
                  text.page = self.nbMapNotebook.GetPageText(0)
            #check for tiles without a page set 
            for tile in self.maplist:
              tile.GenerateMapDisplay(gv.MapZoomFactor)
              if (tile.page == None):
                if (ImportFile):
                  pageindex = self.nbMapNotebook.GetSelection()
                  tile.page = self.nbMapNotebook.GetPageText(pageindex)
                else:
                  tile.page = self.nbMapNotebook.GetPageText(0)
            if (tilesets_loaded):
              self.DrawTileWindow(True)
            else:
              self.DrawTileWindow(False)
            return True

  def ReadGeomorphFile(self, filename):
    """Changes made to the tag structure in this function must be made in ReadMapFile() as well."""
    tilesets_loaded = False
    Geomorph = Geomorph_Record()
    version = 2.1 #This is the original format, default to this version unless otherwise set.
    try:
      mapfile = open(filename, 'r')
    except IOError:
      '''Log error of mapfile read'''
      logging.error("ReadGeomorphFile:  Could not open %s", filename)
      return False
    else:
      line = mapfile.readline()
      line.rstrip("\n\r")
      info = line.split()
      header = True
      while (header == True):
        if (info[0] == '#'):
          #reading comment lines
          line = mapfile.readline()
          info = line.split()
        elif (info[0] != '#'):
          header = False

      if info[0] != 'MAPFILE':
        logging.error("ReadMapFile:  No MAPFILE tag read, invalid mapfile")
        '''Not a map file'''
        mapfile.close()
        return False
      else:
        read_file = True
        while (read_file == True):
          line = mapfile.readline()
          line.rstrip("\n\r")
          info = line.split()
          newtile = Tile()
          if (info[0] == 'TILESET'):
            if (version == 2.1):
              result = self.ReadTilesetFile(info[1], False)
              if (result == False):
                text = "Error in ReadGeomorphFile: Could not open tileset file ", str(info[1])
                wx.MessageBox(message=text, caption="Error", style=wx.ICON_EXCLAMATION)
            elif (version == 2.2):
              set_loaded = self.CheckDuplicateTileset(info[1])
              result = False
              if not(set_loaded):
                TilesetPath = os.path.join(gv.tiles_directory,str(info[1]))
                os.chdir(TilesetPath)
                filelist = glob.glob('*.set')
                if (filelist == []):
                  logging.critical("No tileset file found in %s", TilesetPath)
                  result = False
                else:
                  filename = os.path.join(str(info[1]),str(filelist[0]))
                  result = self.ReadTilesetFile(filename, True)
                if (result == False):
                  text = "Error in ReadGeomorphFile: Could not open tileset file ", str(info[1])
                  wx.MessageBox(message=text, caption="Error", style=wx.ICON_EXCLAMATION)
            else:
              #reading current version
              #check for spaces in filenames
              if (len(info) > 3):
                while (len(info) > 3):
                  length = len(info)
                  info[1] = (info[1]) +" " + (info[2])
                  info.remove(info[2])

              set_loaded = self.CheckDuplicateTileset(info[2])
              result = False
              if not(set_loaded):
                #try to load based on tileset ID
                TilesetPath = os.path.join(gv.tiles_directory,str(info[2]))
                try:
                  os.chdir(TilesetPath)
                except OSError:
                  text = "Error in ReadMapFile: Could not change to "+TilesetPath+"\n"
                  wx.MessageBox(message=text, caption="Error", style=wx.ICON_EXCLAMATION)
                  return False
                filelist = glob.glob('*.set')
                if (filelist == []):
                  result = self.ReadTilesetFile(info[1], False)
                else:
                  filename = os.path.join(str(info[2]),str(filelist[0]))
                  result = self.ReadTilesetFile(filename, True)
                if (result == False):
                  text = "Error in ReadGeomorphFile: Could not open tileset file ", str(info[1])
                  wx.MessageBox(message=text, caption="Error", style=wx.ICON_EXCLAMATION)

            if (result == True):
              tilesets_loaded = True
          elif info[0] == 'VIEWGRID':
            if (info[1] == 'ON'):
              gv.DisplayGrid = True
            else:
              gv.DisplayGrid = False
          elif (info[0] == 'GEOMORPH_RIGHT'):
            Geomorph.geomorph = True
            Geomorph.geomorphRight = int(info[1])
          elif (info[0] == 'GEOMORPH_LEFT'):
            Geomorph.geomorph = True
            Geomorph.geomorphLeft = int(info[1])
          elif (info[0] == 'GEOMORPH_TOP'):
            Geomorph.geomorph = True
            Geomorph.geomorphTop = int(info[1])
          elif (info[0] == 'GEOMORPH_BOTTOM'):
            Geomorph.geomorph = True
            Geomorph.geomorphBottom = int(info[1])
          elif (info[0] == 'MAP_LAYERS'):
            Geomorph.LayerDisplay = []
            Geomorph.LayerList = []
            readtext = True
            while (readtext == True):
              line = mapfile.readline()
              line = line.rstrip("\n\r")
              info = line.split()
              if (info[0] == "END_LAYERS"):
                readtext = False
              else:
                Geomorph.LayerList.append(info[0])
                if (info[1] == 'True'):
                  Geomorph.LayerDisplay.append(True)
                else:
                  Geomorph.LayerDisplay.append(False)
          elif (info[0] == 'VERSION'):
            version = float(info[1])
          elif (info[0] == 'ROOM_ICONS'):
            readtext = True
            while (readtext == True):
              line = mapfile.readline()
              line = line.rstrip("\n\r")
              info = line.split()
              if (info[0] == 'ROOM_INFO_START'):
                room = RoomInfo()
                room.Icon = self.RoomIcon
              elif (info[0] == 'ROOM_DESCRIPTION'):
                if (version >= 2.4):
                  line = mapfile.readline()
                  line = line.rstrip("\n\r")
                  room.Description = line
                else:
                  room.Description = info[1]
              elif (info[0] == 'ROOM_LAYER'):
                if (version < 2.6):
                  room.Layer = 0
                else:
                  room.Layer = int(info[1])
              elif (info[0] == 'ROOM_ICON'):
                if (info[1] == 'Trap'):
                  room.Icon = self.TrapIcon
                  room.IconType = 'Trap'
                elif (info[1] == 'Monster'):
                  room.Icon = self.MonsterIcon
                  room.IconType = 'Monster'
                elif (info[1] == 'NPC'):
                  room.Icon = self.NPC_Icon
                  room.IconType = 'NPC'
                elif (info[1] == 'Treasure'):
                  room.Icon = self.TreasureIcon
                  room.IconType = 'Treasure'
                else:
                  room.Icon = self.RoomIcon
                  room.IconType = 'Room'
              elif (info[0] == 'ROOM_POSITION'):
                room.x = float(info[1])
                room.y = float(info[2])
                room.placed = True
              elif (info[0] == 'ROOM_XML_FILE'):
                room.xml_file = mapfile.readline().rstrip('\n\r')
              elif (info[0] == 'ROOM_XML_PATH'):
                room.xml_path = mapfile.readline().rstrip('\n\r')
              elif (info[0] == 'ROOM_INFO_END'):
                Geomorph.RoomList.append(room)
              elif (info[0] == 'ROOM_ICONS_END'):
                readtext = False
          elif (info[0] == 'ANNOTATIONS'):
            readtext = True
            text = Annotation()
            while (readtext == True):
              line = mapfile.readline()
              line = line.rstrip("\n\r")
              info = line.split()
              if (info[0] == 'TEXT'):
                text.x = float(info[1])
                text.y = float(info[2])
                info.pop(0)
                info.pop(0)
                info.pop(0)
                text.text = info[0]
                info.pop(0)
                while (len(info) > 0):
                  text.text += " "
                  text.text += info[0]
                  info.pop(0)
              elif(info[0] == 'FONT_PT_SIZE'):
                pt_size = int(info[1])
              elif(info[0] == 'FONT_FAMILY'):
                family = int(info[1])
              elif(info[0] == 'FONT_STYLE'):
                style = int(info[1])
              elif(info[0] == 'FONT_WEIGHT'):
                weight = int(info[1])
              elif(info[0] == 'FONT_FACENAME'):
                info.pop(0)
                facename = info[0]
                info.pop(0)
                while (len(info) != 0):
                  facename += " "
                  facename += info[0]
                  info.pop(0)
              elif(info[0] == 'TEXT_BG'):
                text.bg = wx.Colour(int(info[1]), int(info[2]), int(info[3]))
              elif(info[0] == 'TEXT_FG'):
                text.fg = wx.Colour(int(info[1]), int(info[2]), int(info[3]))
              elif(info[0] == 'OPAQUE'):
                if (info[1] == 'ON'):
                  text.opaque = True
                elif (info[1] == 'OFF'):
                  text.opaque = False
              elif(info[0] == 'END_TEXT'):
                text.font = wx.Font(pt_size, family, style, weight,
                                    False, facename, wx.FONTENCODING_DEFAULT)
                Geomorph.TextList.append(text)
                text = Annotation()
              elif(info[0] == 'END_ANNOTATIONS'):
                readtext = False
                for label in Geomorph.TextList:
                  label = self.CreateTextLabelBitmap(label, gv.MapZoomFactor)
          elif (info[0] == 'BACKGROUND'):
            pass  #ignore this tag for now
          elif (info[0] == 'SNAP_GRID'):
            if (info[1] == 'ON'):
              gv.SnapToGrid == True
            else:
              gv.SnapToGrid == False
          elif (info[0] == 'GRID_COLOR'):
            pass #ignore this tag
          elif (info[0] == 'MAP_ZOOM'):
            gv.MapZoomFactor = int(info[1])
          elif (info[0] == 'ROWS'):
            self.MapStruct.rows = int(info[1])
          elif (info[0] == 'COLUMNS'):
            self.MapStruct.columns = int(info[1])
          elif (info[0] == 'PREVIEW'):
            Geomorph.preview = mapfile.readline()
          elif (info[0] == 'BEGIN_MAP_DEFINITION'):
            read_map = True
            while (read_map == True):
              line = mapfile.readline()
              info = line.split()
              if (info[0] == 'TILE'):
                newtile.tilesetID = info[1]
                newtile.tileID = int(info[2])
                for tile in self.tilelist:
                  if ((newtile.tilesetID == tile.tilesetID) and 
                      (newtile.tileID == tile.tileID)):
                    newtile.key_index = tile.key_index
                    tile.num_used += 1
                    for tset in gv.tilesets:
                      if (tset.SetID == tile.tilesetID):
                        tset.used = True
                    if (tile.num_used >= tile.copies):
                      newtile.dimmed = True
                      tile.dimmed = True
                newtile.dimmed = True
              elif (info[0] == 'TILE_LAYER'):
                newtile.layer = int(info[1])
              elif (info[0] == 'POSITION'):
                if (self.MapStruct.geomorph):
                  newtile.MapPosition = wx.Point2D(float(info[1])+1, float(info[2])+1)
                else:
                  newtile.MapPosition = wx.Point2D(float(info[1]), float(info[2]))
              elif (info[0] == 'A_SIDE'):
                newtile.showingBside = False
              elif (info[0] == 'B_SIDE'):
                newtile.showingBside = True
              elif (info[0] == 'ROTATION'):
                newtile.rotation = float(info[1])
              elif (info[0] == 'END_TILE'):
                addtile = self.ioAssignMapTileValues(newtile)
                Geomorph.TileList.append(addtile)
                newtile = Tile()
              elif (info[0] == 'END_MAP_DEFINITION'):
                read_map = False
          elif (info[0] == 'END_MAP_FILE'):
            mapfile.close()
            for tile in self.maplist:
              tile.GenerateMapDisplay(gv.MapZoomFactor)
            return Geomorph

  def ioAssignMapTileValues(self, newtile):
    found = False
    for tile in self.tilelist:
      if ((newtile.tilesetID == tile.tilesetID) and (newtile.tileID == tile.tileID)):
        found = True
        newtile.sideA = tile.sideA
        newtile.sideB = tile.sideB
        newtile.actualXsize = tile.actualXsize
        newtile.actualYsize = tile.actualYsize
        #set up newtile.MapRect and mapimage
        newtile.selected = False
        newtile.shown = True

        Xscale = newtile.actualXsize
        Yscale = newtile.actualYsize
        if (newtile.showingBside):
          mapimage = newtile.sideB
        else:
          mapimage = newtile.sideA
        mapimage = mapimage.Scale(Xscale, Yscale)
        mapimage = wx.BitmapFromImage(mapimage)
        newtile.mapdisplay = mapimage #wxImage to display on the MapPanel
        newtile.selected = False

        xpos = newtile.MapPosition.x
        ypos = newtile.MapPosition.y
        if ((newtile.rotation == 90) or (newtile.rotation == 270)):
          newtile.MapRect = wx.Rect2D(xpos, ypos, Yscale, Xscale)
        else:
          newtile.MapRect = wx.Rect2D(xpos, ypos, Xscale, Yscale)
        break
    if (not found):
      #no tile was found with a matching index in the loaded tilesets
      #this is possible when a user has added symbols, but these were not sent 
      #out when the map was shared.
      if (newtile.tilesetID == "SYMBOLS"):
        newtile.sideA = app.ImageNotFound
        newtile.sideB = app.ImageNotFound
        newtile.actualXsize = 1
        newtile.actualYsize = 1
        newtile.selected = False
        Xscale = newtile.actualXsize
        Yscale = newtile.actualYsize
        if (newtile.showingBside):
          mapimage = newtile.sideB
        else:
          mapimage = newtile.sideA
        mapimage = mapimage.Scale(Xscale, Yscale)
        newtile.mapdisplay = wx.BitmapFromImage(mapimage)
        newtile.selected = False

        xpos = newtile.MapPosition.x
        ypos = newtile.MapPosition.y
        if ((newtile.rotation == 90) or (newtile.rotation == 270)):
          newtile.MapRect = wx.Rect2D(xpos, ypos, Yscale, Xscale)
        else:
          newtile.MapRect = wx.Rect2D(xpos, ypos, Xscale, Yscale)
    return newtile

  def SplashScreen(self):
    frame = pymSplashScreen()
    if (not frame):  #Exit if frame could not be created
      logging.error("Could not start splash screen")
      return None
    frame.Show()
    return frame.GetScreenRect()

  def SaveIniFile(self):
    filename = os.path.join(gv.root_directory,"pymapper.ini")
    try:
      ini = open(filename, 'w')
    except IOError:
      logging.critical("SaveIniFile: Could not open %s for writing", filename)
      return False
    ini.write("# PyMapper settings file\n")
    ini.write("SETTINGS_VERSION 3.0\n")

    ini.write("TILESET_PAGES\n")
    for page in gv.TilePageList:
      if (page.tilesets == []):
        continue
      else:
        ini.write(str(page.PageName)+"\n")
    ini.write("END_TILE_PAGES\n")

    temp_tileset_names = []
    write_pages = []
    for tset in gv.tilesets:
      if (tset.loaded) and (not tset.SetID == 'MARKERS'):
        ini.write("TILESET\n")
        ini.write(tset.filename+"\n")
        temp_tileset_names.append(tset.Name)
        ini.write(tset.Name+"\n")  #added to settings version 3.0

    #check pages for duplicated tilesets
    num_tilesets = 0
    for page in gv.TilePageList:
      page.tilesets = list(set(page.tilesets)) #removes duplicates


    for page in gv.TilePageList:
      ini.write("TILESET_PAGE_ASSIGNMENT "+str(len(page.tilesets))+"\n")
      ini.write(page.PageName+"\n")
      for tilepage in page.tilesets:
        ini.write(tilepage+"\n")

    if (gv.AutoSave):
      ini.write("BACKUP\n")
      ini.write(str(gv.backup_directory)+"\n")
    (width, height) = self.frame.GetSizeTuple()
    (dx, dy) = self.frame.GetPositionTuple()
    ini.write("PYMAPPER_WINDOW "+str(dx)+" "+str(dy)+" "+str(width)+" "+str(height)+"\n")
    ini.write("SHOW_TIPS\n")
    ini.write(str(gv.ShowTips) + " " + str(gv.LastTip) + "\n")
    ini.write("TILE_ZOOM\n")
    ini.write(str(gv.TileZoomFactor)+ " " + str(gv.TileZoomIncrement)+"\n")
    ini.write("MAP_ZOOM\n")
    ini.write(str(gv.MapZoomFactor)+ " " + str(gv.MapZoomIncrement)+"\n")
    ini.write(("SHOW_ICON_NAMES " + str(gv.ShowIconNamesOnMap) + "\n"))
    ini.write(("SNAP_ICONS " + str(gv.SnapIconToGrid) + "\n"))
    ini.write("TILE_BORDER\n")
    ini.write(str(gv.tileborderwidth)+"\n")
    ini.write("TILE_BACKGROUND\n")
    ini.write(str(gv.TilePanelBackgroundColor.Red()) + " " +
              str(gv.TilePanelBackgroundColor.Green()) + " " +
              str(gv.TilePanelBackgroundColor.Blue()) + " " +
              str(gv.TilePanelBackgroundColor.Alpha())+"\n")
    ini.write("MAP_BACKGROUND\n")
    ini.write(str(gv.MapPanelBackgroundColor.Red()) + " " +
              str(gv.MapPanelBackgroundColor.Green()) + " " +
              str(gv.MapPanelBackgroundColor.Blue()) + " " +
              str(gv.MapPanelBackgroundColor.Alpha())+"\n")
    ini.write("GRID_OPTIONS\n")
    ini.write(str(gv.DisplayGrid) + " ")
    ini.write(str(gv.GridColor.Red()) + " " +
              str(gv.GridColor.Green()) + " " +
              str(gv.GridColor.Blue()) + " " +
              str(gv.GridColor.Alpha())+" ")
    ini.write(str(gv.GridPenWidth) + " ")
    ini.write(str(gv.GridPenStyle) + "\n")
    ini.write(str("GRID_SCALE "+str(gv.GridScale))+ "\n")
    if (gv.DrawGridOnTop):
      ini.write("GRID_ON_TOP\n")
    ini.write("OUTLINE_ON_HOVER " + str(gv.OutlineOnHover)+"\n")
    ini.write("RESET_TILE_STATISTICS_BY_PAGE " + str(gv.ResetTileStatistics)+"\n")
    ini.write("HOVER_OPTIONS\n")
    ini.write(str(gv.hover_interval) + " ")
    ini.write(str(gv.DisplayOnHover) + "\n")
    ini.write("SHOW_DRAWING_HANDLES "+str(gv.DrawHandles)+"\n")
    ini.write("SELECTION_OPTIONS\n")
    ini.write(str(gv.SelectionColor.Red()) + " " +
              str(gv.SelectionColor.Green()) + " " +
              str(gv.SelectionColor.Blue()) + " " +
              str(gv.SelectionColor.Alpha())+" ")
    ini.write(str(gv.SelectionPenWidth) + " ")
    ini.write(str(gv.SelectionPenStyle) + "\n")
    ini.write("BACKGROUND_OPTIONS\n")
    ini.write(str(gv.DisplayBackground) + " ")
    ini.write(str(gv.BackgroundOpacity) + " ")
    ini.write(str(self.MapStruct.bg_displaymode) + " ")
    ini.write(str(self.MapStruct.bg_x_dimension) + " ")
    ini.write(str(self.MapStruct.bg_y_dimension) + "\n")
    ini.write(str(self.MapStruct.background_filename) + "\n")
    ini.write("AUTO_SAVE\n")
    ini.write(str(gv.AutoSave) + " ")
    ini.write(str(gv.AutoSaveInterval) + "\n")
    ini.write("SAVE_INI_ON_CLOSE\n")
    ini.write(str(gv.SaveIniFile) +"\n")
    ini.write("READ_SRD_ON_STARTUP\n")
    ini.write(str(gv.ReadSRDFileData) + "\n")
    ini.write("READ_5E_ON_STARTUP\n")
    ini.write(str(gv.Read5EditionFileData) + "\n")
    if (not gv.ChangeDefaultFolder):
      ini.write("KEEP_DEFAULT_FOLDERS\n")
    ini.write("DUAL_TILE_DISPLAY ")
    ini.write(str(gv.DualDisplayTileWindow) + "\n")
    if (gv.ShowTutorial == False):
      ini.write("NO_TUTORIAL\n")
    if (gv.SavePrintResolution):
      ini.write("PRINT_RESOLUTION " + str(gv.PrintResolution)+"\n")
    ini.write("SHOW_GRID_COORDINATES " + str(gv.ShowGridCoordinates)+"\n")
    ini.write("LIMIT_TILE_USAGE " + str(gv.LimitTiles)+"\n")
    ini.write("CONDITION_COLOR_BLINDED " + str(gv.ConditionColors.BlindedColor.Red()) + " " +str(gv.ConditionColors.BlindedColor.Green()) + " " +str(gv.ConditionColors.BlindedColor.Blue()) + " " +str(gv.ConditionColors.BlindedColor.Alpha()) + "\n")
    ini.write("CONDITION_COLOR_CHARMED " + str(gv.ConditionColors.CharmedColor.Red()) + " " +str(gv.ConditionColors.CharmedColor.Green()) + " " +str(gv.ConditionColors.CharmedColor.Blue()) + " " +str(gv.ConditionColors.CharmedColor.Alpha()) + "\n")
    ini.write("CONDITION_COLOR_CONCENTRATING " + str(gv.ConditionColors.ConcentratingColor.Red()) + " " +str(gv.ConditionColors.ConcentratingColor.Green()) + " " +str(gv.ConditionColors.ConcentratingColor.Blue()) + " " +str(gv.ConditionColors.ConcentratingColor.Alpha()) + "\n")
    ini.write("CONDITION_COLOR_DEAFENED " + str(gv.ConditionColors.DeafenedColor.Red()) + " " +str(gv.ConditionColors.DeafenedColor.Green()) + " " +str(gv.ConditionColors.DeafenedColor.Blue()) + " " +str(gv.ConditionColors.DeafenedColor.Alpha()) + "\n")
    ini.write("CONDITION_COLOR_FRIGHTENED " + str(gv.ConditionColors.FrightenedColor.Red()) + " " +str(gv.ConditionColors.FrightenedColor.Green()) + " " +str(gv.ConditionColors.FrightenedColor.Blue()) + " " +str(gv.ConditionColors.FrightenedColor.Alpha()) + "\n")
    ini.write("CONDITION_COLOR_GRAPPLED " + str(gv.ConditionColors.GrappledColor.Red()) + " " +str(gv.ConditionColors.GrappledColor.Green()) + " " +str(gv.ConditionColors.GrappledColor.Blue()) + " " +str(gv.ConditionColors.GrappledColor.Alpha()) + "\n")
    ini.write("CONDITION_COLOR_INCAPACITATED " + str(gv.ConditionColors.IncapacitatedColor.Red()) + " " +str(gv.ConditionColors.IncapacitatedColor.Green()) + " " +str(gv.ConditionColors.IncapacitatedColor.Blue()) + " " +str(gv.ConditionColors.IncapacitatedColor.Alpha()) + "\n")
    ini.write("CONDITION_COLOR_INVISIBLE " + str(gv.ConditionColors.InvisibleColor.Red()) + " " +str(gv.ConditionColors.InvisibleColor.Green()) + " " +str(gv.ConditionColors.InvisibleColor.Blue()) + " " +str(gv.ConditionColors.InvisibleColor.Alpha()) + "\n")
    ini.write("CONDITION_COLOR_PARALYZED " + str(gv.ConditionColors.ParalyzedColor.Red()) + " " +str(gv.ConditionColors.ParalyzedColor.Green()) + " " +str(gv.ConditionColors.ParalyzedColor.Blue()) + " " +str(gv.ConditionColors.ParalyzedColor.Alpha()) + "\n")
    ini.write("CONDITION_COLOR_PETRIFIED " + str(gv.ConditionColors.PetrifiedColor.Red()) + " " +str(gv.ConditionColors.PetrifiedColor.Green()) + " " +str(gv.ConditionColors.PetrifiedColor.Blue()) + " " +str(gv.ConditionColors.PetrifiedColor.Alpha()) + "\n")
    ini.write("CONDITION_COLOR_POISONED " + str(gv.ConditionColors.PoisonedColor.Red()) + " " +str(gv.ConditionColors.PoisonedColor.Green()) + " " +str(gv.ConditionColors.PoisonedColor.Blue()) + " " +str(gv.ConditionColors.PoisonedColor.Alpha()) + "\n")
    ini.write("CONDITION_COLOR_PRONE " + str(gv.ConditionColors.ProneColor.Red()) + " " +str(gv.ConditionColors.ProneColor.Green()) + " " +str(gv.ConditionColors.ProneColor.Blue()) + " " +str(gv.ConditionColors.ProneColor.Alpha()) + "\n")
    ini.write("CONDITION_COLOR_RESTRAINED " + str(gv.ConditionColors.RestrainedColor.Red()) + " " +str(gv.ConditionColors.RestrainedColor.Green()) + " " +str(gv.ConditionColors.RestrainedColor.Blue()) + " " +str(gv.ConditionColors.RestrainedColor.Alpha()) + "\n")
    ini.write("CONDITION_COLOR_STUNNED " + str(gv.ConditionColors.StunnedColor.Red()) + " " +str(gv.ConditionColors.StunnedColor.Green()) + " " +str(gv.ConditionColors.StunnedColor.Blue()) + " " +str(gv.ConditionColors.StunnedColor.Alpha()) + "\n")
    ini.write("CONDITION_COLOR_TURNED " + str(gv.ConditionColors.TurnedColor.Red()) + " " +str(gv.ConditionColors.TurnedColor.Green()) + " " +str(gv.ConditionColors.TurnedColor.Blue()) + " " +str(gv.ConditionColors.TurnedColor.Alpha()) + "\n")
    ini.write("CONDITION_COLOR_UNCONSCIOUS " + str(gv.ConditionColors.UnconsciousColor.Red()) + " " +str(gv.ConditionColors.UnconsciousColor.Green()) + " " +str(gv.ConditionColors.UnconsciousColor.Blue()) + " " +str(gv.ConditionColors.UnconsciousColor.Alpha()) + "\n")
    ini.write("CONDITION_BAR_THICKNESS " + str(gv.ConditionBarThickness) + "\n")
    
    ini.write("END_INI")
    ini.close()
    return True

  def SaveMapFile(self, filename):
    """If filename == None, then prompt for a filename"""
    if (filename == None):
      self.OnFileSaveAs()
      return
    try:
      savefile = open(filename, 'w')
    except IOError:
      logging.critical("SaveMapFile:  Could not open %s for writing", filename)
      return
    savefile.write("MAPFILE\n")
    savefile.write("VERSION "+str(gv.MapfileSpecificationVersion)+" \n")
    
    #check to see if the dungeon resources need to be loaded
    loadD20 = False
    loadDnD5 = False
    
    for room in gv.RoomList:
      if (isinstance(room.monster, srd.Monster5E_Record)) or (isinstance(room.npc, srd.Monster5E_Record)):
        loadDnD5 = True
      elif (isinstance(room.monster, srd.Monster_Record)) or (isinstance(room.npc, srd.NPC_Record)):
        loadD20 = True
    
    if (loadDnD5):
      savefile.write("LOAD_DND5_RESOURCES\n")
    if (loadD20):
      savefile.write("LOAD_D20_RESOURCES\n")


    if (gv.LayerList):
      savefile.write("MAP_LAYERS\n")
      for layer in gv.LayerList:
        savefile.write(layer.name+" "+str(layer.display)+" "+str(layer.index)+" "+str(layer.opacity)+" \n")
      savefile.write("END_LAYERS\n")
    if (gv.tilesets):
      for tile in self.maplist:
        for tset in gv.tilesets:
          if (tset.SetID == tile.tilesetID):
            tset.used = True
      for TileSet in gv.tilesets:
        if (TileSet.used):
          savefile.write("TILESET "+str(TileSet.filename)+ " " +str(TileSet.SetID)+" \n")
    if (gv.SnapToGrid == True):
      savefile.write("SNAP_GRID ON \n")
    else:
      savefile.write("SNAP_GRID OFF \n")
    if (self.MapStruct.gridcolor):
      red = self.MapStruct.gridcolor.Red()
      green = self.MapStruct.gridcolor.Green()
      blue = self.MapStruct.gridcolor.Blue()
      alpha = self.MapStruct.gridcolor.Alpha()
      savefile.write("GRID_COLOR "+repr(red)+" "+repr(green)+" "+repr(blue)+" "+repr(alpha)+" \n")
    else:
      savefile.write("GRID_COLOR NONE \n")
    savefile.write("MAP_ZOOM "+repr(gv.MapZoomFactor)+" \n")
    savefile.write("ROWS "+repr(self.MapStruct.rows)+" \n")
    savefile.write("COLUMNS "+repr(self.MapStruct.columns)+" \n")
    if (gv.DisplayGrid):
      savefile.write("VIEWGRID ON \n")
    else:
      savefile.write("VIEWGRID OFF \n")

    savefile.write("MAP_PAGES \n")
    for page in gv.MapPageList:
      savefile.write("START_PAGE \n")
      savefile.write("PAGE_ID "+str(page.PageID)+"\n")
      savefile.write("PAGE_ZOOM "+str(page.ZoomFactor)+"\n")
      savefile.write("PAGE_XSCROLL "+str(page.Xscroll)+"\n")
      savefile.write("PAGE_YSCROLL "+str(page.Yscroll)+"\n")
      savefile.write("PAGE_NAME\n")
      savefile.write(str(page.PageName)+"\n")
      savefile.write("PAGE_BACKGROUND_FILENAME\n")
      savefile.write(str(page.background_filename)+"\n")
      savefile.write(str(page.background_filepath)+"\n")
      savefile.write("PAGE_BACKGROUND_DISPLAY_MODE "+str(page.bg_displaymode)+"\n")
      savefile.write("PAGE_BACKGROUND_DIMENSION " + str(page.bg_x_dimension) + " " + str(page.bg_y_dimension) + "\n")
      savefile.write("END_PAGE\n")
    savefile.write("END_MAP_PAGES\n")

    if (self.MapStruct.geomorph):
      savefile.write("GEOMORPH_RIGHT "+str(self.MapStruct.geomorphData.geomorphRight)+"\n")
      savefile.write("GEOMORPH_TOP "+str(self.MapStruct.geomorphData.geomorphTop)+"\n")
      savefile.write("GEOMORPH_LEFT "+str(self.MapStruct.geomorphData.geomorphLeft)+"\n")
      savefile.write("GEOMORPH_BOTTOM "+str(self.MapStruct.geomorphData.geomorphBottom)+"\n")

    savefile.write("BEGIN_MAP_DEFINITION \n")
    for tile in self.maplist:
      ''' TILE tilesetID XY_MapPosition'''
      savefile.write("TILE "+(tile.tilesetID)+" "+repr(tile.tileID)+" \n")
      if (self.MapStruct.geomorph):
        savefile.write("POSITION "+repr(tile.MapPosition.x-1)+" "+repr(tile.MapPosition.y-1)+" \n")
      else:
        savefile.write("POSITION "+repr(tile.MapPosition.x)+" "+repr(tile.MapPosition.y)+" \n")
      if (tile.showingBside):
        savefile.write("B_SIDE \n")
      else:
        savefile.write("A_SIDE \n")
      savefile.write("ROTATION "+repr(tile.rotation)+" \n")
      savefile.write("TILE_LAYER "+str(tile.layer)+" \n")
      savefile.write("TILE_PAGE\n" + str(tile.page)+"\n")
      savefile.write("END_TILE \n")
    savefile.write("END_MAP_DEFINITION \n")

    savefile.write("ANNOTATIONS\n")
    for txt in self.textlist:
      savefile.write("TEXT "+ str(txt.x)+ " " + str(txt.y) + " " + str(txt.text) +"\n")
      savefile.write("FONT_PT_SIZE " + str(txt.font.GetPointSize())+"\n")
      savefile.write("FONT_FAMILY " + str(txt.font.GetFamily())+"\n")
      savefile.write("FONT_STYLE " + str(txt.font.GetStyle())+"\n")
      savefile.write("FONT_WEIGHT " + str(txt.font.GetWeight())+"\n")
      savefile.write("FONT_FACENAME " + str(txt.font.GetFaceName())+"\n")
      savefile.write("TEXT_BG " + str(txt.bg.Red()) + " " + str(txt.bg.Green()) + " " + str(txt.bg.Blue()) + "\n")
      savefile.write("TEXT_FG " + str(txt.fg.Red()) + " " + str(txt.fg.Green()) + " " + str(txt.fg.Blue()) + "\n")
      savefile.write("OPAQUE ")
      if (txt.opaque==True):
        savefile.write("ON\n")
      else:
        savefile.write("OFF\n")
      savefile.write("ANNO_PAGE\n" + str(txt.page)+"\n")
      savefile.write("END_TEXT\n")
    savefile.write("END_ANNOTATIONS\n")
    
    if (gv.RoomList != []):
      savefile.write("ROOM_ICONS\n")
      for room in gv.RoomList:
        savefile.write("ROOM_INFO_START\n")
        savefile.write("ROOM_DESCRIPTION\n")
        savefile.write(str(room.Description)+"\n")
        savefile.write("ROOM_ICON " + room.IconType + "\n")
        if (room.monster):
          if (room.monster.version == '5E'):
            savefile.write("MONSTER_5E_UNIQUE_ID " + str(room.monster.uniqueID) + "\n")
          elif (room.monster.version == '5E_NPC'):
            savefile.write("MONSTER_5E_NPC_UNIQUE_ID " + str(room.monster.uniqueID) + "\n")
          else:  #3.5 and PF monsters/npc's
            savefile.write("MONSTER_UNIQUE_ID " + str(room.monster.uniqueID) + "\n")
          savefile.write("MONSTER_HP " + str(room.monster.HP) + "\n")
          if (room.monster.customName):
            savefile.write("MONSTER_CUSTOM_NAME\n")
            savefile.write(str(room.monster.customName)+"\n")
          if (room.monster.filename):
            savefile.write("MONSTER_CUSTOM_IMAGE\n")
            savefile.write((room.monster.filename + "\n"))
        if (room.trap):
          savefile.write("TRAP_UNIQUE_ID\n")
          savefile.write(str(room.trap.desc)+"\n")
        savefile.write("ROOM_LAYER " + str(room.Layer) + "\n")
        if (room.placed):
          savefile.write("ROOM_POSITION " + str(room.x) + " " + str(room.y) + "\n")
        savefile.write("ROOM_XML_FILE\n")
        savefile.write(str(room.xml_file)+"\n")
        savefile.write("ROOM_XML_PATH\n")
        savefile.write(str(room.xml_path)+"\n")
        savefile.write("ROOM_PAGE\n"+str(room.page)+"\n")
        savefile.write("ROOM_HIGHLIGHT_COLOR "+str(room.highlightColor.Red())+" "+str(room.highlightColor.Green())+" "+str(room.highlightColor.Blue())+" "+str(room.highlightColor.Alpha())+"\n")  
        savefile.write("ROOM_INFO_END\n")
      savefile.write("ROOM_ICONS_END\n")
    if (self.DrawingList):
      self.SaveDrawingItems(savefile)
    savefile.write("END_MAP_FILE")
    savefile.close()
    logging.info("Map File saved")
    gv.PromptSave = False
    return

  def SaveDrawingItems(self, savefile):
    """savefile must be an open and valid file object"""
    savefile.write("BEGIN_DRAWING_ITEMS\n")
    #item = gv.DrawingObject_Record()
    for item in self.DrawingList:
      if (item.tool == 'Freehand'):
        savefile.write("DRAW_FREEHAND\n")
        for point in item.line:
          savefile.write("XY_POINT {0} {1}\n".format(point.x, point.y))
        color = item.pen.GetColour()
        Cwidth = item.pen.GetWidth()
        Cstyle = item.pen.GetStyle()
        savefile.write("LINE_COLOR {0} {1} {2} {3}\n".format(color.red, color.green, color.blue, color.alpha))
        savefile.write("LINE_WIDTH {0}\n".format(Cwidth))
        savefile.write("LINE_STYLE {0}\n".format(Cstyle))
        brush = item.brush.GetColour()
        savefile.write("BRUSH_COLOR {0} {1} {2} {3}\n".format(brush.red, brush.green, brush.blue, brush.alpha))
        #savefile.write("PAGE_INDEX "+str(item.page_index)+"\n")  #removed in 9.1; replaced by PAGE_NAME
        savefile.write("PAGE_NAME\n" + item.page_name +"\n")
        if (item.object_type == 'fog'):
          savefile.write("FOG_ITEM\n")  #default is a draw item.
        savefile.write("END_FREEHAND\n")
      elif (item.tool == 'Line'):
        savefile.write("DRAW_LINE\n")
        for point in item.line:
          savefile.write("XY_POINT {0} {1}\n".format(point.x, point.y))
        color = item.pen.GetColour()
        Cwidth = item.pen.GetWidth()
        Cstyle = item.pen.GetStyle()
        savefile.write("LINE_COLOR {0} {1} {2} {3}\n".format(color.red, color.green, color.blue, color.alpha))
        savefile.write("LINE_WIDTH {0}\n".format(Cwidth))
        savefile.write("LINE_STYLE {0}\n".format(Cstyle))
        brush = item.brush.GetColour()
        savefile.write("BRUSH_COLOR {0} {1} {2} {3}\n".format(brush.red, brush.green, brush.blue, brush.alpha))
        #savefile.write("PAGE_INDEX "+str(item.page_index)+"\n")
        savefile.write("PAGE_NAME\n" + item.page_name +"\n")
        if (item.object_type == 'fog'):
          savefile.write("FOG_ITEM\n")  #default is a draw item.
        savefile.write("END_LINE\n")
      elif (item.tool == 'Multiline'):
        savefile.write("DRAW_MULTILINE\n")
        for point in item.line:
          savefile.write("XY_POINT {0} {1}\n".format(point.x, point.y))
        color = item.pen.GetColour()
        Cwidth = item.pen.GetWidth()
        Cstyle = item.pen.GetStyle()
        savefile.write("LINE_COLOR {0} {1} {2} {3}\n".format(color.red, color.green, color.blue, color.alpha))
        savefile.write("LINE_WIDTH {0}\n".format(Cwidth))
        savefile.write("LINE_STYLE {0}\n".format(Cstyle))
        brush = item.brush.GetColour()
        savefile.write("BRUSH_COLOR {0} {1} {2} {3}\n".format(brush.red, brush.green, brush.blue, brush.alpha))
        #savefile.write("PAGE_INDEX "+str(item.page_index)+"\n")
        savefile.write("PAGE_NAME\n" + item.page_name +"\n")
        if (item.object_type == 'fog'):
          savefile.write("FOG_ITEM\n")  #default is a draw item.
        savefile.write("END_MULTILINE\n")
      elif (item.tool == 'OutlineRect'):
        savefile.write("DRAW_OUTLINE_RECT\n")
        savefile.write("RECT {0} {1} {2} {3}\n".format(item.rect.x, item.rect.y, item.rect.width, item.rect.height))
        color = item.pen.GetColour()
        Cwidth = item.pen.GetWidth()
        Cstyle = item.pen.GetStyle()
        savefile.write("LINE_COLOR {0} {1} {2} {3}\n".format(color.red, color.green, color.blue, color.alpha))
        savefile.write("LINE_WIDTH {0}\n".format(Cwidth))
        savefile.write("LINE_STYLE {0}\n".format(Cstyle))
        brush = item.brush.GetColour()
        savefile.write("BRUSH_COLOR {0} {1} {2} {3}\n".format(brush.red, brush.green, brush.blue, brush.alpha))
        #savefile.write("PAGE_INDEX "+str(item.page_index)+"\n")
        savefile.write("PAGE_NAME\n" + item.page_name +"\n")
        if (item.object_type == 'fog'):
          savefile.write("FOG_ITEM\n")  #default is a draw item.
        savefile.write("END_OUTLINE_RECT\n")
      elif (item.tool == 'FillRect'):
        savefile.write("DRAW_FILL_RECT\n")
        savefile.write("RECT {0} {1} {2} {3}\n".format(item.rect.x, item.rect.y, item.rect.width, item.rect.height))
        color = item.pen.GetColour()
        Cwidth = item.pen.GetWidth()
        Cstyle = item.pen.GetStyle()
        savefile.write("LINE_COLOR {0} {1} {2} {3}\n".format(color.red, color.green, color.blue, color.alpha))
        savefile.write("LINE_WIDTH {0}\n".format(Cwidth))
        savefile.write("LINE_STYLE {0}\n".format(Cstyle))
        brush = item.brush.GetColour()
        savefile.write("BRUSH_COLOR {0} {1} {2} {3}\n".format(brush.red, brush.green, brush.blue, brush.alpha))
        #savefile.write("PAGE_INDEX "+str(item.page_index)+"\n")
        savefile.write("PAGE_NAME\n" + item.page_name +"\n")
        if (item.object_type == 'fog'):
          savefile.write("FOG_ITEM\n")  #default is a draw item.
        savefile.write("END_FILL_RECT\n")
      elif (item.tool == 'OutlineCircle'):
        (Xcircle, Ycircle) = item.circle[0]
        radius = item.circle[1]
        savefile.write("DRAW_OUTLINE_CIRCLE\n")
        savefile.write("CIRCLE {0} {1} {2}\n".format(Xcircle, Ycircle, radius))
        color = item.pen.GetColour()
        Cwidth = item.pen.GetWidth()
        Cstyle = item.pen.GetStyle()
        savefile.write("LINE_COLOR {0} {1} {2} {3}\n".format(color.red, color.green, color.blue, color.alpha))
        savefile.write("LINE_WIDTH {0}\n".format(Cwidth))
        savefile.write("LINE_STYLE {0}\n".format(Cstyle))
        brush = item.brush.GetColour()
        savefile.write("BRUSH_COLOR {0} {1} {2} {3}\n".format(brush.red, brush.green, brush.blue, brush.alpha))
        #savefile.write("PAGE_INDEX "+str(item.page_index)+"\n")
        savefile.write("PAGE_NAME\n" + item.page_name +"\n")
        if (item.object_type == 'fog'):
          savefile.write("FOG_ITEM\n")  #default is a draw item.
        savefile.write("END_OUTLINE_CIRCLE\n")
      elif (item.tool == 'FillCircle'):
        (Xcircle, Ycircle) = item.circle[0]
        radius = item.circle[1]
        savefile.write("DRAW_FILLED_CIRCLE\n")
        savefile.write("CIRCLE {0} {1} {2}\n".format(Xcircle, Ycircle, radius))
        color = item.pen.GetColour()
        Cwidth = item.pen.GetWidth()
        Cstyle = item.pen.GetStyle()
        savefile.write("LINE_COLOR {0} {1} {2} {3}\n".format(color.red, color.green, color.blue, color.alpha))
        savefile.write("LINE_WIDTH {0}\n".format(Cwidth))
        savefile.write("LINE_STYLE {0}\n".format(Cstyle))
        brush = item.brush.GetColour()
        savefile.write("BRUSH_COLOR {0} {1} {2} {3}\n".format(brush.red, brush.green, brush.blue, brush.alpha))
        #savefile.write("PAGE_INDEX "+str(item.page_index)+"\n")
        savefile.write("PAGE_NAME\n" + item.page_name +"\n")
        if (item.object_type == 'fog'):
          savefile.write("FOG_ITEM\n")  #default is a draw item.
        savefile.write("END_FILLED_CIRCLE\n")
      elif (item.tool == 'Image'):
        savefile.write("DRAW_IMAGE\n")
        savefile.write("RECT {0} {1} {2} {3}\n".format(item.rect.x, item.rect.y, item.rect.width, item.rect.height))
        savefile.write("IMAGE_FILENAME\n")
        savefile.write(item.image_filename)
        savefile.write("\n")
        savefile.write("IMAGE_PATH\n")
        savefile.write(item.image_path)
        savefile.write("\n")
        #savefile.write("PAGE_INDEX "+str(item.page_index)+"\n")
        savefile.write("PAGE_NAME\n" + item.page_name +"\n")
        savefile.write("END_IMAGE\n")
    savefile.write("END_DRAWING_ITEMS\n")
    return

  def CheckDuplicateTileset(self, setID):
    for tset in gv.tilesets:
      if ((setID == tset.SetID) and (tset.loaded == True)):
        return True
    return False

  def OnTileRightClick(self, event):
    if (gv.SelectMode == 'draw'):
      #tile window is inactive while drawing
      return
    self.hovertimer.Stop()
    foundtile = False
    for tile in self.tilelist:
      if (tile.selected):
        foundtile = True
        break
    menu = wx.Menu()
    # Show how to put an icon in the menu
    item = wx.MenuItem(menu, self.popupID51,"Zoom In")
    bmp1 = wx.Bitmap(os.path.join(gv.artwork_directory,"ZoomIn.png"), wx.BITMAP_TYPE_PNG)
    item.SetBitmap(bmp1)
    menu.AppendItem(item)
    # add some other items
    item2 = wx.MenuItem(menu, self.popupID52, "Zoom Out")
    bmp2 = wx.Bitmap(os.path.join(gv.artwork_directory,"ZoomOut.png"), wx.BITMAP_TYPE_PNG)
    item2.SetBitmap(bmp2)
    menu.AppendItem(item2)
    item7 = wx.MenuItem(menu, self.popupID57, "Flip All Tiles")
    bmp7 = wx.Bitmap(os.path.join(gv.artwork_directory,"flip_tile.png"), wx.BITMAP_TYPE_PNG)
    item7.SetBitmap(bmp7)
    menu.AppendItem(item7)

    if (foundtile):
      item3 = wx.MenuItem(menu, self.popupID53, "Properties")
      bmp3 = wx.Bitmap(os.path.join(gv.artwork_directory,"properties3.bmp"), wx.BITMAP_TYPE_BMP)
      item3.SetBitmap(bmp3)
      item4 = wx.MenuItem(menu, self.popupID54, "Filter tile")
      bmp4 = wx.Bitmap(os.path.join(gv.artwork_directory,"filter_tile.png"), wx.BITMAP_TYPE_PNG)
      item4.SetBitmap(bmp4)
      item5 = wx.MenuItem(menu, self.popupID55, "Filter tileset")
      bmp5 = wx.Bitmap(os.path.join(gv.artwork_directory,"filter_tileset.png"), wx.BITMAP_TYPE_PNG)
      item5.SetBitmap(bmp5)
      item8 = wx.MenuItem(menu, self.popupID58, "Highlight Tile on Map")
      bmp8 = wx.Bitmap(os.path.join(gv.artwork_directory,"highlight_tile.png"), wx.BITMAP_TYPE_PNG)
      item8.SetBitmap(bmp8)
      menu.AppendItem(item3)
      menu.AppendItem(item4)
      menu.AppendItem(item5)
      menu.AppendItem(item8)

    if (self.TilePanelFiltered):
      item6 = wx.MenuItem(menu, self.popupID56, "Clear Filters")
      bmp6 = wx.Bitmap(os.path.join(gv.artwork_directory,"clear_filter.bmp"), wx.BITMAP_TYPE_BMP)
      item6.SetBitmap(bmp6)
      menu.AppendItem(item6)

    # make a submenu
    #sm = wx.Menu()
    #sm.Append(self.popupID8, "sub item 1")
    #sm.Append(self.popupID9, "sub item 2")
    #menu.AppendMenu(self.popupID7, "Test Submenu", sm)
    #wx.EVT_MENU(menu, 'ZoomIn', self.MenuSelectionCb)
    self.TilePanel.PopupMenu(menu)
    menu.Destroy()
    self.hovertimer.Start(gv.hover_interval)
    return

  def RTileClickZoomIn(self, event):
    gv.TileZoomFactor = gv.TileZoomFactor + gv.TileZoomIncrement
    self.DrawTileWindow(True)
    return

  def RTileClickFlipAllTiles(self, event):
    for tile in self.tilelist:
      if (tile.sideB == None):
        continue
      if (tile.showingBside == True):
        tile.tiledisplay = tile.sideA
        tile.showingBside = False
      else:
        tile.tiledisplay = tile.sideB
        tile.showingBside = True
    self.DrawTileWindow(False)

  def RTileClickShowTileOnMap(self, event):
    for tile in self.tilelist:
      if (tile.selected == True):
        HLTile = tile
        break
    for maptile in self.maplist:
      if ((HLTile.tileID == maptile.tileID) and (HLTile.tilesetID == maptile.tilesetID)):
        maptile.highlight = True
        self.DrawMapWindow()
    return

  def RTileClickZoomOut(self, event):
    gv.TileZoomFactor = gv.TileZoomFactor - gv.TileZoomIncrement
    if (gv.TileZoomFactor < 1):
      gv.TileZoomFactor = 5
    self.DrawTileWindow(True)
    return

  def RTileClickProperties(self, event):
    for tile in self.tilelist:
      if (tile.selected == True):
        dlg = TilePropertiesDialogCore(self.frame, tile)
        dlg.Show(True)
    return

  def RTileClickFilterTile(self, event):
    for tile in self.tilelist:
      if (tile.selected == True):
        tile.ShowOnTilePanel = False
        tile.selected = False
        self.TilePanelFiltered = True
    if (self.TilePanelFiltered):
      self.DrawTileWindow(True)
    return

  def RTileClickFilterTileset(self, event):
    filter_setID = None
    for tile in self.tilelist:
      if (tile.selected == True):
        filter_setID = tile.tilesetID
        tile.selected = False
        break
    if (filter_setID == None):
      return
    for tile in self.tilelist:
      if (tile.tilesetID == filter_setID):
        tile.ShowOnTilePanel = False
        self.TilePanelFiltered = True
    if (self.TilePanelFiltered):
      self.DrawTileWindow(True)
    return

  def RTileClickClearFilters(self, event):
    self.TilePanelFiltered = False
    for tset in gv.tilesets:
      tset.DisplayTileWindow = True
    for tile in self.tilelist:
      tile.ShowOnTilePanel = True
    self.DrawTileWindow(True)
    
  def RMapClickChangeIconHighlight(self, event=None):
    found = False
    for room in gv.RoomList:
      rect = wx.Rect(int(room.x * gv.MapZoomFactor),
                     int(room.y * gv.MapZoomFactor),
                     room.MapRect.width, room.MapRect.height)
      gridpoint = self.MapPanel.CalcUnscrolledPosition(gv.LastPoint)
      found = rect.Contains(gridpoint)
      if (found):
        if (event.GetId() == self.popupID20): #change to red
          room.highlightColor = wx.RED
        elif (event.GetId() == self.popupID21): #change to blue
          room.highlightColor = wx.BLUE
        elif (event.GetId() == self.popupID22): #change to green
          room.highlightColor = wx.GREEN
        elif (event.GetId() == self.popupID23): #change to yellow
          room.highlightColor = wx.Colour(255,225,0,255)
        elif (event.GetId() == self.popupID24): #change to purple
          room.highlightColor = wx.Colour(178,0,255,255)
        self.DrawMapWindow(printing=False, drawOnly=False)
        break
        
    return
  
  def RMapClickCopyIcon(self, event=None):
    found = False
    for room in gv.RoomList:
      rect = wx.Rect(int(room.x * gv.MapZoomFactor),
                     int(room.y * gv.MapZoomFactor),
                     room.MapRect.width, room.MapRect.height)
      gridpoint = self.MapPanel.CalcUnscrolledPosition(gv.LastPoint)
      found = rect.Contains(gridpoint)
      if (found):
        break
    if (found):
      newIcon = copy.copy(room)
      newIcon.Index = len(gv.RoomList)
      newIcon.x += 1.0
      newIcon.y += 1.0
      if (room.trap):  #copy the trap record
        newIcon.trap = copy.copy(room.trap)
      elif(room.npc):  #copy the npc record
        newIcon.npc = copy.copy(room.npc)
      elif (room.monster):
        newIcon.monster = copy.copy(room.monster)
      gv.RoomList.append(newIcon)
      self.DrawMapWindow()
    return
  
  def RMapClickDeleteIcon(self, event=None):
    found = False
    for room in gv.RoomList:
      rect = wx.Rect(int(room.x * gv.MapZoomFactor),
                     int(room.y * gv.MapZoomFactor),
                     room.MapRect.width, room.MapRect.height)
      gridpoint = self.MapPanel.CalcUnscrolledPosition(gv.LastPoint)
      found = rect.Contains(gridpoint)
      if (found):
        break
    if (found):
      gv.RoomList.remove(room)
      self.DrawMapWindow()
    return

  def RMapClickAddSymbol(self, event):

    return
  
  def RMapAddIconNPC(self, event):
    monster = RoomInfo()
    dlg = Monsters5EDialog(self.frame, '5E_NPC')
    dlg.ID_OK.SetLabel("Select NPC")
    add_monster = dlg.ShowModal()
    if (add_monster) and (dlg.MonsterUniqueID != None):
      monster.Description =  dlg.txName.GetValue() #monster name
      point2 = self.MapPanel.ScreenToClient(gv.RightMousePoint)
      point3 = self.MapPanel.CalcUnscrolledPosition(point2)
      if (gv.SnapIconToGrid):
        monster.x = point3.x // (1.0*gv.MapZoomFactor)
        monster.y = point3.y // (1.0*gv.MapZoomFactor)
      else:
        monster.x = point3.x / (1.0*gv.MapZoomFactor)
        monster.y = point3.y / (1.0*gv.MapZoomFactor)
      monster.Icon = self.NPC_Icon
      monster.IconType = 'NPC'
      
      for m in gv.NPC_5E:
        if (m.uniqueID == dlg.MonsterUniqueID):
          monster.monster = copy.deepcopy(m)
          break
      
      if (monster.monster.filename):  #custom image associated with this NPC
        monster.monster.image = wx.Image(os.path.join(gv.tokens_directory, monster.monster.filename), wx.BITMAP_TYPE_ANY)
        if (not monster.monster.image.IsOk()):
          logging.error("Could not find custom monster image %s in the tokens folder", room.monster.filename)
          room.monster.image = None
          
      if (isinstance(m.size, int)):
        if ((m.size == 0) or (m.size == 1) or (m.size == 2)):
          monster.IconSize = 1
        elif (m.size == 3):
          monster.IconSize = 2
        elif (m.size == 4):
          monster.IconSize = 3
        elif (m.size == 5):
          monster.IconSize = 4
      else:
        monster.IconSize = 1
      pageindex = self.nbMapNotebook.GetSelection()
      monster.page = self.nbMapNotebook.GetPageText(pageindex)
      monster.placed = True
      monster.Layer = gv.ActiveLayer
      gv.RoomList.append(monster)
      self.UndoActionEvent(flag='ADD_ICON', icon=monster)
      dlg.Destroy()
      self.DrawMapWindow()
    return
  
  def RMapAddIconMonster(self, event):
    monster = RoomInfo()
    dlg = Monsters5EDialog(self.frame, '5E')
    dlg.ID_OK.SetLabel("Select Monster")
    add_monster = dlg.ShowModal()
    if (add_monster) and (dlg.MonsterUniqueID != None):
      monster.Description =  dlg.txName.GetValue() #monster name
      point2 = self.MapPanel.ScreenToClient(gv.RightMousePoint)
      point3 = self.MapPanel.CalcUnscrolledPosition(point2)
      if (gv.SnapIconToGrid):
        monster.x = point3.x // (1.0*gv.MapZoomFactor)
        monster.y = point3.y // (1.0*gv.MapZoomFactor)
      else: 
        monster.x = point3.x / (1.0*gv.MapZoomFactor)
        monster.y = point3.y / (1.0*gv.MapZoomFactor)
      monster.Icon = self.MonsterIcon
      monster.IconType = 'Monster'
      
      for m in gv.Monsters5E:
        if (m.uniqueID == dlg.MonsterUniqueID):
          monster.monster = copy.deepcopy(m)
          monster.monster.version = '5E'
          break
      
      if (monster.monster.filename):  #custom image associated with this monster
        monster.monster.image = wx.Image(os.path.join(gv.tokens_directory, monster.monster.filename), wx.BITMAP_TYPE_ANY)
        if (not monster.monster.image.IsOk()):
          logging.error("Could not find custom monster image %s in the tokens folder", monster.monster.filename)
          monster.monster.image = None

      pageindex = self.nbMapNotebook.GetSelection()
      monster.page = self.nbMapNotebook.GetPageText(pageindex)
      monster.placed = True
      if (isinstance(m.size, int)):
        if ((m.size == 0) or (m.size == 1) or (m.size == 2)):
          monster.IconSize = 1
        elif (m.size == 3):
          monster.IconSize = 2
        elif (m.size == 4):
          monster.IconSize = 3
        elif (m.size == 5):
          monster.IconSize = 4
      else:
        monster.IconSize = 1
      gv.RoomList.append(monster)
      self.UndoActionEvent(flag='ADD_ICON', icon=monster)
      dlg.Destroy()
      self.DrawMapWindow()
    return
  
  def RMapAddIconTrap(self, event):
    trap_info = RoomInfo()
    dlg = TrapsDialog(self.frame)
    dlg.ID_OK.SetLabel("Select Trap")
    dlg.bAddTrap.Show(False)
    dlg.bDeleteTrap.Show(False)
    dlg.bClearSelection.Show(False)
    dlg.bUpdateSelectedTrap.Show(False)
    result = dlg.ShowModal()
    if (result == True):
      trap_info.trap = dlg.selected_trap
      trap_info.IconType = 'Trap'
      trap_info.Icon = self.TrapIcon
      trap_info.Description =  dlg.txDescription.GetValue() #trap name
      point2 = self.MapPanel.ScreenToClient(gv.RightMousePoint)
      point3 = self.MapPanel.CalcUnscrolledPosition(point2)
      if (gv.SnapIconToGrid):
        trap_info.x = point3.x // (1.0*gv.MapZoomFactor)
        trap_info.y = point3.y // (1.0*gv.MapZoomFactor)
      else:
        trap_info.x = point3.x / (1.0*gv.MapZoomFactor)
        trap_info.y = point3.y / (1.0*gv.MapZoomFactor)
      pageindex = self.nbMapNotebook.GetSelection()
      trap_info.page = self.nbMapNotebook.GetPageText(pageindex)
      trap_info.placed = True
      gv.RoomList.append(trap_info)
      self.UndoActionEvent(flag='ADD_ICON', icon=trap_info)
      gv.RoomList.append(trap_info)
      self.DrawMapWindow()
    dlg.Destroy()
    return

  def RMapAddIconRoom(self, event=None, room=None):
    if (room == None):
      Room = RoomInfo()
      dlg = wx.TextEntryDialog(self.frame, message="Enter Room Description",
                               caption="Add Description", style=wx.OK|wx.CANCEL)
      if (dlg.ShowModal()==wx.ID_OK):
        Room.Description = dlg.GetValue()
        point2 = self.MapPanel.ScreenToClient(gv.RightMousePoint)
        point3 = self.MapPanel.CalcUnscrolledPosition(point2)
        if (gv.SnapIconToGrid):
          Room.x = point3.x // (1.0*gv.MapZoomFactor)
          Room.y = point3.y // (1.0*gv.MapZoomFactor)
        else:
          Room.x = point3.x / (1.0*gv.MapZoomFactor)
          Room.y = point3.y / (1.0*gv.MapZoomFactor)
          
        Room.Icon = self.RoomIcon
        pageindex = self.nbMapNotebook.GetSelection()
        Room.page = self.nbMapNotebook.GetPageText(pageindex)
        Room.placed = True
        gv.RoomList.append(Room)
        self.UndoActionEvent(flag='ADD_ICON', icon=Room)
        dlg.Destroy()
      else: 
        return
    else:
      Room = room
    if (event):
      frm = IconEditorFrame(par=self.frame, caption=Room.Description, room=Room, position=gv.RightMousePoint)
    else:
      point = room.windowPosition #wx.Point(int(room.x * gv.MapZoomFactor), int(room.y * gv.MapZoomFactor))
      #override the positioning if it would place the editor off the screen.  This can 
      #occur when multiple displays were used in creating the room, but then opened on
      #a single screen.
      displayRect = wx.Display().GetClientArea()
      if (point.x > displayRect.width) or (point.y > displayRect.height):
        point.x = 100
        point.y = 100
      frm = IconEditorFrame(par=self.frame, caption=Room.Description, room=Room, position=point)
    frm.Show()
    frm.Raise()
    gv.rtc_open = True
    gv.rtc_icon = Room  #this is the current active icon; the RoomInfo class
    self.DrawMapWindow()
    return

  def OnMapRightClick(self, event):
    if (self.TileInMotion):
      return
    self.DisplayHoverInformation(False)  #clear any hover display
    self.hovertimer.Stop() #suspend hovertimer

    gv.RightMousePoint = event.GetPosition()
    gridpoint = self.MapPanel.CalcUnscrolledPosition(event.GetPosition())
    foundtile = False
    point = wx.Point2D(gridpoint.x, gridpoint.y)
    if (gv.SelectMode == 'icon'):
      for label in self.textlist:
        found = label.extent.Contains(point)
        if (found == True):
          label.selected = True
          break
    else:
      for tile in self.maplist:
        if (tile.selected):
          foundtile = True
          break

    menu = wx.Menu()
    icon_menu = wx.Menu()
    rotate_menu = wx.Menu()
    order_menu = wx.Menu()
    symbol_menu = wx.Menu()
    icon_menu = wx.Menu()
    self.layer_menu = wx.Menu()
    
    #build the icon submenu

    IconSubmenu = wx.Menu()
    item31 = wx.MenuItem(IconSubmenu, self.popupID31, "NPC")
    item32 = wx.MenuItem(IconSubmenu, self.popupID32, "Room")
    item33 = wx.MenuItem(IconSubmenu, self.popupID33, "Monster")
    item35 = wx.MenuItem(IconSubmenu, self.popupID35, "Trap")
    
    bmp31 = wx.Bitmap(os.path.join(gv.artwork_directory,"npc_icon_small.png"), wx.BITMAP_TYPE_PNG)
    item31.SetBitmap(bmp31)
    bmp32 = wx.Bitmap(os.path.join(gv.artwork_directory,"scroll_icon.png"), wx.BITMAP_TYPE_PNG)
    item32.SetBitmap(bmp32)
    bmp33 = wx.Bitmap(os.path.join(gv.artwork_directory,"monster_icon_small.png"), wx.BITMAP_TYPE_PNG)
    item33.SetBitmap(bmp33)
    bmp35 = wx.Bitmap(os.path.join(gv.artwork_directory,"trap.png"), wx.BITMAP_TYPE_PNG)
    item35.SetBitmap(bmp35)
    
    self.Bind(wx.EVT_MENU, self.RMapAddIconNPC, id=self.popupID31)
    self.Bind(wx.EVT_MENU, self.RMapAddIconRoom, id=self.popupID32)
    self.Bind(wx.EVT_MENU, self.RMapAddIconMonster, id=self.popupID33)
    self.Bind(wx.EVT_MENU, self.RMapAddIconTrap, id=self.popupID35)
    
    if (gv.DnD_5E_data_available):
      IconSubmenu.AppendItem(item32)
      IconSubmenu.AppendItem(item33)
      IconSubmenu.AppendItem(item31)
      IconSubmenu.AppendItem(item35)
    else: #(not gv.DnD_5E_data_available):
      item32.SetItemLabel("5E Dungeon data not available")
      IconSubmenu.AppendItem(item32)
      IconSubmenu.Enable(self.popupID32, False)
    menu.AppendSubMenu(IconSubmenu, "Add DnD 5E Information Icon...")

    #build the symbol submenu
    if (gv.SelectMode == 'icon'):
      mouse_pos = event.GetPosition()
      screenpoint = self.MapPanel.CalcUnscrolledPosition(mouse_pos)
      point2 = self.MapPanel.ScreenToClient(screenpoint)
      for room in gv.RoomList:
        rect = wx.Rect(int(room.x * gv.MapZoomFactor), int(room.y * gv.MapZoomFactor),room.MapRect.width, room.MapRect.height)
        found = rect.Contains(point2)
        if (found):
          item16 = wx.MenuItem(menu, self.popupID16,"Delete Icon")
          bmp16 = wx.Bitmap(os.path.join(gv.artwork_directory,"DeleteIcon.png"), wx.BITMAP_TYPE_PNG)
          item16.SetBitmap(bmp16)
          item18 = wx.MenuItem(menu, self.popupID18, "Copy Icon")
          bmp18 = wx.Bitmap(os.path.join(gv.artwork_directory, "clipboard copy.png"), wx.BITMAP_TYPE_PNG)
          item18.SetBitmap(bmp18)
          menu.AppendItem(item16)  #add the 'Delete Icon' sub-menu only if an icon was found
          menu.AppendItem(item18)  #add the 'Copy Icon' item only if an icon was found
          ColorSubmenu = wx.Menu()
          item20 = wx.MenuItem(ColorSubmenu, self.popupID20, "Red")
          item21 = wx.MenuItem(ColorSubmenu, self.popupID21, "Blue")
          item22 = wx.MenuItem(ColorSubmenu, self.popupID22, "Green")
          item23 = wx.MenuItem(ColorSubmenu, self.popupID23, "Yellow")
          item24 = wx.MenuItem(ColorSubmenu, self.popupID24, "Purple")
          bmp20 = wx.Bitmap(os.path.join(gv.artwork_directory,"ChangeHighlightRed.png"), wx.BITMAP_TYPE_PNG)
          bmp21 = wx.Bitmap(os.path.join(gv.artwork_directory,"ChangeHighlightBlue.png"), wx.BITMAP_TYPE_PNG)
          bmp22 = wx.Bitmap(os.path.join(gv.artwork_directory,"ChangeHighlightGreen.png"), wx.BITMAP_TYPE_PNG)
          bmp23 = wx.Bitmap(os.path.join(gv.artwork_directory,"ChangeHighlightYellow.png"), wx.BITMAP_TYPE_PNG)
          bmp24 = wx.Bitmap(os.path.join(gv.artwork_directory,"ChangeHighlightPurple.png"), wx.BITMAP_TYPE_PNG)
          item20.SetBitmap(bmp20)
          item21.SetBitmap(bmp21)
          item22.SetBitmap(bmp22)
          item23.SetBitmap(bmp23)
          item24.SetBitmap(bmp24)
          self.Bind(wx.EVT_MENU, self.RMapClickChangeIconHighlight, id=self.popupID20)
          self.Bind(wx.EVT_MENU, self.RMapClickChangeIconHighlight, id=self.popupID21)
          self.Bind(wx.EVT_MENU, self.RMapClickChangeIconHighlight, id=self.popupID22)
          self.Bind(wx.EVT_MENU, self.RMapClickChangeIconHighlight, id=self.popupID23)
          self.Bind(wx.EVT_MENU, self.RMapClickChangeIconHighlight, id=self.popupID24)
          
          ColorSubmenu.AppendItem(item20)
          ColorSubmenu.AppendItem(item21)
          ColorSubmenu.AppendItem(item22)
          ColorSubmenu.AppendItem(item23)
          ColorSubmenu.AppendItem(item24)
          menu.AppendSubMenu(ColorSubmenu, "Change Highlight Color:")
          break

    item = wx.MenuItem(menu, self.popupID1,"Zoom In")
    bmp1 = wx.Bitmap(os.path.join(gv.artwork_directory,"ZoomIn.png"), wx.BITMAP_TYPE_PNG)
    item.SetBitmap(bmp1)
    menu.AppendItem(item)
    # add some other items
    bmp2 = wx.Bitmap(os.path.join(gv.artwork_directory,"ZoomOut.png"), wx.BITMAP_TYPE_PNG)
    item2 = wx.MenuItem(menu, self.popupID2, "Zoom Out")
    item2.SetBitmap(bmp2)
    menu.AppendItem(item2)
    item6 = wx.MenuItem(menu, self.popupID6, "Show All")
    bmp6 = wx.Bitmap(os.path.join(gv.artwork_directory,"select_all.png"), wx.BITMAP_TYPE_PNG)
    item6.SetBitmap(bmp6)
    menu.AppendItem(item6)
    item7 = wx.MenuItem(menu, self.popupID7, "Add Text...")
    bmp7 = wx.Bitmap(os.path.join(gv.artwork_directory,"text_icon.png"), wx.BITMAP_TYPE_PNG)
    item7.SetBitmap(bmp7)
    menu.AppendItem(item7)
    if (gv.SelectMode == 'tile'):
      if (self.maplist != []):
        item3 = wx.MenuItem(menu, self.popupID3, "Delete Tile")
        bmp3 = wx.Bitmap(os.path.join(gv.artwork_directory,"DeleteIcon.png"), wx.BITMAP_TYPE_PNG)
        item3.SetBitmap(bmp3)
        menu.AppendItem(item3)
      bmp4 = wx.Bitmap(os.path.join(gv.artwork_directory,"RotateRight.png"), wx.BITMAP_TYPE_PNG)
      bmp5 = wx.Bitmap(os.path.join(gv.artwork_directory,"RotateLeft.png"), wx.BITMAP_TYPE_PNG)
      bmp6 = wx.Bitmap(os.path.join(gv.artwork_directory,"Rotate180.png"), wx.BITMAP_TYPE_PNG)
      item4 = wx.MenuItem(menu, self.popupID4, "Rotate Right")
      item5 = wx.MenuItem(menu, self.popupID5, "Rotate Left")
      item13 = wx.MenuItem(menu, self.popupID13, "Rotate 180")
      item4.SetBitmap(bmp4)
      item5.SetBitmap(bmp5)
      item13.SetBitmap(bmp6)
      rotate_menu.AppendItem(item4)
      rotate_menu.AppendItem(item5)
      rotate_menu.AppendItem(item13)
      menu.AppendSubMenu(rotate_menu, "Rotate Tile:")

      bmp9 = wx.Bitmap(os.path.join(gv.artwork_directory,"MoveUp.png"), wx.BITMAP_TYPE_PNG)
      bmp10 = wx.Bitmap(os.path.join(gv.artwork_directory,"MoveTop.png"), wx.BITMAP_TYPE_PNG)
      bmp11 = wx.Bitmap(os.path.join(gv.artwork_directory,"MoveDown.png"), wx.BITMAP_TYPE_PNG)
      bmp12 = wx.Bitmap(os.path.join(gv.artwork_directory,"MoveBottom.png"), wx.BITMAP_TYPE_PNG)
      item9 = wx.MenuItem(menu, self.popupID9, "Move Up")
      item10 = wx.MenuItem(menu, self.popupID10, "Move to Top")
      item11 = wx.MenuItem(menu, self.popupID11, "Move Down")
      item12 = wx.MenuItem(menu, self.popupID12, "Move to Bottom")
      item9.SetBitmap(bmp9)
      item10.SetBitmap(bmp10)
      item11.SetBitmap(bmp11)
      item12.SetBitmap(bmp12)
      order_menu.AppendItem(item10)
      order_menu.AppendItem(item9)
      order_menu.AppendItem(item11)
      order_menu.AppendItem(item12)
      menu.AppendSubMenu(order_menu, "Display Order:")

      if (not foundtile):
        item4.Enable(False)
        item5.Enable(False)
        item9.Enable(False)
        item10.Enable(False)
        item11.Enable(False)
        item12.Enable(False)
        item13.Enable(False)

    if (gv.SelectMode == 'icon'):
      item8 = wx.MenuItem(menu, self.popupID8, "Edit Text Properties...")
      menu.AppendItem(item8)

    gv.templist = []
    for layer in gv.LayerList:
      var = wx.Window.NewControlId()
      gv.templist.append(var)
      self.Bind(wx.EVT_MENU, self.RMapClickAssignLayer, id=var)
      self.layer_menu.Append(var, layer.name)
    menu.AppendSubMenu(self.layer_menu, "Assign Layer:")

    #make a submenu
    #sm = wx.Menu()
    #sm.Append(self.popupID9, "sub item 1")
    #sm.Append(self.popupID10, "sub item 2")
    #menu.AppendMenu(self.popupID7, "Test Submenu", sm)
    #wx.EVT_MENU(menu, 'ZoomIn', self.MenuSelectionCb)

    self.MapPanel.PopupMenu(menu)
    menu.Destroy()
    self.hovertimer.Start()
    return

  def CalculateMapExtents(self, tilelist):
    """Returns a wxRect with the grid coordinates of the map limits"""
    if (self.MapStruct.geomorph):
      return wx.Rect(0,0,16,18)
    else:
      rect = wx.Rect(10000,10000,0,0)
      for tile in tilelist:
        gridX = tile.MapRect.x
        gridY = tile.MapRect.y
        Xgridsize = tile.MapRect.width + gridX
        Ygridsize = tile.MapRect.height + gridY
        if (rect.width < Xgridsize):
          rect.width = Xgridsize
        if (rect.height < Ygridsize):
          rect.height = Ygridsize
        if (rect.x > gridX):
          rect.x = gridX
        if (rect.y > gridY):
          rect.y = gridY

      text = Annotation()
      for text in self.textlist:
        gridX = (text.extent.x/gv.MapZoomFactor) #text extent is in pixels
        gridY = (text.extent.y/gv.MapZoomFactor)
        Xgridsize = (text.extent.width/gv.MapZoomFactor) + gridX
        Ygridsize = (text.extent.height/gv.MapZoomFactor) + gridY
        if (rect.width < Xgridsize):
          rect.width = Xgridsize
        if (rect.height < Ygridsize):
          rect.height = Ygridsize
        if (rect.x > gridX):
          rect.x = gridX
        if (rect.y > gridY):
          rect.y = gridY

      rect.width -= rect.x
      rect.height -= rect.y
      return rect

  def RMapClickEditTextFontData(self, event):
    for label in self.textlist:
      if (label.selected == True):
        dlg = TextOptionsDialogCore(self.frame, False, label)
        if (dlg.ShowModal() == True):
          label.bg = dlg.BackgroundColor
          label.fg = dlg.ForegroundColor
          label.font = dlg.TextFont
          #label.fontdata = dlg.FontData
          label.opaque = dlg.rbOpaque.GetValue()
          label = self.CreateTextLabelBitmap(label, gv.MapZoomFactor)
          self.DrawMapWindow()

  def RMapClickDisplayUp(self, event):
    self.MoveUpDisplayOrder('SINGLE')
    return
  def RMapClickDisplayTop(self, event):
    self.MoveUpDisplayOrder('TOP')
    return
  def RMapClickDisplayDown(self, event):
    self.MoveDownDisplayOrder('SINGLE')
    return
  def RMapClickDisplayBottom(self, event):
    self.MoveDownDisplayOrder('BOTTOM')
    return

  def RMapClickAssignLayer(self, event):
    if (self.selectlist == []):
      return
    for layer in gv.LayerList:
      if (event.GetId() == layer.index):
        self.selectlist[0].layer = lyaer.index
        break
    return

  def UpdateLayerMenu(self, event):
    return

  def RMapClickAddText(self, event):
    point2 = self.MapPanel.ScreenToClient(gv.RightMousePoint)
    point3 = self.MapPanel.CalcUnscrolledPosition(point2)
    dlg = wx.TextEntryDialog(self.frame, "Enter Text Annotation", "Text:")
    result = dlg.ShowModal()
    if (result == wx.ID_OK):
      label = Annotation()
      label.text = dlg.GetValue()
      label.x = point3.x / (1.0*gv.MapZoomFactor)
      label.y = point3.y / (1.0*gv.MapZoomFactor)
      label.point = point3
      label.fg = gv.TextForegroundColor
      label.bg = gv.TextBackgroundColor
      label.font = gv.TextFont
      #label.fontdata = gv.FontData
      label.opaque = gv.OpaqueBackground
      label.zoomfactor = gv.MapZoomFactor
      index = self.nbMapNotebook.GetSelection()
      label.page = self.nbMapNotebook.GetPageText(index)
      label = self.CreateTextLabelBitmap(label, gv.MapZoomFactor)
      self.UndoActionEvent(flag='ADD_TEXT', text=label)
      self.textlist.append(label)
      self.DrawMapWindow()
    dlg.Destroy()
    return

  def RMapClickShowAll(self, event=None):
    """Must call self.DrawMapWindow() after this function"""
    self.MapStruct.GridExtents = self.CalculateMapExtents(self.maplist)
    MPsize = self.MapPanel.GetSize()
    zf1 = (1.0*MPsize.GetWidth())/(1.0*(self.MapStruct.GridExtents.GetWidth()+1))
    zf2 = (1.0*MPsize.GetHeight())/(1.0*(self.MapStruct.GridExtents.GetHeight()+1))
    #zf1 = (1.0*MPsize.GetWidth())/(1.0*(self.MapStruct.GridExtents.GetX()))
    #zf2 = (1.0*MPsize.GetHeight())/(1.0*(self.MapStruct.GridExtents.GetY()))

    zf3 = int(min(zf1, zf2))
    gv.MapZoomFactor = (min(100, zf3))
    if (gv.MapZoomFactor == 0):
      gv.MapZoomFactor = 25
    self.frame.MapWindowZoomSlider.SetValue(gv.MapZoomFactor)
    gv.MapOffset.x = self.MapStruct.GridExtents.GetX() * gv.MapZoomFactor
    gv.MapOffset.y = self.MapStruct.GridExtents.GetY() * gv.MapZoomFactor
    #regenerate map display images
    for tile in self.maplist:
      tile.GenerateMapDisplay(gv.MapZoomFactor)
      
    PixelsPerUnit = self.MapPanel.GetScrollPixelsPerUnit()
    self.MapPanel.Scroll(gv.MapOffset.x*PixelsPerUnit[0], gv.MapOffset.y*PixelsPerUnit[1])
    return

  def RMapClickZoomIn(self, event):
    gv.MapZoomFactor = gv.MapZoomFactor + gv.MapZoomIncrement
    self.DrawMapWindow()
    return

  def RMapClickDeleteTile(self,event):
    for tile in self.maplist:
      if (tile.selected):
        self.DeleteMapTile(tile)
        self.MapStruct.GridExtents = self.CalculateMapExtents(self.maplist)
        self.DrawMapWindow()
        break
    return

  def RMapClickZoomOut(self, event):
    gv.MapZoomFactor = gv.MapZoomFactor - gv.MapZoomIncrement
    if (gv.MapZoomFactor < 1):
      gv.MapZoomFactor = 5
    self.MapStruct.GridExtents = self.CalculateMapExtents(self.maplist)
    self.DrawMapWindow()
    return

  def RMapClickRotateCW(self, event):
    for tile in self.maplist:
      if (tile.selected):
        tile = self.ChangeTileRotation(tile, 'CW')
        break
    self.MapStruct.GridExtents = self.CalculateMapExtents(self.maplist)
    self.DrawMapWindow()
    return

  def RMapClickRotateCCW(self, event):
    for tile in self.maplist:
      if (tile.selected):
        tile = self.ChangeTileRotation(tile, 'CCW')
        break
    self.MapStruct.GridExtents = self.CalculateMapExtents(self.maplist)
    self.DrawMapWindow()
    return

  def RMapClickRotate180(self, event):
    for tile in self.maplist:
      if (tile.selected):
        tile = self.ChangeTileRotation(tile, 'CCW')
        tile = self.ChangeTileRotation(tile, 'CCW')
        break
    self.MapStruct.GridExtents = self.CalculateMapExtents(self.maplist)
    self.DrawMapWindow()
    return

  def ReadTilesetFile(self, filename, RelativePath=False):
    tilesetVersion = None  #read from TILESET tag
    """ PageList is the list of page names where this tileset will display on"""
    if (RelativePath == True):
      filename = os.path.join(gv.tiles_directory,filename)

    #check this tileset against the list and exit if trying to load the same set twice
    for item in gv.tilesets:
      if (item.filename == filename) and (item.loaded):
        #found a set already loaded
        return
    try:
      setfile = open(filename, 'r')
    except IOError:
      #attempt to extract the filename and set folder from the filename
      path1,setFilename = os.path.split(filename)
      oldpath,tileFolder = os.path.split(path1)
      newPath = os.path.join(gv.tiles_directory,tileFolder,setFilename)
      try:
        setfile = open(newPath, 'r')
        logging.info("PymapperAppMain::ReadTilesetFile found alternate location for tileset %s",filename)
      except IOError:
        logging.error("PymapperAppMain::ReadTilesetFile: could not open Tileset %s", filename)
        return False
    header = True
    delta = 0
    progress = wx.ProgressDialog("Loading Tileset", str(filename), maximum=100, parent=self.frame, style=wx.PD_APP_MODAL | wx.PD_AUTO_HIDE | wx.PD_SMOOTH)
    if (gv.StartupOffset):
      offset_pt = wx.Point(gv.StartupOffset.GetX()+gv.StartupOffset.GetWidth(),
                           gv.StartupOffset.GetY())
      progress.Move(offset_pt)
    progress.Update(delta)
    line = setfile.readline()
    line = line.rstrip('\n\r')
    info = line.split()

    while (header == True):
      if (info[0] == '#'):
        #reading comment lines
        line = setfile.readline()
        info = line.split()
      elif (info[0] != '#'):
        header = False
    if (info[0] != 'TILESET'):
      '''Not a tileset file'''
      logging.error("PymapperAppMain::ReadTilesetFile: invalid tileset file format in %s, ",filename)
      progress.Update(100)
      setfile.close()
      return False
    else:
      read_file = True
      newtile = Tile()
      tileset = TileSet()
      while (read_file == True):
        delta += 2
        if (delta > 100):
          delta = 99
        progress.Update(delta)
        line = setfile.readline()
        line = line.rstrip('\n\r')
        info = line.split()
        if (info == []):
          #read an empty line, continue on to the next line
          pass
        elif (info[0] == 'VERSION'):
          tilesetVersion = float(info[1])
        elif (info[0] == 'SET_ID'):
          tileset.SetID = info[1]
          if (self.CheckDuplicateTileset(info[1])):
            #duplicate tileset, don't continue loading
            progress.Update(100)
            setfile.close()
            return True
          else:
            newtile.tilesetID = info[1]
        elif ((info[0] == '#') or (info[0] == [])):
          #comment line, or an empty line, skip reading
          continue
        elif (info[0] == 'NAME'):
          info.pop(0) #remove the tag
          tileset.Name = info[0]
          info.pop(0)
          while (len(info) > 0):
            tileset.Name += " "
            tileset.Name += info[0]
            info.pop(0)
        elif (info[0] == 'NUM_SETS'):
          tileset.copies = int(info[1])
        elif (info[0] == "TILE"):
          newtile.tileID = int(info[1])
          read_tile = True
          while (read_tile == True):
            line = setfile.readline()
            info = line.split()
            if (info == []):
              logging.error("PymapperAppMain::ReadTilesetFile:  TILE tag not found")
              progress.Update(100)
              return False
            elif info[0] == 'IMAGE_A':
              #the filename may have spaces, so need to join all the elements
              name = ""
              count = 1
              for i in info:
                if i == info[0]:
                  continue
                elif i == info[1]:
                  name = i
                else:
                  name = name + " " + i
              if (tilesetVersion == None):
                #tilesets saved previous to tileset version 2.0 (pymapper version 9.4) include a leading \ on the pathname
                #this results in the incorrect path join (assumes an absolute path)
                name = name.lstrip("\\")  #in case of the win32 version .set files
                name = name.lstrip("/")   #in case of the mac version .set files
              
              newtile.filenameA = os.path.join(gv.root_directory,name)
              newtile.filenameA = os.path.normpath(newtile.filenameA)
              newtile.sideA = wx.Image(newtile.filenameA, wx.BITMAP_TYPE_ANY)
              if (not newtile.sideA.IsOk()):
                logging.error("PymapperAppMain::ReadTilesetError:  Could not open side A filename: %s", newtile.filenameA)
                logging.error("PymapperAppMain::ReadTilesetError:  gv.root_directory = %s", gv.root_directory)
                logging.error("PymapperAppMain::ReadTilesetError:  filename = %s", name)
                newtile.sideA = self.ImageNotFound
            elif info[0] == 'NO_IMAGE_B':
              newtile.sideB = None
              newtile.filenameB = None
            elif info[0] == 'IMAGE_B':
              name = ""
              count = 1
              for i in info:
                if i == info[0]:
                  continue
                elif i == info[1]:
                  name = i
                else:
                  name = name + " " + i
              if (tilesetVersion == None):
                #tilesets saved previous to tileset version 2.0 (pymapper version 9.4) include a leading \ on the pathname
                #this results in the incorrect path join (assumes an absolute path)
                name = name.lstrip("\\")  #in case of the win32 version .set files
                name = name.lstrip("/")   #in case of the mac version .set files
              newtile.filenameB = os.path.join(gv.root_directory,name)
              newtile.filenameB = os.path.normpath(newtile.filenameB)
              newtile.sideB = wx.Image(newtile.filenameB, wx.BITMAP_TYPE_ANY)
              if (not newtile.sideB.IsOk()):
                logging.error("PymapperAppMain::ReadTilesetError:  Could not open side B filename: %s",newtile.filenameB)
                logging.error("PymapperAppMain::ReadTilesetError:  gv.root_directory = %s", gv.root_directory)
                logging.error("PymapperAppMain::ReadTilesetError:  filename = %s", name)
                newtile.sideB = self.ImageNotFound
            elif info[0] == 'XSIZE':
              newtile.actualXsize = int(info[1])
            elif info[0] == 'YSIZE':
              newtile.actualYsize = int(info[1])
            elif (info[0] == 'RANDOM_DUNGEON_TAGS'):
              info.pop(0)
              for data in info:
                newtile.random_def.append(data)
            elif (info[0] == 'TILE_NAME'):
              info.pop(0)
              newtile.tilenameA = info[0]
              newtile.tilenameB = info[0]
              info.pop(0)
              while (len(info) > 0):
                newtile.tilenameA += " "
                newtile.tilenameA += info[0]
                newtile.tilenameB += " "
                newtile.tilenameB += info[0]
                info.pop(0)
            elif (info[0] == 'TILE_NAME_A'):
              info.pop(0)
              newtile.tilenameA = info[0]
              info.pop(0)
              while (len(info) > 0):
                newtile.tilenameA += " "
                newtile.tilenameA += info[0]
                info.pop(0)
            elif (info[0] == 'TILE_NAME_B'):
              info.pop(0)
              newtile.tilenameB = info[0]
              info.pop(0)
              while (len(info) > 0):
                newtile.tilenameB += " "
                newtile.tilenameB += info[0]
                info.pop(0)
            elif (info[0] == 'FILTER_TAGS'):
              info.pop(0)
              newtile.taglist = []
              while (len(info) > 0):
                newtile.taglist.append(str(info[0]))
                info.pop(0)
            elif info[0] == 'ROTATION':
              newtile.rotation = int(info[1])
            elif info[0] == 'TILE_COUNT':
              newtile.count = int(info[1])
            elif (info[0] == 'TOP_EDGE_A'):
              newtile.TopEdgeA = []
              line = setfile.readline()
              newtile.TopEdgeA = line.split()
              newtile.random_defA = True
            elif (info[0] == 'BOTTOM_EDGE_A'):
              newtile.BottomEdgeA = []
              line = setfile.readline()
              newtile.BottomEdgeA = line.split()
              newtile.random_defA = True
            elif (info[0] == 'RIGHT_EDGE_A'):
              newtile.RightEdgeA = []
              line = setfile.readline()
              newtile.RightEdgeA = line.split()
              newtile.random_defA = True
            elif (info[0] == 'LEFT_EDGE_A'):
              newtile.LeftEdgeA = []
              line = setfile.readline()
              newtile.LeftEdgeA = line.split()
              newtile.random_defA = True
            elif (info[0] == 'TOP_EDGE_B'):
              newtile.TopEdgeB = []
              line = setfile.readline()
              newtile.TopEdgeB = line.split()
              newtile.random_defB = True
            elif (info[0] == 'BOTTOM_EDGE_B'):
              newtile.BottomEdgeB = []
              line = setfile.readline()
              newtile.BottomEdgeB = line.split()
              newtile.random_defB = True
            elif (info[0] == 'RIGHT_EDGE_B'):
              newtile.RightEdgeB = []
              line = setfile.readline()
              newtile.RightEdgeB = line.split()
              newtile.random_defB = True
            elif (info[0] == 'LEFT_EDGE_B'):
              newtile.LeftEdgeB = []
              line = setfile.readline()
              newtile.LeftEdgeB = line.split()
              newtile.random_defB = True
            elif info[0] == 'ENDTILE':
              read_tile = False
              newtile.tilesetID = tileset.SetID
              newtile.tilesetName = tileset.Name
              #set the rest of the params
              newtile.shown = True
              newtile.sort = False
              newtile.text = None
              newtile.mapdisplay = None # No tile set to the MapPanel yet
              newtile.tiledisplay = newtile.sideA
              newtile.showingBside = False
              newtile.key_index = gv.key_index
              gv.key_index += 1
              newtile.copies = (tileset.copies * newtile.count)  #total num available
              if (newtile.sideA == None):
                logging.error("Could not find sideA image")
                newtile.sideA = self.ImageNotFound
              if (newtile.sideB == None) and (newtile.filenameB != None):
                logging.error("Could not find sideB image")
                newtile.sideB = self.ImageNotFound
              self.tilelist.append(newtile)
              newtile = Tile()
        elif info[0] == "END":
          tileset.filename = filename
          if (gv.TileImportLocation == 'NewPage'):
            self.RTilebookAddPage(name=tileset.Name)
            gv.TilePageList[len(gv.TilePageList)-1].tilesets.append(tileset.Name)
          else:
            gv.TilePageList[self.nbTileNotebook.GetSelection()].tilesets.append(tileset.Name)
          tileset.loaded = True
          tileset.delete = False
          read_file = False
          add_set = True
          for item in gv.tilesets:
            if (tileset.SetID == item.SetID):
              #the tileset is in the list; update the list
              item.loaded = True
              add_set = False
              break
          if (add_set):
            #a new tileset was loaded
            gv.tilesets.append(tileset)
        else:
          setfile.close()
          logging.error("ReadTilesetFile reached end of tileset file without reading END tag:  tileset = %s", tileset.SetID)
          progress.Update(100)
          return False
    progress.Update(100)
    setfile.close()
    return True

  def ScrollMapPanelTop(self, event):
    event.Skip()
    pass

  def ScrollMapPanelBottom(self,event):
    event.Skip()
    pass

  def ScrollMapPanelLineup(self, event):
    if (event.GetOrientation() == wx.HORIZONTAL):
      self.ChangeMapOffset("x_pos", gv.ScrollIncrement)
    if (event.GetOrientation() == wx.VERTICAL):
      self.ChangeMapOffset("y_pos", gv.ScrollIncrement)
    event.Skip()
    return

  def ScrollMapPanelLinedown(self, event):
    if (event.GetOrientation() == wx.HORIZONTAL):
      self.ChangeMapOffset("x_neg", gv.ScrollIncrement)
    if (event.GetOrientation() == wx.VERTICAL):
      self.ChangeMapOffset("y_neg", gv.ScrollIncrement)
    event.Skip()
    return

  def ScrollMapPanelPageup(self, event):
    if (event.GetOrientation() == wx.HORIZONTAL):
      self.ChangeMapOffset("x_pos", gv.ScrollIncrement*gv.MapZoomFactor)
    if (event.GetOrientation() == wx.VERTICAL):
      self.ChangeMapOffset("y_pos", gv.ScrollIncrement*gv.MapZoomFactor)
    event.Skip()
    return

  def ScrollMapPanelPagedown(self, event):
    if (event.GetOrientation() == wx.HORIZONTAL):
      self.ChangeMapOffset("x_neg", gv.ScrollIncrement*gv.MapZoomFactor)
    if (event.GetOrientation() == wx.VERTICAL):
      self.ChangeMapOffset("y_neg", gv.ScrollIncrement*gv.MapZoomFactor)
    event.Skip()
    return

  def ScrollMapPanelThumbtrack(self, event):
    event.Skip()
    return

  def ScrollMapPanelThumbrelease(self, event):
    if (event.GetOrientation() == wx.HORIZONTAL):
      gv.MapOffset.x = event.GetPosition()
    if (event.GetOrientation() == wx.VERTICAL):
      gv.MapOffset.y = event.GetPosition()
    event.Skip()
    return

  def RollDice(self, rollString):
    """combo is equivalent to 3d6, or 1d12+5.  Returns an integer
    Format for combo is NdSxM+A
    The format is NdSxM+A where:
    N = Number of times to roll the dice (required)
    d = Dice separator (required)
    S = Number of sides on the die (required)
    x = Multiplier separator (optional)
    M = Multiplier after all of the dice have been rolled (optional, defaults to 1 if no value given)
    + = Additive separator, may also be - (minus sign) (optional)
    A = Additive modifier added after dice are rolled and multiplied (optional, defaults to 0 if no value given)
    """
    #Check for additive modifier
    Additive_modifier = 0
    if ('+' in rollString):
      combo = rollString.split("+")
      sign = 1
    elif ('-' in rollString):
      combo = rollString.split("-")
      sign = -1
    else:
      combo = rollString.split(" ")
    if (len(combo) > 1):
      if (combo[1] != ''):
        try:
          Additive_modifier = int(combo[1]) * sign
        except:
          Additive_modifier = 0
      else:
        Additive_modifier = 0
    
    #check for multiplication modifier
    Multiply_modifier = 1
    if ('x' in combo[0]):
      combo = combo[0].split("x")
      if (len(combo) > 1):
        Multiply_modifier = int(combo[1])
      else:
        Multiply_modifier = 1
    
    #determine number of throws, and number of dice sides
    combo = combo[0].split("d")
    if (combo[0].isdigit()):
      throws = int(combo[0])
    else:
      logging.error("RollDice could not roll %s",combo[0])
      return 0
    
    if (combo[1].isdigit()):
      sides = int(combo[1])
    else:
      logging.error("RollDice could not roll %s",combo[0])
      return 0

    rolling = True
    count = 0
    result = 0
    while (rolling):
      result += random.randint(1,sides)
      count += 1
      if (count == throws):
        rolling = False
        
    result *= Multiply_modifier
    result += Additive_modifier
    return result

if __name__ == '__main__':
  app = PyMapperAppMain(0)
  gv.PyMapperApp = app
  app.MainLoop()
  #profile.run('app.MainLoop()', 'speed_profiles.txt')
