import subprocess

RUN_DIR = "runs/march28"
VIDEO = "data/march28.mp4"

command = [
    "python",
    "extract_video_frames_to_run.py",
    "--run_dir", RUN_DIR,
    "--video", VIDEO,
    "--out_subdir", "frames/video",
    "--start_sec", "0.0",
    "--lidar_fps", "10"
]

subprocess.run(command)
