import sys
import pymysql
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem
from database import Ui_database


class MainWindow(QWidget, Ui_database):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.connectBtn.clicked.connect(self.showTables)
        self.executeBtn.clicked.connect(self.executesql)
        self.table.cellClicked.connect(self.datachanged)

    def datachanged(self, row, col):
        tablename = self.table.item(row, 0).text()
        self.sqlLine.setText('select * from {}'.format(tablename))
        self.executesql()

    def showTables(self):
        host = self.hostLine.text()
        database = self.portLine.text()
        user = self.userLine.text()
        password = self.passwordLine.text()
        self.db = pymysql.connect(host=host, port=3306, user=user,
                             password=password, db=database, charset='utf8')
        sql = 'show tables'
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            self.db.commit()
            results = cursor.fetchall()
            self.table.setRowCount(len(results))
            for i in range(len(results)):
                self.table.setItem(i, 0, QTableWidgetItem(results[i][0]))
        except:
            self.db.rollback()
            print('Show RollBack')
        cursor.close()

    def executesql(self):
        sql = self.sqlLine.text()
        try:
            temp = sql.split()
            if 'select' in temp:
                if '*' in temp:
                    cursor = self.db.cursor()
                    ind = temp.index('from')
                    cursor.execute('desc {}'.format(temp[ind+1]))
                    results = cursor.fetchall()
                    title = []
                    for item in results:
                        title.append(item[0])
                    print(title)
                    self.data.setColumnCount(len(title))
                    self.data.setHorizontalHeaderLabels(title)
                    cursor.close()
                else:
                    ind = temp.index('select')
                    titles = temp[ind+1].split(',')
                    print(titles)
                    self.data.setColumnCount(len(titles))
                    self.data.setHorizontalHeaderLabels(titles)
            else:
                print('非查询sql')
        except:
            self.db.rollback()
            print('Title RollBack')
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            print(results)
            row = len(results)
            column = len(results[0])
            self.data.setRowCount(row)
            self.data.setColumnCount(column)
            for i in range(row):
                for j in range(column):
                    if type(results[i][j]) == str:
                        self.data.setItem(i, j, QTableWidgetItem(results[i][j]))
                    else:
                        self.data.setItem(i, j, QTableWidgetItem(str(results[i][j])))
        except:
            self.db.rollback()
            print('SQL RollBack')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    # win.setStyleSheet(qss)
    win.show()
    sys.exit(app.exec_())
