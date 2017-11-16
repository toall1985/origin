import os

write_info = "import sys\nimport xbmcplugin\nimport xbmcgui\n\nList = ['Addon has been wiped, please uninstall.',\n'Due to the potentially copyright infringing nature of some',\
\n'media openly sourced on the internet it is not worth continuing development',\n'and potentially jeopordizing personal life for a hobby. I respect the decisions',\
\n'of those that chose to continue so hopefully you can all respect mine too']\n\nfor item in List:\n\tok=True\
\n\tliz=xbmcgui.ListItem(item, iconImage='DefaultFolder.png')\n\txbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url='',listitem=liz,isFolder=False)\
\n\nxbmcplugin.endOfDirectory(int(sys.argv[1]))"

cf = os.getcwd()

Next = os.walk('.').next()[1]
for item in Next:
    if 'plugin' in item:
        file_to_change = os.path.join(cf,item,'default.py')
        write_file = open(file_to_change,'w+')
        write_file.write(write_info)
        write_file.close()



