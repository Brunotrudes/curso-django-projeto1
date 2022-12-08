# O nosso repositório para as próximas aulas está no seguinte link:

# https://github.com/luizomf/curso-django-projeto1

# Todo o código digitado nas aulas posteriores será publicado nele. Além
# disso,
# ara cada uma das aulas, vou fazer commit das alterações e você terá acesso
#  ao código digitado naquela aula.

# Provavelmente, não teremos apenas este repositório ao longo do curso todo,
# mas por agora guarde este link.

# Problemas com chaves SSH no Windows

# Observação: antes de mais nada, caso não queira ter que passar pelo
# transtorno de tentar fazer chaves SSH funcionarem corretamente no Windows,
#  simplesmente use seu usuário e senha do github ao fazer push e pull do
#  repositório. Assim não terá que configurar nada.

# Problema: no momento em que eu estava testando os comandos do GIT com chaves
# SSH das aulas anteriores no Windows, tive que adicionar as chaves SSH
# manualmente ao ssh-agent do Windows. Eu achei um processo meio complicado,
# porque deve ser feito a cada vez que você abrir o terminal novamente.
# Por isso, pesquisei e encontrei uma solução que achei melhor
# em https://stackoverflow.com/questions/18404272/running-ssh-agent-when-
# -starting-git-bash-on-windows.

# Fiz o seguinte:

# Observação: todos os comandos são para uso com o Git Bash. Não execute isso
# no CMD, PowerShell ou Windows Terminal, já que eu não testei os comandos
# nesses programas e podem não funcionar como esperado.

# Passo 1 - Crie um arquivo chamado config na pasta .ssh dentro da pasta do
#  seu usuário.

# touch ~/.ssh/config
# code ~/.ssh/config
# Passo 2 - Cole o seguinte conteúdo (substitua o que for necessário):

# Host *
#     IgnoreUnknown AddKeysToAgent,UseKeychain
#     UseKeychain yes
#     AddKeysToAgent yes
#     IdentityFile ~/.ssh/id_rsa
#     User SEU_USUARIO_DO_SISTEMA
#     Port 22

# Host github.com
#     HostName github.com
#     User SEU_USUARIO_DO_GITHUB
#     IdentityFile ~/.ssh/id_rsa
# Passo 3 - Salve o arquivo e reinicie o computador

# No meu caso funcionou normalmente. Caso não funcione contigo, por favor,
#  tente pesquisar um pouco mais a fundo sobre como fazer as chaves SSH
# funcionarem corretamente no Windows.
