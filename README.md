# Create Your Own Story App
##### Written by Brett Grentell
*Responsibilities*
This  app should load a story book from a text based file, then allow the user to choose their way through the story.  The user begins with the first passage, then the application should display a list of options for the user to select.  Upon the user selecting an option, the application should then display the next passage for that option.  The story ends when the user selects a passage which marks the end of the story.

*Coding Style*
- Variable names should be described in a comment at the point of declaration,
- Variable and method names should be in camel case, while constants should use underscores to separate words,
- Code groups should use the magic number 7+/-2 for readability,
- A for loop and try-error should start their own code group,
- If statements should start their own code group,
- Comments should describe not HOW the code works, but the WHAT and the WHY it does it that way,
- A comment on each method should be made at the beginning of the method, about what the method does and why,
- Some sidebar comments should be made to clarify code which is not immediately obvious,
- Doesn't use variable names for more than one purpose,
- Variables should be initialized when they are declared,
- 80 characters per line max.

*Features*
- The application will read the story book from a text file.  The passages from the file will be read into a global variable dictionary for storage.  If the file cannot be found, and error mechanism will display a message for the user, then end the program.
- The application will allow input and output to the user, looping through passages while the user selects a passage at each turn.  If the user selects an option that is out of the bounds of the available options presented, an error is displayed so that the user can select a valid option.
- The application will allow tbe user to save the walkthrough of the story to a file so that the user can view their created story.  The walkthrough will be saved via a method to a global variable. 

*Implementation Plan*
 - Implementation of reading and writing is implemented first:
   - Reading the passages into a dictionary object,
   - Implement serialization feature to translate a story path to a full story.
   - Then writing capabilities of the full story.
   - Error mechanisms are implemented for reading and write errors.
 - Story traversal is then implemented:
   - Looping through passages is implemented,
   - Options selectable by user is implemented,
   - Error mechanisms implemented (for invalid options),
   - Storage of reader's path is implemented.
 - Final serialization of story:
   - The story is then serialized by traversing the user's path through the story, combined with the passages dictionary,
   - The next thing to be implemented will be to save the whole story to a text file.

*References*
https://www.cs.cmu.edu/~pattis/15-1XX/15-200/lectures/style/index.html
