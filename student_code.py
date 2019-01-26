import read, copy
from util import *
from logical_classes import *
#import pdb


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        if fact.name=="fact":  #checking if the input is actually a fact. Or should I do isinstance(fact,Fact)? 
            if fact not in self.facts: 
                self.facts.append (fact)
                print("Asserting {!r}".format(fact))
            # pdb.set_trace()
    
    def kb_ask(self, fact):
        list_of_bindings = ListOfBindings()
        if isinstance(fact, Fact): 
            for items in self.facts:
                if match(items.statement, fact.statement): 
                    list_of_bindings.add_bindings(match(items.statement, fact.statement))

            
        return list_of_bindings
        print("Asking {!r}".format(fact))