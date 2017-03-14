Done - MESSAGING: ID of match is sent to de show view (-1 if you are trying to see your profile). A set of comments (posts) is created for that match. This comments can only be made and view by the 2 people that matched.
All the comments will have the id of the match. (there are 2 matches between two people so there is a special case in the controller)
Done - Messages opened implementation
Done - Ordered matches by percentage
Done - Notification when you have new messages from a match (text on top of profiles page)
Done - Update location when call reloaded
Done - Update city 

Added checking profile completion.
Now if the user doesn't fill one of the the parts of the profile they will get redirected to that page when trying to see their matches.
Added some checking in case one of the users doesn't provide their location (if its a random user the auth.user.id will not try to match with them, without getting any error) if the user logged in is the one witouth a location it will display a message and will try to update their location (So they have to accept the sharing location thing)

UPDATED 3/14/17
Fixed new message notification
Added titles and favion.ico to the views
Solved some errors
Fixed update profile page

UPDATED 3/11/17 BY VINCENT:

DONE - all the extra photos for the buttons
DONE - extended layout to 3 missing pages
DONE - added BIO for the dog and for the user; displays on profile page
DONE - added back button to pages that were missing it
DONE - fixed a minor bug when there was no extra photos for profiles



