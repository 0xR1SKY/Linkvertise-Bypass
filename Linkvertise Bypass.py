import requests

link = input("Enter Linkvertise link to bypass : ") # Getting the linkvertise link that the user wants to bypass


response = requests.get("https://api.bypass.vip/bypass?url=" + link) # Using the free Bypass.vip API to get the destination link (bypass the linkvertise ads)
result = str(response.content).split('"') # Splitting the response we get so we can only get the final link we need and not other useless info

print("\n\n")



# Displaying the final link with this method because of the splitting we did above
# The link we need starts from the 8th place in the array of the response so it will be result[7]

#	After some testing, it appears some links might have a script as output instead of a link
# That's why I use this method instead of just printing the result[7] (which would work if the response was just a link)
# In case it is just a link, it will just print the result[7] and exit the loop


i=7 # Because we just need the response starting from the 8th position (index 7 because arrays start from 0)
while i < (len(result)-1): # Works while the index i is less than the length of (the result array - 1), because the last item in the array "result" is always the character '}' which we do not need
	
	# Due to some links ending up on scripts we need to format it correctly. This will not change anything in normal links, at least from my tests
	# This change is necessary because of the response the Bypass.vip API which is given, in order to have the correct format when printing
	cur=result[i].replace("\\\\r\\\\n",'\n').replace("\\\\",'').replace("\\",'')
	
	# Finally printing the destination link/script
	# Correcting any " that may have got lost during the splitting I did before. (see how array "result" is made in line 7 if this is not understandable)
	if (i<len(result)-2):
		print(cur, end ='"')
	else:
		print(cur)
	i+=1 # Updating the index of array "result" so it can continue to the next one if necessary

input("\n\nPress Enter to exit...")