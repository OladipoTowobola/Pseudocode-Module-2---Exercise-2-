begin
  CUBIC_INCHES_PER_CUBIC_FOOT = 1728

  model_name = input("Enter the refrigerator model name: ")
  height = float(input("Enter the height in inches: "))
  width = float(input("Enter the width in inches: "))
  depth = float(input("Enter the depth in inches: "))

  capacity_cubic_inches = height * width * depth
  capacity_cubic_feet = capacity_cubic_inches / CUBIC_INCHES_PER_CUBIC_FOOT

  print(f"Refrigerator Model: {model_name}")
  print(f"Capacity: {capacity_cubic_feet:.2f} cubic feet")
 end 
