# Databricks_ci_cd















### CAPA GOLDEN

### Nuevas columnas agregadas

- **gross_sale**:  
  Representa la venta bruta por transacción. Se calcula como el producto del precio unitario (`Price`) por la cantidad de unidades vendidas (`Units_Sold`). El valor es truncado a 2 decimales para mantener la precisión financiera.

  Fórmula:  
  `gross_sale = trunc((Price * Units_Sold), 2)`

- **total_sales**:  
  Representa la venta neta por transacción. Se calcula restando el descuento aplicado (`Discount`) al valor de la venta bruta. El resultado también es truncado a 2 decimales.

  Fórmula:  
  `total_sales = trunc((Price * Units_Sold) - Discount, 2)`
