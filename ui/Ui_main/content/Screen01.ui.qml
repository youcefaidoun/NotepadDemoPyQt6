import QtQuick
import QtQuick.Controls
import Ui_main

Rectangle {
    width: Constants.width
    height: Constants.height

    color: Constants.backgroundColor

    Text {
        text: qsTr("Hello Ui_main")
        anchors.centerIn: parent
        font.family: Constants.font.family
    }
}
