import sys
import unittest

class OpenCVTest(unittest.TestCase):
    def test_import(self):
        import cv2

    def test_video_capture(self):
        import cv2
        videoCapture = cv2.VideoCapture("./assets/videos/fair_960x540.mp4")
        self.assertTrue(videoCapture.isOpened())

if __name__ == '__main__':
    unittest.main()
