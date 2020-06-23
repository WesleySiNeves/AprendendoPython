import os

#/*Classes para manipulação dos diretorios*/
class UtilsDiretory(object):
  def __init__(self):
    self.DiretorioProjeto =""

  
  def get_diretorio(self,diretorio_base,sub_dir):
    return r"{0}/{1}".format(diretorio_base,sub_dir)
  
  
  def clear_diretorio(self,diretorio):
    for file in os.listdir(diretorio):
        full_name =os.path.join(diretorio, file)
        
        if os.path.exists(full_name):
            os.remove(full_name) 


#/*Classe para as configurações da rede */
class NetWorkConfiguration(object):
    def __init__(self):
        self.IdModelo =""
        self.NomeModelo=""
        self.TamanhoModelo=""
        self.EPOCHS=""
        self.INIT_LR=""
        self.BS=""
        self.IMAGE_SIZE=""
        self.Descricao=""
        self.DataCriacao=""
        self.QuantidadeImagensTotais=""
        self.QuantidadeImagensCovid=""
        self.QuantidadeImagensPneumonia=""
        self.QuantidadeImagensNormal =""
        self.QuantidadeImagensTrainX=""
        self.QuantidadeImagensTestX=""
        self.QuantidadeImagensTrainY=""
        self.QuantidadeImagensTestY=""
        self.Rotation_range=""
        self.Fill_mode=""
        self.Test_size=""
        self.TipoCNN=""
        self.NomeNoteBook = ""
        self.Acuracia = ""
        self.Sensitividade =""
        self.Especificidade =""


    def to_dictionary(self):
        self.NomeModelo = self.get_ModelName()
        return {
            'IdModelo' : self.IdModelo,
            'NomeModelo' :self.NomeModelo,
            'TamanhoModelo':self.TamanhoModelo,
            'EPOCHS' :self.EPOCHS,
            'INIT_LR' :self.INIT_LR,
            'BS' : self.BS,
            'IMAGE_SIZE' :self.IMAGE_SIZE,
            'Descricao' :self.Descricao,
            'DataCriacao' :self.DataCriacao,
            'QuantidadeImagensTotais' :self.QuantidadeImagensTotais,
            'QuantidadeImagensCovid' :self.QuantidadeImagensCovid,
            'QuantidadeImagensPneumonia' :self.QuantidadeImagensPneumonia,
            'QuantidadeImagensNormal' :self.QuantidadeImagensNormal,
            'QuantidadeImagensTrainX' :self.QuantidadeImagensTrainX,
            'QuantidadeImagensTestX' :self.QuantidadeImagensTestX,
            'QuantidadeImagensTrainY' :self.QuantidadeImagensTrainY,
            'QuantidadeImagensTestY' :self.QuantidadeImagensTestY,
            'Rotation_range' :self.Rotation_range,
            'Fill_mode' :self.Fill_mode,
            'Test_size' :self.Test_size,
            "TipoCNN" :self.TipoCNN,
            "NomeNoteBook" :self.NomeNoteBook,
            "Acuracia" :self.Acuracia,
            "Sensitividade" :self.Sensitividade,
            "Especificidade" :self.Especificidade,

        }
    def get_ModelName(self):
      self.NomeModelo = "Model_{0}_{1}_{2}_EPOCHS_{3}_BS_{4}_ACC_{5}_Sens_{6}_Espec".format(config.TipoCNN,config.NomeNoteBook,config.EPOCHS,config.BS,config.Acuracia,config.Sensitividade,config.Especificidade) 
      return self.NomeModelo

    def get_propriedades(self):
      return [i for i in self.__dict__.keys() if i[:1] != '_']

    # Métodos são funções, que recebem como parâmetro atributos do objeto criado    
    def getInformacoes(self):
        print('Modelo {0}|{1} criado em {2} |com {3} EPOCHS|{4} IMG_COVID| {5} IMGPNEU|{6} IMGNORMAL'.
        format(self.IdModelo,self.NomeModelo,str(self.DataCriacao),self.EPOCHS,self.QuantidadeImagensCovid,self.QuantidadeImagensPneumonia,self.QuantidadeImagensNormal))