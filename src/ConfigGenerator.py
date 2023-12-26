# script for AAI arena configuration generation

class AAIObj:
    """A class to hold AnimalAI objects attributes"""
    def __init__(self, name, positions=None, rotations=None, sizes=None, colors=None, additional=None, warning=True) -> None:
        """Initialization of several objects of the same type.
        :param name: Official name of target type of object
        :param positions: (x,y,z) position of each object of target type, randomized by default 
        :param rotations: 0~360 degree rotation of each object of target type, randomized by default 
        :param sizes: (x,y,z) size of each object of target type, randomized by default 
        :param colors: (r,g,b) color of each object of target type, randomized by default 
        :param additional: additional parameters, not defined here, leave for extension
        :param warning: True, prompt a warning message when length of attribute list is different from number of objects; False, turn off the warning message
        """
        
        self. name = name
        self.positions = positions
        self.rotations = rotations
        self.sizes = sizes
        self.colors = colors
        self.additional = additional
        
        if warning: # prompt a warning message when any object miss any attributes
            length = 0 # number of objects in an attribute, should be same in all attributes
            if positions != None:
                length = len(positions)
                
            if rotations != None: # check number of objects in rotations
                if length > 0:
                    if len(rotations) != length:
                        print("Error: wrong rotations length for "+name+"!\n")
                else:
                    length = len(rotations)
                    
            if sizes != None: # check number of objects in rotations
                if length > 0:
                    if len(sizes) != length:
                        print("Error: wrong sizes length for "+name+"!\n")
                else:
                    length = len(sizes)
                    
            if colors != None: # check number of objects in rotations
                if length > 0:
                    if len(colors) != length:
                        print("Error: wrong colors length for "+name+"!\n")
                else:
                    length = len(colors)
        return
        

class ConfigWriter:
    """A class to write AnimalAI objects into configuration files"""
    def __init__(self) -> None:
        return
        
    def writeHeader(self, file, passMark=None, time=None, notes=None):
        """Write configuration file header and default arena header. 
        Useful when having only one arena in a configuration file
        :param file: path of target configuration file
        :param passMark: pass mark of first arena, float
        :param time: time limit of first arena, integer
        :param notes: Optional notes at the top of file introducing arena"""
        self.writeConfigHeader(file, notes)
        self.writeArenaHeader(file, passMark, time)
            
    def writeConfigHeader(self, file, notes=None):
        """Write configuration file header 
        :param file: path of target configuration file
        :param notes: Optional notes at the top of file introducing arenas"""
        with open(file, 'w') as f:
            if notes != None:
                f.write("#{}\n".format(notes))
            f.write("!ArenaConfig\narenas:\n")
            
    
            
    def writeArenaHeader(self, file, passMark=None, time=None, blackouts=None, arena=0, additional=None):
        """Write arena header. Useful when having multiple arenas in a configuration file
        :param file: path of target configuration file
        :param passMark: pass mark of this arena, float
        :param time: time limit of this arena, integer, setting to values <=0 to make arena permanent
        :param arena: index of this arena
        :param addition: a list of additional attributes of this arena, [("title", values),...]"""
        with open(file, 'a') as f:
            f.write("  {}: !Arena\n".format(arena))
            if passMark != None:
                f.write("    pass_mark: {}\n".format(passMark))
            if time != None:
                f.write("    t: {}\n".format(time))
            if blackouts != None:
                f.write("    blackouts: {}\n".format(blackouts))
            if additional != None:
                for attr in additional:
                    f.write("    {}: {}\n".format(attr[0],attr[1]))
            f.write("    items:\n")
            
    def writeItems(self, file, objects):
        """Write a list of different type of objects in same arena
        :param file: path of target configuration file
        :param objects: list of different type of objects"""
        with open(file, 'a') as f:
            for obj in objects:
                self.writeObject(f, obj)
            
    def writeObject(self, f, obj):
        """Write a type of objects in same arena
        :param f: handler of target configuration file
        :param obj: a type of objects, instantiation of AAIObj class"""
        f.write("    - !Item\n")
        f.write("      name: {}\n".format(obj.name))
        if obj.positions != None:
            f.write("      positions: \n")
            for pos in obj.positions:
                f.write("      - !Vector3 {{x: {}, y: {}, z: {}}}\n".format(pos[0], pos[1], pos[2]))
        if obj.rotations != None:
            f.write("      rotations: {}\n".format(obj.rotations))
        if obj.sizes != None:
            f.write("      sizes: \n")
            for size in obj.sizes:
                f.write("      - !Vector3 {{x: {}, y: {}, z: {}}}\n".format(size[0], size[1], size[2]))
        if obj.colors != None:
            f.write("      colors: \n")
            for color in obj.colors:
                f.write("      - !RGB {{r: {}, g: {}, b: {}}}\n".format(color[0], color[1], color[2]))
        if obj.additional != None:
            obj.writeAdditional(f)

if __name__ == "__main__":
    cw = ConfigWriter()
    file1 = "example1.yml"
    cw.writeHeader(file1, None, 250, "Example 1 showing basic usage.")
    
    objs = []
    objs.append(AAIObj("Wall", positions=[(21,0,10)],rotations=[0],sizes=[(5,3,1)],colors=[(255,0,255)]))
    objs.append(AAIObj("GoodGoalBounce", positions=[(18,0,22),(26,0,15)],rotations=[90, 60],sizes=[(1,1,1), (3,3,3)])) # GoodGoalBounce cannot change color
    objs.append(AAIObj("Agent",positions=[(20,0,15)],rotations=[0]))
    cw.writeItems(file1, objs)
    
    file2 = "example2.yml"
    cw.writeConfigHeader(file2, "Example 2 showing additional attributes and ranomization.")
    cw.writeArenaHeader(file2, passMark=1, time=250, blackouts=None, arena=0, additional=[("blackouts", [20,50])])
    
    objs = []
    objs.append(AAIObj("Wall", positions=[(10,0,10),(21,0,10)],rotations=None,sizes=None,colors=None))
    objs.append(AAIObj("GoodGoalBounce", positions=None,rotations=None,sizes=None))
    objs.append(AAIObj("Agent",positions=None,rotations=None))
    cw.writeItems(file2, objs)
    
    print("Done.")