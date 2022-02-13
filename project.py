import hou
import os
# from hutil.Qt import QtWidgets
from PySide2 import QtWidgets

print("loading project")

class ProjectManager(QtWidgets.QWidget):
    def __init__(self):
        super(ProjectManager, self).__init__()
        self.proj = hou.getenv('JOB') + '/'
        # Create Widget
        self.labelTitle = QtWidgets.QLabel('Project Manager :')
        self.label = QtWidgets.QLabel(self.proj)
        self.listwidget = QtWidgets.QListWidget()


        self.onCreateInterface()

        # layout
        mainLayout = QtWidgets.QVBoxLayout()
        # add widget to layout
        self.btn = QtWidgets.QPushButton('Click me')
        mainLayout.addWidget(self.labelTitle)
        mainLayout.addWidget(self.label)
        mainLayout.addWidget(self.listwidget)
        mainLayout.addWidget(self.btn)

        self.setLayout(mainLayout)


    def openScene(self, item):
        print('open ' + item.data())
        hipFile = self.proj + item.data()
        print(hipFile)
        hou.hipFile.load(hipFile)
    
    
    def onCreateInterface(self):
        print("creating interface")


        for file in os.listdir(self.proj):
            if file.endswith('.hip'):
                self.listwidget.addItem(file)
    
        self.listwidget.doubleClicked.connect(self.openScene)
