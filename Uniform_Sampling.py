#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib.pyplot as plt

from Random import Random
#################
# Uniform Sampling
#################

#This piece of code will try to simple sampling. We will sample a sin function.

#User define functions

#Target Sample
def uniform_proposal():
    return random.rand()

def target_function(x):
    return np.sin(x)

def rejection_sampling(target_func, num_samples):
    samples = []
    accepts = []
    rejects = []
    num_ace = 0
    num_rejected =0
    for i in range(num_samples):
        x = random.rand()
        u = random.rand()
        if u < target_func(x):
            samples.append(x)
            accepts.append(x)
            num_ace +=1
        else:
            num_rejected += 1
            rejects.append(x)
    acceptance_rate = (num_ace) / (num_ace+num_rejected)
    return samples, acceptance_rate

def rejection(target_func, num_samples):
    x_accepts = []
    y_rejects = []
    y_accepts = []
    x_rejects = []
    num_ace = 0
    num_rejected =0
    for i in range(num_samples):
        x = random.rand()
        y = random.rand()
        if y < target_func(x):
            x_accepts.append(x)
            y_accepts.append(y)
            num_ace +=1
        else:
            num_rejected += 1
            x_rejects.append(x)
            y_rejects.append(y)
    acceptance_rate = (num_ace) / (num_ace+num_rejected)
    return x_accepts,x_rejects, y_accepts, y_rejects, acceptance_rate

if __name__ == "__main__":


	# default number of samples
	Nsample = 1000
	xmin = 0
	xmax = 1
	seed = 5555
	random = Random(seed)

	# read the user-provided seed from the command line (if there)
	#figure out if you have to have -- flags before - flags or not
	if '-Nsample' in sys.argv:
		p = sys.argv.index('-Nsample')
		Nsample = int(sys.argv[p+1])
	if '-seed' in sys.argv:
		p = sys.argv.index('-seed')
		seed = int(sys.argv[p+1])
	if '-h' in sys.argv or '--help' in sys.argv:
		print ("Usage: %s [-seed] seed [-Nsample] number" % sys.argv[0])
		print
		sys.exit(1)  
	
	# Plot the target and proposal distributions

	x = np.linspace(0, 1.0, 1000)
	fig, ax = plt.subplots(figsize=(10, 6))
	ax.plot(x, target_function(x), label='Target Distribution')
	ax.axhline(y=0, color='gray', alpha=0.5)
	ax.axhline(y=0.5, color='gray', alpha=0.5)
	ax.axhline(y=1.0, color='gray', alpha=0.5)
	ax.fill_between(x, 0, target_function(x), alpha=0.2)
	ax.fill_between(x, 1.0, target_function(x), alpha=0.2)
	ax.plot(x, np.ones_like(x), label='Primary Sampling Distribution')
	ax.legend()
	plt.savefig("Step1_FindingFunction")
	plt.show()


	c = 1
	num_samples = Nsample
	x_min = 0
	x_max = 1
	samples, acceptance_rate = rejection_sampling(target_function, num_samples)

	print(f"Acceptance rate: {acceptance_rate}")
	plt.hist(samples, bins=20, density=True)
	plt.plot(np.linspace(x_min, x_max, 1000), target_function(np.linspace(x_min, x_max, 1000)), 'r')
	plt.savefig("Step2_Sampling")
	plt.show()


	ax,rx, ay, ry, acceptance_rate = rejection(target_function, num_samples)

	print(f"Acceptance rate: {acceptance_rate}")
	plt.plot(ax,ay,'ro')
	plt.plot(rx,ry,'bo')
	plt.plot(np.linspace(x_min, x_max, 1000), target_function(np.linspace(x_min, x_max, 1000)), 'r')
	plt.show()