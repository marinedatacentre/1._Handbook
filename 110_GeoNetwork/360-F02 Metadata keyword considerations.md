Last Edit Date: 2015-March-20 330-F02

**Metadata keyword encoding**

There is no particular keyword requirement as to the ISO 19115/19119 metadata profile used, but metadata records need to include keywords expressed in one of the following four encoding forms.

1.  **URI only** (preferred format)

> Encode as character strings (gco:CharacterString), each containing the URI of a concept from your local KOS (if any). This encoding form is currently the favoured recommendation as it uses a direct URI link to the semantic keyword concept.
>
> An example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p>&lt;gmd:descriptiveKeywords&gt; &lt;gmd:MD_Keywords&gt;</p>
<p>&lt;gmd:keyword&gt;</p>
<p>&lt;gco:CharacterString&gt;</p>
<p><strong>http://vocab.nerc.ac.uk/collection/A03/current/Beach</strong></p>
<p>&lt;/gco:CharacterString&gt;</p>
<p>&lt;/gmd:keyword&gt;</p></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>&lt;gmd:thesaurusName&gt; &lt;gmd:CI_Citation&gt;</p>
<p>&lt;gmd:title&gt;</p>
<p>&lt;gco:CharacterString&gt;</p>
<p>Oregon Coastal Atlas Coastal Erosion Thesaurus discovery terms</p>
<p>&lt;/gco:CharacterString&gt;</p>
<p>&lt;/gmd:title&gt;</p>
<p>&lt;gmd:date&gt;</p>
<p>&lt;gmd:CI_Date&gt;</p>
<p>&lt;gmd:date&gt;</p>
<p>&lt;gco:Date&gt;2011-08-19&lt;/gco:Date&gt;</p>
<p>&lt;/gmd:date&gt;</p>
<p>&lt;gmd:dateType&gt;</p>
<p>&lt;gmd:CI_DateTypeCode codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/ resources/Codelist/gmxCodelists.xml#CI_DateTypeCode" codeListValue="revision"&gt;</p>
<p>Revision</p>
<p>&lt;/gmd:CI_DateTypeCode&gt; &lt;/gmd:dateType&gt;</p>
<p>&lt;/gmd:CI_Date&gt; &lt;/gmd:date&gt;</p>
<p>&lt;/gmd:CI_Citation&gt;</p>
<p>&lt;/gmd:thesaurusName&gt;</p>
<p>&lt;/gmd:MD_Keywords&gt;</p>
<p>&lt;/gmd:descriptiveKeywords&gt;</p></td>
</tr>
</tbody>
</table>

2.  **Label only** (acceptable, but not preferred)

> Encode as character strings, each containing the label of a concept from your local KOS (if any). However, this does not support a direct link to the concept. Instead, the mediator must search all the local KOS for the relevant concept based on the label. Therefore, this encoding form is not preferred.
>
> An example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p>&lt;gmd:descriptiveKeywords&gt; &lt;gmd:MD_Keywords&gt;</p>
<p>&lt;gmd:keyword&gt;</p>
<p>&lt;gco:CharacterString&gt;<strong>Beach</strong>&lt;/gco:CharacterString&gt;</p>
<p>&lt;/gmd:keyword&gt;</p>
<p>&lt;gmd:thesaurusName&gt;</p>
<p>&lt;gmd:CI_Citation&gt;</p>
<p>&lt;gmd:title&gt;</p>
<p>&lt;gco:CharacterString&gt;</p>
<p>Oregon Coastal Atlas Coastal Erosion Thesaurus discovery terms</p>
<p>&lt;/gco:CharacterString&gt;</p>
<p>&lt;/gmd:title&gt;</p>
<p>&lt;gmd:date&gt;</p>
<p>&lt;gmd:CI_Date&gt;</p>
<p>&lt;gmd:date&gt;</p>
<p>&lt;gco:Date&gt;2011-08-19&lt;/gco:Date&gt;</p>
<p>&lt;/gmd:date&gt;</p>
<p>&lt;gmd:dateType&gt;</p>
<p>&lt;gmd:CI_DateTypeCode</p>
<p>codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/ resources/Codelist/gmxCodelists.xml#CI_DateTypeCode" codeListValue="revision"&gt;</p>
<p>Revision</p>
<p>&lt;/gmd:CI_DateTypeCode&gt; &lt;/gmd:dateType&gt;</p>
<p>&lt;/gmd:CI_Date&gt; &lt;/gmd:date&gt;</p>
<p>&lt;/gmd:CI_Citation&gt;</p>
<p>&lt;/gmd:thesaurusName&gt;</p>
<p>&lt;/gmd:MD_Keywords&gt;</p>
<p>&lt;/gmd:descriptiveKeywords&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

