import subprocess
import os

RUN_DIR = "march28_run"
VIDEO_FILE = "march28.mp4"

def extract_frames():

    if not os.path.exists(RUN_DIR):
        print("Run directory not found")
        return

    command = [
        "python",
        "extract_video_frames_to_run.py",
        "--run_dir", RUN_DIR,
        "--video", VIDEO_FILE,
        "--out_subdir", "frames/video",
        "--start_sec", "0.0",
        "--lidar_fps", "10"
    ]

    subprocess.run(command)

    print("Frames extracted successfully")


if __name__ == "__main__":
    extract_frames()
