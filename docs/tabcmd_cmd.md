---
title: tabcmd Commands
layout: docs
---

You can use the following commands with the tabcmd command line tool in Tableau Online:

**Important**: To ensure availability and avoid disruption with Tableau Online, make sure to upgrade your tabcmd client to a version greater than version 2020.2 before January 2022. The tabcmd versions are API backward compatible and should not require code changes. For more information, see Install tabcmd.

* TOC
{:toc}

# addusers *group-name*
Adds users to the specified group.

## Example

`tabcmd addusers "Development" --users "users.csv"`

## Options
`--users`

Add the users in the given .csv file to the specified group. The file should be a simple list with one user name per line. User names are not case sensitive. The users should already be created on Tableau Online.

For more information, see [CSV Import File Guidelines](https://help.tableau.com/current/online/en-us/csvguidelines.htm).

# --[no-]complete

When set to complete this option requires that all rows be valid for any change to succeed. If not specified, --complete is used.

Global options
The following options are used by all tabcmd commands. The `--server`, `--user`, and `--password` options are required at least once to begin a session. An authentication token is stored so subsequent commands can be run without including these options. This token remains valid for five minutes after the last command that used it.
<dl>
<dt>-h, --help</dt>

<dd>Displays the help for the command.

>Note: Some commands listed may not apply when using tabcmd with Tableau Online.
</dd>

<dt>-s, --server</dt>

<dd>The Tableau Online URL, which is required at least once to begin session.</dd>

<dt>-u, --user</dt>

<dd>The Tableau Online username, which is required at least once to begin session.</dd>

<dt>-p, --password</dt>

<dd>The Tableau Online password, which is required at least once to begin session.</dd>

<dt>--password-file</dt>

<dd>Allows the password to be stored in the given .txt file rather than the command line for increased security.</dd>

<dt>-t, --site</dt>

<dd>Indicates that the command applies to the site specified by the Tableau Online site ID, surrounded by single quotes or double quotes. Use this option if the user specified is associated with more than one site. Site ID is case-sensitive when using a cached authentication token. If you do not match case you may be prompted for a password even if the token is still valid.</dd>

<dt>--no-prompt</dt>

<dd>When specified, the command will not prompt for a password. If no valid password is provided the command will fail.</dd>

<dt>--[no-]cookie</dt>

<dd>When specified, the session ID is saved on login so subsequent commands will not need to log in. Use the no- prefix to not save the session ID. By default, the session is saved.</dd>

<dt>--timeout</dt>

<dd>Waits the specified number of seconds for the server to complete processing the command. By default, the process will wait until the server responds.<dd>

<dt>--</dt>

<dd>Specifies the end of options on the command line. You can use -- to indicate to tabcmd that anything that follows -- should not be interpreted as an option setting and can instead be interpreted as a value for the command. This is useful if you need to specify a value in the command that includes a hyphen. The following example shows how you might use -- in a tabcmd command, where -430105/Sheet1 is a required value for the export command.

          `tabcmd export --csv -f "D:\export10.csv" -- -430105/Sheet1`</dd>

</dl>


# createextracts
Creates extracts for a published workbook or data source.

## Options
<dl>
<dt>-d, --datasource</dt>

<dd>The name of the target data source for extract creation.</dd>

<dt>--embedded-datasources</dt>

<dd>A space-separated list of embedded data source names within the target workbook. Enclose data source names with double quotes if they contain spaces. Only available when creating extracts for a workbook.</dd>

<dt>--encrypt</dt>

<dd>Create encrypted extract.</dd>

<dt>--include-all</dt>

<dd>Include all embedded data sources within target workbook. Only available when creating extracts for workbook.</dd>

<dt>--parent-project-path</dt>

<dd>Path of the project that is the parent of the project that contains the target resource. Must specify the project name with `--project`.</dd>

<dt>--project</dt>

<dd>The name of the project that contains the target resource. Only necessary if --workbook or --datasource is specified. If unspecified, the default project 'Default' is used.</dd>

<dt>-u, -url</dt>

<dd>The canonical name for the resource as it appears in the URL.</dd>

<dt>-w, -workbook</dt>

<dd>The name of the target workbook for extract creation.</dd>
</dl>

<details><summary>Global options</summary>

The following options are used by all tabcmd commands. The `--server`, `--user`, and `--password` options are required at least once to begin a session. An authentication token is stored so subsequent commands can be run without including these options. This token remains valid for five minutes after the last command that used it.
<dl>
<dt>-h, --help</dt>

<dd>Displays the help for the command.

Note: Some commands listed may not apply when using tabcmd with Tableau Online.</dd>

<dt>-s, --server</dt>

<dd>The Tableau Online URL, which is required at least once to begin session.</dd>

<dt>-u, --user</dt>

<dd>The Tableau Online username, which is required at least once to begin session.</dd>

<dt>-p, --password</dt>

<dd>The Tableau Online password, which is required at least once to begin session.</dd>

<dt>--password-file</dd>

<dd>Allows the password to be stored in the given .txt file rather than the command line for increased security.</dd>

<dt>-t, --site</dt>

<dd>Indicates that the command applies to the site specified by the Tableau Online site ID, surrounded by single quotes or double quotes. Use this option if the user specified is associated with more than one site. Site ID is case-sensitive when using a cached authentication token. If you do not match case you may be prompted for a password even if the token is still valid.</dd>

<dt>--no-prompt</dt>

<dd>When specified, the command will not prompt for a password. If no valid password is provided the command will fail.</dd>

<dt>--[no-]cookie</dt>

<dd>When specified, the session ID is saved on login so subsequent commands will not need to log in. Use the no- prefix to not save the session ID. By default, the session is saved.</dd>

<dt>--timeout</dt>

<dd>Waits the specified number of seconds for the server to complete processing the command. By default, the process will wait until the server responds.</dd>

<dt>--</dt>

<dd>Specifies the end of options on the command line. You can use -- to indicate to tabcmd that anything that follows -- should not be interpreted as an option setting and can instead be interpreted as a value for the command. This is useful if you need to specify a value in the command that includes a hyphen. The following example shows how you might use -- in a tabcmd command, where -430105/Sheet1 is a required value for the export command.

```tabcmd export --csv -f "D:\export10.csv" -- -430105/Sheet1```
</dd>

</dl>
</details>

# creategroup *group-name*
Creates a group. Use addusers to add users after the group has been created.

## Example

```tabcmd creategroup "Development"```

<details><summary>Global options</summary>

The following options are used by all tabcmd commands. The `--server`, `--user`, and `--password` options are required at least once to begin a session. An authentication token is stored so subsequent commands can be run without including these options. This token remains valid for five minutes after the last command that used it.
<dl>
<dt>-h, --help</dt>

<dd>Displays the help for the command.

Note: Some commands listed may not apply when using tabcmd with Tableau Online.</dd>

<dt>-s, --server</dt>

<dd>The Tableau Online URL, which is required at least once to begin session.</dd>

<dt>-u, --user</dt>

<dd>The Tableau Online username, which is required at least once to begin session.</dd>

<dt>-p, --password</dt>

<dd>The Tableau Online password, which is required at least once to begin session.</dd>

<dt>--password-file</dd>

<dd>Allows the password to be stored in the given .txt file rather than the command line for increased security.</dd>

<dt>-t, --site</dt>

<dd>Indicates that the command applies to the site specified by the Tableau Online site ID, surrounded by single quotes or double quotes. Use this option if the user specified is associated with more than one site. Site ID is case-sensitive when using a cached authentication token. If you do not match case you may be prompted for a password even if the token is still valid.</dd>

<dt>--no-prompt</dt>

<dd>When specified, the command will not prompt for a password. If no valid password is provided the command will fail.</dd>

<dt>--[no-]cookie</dt>

<dd>When specified, the session ID is saved on login so subsequent commands will not need to log in. Use the no- prefix to not save the session ID. By default, the session is saved.</dd>

<dt>--timeout</dt>

<dd>Waits the specified number of seconds for the server to complete processing the command. By default, the process will wait until the server responds.</dd>

<dt>--</dt>

<dd>Specifies the end of options on the command line. You can use -- to indicate to tabcmd that anything that follows -- should not be interpreted as an option setting and can instead be interpreted as a value for the command. This is useful if you need to specify a value in the command that includes a hyphen. The following example shows how you might use -- in a tabcmd command, where -430105/Sheet1 is a required value for the export command.

```tabcmd export --csv -f "D:\export10.csv" -- -430105/Sheet1```
</dd>

</dl>
</details>

# createproject *project-name*
Creates a project.

## Example

```tabcmd createproject -n "Quarterly_Reports" -d "Workbooks showing quarterly sales reports."```

## Options
<dl>
<dt>-n, --name</dt>

<dd>Specifies the name of the project that you want to create.</dd>

<dt>--parent-project-path</dt>

<dd>Specifies the name of the parent project for the nested project as specified with the -n option. For example, to specify a project called "Nested" that exists in a "Main" project, use the following syntax: ```--parent-project-path "Main" -n "Nested".```</dd>

<dt>-d, --description</dt>

<dd>Specifies a description for the project.</dd>
</dl>

<details><summary>Global options</summary>

The following options are used by all tabcmd commands. The `--server`, `--user`, and `--password` options are required at least once to begin a session. An authentication token is stored so subsequent commands can be run without including these options. This token remains valid for five minutes after the last command that used it.
<dl>
<dt>-h, --help</dt>

<dd>Displays the help for the command.

Note: Some commands listed may not apply when using tabcmd with Tableau Online.</dd>

<dt>-s, --server</dt>

<dd>The Tableau Online URL, which is required at least once to begin session.</dd>

<dt>-u, --user</dt>

<dd>The Tableau Online username, which is required at least once to begin session.</dd>

<dt>-p, --password</dt>

<dd>The Tableau Online password, which is required at least once to begin session.</dd>

<dt>--password-file</dd>

<dd>Allows the password to be stored in the given .txt file rather than the command line for increased security.</dd>

<dt>-t, --site</dt>

<dd>Indicates that the command applies to the site specified by the Tableau Online site ID, surrounded by single quotes or double quotes. Use this option if the user specified is associated with more than one site. Site ID is case-sensitive when using a cached authentication token. If you do not match case you may be prompted for a password even if the token is still valid.</dd>

<dt>--no-prompt</dt>

<dd>When specified, the command will not prompt for a password. If no valid password is provided the command will fail.</dd>

<dt>--[no-]cookie</dt>

<dd>When specified, the session ID is saved on login so subsequent commands will not need to log in. Use the no- prefix to not save the session ID. By default, the session is saved.</dd>

<dt>--timeout</dt>

<dd>Waits the specified number of seconds for the server to complete processing the command. By default, the process will wait until the server responds.</dd>

<dt>--</dt>

<dd>Specifies the end of options on the command line. You can use -- to indicate to tabcmd that anything that follows -- should not be interpreted as an option setting and can instead be interpreted as a value for the command. This is useful if you need to specify a value in the command that includes a hyphen. The following example shows how you might use -- in a tabcmd command, where -430105/Sheet1 is a required value for the export command.

```tabcmd export --csv -f "D:\export10.csv" -- -430105/Sheet1```
</dd>

</dl>
</details>

# createsiteusers *filename.csv*

Adds users to a site, based on information supplied in a comma-separated values (CSV) file. If the user is not already created on the server, the command creates the user before adding that user to the site.

The CSV file must contain one or more user names and can also include (for each user) a password, full name, license type, administrator level, publisher (yes/no), and email address. For information about the format of the CSV file, see CSV Import File Guidelines.

As an alternative to including administrator level and publisher permissions in the CSV file, you can pass access level information by including the --role option and specifying the site role you want to assign users listed in the CSV file.

By default, users are added to the site that you are logged in to. To add users to a different site, include the global --site option and specify that site. (You must have permissions to create users on the site you specify.)

## Example

```tabcmd createsiteusers "users.csv" --role "Explorer"```

## Options
<dl>
<dt>--admin-type</dt>

<dd>Deprecated. Use the --role option instead.</dd>

<dt>--auth-type</dt>

<dd>Sets the authentication type (TableauID or SAML) for all users in the .csv file. If unspecified, the default is TableauID.

Note: To use SAML authentication, the site itself must be SAML-enabled as well. For information, see Enable SAML Authentication on a Site.</dd>

<dt>--[no-]complete</dt>

<dd>Deprecated. Default error behavior: if there are more than 3 errors within a ten-row span, then the command will fail.</dd>

<dt>--no-publisher</dt>

<dd>Deprecated. Use the `--role` option instead.</dd>

<dt>--nowait</dt>

<dd>Do not wait for asynchronous jobs to complete.</dd>

<dt>--publisher</dt>

<dd>Deprecated. Use the --role option instead.</dd>

<dt>--role</dt>

<dd>Specifies a site role for all users in the .csv file. When you want to assign site roles using the --role option, create a separate CSV file for each site role.

Valid values are: ServerAdministrator, SiteAdministratorCreator, SiteAdministratorExplorer, SiteAdministrator, Creator, ExplorerCanPublish, Publisher, Explorer, Interactor, Viewer, and Unlicensed.

The default is Unlicensed for new users and unchanged for existing users. Users are added as unlicensed also if you have a user-based server installation, and if the createsiteusers command creates a new user, but you have already reached the limit on the number of licenses for your users.

Note: On a multi-site Tableau Server, if you want to assign the ServerAdministrator site role using the --role option, use the createusers command instead of createsiteusers.
</dd>
<dt>--silent-progress</dt>

<dd>Do not display progress messages for the command.</dd>
</dl>

<details><summary>Global options</summary>

The following options are used by all tabcmd commands. The `--server`, `--user`, and `--password` options are required at least once to begin a session. An authentication token is stored so subsequent commands can be run without including these options. This token remains valid for five minutes after the last command that used it.
<dl>
<dt>-h, --help</dt>

<dd>Displays the help for the command.

Note: Some commands listed may not apply when using tabcmd with Tableau Online.</dd>

<dt>-s, --server</dt>

<dd>The Tableau Online URL, which is required at least once to begin session.</dd>

<dt>-u, --user</dt>

<dd>The Tableau Online username, which is required at least once to begin session.</dd>

<dt>-p, --password</dt>

<dd>The Tableau Online password, which is required at least once to begin session.</dd>

<dt>--password-file</dd>

<dd>Allows the password to be stored in the given .txt file rather than the command line for increased security.</dd>

<dt>-t, --site</dt>

<dd>Indicates that the command applies to the site specified by the Tableau Online site ID, surrounded by single quotes or double quotes. Use this option if the user specified is associated with more than one site. Site ID is case-sensitive when using a cached authentication token. If you do not match case you may be prompted for a password even if the token is still valid.</dd>

<dt>--no-prompt</dt>

<dd>When specified, the command will not prompt for a password. If no valid password is provided the command will fail.</dd>

<dt>--[no-]cookie</dt>

<dd>When specified, the session ID is saved on login so subsequent commands will not need to log in. Use the no- prefix to not save the session ID. By default, the session is saved.</dd>

<dt>--timeout</dt>

<dd>Waits the specified number of seconds for the server to complete processing the command. By default, the process will wait until the server responds.</dd>

<dt>--</dt>

<dd>Specifies the end of options on the command line. You can use -- to indicate to tabcmd that anything that follows -- should not be interpreted as an option setting and can instead be interpreted as a value for the command. This is useful if you need to specify a value in the command that includes a hyphen. The following example shows how you might use -- in a tabcmd command, where -430105/Sheet1 is a required value for the export command.

```tabcmd export --csv -f "D:\export10.csv" -- -430105/Sheet1```
</dd>

</dl>
</details>

# delete workbook-name or datasource-name
Deletes the specified workbook or data source from the server.

This command takes the name of the workbook or data source as it is on the server, not the file name when it was published.

## Example

`tabcmd delete "Sales_Analysis"`

## Options
<dl>
<dt>-r, --project</dt>

<dd>The name of the project containing the workbook or data source you want to delete. If not specified, the “Default” project is assumed.</dd>

<dt>--parent-project-path</dt>

<dd>Specifies the name of the parent project for the nested project as specified with the -r option. For example, to specify a project called "Nested" that exists in a "Main" project, use the following syntax: --parent-project-path "Main" -r "Nested".</dd>

<dt>--workbook</dt>

<dd>The name of the workbook you want to delete.</dd>

<dt>--datasource</dt>

<dd>The name of the data source you want to delete.</dd>
</dl>

<details><summary>Global options</summary>

The following options are used by all tabcmd commands. The `--server`, `--user`, and `--password` options are required at least once to begin a session. An authentication token is stored so subsequent commands can be run without including these options. This token remains valid for five minutes after the last command that used it.
<dl>
<dt>-h, --help</dt>

<dd>Displays the help for the command.

Note: Some commands listed may not apply when using tabcmd with Tableau Online.</dd>

<dt>-s, --server</dt>

<dd>The Tableau Online URL, which is required at least once to begin session.</dd>

<dt>-u, --user</dt>

<dd>The Tableau Online username, which is required at least once to begin session.</dd>

<dt>-p, --password</dt>

<dd>The Tableau Online password, which is required at least once to begin session.</dd>

<dt>--password-file</dd>

<dd>Allows the password to be stored in the given .txt file rather than the command line for increased security.</dd>

<dt>-t, --site</dt>

<dd>Indicates that the command applies to the site specified by the Tableau Online site ID, surrounded by single quotes or double quotes. Use this option if the user specified is associated with more than one site. Site ID is case-sensitive when using a cached authentication token. If you do not match case you may be prompted for a password even if the token is still valid.</dd>

<dt>--no-prompt</dt>

<dd>When specified, the command will not prompt for a password. If no valid password is provided the command will fail.</dd>

<dt>--[no-]cookie</dt>

<dd>When specified, the session ID is saved on login so subsequent commands will not need to log in. Use the no- prefix to not save the session ID. By default, the session is saved.</dd>

<dt>--timeout</dt>

<dd>Waits the specified number of seconds for the server to complete processing the command. By default, the process will wait until the server responds.</dd>

<dt>--</dt>

<dd>Specifies the end of options on the command line. You can use -- to indicate to tabcmd that anything that follows -- should not be interpreted as an option setting and can instead be interpreted as a value for the command. This is useful if you need to specify a value in the command that includes a hyphen. The following example shows how you might use -- in a tabcmd command, where -430105/Sheet1 is a required value for the export command.

```tabcmd export --csv -f "D:\export10.csv" -- -430105/Sheet1```
</dd>

</dl>
</details>

# deleteextracts

Deletes extracts for a published workbook or data source.

## Options
<dl>
    <dt>-d, --datasource</dt>
    <dd>The name of the target data source for extract deletion.</dd>
    <dt>--embedded-datasources</dt>
    <dd>A space-separated list of embedded data source names within the target workbook. Enclose data source names with double quotes if they contain spaces. Only available when deleting extracts for a workbook.</dd>
    <dt>--encrypt</dt>
    <dd>Create encrypted extract.</dd>

    <dt>--include-all</dt>

    <dd>Include all embedded data sources within target workbook.</dd>

    <dt>--parent-project-path</dt>

    <dd>Path of the project that is the parent of the project that contains the target resource. Must specify the project name with --project.</dd>

    <dt>--project</dt>

    <dd>The name of the project that contains the target resource. Only necessary if --workbook or --datasource is specified. If unspecified, the default project 'Default' is used.</dd>

    <dt>-u, -url</dt>

    <dd>The canonical name for the resource as it appears in the URL.</dd>

    <dt>-w, -workbook</dt>

    <dd>The name of the target workbook for extract deletion.</dd>
</dl>

<details><summary>Global options</summary>

The following options are used by all tabcmd commands. The `--server`, `--user`, and `--password` options are required at least once to begin a session. An authentication token is stored so subsequent commands can be run without including these options. This token remains valid for five minutes after the last command that used it.
<dl>
<dt>-h, --help</dt>

<dd>Displays the help for the command.

Note: Some commands listed may not apply when using tabcmd with Tableau Online.</dd>

<dt>-s, --server</dt>

<dd>The Tableau Online URL, which is required at least once to begin session.</dd>

<dt>-u, --user</dt>

<dd>The Tableau Online username, which is required at least once to begin session.</dd>

<dt>-p, --password</dt>

<dd>The Tableau Online password, which is required at least once to begin session.</dd>

<dt>--password-file</dd>

<dd>Allows the password to be stored in the given .txt file rather than the command line for increased security.</dd>

<dt>-t, --site</dt>

<dd>Indicates that the command applies to the site specified by the Tableau Online site ID, surrounded by single quotes or double quotes. Use this option if the user specified is associated with more than one site. Site ID is case-sensitive when using a cached authentication token. If you do not match case you may be prompted for a password even if the token is still valid.</dd>

<dt>--no-prompt</dt>

<dd>When specified, the command will not prompt for a password. If no valid password is provided the command will fail.</dd>

<dt>--[no-]cookie</dt>

<dd>When specified, the session ID is saved on login so subsequent commands will not need to log in. Use the no- prefix to not save the session ID. By default, the session is saved.</dd>

<dt>--timeout</dt>

<dd>Waits the specified number of seconds for the server to complete processing the command. By default, the process will wait until the server responds.</dd>

<dt>--</dt>

<dd>Specifies the end of options on the command line. You can use -- to indicate to tabcmd that anything that follows -- should not be interpreted as an option setting and can instead be interpreted as a value for the command. This is useful if you need to specify a value in the command that includes a hyphen. The following example shows how you might use -- in a tabcmd command, where -430105/Sheet1 is a required value for the export command.

```tabcmd export --csv -f "D:\export10.csv" -- -430105/Sheet1```
</dd>

</dl>
</details>


# deletegroup *group-name*
Deletes the specified group from the server.

## Example

`tabcmd deletegroup "Development"`

<details><summary>Global options</summary>

The following options are used by all tabcmd commands. The `--server`, `--user`, and `--password` options are required at least once to begin a session. An authentication token is stored so subsequent commands can be run without including these options. This token remains valid for five minutes after the last command that used it.
<dl>
<dt>-h, --help</dt>

<dd>Displays the help for the command.

Note: Some commands listed may not apply when using tabcmd with Tableau Online.</dd>

<dt>-s, --server</dt>

<dd>The Tableau Online URL, which is required at least once to begin session.</dd>

<dt>-u, --user</dt>

<dd>The Tableau Online username, which is required at least once to begin session.</dd>

<dt>-p, --password</dt>

<dd>The Tableau Online password, which is required at least once to begin session.</dd>

<dt>--password-file</dd>

<dd>Allows the password to be stored in the given .txt file rather than the command line for increased security.</dd>

<dt>-t, --site</dt>

<dd>Indicates that the command applies to the site specified by the Tableau Online site ID, surrounded by single quotes or double quotes. Use this option if the user specified is associated with more than one site. Site ID is case-sensitive when using a cached authentication token. If you do not match case you may be prompted for a password even if the token is still valid.</dd>

<dt>--no-prompt</dt>

<dd>When specified, the command will not prompt for a password. If no valid password is provided the command will fail.</dd>

<dt>--[no-]cookie</dt>

<dd>When specified, the session ID is saved on login so subsequent commands will not need to log in. Use the no- prefix to not save the session ID. By default, the session is saved.</dd>

<dt>--timeout</dt>

<dd>Waits the specified number of seconds for the server to complete processing the command. By default, the process will wait until the server responds.</dd>

<dt>--</dt>

<dd>Specifies the end of options on the command line. You can use -- to indicate to tabcmd that anything that follows -- should not be interpreted as an option setting and can instead be interpreted as a value for the command. This is useful if you need to specify a value in the command that includes a hyphen. The following example shows how you might use -- in a tabcmd command, where -430105/Sheet1 is a required value for the export command.

```tabcmd export --csv -f "D:\export10.csv" -- -430105/Sheet1```
</dd>

</dl>
</details>


# deleteproject *project-name*
Deletes the specified project from the server.

Using tabcmd, you can specify only a top-level project in a project hierarchy. To automate tasks you want to perform on a project within a parent project, use the equivalent Tableau REST API(Link opens in a new window) call.

## Example

`tabcmd deleteproject "Designs"`

## Option
<dl>

<dt>--parent-project-path</dt>

<dd>Specifies the name of the parent project for the nested project as specified with the command. For example, to specify a project called "Designs" that exists in a "Main" project, use the following syntax: --parent-project-path "Main" "Designs".</dd>
</dl>

<details><summary>Global options</summary>

The following options are used by all tabcmd commands. The `--server`, `--user`, and `--password` options are required at least once to begin a session. An authentication token is stored so subsequent commands can be run without including these options. This token remains valid for five minutes after the last command that used it.
<dl>
<dt>-h, --help</dt>

<dd>Displays the help for the command.

Note: Some commands listed may not apply when using tabcmd with Tableau Online.</dd>

<dt>-s, --server</dt>

<dd>The Tableau Online URL, which is required at least once to begin session.</dd>

<dt>-u, --user</dt>

<dd>The Tableau Online username, which is required at least once to begin session.</dd>

<dt>-p, --password</dt>

<dd>The Tableau Online password, which is required at least once to begin session.</dd>

<dt>--password-file</dd>

<dd>Allows the password to be stored in the given .txt file rather than the command line for increased security.</dd>

<dt>-t, --site</dt>

<dd>Indicates that the command applies to the site specified by the Tableau Online site ID, surrounded by single quotes or double quotes. Use this option if the user specified is associated with more than one site. Site ID is case-sensitive when using a cached authentication token. If you do not match case you may be prompted for a password even if the token is still valid.</dd>

<dt>--no-prompt</dt>

<dd>When specified, the command will not prompt for a password. If no valid password is provided the command will fail.</dd>

<dt>--[no-]cookie</dt>

<dd>When specified, the session ID is saved on login so subsequent commands will not need to log in. Use the no- prefix to not save the session ID. By default, the session is saved.</dd>

<dt>--timeout</dt>

<dd>Waits the specified number of seconds for the server to complete processing the command. By default, the process will wait until the server responds.</dd>

<dt>--</dt>

<dd>Specifies the end of options on the command line. You can use -- to indicate to tabcmd that anything that follows -- should not be interpreted as an option setting and can instead be interpreted as a value for the command. This is useful if you need to specify a value in the command that includes a hyphen. The following example shows how you might use -- in a tabcmd command, where -430105/Sheet1 is a required value for the export command.

```tabcmd export --csv -f "D:\export10.csv" -- -430105/Sheet1```
</dd>

</dl>
</details>


# deletesiteusers *filename.csv*
Removes users from from the site that you are logged in to. The users to be removed are specified in a file that contains a simple list of one user name per line. (No additional information is required beyond the user name.)

By default, if the server has only one site, or if the user belongs to only one site, the user is also removed from the server. On a Tableau Server Enterprise installation, if the server contains multiple sites, users who are assigned the site role of Server Administrator are removed from the site but are not removed from the server.

If the user owns content, the user's role is change to Unlicensed, but the user is not removed from the server or the site. The content is still owned by that user. To remove the user completely, you must change the owner of the content and then try removing the user again.

## Example

`tabcmd deletesiteusers "users.csv"`

<details><summary>Global options</summary>

The following options are used by all tabcmd commands. The `--server`, `--user`, and `--password` options are required at least once to begin a session. An authentication token is stored so subsequent commands can be run without including these options. This token remains valid for five minutes after the last command that used it.
<dl>
<dt>-h, --help</dt>

<dd>Displays the help for the command.

Note: Some commands listed may not apply when using tabcmd with Tableau Online.</dd>

<dt>-s, --server</dt>

<dd>The Tableau Online URL, which is required at least once to begin session.</dd>

<dt>-u, --user</dt>

<dd>The Tableau Online username, which is required at least once to begin session.</dd>

<dt>-p, --password</dt>

<dd>The Tableau Online password, which is required at least once to begin session.</dd>

<dt>--password-file</dd>

<dd>Allows the password to be stored in the given .txt file rather than the command line for increased security.</dd>

<dt>-t, --site</dt>

<dd>Indicates that the command applies to the site specified by the Tableau Online site ID, surrounded by single quotes or double quotes. Use this option if the user specified is associated with more than one site. Site ID is case-sensitive when using a cached authentication token. If you do not match case you may be prompted for a password even if the token is still valid.</dd>

<dt>--no-prompt</dt>

<dd>When specified, the command will not prompt for a password. If no valid password is provided the command will fail.</dd>

<dt>--[no-]cookie</dt>

<dd>When specified, the session ID is saved on login so subsequent commands will not need to log in. Use the no- prefix to not save the session ID. By default, the session is saved.</dd>

<dt>--timeout</dt>

<dd>Waits the specified number of seconds for the server to complete processing the command. By default, the process will wait until the server responds.</dd>

<dt>--</dt>

<dd>Specifies the end of options on the command line. You can use -- to indicate to tabcmd that anything that follows -- should not be interpreted as an option setting and can instead be interpreted as a value for the command. This is useful if you need to specify a value in the command that includes a hyphen. The following example shows how you might use -- in a tabcmd command, where -430105/Sheet1 is a required value for the export command.

```tabcmd export --csv -f "D:\export10.csv" -- -430105/Sheet1```
</dd>

</dl>
</details>


# export
Exports a view or workbook from Tableau Online and saves it to a file. This command can also export just the data used for a view. View data is exported at the summary level. To export detail-level data, you must use the Tableau Server UI. For details, see Download Views and Workbooks(Link opens in a new window).

Note the following when you use this command:

* **Permissions**: To export, you must have the **Export Image** permission. By default, this permission is Allowed or Inherited for all roles, although permissions can be set per workbook or view.

* **Exporting data**: To export just the data for a view, use the --csv option. This exports the summary data used in a view to a .csv file.

* **Specifying the view, workbook, or data to export**:

    * Use part of the URL to identify what to export, specifically the "workbook/view" string as it appears in the URL for the workbook or view. Do not use the “friendly name,” and exclude the :iid=<n> session ID at the end of the URL.

        For example, the Tableau sample view Global Temperatures in the Regionalworkbook has a URL similar to this: <server_name>/#/views/Regional/GlobalTemperatures?:iid=3

        To export the Global Temperatures view, use the string Regional/GlobalTemperatures.

        Do notuse Regional/Global Temperatures, or Regional/GlobalTemperatures?:iid=3.

    * If the server is running multiple sites and the view or workbook is on a site other than Default, Use -t <site_id>.

    * To export a workbook, get the URL string by opening a view in the workbook, and include the view in the string you use.

        In the above example, to export the Regional workbook, use the string `Regional/GlobalTemperatures`.

    * To export a workbook, it must have been published with **Show Sheets as Tabs** selected in the Tableau Desktop Publish dialog box.

        Note: The Tableau workbook that contains the [admin views](https://help.tableau.com/current/online/en-us/adminview.htm) cannot be exported.

    * To filter the data you download, add a parameter filter using this format:
    `?<filter_name>=value`
    or, if filtering on a parameter and that parameter has a display name that matches the name of a measure or dimension:
    `?Parameters.<filter_name>=value`

* **The saved file's format**: Your format options depend on what's being exported. A workbook can only be exported as a PDF using the --fullpdf argument. A view can be exported as a PDF (--pdf) or a PNG (--png).

* **The saved file's name and location** (optional): If you don't provide a name, it will be derived from the view or workbook name. If you don't provide a location, the file will be saved to your current working directory. Otherwise, you can specify a full path or one that's relative to your current working directory.
Note: You must include a file name extension such as .csv or .pdf. The command does not automatically add an extension to the file name that you provide.

Dashboard web page objects not included in PDF exports: A dashboard can optionally include a web page object. If you are performing an export to PDF of a dashboard that includes a web page object, the web page object won't be included in the PDF.

Non-ASCII and non-standard ASCII characters and PDF exports: If you are exporting a view or workbook with a name that includes a character outside the ASCII character set, or a non-standard ASCII character set, you need to URL encode (percent-encode) the character.

For example if your command includes the city Zürich, you need to URL encode it as Z%C3%BCrich:

tabcmd export "/Cities/Sheet1?locationCity=Z%C3%BCrich" -fullpdf

Clearing the Cache to Use Real-Time Data

You can optionally add the URL parameter ?:refresh=yes to force a fresh data query instead of pulling the results from the cache. If you are using tabcmd with your own scripting and the refresh URL parameter is being used a great deal, this can have a negative impact on performance. It's recommended that you use refresh only when real-time data is required—for example, on a single dashboard instead of on an entire workbook.

## Examples

Views

tabcmd export "Q1Sales/Sales_Report" --csv -f "Weekly-Report.csv"

tabcmd export -t Sales "Sales/Sales_Analysis" --pdf -f "C:\Tableau_Workbooks\Weekly-Reports.pdf"

tabcmd export "Finance/InvestmentGrowth" --png

tabcmd export "Finance/InvestmentGrowth?:refresh=yes" --png

Workbooks

tabcmd export "Q1Sales/Sales_Report" --fullpdf

tabcmd export "Sales/Sales_Analysis" --fullpdf --pagesize tabloid -f "C:\Tableau_Workbooks\Weekly-Reports.pdf"

Options
-f, --filename

Saves the file with the given filename and extension.

--csv

View only. Export the view's data (summary data) in .csv format.

--pdf

View only. Export as a PDF.

--png

View only. Export as an image in .png format.

--fullpdf

Workbook only. Export as a PDF. The workbook must have been published with Show Sheets as Tabs enabled.

--pagelayout

Sets the page orientation (landscape or portrait) of the exported PDF. If not specified, its Tableau Desktop setting will be used.

--pagesize

Sets the page size of the exported PDF as one of the following: unspecified, letter, legal, note folio, tabloid, ledger, statement, executive, a3, a4, a5, b4, b5, or quarto. Default is letter.

--width

Sets the width in pixels. Default is 800 px.

--height

Sets the height in pixels. Default is 600 px.

Global options
get url
Gets the resource from Tableau Online that's represented by the specified (partial) URL. The result is returned as a file.

Note the following when you use this command:

Permissions: To get a file, you must have the Download/Web Save As permission. By default, this permission is allowed or inherited for all roles, although permissions can be set per workbook or view.

Specifying a view or workbook to get: You specify a view to get using the "/views/<workbookname>/<viewname>.<extension>" string, and specify a workbook to get using the "/workbooks/<workbookname>.<extension>" string. Replace <workbookname> and <viewname> with the names of the workbook and view as they appear in the URL when you open the view in a browser and replace <extension> with the type of file you want to save. Do not use the session ID at the end of the URL (?:iid=<n>) or the "friendly" name of the workbook or view.

For example, when you open a view Regional Totals in a workbook named Metrics Summary, the URL will look similar to this:

/views/MetricsSummary_1/RegionalTotals?:iid=1

Use the string /views/MetricsSummary_1/RegionalTotals.<extension> to get the view.

Use the string /workbooks/MetricsSummary_1.<extension> to get the workbook.

File extension: The URL must include a file extension. The extension determines what's returned. A view can be returned in PDF, PNG, or CSV (summary data only) format. A Tableau workbook is returned as a TWB if it connects to a published data source or uses a live connection, or a TWBX if it connects to a data extract.

Note: If you are downloading a view to a PDF or PNG file, and if you include a --filename parameter that includes the .pdf or .png extension, you do not have to include a .pdf or .png extension in the URL.

The saved file's name and location (optional): The name you use for --filename should include the file extension. If you don't provide a name and file extension, both will be derived from the URL string. If you don't provide a location, the file is saved to your current working directory. Otherwise, you can specify a full path or one that's relative to your current working directory.

PNG size (optional): If the saved file is a PNG, you can specify the size, in pixels, in the URL.

Clearing the cache to use real-time data

You can optionally add the URL parameter ?:refresh=yes to force a fresh data query instead of pulling the results from the cache. If you are using tabcmd with your own scripting, using the refresh parameter a great deal can have a negative impact on performance. It's recommended that you use refresh only when real-time data is required—for example, on a single dashboard instead of on an entire workbook.

Examples

Views

tabcmd get "/views/Sales_Analysis/Sales_Report.png" --filename "Weekly-Report.png"

tabcmd get "/views/Finance/InvestmentGrowth.pdf" -f "Q1Growth.pdf"

tabcmd get "/views/Finance/InvestmentGrowth" -f "Q1Growth.pdf"

tabcmd get "/views/Finance/InvestmentGrowth.csv"

tabcmd get "/views/Finance/InvestmentGrowth.png?:size=640,480" -f growth.png

tabcmd get "/views/Finance/InvestmentGrowth.png?:refresh=yes" -f growth.png

Workbooks

tabcmd get "/workbooks/Sales_Analysis.twb" -f "C:\Tableau_Workbooks\Weekly-Reports.twb"

<details><summary>Global options</summary>

The following options are used by all tabcmd commands. The `--server`, `--user`, and `--password` options are required at least once to begin a session. An authentication token is stored so subsequent commands can be run without including these options. This token remains valid for five minutes after the last command that used it.
<dl>
<dt>-h, --help</dt>

<dd>Displays the help for the command.

Note: Some commands listed may not apply when using tabcmd with Tableau Online.</dd>

<dt>-s, --server</dt>

<dd>The Tableau Online URL, which is required at least once to begin session.</dd>

<dt>-u, --user</dt>

<dd>The Tableau Online username, which is required at least once to begin session.</dd>

<dt>-p, --password</dt>

<dd>The Tableau Online password, which is required at least once to begin session.</dd>

<dt>--password-file</dd>

<dd>Allows the password to be stored in the given .txt file rather than the command line for increased security.</dd>

<dt>-t, --site</dt>

<dd>Indicates that the command applies to the site specified by the Tableau Online site ID, surrounded by single quotes or double quotes. Use this option if the user specified is associated with more than one site. Site ID is case-sensitive when using a cached authentication token. If you do not match case you may be prompted for a password even if the token is still valid.</dd>

<dt>--no-prompt</dt>

<dd>When specified, the command will not prompt for a password. If no valid password is provided the command will fail.</dd>

<dt>--[no-]cookie</dt>

<dd>When specified, the session ID is saved on login so subsequent commands will not need to log in. Use the no- prefix to not save the session ID. By default, the session is saved.</dd>

<dt>--timeout</dt>

<dd>Waits the specified number of seconds for the server to complete processing the command. By default, the process will wait until the server responds.</dd>

<dt>--</dt>

<dd>Specifies the end of options on the command line. You can use -- to indicate to tabcmd that anything that follows -- should not be interpreted as an option setting and can instead be interpreted as a value for the command. This is useful if you need to specify a value in the command that includes a hyphen. The following example shows how you might use -- in a tabcmd command, where -430105/Sheet1 is a required value for the export command.

```tabcmd export --csv -f "D:\export10.csv" -- -430105/Sheet1```
</dd>

</dl>
</details>


# login
Logs in a Tableau Online user.

Use the --server, --site, --username, --password global options to create a session.

Note: When you use the tabcmd login command, you cannot use SAML single sign-on (SSO), even if your site is configured to use SAML. To log in, you must pass the user name and password of a user who has been created in your site. You will have the permissions of the Tableau Server user that you're signed in as.

If you want to log in using the same information you've already used to create a session, just specify the --password option. The server and user name stored in the cookie will be used.

If the server is using a port other than 80 (the default), you will need to specify the port.

You need the --site (-t) option only if the server is running multiple sites and you are logging in to a site other than the Default site. If you do not provide a password you will be prompted for one. If the --no-prompt option is specified and no password is provided the command will fail.

Once you log in, the session will continue until it expires on the server or the logout command is run.

## Example

Log in to the Tableau Online site with the specified site ID:

`tabcmd login -s https://online.tableau.com -t siteID -u user@email.com -p password`

## Options
<dl>
<dt>-s, --server</dt>

<dd>If you are running the command from a Tableau Server computer that’s on your network, you can use http://localhost. Otherwise, specify the computer's URL, such as http://bigbox.myco.com or http://bigbox.

If the server is using SSL, you will need to specify https:// in the computer's URL.

For Tableau Online, specify the URL https://online.tableau.com.</dd>

<dt>-t, --site</dt>

<dd>Include this option if the server has multiple sites, and you are logging in to a site other than the default site.

The site ID is used in the URL to uniquely identify the site. For example, a site named West Coast Sales might have a site ID of west-coast-sales.</dd>

<dt>-u, --username</dt>

<dd>The user name of the user logging in. For Tableau Online, the user name is the user's email address.</dd>

<dt>-p, --password</dt>

<dd>Password for the user specified for --username. If you do not provide a password you will be prompted for one.</dd>

<dt>--password-file</dt>

<dd>Allows the password to be stored in the given filename.txt file rather than the command line, for increased security.</dd>

<dt>-x, --proxy</dt>

<dd>Use to specify the HTTP proxy server and port (Host:Port) for the tabcmd request.</dd>

<dt>--no-prompt</dt>

<dd>Do not prompt for a password. If no password is specified, the login command will fail.</dd>

<dt>--cookie</dt>

<dd>Saves the session ID on login. Subsequent commands will not require a login. This value is the default for the command.</dd>

<dt>--no-cookie</dt>

<dd>Do not save the session ID information after a successful login. Subsequent commands will require a login.</dd>

<dt>--timeout SECONDS</dt>

<dd>The number of seconds the server should wait before processing the login command. Default: 30 seconds.</dd>
</dl>

<details><summary>Global options</summary>

The following options are used by all tabcmd commands. The `--server`, `--user`, and `--password` options are required at least once to begin a session. An authentication token is stored so subsequent commands can be run without including these options. This token remains valid for five minutes after the last command that used it.
<dl>
<dt>-h, --help</dt>

<dd>Displays the help for the command.

Note: Some commands listed may not apply when using tabcmd with Tableau Online.</dd>

<dt>-s, --server</dt>

<dd>The Tableau Online URL, which is required at least once to begin session.</dd>

<dt>-u, --user</dt>

<dd>The Tableau Online username, which is required at least once to begin session.</dd>

<dt>-p, --password</dt>

<dd>The Tableau Online password, which is required at least once to begin session.</dd>

<dt>--password-file</dd>

<dd>Allows the password to be stored in the given .txt file rather than the command line for increased security.</dd>

<dt>-t, --site</dt>

<dd>Indicates that the command applies to the site specified by the Tableau Online site ID, surrounded by single quotes or double quotes. Use this option if the user specified is associated with more than one site. Site ID is case-sensitive when using a cached authentication token. If you do not match case you may be prompted for a password even if the token is still valid.</dd>

<dt>--no-prompt</dt>

<dd>When specified, the command will not prompt for a password. If no valid password is provided the command will fail.</dd>

<dt>--[no-]cookie</dt>

<dd>When specified, the session ID is saved on login so subsequent commands will not need to log in. Use the no- prefix to not save the session ID. By default, the session is saved.</dd>

<dt>--timeout</dt>

<dd>Waits the specified number of seconds for the server to complete processing the command. By default, the process will wait until the server responds.</dd>

<dt>--</dt>

<dd>Specifies the end of options on the command line. You can use -- to indicate to tabcmd that anything that follows -- should not be interpreted as an option setting and can instead be interpreted as a value for the command. This is useful if you need to specify a value in the command that includes a hyphen. The following example shows how you might use -- in a tabcmd command, where -430105/Sheet1 is a required value for the export command.

```tabcmd export --csv -f "D:\export10.csv" -- -430105/Sheet1```
</dd>

</dl>
</details>


# logout
Logs out of the server.

## Example

```tabcmd logout```

# publish *filename.twb(x)*, *filename.tds(x)*, or *filename.hyper*
Publishes the specified workbook (.twb(x)), data source (.tds(x)), or extract (.hyper) to Tableau Online.

If you are publishing a workbook, by default, all sheets in the workbook are published without database user names or passwords.

The permissions initially assigned to the workbook or data source are copied from the project that the file is published to. Permissions for the published resource can be changed after the file has been published.

If the workbook contains user filters, one of the thumbnail options must be specified.

## Example

`tabcmd publish "analysis_sfdc.hyper" -n "Sales Analysis"
--oauth-username "user-name" --save-oauth`

If the file is not in the same directory as tabcmd, include the full path to the file.

# Example

`tabcmd publish "\\computer\volume\Tableau Workbooks\analysis_sfdc.hyper" -n "Sales Analysis" --oauth-username "username" --save-oauth`

# Options
<dl>
<dt>-n, --name<dt>

<dd>Name of the workbook or data source on the server. If omitted, the workbook, data source, or data extract will be named after filename.</dd>

<dt>-o, --overwrite</dt>

<dd>Overwrites the workbook, data source, or data extract if it already exists on the server.</dd>

<dt>-r, --project</dt>

<dd>Publishes the workbook, data source, or data extract into the specified project. Publishes to the “Default” project if not specified.</dd>

<dt>--parent-project-path</dt>

<dd>Specifies the name of the parent project for the nested project as specified with the -r option. For example, to specify a project called "Nested" that exists in a "Main" project, use the following syntax: --parent-project-path "Main" -r "Nested".</dd>

<dt>--db-username</dt>

<dd>Use this option to publish a database user name with the workbook, data source, or data extract.

If you connect to the data through a protected OAuth connection and access token, us the --oauth-username option instead.</dd>

<dt>--db-password</dt>

<dd>Use this option to publish a database password with the workbook, data source, or extract.</dd>

<dt>--save-db-password</dt>

<dd>Stores the provided database password on the server.</dd>

<dt>--oauth-username</dt>

<dd>The email address of the user account. Connects the user through a preconfigured OAuth connection, if the user already has a saved access token for the cloud data source specified in --name. Access tokens are managed in user preferences.

For existing OAuth connections to the data source, use this option instead of --db-username and --db-password.</dd>

<dt>--save-oauth</dt>

<dd>Saves the credential specified by --oauth-username as an embedded credential with the published workbook or data source.

Subsequently, when the publisher or server administrator signs in to the server and edits the connection for that workbook or data source, the connection settings will show this OAuth credential as embedded in the content.

If you want to schedule extract refreshes after publishing, you must include this option with --oauth-username. This is analogous to using --save-db-password with a traditional database connection.</dd>

<dt>--thumbnail-username</dt>

<dd>If the workbook contains user filters, the thumbnails will be generated based on what the specified user can see. Cannot be specified when --thumbnail-group option is set.</dd>

<dt>--thumbnail-group</dt>

<dd>If the workbook contains user filters, the thumbnails will be generated based on what the specified group can see. Cannot be specified when --thumbnail-usernameoption is set.</dd>

<dt>--tabbed</dt>

<dd>When a workbook with tabbed views is published, each sheet becomes a tab that viewers can use to navigate through the workbook. Note that this setting will override any sheet-level security.</dd>

<dt>--append</dt>

<dd>Append the extract file to the existing data source.</dd>

<dt>--replace</dt>

<dd>Use the extract file to replace the existing data source.</dd>

<dt>--disable-uploader</dt>

<dd>Disable the incremental file uploader.</dd>

<dt>--restart</dd>

<dd>Restart the file upload.</dd>
</dl>

<details><summary>Global options</summary>

The following options are used by all tabcmd commands. The `--server`, `--user`, and `--password` options are required at least once to begin a session. An authentication token is stored so subsequent commands can be run without including these options. This token remains valid for five minutes after the last command that used it.
<dl>
<dt>-h, --help</dt>

<dd>Displays the help for the command.

Note: Some commands listed may not apply when using tabcmd with Tableau Online.</dd>

<dt>-s, --server</dt>

<dd>The Tableau Online URL, which is required at least once to begin session.</dd>

<dt>-u, --user</dt>

<dd>The Tableau Online username, which is required at least once to begin session.</dd>

<dt>-p, --password</dt>

<dd>The Tableau Online password, which is required at least once to begin session.</dd>

<dt>--password-file</dd>

<dd>Allows the password to be stored in the given .txt file rather than the command line for increased security.</dd>

<dt>-t, --site</dt>

<dd>Indicates that the command applies to the site specified by the Tableau Online site ID, surrounded by single quotes or double quotes. Use this option if the user specified is associated with more than one site. Site ID is case-sensitive when using a cached authentication token. If you do not match case you may be prompted for a password even if the token is still valid.</dd>

<dt>--no-prompt</dt>

<dd>When specified, the command will not prompt for a password. If no valid password is provided the command will fail.</dd>

<dt>--[no-]cookie</dt>

<dd>When specified, the session ID is saved on login so subsequent commands will not need to log in. Use the no- prefix to not save the session ID. By default, the session is saved.</dd>

<dt>--timeout</dt>

<dd>Waits the specified number of seconds for the server to complete processing the command. By default, the process will wait until the server responds.</dd>

<dt>--</dt>

<dd>Specifies the end of options on the command line. You can use -- to indicate to tabcmd that anything that follows -- should not be interpreted as an option setting and can instead be interpreted as a value for the command. This is useful if you need to specify a value in the command that includes a hyphen. The following example shows how you might use -- in a tabcmd command, where -430105/Sheet1 is a required value for the export command.

```tabcmd export --csv -f "D:\export10.csv" -- -430105/Sheet1```
</dd>

</dl>
</details>

# refreshextracts *workbook-name* or *datasource-name*
Performs a full or incremental refresh of extracts belonging to the specified workbook or data source.

This command takes the name of the workbook or data source as it appears on the server, not the file name when it was published. Only an administrator or the owner of the workbook or data source is allowed to perform this operation.

>Notes:
* This method will fail and result in an error if your Server Administrator has disabled the RunNow setting for the site. For more information, see Tableau Server Settings(Link opens in a new window).
* You can use tabcmd to refresh supported data sources that are hosted in the cloud. For example, SQL Server, MySQL, PostgreSQL on a cloud platform; Google Analytics; and so on.
* To refresh on-premises data with tabcmd, the data source must be a type that can be configured for Tableau Bridge Recommended schedules. For all other data sources that connect to on-premises data, you can use Bridge or the command-line data extract utility. Learn more at Use Bridge to Keep Data Fresh and Automate Extract Refresh Tasks from the Command Line.

## Examples

`tabcmd refreshextracts --datasource sales_ds`

`tabcmd refreshextracts --project "Sales External" --datasource sales_ds`

`tabcmd refreshextracts --project "Sales External" --parent-project-path "Main" --project "Sales External" --datasource sales_ds`

`tabcmd refreshextracts --workbook "My Workbook"`

`tabcmd refreshextracts --url SalesAnalysis
tabcmd refreshextracts --workbook "My Workbook" --addcalculations`

`tabcmd refreshextracts --datasource sales_ds --removecalculations`

## Options
<dl>
<dt>--incremental</dt>

<dd>Runs the incremental refresh operation.</dd>

<dt>--synchronous</dt>

<dd>Adds the full refresh operation to the queue used by the Backgrounder process, to be run as soon as a Backgrounder process is available. If a Backgrounder process is available, the operation is run immediately. The refresh operation appears on the Background Tasks report.

During a synchronous refresh, tabcmd maintains a live connection to the server while the refresh operation is underway, polling every second until the background job is done.</dd>

<dt>--workbook</dt>

<dd>The name of the workbook containing extracts to refresh. If the workbook has spaces in its name, enclose it in quotes.</dd>

<dt>--datasource</dt>

<dd>The name of the data source containing extracts to refresh.<dd>

<dt>--project</dt>

<dd>Use with --workbook or --datasource to identify a workbook or data source in a project other than Default. If not specified, the Default project is assumed.</dd>

<dt>--parent-project-path</dt>

<dd>Specifies the name of the parent project for the nested project as specified with the --project option.

For example:

* To specify a project called "Nested" that exists in a "Main" project, use the following syntax:
`--parent-project-path "Main" --project "Nested"`
* To specify a project called "Nested2" that is nested within the "Nested" project:
`--parent-project-path "Main/Nested" --project "Nested2"`
</dd>

<dt>--url</dt>

<dd>The name of the workbook as it appears in the URL. A workbook published as “Sales Analysis” has a URL name of “SalesAnalysis”.</dd>

<dt>--addcalculations</dt>

<dd>Use with --workbook to materialize calculations in the embedded extract of the workbook or --datasource to materialize calculations in the extract data source. Adds the operation to the queue used by the Backgrounder process. If a Backgrounder process is available, the operation runs immediately. This operation appears on the Background Tasks for Extracts administrative view.</dd>

<dt>--removecalculations</dt>

<dd>Use with --workbook or --datasource to remove calculations that were previously materialized. Adds the operation to the queue used by the Backgrounder process. If a Backgrounder process is available, the operation runs immediately. This operation appears on the Background Tasks for Extracts administrative view.</dd>
</dl>

<details><summary>Global options</summary>

The following options are used by all tabcmd commands. The `--server`, `--user`, and `--password` options are required at least once to begin a session. An authentication token is stored so subsequent commands can be run without including these options. This token remains valid for five minutes after the last command that used it.
<dl>
<dt>-h, --help</dt>

<dd>Displays the help for the command.

Note: Some commands listed may not apply when using tabcmd with Tableau Online.</dd>

<dt>-s, --server</dt>

<dd>The Tableau Online URL, which is required at least once to begin session.</dd>

<dt>-u, --user</dt>

<dd>The Tableau Online username, which is required at least once to begin session.</dd>

<dt>-p, --password</dt>

<dd>The Tableau Online password, which is required at least once to begin session.</dd>

<dt>--password-file</dd>

<dd>Allows the password to be stored in the given .txt file rather than the command line for increased security.</dd>

<dt>-t, --site</dt>

<dd>Indicates that the command applies to the site specified by the Tableau Online site ID, surrounded by single quotes or double quotes. Use this option if the user specified is associated with more than one site. Site ID is case-sensitive when using a cached authentication token. If you do not match case you may be prompted for a password even if the token is still valid.</dd>

<dt>--no-prompt</dt>

<dd>When specified, the command will not prompt for a password. If no valid password is provided the command will fail.</dd>

<dt>--[no-]cookie</dt>

<dd>When specified, the session ID is saved on login so subsequent commands will not need to log in. Use the no- prefix to not save the session ID. By default, the session is saved.</dd>

<dt>--timeout</dt>

<dd>Waits the specified number of seconds for the server to complete processing the command. By default, the process will wait until the server responds.</dd>

<dt>--</dt>

<dd>Specifies the end of options on the command line. You can use -- to indicate to tabcmd that anything that follows -- should not be interpreted as an option setting and can instead be interpreted as a value for the command. This is useful if you need to specify a value in the command that includes a hyphen. The following example shows how you might use -- in a tabcmd command, where -430105/Sheet1 is a required value for the export command.

```tabcmd export --csv -f "D:\export10.csv" -- -430105/Sheet1```
</dd>

</dl>
</details>

# removeusers *group-name*
Removes users from the specified group.

## Example

`tabcmd removeusers "Development" --users "users.csv"`

## Options
<dl>

<dt>--users</dt>

<dd>Remove the users in the given .csv file from the specified group. The file should be a simple list with one user name per line.</dd>

<dt>--[no-]complete</dt>

<dd>Requires that all rows be valid for any change to succeed. If not specified --complete is used.</dd>
</dl>

<details><summary>Global options</summary>

The following options are used by all tabcmd commands. The `--server`, `--user`, and `--password` options are required at least once to begin a session. An authentication token is stored so subsequent commands can be run without including these options. This token remains valid for five minutes after the last command that used it.
<dl>
<dt>-h, --help</dt>

<dd>Displays the help for the command.

Note: Some commands listed may not apply when using tabcmd with Tableau Online.</dd>

<dt>-s, --server</dt>

<dd>The Tableau Online URL, which is required at least once to begin session.</dd>

<dt>-u, --user</dt>

<dd>The Tableau Online username, which is required at least once to begin session.</dd>

<dt>-p, --password</dt>

<dd>The Tableau Online password, which is required at least once to begin session.</dd>

<dt>--password-file</dd>

<dd>Allows the password to be stored in the given .txt file rather than the command line for increased security.</dd>

<dt>-t, --site</dt>

<dd>Indicates that the command applies to the site specified by the Tableau Online site ID, surrounded by single quotes or double quotes. Use this option if the user specified is associated with more than one site. Site ID is case-sensitive when using a cached authentication token. If you do not match case you may be prompted for a password even if the token is still valid.</dd>

<dt>--no-prompt</dt>

<dd>When specified, the command will not prompt for a password. If no valid password is provided the command will fail.</dd>

<dt>--[no-]cookie</dt>

<dd>When specified, the session ID is saved on login so subsequent commands will not need to log in. Use the no- prefix to not save the session ID. By default, the session is saved.</dd>

<dt>--timeout</dt>

<dd>Waits the specified number of seconds for the server to complete processing the command. By default, the process will wait until the server responds.</dd>

<dt>--</dt>

<dd>Specifies the end of options on the command line. You can use -- to indicate to tabcmd that anything that follows -- should not be interpreted as an option setting and can instead be interpreted as a value for the command. This is useful if you need to specify a value in the command that includes a hyphen. The following example shows how you might use -- in a tabcmd command, where -430105/Sheet1 is a required value for the export command.

```tabcmd export --csv -f "D:\export10.csv" -- -430105/Sheet1```
</dd>

</dl>
</details>

# runschedule *schedule-name*
Runs the specified schedule.

This command takes the name of the schedule as it is on the server.

This command is not available for Tableau Online.

Note: This method will fail and result in an error if your Server Administrator has disabled the RunNow setting for the site. For more information, see Tableau Server Settings(Link opens in a new window).

# Example

```tabcmd runschedule "5AM Sales Refresh"```

<details><summary>Global options</summary>

The following options are used by all tabcmd commands. The `--server`, `--user`, and `--password` options are required at least once to begin a session. An authentication token is stored so subsequent commands can be run without including these options. This token remains valid for five minutes after the last command that used it.
<dl>
<dt>-h, --help</dt>

<dd>Displays the help for the command.

Note: Some commands listed may not apply when using tabcmd with Tableau Online.</dd>

<dt>-s, --server</dt>

<dd>The Tableau Online URL, which is required at least once to begin session.</dd>

<dt>-u, --user</dt>

<dd>The Tableau Online username, which is required at least once to begin session.</dd>

<dt>-p, --password</dt>

<dd>The Tableau Online password, which is required at least once to begin session.</dd>

<dt>--password-file</dd>

<dd>Allows the password to be stored in the given .txt file rather than the command line for increased security.</dd>

<dt>-t, --site</dt>

<dd>Indicates that the command applies to the site specified by the Tableau Online site ID, surrounded by single quotes or double quotes. Use this option if the user specified is associated with more than one site. Site ID is case-sensitive when using a cached authentication token. If you do not match case you may be prompted for a password even if the token is still valid.</dd>

<dt>--no-prompt</dt>

<dd>When specified, the command will not prompt for a password. If no valid password is provided the command will fail.</dd>

<dt>--[no-]cookie</dt>

<dd>When specified, the session ID is saved on login so subsequent commands will not need to log in. Use the no- prefix to not save the session ID. By default, the session is saved.</dd>

<dt>--timeout</dt>

<dd>Waits the specified number of seconds for the server to complete processing the command. By default, the process will wait until the server responds.</dd>

<dt>--</dt>

<dd>Specifies the end of options on the command line. You can use -- to indicate to tabcmd that anything that follows -- should not be interpreted as an option setting and can instead be interpreted as a value for the command. This is useful if you need to specify a value in the command that includes a hyphen. The following example shows how you might use -- in a tabcmd command, where -430105/Sheet1 is a required value for the export command.

```tabcmd export --csv -f "D:\export10.csv" -- -430105/Sheet1```
</dd>

</dl>
</details>
