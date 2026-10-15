
from pathlib import Path
import cv2
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="View labeled frames for the RTTM auto-labeler project."
    )
    parser.add_argument(
        "--frames",
        required=True,
        help="Folder containing labeled image frames."
    )
    args = parser.parse_args()

    frames_dir = Path(args.frames)

    if not frames_dir.is_dir():
        print(f"Error: Folder not found: {frames_dir}")
        return

    extensions = {".png", ".jpg", ".jpeg", ".bmp"}
    frames = sorted(
        file for file in frames_dir.iterdir()
        if file.suffix.lower() in extensions
    )

    if not frames:
        print("No image frames found.")
        return

    index = 0

    while 0 <= index < len(frames):
        frame = cv2.imread(str(frames[index]))

        if frame is None:
            print(f"Cannot read {frames[index].name}")
            index += 1
            continue

        display = frame.copy()
        cv2.putText(
            display,
            f"Frame {index + 1}/{len(frames)}: {frames[index].name}",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

        cv2.imshow("RTTM Labeled Frame Viewer", display)
        key = cv2.waitKey(0) & 0xFF

        if key == ord("q") or key == 27:
            break
        elif key == ord("n") or key == 32:
            index += 1
        elif key == ord("p"):
            index = max(0, index - 1)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
