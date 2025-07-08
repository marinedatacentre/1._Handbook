---
process_number: 300-F04
title: Connecting Your Atlas
author: Unknown
created: Unknown
modified: Unknown
review_period: 3 years
---

NETMAR Deliverable D7.9.2: ICAN semantic interoperability cookbooks – Part 4
International Coastal Atlas Network Cookbook:
Connecting your Atlas to the
ICWA prototype
© 2012 NETMAR Consortium 1 EC FP7 Project No. 249024

NETMAR Deliverable D7.9.2: ICAN semantic interoperability cookbooks – Part 4
Table of Contents
Introduction.................................................................................................................................3
The ICWA prototype...................................................................................................................3
Connection Requirements...........................................................................................................5
CSW Requirements.................................................................................................................5
KOS Requirements.................................................................................................................7
What is Next?.............................................................................................................................8
Acknowledgements.....................................................................................................................9
Document Information.................................................................................................................9
© 2012 NETMAR Consortium EC FP7 Project No. 249024

NETMAR Deliverable D7.9.2: ICAN semantic interoperability cookbooks – Part 4
Introduction
This document is a step-by-step guide explaining how to connect your atlas as a node in the
International Coastal Web Atlas (ICWA) prototype hosted at http://ican.ucc.ie/. This document is
aimed specifically at members of the International Coastal Atlas Network community and more
generally at scientists, data managers, and system developers.
The ICWA prototype
The ICWA prototype is developed by the Technical Working Group (TWG) of the International
Coastal Atlas Network (ICAN), with the current prototype (version 3) being funded by the
NETMAR project. It provides a common interface for accessing distributed local atlases, such
as MIDA (Marine Irish Digital Atlas), OCA (Oregon Coastal Atlas), and Washington Coastal
Atlas (WCA). The current version of ICWA only supports catalogue search, including “smart
search”. The ICAN TWG are currently investigating the extension of ICWA to support web
mapping. ICWA version 3 is based on five components (Figure 1):
• Ontology Browser (OB)
• Discovery interface (Geo Finder)
• Metadata viewer (Meta Viewer)
• ICWA Mediator (CSW Mediator)
• Semantic Web Service (SWS)
Figure 1: Main components of the ICWA prototype
© 2012 NETMAR Consortium EC FP7 Project No. 249024

NETMAR Deliverable D7.9.2: ICAN semantic interoperability cookbooks – Part 4
The first three components are frontend graphical user interfaces hosted at http://ican.ucc.ie/. A
user can interact with these components in a web browser, and perform tasks such as ontology
browsing, data search and metadata visualisation across distributed atlases.
The other components are backend web services. The ICWA mediator (CSW Mediator)
communicates with local atlases through standard OGC CSW (Catalogue Service for the Web)
interfaces. It queries the knowledge organisation system (KOS) through the semantic web
service (SWS) interface. ICWA uses a knowledge organisation system to improve data
discovery by exploiting the semantics of keywords and allowing users to search data by
“meaning” rather than by “mere keywords”.
For example, as illustrated in Figure 2, a user arrives at the ICAN portal and requests “coastline”
data. The ICWA mediator is connected to a global knowledge organisation system that is aware
that “coastline” is related to both “shoreline” and “high resolution coastline”. The user request,
together with this information from the global knowledge organisation system, is then passed on
to the local atlases that search for “coastline”, “shoreline” and “high resolution coastline”. Each
local atlas then returns the relevant metadata results to the ICWA mediator. In turn, these
individual metadata results are aggregated and passed to the graphical user interface. This is
an implementation of the so-called “smart-search”1.
I’d like
“coastline”
data
“Coastline”
“Shoreline”
“High Res. Coast”
Global
ICWA Mediator KOS
“Coastline” “Shoreline” “High Res. Coast”
MIDA OCA WCA
…
MIDA OCA WCA
KOS KOS KOS
Figure 2: Illustrating the use for knowledge organisation systems in the ICWA
1 Latham, S. E.; Cramer, R.; Grant, M.; Kershaw, P.; Lawrence, B. N.; Lowry, R.; Lowe, D.; O'Neill, K.; Miller, P.; Pascoe, S.;
Pritchard, M.; Snaith, H.; Woolf, A. (2009) The NERC DataGrid services. Philosophical Transactions of the Royal Society A, 367
(1890). 1015-1019.
© 2012 NETMAR Consortium EC FP7 Project No. 249024

