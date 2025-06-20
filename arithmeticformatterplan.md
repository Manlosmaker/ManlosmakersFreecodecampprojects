A list of strings are recieved that are arithmetical problems
they then need to be converted in the format of problems arranged vertically and side by side by side. The function takse a second argument that then solves the problems
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.
Errors if 
too many problems supplied
Error operatores
Error numbers must only contain digits
Numbesr cannot be more then 4 digirts

Single space between operator and the longhest of the two operands
THe opeartor is on the second line
Numbers are right-aligned 
Four spaces between each problems
dashes at the bottom of each problems


#Stage one
Split the string(s) into a smaller list
Check for errors
Put everything in right aligned
d returns the problems arranged vertically and side-by-side