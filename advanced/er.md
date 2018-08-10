---
layout: page
---

[Advanced Assignments](./)

## Entity Relationship Translation

* Released: 
* Due: 
* Max team of 2

In this assignment, you will write a python program that translates simple ER diagrams into a set of SQL schema definition statements that adheres to the constraints indicated in the ER diagram.  

[Click here for a link to the Instabase Jupytr notebook that you will complete the assignment in](#).


### An Example

As an example, the following JSON object describes an ER diagram with two entity sets (animals, cages) where multiple animals can live in the same cage (one to many), but an animal can live in exactly one cage (exactly once).


        {
          entity_sets: [
            {
              name: "animals",
              key: "aid"
              attrs: {
                aid: "int",
                name: "text",
              }
            },
            { 
              name: "cages",
              key: "cid",
              attrs: {
                cid: "int",
                size: "int",
              }
            }
          ],
          rel_sets: [
            {
              name: "livesin",
              attrs: {
                start_day: "date",
                end_day: "date"
              }
            }
          ],
          relationships: [
            {
              entity_set: "animals",
              rel_set: "livesin",
              constraint: "exactlyone"
            },
            {
              entity_set: "cages",
              rel_set: "livesin",
              constraint: null
          ]
        }


The above statement translates into the following schema definition:

        CREATE TABLE animals(
          aid int primary key,
          name text NOT NULL,
          livesin int NOT NULL references cages(cid)
        );
        CREATE TABLE cages(
          cid int primary key,
          size int NOT NULL
        );


### Description of the Graph

The graph contains entity sets (the boxes), relationship sets (the diamonds), and relationships (the edges).  We will ignore aggregation.  

An entity set in `entity_sets` is a dictionary with the following attributes:

* name: a string that is the name of the entity set
* attrs: a dictionary that maps an attribute name to its type
  * types can be either `int`, `text`, or `date`.
  * you can assume that they are all not null
* key: its value is the attribute name that is the entity set's primary key

An relationship set in `rel_sets` is a dictionary with the following attributes:

* name: a string that is the name of the rel set
* attrs: a dictionary that maps an attribute name to its type
  * types can be either `int` or `str`.

A relationship in `relationships` is a dictionary with the fellowing attributes:

* entity_set: name of the entity set
* rel_set: name of the relationship set
* constraint: describes the type of relationship.  it can take the following values:
  * null: no constraints
  * "atmostone": an at most one relationship (`-->`)
  * "atleastone": an at least one relationship ( === )
  * "exactlyone": an exactly once relationship ( ==> )
  * "weak": a weak entity 


### Details About the Output Schema

**TODO: NEED TO BE SPECIFIC ABOUT HOW ATTRIBUTES AND TABLES SHOULD BE NAMED SO THAT AUTOGRADER TESTS CAN RUN**


