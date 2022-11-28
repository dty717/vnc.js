from tkinter import *
from tkinter import ttk
from components.table import TreeTable
from models.tableDatas import TableDatas
from database.mongodb import dbGetFiveParametersHistory

class HistoryBoard(Frame):
    def __init__(self, master, **kargs):
        super().__init__(master, kargs)
        historyTabs = ttk.Notebook(self, padding=10, style="HistoryBoard")
        historyTabs.pack(fill=BOTH)
        ##
        ## sampleHistory
        ##
        self.historyTableDatas = TableDatas()
        historyTableDatas = self.historyTableDatas
        historyTableDatas.setColumns(
            'time', 'PH', 'temp', 'ele', 'tur', 'O2')
        # column
        historyTableDatas.column("#0", width=50, minwidth=25)
        historyTableDatas.column("time", anchor=CENTER, width=184)
        historyTableDatas.column("PH", anchor=CENTER, width=91)
        historyTableDatas.column("temp", anchor=CENTER, width=91)
        historyTableDatas.column("ele", anchor=CENTER, width=91)
        historyTableDatas.column("tur", anchor=CENTER, width=91)
        historyTableDatas.column("O2", anchor=CENTER, width=91)
        # headingConfigs
        historyTableDatas.heading("#0", text="序号", anchor=CENTER)
        historyTableDatas.heading("time", text="时间", anchor=CENTER)
        historyTableDatas.heading("PH", text="PH", anchor=CENTER)
        historyTableDatas.heading("temp", text="温度", anchor=CENTER)
        historyTableDatas.heading("ele", text="电导率", anchor=CENTER)
        historyTableDatas.heading("tur", text="浊度", anchor=CENTER)
        historyTableDatas.heading("O2", text="溶解氧", anchor=CENTER)
        # data
        histories = list(dbGetFiveParametersHistory(nPerPage=0))
        for index, history in enumerate(histories):
            history['time'] = history['time'].strftime("%Y-%m-%d %H:%M:%S")
            history['PH'] = round(history['PH'], 3)
            history['temp'] = round(history['temp'], 2)
            history['ele'] = round(history['ele'], 3)
            history['tur'] = round(history['tur'], 3)
            history['O2'] = round(history['O2'], 3)
            historyTableDatas.insert(parent='', index='end', iid=index, text=str(
                index+1), values=tuple(history.values())[1:])
        historyTab = Frame(self)
        historyTableScrollBar = Scrollbar(historyTab)
        historyTableScrollBar.pack(side=RIGHT, fill=Y)
        self.historyTreeTable = TreeTable(
            historyTab, historyTableDatas, yscrollcommand=historyTableScrollBar.set, height=20)
        self.historyTreeTable.pack()
        historyTableScrollBar.config(command=self.historyTreeTable.yview)
        historyTab.pack()
        #
        # historyTab = Frame(self,width=50, height=50, bg="red")
        historyTabs.add(historyTab, text="水样历史")
    def refreshPage(self):
        ##
        ## sampleHistory
        ##
        self.historyTreeTable.delete(*self.historyTreeTable.get_children())
        historyTableDatas = self.historyTableDatas
        historyTableDatas.clearDatas()
        # data
        histories = list(dbGetFiveParametersHistory(nPerPage=0))
        for index, history in enumerate(histories):
            history['time'] = history['time'].strftime("%Y-%m-%d %H:%M:%S")
            history['PH'] = round(history['PH'], 3)
            history['temp'] = round(history['temp'], 2)
            history['ele'] = round(history['ele'], 3)
            history['tur'] = round(history['tur'], 3)
            history['O2'] = round(history['O2'], 3)
            historyTableDatas.insert(parent='', index='end', iid=index, text=str(
                index+1), values=tuple(history.values())[1:])
        self.historyTreeTable.refreshDate(historyTableDatas)
# mianBoard = Frame(tabNoteBook, width=100, height=100, bg="red")
# mianBoard.pack(fill=BOTH, expand=1)
