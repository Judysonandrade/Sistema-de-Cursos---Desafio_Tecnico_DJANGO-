-- 1. Criação das Tabelas (Representação do Modelo)

CREATE TABLE core_aluno (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(254) NOT NULL UNIQUE,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    data_ingresso DATE NOT NULL
);

CREATE TABLE core_curso (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    carga_horaria INTEGER NOT NULL,
    valor_inscricao NUMERIC(10, 2) NOT NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE core_matricula (
    id SERIAL PRIMARY KEY,
    aluno_id INTEGER NOT NULL REFERENCES core_aluno(id),
    curso_id INTEGER NOT NULL REFERENCES core_curso(id),
    data_matricula TIMESTAMP WITH TIME ZONE NOT NULL,
    status VARCHAR(10) NOT NULL CHECK (status IN ('PAGO', 'PENDENTE'))
);

-- 2. Consulta SQL Bruta (Utilizada no Relatório/Dashboard)
-- Objetivo: Listar cursos, quantidade de matrículas pagas e total arrecadado, ordenado por receita.

SELECT 
    C.nome AS nome_do_curso, 
    COUNT(M.id) AS qtd_matriculas, 
    SUM(C.valor_inscricao) AS total_gerado
FROM 
    core_curso C
JOIN 
    core_matricula M ON C.id = M.curso_id
WHERE 
    M.status = 'PAGO'
GROUP BY 
    C.nome
ORDER BY 
    total_gerado DESC;