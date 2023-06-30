# Project Description: Wiki

This project involves the implementation of a Wiki encyclopedia, with the following requirements:

Video demo: https://www.youtube.com/watch?v=6ElbJxQ5JFQ

## Entry Page

- Visiting `/wiki/TITLE`, where `TITLE` is the title of an encyclopedia entry, should render a page displaying the contents of that encyclopedia entry.
- The view retrieves the content of the encyclopedia entry by calling the appropriate utility function.
- If the requested entry does not exist, the user is presented with an error page indicating that the requested page was not found.
- If the entry exists, the user is presented with a page displaying the content of the entry. The title of the page includes the name of the entry.

## Index Page

- `index.html` should be updated to allow users to click on any entry name, which takes them directly to that entry's page.
- Instead of merely listing the names of all pages in the encyclopedia, the index page provides direct navigation to specific entries.

## Search

- Users can type a query into the search box in the sidebar to search for an encyclopedia entry.
- If the query matches the name of an encyclopedia entry, the user is redirected to that entry's page.
- If the query does not match the name of an encyclopedia entry, the user is taken to a search results page displaying a list of all encyclopedia entries that have the query as a substring. For example, if the search query is "ytho," then "Python" should appear in the search results.
- Clicking on any of the entry names on the search results page takes the user to that entry's page.

## New Page

- Clicking "Create New Page" in the sidebar takes the user to a page where they can create a new encyclopedia entry.
- Users can enter a title for the page and enter the Markdown content for the page in a textarea.
- Users can click a button to save their new page.
- When the page is saved, if an encyclopedia entry already exists with the provided title, the user is presented with an error message.
- Otherwise, the encyclopedia entry is saved to disk, and the user is taken to the new entry's page.

## Edit Page

- On each entry page, the user can click a link to be taken to a page where they can edit that entry's Markdown content in a textarea.
- The textarea is pre-populated with the existing Markdown content of the page.
- The user can click a button to save the changes made to the entry.
- Once the entry is saved, the user is redirected back to that entry's page.

## Random Page

- Clicking "Random Page" in the sidebar takes the user to a random encyclopedia entry.

## Markdown to HTML Conversion

- On each entry's page, any Markdown content in the entry file is converted to HTML before being displayed to the user.

## Note

CS50W project1: https://cs50.harvard.edu/web/2020/projects/1/wiki/
