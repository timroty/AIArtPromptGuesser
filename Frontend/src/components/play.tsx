import React from 'react';
import { useState, useEffect } from 'react';
import { GetRandomImage, GuessImage } from '../services/accessor'
import { Image } from '../models/Image'
import { TextField, Button } from '@mui/material';
import { useRouter } from 'next/router';

const copy = require('clipboard-copy');

interface PlayComponentProps {
  promptId: string | undefined;
}

interface Guess {
  text: string;
  score: number;
}

const PlayComponent: React.FC<PlayComponentProps> = ({ promptId }) => {
  let [guessingImage, setGuessingImage] = useState<Image | null>(null);
  let [currentGuess, setCurrentGuess] = useState<string>("");
  let [previousGuesses, setPreviousGuesses] = useState<Guess[]>([]);
  let [guessCount, setGuessCount] = useState<number>(0);
  let [highScore, setHighScore] = useState<number>(0);
  let [roundEnd, setRoundEnd] = useState<boolean>(false);

  const maxGuesses = 10;
  const router = useRouter();

  useEffect(() => {
    if (!promptId){
      (async () => {
        var randomImage = await GetRandomImage();
        setGuessingImage(randomImage);
      })();
    }
  }, []);

  const handleGuessTextChange = (e) => { 
    setCurrentGuess(e.target.value);
  }

  const handlePromptGuess = () => { 
    (async () => {
      var score = await GuessImage(guessingImage?.id ?? -1, currentGuess)

      const guess: Guess = {
        text: currentGuess,
        score: score,
      };

      setGuessCount(++ guessCount);
      setPreviousGuesses((previousGuesses) => [...previousGuesses, guess]);
      if (score > highScore){
        setHighScore(score);
      }
      if (score == 100 || guessCount + 1 >= maxGuesses){
        setRoundEnd(true);
      }
    })();
  }

  const handlePlayAgain = () => { 
    if (router.pathname == '/play'){
     router.reload();
    } else {
     router.push('/play');
    }
   }

  let shareText = 'I got a high score of ' + highScore + ' in ' + guessCount + 
      ' guesses on Ai Art Prompt Guesser. Can you beat my score? ' + 
      process.env.NEXT_PUBLIC_BACKEND_BASE_URL + 'play/' + guessingImage?.id;

  

  return (
    <div>
      { guessingImage != null ? (
        <>
        <div>
          <div>
            <img src={guessingImage.reference_url} alt="Guessing Image" />
          </div>
          { !roundEnd ? (
            <>
              <TextField value={currentGuess} label="Search"
              onChange={ (e) => handleGuessTextChange(e)}
              onKeyUp={ (e) => { if (e.key === 'Enter') {handlePromptGuess()} } } 
              />
              <Button variant="outlined" onClick={handlePromptGuess}>
                Guess
              </Button>
            </>
          ) : ( 
          <>
            {highScore == 100 ? (
              <div>
              You win! 
              </div>
            ) : (
              <>
                <div>
                You ran out of guesses! 
                </div>
                <div>
                The prompt was TODO
                </div>
              </>
            )}
            
              <div>
                <Button
                  onClick={() => {
                    copy(shareText);
                  }}
                  >
                  Share
                </Button> 
                <Button
                  onClick={() => {
                    handlePlayAgain()
                  }}
                  >
                  Play again
                </Button> 
              </div>
          </>
          )}
         
        </div>
        {previousGuesses.map((guess, index) => {
            return (
              <div key={index}>
                {index}. {guess.text} : {guess.score}
              </div>
            );
          })}
        </>
        
      ) : ( <> </>)}
    </div>
  );
};

export default PlayComponent;