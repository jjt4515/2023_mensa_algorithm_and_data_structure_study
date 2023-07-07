class Stack :
    
    def __init__ (self) :
        self.__stack__=[]
        
    def top(self) :    
        try :
            return self.stack[-1]
        except Exception as e:    
                print("stack's size zero. Try push!", e)
                
    def pop(self) :
        try :
            return self.stack[-1]
        except Exception as e:    
                print("stack's size zero. Try push!", e)    
                  
    def push(self, data) : 
        (self.__stack__).append(data)
        
    def empty(self) :
        if len(self.__stack__) == 0 :
            return True
        else :
            return False
        
    def size(self) :
        return len(self.__stack__)        
