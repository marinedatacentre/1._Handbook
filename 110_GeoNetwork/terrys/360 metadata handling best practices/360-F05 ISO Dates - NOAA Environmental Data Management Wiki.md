330-F05

- [Log
  in](https://geo-ide.noaa.gov/wiki/index.php?title=Special:UserLogin&returnto=ISO+Dates)

Top of Form

![](media/image1.wmf)

![](media/image2.wmf)

# ISO Dates

From NOAA Environmental Data Management Wiki

Jump to:[navigation](#mw-navigation), [search](#p-search)

There are many dates included in the ISO Metadata Standards and they
have several different types - each with its own characteristics. This
page has information about valid formats for those dates.

Ron Lake\'s blog includes a helpful
[description](http://www.galdosinc.com/archives/151) of time in GML.

Contents

 \[\] 

> [1 gco:Date Type](#gco:Date_Type)
>
> [2 gco:DateTime Type](#gco:DateTime_Type)
>
> [3 gmd:CI_Date Type](#gmd:CI_Date_Type)
>
> [4 On-Going Datasets](#On-Going_Datasets)
>
> [5 Relative Times](#Relative_Times)
>
> [6 Uncertain Times](#Uncertain_Times)
>
> [7 Translating FGDC Dates](#Translating_FGDC_Dates)

## gco:Date Type

> Date: gives values for year, month and day. Character encoding of a
> date is a string which shall follow the format for date specified by
> [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601). A full date is
> formatted as YYYYMMDD or YYYY-MM-DD. This type is used in the
> following fields:

- MI_Metadata.dateStamp - The ISO definition of this field is \"date
  that the metadata was created\". Common usage seems to be evolving
  towards \"date that the metadata was created or updated\" because it
  seems reasonable that, once the metadata have been updated, the date
  of that update is more interesting than the original creation date.
  Also, the update actually creates the current metadata, so this usage
  seems consistent with the ISO definition. Finally, the
  MD_MaintenanceInformation object does not include a dateOfLastUpdate
  field.

- MD_MaintenanceInformation.dateOfNextUpdate

- CI_Citation.editionDate - The ISO edition field is synonymous with the
  concept of version, so this is the release date for the version of the
  resource being cited.

## gco:DateTime Type

> DateTime: combination of a date and a time type (given by an hour,
> minute and second). Character encoding of a DateTime shall follow [ISO
> 8601](http://en.wikipedia.org/wiki/ISO_8601). Combined dates and times
> should be formatted as YYYYMMDDThh:mm:ss, YYYYMMDDThhmmss, or
> YYYY-MM-DDThh:mm:ss. These representations include no TimeZone
> indicator, so they are assumed to be local time. YYYYMMDDThh:mm:ssZ
> would indicate universal time.

- MD_Usage.usageDateTime

- DQ_Element.dateTime

- LI_ProcessStep.dateTime

- MD_StandardOrderProcess.plannedAvailableDateTime

> \<gmd:dateTime\>
>
> \<gco:DateTime\>2001-01-01T00:00:00\</gco:DateTime\>
>
> \</gmd:dateTime\>
>
> Note: This element was incorrectly defined in the ISO 19139 nschema as
> an xs:dateTime. That type does not allow all of the ISO 8601 options.
> Specifically, it does not allow the specification of a time range. It
> will likely be deprecated in the revision of the standard and replaced
> with stepDateTime.

## gmd:CI_Date Type

> This type is used only in the CI_Citation and is the only date type
> that includes a code from the CI_DateTypeCode codelist. Valid values
> from the CI_DateTypeCode CodeList are: creation (001), publication
> (002), and revision (003).

- CI_Citation.date.CI_Date.date

> \<gmd:CI_Date\>
>
> \<gmd:date\>
>
> \<gco:Date\>2000-01-01\</gco:Date\>
>
> \</gmd:date\>
>
> \<gmd:dateType\>
>
> \<gmd:CI_DateTypeCode
>
> codeList=\"http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#CI_DateTypeCode\"
>
> codeListValue=\"creation\"\>creation\</gmd:CI_DateTypeCode\>
>
> \</gmd:dateType\>
>
> \</gmd:CI_Date\>

## On-Going Datasets

> Many datasets are collected continuously through time. In these cases,
> a clear publication date does not exist. This situation can be
> indicated by a combination of \"inapplicable\" for the citation date,
> a status code = onGoing, and an endPosition with
> indeterminatePosition=now:
>
> \<gmd:date\>
>
> \<gmd:CI_Date\>
>
> \<gmd:date gco:nilReason=\"inapplicable\"/\>
>
> \<gmd:dateType\>
>
> \<gmd:CI_DateTypeCode
> codeList=\"http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#CI_DateTypeCode\"
>
> codeListValue=\"publication\"\>publication\</gmd:CI_DateTypeCode\>
>
> \</gmd:dateType\>
>
> \</gmd:CI_Date\>
>
> \</gmd:date\>
>
> \...
>
> \<gmd:status\>
>
> \<gmd:MD_ProgressCode codeListValue=\"onGoing\"
> codeList=\"http://www.isotc211.org/2005/resources
>
> /codeList.xml#MD_ProgressCode\"\>onGoing\</gmd:MD_ProgressCode\>
>
> \</gmd:status\>
>
> \...
>
> \<gmd:temporalElement\>
>
> \<gmd:EX_TemporalExtent id=\"boundingTemporalExtent\"\>
>
> \<gmd:extent\>
>
> \<gml:TimePeriod gml:id=\"d1e50\"\>
>
> \<gml:beginPosition\>2003-01-18T00:23:00.000Z\</gml:beginPosition\>
>
> \<gml:endPosition indeterminatePosition=\"now\"/\>
>
> \</gml:TimePeriod\>
>
> \</gmd:extent\>
>
> \</gmd:EX_TemporalExtent\>
>
> \</gmd:temporalElement\>

## Relative Times

> In some situations it is necessary to express a time in terms of a
> fixed period before the present. For example, on-going data processing
> systems might use observation sets and products from the previous day
> in the creation of a product for today. In these cases the duration
> and the end of the time period are known, so the XML looks like:
>
> \<gmd:temporalElement\>
>
> \<gmd:EX_TemporalExtent\>
>
> \<gmd:extent\>
>
> \<gml:TimePeriod gml:id=\"id\"\>
>
> \<gml:beginPosition indeterminatePosition=\"now\"/\>
>
> \<gml:endPosition indeterminatePosition=\"now\"/\>
>
> \<gml:duration\>P1D\</gml:duration\>
>
> \</gml:TimePeriod\>
>
> \</gmd:extent\>
>
> \</gmd:EX_TemporalExtent\>
>
> \</gmd:temporalElement\>
>
> See [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) for information
> on durations.

## Uncertain Times

> The GML elements for describing time positions (beginPosition and
> endPosition) include the indeterminatePosition attribute that can have
> values of before, after, now, and unknown. This attribute can be used
> with a time value to express uncertain times. For example, a dataset
> that began sometime before 1980 and continues to the present could be
> described as:
>
> \<gmd:extent\>
>
> \<gml:TimePeriod gml:id=\"id\"\>
>
> \<gml:beginPosition
> indeterminatePosition=\"before\"\>1980\</gml:beginPosition\>
>
> \<gml:endPosition indeterminatePosition=\"now\"/\>
>
> \</gml:TimePeriod\>
>
> \</gmd:extent\>

## Translating FGDC Dates

> The FGDC Standard allows a variety of date representations including
> \"Free Date\" in many locations. A number of assumptions must be made
> in order to translate these dates into the more structured formats
> required by ISO. If using XSLT\'s to translate FGDC date content to
> ISO (such as the NOAA transforms), logic must be added to achieve the
> highest level of interoperability and and highest rate of valid ISO
> input. These assumptions might be based on the length of the FGDC date
> string:
>
> 4 characters = YYYY
>
> 6 characters = YYYYMM or bcYYYY
>
> 7 characters = \'unknown\'
>
> 8 characters = YYYYMMDD or bcYYYYMM
>
> 10+ characters = bcYYYYMMDD or ccYYYYYYY\... or cdYYYYYYY\...
>
> This DECODE query is used in selecting dates dates with YYYYMMDD,
> YYYYMM and YYYY formats from Oracle (other formats are invalid):
>
> decode(LENGTH(DATETIME),6,\'\<gml:Date\>\'\|\|SUBSTR(DATETIME,1,4)\|\|\'-\'\|\|SUBSTR(DATETIME,5,2)\|\|\'\</gml:Date\>\',8,\'\<gml:Date\>\'\|\|DATETIME\|\|\'\</gml:Date\>\',4,\'\<gml:Date\>\'\|\|DATETIME\|\|\'\</gml:Date\>\',\'\<gml:Date\>\"\'\|\|DATETIME\|\|\'\"
> is an invalid date format\</gml:Date\>\')DATETIME
>
> Other assumptions must be made as well such as
>
> \- accounting for non-standard dates
>
> \- accounting for various capilatizations such as \'Unknown\' or
> \'unknown\' or \'UNKNOWN\'
>
> \- accounting for common misspellings such as \'unkown\', \'unknow\'
> ,\'unkwon\', etc.
>
> \- accounting for extra spaces
>
> \- accounting for input dates that start with bc, cc, or cd
>
> The indeterminatePosition can be used in a couple of cases if the date
> is unknown or unpublished
>
> \<gml:timePosition indeterminatePosition=\"unknown\"\>
>
> \<gml:timePosition indeterminatePosition=\"now\"\>
>
> If the date can not be recognized, set it as a reason for having no
> date:
>
> \<gmd:dateTime gco:nilReason=\"Date Content\"/\>.
>
> Of course, many of these will not be valid values for nilReason so
> they will be identified as problems during record validation. For the
> NOAA transforms, if a date is missing or cannot not be determined,
> gco:nilReason will be set to \'unknown\' by default. Ending dates of
> \'present\' and \'unknown\' (also taking
