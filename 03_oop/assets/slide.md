---
theme : "night"
transition: "slide"
highlightTheme: "monokai"
slideNumber: false
title: "P3L3 - Object-Oriented Programming in Python"
verticalSeparator: 'xxx'
presentation:
    width: 1500
    height: 1000

---

<h2>Object-Oriented Programming in Python</h2>
<img alt="python logo" src="./python-logo-only.png"/>

---

<h3><strong> ✅ Objectives </strong></h3>

* Define Object-Oriented Programming
* Understand the benefits of OOP
* Build Classes
* Create instances of those classes
* Use `__init__` to instantiate objects with attribute values

xxx

* Add instance methods to our classes
* Understand the use of the `self`` keyword in instances
* Know the principles of OO Design
* Stretch: object properties, mass assignment

---

<h3>What is OOP? 🤔</h3>

<div style="font-size: 1.8rem" >

* a programming paradigm  
* seeks to encapsulate information and it's related behaviors together as objects
* models concepts and objects in the real world. 
* easier to reason about and solve problems involving those data, 
* facilitates structuring our programs in ways that can share and reuse these objects.
* contrast to Procedural Programming, 
  * written in sequential order and 
  * procedures are called when behaviour needs to be shared between pages in an application.
</div>


---

<img src="./OOPConcept.jpg" style="width: 900px">

---


<section data-background-color="mistyrose" >
  <h3>Classes and Instances</h3>
  <img src="./classes_instances.png" />
</section>


---

### A Python Class is...

* a blueprint or template for creating individual objects
* a data structure which assigns values and methods to objects

<div style="display: flex;">
  <div style="width: 35%; height: 100%">
    <img src="./604px-CPT-OOP-objects_and_classes_-_attmeth.svg.png" />
  </div>

  <div style="width: 65%; height: 100%">
    <img src="./OOP-là-gì-3.jpg" />
  </div>
</div>

---

### An object is...

<div style="display: flex;">
  <div style="font-size: 1.75rem; width: 50%">
    <ul>
      <li> an individual collection of variables (attributes), functions (methods), and data structures</li>
      <li> constructed from a class</li>
      <li> also called an 'instance'</li>
      <li> a representation of a real world object or event</li>
    </ul>
  </div>

  <div style="width: 50%">
    <img src="./CookieCutter.png" />
    
  </div>
</div>


---

#### You actually already have some experience with classes and instances!

<pre>
  <code class="language-python" data-trim >
    type("hello") # => < class 'str'>
    42.__class__ # => < class 'int'>
  </code>
</pre>

<p>What happens when you enter <code>dir("world")</code> in a Python shell?</p>

#### Let's build a class and some instances! 👷

---

#### Some strengths of OOP

* having total control of what objects look like just by updating their class

#### Some weaknesses of OOP

* becuase my objects have to conform to a class, I lose flexibility in changing their attributes without changing the class

---

#### Example Application Domains

* healthcare {.fragment}
* FinTech/banking {.fragment}
* insurance {.fragment}
* sales {.fragment}
* eCommerce {.fragment}
* accounting {.fragment}
* booking software for hospitality and travel {.fragment}

---

#### OOP Design Principles 🧭

* single responsibility
* separation of concerns
* DRY
* domain modeling

---

#### Single Responsibility

<div style="display: flex;">
  <div style="width: 50%">
    <img src="./SingleResponsibility2.png" />
  </div>

  <div style="width: 50%">
    <img src="./SingleResponsibility.png" />
  </div>
</div>

xxx

<div style="display: flex;">
  <div style="width: 45%">
    <img src="./ExampleSingleReponsibility.png" />
    <h5 class="fragment" style="color:red">Overloaded 🚫<h5>
  </div>

  <div style="width: 55%">
    <img class="fragment" src="./ExampleSingleReponsibility1.png" />
    <img class="fragment" src="./ExampleSingleReponsibility21.png" />
    <h5 class="fragment" style="color:green">Classes separated to reduce complexity of our classes 👍</h5>
  </div>
</div>

---

#### Separation of Concerns

* Supports high cohesion among components {.fragment} 
* Supports low coupling among components {.fragment}
* Increases modularity {.fragment}
* Increases maintainability {.fragment}
* Increases reusability {.fragment}

xxx

<h5>Cohesion</h5>

<img style="width: 75%" src='./cohesion-coupling.webp' />

<div style="font-size: 1.5rem">

* cohesive components perform only one task
* cohesion is the internal glue that keeps a module together
* it is a measure of the degree to which the elements in the module are functionally related

</div>


---

<section data-background-color="mistyrose">

  <h5>Coupling</h5>

  <div style="display: flex;">
  <div style="width: 50%">
    <img src="./coupling-examples.webp" />
  </div>

  <div style="width: 50%">
    <ul style="font-size: 1.5rem">
      <li class='fragment'>good software has low coupling</li>
      <li class='fragment'>coupling increases with the number of calls or the amount of data shared between modules</li>
      <li class='fragment'>a design with high coupling will have more errors</li>
      <li class='fragment'>it measures the degree of interdependence between modules</li>
    </ul>
  </div>
</div>

</section>


---

##### D.R.Y. 🌞🌵

<iframe width="760" height="515" src="https://www.youtube.com/embed/8hOZe5oVzJY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

---

#### Domain Modeling 📐

<div style="display: flex;">
  <div style="width: 40%; font-size: 2rem">
    <p>A structured visual representation of interconnected concepts or real-world objects that incorporates vocabulary, key concepts, behavior, and relationships of all its entities.</p>
  </div>

  <div style="width: 60%">
    <img src="./vehicles-domain.webp" />
   
  </div>
</div>


xxx

<img src="./bookshopclass.jpg" />


---

#### How will objects help us going forward? 🚗 

<div style="display: flex">
  <div style="width: 50%" >
    <img src="./pet_class.png" />
  </div>

  <div style="width: 50%">
    <img src="./pets_table.png" />
  </div>
</div>

xxx

<img src="./analogy.png" />

---

<section data-background-image="https://media.giphy.com/media/3oKGzEisePrzPMOWEo/giphy.gif" data-background-size="1200px">
 

</section>


---


