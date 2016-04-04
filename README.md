# Week 12 Deliverables (E8) - Due 4/12/16
For this week make sure that you have completed the following:
    
* Fork Assignment 9 to your own github repository.
    * You can access assignment 9
      [HERE](https://github.com/Geospatial-Python/assignment_09)
* Clone the repository locally

## Deliverables
1. Create a GUI application that can be launched from a script named `view.py`.
   The GUI should include:
    * A single window (QMainWindow or QWidget)
    * A `File` menu with at least one entry - `Quit`.  The quit item should
      exit the program.
    * The code should be presented using the following conventions:
        a. Include an `if '__name__' == __main__:` block
        b. Write your GUI in a class, inhereting from QMainWindow, QWidget, or
another appropriate parent.  You should have at least an `__init__` method and
a `init_ui` method.
        c. Call a function called `main` when the application is launched and
an instance of your GUI class is created
    * A central widget.  This can be an empty widget, a text box, a graphic -
      we will replace this next week with something else, so the important part
for now is having something in the window.
    
    Note: For the above requirements, the linked readings offer step-by-step
examples of how to achieve this.
1. If you wrote a script for last week demonstrating your point pattern
   analysis code, please move that code into an iPython notebook.  Extend the
notebook to:
    * Plot the point pattern.  To do this, please write a function that takes
      two vectors (x, y) as arguments and then generates a plot.  
    * Plot the results of the G-function.  You can see an example of this in a
      previous week's readings.  In addition to plotting the observed function,
plot the upper and lower confidence thresholds in a different line color.  For
example, if the observed value is red, then the upper and lower thresholds
(with p=0.05 maybe) could be blue.
    
    Hint: To get plots to automatically display in a notebook add `%pylab
inline` to the first cell (where your other imports are)
1. Update any other support code as necessary.
