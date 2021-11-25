import ephem
mars = ephem.Mars()
mars.compute('2008/1/1')
print(mars.ra)