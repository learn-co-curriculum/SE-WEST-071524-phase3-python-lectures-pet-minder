---
theme : "night"
transition: "slide"
highlightTheme: "monokai"
slideNumber: false
title: "P3L1 - Python Fundamentals"
verticalSeparator: 'xxx'
presentation:
    width: 1500
    height: 1000

---

<h2>Python Fundamentals</h2>
<img alt="python logo" src="./python-logo-only.png"/>

---

<h2><strong> ✅ Objectives </strong></h2>

- Review a brief history of Python
- Use 'pip' to manage Python packages
- Debug Python code with `shell`, `print`, and `ipdb`
- Review common Python data types
- Understand Python conditionals and control flow
- Write Python functions
 
xxx

- Review Python variable scope and the `global` keyword
- Read Python error messages and exceptions
- Handle errors with `try:` and `except:`

---

<h2>What is Python ❓</h2>

- interpreted scripting language
- object-oriented
- dynamically typed
- supports modules and packages
- extensive standard library
- emphasis on readability

---

<h3>A little history... 📚</h3>

<div style="display: flex;">
  <div style="width: 35%; height: 100%">
    <img src="./guidovr.jpg">
  </div>

  <div style="font-size: 1.5rem; margin: 0.85rem 1rem; width: 65%; height: 100%">
  
- Who: Guido van Rossum
- When: February 20, 1991
- Eponym: Monty Python's Flying Circus

    <p>Began as a personal project based on another language he wrote called ABC with the intention of making it easier to read and program in C.</p>

    _Python is an experiment in how much freedom programmers need. Too much freedom and nobody can read another's code; too little and expressiveness is endangered._

   _-Guido van Rossum_

  </div>
</div>

---

<h2>PyPi and Pip</h2>

<div style="display: flex;">
  <div style="width: 40%">
    <h5>What do PyPi and Pip stand for?</h5>
  </div>
  <div style="font-size: 1.5rem; margin-top: 0.85rem; width: 60%">
    <textarea style="font-size: 1.5rem; border: 2px solid black; padding: 1rem; width: 90%; background: #333; color: #eee" rows="5" cols="35"></textarea>    
  </div>
</div>

<p>Let's install a popular package for sending HTTP requests</p>

```python
pip install requests
```
[PyPi](https://pypi.org/)

---

To install a specific version:
```python
pip install requests==2.22.0
```
To uninstall a package:
```python
pip uninstall requests
```

When deploying, you will use pip to create a requirements file:
```python
pip install -r requirements.txt
```

---

### The Python Shell

<img src="./py_shell.png" />

- Python comes with a built in REPL.
- Start a REPL by typing `python` at the command line.
- Exit with `exit()` or `ctrl + d`

##### Let's try it!

---

### Python's Common Data Types

<div style="font-size: 1.5rem" >

| Example                       | Data Type | Name       |
| ----------------------------- | --------- | ---------- |
| `"Hello Python"`              | str       | string     |
| `20`                          | int       | integer    |
| `20.5`                        | float     | float      |
| `[1, 2, 3]`                   | list      | list       |
| `(1, 2, 3)`                   | tuple     | tuple      |
| `{"name": "Mimi", "age": 10}` | dict      | dictionary |
| `{2, 4, 6}`                   | set       | set        |
| `True`                        | bool      | boolean    |
| `None`                        | NoneType  | NoneType   |

</div>

---

<div style="display: in-line block">
    <iframe src="https://www.classtools.net/dragdrop/202307_DS3M2K" style="position:relative;top:0;left:0;width:900px;height:650px;overflow:none;border:none"></iframe>
</div>

---

### The Virtual Environment 🌲

#### Pyenv

Pyenv is the tool we'll use to install and manage different versions of Python.

- `pyenv versions` will show you what Python versions are currently installed on your machine
- `pyenv install -l` will show a list of versions available to install
- `pyenv install 3.9.2` will install that version on your machine
- `pyenv global 3.9.2` will set that as the global version on your machine

---

#### Pipenv

<p style="font-size: 1.7rem">Pipenv is a tool built upon <code>pip</code> which can create virtual environments and install packages in them.</p>

<div style="font-size: 1.5rem">

- `Pipfile`: look for this first, it is analogous to npm's package.json file and lists the dependencies and Python version for the current project
- `Pipfile.lock`: similar to package-lock.json, this file describes both the Pipfile dependencies AND their dependencies with exact versions

If the project directory doesn't have these, you need to create a virtual environment

<pre style="font-size: 1.7rem"><code>pipenv --python 3.8.13</code></pre>

Now you can start adding dependencies similarly to how you would install packages with `pip`:

<pre style="font-size: 1.7rem"><code>pipenv install requests</code></pre>

</div>

xxx

<div style="font-size: 1.5rem">

| Command          | Description                                               |
| ---------------- | --------------------------------------------------------- |
| `pipenv install` | creates the virtual environment and installs dependencies |
| `pipenv shell`   | activates the virtual environment                         |
| `ctrl + d`       | deactivates the virtual environment                       |
| `pipenv -rm`     | removes the virtual environment                           |

</div>

---

## Let's dive into the code! 🤿

---
