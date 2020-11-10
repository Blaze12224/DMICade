import window_handler

class ProjectManager:

    def __init__(self):
        pass

    def start(self):
        win_handler = window_handler.WindowHandler()
        win_handler.start()

pm = ProjectManager()
pm.start()