from jproperties import Properties
propfile = Properties()
class PropReader:
    def readProp(Key):
        with open("Config.properties", "rb") as configfile:
            propfile.load(configfile)
        return propfile.get(Key).data


#print all the values from prop file
# itemview = propfile.items()
# for item in itemview:
#     print(item[1].data)
#
# print(readProp("password"))