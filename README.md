# Perspective-transformation-Country-Flag-Pattern-
My approach during this assignment:
1. Understood perspective transformation and some of the other functions used for this in CV2 and so some tutorials where these are used.
2. I broke this down into 3 steps and solved it:
* Get the necessary coordinates
* Creating the Homography matrix
* wrapping and getting the resultant image
3. Then debugged some challenges which I have explained it in Error Handling


A few errors which I faced along the way and how I handled it:
1. The image of the pattern was inverted after being projected.
Solution: I just had to change the order of the coordinates
2. The RGB color were not applied and so it looked more like a Blue and white flag
Solution: Just use the function along with the RGB coloring
3. The image was very dull. It showed some coloring but was dull with its background.
Solution: After some digging around on the internet and some Q and A with Gemini(LLM), I understood that the problem here was due to the lack of isolation of the foreground from the background which was due to the Addweight parameter. So I used greymasking and bitwise operations to provide isolation.
