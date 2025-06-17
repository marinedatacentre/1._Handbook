**Purpose:**

How to perform editing multiple records -- adding and replacing content,
adding and deleting elements. The process is:

1.  choose a set of records

2.  define the edits

3.  apply changes

4.  save (execute task)

5.  Observe success feedback, or remedy any issues

+----------+---------------------------------+----------------------------+
| **Step** | **Major Activity**              | **References, Forms and    |
|          |                                 | Details**                  |
+:========:+:================================+:===========================+
| 1        | Log into GeoNetwork as          |                            |
|          | administrator                   |                            |
+----------+---------------------------------+----------------------------+
| 2        | Switch to tabs:                 |                            |
|          |                                 |                            |
|          | - contribute                    |                            |
|          |                                 |                            |
|          | - batch editing                 |                            |
+----------+---------------------------------+----------------------------+
| 3        | Select the number of records to | - Choices of records per   |
|          | display per page:               |   page are 30, 60 or 120   |
|          |                                 |                            |
|          | - click the "on" in the records |                            |
|          |   to show                       |                            |
+----------+---------------------------------+----------------------------+
| 4        | If desired, apply a filter      | - Often not required       |
|          | (left column) to narrow the     |                            |
|          | record choices                  |                            |
+----------+---------------------------------+----------------------------+
| 5        | Click on the "sorted" button to | - Sorting by title enables |
|          | sort by title                   |   stepping through a set   |
|          |                                 |   of metadata              |
|          |                                 |   systematically without   |
|          |                                 |   duplication              |
+----------+---------------------------------+----------------------------+
| 6        | Choose the set of records:      | - Sometimes the batch will |
|          |                                 |   not conclude             |
|          | - click on the unlabelled       |   successfully if many     |
|          |   button for choices, or select |   records are chosen       |
|          |   records individually          |                            |
|          |                                 | - "all in page" is often a |
|          | - click on the "1 -- x          |   good choice              |
|          |   left-right-begin-end" button  |                            |
|          |   to select records from one or |                            |
|          |   more pages                    |                            |
|          |                                 |                            |
|          | - a good approach is to select  |                            |
|          |   only one record as a trial    |                            |
+----------+---------------------------------+----------------------------+
| 7        | Define the edits:               | - There are 2 or 3         |
|          |                                 |   choices,(3 with recent   |
|          | - if available and appropriate, |   4.2+ GeoNetwork          |
|          |   use "Search and replace" as   |   releases)                |
|          |   it is simple, fast and not    |                            |
|          |   entry-error-prone             | - "xpath editing" can      |
|          |                                 |                            |
|          | - "Form Editing" is a good      |   - add and replace        |
|          |   choice if something in a      |     contents               |
|          |   standard field requires       |                            |
|          |   updating                      |   - add, modify and remove |
|          |                                 |     elements               |
|          | - "xpath editing" requires      |                            |
|          |   xpath expertise background.   | - unless carefully         |
|          |   Refer to the next step. This  |   constrained, major       |
|          |   process can modify a metadata |   unwanted changes can     |
|          |   record for almost any         |   occur                    |
|          |   requirement.                  |                            |
+----------+---------------------------------+----------------------------+
| 8        | Step only appropriate for xpath | - Try to fully qualify the |
|          | editing.                        |   desired xml changes      |
|          |                                 |                            |
|          | - Click on "Examples", and      | - providing "Text or XML   |
|          |   choose a task reasonably      |   value" will be           |
|          |   close to what is planned      |   restricted if the wrong  |
|          |                                 |   preceding function was   |
|          | - modify:                       |   chosen                   |
|          |                                 |                            |
|          |   - optional title for the task |                            |
|          |                                 |                            |
|          |   - select add, replace or      |                            |
|          |     remove                      |                            |
|          |                                 |                            |
|          |   - very carefully define the   |                            |
|          |     xslt task                   |                            |
+----------+---------------------------------+----------------------------+
| 9        | Click on the "+" to place the   | - Task title, xslt         |
|          | planned task in the "to be      |   expression and value     |
|          | processed" queue                |   will be displayed, and   |
|          |                                 |   can be edited, deleted   |
|          |                                 |   or copied to clipboard   |
|          |                                 |                            |
|          |                                 | - all tasks and previous   |
|          |                                 |   steps can be removed     |
|          |                                 |   using "Reset changes"    |
+----------+---------------------------------+----------------------------+
| 10       | Click "Save" to execute         | - A failure with no        |
|          |                                 |   details may mean the     |
|          | - If successful, a short        |   task was successful even |
|          |   standard list of activities   |   though flagged as an     |
|          |   will be displayed             |   error. This requires     |
|          |                                 |   further investigation    |
|          | - if not successful, the        |                            |
|          |   standard list will be         | - the above may occur if   |
|          |   displayed , and possibly a    |   too mant records were    |
|          |   detailed list by record of    |   chosen for a batch       |
|          |   failures                      |   operation                |
+----------+---------------------------------+----------------------------+
