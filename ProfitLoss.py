costPrice = input("Enter Cost Price (In $) ")
sellingPrice = input("Enter Selling Price (In $) ")
if costPrice > sellingPrice:
	loss = costPrice - sellingPrice
	print("Loss = $ " + str(loss))
elif costPrice == sellingPrice:
	print("No Profit No Loss ")
else:
	profit = sellingPrice - costPrice
	print("profit = $ " + str(profit))
