from bardapi import Bard

token = 'fAgRg13fq_foOFEdAfjQpH19tP2KfH6gh4M7qGqG0EZyaq1Vec6IXm9jN-KigmrAPDxmlw.'
bard = Bard(token=token)
bard.get_answer("Hello")['content']