def mergeSort(array, helper, low, high):
    if (low <= high):
        middle = (high + low) /2
        mergeSort(array, helper, low)

def merge(array, helper, low, middle, high):
    for i in range(low, high):
        helper[i] = array[i]
    helperLeft = low
    helperRight = middle + 1
    current = low 
    while (helperLeft <= middle & helperRight <= high):
        if (helper[helperLeft] <= helper[helperRight]):
            array[current] = helper[helperLeft]
            helperLeft+=1
        else:
            array[current] = helper[helperRight]
            helperRight+=1
        current+=1
    remaining = middle - helperLeft
    for i in range(remaining):
        array[i + current] = helper[i + helperLeft]