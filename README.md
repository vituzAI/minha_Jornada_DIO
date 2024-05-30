# DIO | Resumos Git e GitHub

Repósitorio Para Armazenar Resumos Sobre Git e GitHub do Curso de Versionamento de Código de Git e GitHub.

[Digital Innovation One](https://www.dio.me/)

## 📚 Documentação 

- [Documentação Git](https://git-scm.com/doc)
- [Documentação GitHub](https://docs.github.com/pt)


## 💻 Resumos Das Aulas 

# O que é Git?
Git é um sistema de controle de versão distribuído criado por Linus Torvalds em 2005. Ele permite que múltiplos desenvolvedores trabalhem em um projeto ao mesmo tempo sem sobrescrever o trabalho uns dos outros. Git é amplamente utilizado em desenvolvimento de software para rastrear mudanças no código-fonte ao longo do tempo.

## ⚙ Fluxo de Trabalho Básico do Git:
```
Clone: Clonar um repositório remoto para um repositório local.
git clone https://github.com/usuario/repositorio.git
```
```
Branch: Criar uma nova branch para desenvolver uma funcionalidade.
git checkout -b nova-funcionalidade
```
```
Commit: Fazer commit das mudanças.
git add .
git commit -m "Implementa nova funcionalidade"
```
```
Push: Enviar as mudanças para o repositório remoto.
git push origin nova-funcionalidade
```
```
Merge: Mesclar a branch com a branch principal (geralmente main ou master).
git checkout main
git merge nova-funcionalidade
```
# O que é GitHub?
GitHub é uma plataforma de hospedagem de código-fonte com controle de versão usando Git. Ele fornece uma interface gráfica para gerenciar repositórios Git, além de diversas funcionalidades adicionais, como:

- Pull Requests: Permite que desenvolvedores revisem e discutam mudanças propostas antes de integrá-las ao projeto principal.
- Issues: Sistema de gerenciamento de tarefas e bugs.
- Actions: Automatização de fluxos de trabalho, como testes e deploy.
- Wikis e Documentação: Facilita a criação e manutenção de documentação.
- Comunidade e Colaboração: Facilita a colaboração com outros desenvolvedores e contribuições de código aberto.

## 💾 Integração entre Git e GitHub:
- Criar um repositório no GitHub: Pode ser feito diretamente na interface web.
- Clonar o repositório: Para trabalhar localmente, use o comando `git clone`.
- Adicionar o repositório remoto: Se o repositório já existe localmente.
`git remote add origin https://github.com/usuario/repositorio.git`
- Push e Pull: Para sincronizar as mudanças entre o repositório local e o remoto.

## Benefícios do Git e GitHub:
- Colaboração: Vários desenvolvedores podem trabalhar simultaneamente.
- Histórico de mudanças: Fácil rastreamento de alterações e reverter para versões anteriores.
- Revisão de código: Facilita a identificação de bugs e melhoria de código através de revisões.
- Automatização: GitHub Actions permite automatizar testes e deploys.

**Git e GitHub são ferramentas essenciais para o desenvolvimento moderno de software, proporcionando um ambiente robusto para colaboração e controle de versão.**

## 🔎 REFÊRENCIAS
[Digital Innovation One](https://www.dio.me/) Versionamento de Código com Git e GitHub
