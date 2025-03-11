# Backend 

## Arquitetura de software e padrões de projetos
Arquitetura de software é relacionada estrutura do sistema.
- Decisões de alto nivel
- Distribuição de responsabilidades 
- Comunicação entre componentes

Padrões de projeto é relacionado a soluções reutilizáveis para problemas recorrentes
- Níveis mais baixos de design
- Soluções/problemas específicos
- Detalhes da implementação de classes e objetos
- Boas práticas de design comprovadas ao longo do tempo

## Camada física (tier) x Camada lógica (layer)
Camada física (tier) 
- Infraestrutura separada
- Implementação concreta do sistema
- Infraestrutura real que suporta a execução da aplicação

Camada lógica (layer)
- Estrutura do sistema com base em uma perspectiva funcional e conceitual
- Lógica de negócios, serviços, funcionalidades

## Padrões
Arquiteturais 
- Organização global
- Divisão de responsabilidades 
- Comunicação entre componentes
- Exemplo: MVC

Estruturais
- Organização de classes e objetos
- Como as partes individuais se relacionam 
- Mais relacionado à codificação
- Exemplo: Composite

Comportamentais
- Padrões de interação e responsabilidades entre objetos
- Exemplo: Strategy e Observer


## Arquitetura Java EE (Enterprise Edition)
- 4 camadas lógicas: cliente, web, negócios e sistema de informação corporativa
- Considerada aplicação de 3 camadas (físicas): máquina do cliente, java EE server, database server 
