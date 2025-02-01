#Compile qasm code to a quantum circuit
from os import listdir
from os.path import isfile, join



#Basic gates might be read from qasm file:
qasmgatename=["cz","cx","ccx","h","u3","sx","rx","ry","sxdg","s"]


two_qubit_gates=["cz","cx"]
three_qubits_gates=["ccx"]
single_qubit_gates=["h","sx","sxdg","s"]
single_qubit_single_param=["rx","ry"]
single_qubit_three_param=["u3"]


#Class of quantum circuit
class quantumCircuit:
    
    #initialize the class
    def __init__(self):
        pass
    
    def construct_from_gate_list():
        pass

    


class qasmReader:
    
    
    #initialize the class
    def init(self):
        self._qasmstring = ""
        self._nqubit=None
        self._gates=[]
        print(self._gates)
        
        
    def read_from_file(self,filename):
        self._qasmfilename=filename
        with open(filename) as f:
            self._qasmstring = f.read()
        return self._qasmstring
    
    
    def parse(self):
        #Skip the first seven line
        qasmstring = self._qasmstring
        qasmstring = qasmstring.split("\n")[7:]
        #Filter out empty string
        qasmstring = list(filter(None, qasmstring))
        #Filter our all comment string start with //
        qasmstring = [x for x in qasmstring if not x.startswith("//")]
        self._nqubit = int(qasmstring[0].split(" ")[1][2:-2])
        qasmstring = qasmstring[1:]
        self._gates=[]
        for tmpstring in qasmstring:
            tmpstring = tmpstring.split(" ")
            if tmpstring[0] in single_qubit_gates:
                qubits=int(tmpstring[1][2:-2])
                self._gates.append((tmpstring[0],qubits))
            elif tmpstring[0] in two_qubit_gates:
                qubits=tmpstring[1][:-1].split(",")
                qubits=[int(x[2:-1]) for x in qubits]
                self._gates.append((tmpstring[0],(qubits[0],qubits[1])))
            elif tmpstring[0] in three_qubits_gates:
                qubits=tmpstring[1][:-1].split(",")
                qubits=[int(x[2:-1]) for x in qubits]
                self._gates.append((tmpstring[0],(qubits[0],qubits[1],qubits[2])))
            else:
                gatename=tmpstring[0][:2]
                gateparams=tmpstring[0][3:-1].split(",")
                gateaparamsfloat=[]
                for param in gateparams:
                    if param=='0':
                        gateaparamsfloat.append(0.0)
                    else:
                        gateaparamsfloat.append(float(param[3:]))
                if gatename in single_qubit_single_param:
                    qubits=int(tmpstring[1][2:-2])
                    self._gates.append(((gatename,gateaparamsfloat),qubits))
                elif gatename in single_qubit_three_param:
                    qubits=int(tmpstring[1][2:-2])
                    self._gates.append(((gatename,gateaparamsfloat),qubits))
                else:
                    print("Error: Gate not supported")
                    print(tmpstring[0])
        print(*self._gates,sep='\n')
        
 
 
def parse_all_qasm_file():
    qasmreader = qasmReader()
        
    onlyfiles = [f for f in listdir("qasm/tests/") if isfile(join("qasm/tests/", f))]
    
    for file in onlyfiles:
        qasmreader.read_from_file("qasm/tests/"+file)
        qasmreader.parse()  


        

if __name__ == "__main__":
    #parse_all_qasm_file()
    #qasmreader = qasmReader()
    
    #qasmreader.read_from_file("qasm/tests/1.1.qasm")
    #qasmreader.parse()  
    parse_all_qasm_file()