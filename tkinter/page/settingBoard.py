from tkinter import *
from tkinter import ttk
from components.groupLabelButton import GroupLabelButton
from components.labelButton import LabelTextButton, SwitchLabelButton
from PIL import Image
from tool.bytesConvert import floatToRegister
from config.config import *
from service.device import write_single_register, write_multiple_registers, DeviceAddr, deviceInfo, deviceController

class SettingBoard(Frame):
    def __init__(self, master, imgDicts, **kargs):
        super().__init__(master, kargs)
        #
        #calibrateTimeGroup
        #
        calibrateTimeGroup = GroupLabelButton(self, title="标定时间")
        calibrateTimeGroup.pack(pady=20)
        self.calibrateDayLabelText = LabelTextButton(calibrateTimeGroup, text="标定日",
                                                command=lambda content: write_single_register(DeviceAddr.calibrateDayAddr.value, int(float(content)),
                                                                                              lambda rec: setattr(deviceController, 'calibrateDay', int(float(content))), repeatTimes=0, needMesBox=True)
                                                )
        self.calibrateDayLabelText.setText(deviceController.calibrateDay)
        self.calibrateDayLabelText.pack(anchor=W, pady=5)
        self.calibrateHourLabelText = LabelTextButton(calibrateTimeGroup, text="标定时",
                                                 command=lambda content: write_single_register(DeviceAddr.calibrateHourAddr.value, int(float(content)),
                                                                                               lambda rec: setattr(deviceController, 'calibrateHour', int(float(content))), repeatTimes=0, needMesBox=True)
                                                 )
        self.calibrateHourLabelText.setText(deviceController.calibrateHour)
        self.calibrateHourLabelText.pack(anchor=W, pady=5)
        self.calibrateMinuteLabelText = LabelTextButton(calibrateTimeGroup, text="标定分",
                                                   command=lambda content: write_single_register(DeviceAddr.calibrateMinuteAddr.value, int(float(content)),
                                                                                                 lambda rec: setattr(deviceController, 'calibrateMinute', int(float(content))), repeatTimes=0, needMesBox=True)
                                                   )
        self.calibrateMinuteLabelText.setText(deviceController.calibrateMinute)
        self.calibrateMinuteLabelText.pack(anchor=W, pady=5)
        self.switchImmediateCalibrate = SwitchLabelButton(calibrateTimeGroup, imgDicts, text="立即标定",
                                                     textYES="开始", clickYES=lambda: write_single_register(DeviceAddr.immediateCalibrateAddr.value, 1, lambda rec: setattr(deviceController, 'immediateCalibrate', 1) or self.switchImmediateCalibrate.open(), repeatTimes=0, needMesBox=True),
                                                     textNO="取消", clickNO=lambda: write_single_register(DeviceAddr.immediateCalibrateAddr.value, 0, lambda rec: setattr(deviceController, 'immediateCalibrate', 0) or self.switchImmediateCalibrate.close(), repeatTimes=0, needMesBox=True),
                                                     )
        if deviceController.immediateCalibrate == 1:
            self.switchImmediateCalibrate.open()
        else:
            self.switchImmediateCalibrate.close()
        self.switchImmediateCalibrate.pack(anchor=W, pady=5)
        #
        #concentrationSettingValueGroup
        #
        concentrationSettingValueGroup = GroupLabelButton(self, title="标定浓度")
        concentrationSettingValueGroup.pack(pady=10)
        self.concentration1SettingValueLabelText = LabelTextButton(concentrationSettingValueGroup, text="标一浓度",
                                                              command=lambda content: write_multiple_registers(DeviceAddr.concentration1SettingValueAddr.value, floatToRegister(content),
                                                                                                               lambda rec: setattr(deviceController, 'concentration1SettingValue', float(content)), repeatTimes=0, needMesBox=True)
                                                              )
        self.concentration1SettingValueLabelText.setText(
            deviceController.concentration1SettingValue)
        self.concentration1SettingValueLabelText.pack(anchor=W, pady=5)
        self.concentration2SettingValueLabelText = LabelTextButton(concentrationSettingValueGroup, text="标二浓度",
                                                              command=lambda content: write_multiple_registers(DeviceAddr.concentration2SettingValueAddr.value, floatToRegister(content),
                                                                                                               lambda rec: setattr(deviceController, 'concentration2SettingValue', float(content)), repeatTimes=0, needMesBox=True)
                                                              )
        self.concentration2SettingValueLabelText.setText(
            deviceController.concentration2SettingValue)
        self.concentration2SettingValueLabelText.pack(anchor=W, pady=5)
        self.concentration3SettingValueLabelText = LabelTextButton(concentrationSettingValueGroup, text="标三浓度",
                                                              command=lambda content: write_multiple_registers(DeviceAddr.concentration3SettingValueAddr.value, floatToRegister(content),
                                                                                                               lambda rec: setattr(deviceController, 'concentration3SettingValue', float(content)), repeatTimes=0, needMesBox=True)
                                                              )
        self.concentration3SettingValueLabelText.setText(
            deviceController.concentration3SettingValue)
        self.concentration3SettingValueLabelText.pack(anchor=W, pady=5)
        #
        #sampleTimeGroup
        #
        sampleTimeGroup = GroupLabelButton(self, title="做样时间")
        sampleTimeGroup.pack(pady=20)
        self.measurementIntervalLabelText = LabelTextButton(sampleTimeGroup, text="间隔时间",
                                                       command=lambda content: write_single_register(DeviceAddr.measurementIntervalAddr.value, int(float(content)),
                                                                                                     lambda rec: setattr(deviceController, 'measurementInterval', int(float(content))), repeatTimes=0, needMesBox=True)
                                                       )
        self.measurementIntervalLabelText.setText(
            deviceController.measurementInterval)
        self.measurementIntervalLabelText.pack(anchor=W, pady=5)
        # self.pack()
        # self.entrythingy = Entry()
        # self.entrythingy.pack()
        # # Create the application variable.
        # self.contents = StringVar()
        # # Set it to some value.
        # self.contents.set("this is a variable")
        # # Tell the entry widget to watch this variable.
        # self.entrythingy["textvariable"] = self.contents
        # # Define a callback for when the user hits return.
        # # It prints the current value of the variable.
        # self.entrythingy.bind('<Key-Return>',
        #                      self.print_contents)
    def refreshPage(self):
        self.calibrateDayLabelText.setText(deviceController.calibrateDay)
        self.calibrateHourLabelText.setText(deviceController.calibrateHour)
        self.calibrateMinuteLabelText.setText(deviceController.calibrateMinute)
        if deviceController.immediateCalibrate == 1:
            self.switchImmediateCalibrate.open()
        else:
            self.switchImmediateCalibrate.close()
        self.concentration1SettingValueLabelText.setText(
            deviceController.concentration1SettingValue)
        self.concentration2SettingValueLabelText.setText(
            deviceController.concentration2SettingValue)
        self.concentration3SettingValueLabelText.setText(
            deviceController.concentration3SettingValue)
        self.measurementIntervalLabelText.setText(
            deviceController.measurementInterval)
        return
    # def print_contents(self, event):
    #     print("Hi. The current entry content is:",
    #           self.contents.get())


# mianBoard = Frame(tabNoteBook, width=100, height=100, bg="red")
# mianBoard.pack(fill=BOTH, expand=1)
