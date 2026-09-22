# Ficha de Avaliação de RPA - Matriz de Viabilidade

## 1. Informações do Processo

- **Nome do Processo:** Conciliação Bancária Diária
- **Cenário Escolhido:** Cenário A
- **Área/Departamento:** Financeiro / Tesouraria

## 2. Características do Processo

- **Gatilho (Trigger):** Disponibilidade diária do extrato bancário.
- **Sistemas Envolvidos:** Portal/Aplicativo do Banco e Sistema ERP.
- **Entradas (Inputs):** Arquivo de extrato bancário em formato `.csv`.
- **Saídas (Outputs):** Baixas processadas no ERP e relatório de exceções (linhas não conciliadas).

## 3. Critérios de Elegibilidade para RPA

| Critério                      | Avaliação | Justificativa                                                                                                               |
| ----------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Dados Estruturados**        | Sim       | Os dados de entrada vêm em um formato tabular padrão (`.csv`) com colunas pré-definidas.                                    |
| **Regras Baseadas em Lógica** | Sim       | A automação pode seguir regras fixas (se CNPJ e Valor do arquivo CSV forem idênticos à pendência no ERP, executar a baixa). |
| **Estabilidade do Processo**  | Sim       | A conciliação por CNPJ/Valor é um procedimento contábil padronizado, sem mudanças sistêmicas frequentes.                    |
| **Subjetividade**             | Não       | Não há necessidade de interpretação humana, empatia ou julgamento cognitivo complexo na etapa de cruzamento de dados.       |

## 4. Conclusão de Viabilidade

**Veredito:** 🟢 ALTA VIABILIDADE PARA RPA

**Justificativa:**
O processo é previsível, repetitivo e governado por regras de negócio rígidas e documentadas. A automação deste cenário reduzirá trabalhos manuais de "copiar e colar" e diminuirá a incidência de erros de digitação humanos, liberando os analistas para atuar apenas nas exceções (pagamentos que não deram _match_ automático).