NETMAR Deliverable D7.9.2: ICAN semantic interoperability cookbooks – Part 4
Connection Requirements
In order to connect your atlas as a node in the ICWA, you need to:
1. Provide access to your metadata through a CSW2 interface supporting the CSW ISO
Metadata Application Profile2, which supports both Dublin Core3 and the ISO
191154/191195/191396 metadata standards.
2. Optionally, provide your local KOS that defines the terms used as keywords in your
metadata records and specifies how they semantically relate to the ICAN global KOS
terms.
The subsequent sections explain these two requirements. Any feedback regarding these
requirements and technology compatibility to implement and test these requirements is
welcome, and may be provided by contacting the author whose details are listed at the end of
this document.
CSW Requirements
The ICWA mediator supports CSW 2.0.2 fully and CSW 2.0.1 partially. Therefore, we
recommend that you use CSW 2.0.2 for delivering your metadata to the ICWA mediator.
The ICWA mediator requires CSW 2.0.2 supporting the ISO Metadata Application Profile
version 1.0.0, that is able to deliver metadata in Dublin Core and ISO 19115/19139. ISO
19119/19139 service metadata is also supported by the ICWA mediator.
The ICWA mediator has been tested with GeoNetwork 2.4 and later versions. GeoNetwork
automatically provides a mapping from ISO 19115/19119 to Dublin Core. The mediator should
support other CSW 2.0.2 implementations. Currently, all ICAN CSW nodes use GeoNetwork,
and ICWA functionality is tested against this. Other CSW servers will be tested in future, but
please contact the author if you have a particular CSW server that requires testing.
There is no particular requirement as to the ISO 19115/19119 metadata profile used, but
metadata records need to include keywords expressed in one of the following four encoding
forms:
1. As character strings (gco:CharacterString), each containing the URI of a concept from
your local KOS (if any). This encoding form is currently the favoured recommendation as
it uses a direct URI link to the semantic keyword concept. An example:
<gmd:descriptiveKeywords>
<gmd:MD_Keywords>
<gmd:keyword>
<gco:CharacterString>
http://vocab.nerc.ac.uk/collection/A03/current/Beach
</gco:CharacterString>
</gmd:keyword>
2 http://www.opengeospatial.org/standards/cat/
3 http://www.dublincore.org/
4 http://www.iso.org/iso/catalogue_detail.htm?csnumber=26020
5 http://www.iso.org/iso/catalogue_detail.htm?csnumber=39890
6 http://www.iso.org/iso/catalogue_detail.htm?csnumber=32557
© 2012 NETMAR Consortium EC FP7 Project No. 249024

NETMAR Deliverable D7.9.2: ICAN semantic interoperability cookbooks – Part 4
<gmd:thesaurusName>
<gmd:CI_Citation>
<gmd:title>
<gco:CharacterString>
Oregon Coastal Atlas Coastal Erosion Thesaurus discovery terms
</gco:CharacterString>
</gmd:title>
<gmd:date>
<gmd:CI_Date>
<gmd:date>
<gco:Date>2011-08-19</gco:Date>
</gmd:date>
<gmd:dateType>
<gmd:CI_DateTypeCode
codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/
resources/Codelist/gmxCodelists.xml#CI_DateTypeCode" codeListValue="revision">
Revision
</gmd:CI_DateTypeCode>
</gmd:dateType>
</gmd:CI_Date>
</gmd:date>
</gmd:CI_Citation>
</gmd:thesaurusName>
</gmd:MD_Keywords>
</gmd:descriptiveKeywords>
2. As character strings, each containing the label of a concept from your local KOS (if any).
However, this does not support a direct link to the concept. Instead, the mediator must
search all the local KOS for the relevant concept based on the label. Therefore, this
encoding form is not preferred. An example:
<gmd:descriptiveKeywords>
<gmd:MD_Keywords>
<gmd:keyword>
<gco:CharacterString>Beach</gco:CharacterString>
</gmd:keyword>
<gmd:thesaurusName>
<gmd:CI_Citation>
<gmd:title>
<gco:CharacterString>
Oregon Coastal Atlas Coastal Erosion Thesaurus discovery terms
</gco:CharacterString>
</gmd:title>
<gmd:date>
<gmd:CI_Date>
<gmd:date>
<gco:Date>2011-08-19</gco:Date>
</gmd:date>
<gmd:dateType>
<gmd:CI_DateTypeCode
codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/
resources/Codelist/gmxCodelists.xml#CI_DateTypeCode" codeListValue="revision">
Revision
</gmd:CI_DateTypeCode>
</gmd:dateType>
</gmd:CI_Date>
</gmd:date>
</gmd:CI_Citation>
</gmd:thesaurusName>
</gmd:MD_Keywords>
</gmd:descriptiveKeywords>
3. As anchor elements (gmx:Anchor), each containing both the URI and label of a concept
from your local KOS (if any). This encoding form is currently not supported by
© 2012 NETMAR Consortium EC FP7 Project No. 249024

