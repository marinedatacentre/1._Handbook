**Purpose:**

Recover error in \*not\* setting GeoNetwork parameters correctly in Reverse Proxy environment. The website normally has

- a host, poet and protocol that is externally advertised, and

- an internal website redirection to localhost, via http or https

For GeoNetwork, the “use proxy” should **not** be checked. However, sometimes this error occurs.

Process by Jean Luis Rodriguez (2023-01-31)

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 50%" />
<col style="width: 31%" />
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
<td style="text-align: left;"><p>The correct settings for GeoNetwork are to complete host, port and protocol settings, and</p>
<p>not to select proxy</p></td>
<td style="text-align: left;"><blockquote>
<p>Example:</p>
</blockquote>
<ul>
<li><p>Host: soggy.zoology.ubc.ca</p></li>
<li><p>Port 443</p></li>
<li><p>Protocol: https</p></li>
</ul>
<p>Wrong proxy setting</p>
<ul>
<li><p>Proxy: localhost</p></li>
<li><p>Port: 8080/8443</p></li>
<li><p>Protocol: http/https</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: left;"><p>If they were set, the metadata needs correction.</p>
<ul>
<li><p>In GeoNetwork, Go to</p></li>
</ul>
<blockquote>
<p>Contribute -&gt; BatchUpdate</p>
</blockquote>
<ul>
<li><p>Replace <a href="https://localhost:8443/geonetwork">https://localhost:8443/geonetwork</a></p></li>
</ul>
<blockquote>
<p>With</p>
</blockquote>
<ul>
<li><p>https://soggy.zoology.ubc.ca/geonetwork</p></li>
</ul></td>
<td style="text-align: left;"><ul>
<li><p>explicit details may vary slightly</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: left;"><p>Go to</p>
<p>Admin Console -&gt; Tools -&gt; Reindex records</p>
<p>And reindex</p></td>
<td style="text-align: left;"><ul>
<li></li>
</ul></td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: left;">Check that proper behaviour occurs</td>
<td style="text-align: left;"><ul>
<li></li>
</ul></td>
</tr>
</tbody>
</table>
