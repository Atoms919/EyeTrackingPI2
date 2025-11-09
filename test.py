from pyEyeTrack.PyEyeTrackRunnerClass import pyEyeTrack

if __name__ == "__main__":
    ptr = pyEyeTrack()

    ptr.pyEyeTrack_runner(
	UI=True,
	pupilTracking=True,
	eyeTrackingLog=True,
	eyeTrackingFileName='User_1'
    )

