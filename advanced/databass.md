---
layout: page
---

[Advanced Assignments](./)

## DataBass Assignments

This series of assignments are self contained, and will ask you to modify parts of the [DataBass](https://www.github.com/w4111/databass) database system.  DataBass is pretty full featured!  It can:

* Parse and translate SQL queries into a query plan, optimize the plan, and run it
* Supports SELECT, PROJECT, JOIN, GROUP BY, LIMIT, ORDER BY statements
* Supports nested queries
* Automatically registers CSV files as database tables
* Uses a simple cost-based optimizer to join ordering optimization

To get started, clone the github repository, install the relevant python packages:

        git clone git@github.com:w4111/databass.git
        pip install numpy click pandas parsimonious

Now test it out:

        cd databass/src/engine
        python test.py

Now you are ready to [read the system architecture and documentation](https://github.com/w4111/databass/blob/master/docs/design.md)

Each assignment modifies a different part of the engine:

1. [Add to the Parser](./parser)
1. [Add an operator and get it to run](./op)
1. [Join ordering optimization](./join)
1. [Query compilation](./compile)

