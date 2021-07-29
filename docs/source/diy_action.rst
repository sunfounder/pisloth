DIY Action
===============

Through the previous courses, do you have a deeper understanding of Pisloth? And next let’s try to design the movement of Pisloth by ourselves.

**Code**

.. code:: python

    from pisloth import Sloth
    import time

    sloth = Sloth([1,2,3,4])
    sloth.add_action("my_action", [
        [ 45,0  ,0, 0],
        [0,   0, 0,   0]
        ])

    def main():
        sloth.do_action("my_action", 1, 80)
        time.sleep(1)
        
    if __name__ == "__main__":
        while True:
            main()  

**How it works?**

You can customize the action of Pisloth through the ``add_action`` function, the first parameter is the name of the action,
The second parameter is a two-dimensional array. The four parameters in the array are used to control the four servos of the Pisloth leg. 
For how to choose the value we will introduce it in detail in the next lesson.

.. code:: python

    sloth = Sloth([1,2,3,4])
    sloth.add_action("my_action", [
        [ 45,0  ,0, 0],
        [0,   0, 0,   0]
        ])

Then use the ``do_action'' function to make pisloth do the action to see the actual effect.