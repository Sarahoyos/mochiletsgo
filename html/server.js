const express = require('express');
const path = require('path');
const PORT = process.env.PORT || 5000;

express()
  .use(express.static(path.join(__dirname, '../../dist/apps/desplegue_pagina')))
  .get('*', (_, res) => {
    res.sendFile('SignUpAD.html', {
      root: path.join(__dirname, '../../dist/apps/desplegue_pagin'),
    });
  })
  .listen(PORT, () => console.log(`Listening on ${PORT}`));
