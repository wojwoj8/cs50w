# Project Description: Email Client

This project involves the implementation of a single-page email client using JavaScript, HTML, and CSS. The main file for implementation is `inbox.js`.

Video Demo: https://www.youtube.com/watch?v=cGNQbl4WS3o

## Requirements:

Using JavaScript, HTML, and CSS, complete the implementation of your single-page-app email client inside of `inbox.js`. The following requirements were fulfilled:

## Send Mail

- When a user submits the email composition form, add JavaScript code to actually send the email.
- A POST request should be made to `/emails`, passing values for recipients, subject, and body.
- After the email is sent, the user's sent mailbox should be loaded.

## Mailbox

- When a user visits their Inbox, Sent mailbox, or Archive, the appropriate mailbox should be loaded.
- A GET request should be made to `/emails/<mailbox>` to request the emails for the specified mailbox.
- Upon visiting a mailbox, the application should query the API for the latest emails in that mailbox.
- The name of the mailbox should appear at the top of the page.
- Each email should be rendered in its own box (`<div>` with a border), displaying the sender, subject line, and timestamp.
- Unread emails should have a white background, while read emails should have a gray background.

## View Email

- When a user clicks on an email, they should be taken to a view where they can see the content of that email.
- A GET request should be made to `/emails/<email_id>` to request the email.
- The application should display the email's sender, recipients, subject, timestamp, and body.
- An additional `<div>` should be added to `inbox.html` for displaying the email.
- The appropriate views should be hidden or shown when navigation options are clicked.
- After viewing an email, it should be marked as read by sending a PUT request to `/emails/<email_id>`.

## Archive and Unarchive

- Users should be able to archive and unarchive received emails.
- When viewing an Inbox email, a button should be presented to archive the email.
- When viewing an Archive email, a button should be presented to unarchive the email.
- This requirement doesn't apply to emails in the Sent mailbox.
- A PUT request should be sent to `/emails/<email_id>` to mark an email as archived or unarchived.
- After archiving or unarchiving an email, the user's inbox should be loaded.

## Reply

- Users should be able to reply to an email.
- When viewing an email, a "Reply" button should be presented to allow replying.
- Clicking the "Reply" button should take the user to the email composition form.
- The composition form should be pre-filled with the recipient field set to the sender of the original email.
- The subject line should be pre-filled with "Re: <"original subject>".
- The body of the email should be pre-filled with a line like "On Jan 1 2020, 12:00 AM foo@example.com wrote:" followed by the original text of the email.

## Note

CS50W project3: https://cs50.harvard.edu/web/2020/projects/3/mail/
