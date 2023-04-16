import React from 'react';
import './App.css';
import Board from './components/Board';
import Options from './components/Options';
import { Box, Stack } from '@mui/material';

function App() {
  return (
    <div className="App">
      <Stack direction="row" spacing={2} >
        <h1 className="title">8-Puzzle</h1>
        <Board />
        <Box>
          <Options />
        </Box>
      </Stack>
      
    </div>
  );
}

export default App;
