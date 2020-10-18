import QtQuick 2.7
import QtQuick.Window 2.2
import QtQuick.Controls 1.4
import QtGraphicalEffects 1.0

ApplicationWindow {
  id: mainWindow
  height: 160
  width: 300
  title: "PornHub"
  visible: true

  Item {
    id: page
    visible: true
    width: parent.width
    height: parent.height

    Rectangle {
      id: myRect
      height: {
        console.log("I\'m  a comment")
        return parent.height
      }
      width: parent.width

      color: "#FF0000"

      Text {
        id: mainText
        text: "I am some text"
        height: 50
        width: parent.width
        font.pixelSize: 12
        horizontalAlignment: Text.AlignHCenter
      }

      Button {
        id: mainButton
        text: "Push this button"
        anchors.top: mainText.bottom
        onClicked: {
          if(myRect.color == "#000000"){
            myRect.color = "#FF0000"
            mainText.color = "#FFFFFF"
          }
          else {
            myRect.color = "#000000"
          }
        }
      }

    }
  }
}
