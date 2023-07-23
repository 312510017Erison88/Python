from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GArc, GLabel, GLine

SIZE = 100

def main():
    window = GWindow(width=500, height=500)
    background = GRect(400, 350, x=50, y=60)
    background.color = "gold"
    background.filled = True
    background.fill_color = "gain sboro"
    window.add(background)

    face = GOval(150, 125, x=175, y=200)
    face.line_width = 100
    face.color = "saddle brown"
    face.filled = True
    face.fill_color = "white"
    window.add(face)

    l_ear = GOval(50, 50, x=185, y=188)
    l_ear.color = "saddle brown"
    l_ear.filled = True
    l_ear.fill_color = "white"
    window.add(l_ear)

    r_ear = GOval(50, 50, x=265, y=188)
    r_ear.color = "saddle brown"
    r_ear.filled = True
    r_ear.fill_color = "white"
    window.add(r_ear)

    l_ear_2 = GOval(48, 48, x=188, y=192)
    l_ear_2.color = "light pink"
    l_ear_2.filled = True
    l_ear_2.fill_color = "light pink"
    window.add(l_ear_2)

    r_ear_2 = GOval(48, 48, x=264, y=192)
    r_ear_2.color = "light pink"
    r_ear_2.filled = True
    r_ear_2.fill_color = "light pink"
    window.add(r_ear_2)

    l_ear_w = GOval(48, 48, x=192, y=204)
    l_ear_w.color = "white"
    l_ear_w.filled = True
    l_ear_w.fill_color = "white"
    window.add(l_ear_w)

    r_ear_w = GOval(48, 48, x=260, y=204)
    r_ear_w.color = 'white'
    r_ear_w.filled = True
    r_ear_w.fill_color = "white"
    window.add(r_ear_w)

    hand1 = GOval(38, 28, x=200, y=312)
    hand1.color = "saddle brown"
    hand1.filled = True
    hand1.fill_color = "white"
    window.add(hand1)

    hand2 = GOval(38, 28, x=260, y=312)
    hand2.color = "saddle brown"
    hand2.filled = True
    hand2.fill_color = "white"
    window.add(hand2)

    l_chip = GOval(34, 18, x=196, y=262)
    l_chip.color = 'light pink'
    l_chip.filled = True
    l_chip.fill_color = "light pink"
    window.add(l_chip)

    r_chip = GOval(34, 18, x=268, y=262)
    r_chip.color = "light pink"
    r_chip.filled = True
    r_chip.fill_color = "light pink"
    window.add(r_chip)

    l_eye = GOval(38, 38, x=200, y=238)
    l_eye.color = 'black'
    l_eye.filled = True
    l_eye.fill_color = "black"
    window.add(l_eye)

    r_eye = GOval(38, 38, x=262, y=238)
    r_eye.color = "black"
    r_eye.filled = True
    r_eye.fill_color = "black"
    window.add(r_eye)

    l_eye_1 = GOval(18, 18, x=206, y=254)
    l_eye_1.color = 'white'
    l_eye_1.filled = True
    l_eye_1.fill_color = "white"
    window.add(l_eye_1)

    r_eye_1 = GOval(18, 18, x=266, y=254)
    r_eye_1.color = "white"
    r_eye_1.filled = True
    r_eye_1.fill_color = "white"
    window.add(r_eye_1)

    l_eye_2 = GOval(3, 3, x=221, y=245)
    l_eye_2.color = 'white'
    l_eye_2.filled = True
    l_eye_2.fill_color = "white"
    window.add(l_eye_2)

    r_eye_2 = GOval(3, 3, x=281, y=245)
    r_eye_2.color = "white"
    r_eye_2.filled = True
    r_eye_2.fill_color = "white"
    window.add(r_eye_2)

    l_eye_3 = GOval(6, 6, x=227, y=249)
    l_eye_3.color = 'white'
    l_eye_3.filled = True
    l_eye_3.fill_color = "white"
    window.add(l_eye_3)

    r_eye_3 = GOval(6, 6, x=287, y=249)
    r_eye_3.color = "white"
    r_eye_3.filled = True
    r_eye_3.fill_color = "white"
    window.add(r_eye_3)

    nose = GOval(8, 5, x=246, y=276)
    nose.color = "black"
    nose.filled = True
    nose.fill_color = "black"
    window.add(nose)

    mouse = GOval(28, 22, x=234, y=288)
    mouse.color = "salmon"
    mouse.filled = True
    mouse.fill_color = "salmon"
    window.add(mouse)

    mouse_1 = GRect(28, 8, x=234, y=288)
    mouse_1.color = "white"
    mouse_1.filled = True
    mouse_1.fill_color = "white"
    window.add(mouse_1)

    l_line = GLine(173, 276, 198, 280)
    l_line.color = "black"
    window.add(l_line)

    l_line_2 = GLine(175, 292, 200, 286)
    l_line_2.color = "black"
    window.add(l_line_2)

    r_line = GLine(298, 280, 325, 276)
    r_line.color = "black"
    window.add(r_line)

    r_line_2 = GLine(298, 286, 323, 292)
    r_line_2.color = "black"
    window.add(r_line_2)

    l_finger = GOval(4, 10, x=224, y=330)
    l_finger.color = 'gray'
    l_finger.filled = True
    l_finger.fill_color = "gray"
    window.add(l_finger)
    l_finger = GOval(4, 10, x=214, y=330)
    l_finger.color = 'gray'
    l_finger.filled = True
    l_finger.fill_color = "gray"
    window.add(l_finger)

    r_finger = GOval(4, 10, x=274, y=330)
    r_finger.color = "gray"
    r_finger.filled = True
    r_finger.fill_color = "gray"
    window.add(r_finger)
    r_finger = GOval(4, 10, x=282, y=330)
    r_finger.color = "gray"
    r_finger.filled = True
    r_finger.fill_color = "gray"
    window.add(r_finger)

    label = GLabel("Hello!")
    label.font = '-40'
    label.color = 'navy'
    label.move((window.width - label.width)/2, 140)
    window.add(label)


####### DO NOT EDIT CODE BELOW THIS LINE ########
if __name__ == '__main__':
 main()