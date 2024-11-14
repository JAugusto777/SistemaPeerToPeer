# Sistema de Compartilhamento de Arquivos P2P
Este projeto é um sistema de compartilhamento de arquivos ponto a ponto (P2P) desenvolvido para explorar e aplicar habilidades em Python, Flask, Socket.IO, Tkinter, e arquitetura cliente-servidor. O objetivo é oferecer uma experiência prática e educativa de construção de uma rede de compartilhamento de arquivos semelhante ao BitTorrent, com interface gráfica para o usuário.
Funcionalidades - 
  Registro de Usuário: Registra novos usuários com um identificador exclusivo no sistema, permitindo que compartilhem arquivos.
  Compartilhamento de Arquivos: Permite o upload de arquivos para o servidor, que serão disponibilizados a outros usuários conectados.
  Listagem de Arquivos: Exibe arquivos disponíveis no sistema, com informações sobre quem compartilhou cada arquivo.
  Download de Arquivos: Permite o download de arquivos compartilhados por outros usuários, com salvamento automático em uma pasta designada.
  Atualização Dinâmica: Utiliza Socket.IO para manter usuários sincronizados e gerenciar eventos de conexão e desconexão.
-Tecnologias e Habilidades Desenvolvidas
  Backend
    Flask: Criação de um servidor HTTP para gerenciar registros de usuários e endpoints para upload, listagem e download de arquivos.
    Socket.IO: Gerenciamento de conexões em tempo real para atualizações e interações entre clientes e servidor.
    Gerenciamento de Arquivos: Leitura, escrita e organização de arquivos usando bibliotecas padrão do Python.
    Armazenamento de Dados com JSON: Persistência dos dados dos arquivos compartilhados e usuários registrados em formato JSON.
Frontend (Interface do Cliente)

  Tkinter: Desenvolvimento de uma interface gráfica para facilitar a interação do usuário com o sistema.
  
  Interface Intuitiva: Criação de uma interface que permite o registro de usuários, compartilhamento e download de arquivos de forma simplificada.
  Gerenciamento de Diretórios e Arquivos: Automatização do salvamento de arquivos em diretórios específicos, com criação dinâmica de pastas.
  Arquitetura de Software e Redes
  Arquitetura Cliente-Servidor: Implementação de uma comunicação estruturada entre cliente e servidor, com troca de dados via HTTP e WebSocket.
  P2P Básico: Estrutura de compartilhamento de arquivos que distribui o conteúdo de forma descentralizada.
  Tratamento de Erros e Conexão: Validação e tratamento de erros de conexão com o servidor e operações de upload/download.
Como Executar
Clone o repositório e instale as dependências.
Inicie o servidor Flask com Socket.IO:
bash
Copiar código
python server.py


Execute o cliente com Tkinter:
bash
Copiar código
python client.py


Registre-se e comece a compartilhar e baixar arquivos.
Possibilidades de Expansão
Este projeto pode ser expandido para incluir:
Autenticação de usuários.
Criptografia de arquivos durante o upload e download.
Distribuição de arquivos entre vários peers para maior resiliência.
Habilidades e Competências Desenvolvidas
Programação em Python com foco em sistemas de rede e arquitetura cliente-servidor.
Manipulação de arquivos e organização de diretórios.
Criação de interfaces gráficas com Tkinter e design orientado ao usuário.
Comunicação em tempo real e sincronização entre múltiplos clientes via WebSocket.

