import vlc


def main():
    file = vlc.MediaPlayer('audio/when.mp3')
    file.play()


if __name__ == '__main__':
    main()
