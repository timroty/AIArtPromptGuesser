export interface Image {
  id: number;
  reference_url: string;
}

export interface ArtPiece {
  id: number;
  reference_url: string;
  prompt: string;
  model: string;
}