import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

class VideoBackgroundWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("GUI with Video Background")
        self.setGeometry(100, 100, 800, 600)

        # Create a QtMultimedia player, video widget, and playlist
        self.media_player = QMediaPlayer(self)
        self.video_widget = QVideoWidget(self)
        self.media_playlist = QMediaPlaylist()
        self.media_content = QMediaContent(QUrl.fromLocalFile("tony1.gif"))  # Replace with your video file path
        self.media_playlist.addMedia(self.media_content)
        self.media_playlist.setCurrentIndex(0)

        # Set the media playlist to loop
        self.media_playlist.setPlaybackMode(QMediaPlaylist.Loop)

        # Set the playlist to the media player
        self.media_player.setPlaylist(self.media_playlist)
        self.media_player.setVideoOutput(self.video_widget)

        # Create a layout for the video widget
        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)
        self.setLayout(layout)

        # Play the video
        self.media_player.play()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoBackgroundWindow()
    window.show()
    sys.exit(app.exec_())
