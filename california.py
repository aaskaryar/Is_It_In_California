def is_in_california(latitude, longitude):
    california_bounds = {
        'min_lat': 32.53,
        'max_lat': 42.01,
        'min_long': -124.41,
        'max_long': -116.05
    }
    if (california_bounds['min_lat'] <= latitude <= california_bounds['max_lat'] and
            california_bounds['min_long'] <= longitude <= california_bounds['max_long']):
        return True
    else:
        return False

      
      
##output data
# is_in_california(34.052235,-118.243683 )
# Out[107]: True

# is_in_california(33.569592,-117.726372 )
# Out[108]: True

# is_in_california(36.169941,-115.139832 )
# Out[109]: True

# is_in_california(40.712776,-74.005974 )
# Out[110]: False
