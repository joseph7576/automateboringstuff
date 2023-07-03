# part 1

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory:dict):
    print("Inventory:")
    
    item_total = 0
    
    for stuff, count in inventory.items():
        item_total += count    
        print(f'{count} {stuff}')
        
    print("Total number of items: " + str(item_total))


displayInventory(stuff)


# part 2

# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'] -> example

def addToInventory(inventory:dict, addedItems:list):
    
    for stuff in addedItems:
        if stuff in inventory:
            inventory[stuff] += 1
        else:
            inventory[stuff] = 1
            
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)

displayInventory(inv)