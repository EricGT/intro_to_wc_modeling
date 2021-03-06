.. _vector_graphics:

Drawing vector graphics with Adobe Illustrator and Inkscape
===========================================================
Broadly, there are two types of graphics: vector graphics and raster graphics. Vector graphics are combinations of elemental graphical objects such as lines, curves, arcs, ellipses, text, strokes, fills, and gradients. Consequently, vector graphics are vector graphics are infinitely scalable (i.e. they never become pixelated when they are enlarged) and well-suited for scientific diagrams. Two of the most common vector graphic editing programs are `Illustrator <https://www.adobe.com/products/illustrator.html>`_ and `Inkscape <https://inkscape.org>`_. Some of the most common file formats used to store vector graphics include .ai, .eps, .pdf, and .svg.

Raster graphics are matrices of colored pixels. Raster graphics are commonly used to describe photographs as well as to display graphics originally created as vector graphics in websites and other documents. Some of the most common raster graphic editing programs are `Photoshop <https://www.adobe.com/products/photoshop.html>`_ and `Gimp <https://www.gimp.org/>`_. Photoshop is a commercial program developed by Adobe and Gimp is a free, open-source program. Photoshop is the standard among graphics professionals, but Gimp is easier to learn and sufficient for our needs as scientists. Some of the most common file formats used to store raster graphics are .gif, .jpg, and .png format.

In this tutorial, we will teach you how to draw vector graphics with Illustrator and Inkscape by drawing a picture of a cell.

Key concepts
------------

* Raster graphics vs. Vector graphics
* Fundamental vector graphic objects
* Color models
* Selecting and editing graphical objects
* Grouping objects
* Masking objects
* Exporting diagrams


Fundamental vector graphic objects
----------------------------------
As introduced above, vector graphics are composed of the following elemental graphical objects:

* Paths

    * Bezier curves
    * Lines

* Shapes

    * Circles
    * Ellipses
    * Polygons
    * Rectangles

* Text
* Fills and strokes

    * Solid
    * Gradient

* Groups
* Masks
* Layers


Color models
------------
Vector graphics can be described using one of several common color models:

* CMYK (Cyan, Magenta, Yellow, Black): CMYK is a subtractive color model which represents colors as tuple of cyan, magenta, yellow, and black values, each of which ranges from 0 to 100%. CMYK is the native color model for many printers. For this reason, some journals prefer CMYK.
* RGB (Red, Green, Blue): RGB is an additive color model which represents colors as tuples of red, green, and blue values, each of which ranges from 0 to 255. RGB is the native color model for many monitors. For this reason, RGB is most common color model for web-based graphics and some journals prefer RGB.
* HSB (Hue, Saturation, Brightness) / HSV (Hue, Saturation, Value): HSB is a cylindrical color model which makes it easy to manipulate saturation and brightness separately from color. For this reason, HSB is useful to designing color palettes.
* Grayscale: is an additive color model which represents colors as integers between 0 and 255.

Illustrator supports all four of these color models, and documents created in any one of these color models can be exported to any of the other color models. Inkscape only supports the RGB color model.

We recommend using RGB except for submissions to journals which require CMYK figures.


Vector graphics drawing tools: Illustrator vs Inkscape
------------------------------------------------------
Illustrator and Inkscape are two of the most popular vector graphics editing programs. Illustrator is a commercial program developed by Adobe and Inkscape is a free, open-source program. Illustrator is the industry standard and is more powerful than Inkscape.

Illustrator and Inkscape share many of the same core functionality. However, Inkscape lacks many of the more advanced features of Illustrator. In addition, Illustrator is substantially faster than Inkscape, especially for large graphics. This is critical for editing complex plots generated by graphing utilities such as matplotlib. Furthermore, there are substantially more tutorials and examples for Illustrator than for Inkscape. However, some people find Inkscape easier to learn. Below is a list of some of the limitations of Inkscape compared to Illustrator.

* Significantly slower for complex graphics
* Interface is less polished
* Poor default options for subscripts, superscripts
* No linked text boxes for continued text flow
* No tool to edit spacing of dashes
* No CMYK support
* No native support for a binary file format such as .ai
* Less control over .png export
* No .gif, .jpg export


Vector graphics file formats
----------------------------
Some of the most common file formats used to represent vector graphics include AI, EPS, PDF, and SVG. AI is a proprietary and efficient binary format that is used by Illustrator. SVG (Scalable Vector Graphics) is an XML-based open standard for describing vector graphics and the native format for Inkscape. Because SVG is an XML format, SVG is easy to generate programmatically. However, because SVG is an XML format, SVG is also inefficient and poorly suited to large graphics such as complex plots created by matplotlib. EPS and PDF are binary vectors graphics formats that are supported by both Illustrator and Inkscape. Consequently, these formats should be used to provide graphics to journals.


Required software
-----------------
This tutorial requires Illustrator and Inkscape.

On Ubuntu, you can use this command to install Inkscape::

    sudo apt-get install inkscape


Illustrator exercise
--------------------
In this exercise we will learn how to use Illustrate by drawing a digram of a cell

