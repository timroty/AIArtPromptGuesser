import axios from 'axios';
import { Image } from '../models/Image'

export async function GetRandomImage() {
  let config = {
    method: 'get',
    url: process.env.NEXT_PUBLIC_BACKEND_BASE_URL + '/api/image',
  };
  
  let response = (await axios(config)).data;

  return response as Image;
}

export async function GuessImage(photoId : number, guessText : string) {
  let config = {
    method: 'post',
    url: process.env.NEXT_PUBLIC_BACKEND_BASE_URL + 'api/image/guess',
    headers: { 
      'Content-Type': 'application/json'
    },
    data: {
      id: photoId,
      guess: guessText
    }
  };
  
  let response = (await axios(config)).data;

  return response as number;
}