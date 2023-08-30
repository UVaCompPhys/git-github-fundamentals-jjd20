import math
import matplotlib.pyplot as plt

"""calculateNSphereDimension: Method used to calculate the dimension of an nSphere
        dimension: the dimension of the nSphere that is to have it's volume calculated
        radius: the radius of the nSphere tha is to have it's volume calculated
"""
def calculateNSphereDimension(dimension, radius):
    return ( (math.pi ** (dimension/2))  / (math.gamma( (dimension/2) + 1)) ) * (radius ** dimension)

#Declares information required for the plots to be created 
fig1 = plt.figure(1,figsize=(40,40))
fig2 = plt.figure(2,figsize=(40,40))
fig3 = plt.figure(3,figsize=(40,40))
fig4 = plt.figure(4,figsize=(40,40))
axReg = fig1.add_subplot(111)
axLog = fig2.add_subplot(111)
ax3D = fig3.add_subplot(111, projection='3d')
axLog3D = fig4.add_subplot(111, projection='3d')

#Nested loops to calculate the volume of each n-sphere dimension at each prescribed radius
for dimensionN in range(0,51,1):
    for radiusR in range(0,205,5):
        
        #Python can only find a range through integers, so the radius is initially 100x larger than it should be
        radiusR = radiusR/100
        volume = calculateNSphereDimension(dimensionN, radiusR)
        
        #For the plot of the values of the natural logarithm of the volume
        lnVolume = -1
        if volume > 1:
            lnVolume = math.log(volume)
            
        #Creates one plot with the value of the volume
        axReg.plot(dimensionN,volume,color="k",marker = 'o')
        axReg.set_xlabel('Dimension of n-Sphere')
        axReg.set_ylabel('Volume')
        axReg.set_title('Figure 1: Dimension v Volume')
        
        #
        ax3D.scatter(dimensionN, radiusR, volume)
        ax3D.set_xlabel('Dimension of n-Sphere')
        ax3D.set_ylabel('Radius of n-Sphere')
        ax3D.set_zlabel('Volume')
        ax3D.set_title('Figure 3: 3D Plot of Dimension v Radius v Volume')

        #Creates a second plot with the value of the natural logarithm of the volume (provided that the volume is >= 1) 
        #The intention here is to better visualize the spread out data as seen in the first figure
        if lnVolume > 0:
            #
            axLog.plot(dimensionN,lnVolume,color="b",marker = 'o')
            axLog.set_xlabel('Dimension of n-Sphere')
            axLog.set_ylabel('Natural Logarithm of Volume (for volumes >=1)')
            axLog.set_title('Figure 2: Dimension v Natural Logarithm of Volumes (for volumes >= 1)')
            
            #
            axLog3D.scatter(dimensionN, radiusR, lnVolume)
            axLog3D.set_xlabel('Dimension of n-Sphere')
            axLog3D.set_ylabel('Radius of n-Sphere')
            axLog3D.set_zlabel('Natural Logarithm of Volume (for volumes >=1)')
            axLog3D.set_title('Figure 4: 3D Plot of Dimension v Radius v Natural Logarithm of Volumes (for volumes >= 1)')
            
plt.show()
        

