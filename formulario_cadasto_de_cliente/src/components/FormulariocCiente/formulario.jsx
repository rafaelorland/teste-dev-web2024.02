import React, { useState } from 'react';

import { FormularioWrapper } from './FormularioWrapper';
import Input from './input';
import Select from './select';
import Button from './button';


function FormularioCadastroCliente() {
  const [cliente, setCliente] = useState({
    nome: '',
    cpf: '',
    email: '',
    telefone: '',
    sexo: '',
    nascimento: ''
  });

  const handleSubmit = (event) => {
    event.preventDefault();

    for (const campo in cliente) {
      if (!cliente[campo]) {
        console.log('Por favor, preencha todos os campos do formulário.');
        return;
      }
    }

    console.log('Dados do cliente:', JSON.stringify(cliente));

    setCliente({
      nome: '',
      cpf: '',
      email: '',
      telefone: '',
      sexo: '',
      nascimento: ''
    });
  };

  const handleChange = (event) => {
    const { name, value } = event.target;
    setCliente({ ...cliente, [name]: value });
  };

  return (
    <FormularioWrapper onSubmit={handleSubmit}>
      <Input
        label="Nome:"
        id="nome"
        name="nome"
        value={cliente.nome}
        onChange={handleChange}
        required
      />
      <Input
        label="CPF:"
        id="cpf"
        name="cpf"
        value={cliente.cpf}
        onChange={handleChange}
        required
      />
      <Input
        label="Email:"
        type="email"
        id="email"
        name="email"
        value={cliente.email}
        onChange={handleChange}
        required
      />
      <Input
        label="Telefone:"
        id="telefone"
        name="telefone"
        value={cliente.telefone}
        onChange={handleChange}
        required
      />
      <Select
        label="Sexo:"
        id="sexo"
        name="sexo"
        value={cliente.sexo}
        onChange={handleChange}
        required
      >
        <option value="">Selecione</option>
        <option value="Masculino">Masculino</option>
        <option value="Feminino">Feminino</option>
        <option value="Outro">Outro</option>
      </Select>
      <Input
        label="Data de Nascimento:"
        type="date"
        id="nascimento"
        name="nascimento"
        value={cliente.nascimento}
        onChange={handleChange}
        required
      />
      <Button type="submit">Cadastrar</Button>
    </FormularioWrapper>
  );
}

export default FormularioCadastroCliente;
