import PyQt4.QtGui as gui, PyQt4.QtCore as core

app = gui.QApplication([])

cb = gui.QComboBox()

cb.addItem('int 1',1)
cb.addItem('int 2',5)
cb.addItem('int 3',3)
cb.addItem('int 4',4)

print cb.itemData(0).toInt()[0]

core.pyqtSlot('int')
def f(index):
    data,can_convert =  cb.itemData(index).toInt()
    if can_convert:
        print 'integer:',data

cb.currentIndexChanged.connect(f)

cb.show()

app.exec_()