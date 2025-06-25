**Purpose:**



How to perform editing multiple records -- adding and replacing content, adding and deleting elements. The process is:



1.  choose a set of records



2.  define the edits



3.  apply changes



4.  save (execute task)



5.  Observe success feedback, or remedy any issues



| **Step** | **Major Activity** | **References, Forms and Details** |
| -------- | ------------------ | --------------------------------- |
| 1 | Log into GeoNetwork as administrator |  |
| 2 | Switch to tabs: |  |
|  |  |  |
|  | - contribute |  |
|  |  |  |
|  | - batch editing |  |
| 3 | Select the number of records to display per page: | - Choices of records per page are 30, 60 or 120 |
|  |  |  |
|  | - click the "on" in the records to show |  |
| 4 | If desired, apply a filter (left column) to narrow the record choices | - Often not required |
| 5 | Click on the "sorted" button to sort by title | - Sorting by title enables stepping through a set of metadata systematically without duplication |
| 6 | Choose the set of records: | - Sometimes the batch will not conclude successfully if many records are chosen |
|  |  |  |
|  | - click on the unlabelled button for choices, or select records individually | - "all in page" is often a good choice |
|  |  |  |
|  | - click on the "1 -- x left-right-begin-end" button to select records from one or more pages |  |
|  |  |  |
|  | - a good approach is to select only one record as a trial |  |
| 7 | Define the edits: | - There are 2 or 3 choices,(3 with recent 4.2+ GeoNetwork releases) |
|  |  |  |
|  | - if available and appropriate, use "Search and replace" as it is simple, fast and not entry-error-prone | - "xpath editing" can |
|  |  |  |
|  | - "Form Editing" is a good choice if something in a standard field requires updating | - add and replace contents |
|  |  |  |
|  | - "xpath editing" requires xpath expertise background. Refer to the next step. This process can modify a metadata record for almost any requirement. | - add, modify and remove elements |
|  |  |  |
|  |  | - unless carefully constrained, major unwanted changes can occur |
| 8 | Step only appropriate for xpath editing. | - Try to fully qualify the desired xml changes |
|  |  |  |
|  | - Click on "Examples", and choose a task reasonably close to what is planned | - providing "Text or XML value" will be restricted if the wrong preceding function was chosen |
|  |  |  |
|  | - modify: |  |
|  |  |  |
|  | - optional title for the task |  |
|  |  |  |
|  | - select add, replace or remove |  |
|  |  |  |
|  | - very carefully define the xslt task |  |
| 9 | Click on the "+" to place the planned task in the "to be processed" queue | - Task title, xslt expression and value will be displayed, and can be edited, deleted or copied to clipboard |
|  |  |  |
|  |  | - all tasks and previous steps can be removed using "Reset changes" |
| 10 | Click "Save" to execute | - A failure with no details may mean the task was successful even though flagged as an error. This requires further investigation |
|  |  |  |
|  | - If successful, a short standard list of activities will be displayed | - the above may occur if too mant records were chosen for a batch operation |
|  |  |  |
|  | - if not successful, the standard list will be displayed , and possibly a detailed list by record of failures |  |

