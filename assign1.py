item1 = int(input())
item2 = int(input())
item3 = int(input())
totalcost = item1+item2+item3
if(totalcost>50):
  print(f"Total cost after discount is ${totalcost-0.10*totalcost}")
else:
  print(f"Total cost without discount is ${totalcost}")