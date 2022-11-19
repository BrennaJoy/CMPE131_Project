
## Functional Requirements
=======
1. Login -- Koe
2. Logout -- Wilson
3. Create New Account -- Brenna
4. Delete Account -- Timothy 
5. User Home Page (w/messages of users they follow) -- Koe w/Use Case
6. Send message to followers -- Wilson w/Use Case
7. Follow User -- Koe w/Use Case
8. Search for User -- Brenna w/Use Case
9. User Profile -- Wilson w/Use Case
10. Send/Receive Messages -- Timothy w/Use Case
11. Post Reactions (?) -- Timothy
12. *Post Image with Message -- Brenna

## Non-functional Requirements
=======
1. Works on Chrome
2. Mobile/Desktop
3. Localization -- Language Support
4. Can support 3 simultaneous users

## Use Cases
=======

1. Use case name: Send message to followers

Pre condition: must have followers and the user must be logged in

Triggers: Users must click on the message symbol

Primary sequence:
The user click on the “post message” box
The user types the message
The user press enter or click “post
The system shows the message on the homepage

Primary postconditions: Users and the followers are able to see the message or status

Alternate sequence: the user only type punctuations
The user click on the “post message” box
The user types only puncutations on the message
The system will show a warning message “the message should contains at least one alphabet or number”
The user retype the message
The user press enter or click “post
The system shows the message on the homepage

2. Use case name: Edit user profile

Pre condition: the user must have an account and logged in

Triggers:
The user click on the profile box and click edit
The user will go to settings and find edit profile

Primary sequence:
The user click on the edit profile picture
The user change the profile picture or delete the profile picture
The user click “finish edit”
The user click on the edit bio
The user types text on bio
The user click “finish edit”
The system will show the edited profile picture and bio

Primary postconditions: the user can update the profile picture and/or bio

Alternate sequence: the picture size is too big
The user click on the edit profile picture
The user change the profile picture
The system will show a warning message “the image size is bigger than 10 MB”
The user select another picture

3. Use Case Name: Search for User

Pre-condition: Must have users, actor must be logged in

Trigger: User clicks on the "Find a User" box and types in a username.

Primary Postconditions: User is able to view other users and go to their profiles. 

Alternate Sequence: The user types in an illegal character.
  
  1. User clicks on the search textbox.
  2. User types in the name to search. 
  3. User clicks the search/enter button.
  4. A message appears informing the user that they entered an invalid character. 
  5. The user is given the opportunity to enter a valid username.

Alternate Sequence: The user types in a name that doesn't exist. 
  
  1. User clicks on the search textbox.
  2. User types in the name to search. 
  3. User clicks the search/enter button.
  4. A message appears informing the user that they entered a username that doesn't exist. 
  5. The user is given the opportunity to enter a valid username.
  
4. Use Case Name: User Home Page (w/messages of users they follow)

Pre-condition: User must have account and must be logged in 

Trigger: User clicks on login 

Primary Sequence:
 
  1. User clicks on username textbox
  2. User types username
  3. User clicks on password textbox
  4. User types password
  5. User click on login
  6. User will be taken to his/her homepage

Primary Postconditions: User is able to view his/her homepage with the messages that user follows
   
5. Use Case Name: Follow User
   
Pre-condition: User must have account and must be logged in 

Trigger: User clicks on "Follow" box

Primary Sequence:
  
  1. User clicks on search box 
  2. User types in the name to search
  3. User clicks on search or enter button
  4. The system shows possible usernames 
  5. User clicks on the username that he/she wants to follow
  6. User clicks "Follow" box

Primary Postconditions: User can see other users' profiles 

  1. User clicks on the search textbox.
  2. User types in the name to search. 
  3. User clicks the search/enter button.
  4. System searches through the userbase
  5. System shows the possible usernames.
  6. The user clicks on the profile they would like to see.
  7.The user is taken to the aforementioned profile.

6. Use Case Name: Send/Receive Messages

Pre-condition: The user has logged into the website.

Trigger: The user selected another user to send messages to.

Primary Sequence:
  
  1. The system opens a chat box for both the sender and receiver.
  2. The system prompts the user to enter a message. 
  3. The user can create a message and send it.
  4. The system displays the message along with the namer of the sender and timestamp in the chat box. 

Primary Postconditions: The message is displayed for both users to see.

Alternate Sequence: The user tries to message a deleted account.
  
  1. The system displays an error message to the user.
  2. The private messaging chat box for the user is closed.
