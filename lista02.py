#1º a variavel com um underscore é apenas uma especie de acordo social entre os desenvolvedores para dizer que ninguem deve mecher naquilo de fora, sendo assim privado, já com dois underscores é para que nao dê problema de hierarquia de herança entre classe mae e filha 

#2º vai dar um erro de atributo pois sem o setter, nao existe nenhum mecanismo de escrita configurado para o nome total

#3º porque a validação no setter é sempre cumprida independente do modulo onde o atributo for importado, ja sem ele sempre terá que fazer a validacao todas as vezes que importar, o que pode gerar problemas

#4º Alem desse Exception pegar qualquer tipo de erro, sendo assim genérico e nao especifica qual foi o erro em si, mesmo que o erro seja esperado do dominio (classificado por quem programou o programa) ou um bug normal despercebido como um AtributeError, o pass garante que mesmo capturando, nada vai ser feito com o erro, nem sequer ser apresentado.

#5º MeuErro herda o comportamento de exception, a mae de quase todas as exceções do python, onde esse comportamento é guardar uma mensagem e mostrar resumidamente entre outros comportamentos