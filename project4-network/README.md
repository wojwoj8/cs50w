# Project Description: Social Network

This project involves the implementation of a social network using Python, JavaScript, HTML, and CSS.

Video Demo: https://www.youtube.com/watch?v=cm6WkaRrBWc

The following requirements were fulfilled:

## New Post

- Users who are signed in should be able to write a new text-based post by filling in text into a text area and then clicking a button to submit the post.
- The "New Post" feature can be implemented as a separate page or as a text box at the top of the "All Posts" page.

## All Posts

- The "All Posts" link in the navigation bar should display a page where all posts from all users are shown, with the most recent posts displayed first.
- Each post should include the username of the poster, the post content, the date and time of the post, and the number of "likes" the post has.

## Profile Page

- Clicking on a username should load that user's profile page.
- The profile page should display the number of followers the user has and the number of people that the user follows.
- All posts made by the user should be displayed in reverse chronological order.
- For other users who are signed in, a "Follow" or "Unfollow" button should be displayed to allow the user to toggle whether they are following the current user's posts.
- Users should not be able to follow themselves.

## Following

- The "Following" link in the navigation bar should display a page where all posts made by users that the current user follows are shown.
- This page should behave similarly to the "All Posts" page but with a limited set of posts.
- This page should only be accessible to signed-in users.

## Pagination

- Posts should be displayed in pages of 10 posts each.
- If there are more than ten posts, a "Next" button should appear to navigate to the next page of posts (older posts).
- If not on the first page, a "Previous" button should appear to navigate to the previous page of posts.

## Edit Post

- Users should be able to edit their own posts by clicking an "Edit" button or link on the post.
- Clicking "Edit" should replace the post's content with a textarea where the user can edit the content.
- The user should be able to "Save" the edited post without requiring a reload of the entire page.
- Security measures should be implemented to prevent users from editing another user's posts.

## "Like" and "Unlike"

- Users should be able to toggle whether they "like" a post by clicking a button or link on the post.
- JavaScript should be used to asynchronously update the server's like count and update the displayed like count on the page without reloading the entire page.

## Note

CS50W project4: https://cs50.harvard.edu/web/2020/projects/4/network/
