.. _Python Programming Language: http://www.python.org/

:title: Home
:save_as: index.html

circuits is a **Lightweight** **Event** driven and **Asynchronous**
**Application Framework** for the `Python Programming Language`_
with a strong **Component** Architecture.

circuits also includes a lightweight, high performance and scalable
HTTP/WSGI compliant web server as well as various I/O and Networking
components.

Features
--------

- event driven
- concurrency support
- component architecture
- asynchronous I/O components
- no required external dependencies
- full featured web framework (circuits.web)
- coroutine based synchronization primitives

Examples
--------

.. html::

   <ul class="nav nav-tabs">
     <li class="active"><a data-toggle="tab" href="#helloworld">Hello World!</a></li>
     <li><a data-toggle="tab" href="#echoserver">Echo Server</a></li>
     <li><a data-toggle="tab" href="#webapp">Web App</a></li>
   </ul>

.. html::

   <div class="tab-content">

.. html::

     <div id="helloworld" class="tab-pane fade in active">

`Hello World! <https://github.com/circuits/circuits/blob/master/examples/hello.py>`_

.. code-include:: ../examples/hello.py
    :lexer: python
    :encoding: utf-8
    :tab-width: 4

.. html::
   
     </div>

.. html::

     <div id="echoserver" class="tab-pane fade in">

A simple `Echo Server <https://github.com/circuits/circuits/blob/master/examples/echoserver.py>`_:

.. code-include:: ../examples/echoserver.py
    :lexer: python
    :encoding: utf-8
    :tab-width: 4

.. html::
   
     </div>

.. html::

     <div id="webapp" class="tab-pane fade in">

A simple `Web Application <https://github.com/circuits/circuits/blob/master/examples/web/controllers.py>`_:

.. code-include:: ../examples/webapp.py
    :lexer: python
    :encoding: utf-8
    :tab-width: 4

.. html::
   
     </div>

.. html::
   
   </div>
