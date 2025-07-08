---
process_number: 360-30
title: Batch Find and fix metadata record errors
author: Peter
created: 2019-12-12
modified: 2023-02-15
review_period: 3 years
---

**Purpose:**

How to perform editing multiple records – adding and replacing content, adding and deleting elements. The process is:

1.  choose a set of records

2.  define the edits

3.  apply changes

4.  save (execute task)

5.  Observe success feedback, or remedy any issues

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 47%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Step</strong></th>
<th style="text-align: left;"><strong>Major Activity</strong></th>
<th style="text-align: left;"><strong>References, Forms and Details</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: left;">Log into GeoNetwork as administrator</td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: left;"><p>Switch to tabs:</p>
<ul>
<li><p>contribute</p></li>
<li><p>batch editing</p></li>
</ul></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: left;"><p>Select the number of records to display per page:</p>
<ul>
<li><p>click the “on” in the records to show</p></li>
</ul></td>
<td style="text-align: left;"><ul>
<li><p>Choices of records per page are 30, 60 or 120</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: left;">If desired, apply a filter (left column) to narrow the record choices</td>
<td style="text-align: left;"><ul>
<li><p>Often not required</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: left;">Click on the “sorted” button to sort by title</td>
<td style="text-align: left;"><ul>
<li><p>Sorting by title enables stepping through a set of metadata systematically without duplication</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: left;"><p>Choose the set of records:</p>
<ul>
<li><p>click on the unlabelled button for choices, or select records individually</p></li>
<li><p>click on the “1 – x left-right-begin-end” button to select records from one or more pages</p></li>
<li><p>a good approach is to select only one record as a trial</p></li>
</ul></td>
<td style="text-align: left;"><ul>
<li><p>Sometimes the batch will not conclude successfully if many records are chosen</p></li>
<li><p>“all in page” is often a good choice</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: left;"><p>Define the edits:</p>
<ul>
<li><p>if available and appropriate, use “Search and replace” as it is simple, fast and not entry-error-prone</p></li>
<li><p>“Form Editing” is a good choice if something in a standard field requires updating</p></li>
<li><p>“xpath editing” requires xpath expertise background. Refer to the next step. This process can modify a metadata record for almost any requirement.</p></li>
</ul></td>
<td style="text-align: left;"><ul>
<li><p>There are 2 or 3 choices,(3 with recent 4.2+ GeoNetwork releases)</p></li>
<li><p>“xpath editing” can</p>
<ul>
<li><p>add and replace contents</p></li>
<li><p>add, modify and remove elements</p></li>
</ul></li>
<li><p>unless carefully constrained, major unwanted changes can occur</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td style="text-align: left;"><p>Step only appropriate for xpath editing.</p>
<ul>
<li><p>Click on “Examples”, and choose a task reasonably close to what is planned</p></li>
<li><p>modify:</p>
<ul>
<li><p>optional title for the task</p></li>
<li><p>select add, replace or remove</p></li>
<li><p>very carefully define the xslt task</p></li>
</ul></li>
</ul></td>
<td style="text-align: left;"><ul>
<li><p>Try to fully qualify the desired xml changes</p></li>
<li><p>providing “Text or XML value” will be restricted if the wrong preceding function was chosen</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">9</td>
<td style="text-align: left;">Click on the “+” to place the planned task in the “to be processed” queue</td>
<td style="text-align: left;"><ul>
<li><p>Task title, xslt expression and value will be displayed, and can be edited, deleted or copied to clipboard</p></li>
<li><p>all tasks and previous steps can be removed using “Reset changes”</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">10</td>
<td style="text-align: left;"><p>Click “Save” to execute</p>
<ul>
<li><p>If successful, a short standard list of activities will be displayed</p></li>
<li><p>if not successful, the standard list will be displayed , and possibly a detailed list by record of failures</p></li>
</ul></td>
<td style="text-align: left;"><ul>
<li><p>A failure with no details may mean the task was successful even though flagged as an error. This requires further investigation</p></li>
<li><p>the above may occur if too mant records were chosen for a batch operation</p></li>
</ul></td>
</tr>
</tbody>
</table>
