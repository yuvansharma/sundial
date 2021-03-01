# sundial

20 May 2020

Calculations for 3D Printed Sundial

As part of the video challenge, I designed a 3D printed sundial. This code was taken from the web. It produces a CAD model of a 3D printable sundial. But I didn't have any 3D printer, so I found a workaround.

Blender allows 3D models to be imported. I found a way to take sundial's 3D model and import in Blender. I used a light source as the Sun. By putting Sun at the correct angle depending on time of day, I could change the direction of light passing through the sundial's holes and hence the shadow. Thus, by recording the video animation of the Sun moving and the sundial's shadow changing, I was able to prove the Sundial works. 

For calculating position of Sun, I used a proper NASA calculation of the Sun's position as a function of latitude/longitude and year on Earth. So if I put the right numbers, I can calculate exact shadow anywhere on Earth at any day in future and in past also. 

Great way of testing the expected shadow of the Sundial. That way, I was able to save the cost of a 3D printing of the Sundial. 

Acknowledgments:
1. The Digital Sundial original CAD STL file is from Mojoptix on Thingiverse. See https://www.thingiverse.com/thing:1068443
2. For Sun angle calculations, I found a nice library called pysolar. That way, I only had to find my home's local latitude/longitude. See https://pysolar.readthedocs.io/ 
