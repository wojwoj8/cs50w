# Project Description: Google Replica Website

This project is a replica of the Google search engine website, built to meet specific requirements outlined below.
Video demo: https://www.youtube.com/watch?v=vPbw84uQO1M

## Website Requirements

1. The website has three pages:

   - `index.html` for regular Google Search
   - `image.html` for Google Image Search
   - `advanced.html` for Google Advanced Search

2. The Google Search page (`index.html`) features links in the upper-right corner to navigate to Image Search and Advanced Search. Both the Image Search page (`image.html`) and the Advanced Search page (`advanced.html`) have a link in the upper-right corner to return to the Google Search page.

3. On the Google Search page (`index.html`), users can enter a query in the search bar, click the "Google Search" button, and get redirected to the Google search results for that query.

4. The search bar and the search button on the Google Search page should be centered with rounded corners, resembling Google's own aesthetics.

5. On the Google Image Search page (`image.html`), users can enter a query in the search bar, click the search button, and get redirected to the Google Image search results for that query.

6. The Google Advanced Search page (`advanced.html`) allows users to provide input for four search fields:

   - "all these words"
   - "this exact word or phrase"
   - "any of these words"
   - "none of these words"

   These options are stacked vertically, and all text fields are left-aligned, similar to Google's own Advanced Search page.

7. The "Advanced Search" button on the Advanced Search page should have a blue background with white text, consistent with Google's own CSS.

8. Clicking the "Advanced Search" button should redirect the user to the search results page for the given query.

9. The Google Search page (`index.html`) includes an "I'm Feeling Lucky" button. When clicked, this button takes the user directly to the first Google search result for the query, bypassing the normal results page.

10. A redirect notice may appear when using the "I'm Feeling Lucky" button. This is an expected consequence of a security feature implemented by Google.

11. The CSS used in the project closely resembles Google's own aesthetics, ensuring visual consistency with the original Google website.

## File Structure

The project consists of the following files:

- `index.html`: The main Google Search page.
- `image.html`: The Google Image Search page.
- `advanced.html`: The Google Advanced Search page.
- `style.css`: CSS file containing the styles for all the pages.
- `images/`: A directory containing any required images.

## Note

The project aims to replicate the functionality and design of Google's search engine website within the given requirements. It is CS50W project0: https://cs50.harvard.edu/web/2020/projects/0/search/
