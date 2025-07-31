# Geometry functions rewrite

Rewrote common geometry functions and compared them to Shapely

## What I Did
- Implemented the following functions
    - Distance between 2 points
    - Check if a point is inside a AABB
    - Check if 2 AABBs overlap
    - Check if a point is inside a polygon (first AABB check, then raycast check)
- Wrote unit tests to see if the results match Shapely
- Did a rough time estimate between the same tests using Shapely
	

## Notes from Tests
I used Powershell Measure-Command to time the tests. All I did was time each library 15 times, and the manual functions in average ran 121 milliseconds faster than the Shapely functions. This is by no means a professional benchmark.

This difference could be based on the fact that shapely does way more input checks and validations then my library. It must also be better dealing with floating point imprecision and I must be using full fledged objects with a more structured class system, whereas mine only uses simple dataclasses. Also I didn't implement ring polygon check, and shapely does.

## Tools
- Python
- Shapely
