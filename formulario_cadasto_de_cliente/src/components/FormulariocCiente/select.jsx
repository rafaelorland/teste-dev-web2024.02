import React from 'react';
import styled from 'styled-components';

const StyledSelect = styled.select`
  width: 90%;
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 5px;
`;

const Select = ({ label, children, ...rest }) => (
  <div>
    <label htmlFor={rest.id}>{label}</label>
    <StyledSelect {...rest}>
      {children}
    </StyledSelect>
  </div>
);

export default Select;
