def mergeSort(alist): #Definition for the mergesort

   print("Splitting ",alist) 

   if len(alist)>1: #only runs if list is not one item
       mid = len(alist)//2
       lefthalf = alist[:mid] #sets up left half, right half, and middle
       righthalf = alist[mid:]

       #recursion
       mergeSort(lefthalf) #runs another merge onto the halfs, will have only 1 item at some point
       mergeSort(righthalf)  

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf): #compares halves repativialy until fully sorted
           if lefthalf[i] < righthalf[j]:
               alist[k]=lefthalf[i]
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           alist[k]=righthalf[j]
           j=j+1
           k=k+1

   print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist) #calls the functions
print(alist)