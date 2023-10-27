class AlunoClass:
  def __init__(self, nome, sobrenome, nota):    
    self.nome = nome;
    self.sobrenome = sobrenome;
    self.nota = nota;

  def mostrarAluno(self):
    return 'Aluno: ' + self.nome + ' ' + self.sobrenome + ' - Nota: ' + str(self.nota);    

  
  def salvar(self, conexao, colecao):    
    mydict = self.__dict__;
    mydict['nome'] = [i.__dict__ for i in self.nome]
    mydict['sobrenome'] = self.sobrenome.__dict__;
    mydict['nota'] = self.nota.__dict__;
    x = conexao[colecao].insert_one(mydict)    
    return x.acknowledged;