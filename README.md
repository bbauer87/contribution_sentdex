# Dinamic use of classes for sentdex Tkinter tutorial
Following [Sentdex](https://github.com/Sentdex) tutorial in Youtube [Multiple Windows/Frames in Tkinter GUI with Python - Tkinter tutorial Python 3.4 p. 4](https://www.youtube.com/watch?v=jBUpjijYtCk&list=PLQVvvaa0QuDclKx-QpC9wntnURXVJqLyk&index=4), you have to hardcode a line each time you create a new class that's a page.

This solution try to offer a dinamic way of iterating throught the classes that should be in SeaofBTCapp's constructor loop.

# Changes needed
1 - Every class that is a page to be shown need to have a name pattern, like start with "Page";

2 - SeaofBTCapp's method "show_frame" now must pass in "string way" the class name. So you need to change all the method's callings.
