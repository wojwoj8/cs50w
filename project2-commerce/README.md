# Project Description: Auction Site

This project involves the implementation of an auction site, with the following requirements:
Video demo: https://www.youtube.com/watch?v=yoRBGG9YLKA

## Models

- The application should have at least three additional models in addition to the User model: Auction Listings, Bids, and Comments.
- The fields and types of each model are determined by the developer, but they should include necessary information related to auction listings, bids, and comments.
- Additional models can be created as per the developer's requirements.

## Create Listing

- Users can visit a page to create a new listing.
- Users can specify a title for the listing, a text-based description, and the starting bid.
- Users can optionally provide a URL for an image and/or select a category (e.g., Fashion, Toys, Electronics, Home, etc.) for the listing.

## Active Listings Page

- The default route of the web application should display all currently active auction listings.
- For each active listing, the page should display at least the title, description, current price, and photo (if available).

## Listing Page

- Clicking on a listing should take users to a specific page for that listing.
- Users can view all details about the listing, including the current price.
- If a user is signed in, they can add the item to their "Watchlist." They can also remove the item if it's already on the watchlist.
- If a user is signed in, they can place a bid on the item. The bid must be equal to or higher than the starting bid and greater than any other bids placed. Otherwise, an error is displayed.
- If the user who created the listing is signed in, they can "close" the auction from the listing page. This action declares the highest bidder as the winner and makes the listing inactive.
- If a signed-in user has won an auction, the closed listing page should indicate so.
- Signed-in users can add comments to the listing page. All comments made on the listing should be displayed.

## Watchlist

- Signed-in users can visit a Watchlist page that displays all the listings they have added to their watchlist.
- Clicking on any listing should take the user to that listing's page.

## Categories

- Users can visit a page displaying a list of all listing categories.
- Clicking on a category name takes the user to a page displaying all active listings in that category.

## Django Admin Interface

- The site administrator can access the Django admin interface.
- The administrator can view, add, edit, and delete any listings, comments, and bids made on the site.

## Note

CS50W project2: https://cs50.harvard.edu/web/2020/projects/2/commerce/