#. Open Illustrator
#. Set the canvas units size
#. Use the ellipsis tool to draw a cell
#. Set the stroke and fill color
#. Add a drop shadow
#. Add a straight line into the cell
#. Add an arrow head to the line
#. Turn the line into a curve
#. Copy the line to create a line out of the cell
#. Add a textual label on top of the cell
#. Create a mask to highlight the area that you want to highlight

    #. Draw a rectangle over the area you want to highlight
    #. Select the rectangle and all of the graphical element below it
    #. Create the mask

#. Save the diagram in AI format
#. Save the diagram to PDF format to use in manuscripts
#. Export the diagram to PNG format to use in PowerPoint and websites

Other useful features
^^^^^^^^^^^^^^^^^^^^^

 * Selecting similar objects
 * Joining lines
 * Placing other documents


Screen capture
^^^^^^^^^^^^^^
.. raw:: html

    <object data="../../_static/tutorials/scientific_communication/vector_graphics/screen_capture.swf" width="697" height="413" >
    </object>

`Open the screen capture in a separate page <../../_static/tutorials/scientific_communication/vector_graphics/index.html>`_

Inkscape exercise
---------------------
In this exercise we will learn how to use Inkscape by drawing a digram of a cell

#. Open Inkscape
#. Set the size of the canvas

    #. Open "File" >> "Document Properties..."
    #. Set "Units" to "in"
    #. Set "Width" to "7.5"
    #. Set "Height" to "5"
    #. Close the window
    #. Type "5" to fit the canvas to your screen

#. Draw the cell membrane

    #. Select the ellipse tool
    #. Drag an ellipse over the canvas
    #. Right click on the ellipse and select "Fill and Stroke..." to edit the line and fill colors and line style of the membrane.

        #. Increase the stroke width of the membrane
        #. Change the stroke style of the membrane to dashed
        #. Apply a radial gradient fill to the body of the membrane
        #. Adjust the center and shape of the radial gradient

    #. Add a drop shadow to the cell by selecting "Filters" >> "Shadows and Glows" >> "Drop Shadow..."

#. Draw an arrow into the cell

    #. Select the Bezier curves tool
    #. Select one or more points on the canvas. Optionally, hold down the control key to draw a straight line.
    #. Double click to finish the curve
    #. Optionally, use the "Align and Distribute" tool to straighten the line
    #. Use the edit path tools to fine tune the curve
    #. Right click on the line and select "Fill and Stroke..." >> "Stroke style" to apply arrow markers to the line

#. Create an arrow which points out of the cell by copying the first arrow

    #. Left click on the first arrow and hold down
    #. While still holding down the left mouse button, click the space bar
    #. Begin dragging your mouse
    #. Press down the control key to constraint the dragging so that the second arrow is vertically aligned with the first

#. Vertically align the cell and lines

    #. Open the "Align and distribute objects" window
    #. Select both the cell and line
    #. Click the "Center on horizontal axis" button to align the objects

#. Add a label to the cell

    #. Select the text tool
    #. Click on the canvas where you want the text to appear
    #. Type "Cell"
    #. Right click on the label and select "Text and Font..." to adjust the font type, font size, text color, and text alignment
    #. Use the dropper tool to copy the cell stroke color to the text
    #. Bring the text in front of the cell by selecting "Object" >> "Raise to Top"

#. Group the cell and label

    #. Select the cell and label
    #. Select "Object" >> "Group"
    #. Now you can move the objects together
    #. Double click on the combine object to access the individual cell and label objects

#. Highlight a specific part of the cell

    #. Draw a rectangle over the portion of the cell that you would like to highlight
    #. Select both this new rectangle and the cell
    #. Right click on the objects and select "Set Mask"

#. Save the diagram

    #. Select "File" >> "Save"
    #. For simple graphics, choose the "Inkscape SVG (.svg)" format. For complex graphics, choose the "Compressed Inkscape SVG (.svgz)" format.

#. Export the diagram

    #. Select "File" >> "Export PNG Image..."
    #. Set the desired export size and resolution


Other useful features
^^^^^^^^^^^^^^^^^^^^^

Selecting other objects with the same fill and/or stroke
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

* Select an object
* Right click on the object and select "Select Same" >> "Fill and Stroke"


Joining lines
"""""""""""""

* Use the "Edit paths by node" to select a node in a curve
* Hold to the shift key and select another node in another curve
* Click the "Join selected nodes" button to join the curves


Embedding graphics
""""""""""""""""""

* Select "File" >> "Import"
* Select the file that you wish to import
* Select whether to "Embed" or "Link" the imported file


Additional tutorials
--------------------

Illustrator
^^^^^^^^^^^
`Kevin Bonham <https://www.youtube.com/watch?v=z2bcqyRxFrI&list=PLhKpKEPEAauYIsyjnIN2YXztNo7BrZVxQ>`_ has several helpful tutorials videos designed for scientists. `Skill Developer <https://www.youtube.com/watch?v=mqJ8FyJwShw&list=PLSraMTfTYtEIrn__P9EzxFY5bYHEPC6gS>`_ also has a large number of brief tutorial videos.

Inkscape
^^^^^^^^
`Derek Banas <https://www.youtube.com/watch?v=zUIOEXssTSE&list=PLGLfVvz_LVvTSi9bKrvGR2_DBg0Tv8Dxo>`_ has several helpful short tutorial videos. The `Inkscape Tutorials Blog <https://inkscapetutorials.org/>`_ has numerous examples of how to draw a variety of graphics.
