#-----------------------------------------------------------------------------
# Name:        fog.py
# Purpose:     simple raytracing for determination of fog-of-war effects for 
#              pymapper program
#
# Author:      Michael Seely, P.E.
#
# Created:     2012/06/12
# RCS-ID:      $Id: fog.py $
# Copyright:   (c) 2012 Michael S Seely, P.E.
# Licence:     Gnu General Public License v3
#-----------------------------------------------------------------------------

from __future__ import division

import wx
import os
import global_vars as gv
import PyMapperDialogs as PyMapperDialogs

FogToolsDialog = None  #reference to the fog tools dialog instance

class FogToolsDialogCore(PyMapperDialogs.FogToolsDialogBase):
  def __init__(self, parent):
    olddir = os.getcwd()
    os.chdir(gv.root_directory)
    PyMapperDialogs.FogToolsDialogBase.__init__(self, parent)
    os.chdir(olddir)
    self.current_tool = None
    self.oldtool = None
    self.PenStyle = wx.SOLID
    self.BrushStyle = wx.BLACK_BRUSH
    self.spAddBrushRadius.SetValue(gv.FogAddBrushRadius)
    self.spAddBrushRadius.SetValue(gv.FogRemoveBrushRadius)
    if (gv.SecondaryScreen):
      self.bUpdateFog.Enable(True)
      self.bUpdateFogOnline.Enable(True)
    else:
      self.bUpdateFog.Enable(False)
      self.bUpdateFogOnline.Enable(False)
    return
  
  def OnUpdateFog(self, event):
    if (gv.SecondaryScreen):
      gv.SecondaryScreen.UpdateImage()
    return
  
  def OnUpdateFogOnline(self, event):
    if (gv.SecondaryScreen):
      gv.SecondaryScreen.UpdateFTP()
    return
  
  def OnShowSecondary(self, event):
    if (gv.SecondaryScreen):
      gv.SecondaryScreen.Raise()
    else:
      gv.PyMapperApp.OnViewSecondaryScreen()
      self.bUpdateFog.Enable(True)
      self.bUpdateFogOnline.Enable(True)
    return
  
  def ChangeMapFogDensity(self, event):
    value = self.slMapFogDensity.GetValue()
    gv.MainFogDensity = value/255
    gv.PyMapperApp.DrawMapWindow()
    return
  
  def ChangeToolBitmaps(self, newtool):
    if (self.oldtool == 'Fog_Select'):
      self.bSelectItem.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_select.png'), wx.BITMAP_TYPE_PNG))
    elif (self.oldtool == 'Fog_EraseFreehand'):
      self.bEraseFog.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'fog_eraser.png'), wx.BITMAP_TYPE_PNG))
    elif (self.oldtool == 'Fog_FillCircle'):
      self.bDrawFilledCircle.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'fog_filled_circle.png'), wx.BITMAP_TYPE_PNG))
    elif (self.oldtool == 'Fog_FillRect'):
      self.bDrawFilledRectangle.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'fog_filled_rectangle.png'), wx.BITMAP_TYPE_PNG))
    elif (self.oldtool == 'Fog_Line'):
      self.bDrawLine.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_line.png'), wx.BITMAP_TYPE_PNG))
    elif (self.oldtool == 'Fog_Multiline'):
      self.bDrawMultiline.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_line_segments.png'), wx.BITMAP_TYPE_PNG))
    elif (self.oldtool == 'Fog_AddFreehand'):
      self.bAddFog.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'fog_brush.png'), wx.BITMAP_TYPE_PNG))
    elif (self.oldtool == 'Fog_AddGenericLight'):
      self.bAddLightSource.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'fog_generic_light.png'), wx.BITMAP_TYPE_PNG))
    elif (self.oldtool == 'Fog_RemoveFillCircle'):
      self.bRemoveFilledCircle.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'fog_remove_filled_circle.png'), wx.BITMAP_TYPE_PNG))
    elif (self.oldtool == 'Fog_RemoveFillRectangle'):
      self.bRemoveFilledRectangle.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'fog_remove_filled_rectangle.png'), wx.BITMAP_TYPE_PNG))
    elif (self.oldtool == 'Fog_RemoveLine'):
      self.bRemoveLine.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'fog_remove_line.png'), wx.BITMAP_TYPE_PNG))
    elif (self.oldtool == 'Fog_RemoveMultiline'):
      self.bRemoveMultiline.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'fog_remove_line_segments.png'), wx.BITMAP_TYPE_PNG))


    if (newtool == 'Fog_Select'):
      self.bSelectItem.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_select_selected.png'), wx.BITMAP_TYPE_PNG))
      gv.DrawHandles = True
    elif (newtool == 'Fog_EraseFreehand'):
      self.bEraseFog.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'fog_eraser_selected.png'), wx.BITMAP_TYPE_PNG))
    elif (newtool == 'Fog_FillCircle'):
      self.bDrawFilledCircle.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'fog_filled_circle_selected.png'), wx.BITMAP_TYPE_PNG))
    elif (newtool == 'Fog_FillRect'):
      self.bDrawFilledRectangle.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'fog_filled_rectangle_selected.png'), wx.BITMAP_TYPE_PNG))
    elif (newtool == 'Fog_Line'):
      self.bDrawLine.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_line_selected.png'), wx.BITMAP_TYPE_PNG))
    elif (newtool == 'Fog_Multiline'):
      self.bDrawMultiline.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'draw_line_segments_selected.png'), wx.BITMAP_TYPE_PNG))
    elif (newtool == 'Fog_AddFreehand'):
      self.bAddFog.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'fog_brush_selected.png'), wx.BITMAP_TYPE_PNG))
    elif (newtool == 'Fog_AddGenericLight'):
      self.bAddLightSource.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'fog_generic_light_selected.png'), wx.BITMAP_TYPE_PNG))            
    elif (newtool == 'Fog_RemoveFillCircle'):
      self.bRemoveFilledCircle.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'fog_remove_filled_circle_selected.png'), wx.BITMAP_TYPE_PNG))
    elif (newtool == 'Fog_RemoveFillRectangle'):
      self.bRemoveFilledRectangle.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'fog_remove_filled_rectangle_selected.png'), wx.BITMAP_TYPE_PNG))
    elif (newtool == 'Fog_RemoveLine'):
      self.bRemoveLine.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'fog_remove_line_selected.png'), wx.BITMAP_TYPE_PNG))
    elif (newtool == 'Fog_RemoveMultiline'):
      self.bRemoveMultiline.SetBitmapLabel(wx.Bitmap(os.path.join(gv.artwork_directory,'fog_remove_line_segments_selected.png'), wx.BITMAP_TYPE_PNG))

    self.oldtool = newtool
    if (newtool == 'Select') or (newtool == 'Delete'):
      gv.PyMapperApp.DrawMapWindow()
      return
    else:
      self.DeSelectItem()
      gv.PyMapperApp.DrawMapWindow()
    return
  
  def DeSelectItem(self):
    for item in gv.PyMapperApp.DrawingList:
      if (item.selected):
        item.selected = False
        break
    return
  
  def OnSelectItem( self, event ):
    gv.DrawingTool = 'Fog_Select'
    self.ChangeToolBitmaps('Fog_Select')
    return

  def OnEraseFog( self, event ):
    gv.DrawingTool = 'Freehand'  #This is the same as freehand, but in white only
    self.ChangeToolBitmaps('Fog_EraseFreehand')
    penWidth = int((gv.MapZoomFactor/gv.GridScale)*self.spRemoveBrushRadius.GetValue())
    gv.DrawingToolPen = wx.Pen(wx.BLACK, width=penWidth)
    gv.DrawingToolBrush = wx.Brush(wx.BLACK)
    return
  
  def OnDrawFog( self, event ):
    gv.DrawingTool = 'Freehand'  #this is the same as freehand, but in black only
    self.ChangeToolBitmaps('Fog_AddFreehand')
    penWidth = int((gv.MapZoomFactor/gv.GridScale)*self.spAddBrushRadius.GetValue())
    gv.DrawingToolPen = wx.Pen(wx.WHITE, width=penWidth)
    gv.DrawingToolBrush = wx.Brush(wx.WHITE, self.spAddBrushRadius.GetValue())
    return
  
  def OnRemoveFogCircle(self, event):
    gv.DrawingTool = 'FillCircle'
    self.ChangeToolBitmaps('Fog_RemoveFillCircle')
    gv.DrawingToolPen = wx.Pen(wx.BLACK, width=1)
    gv.DrawingToolBrush = wx.Brush(wx.BLACK)
    return
    
  def OnDrawFogCircle( self, event ):
    gv.DrawingTool = 'FillCircle'
    self.ChangeToolBitmaps('Fog_FillCircle')
    gv.DrawingToolPen = wx.Pen(wx.WHITE, width=1)
    gv.DrawingToolBrush = wx.Brush(wx.WHITE)
    return

  def OnDrawFogRectangle( self, event ):
    gv.DrawingTool = 'FillRect'
    self.ChangeToolBitmaps('Fog_FillRect')
    gv.DrawingToolPen = wx.Pen(wx.WHITE, width=1)
    gv.DrawingToolBrush = wx.Brush(wx.WHITE)
    return

  def OnRemoveFogRectangle( self, event ):
    gv.DrawingTool = 'FillRect'
    self.ChangeToolBitmaps('Fog_RemoveFillRectangle')
    gv.DrawingToolPen = wx.Pen(wx.BLACK, width=1)
    gv.DrawingToolBrush = wx.Brush(wx.BLACK)
    return
  
  def OnAddGenericLightSource(self, event):
    gv.DrawingTool = 'Point'
    self.ChangeToolBitmaps('Fog_AddGenericLight')
    LightColor = self.cpkLightSource.GetColour()
    density = 0.3  #light density
    LightColor.Set(LightColor.red, LightColor.green, LightColor.blue, alpha=density*255)
    gv.DrawingToolBrush = wx.Brush(LightColor)
    gv.DrawingToolPen = wx.Pen(LightColor, self.spLightRadius.GetValue())
    return

  def OnDrawFogLine( self, event ):
    gv.DrawingTool = 'Line'
    self.ChangeToolBitmaps('Fog_Line')
    penWidth = int((gv.MapZoomFactor/gv.GridScale)*self.spAddLineWidth.GetValue())
    gv.DrawingToolPen = wx.Pen(wx.WHITE, width=penWidth)
    gv.DrawingToolBrush = wx.Brush(wx.WHITE, self.spAddLineWidth.GetValue())
    return

  def OnDrawFogMultiline( self, event ):
    gv.DrawingTool = 'Multiline'
    self.ChangeToolBitmaps('Fog_Multiline')
    penWidth = int((gv.MapZoomFactor/gv.GridScale)*self.spAddLineWidth.GetValue())
    gv.DrawingToolPen = wx.Pen(wx.WHITE, width=penWidth)
    gv.DrawingToolBrush = wx.Brush(wx.WHITE, self.spAddLineWidth.GetValue())
    return

  def OnRemoveFogLine( self, event ):
    gv.DrawingTool = 'Line'
    self.ChangeToolBitmaps('Fog_RemoveLine')
    penWidth = int((gv.MapZoomFactor/gv.GridScale)*self.spRemoveLineWidth.GetValue())
    gv.DrawingToolPen = wx.Pen(wx.BLACK, width=penWidth)
    gv.DrawingToolBrush = wx.Brush(wx.BLACK, self.spRemoveLineWidth.GetValue())
    return

  def OnRemoveFogMultiline( self, event ):
    gv.DrawingTool = 'Multiline'
    self.ChangeToolBitmaps('Fog_RemoveMultiline')
    penWidth = int((gv.MapZoomFactor/gv.GridScale)*self.spRemoveLineWidth.GetValue())
    gv.DrawingToolPen = wx.Pen(wx.BLACK, width=penWidth)
    gv.DrawingToolBrush = wx.Brush(wx.BLACK, self.spRemoveLineWidth.GetValue())
    return


  def OnRevealAll(self, event):
    pageIndex = gv.PyMapperApp.nbMapNotebook.GetSelection()
    fogItem = gv.DrawingObject_Record(startpoint=wx.Point2D(0,0), tool_type='FillRect',
                                      init_brush=wx.BLACK_BRUSH, init_pen=wx.BLACK_PEN,
                                      init_page_name=gv.PyMapperApp.nbMapNotebook.GetPageText(pageIndex))
    fogItem.rect = wx.Rect2D(0,0,gv.PyMapperApp.MapStruct.columns,gv.PyMapperApp.MapStruct.rows)
    gv.PyMapperApp.DrawingList.append(fogItem)
    gv.PyMapperApp.DrawMapWindow()
    return  
    
  def OnConcealAll(self, event):
    pageIndex = gv.PyMapperApp.nbMapNotebook.GetSelection()
    fogItem = gv.DrawingObject_Record(startpoint=wx.Point2D(0,0),tool_type='FillRect',
                                      init_brush=wx.WHITE_BRUSH, init_pen=wx.WHITE_PEN,
                                      init_page_name=gv.PyMapperApp.nbMapNotebook.GetPageText(pageIndex))
    fogItem.rect = wx.Rect2D(0,0,gv.PyMapperApp.MapStruct.columns,gv.PyMapperApp.MapStruct.rows)
    gv.PyMapperApp.DrawingList.append(fogItem)
    gv.PyMapperApp.DrawMapWindow()
    return
  
  def OnClose(self, event):
    FogToolsDialog = None
    event.Skip()
    return
  
  
def DrawLightSource (self):
  return