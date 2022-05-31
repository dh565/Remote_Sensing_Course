# Excluse negative NDVI values from image
NDVI[NDVI < 0] = np.nan

# List minimum LST (humid limit) and maximum LST (dry limit)
MiniList    = []
MaxList     = []

# Create an NDVI vector (0 to 1 with intervals of 0.01)
NDVI_vector = np.round(np.arange(0.01, 1.01, 0.01), 2)

# Find LST values for each NDVI value:
for val in NDVI_vector:
  TS_lst_val = []
  row, col = np.where(NDVI == val) # find real NDVI values that correspond to NDVI values in the created vector
  # For each NDVI value get temperatures
  # Assign a place to these values (rows and columns)
  for i in range(len(row)):
    if np.isfinite(TS[row[i], col[i]]): # exclude nan
      TS_lst_val += [TS[row[i], col[i]]]
  
  # Find if there are LST values that correspond to the NDVI values and take 
  # only maximum and minimum values
  if TS_lst_val != []:
    TS_min_val = np.min(TS_lst_val)
    TS_max_val = np.max(TS_lst_val)
  else:
    TS_min_val = np.nan # all others get nan
    TS_max_val = np.nan

  # Add found values to MiniList and MaxList lists
  MiniList += [TS_min_val]
  MaxList  += [TS_max_val]

# Create line for minimum, lower border
MiniList_fin = []
NDVI_fin     = []
for i, val in enumerate(MiniList):# make sure, again, we exclude the nan's
  if np.isfinite(val):
    MiniList_fin += [val]
    NDVI_fin += [NDVI_vector[i]]

# Get the (a and b) coefficients of the bottom linear regression equation
MinPfit = np.polyfit(NDVI_fin[17:], MiniList_fin[17:], 1)

# Create the line for the upper border
MaxList_fin = []
NDVI_fin = []
for i, val in enumerate(MaxList):
  if np.isfinite(val):
    MaxList_fin += [val]
    NDVI_fin += [NDVI_vector[i]]

# Get the (a' and b') coefficients of the upper linear regression equation
MaxPfit = np.polyfit(NDVI_fin[17:], MaxList_fin[17:], 1)

# Generate the first and last wet and dry limit points
a1, b1 = MaxPfit
a2, b2 = MinPfit
linhamax = [b1 + (a1 * 0), b1 + (a1 * 1)]# max linear regression for trapez
linhamin = [b2 + (a2 * 0), b2 + (a2 * 1)]# min linear regression for trapez
