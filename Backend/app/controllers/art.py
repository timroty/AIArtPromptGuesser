from ..supabase import Supabase
from ..models.db_models.art import Art as ArtModel
from thefuzz import fuzz

class Art:
    def __init__(self):
        self.supabase = Supabase()

    def get_random_art_piece(self):
        response = self.supabase.client.from_("random_art_piece").select('*').limit(1).single().execute()
        art: ArtModel = ArtModel.from_json(response.data)

        return art
    
    def get_art_piece_by_id(self, art_id: int):
        response = self.supabase.client.table("Art").select("*").eq('id', art_id).execute() 
        if len(response.data) == 0:
            return None
        art: ArtModel = ArtModel.from_json(response.data[0])

        return art
    
    def guess_art_prompt(self, art_id: int, guess: str):
        guess = guess.strip().lower()
        response = self.supabase.client.table("Art").select("*").eq('id', art_id).single().execute()
        art: ArtModel = ArtModel.from_json(response.data)
        art.prompt = art.prompt.lower()
        ratio_result: int = fuzz.ratio(guess, art.prompt)
        partial_ratio_result: int = fuzz.partial_ratio(guess, art.prompt)
        token_sort_ratio: int = fuzz.token_sort_ratio(guess, art.prompt)
        token_set_ratio: int = fuzz.token_set_ratio(guess, art.prompt)

        score: float = (ratio_result * .1 + partial_ratio_result * .2 + token_sort_ratio * .3 + token_set_ratio * .4)

        return score
