import sys
import urllib.request
import urllib.error

URL = "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task"
MODEL_PATH = "./model/hand_landmarker.task"


def report_hook(block_number: int, read_size: int, total_file_size: int) -> None:
    downloaded_size = block_number * read_size
    if downloaded_size >= total_file_size:
        downloaded_size = total_file_size

    percent = int(downloaded_size / total_file_size * 100)

    bar = "#" * (percent // 2) + " " * (50 - percent // 2)

    if block_number:
        sys.stdout.write("\033[F")
    print(f"    Progress: |{bar}| ({total_file_size / 1024000:.2f}MB)")


if __name__ == "__main__":
    print(f"Downloading: hand_landmarker.task")
    try:
        urllib.request.urlretrieve(url=URL, filename=MODEL_PATH, reporthook=report_hook)
    except urllib.error.URLError as e:
        print(f"\033[31mFailed: URLError: {e}\033[0m")
        sys.exit(1)

    print("Done.")
