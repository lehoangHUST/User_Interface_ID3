# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ID3.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from datasets.dataset import *
from utils.tree2graphviz import *
from id3 import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1272, 1020)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(920, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1100, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(920, 120, 331, 671))
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(1040, 80, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(940, 810, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(1130, 810, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(40, 10, 871, 781))
        self.listWidget_2.setObjectName("listWidget_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1272, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        # Events button
        self.pushButton.clicked.connect(self.open_file)
        self.pushButton_2.clicked.connect(self.clear)
        self.pushButton_3.clicked.connect(self.submit)

        # Event shortcut 
        self.zoom_in_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Plus), MainWindow)
        self.zoom_out_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Minus), MainWindow)
        self.zoom_in_shortcut.activated.connect(self.zoom_in)
        self.zoom_out_shortcut.activated.connect(self.zoom_out)

        # Algorithms ID3
        self.decision_tree = DecisionTreeID3(max_depth=5, min_samples_split=2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Import CSV"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear Attributes"))
        self.label.setText(_translate("MainWindow", "Attributes"))
        self.pushButton_3.setText(_translate("MainWindow", "Predict"))


    def add_image_in_list(self):
        path_image = 'tree_graph.png'
        pixmap = QtGui.QPixmap(path_image)
        pixmap = pixmap.scaled(QtCore.QSize(800, 700))
        label = QtWidgets.QLabel(f"")
        label.setPixmap(pixmap)
        label.setAlignment(QtCore.Qt.AlignCenter)
        item_widget = QtWidgets.QWidget()
        item_layout = QtWidgets.QVBoxLayout()
        item_layout.addWidget(label)
        item_widget.setLayout(item_layout)

        # Thêm mục vào QListWidget
        list_widget_item = QtWidgets.QListWidgetItem()
        list_widget_item.setSizeHint(QtCore.QSize(800, 700))
        self.listWidget_2.addItem(list_widget_item)
        self.listWidget_2.setItemWidget(list_widget_item, item_widget)


    def open_file(self):
        file_csv, type_file = QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Open file', 'D:/') # All files
        # Train ID3
        X_train, Y_train = Weather(file_csv, 0).preprocessing_data()
        self.decision_tree.fit(X_train, Y_train)
        # Read attributes in fname
        features, label = Weather(file_csv, 0).get_attributes()
        # Get attributes 
        for name_feature, values_feature in features.items():
            item_widget = QtWidgets.QWidget()
            item_layout = QtWidgets.QVBoxLayout()

            label = QtWidgets.QLabel(f"{name_feature}")
            combo_box = QtWidgets.QComboBox()
            for value in values_feature:
                combo_box.addItem(f"{value}")

            item_layout.addWidget(label)
            item_layout.addWidget(combo_box)
            item_widget.setLayout(item_layout)

            # Thêm mục vào QListWidget
            list_widget_item = QtWidgets.QListWidgetItem()
            list_widget_item.setSizeHint(item_widget.sizeHint())
            self.listWidget.addItem(list_widget_item)
            self.listWidget.setItemWidget(list_widget_item, item_widget)

        tree = self.decision_tree.root
        xml_string = object_tree_to_xml_string(tree)
        convert_xml_to_graph(xml_string)
        self.add_image_in_list()


    def clear(self):
        # Clear list attributes and list images 
        self.listWidget.clear()
        self.listWidget_2.clear()
        

    def submit(self):
        print(self.listWidget_2.sizeHint())
        try:
            list_current_features, list_label_features  = [], []
            data = {}
            number_features = self.listWidget.count()
            for index in range(number_features):
                item_widget = self.listWidget.itemWidget(self.listWidget.item(index))
                label_feature = item_widget.findChild(QtWidgets.QLabel)
                combo_box = item_widget.findChild(QtWidgets.QComboBox)
                list_current_features.append(combo_box.currentText())
                list_label_features.append(label_feature.text())
            
            # Convert list to dataframe
            for i in range(number_features):
                data[list_label_features[i]] = [list_current_features[i]]
            
            df = pd.DataFrame(data)
            pred_label = self.decision_tree.predict(df.iloc[:, :])[0]
            self.label_2.setText(pred_label.upper())

        except Exception as err:
            pass


    def create_attributes(self):
        self.pushButton.clicked.connect(self.open_file)

    
    def predidct(self):
        self.pushButton_3.clicked.connect(self.submit)


    def zoom_in(self):
        current_icon_size = self.listWidget_2.iconSize()
        new_size = current_icon_size * 1.2
        self.listWidget_2.setIconSize(new_size)


    def zoom_out(self):
        current_icon_size = self.listWidget_2.iconSize()
        new_size = current_icon_size * 0.8
        print(new_size)
        self.listWidget_2.setIconSize(new_size)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
