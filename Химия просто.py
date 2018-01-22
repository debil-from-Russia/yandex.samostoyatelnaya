def chemical_elements(molecule):
    elements = []
    true_elements = []
    
    for letter in molecule:
        if letter.isalpha() and letter not in elements:
            elements.append(letter)
    for i in range(len(elements)):
        if elements[i].isupper():
            if i==len(elements)-1:
                true_elements.append(elements[i])
            elif elements[i+1].isupper():
                element = elements[i]
                true_elements.append(element)
            elif elements[i+1].islower():
                element = elements[i]+elements[i+1]
                true_elements.append(element)
        else:
            continue
        
            
    return true_elements
                
            