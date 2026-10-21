
import subprocess
import os
import sys

RUN_DIR = "run_directory"
VIDEO_FILE = "video.mp4"
EXTRACTION_SCRIPT = "extract_video_frames_to_run.py"


def extract_frames():
    if not os.path.isdir(RUN_DIR):
        print(f"Error: Run directory not found: {RUN_DIR}")
        return

    if not os.path.isfile(VIDEO_FILE):
        print(f"Error: Video file not found: {VIDEO_FILE}")
        return

    if not os.path.isfile(EXTRACTION_SCRIPT):
        print(f"Error: Extraction script not found: {EXTRACTION_SCRIPT}")
        return

    command = [
        sys.executable,
        EXTRACTION_SCRIPT,
        "--run_dir", RUN_DIR,
        "--video", VIDEO_FILE,
        "--out_subdir", "frames/video",
        "--start_sec", "0.0",
        "--lidar_fps", "10"
    ]

    try:
        subprocess.run(command, check=True)
        print("Frames extracted successfully.")

    except subprocess.CalledProcessError as error:
        print(f"Frame extraction failed: {error}")

    except OSError as error:
        print(f"Could not run extraction script: {error}")


if __name__ == "__main__":
    extract_frames()

