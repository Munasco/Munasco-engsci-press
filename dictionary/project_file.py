import csv
import time
from avltrees import BalancingTree
from lab0_utilities import *

class Engsci_Press:
    def __init__(self):
        pass
    def process_dictionary(self, filename):
        with open(filename, 'r') as f:       
            t = f.readline()
            t.replace('\n', '')
            t_1 = t.split(' (')
            tree = BalancingTree(Node(Word(t_1[0], t_1[1])))
            csv_row = csv.reader(f)
            for row in csv_row:
                if(row != []):
                    row = ''.join(row)
                    n = row.split(' (')
                    if(len(n) == 2):
                        n[1] = '(' + n[1]
                        tree.balanced_insert(Node(Word(n[0], n[1])))
            return tree 
                
    def collate_bsts(self):
        self.dictionary_tree = BalancingTree(Node2(self.process_dictionary('projects/dictionary/Dictionary_in_csv/A.csv')))
        dictionary_format = 'projects/dictionary/Dictionary_in_csv/'
        for i in range(66, 91):
            filename = dictionary_format + str(chr(i)) + '.csv' 
            self.dictionary_tree.balanced_insert(Node(self.process_dictionary(filename)))
        return self.dictionary_tree
    
    def search(self, root, key):
        while root and not root._val == key:
            if key < root._val:
                root = root.left
            else:
                root = root.right
        return root
    
    def output_definition(self, phrase):
        phrase = phrase.capitalize()
        z = self.search(self.dictionary_tree.root, phrase[0])
        p = self.search(z.val.root, phrase)
        x = []
        for i in p.val:
            x.append(i.definition)
        return x
        

    def findName(self, node, language_name):
        if node is None:
            return False
        if language_name in node._val:
            return node.val.definition
        elif language_name < node._val:
            return self.findName(node.left, language_name)
        else:
            return self.findName(node.right, language_name)

if __name__== '__main__':
    dict = Engsci_Press()
    x = time.time()
    dict.collate_bsts()
    print(dict.output_definition("Azure"))
    y = time.time()
    

