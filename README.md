# Automatic picture transmission(APT) decoder

Automatic picture transmission protocol is used by NOAA satellites. They constantly send a frequency modulated signal at 137 to 138 MHz.
Demodulating this FM wave will give an output of audio signal with a frequency of 2400 Hz. This is also known as amplitude modulated subcarrier wave. NOAA satellite sends 120 lines per minute or 1 line per 500 milliseconds. From this AM subcarrier wave, we can extract the amplitudes for 500 milliseconds and normalize them to be in between 0 and 255.

These values can be stored in NumPy array and can be plotted as an image.

Here's an example image:
![example image](https://github.com/jch15/APT-Decoder/blob/main/noaa1.png)


![example image 2](https://github.com/jch15/APT-Decoder/blob/main/noaa2.png)

# How to run?
Make sure that you install `numpy`, `scipy`, `matplotlib` using the following commands

`pip install numpy`

`pip install scipy`

`pip install matplotlib`

Once they are installed, run the program using `python run.py`, it will ask for the WAV file and normalization values. Enter them and it will show you the image as a plot.

I've included `noaa1.wav` file, you can use it see the image sent by the satellite.

NOTE: This script does not use sync bits and hence the images look bent. ~~I was lazy~~(honestly, don't know how to decode sync bits from the signal) ~~to implement that.~~ Feel free to contribute.

# References
https://noaasis.noaa.gov/NOAASIS/pubs/Users_Guide-Building_Receive_Stations_March_2009.pdf

https://en.wikipedia.org/wiki/Automatic_picture_transmission
