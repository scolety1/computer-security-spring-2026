---
title: Dissecting a Web App
---

# Getting Started

Grab the project folder and follow the `README.md` to get up and running.

# Tasks

## Find all the paths/resources supported by the server

Review the server code to identify the resources a client can access.

## Reversing an end-to-end workflow

Please map out all the UI actions/updates, network requests, HTTP traffic, executed code paths on server, and database or file accesses for a single interaction with the app.

Use whatever tools you would like to collect this information. Please select from

For example, what happens when we view the main page?

### Example

Client: Requests `GET /`
Server: `auth.py#load_logged_in_user()` is called
Server: `blog.py#index()` is called
Server: Runs SQL query to get all posts from the `post` table
Server: Opens `blog/index.html` template file
Server: Responds with `200` and rendered template in body
Client: Displays response body

## Authentication

How does the server know whether we provided correct credentials? How does it know we've logged in after we provide correct credentials?

## Surprises

Did anything in the web app surprise you? If so, what?

## Attack surface surveying

- What actions in the app accept user input?
- Which actions result in accessing the database or a file? Is it a read or a write?
- Which actions require being logged in?
- When is user input included as output?
