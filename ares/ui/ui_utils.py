# This file is part of ARES.
#
# Copyright (C) 2015, Dario Incalza <dario.incalza at gmail.com>
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__author__ = 'Dario Incalza'

from PyQt4 import QtCore,QtGui

class CustomTabBar(QtGui.QTabBar):
    '''Subclass QTabBar to implement middle-click closing of tabs'''

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.MidButton:
            self.tabCloseRequested.emit(self.tabAt(event.pos()))
        super(QtGui.QTabBar, self).mouseReleaseEvent(event)
