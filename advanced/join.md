---
layout: page
---


[Advanced Assignments](./) > [DataBass](./databass)

## Join Ordering Optimization


* Released: 
* Due: 
* Max team of 2


In this assignment, you will use simple statistics to implement a simple version of the Selinger join optimizer to determine the join ordering for multi-table joins.
To do so, take a look at `optimizer.py`.  The class performs a single optimization, which is to replace the N-way `From` operator with a join tree that can actually be executed.
Take a look at `expand_from_op` to see our naive implementation.


The key method is `compute_join_order`. Given a list of sources (tables) and join predicate expressions, and statistics, the method returns a list of sources that describe the join order.  Recall that we only consider left-deep join plans, so the three-table ordering of `[A, B, C]` means `(A join B) join C`.

How the code is structured is a bit tricky, so we will explain what each line in the current implementation is doing.  The first line goes through each predicate expression in `exprs` and finds all the references to an attribute by using the `e.collect()` call.

    attrs = flatten([e.collect("Attr") for e in exprs])

For example, if the expression is `T1.a = T2.b`, then the `collect()` call would return `T1.a` and `T2.b`.  

This is important because the next line tells us which tables (`T1` and `T2`) are referenced by the `Attr` objects and potentially participate in some join expression.  We figure out which tables are referenced and put them into a set:

    refs = set(pickone(attrs, "tablename"))

Finally, we simply sort the `sources` so that sources that are referenced in a predicate (`s.alias in refs`) are joined earlier than those not referenced. 

    sources.sort(key=lambda s: s.alias in refs, reverse=True)



#### Selinger

Recall that selinger, as described in class, is an iterative algorithm that first tries all 2-way joins and picks the best.  It then tries all the ways to add a third table and pikcs the best.  Then a fourth, and so on.  For simplicity, you can assume that each tuple is one page access, when computing the cost of a join. Thus the cost of `A join B` where A has 5 tuples and B has 10, is `5 + 5*10`.

In this assignment we will make a number of simplifying assumptions:

* All sources have explicit aliases and the only sources are table scans  (e.g., not subqueries).  

      # data does NOT have explicit alias, can assume this will not happen
      SELECT * FROM data    
      
      # Source is a subquery can assume this will not happen
      SELECT * FROM (SELECT 1) AS T
      
      # data has an explicit alias of T
      SELECT * FROM data AS T

* All attributes also reference the table.  

      # attribute a does not reference its table T, can assume this will not happen
      SELECT * FROM data as T WHERE a = 1 
      
      # can assume it will always referenc the table 
      SELECT * FROM data as T WHERE T.a = 1 

* The only access method is a table scan (no indexes)
* The only join algorithm is nested loop join
* Each attribute's distribution is uniform between its min and max values.  Thus if attribute table `T` has 200 records and `T.a` has min/max values of 0,100, then we assume the selectivity of `T.a = 1` is `1/100`, and will match `2` records.

#### Statistics

To implement our simple version of Selinger, you will need to compute two statistics by editing the `Stat` class definition in `db.py`.   

1. The first is to compute the cardinality of the table.  Since DataBass loads the full table into memory, you can compute an exact estimate.     
1. The second is to compute the domain of a given field.  For a numeric field, it should be the min/max values, while for a non-numeric field such as text, it should be the set of all unique values. 

### Logistics

You will submit your solutions but [submitting a pull request](https://help.github.com/articles/creating-a-pull-request/) to the assignment GitHub repository.    We will consider the latest pull request prior to the submission deadline.


The criteria for your lab being submitted on time is that your code must be **tagged** and  **pushed** by the date and time. This means that if one of the TAs or the instructor were to open up GitHub, they would be able to see your solutions on the GitHub web page.

Just because your code has been committed on your local machine does not mean that it has been **submitted**; it needs to be on GitHub.

There is a bash script `submitJoinLab.sh` that commits your changes, deletes any prior tag, tags the current commit, and pushes the tag to github.  If you are using Linux or Mac OSX, you should be able to run the following:

		$ sh ./submitJoinLab.sh


If the above command worked for you, you can skip to item 6 below.  If not, submit your solutions as follows:

1. Look at your current repository status.

   ```bash
   $ git status
   ```

2. Add and commit your code changes (if they aren't already added and commited).

   ```bash
    $ git commit -a -m 'Join Lab'
   ```

3. Delete any prior local and remote tag (*this will return an error if you have not tagged previously; this allows you to submit multiple times*)

   ```bash
   $ git tag -d joinsubmit
   $ git push origin :refs/tags/joinsubmit
   ```

4. Tag your last commit as the lab to be graded 

   ```bash
   $ git tag -a joinsubmit -m 'submit join lab'
   ```

5. This is the most important part: **push** your solutions to GitHub.

   ```bash
   $ git push origin master --tags
   ```

6. The last thing that we strongly recommend you do is to go to the w4111 GitHub organization  page  to make sure that we can see your solutions.

Just navigate to your repository and check that your latest commits are on GitHub. 
