import pyautogui as gui

class Cursor():
    def moveCur(self):
        while(True):
            try:
                gui.moveTo(486, 789)
                gui.moveRel(0, 10)
                gui.moveTo(789, 486)
                gui.moveRel(10, 0)
            except Exception as e:
                print(str(e))