
# Import modules needed to run commands and check files
import subprocess
import os
import sys

# Set the recording folder and video file
# Replace these values with the paths for any recording date
RUN_DIR = "run_directory"
VIDEO_FILE = "video.mp4"

# Name of the existing script used to extract video frames
EXTRACTION_SCRIPT = "extract_video_frames_to_run.py"


# Define a function to extract frames from the video
def extract_frames():

    # Check whether the recording directory exists
    if not os.path.isdir(RUN_DIR):
        print(f"Error: Run directory not found: {RUN_DIR}")
        return  # Stop if the directory is missing

    # Check whether the video file exists
    if not os.path.isfile(VIDEO_FILE):
        print(f"Error: Video file not found: {VIDEO_FILE}")
        return  # Stop if the video is missing

    # Check whether the frame extraction script exists
    if not os.path.isfile(EXTRACTION_SCRIPT):
        print(f"Error: Extraction script not found: {EXTRACTION_SCRIPT}")
        return  # Stop if the script is missing

    # Build the command to run the extraction script
    command = [
        sys.executable,       # Use the current Python interpreter
        EXTRACTION_SCRIPT,    # Script that extracts video frames
        "--run_dir", RUN_DIR, # Recording directory
        "--video", VIDEO_FILE,  # Input video file
        "--out_subdir", "frames/video",  # Output folder for frames
        "--start_sec", "0.0",  # Start extraction at 0 seconds
        "--lidar_fps", "10"    # Set the sampling rate to 10 FPS
    ]

    # Run the extraction command and detect execution failures
    try:
        subprocess.run(command, check=True)

        # Report success if the command finishes without an error
        print("Frames extracted successfully.")

    # Handle errors if the extraction script returns a failure
    except subprocess.CalledProcessError as error:
        print(f"Frame extraction failed: {error}")

    # Handle errors when the command cannot be started
    except OSError as error:
        print(f"Could not run extraction script: {error}")


# Run the function when this Python file is executed directly
if __name__ == "__main__":
    extract_frames()


