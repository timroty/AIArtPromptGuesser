import React from 'react';

interface PlayComponentProps {
  promptId: string | undefined;
}

const PlayComponent: React.FC<PlayComponentProps> = ({ promptId }) => {
  console.log(promptId)
  return (
    <div>
      
      <h2>Play Value</h2>
      {promptId ? <p>Value: {promptId}</p> : <p>No value specified</p>}
    </div>
  );
};

export default PlayComponent;