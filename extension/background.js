// Copyright (C) 2021  DELATTE_JAILLLON_HERMANN_PERESSE-GOURBIL
// 
// This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or  any later version.
// 
// This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
// 
// You should have received a copy of the GNU General Public License along with this program; if not, go on http://www.gnu.org/licenses/gpl-3.0.html or write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA


//script d'arriere plan
//on ajoute un eventListener sur l'installation, pour inistialliser la précision a 80%
chrome.runtime.onInstalled.addListener(() => {
  chrome.storage.sync.set({ 'StoredPrecision': 80 }, function() {
  });
});
