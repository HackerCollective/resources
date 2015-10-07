Learning [Famo.Us](http://famo.us/)
=====
[![forthebadge](http://forthebadge.com/badges/certified-cousin-terio.svg)](http://forthebadge.com)

## [FamoUs University](http://famo.us/university/) - Famo.us 101

These are my notes, take em' or leave em. These are not *approved* specifications but rather my intrepretation of how to leverage the famous framework, based on tutorials, searching, asking questions, and implementation. The learning curve is pretty shallow compared to your typical MVC js framework, so I think its great for beginners. It does a lot of content rendering with JS which I also think is very cool. I also decided to dive in because of its native mobile approach, and 3D engine. They are just superb. And with that lets begin! :)

## <a name='toc'>Table of Contents</a>

  1. [Developing Content](#intro)
  2. [Styling](#tutorial)
    - [Surface Sizing]()
    - [Positioning]()
  3. [Creating Animations](#zen)
  4. [Handling Events]()

### [[⬆]](#toc) <a name='intro'>Developing Content/a>

#### Developing Content
Famous has a rendering engine that displays content to the DOM.  One of the type of rendering is called **surface**, which maps to a ```<div>``` element in the DOM

Renderings live in, **Contexts**, which themselves are not displayed. They are isolated rendering environments that tell the Engine where renderables live.

Call dependecies for **surfaces** and **Contects**
```javascript 
var Engine = require('famous/core/Engine');
var Surface = require('famous/core/Surface');

var mainContext = Engine.createContext();
```

Content that exist in the **surface**, rendered by **Contexts** can be a string, HTML, or a DOM element. The content can be set when you initialize your surface or by the ```.setContent()``` method.

Push your **surface** to the DOM via 
```javascript 
mainContext.add(firstSurface); 
```
The **Hello, World!** example below is a basic **surface**.
```javascript
var Engine = require('famous/core/Engine');
var Surface = require('famous/core/Surface');

var mainContext = Engine.createContext();
var firstSurface = new Surface({
  content: 'hello world',
});

mainContext.add(firstSurface);
```


#### Styling

You begin styling a surface with adding a **properties** section in your instantiation. Styling a  **surface** is pretty much the same as CSS, but you replace your dashes with camelCase. So instead of ``` text-align```  its now ```textAlign``` For example:

```javascript
var firstSurface = new Surface({
  content: 'hello world',
  properties: {
    color: 'white',
    textAlign: 'center',
    backgroundColor: '#FA5C4F'
  }
});

mainContext.add(firstSurface);
```

To make your surface a particular **size**  you must add it to your surface object. If you do not specify, the surface inherits the size of its parent--the context.
```javascript
var firstSurface = new Surface({
  size: [200, 400],
  content: 'hello world',
  properties: {
    color: 'white',
    textAlign: 'center',
    backgroundColor: '#FA5C4F'
  }
});

mainContext.add(firstSurface);
```
##### Surface Size:
- In pixels with [x, y]
- In only one dimension with [undefined, y] or [x, undefined]. For example,  [undefined, 200] will span the entire length of the x-direction, while only 200 pixles in the y direction. [, ] also works. 
- Have the surface auto-size according to the content with [true, true]. You can put in any statement that evaluates to [true, true]. For example, [1>3, 1>3], [false, false], and [null, null] all work.

##### Positioning
With positioning we add two more requirements; **Transform** and **State Modifier**. The **State Modifier** is an object that is used to translate or move a surface. **Transform** on the other hand is a little more implicit. Instead of traditional positioning surfaces are styled with position:absolute and their positions are defined by matrix3d webkit transforms. More on [Transforms Expanded](https://famo.us/guides/layout).

This means we now have to add more to our method call. Which now looks like this ```mainContext.add(stateModifier).add(surface);```, to  push our newly positioned surface to the DOM. 

Example of a positioned **surface** using **Transform** and **State Modifier** 
```javascript
var Engine = require('famous/core/Engine');
var Surface = require('famous/core/Surface');
var Transform = require('famous/core/Transform');
var StateModifier = require('famous/modifiers/StateModifier');

var mainContext = Engine.createContext();

createModifiedSurface();

function createModifiedSurface() {
  var modifiedSurface = new Surface({
    size: [100, 100],
    content: 'modified surface',
    properties: {
      color: 'white',
      textAlign: 'center',
      backgroundColor: '#FA5C4F'
    }
  });

  var stateModifier = new StateModifier({
    transform: Transform.translate(150, 100, 0)
  });

  mainContext.add(stateModifier).add(modifiedSurface);
}
```
Now on to rotation! This part is pretty dense, so I'll separate it into sections. 
```javascript
var Engine = require('famous/core/Engine');
var Surface = require('famous/core/Surface');
var StateModifier = require('famous/modifiers/StateModifier');
var Transform = require('famous/core/Transform');

var mainContext = Engine.createContext();
```
Here we're making sure we have the correct dependencies, and everything we need to create **surfaces**, **Context** s, **Transform** s, and **State Modifiers**. This example involves 2 **Context** s and 2 **surfaces**.

--- 

```javascript
var translateModifierOne = new StateModifier({
  transform: Transform.translate(200, 0, 0)
});

var translateModifierTwo = new StateModifier({
  transform: Transform.translate(200, 0, 0)
});

var rotateModifierOne = new StateModifier({
  transform: Transform.rotateZ(Math.PI/4)
});

var rotateModifierTwo = new StateModifier({
  transform: Transform.rotateZ(Math.PI/4)
});
```
Here we are doing four things. 
  1. Making a **State Modifier** that will use **Transform** to *TRANSLATE* our surface by 200 pixles in the x direction. This will be applied our first **Context**
  2. Making a **State Modifier** that will use **Transform** to *TRANSLATE* our surface by 200 pixles in the x direction. This will be applied our second **Context**
  3. Making a **State Modifier** that will use **Transform** to *ROTATE* our surface by PI/4 degrees over the z-axis. This will be applied our first **Context**
  4. Making a **State Modifier** that will use **Transform** to *ROTATE* our surface by PI/4 degrees over the z-axis. This will be applied our second **Context**
  
--- 

  
```javascript
var redSurface = new Surface({
  size: [100, 100],
  classes: ['red-bg']
});

var greySurface = new Surface({
  size: [100, 100],
  classes: ['grey-bg']
});
```
Now we are creating our  **surfaces**, in this case we are making one for each **Context**

--- 

```javascript
mainContext
  .add(translateModifierOne)
  .add(rotateModifierOne)
  .add(redSurface);

mainContext
  .add(rotateModifierTwo)
  .add(translateModifierTwo)
  .add(greySurface);
```

Finally we are assigning the **surfaces**, **State Modifiers**, and  **Transforms** to the **Context** s we made earlier.

--- 

**Note**:  Order that you chain modifiers matters! The red surface has its translation applied before the rotation which causes it to be moved and THEN rotated about its origin. However the grey surface is rotated and THEN translated, which because it is rotated PI/4 translated. Because it was rotated first, it is now translated along that angle, instead of linearly like the red square. Causing it to be both below, and further to the left than the red square. 

More positioning!

```javascript
var downMod = new StateModifier({
  transform: Transform.translate(0, 100, 0)
});

var rightMod = new StateModifier({
  transform: Transform.translate(150, 0, 0)
});

var node = mainContext.add(downMod);
node.add(leftSurface);
node.add(rightMod).add(rightSurface);
```
The important component is that you can add ```.add(downMod);``` to all the surfaces simultaneously. By setting our **Context** as a a variable, and then method chaining it with our surfaces and our **State Modifier** s

```javascript
var alignOriginModifier = new StateModifier({
  align: [0.5, 0.5],
  origin: [1, 1]
});
```
**Align** sets the anchor point on the parent element, while **Origin** sets the anchor point on the child element. **Origin** is also the point about which transforms get applied. By default, **origin** is set to [0, 0], a rotation **transform** defaults to rotating about the top left corner.

##### Opacity
Opacity is added to a **State Modifier** just like everything else, ```opacity: 0.5 ```. Everything that gets added to the render tree after that modifier gets that opacity value multiplied to its current opacity.

```javascript
  var modifier = new StateModifier({
  opacity: 0.5,
  transform: Transform.scale(1, 3, 1),
  align: [0.5, 0.5],
  origin: [0.5, 0.5]
});
```
#### Creating Animations
Now we introduce the ```.setTransform()``` method. ```.setTransform()``` takes in a **transform** argument and can also be passed two additional arguments: a **transition object** which defines the animation. This the transition from **transform**'s current value to its new value.  The second argument is the **callback function**. 

In addition, we also need to add another dependency ```var Easing = require('famous/transitions/Easing');```

```javascript
  stateModifier.setTransform(
  Transform.translate(100, 300, 0),
  { duration : 1000, curve: 'easeInOut' }
);
```
To chain animations, simply call your wanted  stateModifier.setTransform's back to back. 
**Note**: that this method only works for chaining .setTransform() on the same state modifier. If you want to chain animations between modifiers, use a completion callback.

You can interrupt an animation before it's over by calling .halt() on the state modifier.

```javascript
surface.on('click', function() {
  stateModifier.halt();
  surface.setContent('halted');
});
```

Physics transitions can give animations a more realistic feel and can be tuned more precisely. (I like these better). For this, we need to add a few more dependecies, but we can take out the easing one. 

```javascript
var Transitionable = require('famous/transitions/Transitionable');
var SpringTransition = require('famous/transitions/SpringTransition');
Transitionable.registerMethod('spring', SpringTransition);
```
There difference is the last part, where instead of bringing in a dependency, we register the spring transition to the transition object with method 'spring'. 

Our last steps are to specify the parameters and apply the transition. Which looks like:

```javascript
var spring = {
  method: 'spring',
  period: 1000,
  dampingRatio: 0.3
};

stateModifier.setTransform(
  Transform.translate(0, 300, 0), spring
);
```

#### Handling Events
1. Surface events
2. Engine events
3. Program events

For the use of events we must include the dependency ```var EventHandler = require('famous/core/EventHandler');```

**surfaces**capture all the falling DOM events listed, and can be registered  with a callback function using the .on() method; click, mousedown, mousemove, mouseup, mouseover, mouseout, touchstart, touchmove, touchend, touchcancel, keydown, keyup, keypress.

Example of a **surface** event, that when click changes the text 'click me' to 'Gennevi is sexy!' :

```javscript
var surface = new Surface({
  size: [undefined, 100],
  content: 'click me',
  properties: {
    color: 'white',
    textAlign: 'center',
    backgroundColor: '#FA5C4F'
  }
});

mainContext.add(surface);

surface.on('click', function() {
  surface.setContent('Gennevi, is Sexy!');
});
```
Document events interact first with the surface that involved, then using the ```.on()``` method they can interact the **Context** containing the **surface**, and then as a default the engine itself. 

We can emit, transmit, and listen to program events using Event Handler objects. This is our second case, the Engine handlers.
```javascript
var eventHandler = new EventHandler();

surface.on('click', function() {
  eventHandler.emit('hello');
});

eventHandler.on('hello', function() {
  surface.setContent('heard hello');
});
```

We have a surface that one clicked emits an event as a string ```'hello'```, and once that string is emitted it is captured with our eventHandler which then switches whatever initial content to 'heard hello'. 

We also have Program Events. 
Example: Program Event - Event Handler
```javascript
var eventHandlerA = new EventHandler();
var eventHandlerB = new EventHandler();

surfaceA.on('click', function() {
  eventHandlerA.emit('hello');
  surfaceA.setContent('said hello');
});

eventHandlerB.subscribe(eventHandlerA);

eventHandlerB.on('hello', function() {
  surfaceB.setContent('heard hello');
});
```

Event handler A emits 'hello' when surface A is clicked. Event handler B listens for the 'hello' event and calls surface B to set its content when the event is triggered.

This logic alone does not produce any results when surface A is clicked because the two event handlers are not transmitting to each other. To do so, event handler B has to subscribe to event handler A using ```.subscribe()``` When event handler B subscribes to event handler A, all events emitted from event handler A will be heard by event handler B.

Now we have Program Events - Pipe & Subscribe

An alternative to ```.subscribe()``` is ```.pipe()```, which directly sends the emmited events from one handler to another. 

```javascript
surfaceA.on('click', function() {
  eventHandlerA.emit('hello');
  surfaceA.setContent('said hello');
});

eventHandlerA.pipe(eventHandlerB);

eventHandlerB.on('hello', function() {
  surfaceB.setContent('heard hello');
});
```
Pipe VS. Subscribe, from your friendly stackoverflow.

>If you do widgetA.pipe(widgetB) then all events from widgetA are sent to widgetB regardless whether widgetB is listening to them. Pipe is like a firehose.

>Subscribe on the other hand, is more performant. WidgetB.subscribe(widgetA) says "of the things you emit, I want to subscribe to a particular subset." Other events are then completely ignored.

>This is especially important when interacting with the DOM, which outputs a lot of events (mousedown, mouseup, touchmove, resize, etc...), and it's preferred to use Subscribe when listening to a DOM element.

Program Events - Views

When you pipe into a view or subscribe from a view, you're actually piping into or subscribing from the input event handler of a view, called ```view._eventInput```.

a view's input handler is the aggregation point of all the events coming into that view. The view can then decide what to do with those events by listening on it's  ```_eventInput ```. For views you also need to include the view dependency, ```var View = require('famous/core/View');```.

View Example:
```javascript
var myView = new View();
mainContext.add(myView);

var surface = new Surface({
  size: [100, 100],
  content: 'click me',
  properties: {
    color: 'white',
    textAlign: 'center',
    backgroundColor: '#FA5C4F'
  }
});

myView.add(surface);

surface.pipe(myView);
// alternatively, myView.subscribe(surface);
// normally inside view module's code
myView._eventInput.on('click', function() {
  surface.setContent('hello');
});
```

Views can broadcasts an event to the outside world from its output handler. Outside of the view, we use ```.on()``` to listen for those events.
```javascript
myView._eventInput.on('click', function() {
  myView._eventOutput.emit('hello');
});
```

###### Best Practices
- A Famo.us app can have more than one context, but a mobile app or full-page web app usually just uses one.
- The order that you chain modifiers matters!
- Listening on Engine events is a catch-all but in most applications, you'll want to capture the events at a lower level.

# [FamoUs University 102](http://famo.us/university/lessons/#/famous-102/) 

#Layouts

## Header & Footer

```javascript
var Engine = require('famous/core/Engine');
var Surface = require('famous/core/Surface');
var HeaderFooterLayout = require("famous/views/HeaderFooterLayout");

var mainContext = Engine.createContext();
```
As always, make sure that you include your propper dependencies so that you can use all the features you want. The only new one in this case is the **Header** and **Footer** which van both be found in the views folder.

```javascript
var layout = new HeaderFooterLayout({
  headerSize: 100,
  footerSize: 50
});
```

```javascript
layout.header.add(new Surface({
  content: "Header",
  properties: {
    backgroundColor: 'gray',
    lineHeight: "100px",
    textAlign: "center"
  }
}));
```

```javascript
layout.content.add(new Surface({
  content: "Content",
  properties: {
    backgroundColor: '#fa5c4f',
    lineHeight: '400px',
    textAlign: "center"
  }
}));
```

```javascript
layout.footer.add(new Surface({
    content: "Footer",
    properties: {
        backgroundColor: 'gray',
        lineHeight: "50px",
        textAlign: "center"
    }
}));
```

Layouts will fill the size of its parent modifier or context. In our example it fills the size of our main context.


#### [Demos](http://famous.org/)
#### [Guides](https://github.com/Famous/famous/tree/master/guides)
  * animations
  * events
  * layout
  * migrating-0.2-to-0.3
  * pitfalls
  * render-tree
  
#### [Projects]()
