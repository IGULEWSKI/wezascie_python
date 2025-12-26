class File:
    def __init__(self,name):#jak nie ma childa to plik jak ma childa to folder
        self.name=name
        self.data=None
        self.child=None
        self.next=None
def get_next_dir(path):
    ...
def get_remaining_path(path):
def cd(root:File,path:str):
    if root!=None:
        if path=="":
            return root
        next_dir=get_next_dir(path)
        cur_child=root.child
        child_name=cur_child.name
        while child_name!=next_dir and cur_child.child != None:
            cur_child=cur_child.next
            child_name=cur_child.name
        if child_name==next_dir:
            return cd(cur_child,get_remaining_path(path))

def touch(root,path):
    next_dir=get_next_dir(path)
    while next_dir != None:
        fil=cd(root,path)
        if fil==None:

        ppath=get_remaining_path(next_dir)
        next_dir=get_next_dir(ppath)


def BRATUSZEWSKArm(fil:File):
    while fil!=None:
        biedny_student=fil.child
        MAJĘCKIrm(biedny_student)
        
def MAJĘCKIrm(fil):
    if fil==None:
        return ""
    MAJĘCKIrm(fil.next)
    if fil.child!=None:
        BRATUSZEWSKArm(fil.child)
    fil=None

        



        
                
        
    



        

    
    
