import subprocess

class WindowHandler:

    _process = None

    def __init__(self):
        pass

    def start(self):
        mtp = '/media/sf_vm_shared_folder/unity_test_build/dmiCade_devTests.x86_64'.split()
        mtp2 = 'nautilus --browser /media/sf_vm_shared_folder/unity_test_build/'.split()
        mtp3 = 'echo test_lmao'.split()
        cp = subprocess.run(mtp2, capture_output=True, shell=True)
        print(cp)
        print('done :))