3.  **As both uri and label** (preferred in the long term; not presently tested by ICWA)

> Encode as anchor elements (gmx:Anchor), each containing both the URI and label of a concept from your local KOS (if any). This encoding form is currently not supported by GeoNetwork (version 2.6.4 and earlier) and, therefore, has not been tested by ICWA. In the long term this will be the preferred encoding form as it supports both a direct URI link to the concept and a label of this concept.
>
> An example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p>&lt;gmd:descriptiveKeywords&gt; &lt;gmd:MD_Keywords&gt;</p>
<p>&lt;gmd:keyword&gt;</p>
<p>&lt;gmx:Anchor xlink:href="<strong>http://vocab.nerc.ac.uk/collection/A03/current/Beach</strong>"&gt; <strong>Beach</strong></p>
<p>&lt;/gmx:Anchor&gt;</p>
<p>&lt;/gmd:keyword&gt;</p>
<p>&lt;gmd:thesaurusName&gt;</p>
<p>&lt;gmd:CI_Citation&gt;</p>
<p>&lt;gmd:title&gt;</p>
<p>&lt;gco:CharacterString&gt;</p>
<p>Oregon Coastal Atlas Coastal Erosion Thesaurus discovery terms</p>
<p>&lt;/gco:CharacterString&gt;</p>
<p>&lt;/gmd:title&gt;</p>
<p>&lt;gmd:date&gt;</p>
<p>&lt;gmd:CI_Date&gt;</p>
<p>&lt;gmd:date&gt;</p>
<p>&lt;gco:Date&gt;2011-08-19&lt;/gco:Date&gt;</p>
<p>&lt;/gmd:date&gt;</p>
<p>&lt;gmd:dateType&gt;</p>
<p>&lt;gmd:CI_DateTypeCode codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/ resources/Codelist/gmxCodelists.xml#CI_DateTypeCode" codeListValue="revision"&gt;</p>
<p>Revision</p>
<p>&lt;/gmd:CI_DateTypeCode&gt; &lt;/gmd:dateType&gt;</p>
<p>&lt;/gmd:CI_Date&gt; &lt;/gmd:date&gt;</p>
<p>&lt;/gmd:CI_Citation&gt;</p>
<p>&lt;/gmd:thesaurusName&gt;</p>
<p>&lt;/gmd:MD_Keywords&gt;</p>
<p>&lt;/gmd:descriptiveKeywords&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

4.  **Uncontrolled free text** (not recommended)

> Encode as character strings containing free text keywords. This is the simplest encoding form. It is not recommended because of its lack of a KOS, but it is supported to enable non-semantic metadata catalogues to be readily connected to the ICWA. Therefore, smart search functionality will not be supported for this encoding form.
>
> An example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><p>&lt;gmd:descriptiveKeywords&gt; &lt;gmd:MD_Keywords&gt;</p>
<p>&lt;gmd:keyword&gt;</p>
<p>&lt;gco:CharacterString&gt;<strong>Beach</strong>&lt;/gco:CharacterString&gt;</p>
<p>&lt;/gmd:keyword&gt;</p>
<p>&lt;/gmd:MD_Keywords&gt;</p>
<p>&lt;/gmd:descriptiveKeywords&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
