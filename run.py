import numpy as np
import scipy.signal
from scipy.io import wavfile
import matplotlib.pyplot as plt

class NOAA:
	def __init__(self, filename, norm):
		#extract the data from WAV file
		self.sampling_rate, self.data = wavfile.read(filename)

		#normalization value which will be later used to bring the amplitudes to be in 0 to 255 range
		self.norm = norm
		self.am_envelope = self.hilbert(self.data)

	def hilbert(self, data):
		#hilbert transfrom will give us an analytical signal
		#this will help us extract the envelopes instantaneously
		#for more info visit the following link
		#https://dsp.stackexchange.com/questions/25845/meaning-of-hilbert-transform

	    #find the analytical signal
	    analytic_signal = scipy.signal.hilbert(data)
	    
	    #extract the amplitude envelope
	    am_envelope = np.abs(analytic_signal)
	    
	    return am_envelope

	def getImageArray(self, am_envelope, norm):
		print("Processing image...")

		#calculate the width and height of the image
		width = int(self.sampling_rate*0.5)
		height = self.am_envelope.shape[0]//width
		print(f"width: {width}, height: {height}")
		
		#create a numpy array with three channels for RGB and fill it up with zeroes
		img_data = np.zeros((height, width, 3), dtype=np.uint8)

		#keep track of pixel values
		x = 0
		y = 0

		#traverse through the am_envelope and replace zeroes in numpy array with intensity values
		for i in range(self.am_envelope.shape[0]):

		    #get the pixel intensity
		    intensity = int(self.am_envelope[i]//norm)

		    #make sure that the pixel intensity is between 0 and 255
		    if intensity < 0:
		        intensity = 0
		    if intensity > 255:
		        intensity = 255

		    #put the pixel on to the image
		    img_data[y][x] = intensity

		    x += 1

		    #if x is greater than width, sweep or jump to next line
		    if x >= width:
		        x = 0
		        y = y+1

		        if y >= height:
		            break

		print("Image processed.")

		return img_data

	def plot(self):
		#get the image data as numpy array
		img_data = self.getImageArray(self.am_envelope, self.norm)

		#plot the numpy array as an image
		print("Plotting the image")
		plt.imshow(img_data, aspect="auto")
		plt.show()




filename = input("Enter the WAV file name: ")
norm = int(input("Enter the normalization (50 to 70 would be good): "))

#create an instance of NOAA object
decoder = NOAA(filename, norm)
decoder.plot()
