#!/usr/bin/env python
#
# gst-python
# Copyright (C) 2002 David I. Lehn
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Library General Public License for more details.
#
# You should have received a copy of the GNU Library General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.
# 
# Author: David I. Lehn <dlehn@users.sourceforge.net>
#

import sys
from gstreamer import *
import gobject
from cp import filter

class Identity(Element):
   def __init__(self):
      self.__gobject_init__()
      self.sinkpad = Pad('sink', PAD_SINK)
      self.add_pad(self.sinkpad)
      self.sinkpad.set_chain_function(self.chain)
      self.sinkpad.set_link_function(self.pad_link)

      self.srcpad = Pad('src', PAD_SRC)
      self.add_pad(self.srcpad)
      self.srcpad.set_link_function(self.pad_link)

   def get_bufferpool(self, pad):
      print 'get_bufferpool:', self, pad
      return self.srcpad.get_bufferpool()

   def pad_link(self, pad, caps):
      print 'pad_link:', self, pad, caps
      return PAD_LINK_OK

   def chain(self, pad, buf):
      self.srcpad.push(buf)

gobject.type_register(Identity)

def main():
   "A GStreamer Python subclassing example of an identity filter"
   gst_debug_set_categories(0L)

   identity = Identity()
   identity.set_name('identity')
   if not identity:
      print 'could not create \"Identity\" element'
      return -1

   return filter([identity])

if __name__ == '__main__':
   ret = main()
   sys.exit (ret)