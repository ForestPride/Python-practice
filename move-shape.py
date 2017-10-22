from graphics import *

def moveShape(shape, newCenter):
    # get the old center.
    oldCenter = shape.getCenter()
    # move the shape to the new center.
    shape.move(newCenter.getX() - oldCenter.getX(),
    newCenter.getY() - oldCenter.getY())

def main():
    # draw a window
    win = GraphWin("move the circle", 800, 600)
    # get a point from the mouse click.
    point = win.getMouse()
    # draw a circle at Point.
    shape = Circle(point, 10)
    shape.draw(win)
    # get a new point each time the mouse clicks.
    for i in range(10):
        newCenter = win.getMouse()
        # move the shape to the new center position.
        moveShape(shape, newCenter)
main()
