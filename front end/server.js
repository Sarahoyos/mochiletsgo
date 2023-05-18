const express = require('express');
const path = require('path');
const PORT = process.env.PORT || 5800;

express()
  .use(express.static(path.join(__dirname, '../../dist/apps/homepage')))
  .get('*', (_, res) => {
    res.sendFile('SignUpAD.html', {
      root: path.join(__dirname, '../../dist/apps/homepage'),
    });
  })
  .listen(PORT, () => console.log(`Listening on ${PORT}`));
