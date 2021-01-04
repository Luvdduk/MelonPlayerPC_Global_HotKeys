'''from pynput.keyboard import Listener, Key
 
store = set()
instance = set()
 
def handleKeyPress( key ):

       
    store.add( key )
    print( 'Press: {}'.format( store ) )
    
 
def handleKeyRelease( key ):
    print( 'Released: {}'.format( key ) )
    if key in store:
        instance = store 
        store.remove( key )
        print("저장된 키:{}".format(instance) )
    

    # 종료
    if key == Key.esc:
        print(store)
 
with Listener(on_press=handleKeyPress, on_release=handleKeyRelease) as listener:
    listener.join()'''


from pynput.keyboard import Listener, Key
 
store={}
 
def handleKeyPress( key , store):

       
    store += key
    print( 'Press: {}'.format( store ) )
    
 
def handleKeyRelease( key ):
    print( 'Released: {}'.format( key ) )
    if key in store:
        instance = store 
        store.remove( key )
        print("저장된 키:{}".format(instance) )
    

    # 종료
    if key == Key.esc:
        print(store)
 
with Listener(on_press=handleKeyPress, on_release=handleKeyRelease) as listener:
    listener.join()