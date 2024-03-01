import React from 'react';
import styled from 'styled-components';

const StyledInput = styled.input`
  width: 90%;
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 5px;
`;

const Input = ({ label, ...rest }) => (
  <div>
    <label htmlFor={rest.id}>{label}</label>
    <StyledInput {...rest} />
  </div>
);

export default Input;