NETMAR Deliverable D7.9.2: ICAN semantic interoperability cookbooks – Part 4
GeoNetwork (version 2.6.4 and earlier) and, therefore, has not been tested by ICWA. In
the long term this will be the preferred encoding form as it supports both a direct URI link
to the concept and a label of this concept. An example:
<gmd:descriptiveKeywords>
<gmd:MD_Keywords>
<gmd:keyword>
<gmx:Anchor xlink:href="http://vocab.nerc.ac.uk/collection/A03/current/Beach">
Beach
</gmx:Anchor>
</gmd:keyword>
<gmd:thesaurusName>
<gmd:CI_Citation>
<gmd:title>
<gco:CharacterString>
Oregon Coastal Atlas Coastal Erosion Thesaurus discovery terms
</gco:CharacterString>
</gmd:title>
<gmd:date>
<gmd:CI_Date>
<gmd:date>
<gco:Date>2011-08-19</gco:Date>
</gmd:date>
<gmd:dateType>
<gmd:CI_DateTypeCode
codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/
resources/Codelist/gmxCodelists.xml#CI_DateTypeCode" codeListValue="revision">
Revision
</gmd:CI_DateTypeCode>
</gmd:dateType>
</gmd:CI_Date>
</gmd:date>
</gmd:CI_Citation>
</gmd:thesaurusName>
</gmd:MD_Keywords>
</gmd:descriptiveKeywords>
4. As character strings containing free text keywords. This is the simplest encoding form. It
is not recommended because of its lack of a KOS, but it is supported to enable non-
semantic metadata catalogues to be readily connected to the ICWA. Therefore, smart
search functionality will not be supported for this encoding form.
<gmd:descriptiveKeywords>
<gmd:MD_Keywords>
<gmd:keyword>
<gco:CharacterString>Beach</gco:CharacterString>
</gmd:keyword>
</gmd:MD_Keywords>
</gmd:descriptiveKeywords>
KOS Requirements
Local knowledge organisation systems are used in ICWA to define the semantics of metadata
keywords used within a local atlas and how these relate semantically to the global KOS
concepts. A local KOS is a SKOS thesaurus organised into one or many concept schemes and
collections. It defines:
• The concepts represented by keywords (themes, parameters, instruments, etc.), their
labels (terms), and definitions (free text explaining the meaning of the concepts).
© 2012 NETMAR Consortium EC FP7 Project No. 249024

NETMAR Deliverable D7.9.2: ICAN semantic interoperability cookbooks – Part 4
• The semantic relationships between the local concepts.
• The semantic relationships between the local concepts and the global ones. These
relationships are referred to as mappings.
You are not required to define your metadata keywords in a KOS. However, you are
recommended to do so as this would improve data search as explained earlier in this document.
The ICWA mediator has a built-in SWS connector for querying global and local KOS. Therefore,
for your KOS to be accessed and used by the mediator, it must be delivered through SWS. You
can implement your own SWS (source code available from CMRC), but this means an extra
maintenance load for you. BODC are hosting and maintaining an operational vocabulary server
(NERC Vocabulary Server, NVS) that feeds the NETMAR SWS hosted by CMRC. You are
strongly recommended to profit from this existing infrastructure and provide BODC with your
KOS for inclusion in the NVS. BODC have made available two worksheets in an Excel
document for defining your concepts, relationships, and mappings in a very intuitive way,
avoiding the hassle of RDF, SKOS and ontology editing tools. Please refer to the
“Understanding Semantics” cookbook for examples of these worksheets.
Once you have finished filling out the worksheets, BODC can load it onto the NVS.
What is Next?
If your atlas fills the requirements above (CSW and KOS), adding it as a node in ICWA is a very
easy process. All you need to do is provide the ICWA administrator (CMRC) with the following
details:
1. URL of your CSW server;
2. Login and password for accessing metadata through your CSW server (if metadata
records are not public);
3. Optionally, but ideally, a logo of your atlas (250x250 PNG image);
4. Method used for encoding keywords (c.f., methods 1 to 4 listed in the CSW
Requirements section above);
5. If you are using method 1, 2 or 3 for keyword encoding then you will need to provide the
ICWA with the following information:
a. URL of the SWS responsible for delivering your KOS if other than the NVS and
the CMRC SWS;
b. URI of the concept schemes containing the concepts used as metadata
keywords.
Once provided with this information, the ICWA administrator can add your atlas in the ICWA
configuration file and it becomes an active node of ICWA.
© 2012 NETMAR Consortium EC FP7 Project No. 249024

NETMAR Deliverable D7.9.2: ICAN semantic interoperability cookbooks – Part 4
Acknowledgements
This cookbook was written for the International Coastal Atlas community under the auspices of
the NETMAR (Open Service Network for Marine Environmental Data) project. NETMAR is
partially funded by the European Commission under Theme ICT-2009.6.4 ICT for environmental
services and climate change adaptation of the Information & Communication Technologies FP7
Programme.
This document has been reviewed by, and incorporates comments from Declan Dunne of the
Coastal and Marine Research Centre, University College Cork; Torill Hamre of the Nansen
Environmental and Remote Sensing Center; Peter Walker of Plymouth Marine Laboratory; and
John Helly of the San Diego Supercomputer Center. Thanks to the reviewers for their help in
making the document clear and readable. Further feedback on this document is welcomed, and
may be provided by contacting the author whose details are below.
Document Information
Author Yassine Lassoued, Coastal and Marine Research Centre
Contact y.lassoued@ucc.ie
Version 2.1
Date 2012 July 30
Revisions 2.1 Responses to NETMAR internal review
2.0 Comments from ICAN community
1.0 2011 December 22
© 2012 NETMAR Consortium EC FP7 Project No. 249024