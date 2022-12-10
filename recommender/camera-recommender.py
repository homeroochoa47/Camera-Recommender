'''
***

This project originally ran on the command line with no user interface, and has since been updated to a django site. This is the original program which the site is based off of.

***
'''


#choices are nodes which contain the the input function which get called and asks the user to select their camera preferences. Depending on what the input is we move to the corresponding child node. We search through the topics in the child nodes and match that with the user input to select which node to move to.
class Choice:

    #the actions dictionary is what we use to traverse the nodes and decide which one is the correct next node based on user input. The structure for the actions dictionary is {'topic: [listof topics], 'inputstring': "string", 'recommendation': "camera recommendation"}
    #Using this structure will make it to where we can ask for an input if an input string exists, and suggest a recommendation if there is no longer a need for user input, meaning we have determined what to recommend them
    def __init__(self, actions = None):
        self.actions = actions #this is a dictionary
        self.children = []
        
    def __repr__(self):
        if type(self.actions['topic']) == list:
            return "/".join(self.actions['topic'])
        else:
            return self.actions['topic']
        
    def get_children(self):
        return self.children
    
    #might be able to clean this up
    def add_child(self, child):
        child_list = self.children
        child_list.append(child)
        self.children = child_list
        return self.children
    
#class of cameras with a couple of methods
class Camera:
    
    #here we add some attributes for our camera, which will be referenced as we accept inputs
    def __init__(self, name, price, type, mech_or_batt, uses ):
        self.name = name
        self.price = price
        self.type = type #rangefinder, slr, point and shoot
        self.mech_or_batt = mech_or_batt
        self.uses = uses

    #adding __repr__ to provide an option to retrieve some more details about the camera
    def __repr__(self): #need to figure out conditionals for final format
        return "The {camera} is a {type} camera which is {mech_or_batt}. It is best used for {uses} and can be bought for about ${price}.".format(camera = self.name, type = self.type, mech_or_batt = self.mech_or_batt, uses = self.uses, price = self.price)
        
    #method to ask user if they want more info about their suggested camera
    def more_info(self):
        answer = input("Would you like to learn more about this camera? \n")
        if "y" in answer:
            print(self)
        elif "n" in answer:
            print ("Happy buying!")
        else:
            print ("Enter yes or no")
            return more_info(self)
            

def request_input(node):
    userinput = input(node.actions['inputstring'])
    return userinput

def restart():
    restart = input('Would you like to start over? ')
    if "y" in restart.lower():
        return traverse(root)
    elif "n" in restart.lower():
        print ("See ya!")
        return
    else:
        print ("Enter yes or no")
        return restart()

def give_recommendation(node):
    print(node.actions['recommendation'])
    node.actions['camera'].more_info()
    return restart()


#function was made to call recursively. Works for now, but will require further refining once all of the tree nodes are added.
def traverse(start_point):
    current_node = start_point
    current_children = start_point.children
    #base case
    if 'recommendation' in current_node.actions.keys():
        return give_recommendation(current_node)
        #call function to get more info or start over
    
    #recursive call
    if 'inputstring' in current_node.actions.keys():
        userinput = request_input(current_node)
        
    for child in current_children:
        for topic in child.actions['topic']:       
            if topic in userinput.lower():
                return traverse(child)
            
    print ("Sorry, I didn't get that. Please try again.")
    traverse(current_node)

#---------------------
 #adding all of the cameras as objects:
himatic = Camera("Minolta Hi-Matic 7S", 75, "fixed lens rangefinder", "fully mechanical with optional batteries", "portraits, landacapes, and snapshots. It's a great all around camera" )

iqzoom = Camera("Pentax IQZoom", 25, "point & shoot", "battery powered", "quick photos and snapshots")

stylus = Camera("Olympus Stylus Zoom", "50 to $100", "point & shoot with a good zoom lens", "battery powered", "quick photos and snapshots")

bigmini = Camera("Konica Big Mini BM-201", "150+", "high-quality fixed lens point & shoot", "battery powered", "quick photos and snapshots with the potential for portraits landscapes, and more" )

olympus_xa = Camera("Olympus XA", 125, "portable fixed lens rangefinder", "battery powered", "portraits, landscapes, and quick photos on the go too")

