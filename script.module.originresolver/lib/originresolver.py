import sys
import xbmcplugin
import xbmcgui

List = ['Addon has been wiped, please uninstall.',
'Due to the potentially copyright infringing nature of some',
'media openly sourced on the internet it is not worth continuing development',
'and potentially jeopordizing personal life for a hobby. I respect the decisions',
'of those that chose to continue so hopefully you can all respect mine too']

for item in List:
	ok=True
	liz=xbmcgui.ListItem(item, iconImage="DefaultFolder.png")
	xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url='',listitem=liz,isFolder=False)

xbmcplugin.endOfDirectory(int(sys.argv[1]))