import mss
import cv2
import numpy as np

def capture_screen(region=None):
    """
    Capture a screenshot of the specified region.

    Args:
        region (dict): Region to capture (e.g., {'top': 100, 'left': 100, 'width': 800, 'height': 600}).

    Returns:
        np.array: Captured image as a NumPy array.
    """
    with mss.mss() as sct:
        monitor = region if region else sct.monitors[1]  # Full screen if no region specified
        screenshot = np.array(sct.grab(monitor))
        return cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)

if __name__ == "__main__":
    # Test screen capture
    region = {"top": 0, "left": 0, "width": 1300, "height": 850}
    frame = capture_screen(region)
    cv2.imshow("Screen Capture", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()