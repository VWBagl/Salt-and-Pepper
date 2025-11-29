class WrongNumberOfPlayersError(Exception):
    pass 
class NoSuchStrategyError(Exception):
    pass

def rps_game_winner(players):
    try:
        if len(players) != 2:
            raise WrongNumberOfPlayersError ('goyda')

        player_1, move_1 = players[0]
        player_2, move_2 = players[1]
        valid_moves = {'R', 'P', 'S'}

        if move_1 not in valid_moves or move_2 not in valid_moves:
            raise NoSuchStrategyError

        if move_1 == move_2:
            return f'{player_1} {move_1}'
        
        rules = {'R':'S','S':'P','P':'R'}
        if rules[move_1] == move_2:
            return f'{player_1} {move_1}'
        else: 
            return f'{player_2} {move_2}'
            
    except WrongNumberOfPlayersError:
        return 'WrongNumberOfPlayersError'
    except NoSuchStrategyError:
        return 'NoSuchStrategyError'