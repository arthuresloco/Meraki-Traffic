# Meraki-Traffic
An extremely crude graph of network traffic upload and download.

This application take the traffic.csv file created by the Meraki Dashboard from Traffic Analytics.  It places the Traffic type,
data sent, and data recieved into an array.  It then places the two traffic paths on a matplotlib x,y graph to visualize the amount of
data sent in any given direction.
To befixed - I need to change the y-axis from using a number plot to leverageing the traffic type array as the substitute for the number
ticks.  That way you can see the actual application consuming the data.

This wil be change in future release to include
-leveraging the traffic analysis API instead of CSV file format
-clean up of Data Representation
-moving to pygal so that I can use SVG file format for a more web friendly representation.
