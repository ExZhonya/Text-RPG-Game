import shutil
from preset import cutscenes as cs
from preset import utils as u
from preset import saves

def welc_asc():
	u.clear()
	print(r"""
			,-.-.     ,----.              _,.----.     _,.---._           ___      ,----.  
	,-..-.-./  \==\ ,-.--` , \   _.-.    .' .' -   \  ,-.' , -  `.  .-._ .'=.'\  ,-.--` , \ 
	|, \=/\=|- |==||==|-  _.-` .-,.'|   /==/  ,  ,-' /==/_,  ,  - \/==/ \|==|  ||==|-  _.-` 
	|- |/ |/ , /==/|==|   `.-.|==|, |   |==|-   |  .|==|   .=.     |==|,|  / - ||==|   `.-. 
	\, ,     _|==/==/_ ,    /|==|- |   |==|_   `-' \==|_ : ;=:  - |==|  \/  , /==/_ ,    / 
	| -  -  , |==|==|    .-' |==|, |   |==|   _  , |==| , '='     |==|- ,   _ |==|    .-'  
	\  ,  - /==/|==|_  ,`-._|==|- `-._\==\.       /\==\ -    ,_ /|==| _ /\   |==|_  ,`-._ 
	|-  /\ /==/ /==/ ,     //==/ - , ,/`-.`.___.-'  '.='. -   .' /==/  / / , /==/ ,     / 
	`--`  `--`  `--`-----`` `--`-----'                `--`--''   `--`./  `--``--`-----``  
																					v0.0.2-unstable_v2
""")

def _options(width):
	u.v_fast_print(f"{'Please Choose One of The Options.':^{width}}")
	u.v_fast_print(f"{'1. START':^{width}}")
	u.v_fast_print(f"{'2. LOAD ':^{width}}")
	u.v_fast_print(f"{'3. QUIT ':^{width}}")

def welc_text():
	width = shutil.get_terminal_size().columns

	u.fast_print(f"{'Welcome to the amazing digital world!':^{width}}")
	u.fast_print(f"{'You will live as a stranded person in a camp alone... for now!':^{width}}")
	u.fast_print("")
	_options(width)

	while True:
		x = u.getch()

		if x == "1":
			cs.start()
			return True
		elif x == "2":
			if saves.slot_menu("load"):
				return True
			welc_asc()
			_options(width)
		elif x == "3":
			return False



def bye_asc():
	u.clear()
	print(r"""
        ,----,                                                              
      ,/   .`|       ,--,                        ,--.       ,--.            
    ,`   .'  :     ,--.'|   ,---,              ,--.'|   ,--/  /| .--.--.    
  ;    ;     /  ,--,  | :  '  .' \         ,--,:  : |,---,': / '/  /    '.  
.'___,/    ,',---.'|  : ' /  ;    '.    ,`--.'`|  ' ::   : '/ /|  :  /`. /  
|    :     | |   | : _' |:  :       \   |   :  :  | ||   '   , ;  |  |--`   
;    |.';  ; :   : |.'  |:  |   /\   \  :   |   \ | :'   |  /  |  :  ;_     
`----'  |  | |   ' '  ; :|  :  ' ;.   : |   : '  '; ||   ;  ;   \  \    `.  
    '   :  ; '   |  .'. ||  |  ;/  \   \'   ' ;.    ;:   '   \   `----.   \ 
    |   |  ' |   | :  | ''  :  | \  \ ,'|   | | \   ||   |    '  __ \  \  | 
    '   :  | '   : |  : ;|  |  '  '--'  '   : |  ; .''   : |.  \/  /`--'  / 
    ;   |.'  |   | '  ,/ |  :  :        |   | '`--'  |   | '_\.'--'.     /  
    '---'    ;   : ;--'  |  | ,'        '   : |      '   : |     `--'---'   
             |   ,/      `--''          ;   |.'      ;   |,'                
             '---'                      '---'        '---'                  
""")

def bye_text():
	width = shutil.get_terminal_size().columns
	u.slow_print(f"{'Thank You for playing my game!':^{width}}")
	u.slow_print(f"{'Your Playtime is very much appreciated!':^{width}}")
	u.slow_print(f"{'See you next time, player!':^{width}}")


#	slow_print(f"{'':^{width}}")
# 	fast_print(f"{'':^{width}}")

if __name__ == "__main__":
	bye_asc()
	bye_text()