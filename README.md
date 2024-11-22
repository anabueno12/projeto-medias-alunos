# projeto-medias-alunos
Passo 1: Criar o Repositório no GitHub
Explicação: O primeiro passo é criar o repositório no GitHub para armazenar o código. Isso permite que você faça o controle de versão do seu projeto e compartilhe com outras pessoas, se necessário.
Acesse o GitHub e crie um novo repositório com o nome projeto-media-alunos.
Clone o repositório para o seu computador utilizando o comando: git clone (e o código)
Esse comando vai criar uma cópia local do repositório em seu computador.

Passo 2: Criar o Commit Inicial para Calcular a Média
Explicação: Agora que o repositório está configurado, vamos criar o arquivo media.py que irá conter a lógica para calcular a média simples das 3 notas do aluno.
Crie um arquivo chamado media.py
Colocar a lógica para receber as 3 notas do aluno e calcular a média simples.
Após salvar o código, adicione o arquivo ao Git com o comando: git add .
E o commit com a mensagem, isso cria um ponto de controle no seu projeto, permitindo que você registre o que foi feito até esse momento.
Envie as mudanças para o repositório remoto no GitHub: git push origin main
Isso envia seu código para o GitHub, tornando-o disponível online.

Passo 3: Criar o Branch feature/verificacao-aprovacao
Explicação: Criar uma nova funcionalidade (feature) normalmente é feito em um novo branch. Isso permite que você trabalhe em novas funcionalidades sem afetar o código principal (branch main).
Crie um novo branch chamado feature/verificacao-aprovacao para implementar a verificação de aprovação/reprovação. O comando para isso é:
git checkout feature/verificacao-aprovacao
Isso cria e muda para o novo branch adicione a lógica para verificar se o aluno foi aprovado ou reprovado com base na média.
Após salvar, adicione o arquivo ao Git com:
git add .
Faça o commit dessa nova funcionalidade com a mensagem
Envie esse novo branch para o repositório remoto:
git push origin main

Passo 4: Mesclar o Branch feature/verificacao-aprovacao 
Explicação: Após concluir a funcionalidade da verificação de aprovação, você precisa mesclar esse branch na main para integrar as mudanças ao código principal volte para o branch main com o comando: git checkout main
Mescle com git merge feature/verificacao-aprovacao
Envie as mudanças para o repositório remoto: git push origin main
Isso atualiza o repositório no GitHub com a funcionalidade de verificação de aprovação já integrada.

Passo 5: Criar o Branch feature/verificacao-recuperacao
Explicação: Agora, você vai criar uma nova funcionalidade para verificar se o aluno está em recuperação, ou seja, se a média for entre 5.0 e 6.0.
Crie um novo branch chamado feature/verificacao-recuperacao:
git checkout  feature/verificacao-recuperacao
Adicione a lógica para verificar se a média está entre 5.0 e 6.0 e, se estiver, o aluno está em recuperação.
Após salvar, adicione o arquivo ao Git:
git add .
Faça o commit com a mensagem:
git commit -m "Adicionada verificação de recuperação"
Envie esse novo branch para o GitHub:
git push origin feature/verificacao-recuperacao

Passo 6: Mesclar o Branch feature/verificacao-recuperacao 
Explicação: Após concluir a funcionalidade de verificação de recuperação, é hora de mesclar essas mudanças na main.
Volte para o branch main com:
git checkout main
Mescle o branch feature/verificacao-recuperacao  (git merge feature/verificacao-recuperacao)
Envie as mudanças para o GitHub: git push origin main

Passo 7: Criar o Branch feature/pesos
Explicação: Agora, vamos refatorar o código para calcular a média ponderada (onde a terceira nota tem um peso maior).
Crie um novo branch chamado feature/pesos:
git checkout  feature/pesos
Refatore o código para implementar o cálculo da média ponderada, onde:
As duas primeiras notas têm peso 1.
A terceira nota tem peso 2.
Após salvar, adicione o arquivo ao Git: git add .
Faça o commit com a mensagem:
git commit -m ""
Envie esse novo branch para o repositório remoto:
git push origin main

Passo 8: Mesclar o Branch feature/pesos na main
Explicação: Após a implementação da média ponderada, mescle o branch feature/pesos na main para atualizar a versão final do código.
Volte para o branch main com:
git checkout main
Mescle o branch feature/pesos na main: git merge feature/pesos
Envie as mudanças para o repositório remoto:
git push origin main

Resumo Final:
O processo todo envolve criar um repositório no GitHub, depois trabalhar em funcionalidades no formato de branches.
Cada branch contém uma funcionalidade específica (cálculo de média simples, aprovação, recuperação e média ponderada).
Cada mudança é comitada e enviada para o GitHub para controle de versão.