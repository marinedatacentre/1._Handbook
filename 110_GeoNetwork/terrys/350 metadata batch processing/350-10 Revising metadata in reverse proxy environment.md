**Purpose:**

Recover error in \*not\* setting GeoNetwork parameters correctly in Reverse Proxy environment. The website normally has

- a host, poet and protocol that is externally advertised, and

- an internal website redirection to localhost, via http or https

For GeoNetwork, the "use proxy" should **not** be checked. However, sometimes this error occurs.

Process by Jean Luis Rodriguez (2023-01-31)

+-------------------+-------------------------------------------------------------------------------------------+--------------------------------------+
| **Step**          | **Major Activity**                                                                        | **References, Forms and Details**    |
+:=================:+:==========================================================================================+:=====================================+
| 1                 | The correct settings for GeoNetwork are to complete host, port and protocol settings, and | > Example:                           |
|                   |                                                                                           |                                      |
|                   | not to select proxy                                                                       | - Host: soggy.zoology.ubc.ca         |
|                   |                                                                                           |                                      |
|                   |                                                                                           | - Port 443                           |
|                   |                                                                                           |                                      |
|                   |                                                                                           | - Protocol: https                    |
|                   |                                                                                           |                                      |
|                   |                                                                                           | Wrong proxy setting                  |
|                   |                                                                                           |                                      |
|                   |                                                                                           | - Proxy: localhost                   |
|                   |                                                                                           |                                      |
|                   |                                                                                           | - Port: 8080/8443                    |
|                   |                                                                                           |                                      |
|                   |                                                                                           | - Protocol: http/https               |
+-------------------+-------------------------------------------------------------------------------------------+--------------------------------------+
| 2                 | If they were set, the metadata needs correction.                                          | - explicit details may vary slightly |
|                   |                                                                                           |                                      |
|                   | - In GeoNetwork, Go to                                                                    |                                      |
|                   |                                                                                           |                                      |
|                   | > Contribute -\> BatchUpdate                                                              |                                      |
|                   |                                                                                           |                                      |
|                   | - Replace <https://localhost:8443/geonetwork>                                             |                                      |
|                   |                                                                                           |                                      |
|                   | > With                                                                                    |                                      |
|                   |                                                                                           |                                      |
|                   | - https://soggy.zoology.ubc.ca/geonetwork                                                 |                                      |
+-------------------+-------------------------------------------------------------------------------------------+--------------------------------------+
| 3                 | Go to                                                                                     | -                                    |
|                   |                                                                                           |                                      |
|                   | Admin Console -\> Tools -\> Reindex records                                               |                                      |
|                   |                                                                                           |                                      |
|                   | And reindex                                                                               |                                      |
+-------------------+-------------------------------------------------------------------------------------------+--------------------------------------+
| 4                 | Check that proper behaviour occurs                                                        | -                                    |
+-------------------+-------------------------------------------------------------------------------------------+--------------------------------------+
