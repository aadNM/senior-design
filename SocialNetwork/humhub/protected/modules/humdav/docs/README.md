# HumDAV
HumHub module for external access to e.g. the contacts over the CardDAV protocol.

## Requirements
- Make sure HumHub URL Rewriting is enabled on your installation (https://docs.humhub.org/docs/admin/installation#pretty-urls)

## Access
- At least two address books are automatically created for each user.
- The URL is organized as follows:
  - All Users: **{domain}/humdav/remote/addressbooks/{username}/main/**
  - Following Users: **{domain}/humdav/remote/addressbooks/{username}/following/**
  - An address book for every Space: **{domain}/humdav/remote/addressbooks/{username}/space_{space_url_id}/**
- There are also (if enabled) the following address books:
  - Profile calendar: **{domain}/humdav/remote/calendars/{username}/personal/**
  - A callender for every Space: **{domain}/humdav/remote/calendars/{username}/space_{space_url_id}/**
  - Please note: You don't have to be a Space member to see the public calendar entries. But the calendars are also displayed only if at least one (for the user) visible entry exists.
- The registration is currently only secured via Basic Auth. Simply enter your HumHub username and password here.
- Later, better authentication methods are planned.