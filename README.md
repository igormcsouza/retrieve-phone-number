# Data Art Test Dev Task

## Instructions

Below is the test task for the Spirent Classic project – please send the response or questions in reply to this email.

Please note: the description is not 100% clearly written – same as the documentation in the project.  If you would like to ask us some questions, we are ready to clarify. The actual solution usually takes around 4 hours.

### Description

Writean application that searches for phone numbers in a set of text files and prints them in a unified format.

Files are located in a directory tree starting with _somewhere_ and should be processed regardless of the nesting level. At the same time, only text files with .txt extension need to be processed, and the others should be ignored.

Phone numbers in the source files can be given with the country code, with a three-digit area code or none at all. At the same time the number can have different spellings. All allowed formats are listed below:

```text
+7 812 number, +7 (495) number, +7812number, +7815 number, 1-814-number
(812) number, 812 number, 812 number, 095-number

123-4567, 123-45-67, 1234567
```

If the city code is not specified, it is considered equal to 812, if the country code is not specified, it is considered equal to 7. You need to find all the numbers in all of the files. Change formatting to the unified "full" format:

```text
+7 (812) 123-4567
```

remove duplicates and print the list of numbers in ascending order.

## How to run the answer

...
