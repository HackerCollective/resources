Frontend Web Dev Resources
===============================

## Intro
Web Development, "is a mix of programming and layout that powers the visuals and interactions of the web."--[Nick Schaden](https://blog.generalassemb.ly/what-is-front-end-web-development/)

## <a name='toc'>Table of Contents</a>

  1. [HTML](#html)
  1. [CSS ](#css)
  1. [Javascript ](#js)
  1. [Design ](#design)
  1. [Unit Testing ](#ut)
  1. [Frontend Build Tools](#fbt)
  1. [Resources For Learning](#resources4learn)
  1. [Getting your website online](#online)
    1. [Domain Name Registration: + Hosting:](#dnrh)
    2. [FTP:](#ftp)
  1. [Using Github](#github)
    1. [Learning Git](#git)
  1. [Getting The Job](#job)

####[[⬆]](#toc)

[Code Database](https://docs.google.com/spreadsheet/ccc?key=0Au-8f__TLXEddGlHSFFhZG1TcnIwaFdxZVVVcXhxN3c&usp=sharing): Used to reference different things you can implement in your code, so that you don’t have to google how to do everything. (Please feel free to edit, revise, and add as well)



1. First things first, what are you going to code in? Before coding, you must download a **text editor**! This allows you to write code that will then be readable by browsers. (_The following text editors are ordered in my preference_)

    1. [Brackets](http://brackets.io/) | a text editor made for web developers, in javascript. I think its awesome.
    2. [Sublime Text](http://www.sublimetext.com/) | I love the colors, and the vast amount of languages it works for | works for all the following web dev. languages *RECOMMENDED FOR BEGINNERS* If you do decide to pick sublime, I recommend downloading two important packages that will streamline your coding: Emmet and SFTP.
    3. [Atom](https://atom.io/) | Made by GitHub, an open source text editor, there is a lot of potential for customizibility
    4. [Vim](http://www.vim.org/) | Vim, is a very old but highly robust editor.
    5. Text Wrangler (Mac App)
    6. Notepad / Notepad ++

---




## The Break Down
### [[⬆]](#toc) <a name='html'>HTML:</a>
 HTML, is essentially the skeleton of your webpage, it is what builds the structure of your site / app.
Tutorials / Guides


### [[⬆]](#toc) <a name='css'>CSS:</a>
CSS, can be thought of as the skin, the appearance, the beauty of your webpage. Its where the design comes in, and where your UI/UX comes into play.

1. Precompilers
    1. [Sass](http://sass-lang.com/)
    2. [Less](http://lesscss.org/)
    3. [Stylus](http://learnboost.github.io/stylus/)
2. Frameworks
    1. [Bootstrap](http://getbootstrap.com/)
    2. [Foundation](http://foundation.zurb.com/)
    3. [Animate.css](https://github.com/daneden/animate.css)
    4. [Typeplate](http://typeplate.com/)
    5. [Pure](http://purecss.io/)
    6. [Odometer](http://github.hubspot.com/odometer/docs/welcome/) (JS + CSS)

### [[⬆]](#toc) <a name='js'>Javascript:</a>
JavaScript provides interaction, functionality, and dynamic ability of your site/app.

1. MV* Javascript
    1. [Knockout.js](http://knockoutjs.com/)
    2. [Angular.js](https://angularjs.org/)
    3. [Meteor.js](https://www.meteor.com/)
    4. [Passport.js](http://passportjs.org/)
    5. [Ember.js](http://emberjs.com/)
    6. [Ampersand.js](http://ampersandjs.com/), A highly modular, loosely coupled, non-frameworky framework for building advanced JavaScript apps.
    7. [Backbone.js](http://backbonejs.org/)
    8. [UI-Lang](http://uilang.com/)
    9. [Famous](https://famo.us/), native mobile feel with the power of js. #TheJQueryKiller
    10. [React](http://facebook.github.io/react/)
2. Gen Frameworks
    1. [Unheap](http://www.unheap.com/)
    2. [Transit](http://ricostacruz.com/jquery.transit/) (JS + jQuery)
    3. [Mousetrap](http://craig.is/killing/mice)
    4. [Coffin](http://fat.github.io/coffin/)
    5. [Two.js](http://jonobr1.github.io/two.js/)
    6. [Odometer](http://github.hubspot.com/odometer/docs/welcome/) (JS + CSS)
    7. [cheet.js](http://namuol.github.io/cheet.js/)
    8. [Headroom.js](http://wicky.nillia.ms/headroom.js/)

### [[⬆]](#toc) <a name='design'>Design:</a>
1. [Dribbble](https://dribbble.com/)
2. [0to255](http://0to255.com/)
3. [CSSFlow](http://www.cssflow.com/)
4. [Subtle Patterns](http://subtlepatterns.com/)
5. [Beautiful web type](http://hellohappy.org/beautiful-web-type/)
6. [UICloud](http://ui-cloud.com/)
7. [PixelsDaily](http://pixelsdaily.com/)
8. [Fribbble](http://fribbble.com/)
9. [Flat UI](http://designmodo.github.io/Flat-UI/)
10. [Font Awesome](http://fortawesome.github.io/Font-Awesome/#)
11. [Fontello](http://fontello.com/)
12. [Ionicons](http://ionicons.com/)
13. [Canva](https://www.canva.com/)
14. [Typewolf](http://www.typewolf.com/open-source-web-fonts) | Open-source fonts.

### [[⬆]](#toc) <a name='ut'>Unit Testing:</a>
1. [Jasmine](http://jasmine.github.io/)
2. [Karma](http://karma-runner.github.io/0.12/index.html)
3. [Mocha](http://visionmedia.github.io/mocha/)
4. [Chai](http://chaijs.com/)
5. [PhantomJS](http://phantomjs.org/)
6. [QUnit](http://qunitjs.com/)
7. [Sinon](http://sinonjs.org/)
8. [Coveralls](https://coveralls.io/)

### [[⬆]](#toc) <a name='fbt'> Frontend Build Tools:</a>
1. [Bower/Package management](http://bower.io/) | Bower works by fetching and installing packages from all over, taking care of hunting, finding, downloading, and saving the stuff you’re looking for. Bower keeps track of these packages in a manifest file, bower.json. How you use packages is up to you. Bower provides hooks to facilitate using packages in your tools and workflows.
2. [Yeoman.io](http://yeoman.io/) | Yeoman helps you kickstart new projects, prescribing best practices and tools to help you stay productive.
3. [Grunt](http://gruntjs.com/) | Grunt in one word: automation. The less work you have to do when performing repetitive tasks like minification, compilation, unit testing, linting, etc, the easier your job becomes. After you've configured it, a task runner can do most of that mundane work for you—and your team—with basically zero effort.
4. [Gulp](http://gulpjs.com/) | Gulp is a streaming build system, very similar to Grunt.
5. [Browserify](http://browserify.org/) | Browserify lets you require('modules') in the browser by bundling up all of your dependencies.
6. [Require.js](http://requirejs.org/) | RequireJS is a JavaScript file and module loader. It is optimized for in-browser use, but it can be used in other JavaScript environments, like Rhino and Node.

### [[⬆]](#toc) <a name='resource4learn'> Great Resources For Learning :</a>
1. [Code Academy](http://www.codecademy.com/) | This is a great FREE resource for alot of the web dev. languages both frontend and backend, and what I found super helpful!
2. [Dash](https://dash.generalassemb.ly/) | This is a great FREE resource for HTML, CSS, JS.
3. [Code School](https://www.codeschool.com/) | Only has some free resources, but the free ones are pretty nice
4. [Tinkernut Web Dev](http://www.youtube.com/watch?v=6Ct6emxVR9w ) | Youtube guide for a very nitty gritty website, very easy to follow, and very light
5. [UW CSE 154 (Web Programming Step By Step)]()
6. [Tut+](http://tutsplus.com/)
7. [Stack Overflow](http://stackoverflow.com/)
8. [HTML5 and CSS3 For Dummies by Andy Harris:](http://www.amazon.com/HTML5-CSS3-All-One-Dummies/dp/1118289382)

### [[⬆]](#toc) <a name='online'> Getting Your Website Online:</a>
##### [[⬆]](#toc) <a name='dnrh'> Domain Name Registration + Hosting: (D + H)</a>
1. [NameCheap](http://www.namecheap.com/) (D+H) | They are the best to our hackers! :)
2. [Go Daddy](http://www.godaddy.com/) (D+H) |
3. [Blue Host](http://www.bluehost.com/) (D+H) |
4. [Award Space](http://www.awardspace.com/) (D+H) |
5. [HostGator](http://www.hostgator.com/) (D+H) |
6. [Just Host](http://www.justhost.com/) (D+H)
7. [GitHub](https://github.com/) (H) | This is what I use for the majority of my hosting, and I’m cool + it’s free, but only for static sites, check [backend resources](https://github.com/mrcoven94/resources/blob/gh-pages/backend-webdev.md) (H) | for the more dynamic free options.
8. [BitBucket](https://bitbucket.org/)
9. [NodeJitsu](https://www.nodejitsu.com/) (H) | Primarily for Node.JS Applications
10. [PythonAnyWhere](https://www.pythonanywhere.com/) (H) | Primarily for Python Applications
11. [DigitalOcean](https://www.digitalocean.com/) (H) | Deploy a server in 60 seconds or less!

##### [[⬆]](#toc) <a name='ftp'> FTP :</a>
1. [CyberDuck](https://cyberduck.io/?l=en) |
2. [Firezilla](https://filezilla-project.org/) |

### [[⬆]](#toc) <a name='github'> Using Github:</a>
1. [Read This Article First (Programming Way of Setting Up Your Site, using Git)](http://readwrite.com/2013/09/30/understanding-github-a-journey-for-2. beginners-part-1#awesm=~ozMC4gq6eTfUby)
3. [Hosting Personal]()
4. [Hosting Multiple Project Sites Tutorials: Video](http://www.youtube.com/watch?v=J8RLq9LXFXk)
5. [Github markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
6. [Github Markdown #2](http://assemble.io/docs/Cheatsheet-Markdown.html)

##### [[⬆]](#toc) <a name='git'> Learning Git :</a>

### [[⬆]](#toc) <a name='job'>Getting The Job:</a>
1. [Amazing list of Front-end Job Interview Questions](https://github.com/darcyclarke/Front-end-Developer-Interview-Questions)

Contributors: [Amit Burstein](https://github.com/amitburst), [David Coven](https://github.com/mrcoven94)
