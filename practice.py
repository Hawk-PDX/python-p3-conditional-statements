dog = "cuddly"

dict_map = {
    "hungry": "Refilling food bowl.",
    "thirsty": "Refilling water bowl.",
    "playful": "Playing tug-of-war.",
    "cuddly": "Snuggling.",
}

# Remember that a dictionary's .get() method lets us set a default value!
owner = dict_map.get(dog, "Reading newspaper.")

# This approach is very concise, but the mapping dictionary itself is not so intuitive to read; as we can see, the keys describe the state of the dog while the values describe the state of the owner. Dictionary mapping is a valuable tool for long lists of conditions, but if/elif/else statements are typically the preferred method for handling switch/case logic in Python.