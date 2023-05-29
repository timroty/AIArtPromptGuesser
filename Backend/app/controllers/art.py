from ..supabase import Supabase
from ..models.db_models.art import Art
from thefuzz import fuzz

class ArtHandler:
    def __init__(self):
        self.supabase = Supabase()

    def get_random_art_piece(self):
        response = self.supabase.client.from_("random_art_piece").select('*').limit(1).single().execute()
        art = Art.from_json(response.data)

        return art
    
    def guess_art_prompt(self, art_id: int, guess: str):
        guess = guess.strip()
        response = self.supabase.client.table("Art").select("*").eq('id', art_id).single().execute()
        art: Art = Art.from_json(response.data)
        ratio_result: int = fuzz.ratio(guess, art.prompt)
        partial_ratio_result: int = fuzz.partial_ratio(guess, art.prompt)
        token_sort_ratio: int = fuzz.token_sort_ratio(guess, art.prompt)
        token_set_ratio: int = fuzz.token_set_ratio(guess, art.prompt)

        score: float = (ratio_result * .1 + partial_ratio_result * .2 + token_sort_ratio * .3 + token_set_ratio * .4)

        return score
