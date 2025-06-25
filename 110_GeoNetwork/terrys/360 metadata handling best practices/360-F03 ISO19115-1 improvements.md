---
process_number: 360-F03
title: ISO19115-1 improvements
author: Terry Curran
created: 2018-08-05
modified: 2018-08-05
review_period: 3 years
---

**ISO 19115-1 New Capabilities**



**Contents**



- [[1 Do you need to unambiguously identify metadata records and parent metadata records?]{.underline}](https://geo-ide.noaa.gov/wiki/index.php?title=ISO_19115-1_New_Capabilities#Do_you_need_to_unambiguously_identify_metadata_records_and_parent_metadata_records.3F)



- [[2 Do you need to identify information elements using your own identifiers?]{.underline}](https://geo-ide.noaa.gov/wiki/index.php?title=ISO_19115-1_New_Capabilities#Do_you_need_to_identify_information_elements_using_your_own_identifiers.3F)



- [[3 Do you need to associate different types of dates with your metadata?]{.underline}](https://geo-ide.noaa.gov/wiki/index.php?title=ISO_19115-1_New_Capabilities#Do_you_need_to_associate_different_types_of_dates_with_your_metadata.3F)



- [[4 Do you need to include citations to information about the metadata standard you are using?]{.underline}](https://geo-ide.noaa.gov/wiki/index.php?title=ISO_19115-1_New_Capabilities#Do_you_need_to_include_citations_to_information_about_the_metadata_standard_you_are_using.3F)



- [[5 Do you need to provide metadata for multiple communities?]{.underline}](https://geo-ide.noaa.gov/wiki/index.php?title=ISO_19115-1_New_Capabilities#Do_you_need_to_provide_metadata_for_multiple_communities.3F)



- [[6 Do you have important documentation or other information that is published in the literature?]{.underline}](https://geo-ide.noaa.gov/wiki/index.php?title=ISO_19115-1_New_Capabilities#Do_you_have_important_documentation_or_other_information_that_is_published_in_the_literature.3F)



- [[7 Do you need to describe data services?]{.underline}](https://geo-ide.noaa.gov/wiki/index.php?title=ISO_19115-1_New_Capabilities#Do_you_need_to_describe_data_services.3F)



- [[8 Do you need to include information about how data are being used and respond to limitations identified by users?]{.underline}](https://geo-ide.noaa.gov/wiki/index.php?title=ISO_19115-1_New_Capabilities#Do_you_need_to_include_information_about_how_data_are_being_used_and_respond_to_limitations_identified_by_users.3F)



- [[9 Do you need special constraints for different time periods or users?]{.underline}](https://geo-ide.noaa.gov/wiki/index.php?title=ISO_19115-1_New_Capabilities#Do_you_need_special_constraints_for_different_time_periods_or_users.3F)



- [[10 Do you need to specify the medium that data are stored or available on?]{.underline}](https://geo-ide.noaa.gov/wiki/index.php?title=ISO_19115-1_New_Capabilities#Do_you_need_to_specify_the_medium_that_data_are_stored_or_available_on.3F)



- [[11 Do you need to identify multiple people or organizations in one role or re-use contact information in multiple metadata records?]{.underline}](https://geo-ide.noaa.gov/wiki/index.php?title=ISO_19115-1_New_Capabilities#Do_you_need_to_identify_multiple_people_or_organizations_in_one_role_or_re-use_contact_information_in_multiple_metadata_records.3F)



- [[12 Do you need to describe coverages with physical measurements, quality information, auxiliary information, reference information, or model results?]{.underline}](https://geo-ide.noaa.gov/wiki/index.php?title=ISO_19115-1_New_Capabilities#Do_you_need_to_describe_coverages_with_physical_measurements.2C_quality_information.2C_auxiliary_information.2C_reference_information.2C_or_model_results.3F)



- [[13 Do you need multiple names for measured or calculated parameters?]{.underline}](https://geo-ide.noaa.gov/wiki/index.php?title=ISO_19115-1_New_Capabilities#Do_you_need_multiple_names_for_measured_or_calculated_parameters.3F)



**Do you need to unambiguously identify metadata records and parent metadata records?**



ISO 19115 includes identifiers for many components but the identifiers for the metadata record (MD_Metadata/fileIdentifier) and for the parent metadata (MD_Metadata/parentIdentifier) are simple character strings. This can make it difficult to consistently provide other information that makes the identifiers unique and easier to use. In 19115-1 the types of these elements have changed to MD_Identifier which now includes a code, an authority, a namespace, a version, and a description. This allows much more consistent and robust identification of metadata records.



**Do you need to identify information elements using your own identifiers?**



The ISO Metadata Standards include identifiers for a large number if components. In 19115 these identifiers included a code and a citation for the authority of the code. This worked well in some cases, but it was difficult to simply associate a namespace with a code. In the revision the identifier has been expanded to include a namespace (called codespace), a version, and a description. This makes the identifiers easier to use in a web environment as well as making them easier for users to understand.



**Do you need to associate different types of dates with your metadata?**



ISO 19115 includes the capability to define several types of dates and time ranges for resources, but only includes a creation date for the metadata. The creation date is important, but having the flexibility to define other dates types is also useful.  ISO 19115-1 includes seventeen date types (creation, publication, lastUpdate, nextUpdate, superseded, ...) and any of them can be associated with the metadata.



**Do you need to include citations to information about the metadata standard you are using?**



Information about the standard and the version of the standard being used can be critical for users that are trying to understand your metadata or find information about the standard. ISO 19115 includes character strings that give the name and version of the standard. ISO 19115-1 includes a complete citation to the standard which unambiguously identifies the standard and makes it easy for users to find information that they might need to understand the standard or use it themselves.



**Do you need to provide metadata for multiple communities?**



In the hyper-connected cloud computing world, well documented data can be confidently reused by many communities and for many purposes. In some case those communities might need metadata presented in a different way or even with different content. ISO 19115-1 introduces the capability to provide citations and links to additional metadata that can be in ISO 19115-1 or in some other metadata standard.



**Do you have important documentation or other information that is published in the literature?**



Structured and standard metadata can only include a portion of the documentation needed to use and understand many datasets. Other important information might published in user guides, data dictionaries, scientific papers or other forms. ISO 19115-1 introduces the capability to add citations to that material to the metadata record.



**Do you need to describe data services?**



The distinction between data and services that provide data is continuing to blur as more and more data is made available using standard web services. This convergence includes not only the data, but metadata. ISO 19115 introduces the capability to facilitate service discovery using broad topic categories and, more importantly, to describe the spatial type, resolution, and spatio-temporal extent  of the data being served.



**Do you need to include information about how data are being used and respond to limitations identified by users?**



ISO 19115 includes information about when and how users are using data as well as limitations that they might identify as they use it. ISO 19115-1 introduces the capability for data providers to include responses to those limitations when they have been addressed.



**Do you need special constraints for different time periods or users?**



Some datasets have special constraints for selected time periods. For example,some data can only be used by the principle investigator or members of the science team for some period of time after they are collected. Use of other data sets might be limited by license arrangements. ISO 19115-1 introduces the capability to specify temporal and spatial extents of constraints. It also allows the specification of specific constraints for particular users.



**Do you need to specify the medium that data are stored or available on?**



ISO 19115 includes the capability to describe the native format that data are stored in and formats that are available to users. ISO 19115-1 introduces the capability to identify the medium the data are stored or available on in a particular format.



**Do you need to identify multiple people or organizations in one role or re-use contact information in multiple metadata records?**



ISO 19115 includes the capability to identify single people or organizations in roles related to the resource being described. ISO 19115-1 introduces the capability to include multiple people or organizations in a single role and to re-use contact information from a database or some other source in multiple roles.



**Do you need to describe coverages with physical measurements, quality information, auxiliary information, reference information, or model results?**



ISO 19115 allows the description of multiple electromagnetic bands in coverages which can be useful for instrument data but difficult to use when datasets include coverages with multiple layers with different types of information. ISO 19115-1 extends the MD_Band object to include this capability. It includes simple descriptive statistics for each layer and allows inclusion of custom layer attributes as well.



**Do you need multiple names for measured or calculated parameters?**



ISO 19115 supports only one name for each parameter in a dataset. This is the local name for the parameter. In many cases it can be helpful to assign standard names from other sources or descriptive names that can be used as labels. !SO 19115-1 adds this capability.
