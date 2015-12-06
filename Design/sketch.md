Learning [Sketch](https://www.sketchapp.com/)
=====
[![forthebadge](http://forthebadge.com/badges/certified-cousin-terio.svg)](http://forthebadge.com)

These are my notes, take em' or leave em. These are not *approved* specifications but rather my intrepretation of how to leverage the Sketch framework, based on tutorials, searching, asking questions, and implementation. 
## Awesome Plugins

These plugins are easily managed if you download [Sketch Toolbox](sketchtoolbox.com)
 1. [Effortless Placeholder Images in Sketch](https://www.youtube.com/watch?v=oQnggDiV1vA&list=PLLnpHn493BHHUZe9bihv37Z6CyXBTyb-9&index=1)
 2. [Easy Content Generation In Sketch](https://www.youtube.com/watch?v=EPljMDOjeuo&list=PLLnpHn493BHHUZe9bihv37Z6CyXBTyb-9&index=2) 
 3. [Annotations For Your Designs With Sketch Measure](https://www.youtube.com/watch?v=lHKt491yqls&index=3&list=PLLnpHn493BHHUZe9bihv37Z6CyXBTyb-9) This actually measures all of the objects on your page and adds labels. One of my **favorite** tools. Provides all of the values for margins in layouts, fonts, etc.
 4. [Better Distributing With Sketch Distributor](https://www.youtube.com/watch?v=BzZKMQe1qQk&list=PLLnpHn493BHHUZe9bihv37Z6CyXBTyb-9&index=4) This allows you to select some items and distribute these layers, and specify the distance between these layers. Instead of simply equally distributing them it will distribute them at a given distance apart. For instance, if you're making a list and want the item each to be 20px a part, distributor allows you to do it easily!
 5. [Better Pasting In Sketch](https://www.youtube.com/watch?v=xv511oaJo0g&list=PLLnpHn493BHHUZe9bihv37Z6CyXBTyb-9&index=5) Fixes some of the inherent issues with Sketch's copy and pasting. ```ctrl + v```
 6. [CSS Layouts In Sketch](https://www.youtube.com/watch?v=EmXXzvrz_vs&index=6&list=PLLnpHn493BHHUZe9bihv37Z6CyXBTyb-9) Allows you to use CSS rules including flexboxe properties to control your layouts. See the [rules](https://github.com/hrescak/Sketch-Flex-Layout)
 7. [Dynamic Artboard Mirroring With Magic Mirror](https://www.youtube.com/watch?v=Gm5wPXOgVtM&list=PLLnpHn493BHHUZe9bihv37Z6CyXBTyb-9&index=9). Shift your artboard into different perspectives
 

### Fonts
Paste the following code to download all of the google fonts onto your computer (~500mb)

```curl https://raw.githubusercontent.com/qrpike/Web-Font-Load/master/install.sh | sh```

#### Using Sketch Measure
- Measuring circles. Create overlay over your element that is measured using ```ctrl + shift + 1``` Particularly if you are measuring the distance between circles, as they take up squares in the DOM. 
- Dimensions of an element: select your layer, and press ```ctrl + shift + 2``` , this will initiate a resolution box. Once you pick your size you will get the measurement of any elements you select.
- Measurement between two objects: ```ctrl + shift + 3```
- Typography information: After selecting text, ```ctrl + shift + 4``` will present information such as size, font, color (hex and rgb).
- Element Properties: Select your element and press ```ctrl + shift + 5```, this will then open a pop up asking which properties you'd like;  **Fill / Color / Gradient, Border Color, Layer Opacity, Shadow, Inner Shadow**
- Labels: Maybe you have multiple elements overlayed, like a play button. Play buttons often have a circle and a triangle, which may have different properties. If you want to turn text into a label so you can easily differentiate your measures, first create some text, select that text and then press ```ctrl + shift + 5```
- Hide measures: Maybe you want to go back into design mode. ```ctrl + shift + H``` to toggle the measures into hidden. 
- Lock Measures in place: ```ctrl + shift + L``` to lock your measures where they are on the page so that you don't accidently select and move them.

#### CSS Layouts In Sketch
- to activate press ``` ctrl + cmd + L```
 

### [Shortcuts](http://sketchshortcuts.com/)
- Create Artboard ``` a```
- Duplicate: ``` CMD +D ```
- Turn element into folder: ``` CMD +g ```
- Text Box: ``` t```
- Oval: ```o```