nikon_fm = Camera("Nikon FM", 125, "interchangeable lens SLR", "fully mechanical with optional batteries", "portraits and landscapes with and has a great selection of lenses")

nikon_fe = Camera("Nikon FE", 150, "interchangeable lens SLR", "battery powered", "portraits and landscapes with and has a great selection of lenses")

olympus_rc = Camera("Olympus 35RC", 100, "small fixed lens rangefinder","fully mechanical with optional batteries", "portraits and landscapes" )
#---------------------

root = Choice(
        {
            'topic': ["first_choice"],
            'inputstring': "What types of photos do you want to take? (Portraits, landscapes, pics of your friends, quick snapshots or maybe a little bit of everything: \n"
        }
            
)

#second level
#---------------------
#portraits or landscapes
root_child1 = Choice(
        {
            'topic': ["portraits", "landscapes"],
            'inputstring': "Nice. Do you wand a camera with a fixed lens or do you want to be able to switch lenses? \n"
        }
)
#snapshots or friends
root_child2 = Choice(
        {
            'topic': ["friends", "snapshots"],
            'inputstring' :"You're probably best off with a point and shoot camera. What's your budget? Enter 'a' for under $50, 'b' for $51-$150, or 'c' for $150+ \n"
        }
)
#everything
root_child3 = Choice(
        {
            'topic': ["everything"],
            'recommendation':"Your best bet would be the Minolta Hi-Matic 7S.", 
            'camera': himatic
        }
)
#---------------------
#under root child 1
portraits_landscapes_fixed = Choice(
        {
        'topic': ['fixed'], 
        'inputstring': "Fixed lens it is. Now, are you interested in a fully mechanical camera, or one that relies on batteries? \n"
        }
)
#under root child 1
portraits_landscapes_interchangeable = Choice(
    {
        'topic': ['switch', 'lenses'],
        'inputstring': "So you'd prefer something with interchangeable lenses. Do you want battery powered or fully mechanical? \n"
    }
)
#---------------------
#under portraits and landscapes -- fixed
fixed_mechanical = Choice(
    {
        'topic': ['mechanical', 'mech'],
        'recommendation': "You might like the Olympus 35 RC",
        'camera': olympus_rc
    }
)
#under portraits and labdscapes -- fixed
fixed_battery = Choice(
    {
        'topic': ['battery', 'batt'],
        'recommencation': "You might like the Olympus XA",
        'camera': olympus_xa
    }
)
#---------------------
#under portraits and landscapes -- interchangeable
interchangeable_mechanical = Choice(
    {
        'topic': ['mechanical', 'mech'],
        'recommendation': "How about the Nikon FM?",
        'camera': nikon_fm
    }
)

interchangeable_battery = Choice(
    {
        'topic': ['battery', 'batt'],
        'recommendation': "How about the Nikon FE?",
        'camera': nikon_fe
    }
)
#---------------------
#under root child 2
snapshots_under50 = Choice(
    {
        'topic': ['a'],
        'recommendation': "Check out the Pentax IQZoom",
        'camera': iqzoom
    }
)

snapshots_51_150 = Choice(
    {
        'topic': ['b'],
        'recommendation':  "Check out the Olympus Stylus Zoom",
        'camera': stylus
    }
)

snapshots_any_price = Choice(
    {
        'topic': ['c'],
        'recommendation': "Check out the Konica Big Mini",
        'camera': bigmini
    }
)
#---------------------



#second level
root.add_child(root_child1)
root.add_child(root_child2)
root.add_child(root_child3)

#third level
root_child1.add_child(portraits_landscapes_fixed)
root_child1.add_child(portraits_landscapes_interchangeable)

root_child2.add_child(snapshots_under50)
root_child2.add_child(snapshots_51_150)
root_child2.add_child(snapshots_any_price)

#fourth level
portraits_landscapes_fixed.add_child(fixed_mechanical)
portraits_landscapes_fixed.add_child(fixed_battery)

portraits_landscapes_interchangeable.add_child(interchangeable_mechanical)
portraits_landscapes_interchangeable.add_child(interchangeable_battery)



print ("\nWelcome to the best friend of the modern youth: a tool that helps you figure out what film camera you should buy! What an exciting way to kick off your new hobby.\n")
print ("Lets start with a few questions to figure out the right choice for you.\n")
traverse(root)

