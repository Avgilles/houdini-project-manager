import hou
import os
# from hutil.Qt import QtWidgets
from PySide2 import QtWidgets

print("loading project")
proj = hou.getenv('JOB') + '/'
print(proj)


def openScene(item):
    print('open ' + item.data())
    hipFile = proj + item.data()
    print(hipFile)
    hou.hipFile.load(hipFile)


def onCreateInterface():
    widget = QtWidgets.QLabel(proj)
    listwidget = QtWidgets.QListWidget()

    for file in os.listdir(proj):
        if file.endswith('.hip'):
            listwidget.addItem(file)

    listwidget.doubleClicked.connect(openScene)

    return listwidget
