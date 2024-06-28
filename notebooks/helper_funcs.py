from impact import Impact
from distgen import Generator

def update_distgen(G,settings=None,verbose=False):
    G.verbose=verbose
    if settings:
        for key in settings:
            val = settings[key]
            if key.startswith('distgen:'):
                key = key[len('distgen:'):]
                if verbose:
                    print(f'Setting distgen {key} = {val}')
                G[key] = val
            
    
    # Get particles
    
    return G

def update_impact(I,settings=None,
               impact_config=None,
               verbose=False):
    
    I.verbose=verbose
    if settings:
        for key in settings:
            val = settings[key]
            if not key.startswith('distgen:'):
               # Assume impact
                if verbose:
                    print(f'Setting impact {key} = {val}')          
                I[key] = val                
   
    return I

# Functions to scan L1 and L2 phases
def getEnergyChangeFromElements(activeMatchStrings,tao):
    #VOLTAGE is just gradient times length; need to manually include phase info
    voltagesArr = [tao.lat_list(i, "ele.VOLTAGE", flags="-no_slaves -array_out") for i in activeMatchStrings]
    voltagesArr = np.concatenate(voltagesArr)
    
    angleMultArr = [tao.lat_list(i, "ele.PHI0", flags="-no_slaves -array_out") for i in activeMatchStrings]
    angleMultArr = np.concatenate(angleMultArr)
    angleMultArr = [np.cos(i * (2*3.1415) ) for i in angleMultArr] #Recall Bmad uses units of 1/2pi

    return( np.dot(voltagesArr, angleMultArr) )


def setLinacGradientAuto(activeMatchStrings, targetVoltage,tao): 
    #Set to a fixed gradient so everything is the same. Not exactly physical but probably close
    baseGradient = 1.0e7
    tao=tao
    for i in activeMatchStrings: tao.cmd(f'set ele {i} GRADIENT = {baseGradient}')
    
    #See the resulting voltage gain
    voltageSum  = getEnergyChangeFromElements(activeMatchStrings,tao)
    
    #print(voltageSum/1e6)
    
    #Uniformly scale gradient to hit target voltage
    for i in activeMatchStrings: tao.cmd(f'set ele {i} GRADIENT = {baseGradient*targetVoltage/voltageSum}')
    
    voltageSum  = getEnergyChangeFromElements(activeMatchStrings,tao)
    
    #print(voltageSum/1e6)

def setLinacPhase(activeMatchStrings, phi0Deg,tao):
    for i in activeMatchStrings: tao.cmd(f'set ele {i} PHI0 = {phi0Deg / 360.}')

def printArbValues(activeElements, attString,tao):
    #The .tolist() is because of issues when activeElements is a numpy array
    namesList = [ tao.lat_list(i, "ele.name", flags="-no_slaves -array_out") for i in activeElements.tolist() ]
    namesList = np.concatenate(namesList)
    valuesList = [ tao.lat_list(i, f"ele.{attString}",flags="-no_slaves -array_out") for i in activeElements.tolist() ]
    valuesList = np.concatenate(valuesList) / 1e9
    
    printThing = np.transpose([namesList, valuesList])
    display(pd.DataFrame(printThing))
