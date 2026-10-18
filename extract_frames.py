import subprocess

RUN_DIR = "march28_dataset"
VIDEO_PATH = "march28_video.mp4"

command = [
    "python",
    "extract_video_frames_to_run.py",
    "--run_dir", RUN_DIR,
    "--video", VIDEO_PATH,
    "--out_subdir", "frames/video",
    "--start_sec", "0.0",
    "--lidar_fps", "10"
]

print("Extracting synchronized frames...")

subprocess.run(command)

print("Finished.")
